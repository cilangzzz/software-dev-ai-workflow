"""
上下文管理器 - 实现 Compaction 和 Reset 策略

基于 Anthropic 的 Harness 架构实现:
1. Compaction: 压缩旧消息，保留最近消息（同一会话内）
   - 保持连续性但无法提供全新的开始
2. Reset: 将结构化检查点写入文件，启动全新消息列表
   - 解决"上下文焦虑" - 模型获得全新窗口，不再过早收尾

参考: Anthropic "Harness design for long-running application development"
"""
from __future__ import annotations

import re
import logging
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass
from datetime import datetime
import subprocess
from pathlib import Path

try:
    import tiktoken
    HAS_TIKTOKEN = True
except ImportError:
    HAS_TIKTOKEN = False

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Token 计数
# ---------------------------------------------------------------------------

_encoder = None


def _get_encoder():
    """获取 tokenizer 编码器"""
    global _encoder
    if _encoder is None:
        if HAS_TIKTOKEN:
            try:
                _encoder = tiktoken.get_encoding("cl100k_base")
            except Exception:
                _encoder = None
    return _encoder


def count_tokens(messages: List[Dict]) -> int:
    """
    计算消息列表的 token 数量

    Args:
        messages: 消息列表

    Returns:
        int: token 数量估计值
    """
    encoder = _get_encoder()

    if encoder is None:
        # 回退到简单估计：每4个字符约1个token
        total = 0
        for msg in messages:
            content = msg.get("content", "")
            if isinstance(content, str):
                total += len(content) // 4
            elif isinstance(content, list):
                for part in content:
                    if isinstance(part, dict) and "text" in part:
                        total += len(part["text"]) // 4
        return total

    total = 0
    for msg in messages:
        content = msg.get("content") or ""
        if isinstance(content, str):
            total += len(encoder.encode(content))
        elif isinstance(content, list):
            for block in content:
                if isinstance(block, dict) and "text" in block:
                    total += len(encoder.encode(block["text"]))

        # 计算工具调用的 tokens
        for tc in msg.get("tool_calls", []):
            fn = tc.get("function", {})
            args = fn.get("arguments", "")
            if isinstance(args, str):
                total += len(encoder.encode(args))

        # 每条消息的额外开销
        total += 4

    return total


# ---------------------------------------------------------------------------
# 上下文焦虑检测
# ---------------------------------------------------------------------------

# 模型尝试过早收尾的模式
ANXIETY_PATTERNS = [
    r"(?i)let me wrap up",
    r"(?i)running (low on|out of) (context|space|tokens)",
    r"(?i)that should be (enough|sufficient)",
    r"(?i)I'll just",
    r"(?i)I think I've covered",
    r"(?i)quickly summarize",
    r"(?i)due to (context |token )?limit",
    r"(?i)to (save|conserve) (context|space|tokens)",
    r"(?i)in the interest of (time|space|brevity)",
    r"(?i)i('ll| will) finalize",
    r"(?i)i('ll| will) stop here",
    r"(?i)i('ve| have) covered the (main|key|essential)",
]


def detect_anxiety(messages: List[Dict]) -> bool:
    """
    检测上下文焦虑信号 - 模型因认为上下文空间不足而试图过早收尾

    Args:
        messages: 消息列表

    Returns:
        bool: 是否检测到焦虑信号
    """
    if not messages:
        return False

    # 只检查最近的几条 assistant 消息
    recent_texts = []
    for msg in reversed(messages[-10:]):
        if msg.get("role") == "assistant" and msg.get("content"):
            recent_texts.append(msg["content"])
        if len(recent_texts) >= 3:
            break

    combined = " ".join(recent_texts)
    matches = sum(1 for p in ANXIETY_PATTERNS if re.search(p, combined))

    if matches >= 2:
        logger.warning(f"Context anxiety detected ({matches} signals found)")
        return True

    return False


# ---------------------------------------------------------------------------
# 检查点
# ---------------------------------------------------------------------------

