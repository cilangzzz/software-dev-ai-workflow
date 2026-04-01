"""
Harness 工作流集成入口
提供命令行接口和程序化API
"""
import os
import sys
import argparse
import logging
from pathlib import Path
from typing import Optional, Dict, Any

# 添加引擎目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from workflow_engine import WorkflowEngine, Phase, PhaseStatus
from quality_gate import QualityGateChecker, GateStatus

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 默认路径配置
DEFAULT_BASE_PATH = Path(__file__).parent.parent  # 5.0-系统模型
DEFAULT_PROFILES_DIR = DEFAULT_BASE_PATH / ".harness" / "config" / "profiles"


def discover_profiles() -> Dict[str, Path]:
    """发现所有可用的Profile"""
    profiles = {}
    profiles_dir = DEFAULT_PROFILES_DIR

    if profiles_dir.exists():
        for profile_file in profiles_dir.glob("*.yaml"):
            profile_name = profile_file.stem
            profiles[profile_name] = profile_file

    return profiles


def run_workflow(
    workspace: str,
    profile: str = "erp-module-builder",
    verbose: bool = False
) -> bool:
    """
    运行工作流

    Args:
        workspace: 工作区路径
        profile: Profile名称或路径
        verbose: 是否输出详细日志

    Returns:
        bool: 是否成功
    """
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # 解析Profile路径
    profiles = discover_profiles()

    if profile in profiles:
        profile_path = profiles[profile]
    elif Path(profile).exists():
        profile_path = Path(profile)
    else:
        logger.error(f"Profile not found: {profile}")
        logger.info(f"Available profiles: {list(profiles.keys())}")
        return False

    logger.info(f"Using profile: {profile_path}")

    # 创建工作流引擎
    engine = WorkflowEngine(workspace, str(profile_path))

    # 执行工作流
    success = engine.run()

    # 输出结果
    if success:
        logger.info("=" * 60)
        logger.info("WORKFLOW PASSED")
        logger.info(f"Final score: {engine.overall_score}")
        logger.info(f"Iterations: {engine.iteration_count}")
        logger.info("=" * 60)
    else:
        logger.error("=" * 60)
        logger.error("WORKFLOW FAILED")
        logger.error("=" * 60)

    return success


def check_quality(workspace: str, gate: str = None) -> bool:
    """
    执行质量门控检查

    Args:
        workspace: 工作区路径
        gate: 指定检查的门控（可选）

    Returns:
        bool: 是否通过
    """
    checker = QualityGateChecker(workspace)

    if gate:
        result = checker.check(gate)
        print(f"\n{gate}: {result.status.value}")
        print(f"  Message: {result.message}")
        if result.errors:
            print("  Errors:")
            for err in result.errors:
                print(f"    - {err}")
        return result.status == GateStatus.PASSED
    else:
        results = checker.check_all([
            {"name": "prd_completeness", "params": {"required_sections": ["功能概述", "用户角色", "功能清单"]}},
            {"name": "user_story_coverage", "params": {"min_coverage": 80}},
            {"name": "architecture_review", "params": {"required_sections": ["架构图", "技术选型"]}},
            {"name": "sql_syntax_check", "params": {}},
            {"name": "api_spec_validation", "params": {}},
            {"name": "unit_test_coverage", "params": {"threshold": 80}},
            {"name": "integration_test_pass", "params": {}},
            {"name": "code_quality", "params": {"min_score": 7.0}},
        ])

        print("\n" + "=" * 60)
        print("Quality Gate Check Results")
        print("=" * 60)

        all_passed = True
        for name, result in results.items():
            status_icon = "✓" if result.status == GateStatus.PASSED else "✗"
            print(f"\n{status_icon} {name}: {result.status.value}")
            print(f"  Message: {result.message}")
            if result.errors:
                print("  Errors:")
                for err in result.errors:
                    print(f"    - {err}")
            if result.status == GateStatus.FAILED:
                all_passed = False

        print("\n" + "=" * 60)
        print(f"Overall: {'PASSED' if all_passed else 'FAILED'}")
        print("=" * 60)

        return all_passed


def main():
    """主入口"""
    parser = argparse.ArgumentParser(
        description="Harness 工作流集成 - 自动化企业系统开发",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 运行ERP模块开发工作流
  python main.py run --workspace "erp/车企模型/.workspace" --profile erp-module-builder

  # 运行MES模块开发工作流
  python main.py run --workspace "mes/车企模型/.workspace" --profile mes-module-builder

  # 执行质量门控检查
  python main.py check --workspace "erp/车企模型"

  # 列出可用Profile
  python main.py list-profiles
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    # run 命令
    run_parser = subparsers.add_parser("run", help="运行工作流")
    run_parser.add_argument(
        "--workspace", "-w",
        required=True,
        help="工作区路径（如 erp/车企模型/.workspace）"
    )
    run_parser.add_argument(
        "--profile", "-p",
        default="erp-module-builder",
        help="Profile名称或路径"
    )
    run_parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="输出详细日志"
    )

    # check 命令
    check_parser = subparsers.add_parser("check", help="执行质量门控检查")
    check_parser.add_argument(
        "--workspace", "-w",
        required=True,
        help="工作区路径"
    )
    check_parser.add_argument(
        "--gate", "-g",
        help="指定检查的门控（可选）"
    )

    # list-profiles 命令
    subparsers.add_parser("list-profiles", help="列出可用Profile")

    args = parser.parse_args()

    if args.command == "run":
        success = run_workflow(
            workspace=args.workspace,
            profile=args.profile,
            verbose=args.verbose
        )
        sys.exit(0 if success else 1)

    elif args.command == "check":
        success = check_quality(
            workspace=args.workspace,
            gate=args.gate
        )
        sys.exit(0 if success else 1)

    elif args.command == "list-profiles":
        profiles = discover_profiles()
        print("\nAvailable Profiles:")
        print("-" * 40)
        for name, path in profiles.items():
            print(f"  {name}: {path}")
        print()

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()