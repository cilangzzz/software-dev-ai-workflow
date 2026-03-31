"""
Harness 工作流编排引擎

实现 Plan -> Contract -> Build -> Evaluate -> Iterate 主循环

模块结构:
- workflow_engine: 工作流编排引擎核心
- phase_executor: 阶段执行器
- context_manager: 上下文管理器
"""

from .workflow_engine import (
    WorkflowEngine,
    WorkflowConfig,
    Phase,
    PhaseStatus,
    PhaseResult,
)

from .phase_executor import (
    PhaseExecutor,
    ExecutionContext,
    PlanExecutor,
    ContractExecutor,
    BuildExecutor,
    EvaluateExecutor,
    IterateExecutor,
    get_executor,
)

from .context_manager import (
    ContextManager,
    Checkpoint,
    count_tokens,
    detect_anxiety,
    create_context_manager,
    get_default_manager,
)

from .quality_gate import (
    QualityGateChecker,
    GateStatus,
    GateResult,
)

__all__ = [
    # Workflow Engine
    "WorkflowEngine",
    "WorkflowConfig",
    "Phase",
    "PhaseStatus",
    "PhaseResult",

    # Phase Executors
    "PhaseExecutor",
    "ExecutionContext",
    "PlanExecutor",
    "ContractExecutor",
    "BuildExecutor",
    "EvaluateExecutor",
    "IterateExecutor",
    "get_executor",

    # Context Manager
    "ContextManager",
    "Checkpoint",
    "count_tokens",
    "detect_anxiety",
    "create_context_manager",
    "get_default_manager",

    # Quality Gate
    "QualityGateChecker",
    "GateStatus",
    "GateResult",
]

__version__ = "1.0.0"