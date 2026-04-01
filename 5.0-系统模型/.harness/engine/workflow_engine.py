"""
Harness 工作流编排引擎
实现 Plan -> Contract -> Build -> Evaluate -> Iterate 主循环
"""
import os
import json
import yaml
from pathlib import Path
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PhaseStatus(Enum):
    """阶段状态枚举"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


class Phase(Enum):
    """工作流阶段枚举"""
    PLAN = "plan"
    CONTRACT = "contract"
    BUILD = "build"
    EVALUATE = "evaluate"
    ITERATE = "iterate"


@dataclass
class PhaseResult:
    """阶段执行结果"""
    phase: Phase
    status: PhaseStatus
    outputs: Dict[str, str] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)
    score: Optional[float] = None
    duration_seconds: float = 0.0


@dataclass
class WorkflowConfig:
    """工作流配置"""
    name: str
    max_rounds: int = 5
    pass_threshold: float = 7.0
    phases: List[Dict] = field(default_factory=list)
    context_config: Dict = field(default_factory=dict)
    tools: List[str] = field(default_factory=list)


class WorkflowEngine:
    """工作流编排引擎"""

    def __init__(self, workspace_path: str, profile_path: str):
        """
        初始化工作流引擎

        Args:
            workspace_path: 工作区路径（如 erp/车企模型/.workspace）
            profile_path: Profile配置文件路径
        """
        self.workspace_path = Path(workspace_path)
        self.profile_path = Path(profile_path)

        # 确保工作区存在
        self.workspace_path.mkdir(parents=True, exist_ok=True)

        # 加载配置
        self.config = self._load_profile()

        # 初始化状态文件路径
        self.spec_file = self.workspace_path / "spec.md"
        self.contract_file = self.workspace_path / "contract.md"
        self.progress_file = self.workspace_path / "progress.md"
        self.feedback_file = self.workspace_path / "feedback.md"

        # 当前状态
        self.current_phase = Phase.PLAN
        self.iteration_count = 0
        self.overall_score = None
        self.score_history: List[float] = []

        # 阶段执行历史
        self.phase_history: List[PhaseResult] = []

    def _load_profile(self) -> WorkflowConfig:
        """加载Profile配置"""
        if not self.profile_path.exists():
            logger.warning(f"Profile not found: {self.profile_path}, using defaults")
            return WorkflowConfig(name="default")

        with open(self.profile_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}

        return WorkflowConfig(
            name=data.get('name', 'unknown'),
            max_rounds=data.get('workflow', {}).get('max_rounds', 5),
            pass_threshold=data.get('workflow', {}).get('pass_threshold', 7.0),
            phases=data.get('workflow', {}).get('phases', []),
            context_config=data.get('context', {}),
            tools=(
                data.get('tools', {}).get('core', []) +
                data.get('tools', {}).get('extended', [])
            )
        )

    def run(self) -> bool:
        """
        执行完整工作流

        Returns:
            bool: 是否成功通过
        """
        logger.info(f"Starting workflow: {self.config.name}")
        total_start = datetime.now()

        # 读取需求规格
        if not self.spec_file.exists():
            logger.error(f"spec.md not found: {self.spec_file}")
            return False

        # 主循环
        for round_num in range(1, self.config.max_rounds + 1):
            logger.info("=" * 60)
            logger.info(f"ROUND {round_num}/{self.config.max_rounds}")
            logger.info("=" * 60)

            # 更新进度
            self._update_progress(round_num)

            # Phase 1: Plan
            plan_result = self._execute_phase(Phase.PLAN)
            self.phase_history.append(plan_result)
            if plan_result.status == PhaseStatus.FAILED:
                logger.error("Plan phase failed")
                return False

            # Phase 2: Contract
            contract_result = self._execute_phase(Phase.CONTRACT)
            self.phase_history.append(contract_result)
            if contract_result.status == PhaseStatus.FAILED:
                logger.error("Contract phase failed")
                return False

            # Phase 3: Build
            build_result = self._execute_phase(Phase.BUILD)
            self.phase_history.append(build_result)
            if build_result.status == PhaseStatus.FAILED:
                logger.error("Build phase failed")
                return False

            # Phase 4: Evaluate
            evaluate_result = self._execute_phase(Phase.EVALUATE)
            self.phase_history.append(evaluate_result)

            # 记录评分
            if evaluate_result.score is not None:
                self.score_history.append(evaluate_result.score)
                logger.info(f"Round {round_num} score: {evaluate_result.score:.1f} / 10")

            # 检查是否通过
            if evaluate_result.score and evaluate_result.score >= self.config.pass_threshold:
                logger.info(f"PASSED with score: {evaluate_result.score}")
                self.overall_score = evaluate_result.score
                self._write_final_report(success=True)
                return True

            # Phase 5: Iterate (如果未通过)
            if round_num < self.config.max_rounds:
                iterate_result = self._execute_phase(Phase.ITERATE)
                self.phase_history.append(iterate_result)
                self.iteration_count += 1

        total_duration = (datetime.now() - total_start).total_seconds()
        logger.warning(
            f"Max rounds reached without passing. "
            f"Last score: {evaluate_result.score}, "
            f"Duration: {total_duration / 60:.1f} minutes"
        )
        self._write_final_report(success=False)
        return False

    def _execute_phase(self, phase: Phase) -> PhaseResult:
        """
        执行单个阶段

        Args:
            phase: 阶段枚举值

        Returns:
            PhaseResult: 阶段执行结果
        """
        logger.info(f"Executing phase: {phase.value}")
        phase_start = datetime.now()

        # 获取阶段配置
        phase_config = self._get_phase_config(phase)
        if not phase_config:
            logger.warning(f"No config found for phase: {phase.value}")
            return PhaseResult(phase=phase, status=PhaseStatus.SKIPPED)

        # 更新状态为运行中
        self.current_phase = phase
        self._update_progress(phase=phase, status=PhaseStatus.RUNNING)

        try:
            # 执行阶段逻辑
            result = self._run_phase_logic(phase, phase_config)

            # 执行质量门控检查
            if result.status == PhaseStatus.COMPLETED:
                gate_result = self._check_quality_gate(phase_config.get('quality_gate', []))
                if not gate_result['passed']:
                    result.status = PhaseStatus.FAILED
                    result.errors.extend(gate_result['errors'])

            # 记录执行时长
            result.duration_seconds = (datetime.now() - phase_start).total_seconds()
            logger.info(
                f"Phase {phase.value} completed: {result.status.value} "
                f"in {result.duration_seconds:.1f}s"
            )

            return result

        except Exception as e:
            logger.error(f"Phase {phase.value} failed with error: {e}")
            return PhaseResult(
                phase=phase,
                status=PhaseStatus.FAILED,
                errors=[str(e)],
                duration_seconds=(datetime.now() - phase_start).total_seconds()
            )

    def _run_phase_logic(self, phase: Phase, config: Dict) -> PhaseResult:
        """
        执行阶段具体逻辑（由子类实现或调用Agent）

        Args:
            phase: 阶段枚举值
            config: 阶段配置

        Returns:
            PhaseResult: 阶段执行结果
        """
        # 这里是占位实现，实际需要调用 Agent 或 Skill
        # 子类可以重写此方法来实现具体的执行逻辑
        logger.info(f"Running phase logic for: {phase.value}")

        outputs = {}

        if phase == Phase.PLAN:
            # Plan阶段：需求分析与规划
            outputs = {
                "prd": "产品/PRD/PRD-{module}.md",
                "user_stories": "产品/UserStory/UserStory-{module}.md",
                "acceptance_criteria": "产品/AcceptanceCriteria/AC-{module}.md"
            }
        elif phase == Phase.CONTRACT:
            # Contract阶段：开发契约制定
            outputs = {
                "contract": ".workspace/contract.md",
                "architecture": "研发/系统架构设计.md"
            }
        elif phase == Phase.BUILD:
            # Build阶段：代码与文档生成
            outputs = {
                "db_design": "研发/数据库设计/DB-{module}.md",
                "api_design": "研发/API设计/API-{module}.md",
                "entities": "代码/backend/src/main/java/**/entity/",
                "crud": "代码/backend/src/main/java/**/{controller,service,mapper}/"
            }
        elif phase == Phase.EVALUATE:
            # Evaluate阶段：测试与验证
            outputs = {
                "test_cases": "代码/tests/",
                "feedback": ".workspace/feedback.md"
            }
            # 示例评分
            score = self._extract_score_from_feedback()
        elif phase == Phase.ITERATE:
            # Iterate阶段：迭代优化
            outputs = {
                "fixes": "代码更新",
                "doc_updates": "文档更新"
            }

        return PhaseResult(
            phase=phase,
            status=PhaseStatus.COMPLETED,
            outputs=outputs
        )

    def _check_quality_gate(self, gates: List[Dict]) -> Dict:
        """
        检查质量门控

        Args:
            gates: 质量门控配置列表

        Returns:
            Dict: 包含 passed 和 errors 的结果
        """
        result = {"passed": True, "errors": []}

        for gate in gates:
            gate_name = gate.get('name', 'unknown')
            gate_type = gate.get('type', 'auto')

            logger.info(f"Checking quality gate: {gate_name}")

            # 占位实现，实际需要调用对应的检查工具
            # 可以根据 gate_type 执行不同的检查
            if gate_type == 'auto':
                # 自动检查
                pass
            elif gate_type == 'manual':
                # 手动检查标记
                pass
            elif gate_type == 'llm':
                # LLM 检查
                pass

        return result

    def _get_phase_config(self, phase: Phase) -> Optional[Dict]:
        """
        获取阶段配置

        Args:
            phase: 阶段枚举值

        Returns:
            Optional[Dict]: 阶段配置字典，不存在返回None
        """
        for p in self.config.phases:
            if p.get('name') == phase.value:
                return p
        return None

    def _update_progress(
        self,
        round_num: int = 0,
        phase: Phase = None,
        status: PhaseStatus = None
    ):
        """
        更新进度文件

        Args:
            round_num: 当前轮次
            phase: 当前阶段
            status: 当前状态
        """
        progress_content = f"""# Workflow Progress