@dataclass
class Checkpoint:
    """上下文检查点"""
    id: str
    messages_summary: str
    token_count: int
    phase: str
    created_at: str
    file_path: Optional[str] = None


# ---------------------------------------------------------------------------
# 上下文管理器
# ---------------------------------------------------------------------------

class ContextManager:
    """上下文生命周期管理"""

    def __init__(
        self,
        workspace_path: str = ".",
        compaction_threshold: int = 80000,
        reset_threshold: int = 150000,
        retention_ratio: float = 0.3
    ):
        """
        初始化上下文管理器

        Args:
            workspace_path: 工作区路径
            compaction_threshold: 压缩阈值（tokens）
            reset_threshold: 重置阈值（tokens）
            retention_ratio: 保留比例（压缩时保留的消息比例）
        """
        self.workspace_path = Path(workspace_path)
        self.compaction_threshold = compaction_threshold
        self.reset_threshold = reset_threshold
        self.retention_ratio = retention_ratio

        self.checkpoints: List[Checkpoint] = []
        self.progress_file = self.workspace_path / "progress.md"

    def should_compact(self, messages: List[Dict]) -> bool:
        """
        判断是否需要压缩

        Args:
            messages: 消息列表

        Returns:
            bool: 是否需要压缩
        """
        token_count = count_tokens(messages)
        return token_count > self.compaction_threshold

    def should_reset(self, messages: List[Dict]) -> bool:
        """
        判断是否需要重置

        Args:
            messages: 消息列表

        Returns:
            bool: 是否需要重置
        """
        token_count = count_tokens(messages)
        anxiety_detected = detect_anxiety(messages)
        return token_count > self.reset_threshold or anxiety_detected

    def compact_messages(
        self,
        messages: List[Dict],
        llm_call: Optional[Callable] = None,
        role: str = "default"
    ) -> List[Dict]:
        """
        压缩消息列表

        Args:
            messages: 原始消息列表
            llm_call: LLM调用函数（用于生成摘要）
            role: 角色类型（决定保留比例）

        Returns:
            List[Dict]: 压缩后的消息列表
        """
        if not messages:
            return messages

        # 根据角色确定保留比例
        retention_map = {
            "planner": 0.50,
            "evaluator": 0.50,
            "builder": 0.20,
            "default": 0.30
        }
        ratio = retention_map.get(role, self.retention_ratio)

        # 分离系统消息
        system_msgs = [m for m in messages if m.get("role") == "system"]
        non_system_msgs = [m for m in messages if m.get("role") != "system"]

        # 保留最近的 N% 消息
        keep_count = max(4, int(len(non_system_msgs) * ratio))
        old_messages = non_system_msgs[:-keep_count]
        recent_messages = non_system_msgs[-keep_count:]

        if not old_messages:
            return messages

        # 对早期消息生成摘要
        summary = self._generate_summary(old_messages, llm_call, role)
        summary_msg = {
            "role": "user",
            "content": f"[COMPACTED CONTEXT - summary of earlier work]\n{summary}"
        }

        logger.info(
            f"Compacted context: {len(old_messages)} old messages -> 1 summary, "
            f"{len(recent_messages)} recent messages retained"
        )

        return system_msgs + [summary_msg] + recent_messages

    def create_checkpoint(
        self,
        messages: List[Dict],
        phase: str,
        llm_call: Optional[Callable] = None
    ) -> Checkpoint:
        """
        创建检查点

        Args:
            messages: 消息列表
            phase: 当前阶段
            llm_call: LLM调用函数

        Returns:
            Checkpoint: 创建的检查点
        """
        import uuid

        checkpoint = Checkpoint(
            id=str(uuid.uuid4())[:8],
            messages_summary=self._generate_checkpoint_summary(messages, llm_call),
            token_count=count_tokens(messages),
            phase=phase,
            created_at=datetime.now().isoformat()
        )

        self.checkpoints.append(checkpoint)

        # 持久化到文件
        self._persist_checkpoint(checkpoint)

        logger.info(f"Created checkpoint: {checkpoint.id} at phase {phase}")
        return checkpoint

    def restore_from_checkpoint(
        self,
        checkpoint: Checkpoint,
        system_prompt: str
    ) -> List[Dict]:
        """
        从检查点恢复

        Args:
            checkpoint: 检查点对象
            system_prompt: 系统提示

        Returns:
            List[Dict]: 恢复后的消息列表
        """
        # 获取最近的代码变更作为额外上下文
        git_context = self._get_git_context()

        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": (
                "You are resuming an in-progress project. Your previous session's "
                "context was reset to give you a clean slate.\n\n"
                "Here is the handoff document from the previous session:\n\n"
                + checkpoint.messages_summary
                + git_context
                + "\n\nContinue from where the previous session left off. "
                "Do NOT redo work that's already completed."
            )}
        ]

    def _generate_summary(
        self,
        messages: List[Dict],
        llm_call: Optional[Callable],
        role: str = "default"
    ) -> str:
        """
        生成消息摘要

        Args:
            messages: 消息列表
            llm_call: LLM调用函数
            role: 角色类型

        Returns:
            str: 摘要文本
        """
        if not llm_call:
            return self._simple_summary(messages)

        # 角色特定的摘要指令
        role_instructions = {
            "evaluator": (
                "Summarize the following QA work log. Preserve: all scores given, "
                "bugs found, quality assessments, and cross-round comparisons. "
                "The evaluator needs this history to track improvement trends."
            ),
            "builder": (
                "Summarize the following build log. Preserve: files created/modified, "
                "current architecture decisions, and the latest error states. "
                "Discard intermediate debugging steps and superseded code."
            ),
            "planner": (
                "Summarize the following planning log. Preserve: key decisions, "
                "requirements, constraints, and stakeholder feedback."
            ),
            "default": (
                "Summarize the following agent work log. Preserve: key decisions, "
                "files created/modified, current progress, and errors encountered."
            )
        }

        instruction = role_instructions.get(role, role_instructions["default"])
        text = self._messages_to_text(messages)

        try:
            summary = llm_call([
                {"role": "system", "content": f"You are a concise summarizer. {instruction}"},
                {"role": "user", "content": text}
            ])
            return summary
        except Exception as e:
            logger.error(f"Failed to generate summary: {e}")
            return self._simple_summary(messages)

    def _generate_checkpoint_summary(
        self,
        messages: List[Dict],
        llm_call: Optional[Callable]
    ) -> str:
        """
        生成检查点摘要（用于重置）

        Args:
            messages: 消息列表
            llm_call: LLM调用函数

        Returns:
            str: 检查点摘要
        """
        if not llm_call:
            return self._simple_summary(messages)

        text = self._messages_to_text(messages)

        try:
            checkpoint = llm_call([
                {"role": "system", "content": (
                    "You are creating a handoff document for the next agent session. "
                    "The next session starts with a COMPLETELY EMPTY context window - "
                    "it has zero memory of anything that happened here.\n\n"
                    "Structure the handoff as:\n"
                    "## Completed Work\n(what was built, with file paths)\n"
                    "## Current State\n(what works, what's broken right now)\n"
                    "## Next Steps\n(exactly what to do next, in order)\n"
                    "## Key Decisions & Rationale\n(why things were done this way)\n"
                    "## Known Issues\n(bugs, incomplete features, technical debt)\n\n"
                    "Be thorough and specific - file paths, function names, error messages. "
                    "The next session's success depends entirely on this document."
                )},
                {"role": "user", "content": text}
            ])
            return checkpoint
        except Exception as e:
            logger.error(f"Failed to generate checkpoint summary: {e}")
            return self._simple_summary(messages)

    def _simple_summary(self, messages: List[Dict]) -> str:
        """
        简单摘要实现（无需LLM）

        Args:
            messages: 消息列表

        Returns:
            str: 简单摘要
        """
        summary_parts = []
        for msg in messages[-10:]:  # 最近10条消息
            role = msg.get("role", "unknown")
            content = str(msg.get("content", ""))[:300]
            summary_parts.append(f"[{role}]: {content}...")

            # 包含工具调用信息
            for tc in msg.get("tool_calls", []):
                fn = tc.get("function", {})
                name = fn.get("name", "?")
                args = fn.get("arguments", "")[:100]
                summary_parts.append(f"[tool_call]: {name}({args})")

        return "\n".join(summary_parts)

    def _messages_to_text(self, messages: List[Dict]) -> str:
        """
        将消息列表转换为可读文本

        Args:
            messages: 消息列表

        Returns:
            str: 可读文本
        """
        parts = []
        for msg in messages:
            role = msg.get("role", "?")
            content = msg.get("content") or ""
            if isinstance(content, list):
                content = " ".join(
                    block.get("text", "") for block in content
                    if isinstance(block, dict)
                )
            if content:
                parts.append(f"[{role}] {content[:3000]}")
            for tc in msg.get("tool_calls", []):
                fn = tc.get("function", {})
                parts.append(
                    f"[tool_call] {fn.get('name', '?')}({fn.get('arguments', '')[:500]})"
                )
        return "\n".join(parts)

    def _persist_checkpoint(self, checkpoint: Checkpoint):
        """
        持久化检查点到文件

        Args:
            checkpoint: 检查点对象
        """
        try:
            self.workspace_path.mkdir(parents=True, exist_ok=True)

            content = f"""# Workflow Checkpoint

## Checkpoint Info
- ID: {checkpoint.id}
- Phase: {checkpoint.phase}
- Token Count: {checkpoint.token_count}
- Created At: {checkpoint.created_at}

## Summary
{checkpoint.messages_summary}
"""
            self.progress_file.write_text(content, encoding='utf-8')
            logger.info(f"Checkpoint persisted to {self.progress_file}")

        except Exception as e:
            logger.error(f"Failed to persist checkpoint: {e}")

    def _get_git_context(self) -> str:
        """
        获取 Git 上下文信息

        Returns:
            str: Git 上下文
        """
        try:
            result = subprocess.run(
                "git diff --stat HEAD~5 2>/dev/null || git log --oneline -5 2>/dev/null",
                shell=True,
                cwd=str(self.workspace_path),
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.stdout.strip():
                return f"\n\nRecent code changes:\n```\n{result.stdout.strip()[:2000]}\n```"
        except Exception:
            pass

        return ""


# ---------------------------------------------------------------------------
# 便捷函数
# ---------------------------------------------------------------------------

def create_context_manager(
    workspace_path: str,
    compaction_threshold: int = 80000,
    reset_threshold: int = 150000
) -> ContextManager:
    """
    创建上下文管理器实例

    Args:
        workspace_path: 工作区路径
        compaction_threshold: 压缩阈值
        reset_threshold: 重置阈值

    Returns:
        ContextManager: 上下文管理器实例
    """
    return ContextManager(
        workspace_path=workspace_path,
        compaction_threshold=compaction_threshold,
        reset_threshold=reset_threshold
    )


# 模块级默认实例
_default_manager: Optional[ContextManager] = None


def get_default_manager() -> ContextManager:
    """获取默认上下文管理器"""
    global _default_manager
    if _default_manager is None:
        _default_manager = ContextManager()
    return _default_manager


if __name__ == "__main__":
    # 测试代码
    manager = ContextManager(workspace_path="./test_workspace")

    # 测试消息
    test_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "assistant", "content": "I'm doing well, thank you!"},
    ]

    # 测试 token 计数
    print(f"Token count: {count_tokens(test_messages)}")

    # 测试焦虑检测
    anxiety_messages = [
        {"role": "assistant", "content": "Let me wrap up quickly... I'm running low on context."}
    ]
    print(f"Anxiety detected: {detect_anxiety(anxiety_messages)}")