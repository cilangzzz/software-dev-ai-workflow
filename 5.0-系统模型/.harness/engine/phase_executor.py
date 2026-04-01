"""
阶段执行器 - 实现各阶段的具体执行逻辑
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from pathlib import Path
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


@dataclass
class ExecutionContext:
    """执行上下文"""
    workspace_path: str
    module_id: str
    tenant_id: Optional[str] = None
    variables: Dict[str, Any] = None

    def __post_init__(self):
        if self.variables is None:
            self.variables = {}


class PhaseExecutor(ABC):
    """阶段执行器基类"""

    def __init__(self, context: ExecutionContext):
        self.context = context
        self.workspace = Path(context.workspace_path)
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None

    @abstractmethod
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行阶段逻辑

        Args:
            inputs: 输入参数

        Returns:
            执行结果，包含:
            - status: 'completed' | 'failed' | 'skipped'
            - outputs: 输出文件路径映射
            - score: 评分（可选，Evaluate阶段使用）
            - errors: 错误列表
        """
        pass

    @abstractmethod
    def get_required_skills(self) -> List[str]:
        """获取该阶段需要的Skills"""
        pass

    def validate_inputs(self, inputs: Dict[str, Any]) -> bool:
        """
        验证输入参数

        Args:
            inputs: 输入参数字典

        Returns:
            bool: 验证是否通过
        """
        return True

    def pre_execute(self, inputs: Dict[str, Any]) -> bool:
        """
        执行前准备

        Args:
            inputs: 输入参数

        Returns:
            bool: 是否准备好执行
        """
        self.start_time = datetime.now()
        logger.info(f"[{self.__class__.__name__}] Starting execution at {self.start_time}")
        return self.validate_inputs(inputs)

    def post_execute(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行后处理

        Args:
            result: 执行结果

        Returns:
            Dict: 处理后的结果
        """
        self.end_time = datetime.now()
        duration = (self.end_time - self.start_time).total_seconds() if self.start_time else 0

        result['duration_seconds'] = duration
        result['executor'] = self.__class__.__name__
        result['timestamp'] = self.end_time.isoformat()

        logger.info(
            f"[{self.__class__.__name__}] Completed in {duration:.1f}s "
            f"with status: {result.get('status', 'unknown')}"
        )

        return result

    def read_file(self, relative_path: str) -> Optional[str]:
        """
        读取工作区文件

        Args:
            relative_path: 相对于工作区的路径

        Returns:
            Optional[str]: 文件内容，不存在返回None
        """
        file_path = self.workspace / relative_path
        if file_path.exists():
            return file_path.read_text(encoding='utf-8')
        return None

    def write_file(self, relative_path: str, content: str) -> bool:
        """
        写入工作区文件

        Args:
            relative_path: 相对于工作区的路径
            content: 文件内容

        Returns:
            bool: 是否成功
        """
        try:
            file_path = self.workspace / relative_path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content, encoding='utf-8')
            logger.info(f"Written file: {file_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to write file {relative_path}: {e}")
            return False


class PlanExecutor(PhaseExecutor):
    """Plan阶段执行器 - 需求分析与规划"""

    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("Executing Plan phase")

        if not self.pre_execute(inputs):
            return {"status": "failed", "errors": ["Input validation failed"]}

        try:
            # 1. 解析需求规格
            spec_content = self._read_spec()
            if not spec_content:
                return {"status": "failed", "errors": ["spec.md not found or empty"]}

            # 2. 调用 requirement-analyzer Skill
            # 实际实现需要调用 Skill 执行器
            prd_content = self._analyze_requirements(spec_content)

            # 3. 调用 user-story-generator Skill
            user_stories = self._generate_user_stories(spec_content)

            # 4. 调用 acceptance-criteria-writer Skill
            acceptance_criteria = self._write_acceptance_criteria(spec_content, user_stories)

            # 5. 写入输出文件
            module_id = self.context.module_id
            outputs = {}

            if prd_content:
                self.write_file(f"产品/PRD/PRD-{module_id}.md", prd_content)
                outputs["prd"] = f"产品/PRD/PRD-{module_id}.md"

            if user_stories:
                self.write_file(f"产品/UserStory/UserStory-{module_id}.md", user_stories)
                outputs["user_stories"] = f"产品/UserStory/UserStory-{module_id}.md"

            if acceptance_criteria:
                self.write_file(f"产品/AcceptanceCriteria/AC-{module_id}.md", acceptance_criteria)
                outputs["acceptance_criteria"] = f"产品/AcceptanceCriteria/AC-{module_id}.md"

            result = {
                "status": "completed",
                "outputs": outputs
            }

            return self.post_execute(result)

        except Exception as e:
            logger.error(f"Plan execution failed: {e}")
            return self.post_execute({
                "status": "failed",
                "errors": [str(e)]
            })

    def get_required_skills(self) -> List[str]:
        return ["requirement-analyzer", "user-story-generator", "acceptance-criteria-writer"]

    def _read_spec(self) -> Optional[str]:
        """读取需求规格文件"""
        return self.read_file("spec.md")

    def _analyze_requirements(self, spec_content: str) -> Optional[str]:
        """
        分析需求规格
        实际实现需要调用 requirement-analyzer Skill
        """
        # 占位实现
        logger.info("Analyzing requirements...")
        return f"# PRD\n\n基于需求规格生成的产品需求文档。\n\n## 原始需求\n\n{spec_content[:500]}..."

    def _generate_user_stories(self, spec_content: str) -> Optional[str]:
        """
        生成用户故事
        实际实现需要调用 user-story-generator Skill
        """
        logger.info("Generating user stories...")
        return "# User Stories\n\n用户故事列表..."

    def _write_acceptance_criteria(self, spec_content: str, user_stories: str) -> Optional[str]:
        """
        编写验收标准
        实际实现需要调用 acceptance-criteria-writer Skill
        """
        logger.info("Writing acceptance criteria...")
        return "# Acceptance Criteria\n\n验收标准列表..."


class ContractExecutor(PhaseExecutor):
    """Contract阶段执行器 - 开发契约制定"""

    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("Executing Contract phase")

        if not self.pre_execute(inputs):
            return {"status": "failed", "errors": ["Input validation failed"]}

        try:
            # 1. 读取PRD
            module_id = self.context.module_id
            prd_content = self.read_file(f"产品/PRD/PRD-{module_id}.md")

            # 2. 调用 architect Skill 生成架构设计
            architecture = self._design_architecture(prd_content)

            # 3. 协商开发契约
            contract = self._negotiate_contract(prd_content, architecture)

            # 4. 生成 contract.md
            outputs = {}

            if architecture:
                self.write_file("研发/系统架构设计.md", architecture)
                outputs["architecture"] = "研发/系统架构设计.md"

            if contract:
                self.write_file(".workspace/contract.md", contract)
                outputs["contract"] = ".workspace/contract.md"

            result = {
                "status": "completed",
                "outputs": outputs
            }

            return self.post_execute(result)

        except Exception as e:
            logger.error(f"Contract execution failed: {e}")
            return self.post_execute({
                "status": "failed",
                "errors": [str(e)]
            })

    def get_required_skills(self) -> List[str]:
        return ["architect", "adr"]

    def _design_architecture(self, prd_content: Optional[str]) -> Optional[str]:
        """
        设计架构
        实际实现需要调用 architect Skill
        """
        logger.info("Designing architecture...")
        return "# 系统架构设计\n\n架构设计文档..."

    def _negotiate_contract(self, prd_content: Optional[str], architecture: Optional[str]) -> Optional[str]:
        """
        协商开发契约
        """
        logger.info("Negotiating contract...")
        return "# 开发契约\n\n本迭代周期的开发契约...\n\n## APPROVED"


class BuildExecutor(PhaseExecutor):
    """Build阶段执行器 - 代码与文档生成"""

    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("Executing Build phase")

        if not self.pre_execute(inputs):
            return {"status": "failed", "errors": ["Input validation failed"]}

        try:
            # 读取契约
            contract = self.read_file(".workspace/contract.md")

            # 1. 调用 db-designer Skill 生成数据库设计
            db_design = self._design_database(contract)

            # 2. 调用 api-designer Skill 生成API设计
            api_design = self._design_api(contract)

            # 3. 调用 entity-generator Skill 生成实体类
            entities = self._generate_entities(db_design)

            # 4. 调用 crud-generator Skill 生成CRUD代码
            crud_code = self._generate_crud(entities, api_design)

            module_id = self.context.module_id
            outputs = {}

            if db_design:
                self.write_file(f"研发/数据库设计/DB-{module_id}.md", db_design)
                outputs["db_design"] = f"研发/数据库设计/DB-{module_id}.md"

            if api_design:
                self.write_file(f"研发/API设计/API-{module_id}.md", api_design)
                outputs["api_design"] = f"研发/API设计/API-{module_id}.md"

            # 代码文件路径
            outputs["entities"] = f"代码/backend/src/main/java/**/entity/"
            outputs["crud"] = f"代码/backend/src/main/java/**/controller,service,mapper/"

            result = {
                "status": "completed",
                "outputs": outputs
            }

            return self.post_execute(result)

        except Exception as e:
            logger.error(f"Build execution failed: {e}")
            return self.post_execute({
                "status": "failed",
                "errors": [str(e)]
            })

    def get_required_skills(self) -> List[str]:
        return ["db-designer", "api-designer", "entity-generator", "crud-generator", "implement", "scaffold"]

    def _design_database(self, contract: Optional[str]) -> Optional[str]:
        """生成数据库设计"""
        logger.info("Designing database...")
        return "# 数据库设计\n\n数据库表结构设计..."

    def _design_api(self, contract: Optional[str]) -> Optional[str]:
        """生成API设计"""
        logger.info("Designing API...")
        return "# API设计\n\nRESTful API接口设计..."

    def _generate_entities(self, db_design: Optional[str]) -> Optional[str]:
        """生成实体类"""
        logger.info("Generating entities...")
        return "Entity classes generated..."

    def _generate_crud(self, entities: Optional[str], api_design: Optional[str]) -> Optional[str]:
        """生成CRUD代码"""
        logger.info("Generating CRUD code...")
        return "CRUD code generated..."


class EvaluateExecutor(PhaseExecutor):
    """Evaluate阶段执行器 - 测试与验证"""

    def __init__(self, context: ExecutionContext, pass_threshold: float = 7.0):
        super().__init__(context)
        self.pass_threshold = pass_threshold

    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("Executing Evaluate phase")

        if not self.pre_execute(inputs):
            return {"status": "failed", "errors": ["Input validation failed"]}

        try:
            # 1. 调用 test-case-generator Skill
            test_cases = self._generate_test_cases()

            # 2. 调用 test-executor Skill
            test_results = self._execute_tests(test_cases)

            # 3. 调用 code-review Skill
            review_results = self._review_code()

            # 4. 生成 feedback.md
            feedback = self._generate_feedback(test_results, review_results)
            score = self._calculate_score(test_results, review_results)

            outputs = {}
            if test_cases:
                outputs["test_cases"] = "代码/tests/"

            if feedback:
                self.write_file(".workspace/feedback.md", feedback)
                outputs["feedback"] = ".workspace/feedback.md"

            result = {
                "status": "completed",
                "score": score,
                "outputs": outputs
            }

            return self.post_execute(result)

        except Exception as e:
            logger.error(f"Evaluate execution failed: {e}")
            return self.post_execute({
                "status": "failed",
                "errors": [str(e)]
            })

    def get_required_skills(self) -> List[str]:
        return ["test-case-generator", "test-executor", "code-review"]

    def _generate_test_cases(self) -> Optional[str]:
        """生成测试用例"""
        logger.info("Generating test cases...")
        return "Test cases generated..."

    def _execute_tests(self, test_cases: Optional[str]) -> Dict[str, Any]:
        """执行测试"""
        logger.info("Executing tests...")
        return {
            "total": 10,
            "passed": 8,
            "failed": 2,
            "coverage": 0.85
        }

    def _review_code(self) -> Dict[str, Any]:
        """代码审查"""
        logger.info("Reviewing code...")
        return {
            "issues": [
                {"severity": "warning", "message": "Potential null pointer"},
                {"severity": "info", "message": "Code style issue"}
            ],
            "quality_score": 8.5
        }

    def _generate_feedback(self, test_results: Dict, review_results: Dict) -> str:
        """生成反馈文档"""
        return f"""# Evaluation Feedback

## Test Results
- Total: {test_results.get('total', 0)}
- Passed: {test_results.get('passed', 0)}
- Failed: {test_results.get('failed', 0)}
- Coverage: {test_results.get('coverage', 0):.1%}

## Code Review
- Issues: {len(review_results.get('issues', []))}
- Quality Score: {review_results.get('quality_score', 0)}

## Recommendations
- Fix failing tests
- Address code review issues
"""

    def _calculate_score(self, test_results: Dict, review_results: Dict) -> float:
        """计算综合评分"""
        # 基于测试结果和代码审查计算评分
        test_score = test_results.get('passed', 0) / max(test_results.get('total', 1), 1) * 10
        coverage_score = test_results.get('coverage', 0) * 10
        review_score = review_results.get('quality_score', 7)

        # 加权平均
        final_score = test_score * 0.4 + coverage_score * 0.3 + review_score * 0.3
        return round(final_score, 1)


class IterateExecutor(PhaseExecutor):
    """Iterate阶段执行器 - 迭代优化"""

    def __init__(self, context: ExecutionContext, previous_score: float = 0.0):
        super().__init__(context)
        self.previous_score = previous_score

    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("Executing Iterate phase")

        if not self.pre_execute(inputs):
            return {"status": "failed", "errors": ["Input validation failed"]}

        try:
            # 1. 读取 feedback.md
            feedback = self.read_file(".workspace/feedback.md")

            # 2. 分析问题
            issues = self._analyze_issues(feedback)

            # 3. 调用 bug-analyzer Skill
            bug_analysis = self._analyze_bugs(issues)

            # 4. 调用 refactor Skill
            refactor_plan = self._plan_refactoring(bug_analysis)

            # 5. 执行修复
            fixes = self._apply_fixes(refactor_plan)

            outputs = {}
            if fixes:
                outputs["fixes"] = "代码更新"
                outputs["doc_updates"] = "文档更新"

            result = {
                "status": "completed",
                "outputs": outputs
            }

            return self.post_execute(result)

        except Exception as e:
            logger.error(f"Iterate execution failed: {e}")
            return self.post_execute({
                "status": "failed",
                "errors": [str(e)]
            })

    def get_required_skills(self) -> List[str]:
        return ["bug-analyzer", "refactor", "implement"]

    def _analyze_issues(self, feedback: Optional[str]) -> List[Dict]:
        """分析问题"""
        logger.info("Analyzing issues...")
        return [
            {"type": "test_failure", "message": "Test case failed"},
            {"type": "code_smell", "message": "Code smell detected"}
        ]

    def _analyze_bugs(self, issues: List[Dict]) -> Dict[str, Any]:
        """分析Bug"""
        logger.info("Analyzing bugs...")
        return {"bugs": issues, "priority": "high"}

    def _plan_refactoring(self, bug_analysis: Dict) -> Dict[str, Any]:
        """规划重构"""
        logger.info("Planning refactoring...")
        return {"steps": ["Fix bug 1", "Refactor module A"]}

    def _apply_fixes(self, refactor_plan: Dict) -> bool:
        """应用修复"""
        logger.info("Applying fixes...")
        return True


# 执行器工厂
def get_executor(phase: str, context: ExecutionContext, **kwargs) -> PhaseExecutor:
    """
    获取阶段执行器

    Args:
        phase: 阶段名称
        context: 执行上下文
        **kwargs: 额外参数

    Returns:
        PhaseExecutor: 阶段执行器实例
    """
    executors = {
        "plan": PlanExecutor,
        "contract": ContractExecutor,
        "build": BuildExecutor,
        "evaluate": lambda ctx: EvaluateExecutor(ctx, kwargs.get('pass_threshold', 7.0)),
        "iterate": lambda ctx: IterateExecutor(ctx, kwargs.get('previous_score', 0.0))
    }

    executor_class = executors.get(phase)
    if executor_class is None:
        raise ValueError(f"Unknown phase: {phase}")

    if callable(executor_class) and not isinstance(executor_class, type):
        return executor_class(context)
    return executor_class(context)