## Status
- Round: {round_num}/{self.config.max_rounds}
- Phase: {phase.value if phase else self.current_phase.value}
- Status: {status.value if status else 'initialized'}
- Iterations: {self.iteration_count}

## Score History
{self._format_score_history()}

## Phase History
{self._format_phase_history()}
"""

        with open(self.progress_file, 'w', encoding='utf-8') as f:
            f.write(progress_content)

    def _format_score_history(self) -> str:
        """格式化评分历史"""
        if not self.score_history:
            return "No scores yet"

        lines = []
        for i, score in enumerate(self.score_history, 1):
            status = "PASS" if score >= self.config.pass_threshold else "FAIL"
            lines.append(f"- Round {i}: {score:.1f} [{status}]")
        return "\n".join(lines)

    def _format_phase_history(self) -> str:
        """格式化阶段历史"""
        if not self.phase_history:
            return "No phase history yet"

        lines = []
        for result in self.phase_history:
            duration = f"{result.duration_seconds:.1f}s" if result.duration_seconds else "N/A"
            lines.append(
                f"- {result.phase.value}: {result.status.value} ({duration})"
            )
        return "\n".join(lines)

    def _extract_score_from_feedback(self) -> Optional[float]:
        """从反馈文件中提取评分"""
        if not self.feedback_file.exists():
            return None

        try:
            content = self.feedback_file.read_text(encoding='utf-8')
            # 尝试匹配评分模式
            import re
            patterns = [
                r'score[:\s]+(\d+(?:\.\d+)?)',
                r'评分[:\s]+(\d+(?:\.\d+)?)',
                r'(\d+(?:\.\d+)?)/10',
                r'(\d+(?:\.\d+)?)\s*[分点]',
            ]

            for pattern in patterns:
                match = re.search(pattern, content, re.IGNORECASE)
                if match:
                    return float(match.group(1))
        except Exception as e:
            logger.warning(f"Failed to extract score: {e}")

        return None

    def _write_final_report(self, success: bool):
        """写入最终报告"""
        report_path = self.workspace_path / "final_report.md"
        report_content = f"""# Workflow Final Report

## Summary
- Status: {'PASSED' if success else 'FAILED'}
- Total Rounds: {self.iteration_count + 1}
- Final Score: {self.overall_score or 'N/A'}
- Pass Threshold: {self.config.pass_threshold}

## Score History
{self._format_score_history()}

## Phase Execution Summary
{self._format_phase_history()}

## Generated Outputs
{_self._format_outputs()}
"""
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)

    def _format_outputs(self) -> str:
        """格式化输出"""
        lines = []
        for result in self.phase_history:
            if result.outputs:
                for key, value in result.outputs.items():
                    lines.append(f"- {key}: {value}")
        return "\n".join(lines) if lines else "No outputs recorded"


if __name__ == "__main__":
    # 示例用法
    workspace = "H:/Documents/software-dev-ai-workflow/5.0-系统模型/erp/车企模型/.workspace"
    profile = "H:/Documents/software-dev-ai-workflow/5.0-系统模型/.harness/config/profiles/erp-module-builder.yaml"

    engine = WorkflowEngine(workspace, profile)
    success = engine.run()
    print(f"Workflow completed: {'PASSED' if success else 'FAILED'}")