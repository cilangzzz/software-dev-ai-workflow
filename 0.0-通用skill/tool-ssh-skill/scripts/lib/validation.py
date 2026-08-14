"""
配置验证和安全检查模块

提供配置文件的验证、过期检查和审查提醒功能。
"""

import sys
import json
from typing import Optional
from .config import ServerConfig, check_config_review_status, check_config_expiration


def validate_before_execution(config: ServerConfig, ignore_warnings: bool = False) -> tuple[bool, Optional[str]]:
    """
    执行前验证配置（过期检查和审查提醒）

    Args:
        config: 服务器配置对象
        ignore_warnings: 是否忽略警告（审查提醒）

    Returns:
        (是否可以继续执行, 错误/警告信息) 元组
    """
    # 检查配置是否已过期（阻止执行）
    is_expired, expiration_msg = check_config_expiration(config)
    if is_expired:
        return False, f"[ERROR] 配置已过期: {expiration_msg}\n拒绝执行以保证安全。"

    # 检查审查状态（警告，不阻止执行）
    if not ignore_warnings:
        review_status = check_config_review_status(config)

        if review_status['needs_review']:
            days_since = review_status['days_since_review']
            interval = config.review_interval_days

            warning_msg = (
                f"[WARNING] 配置 '{config.name}' 需要审查！\n"
                f"  - 距离上次审查: {days_since} 天\n"
                f"  - 建议审查间隔: {interval} 天\n"
                f"  - 环境: {config.environment}\n"
            )

            if config.environment == 'production':
                warning_msg += f"  - ⚠️ 这是生产环境配置，请立即审查！\n"

            warning_msg += f"\n如需忽略此警告，请使用 --ignore-warnings 参数。\n"

            return False, warning_msg

        # 检查即将过期
        if config.expires_at and review_status['expires_in_days'] is not None:
            days_left = review_status['expires_in_days']
            if 0 <= days_left < 7:
                print(f"[INFO] 配置将在 {days_left} 天后过期", file=sys.stderr)

    return True, None


def print_config_warnings(config: ServerConfig):
    """
    打印配置警告信息（不阻止执行）

    Args:
        config: 服务器配置对象
    """
    review_status = check_config_review_status(config)

    if review_status['needs_review']:
        days_since = review_status['days_since_review']
        print(f"[INFO] 配置 '{config.name}' 已 {days_since} 天未审查", file=sys.stderr)

    if config.expires_at and review_status['expires_in_days'] is not None:
        days_left = review_status['expires_in_days']
        if 0 <= days_left < 7:
            print(f"[INFO] 配置将在 {days_left} 天后过期", file=sys.stderr)
