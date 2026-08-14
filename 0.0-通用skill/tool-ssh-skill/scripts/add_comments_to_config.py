#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为现有 SSH config 添加标准注释

读取现有的 SSH config 文件，为每个 Host 添加标准注释元数据
"""

import os
import re
from datetime import datetime


def parse_existing_config(config_path):
    """
    解析现有配置，提取每个 Host 块

    Returns:
        List of (comments, host_line, config_lines) tuples
    """
    if not os.path.exists(config_path):
        return []

    with open(config_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    hosts = []
    current_comments = []
    current_host_line = None
    current_config = []
    in_host_block = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # 检查是否是 Host 行
        if stripped.startswith('Host ') and not stripped.startswith('Host *'):
            # 保存上一个 Host 块
            if current_host_line:
                hosts.append((current_comments, current_host_line, current_config))

            # 开始新的 Host 块
            current_host_line = line
            current_config = []
            in_host_block = True
            # 保留之前收集的注释

        elif in_host_block:
            # 在 Host 块中
            if stripped and not stripped.startswith('#'):
                # 配置行（缩进的）
                if line.startswith((' ', '\t')):
                    current_config.append(line)
                else:
                    # 遇到非缩进的非注释行，Host 块结束
                    in_host_block = False
                    current_comments = []
                    if stripped.startswith('#'):
                        current_comments.append(line)
            elif stripped.startswith('#'):
                # Host 块中的注释（通常不应该有）
                current_config.append(line)
            elif not stripped:
                # 空行，Host 块可能结束
                current_config.append(line)
                in_host_block = False
                current_comments = []
        else:
            # 不在 Host 块中
            if stripped.startswith('#') or not stripped:
                current_comments.append(line)
            else:
                # 非注释非空行，清空注释缓存
                current_comments = []

        i += 1

    # 保存最后一个 Host 块
    if current_host_line:
        hosts.append((current_comments, current_host_line, current_config))

    return hosts


def extract_alias_from_host_line(host_line):
    """从 Host 行提取别名"""
    match = re.match(r'Host\s+(.+)', host_line.strip())
    if match:
        return match.group(1).strip()
    return None


def has_standard_comments(comments):
    """检查是否已有标准注释"""
    comment_text = ''.join(comments)
    return '# description:' in comment_text or '# environment:' in comment_text


def generate_standard_comments(alias):
    """生成标准注释"""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    comments = [
        f"\n# ===== {alias} =====\n",
        f"# description: \n",
        f"# environment: unknown\n",
        f"# tags: \n",
        f"# location: \n",
        f"# created_at: {now}\n",
        f"# updated_at: {now}\n"
    ]

    return comments


def add_comments_to_config(config_path, output_path=None):
    """
    为配置文件添加标准注释

    Args:
        config_path: 输入配置文件路径
        output_path: 输出配置文件路径（如果为 None，则覆盖原文件）
    """
    if output_path is None:
        output_path = config_path

    # 解析现有配置
    hosts = parse_existing_config(config_path)

    print(f"找到 {len(hosts)} 个 Host 配置")

    # 生成新配置
    new_lines = []
    processed_count = 0
    skipped_count = 0

    for comments, host_line, config_lines in hosts:
        alias = extract_alias_from_host_line(host_line)

        if not alias:
            # 无法提取别名，保持原样
            new_lines.extend(comments)
            new_lines.append(host_line)
            new_lines.extend(config_lines)
            skipped_count += 1
            continue

        # 检查是否已有标准注释
        if has_standard_comments(comments):
            # 已有标准注释，保持原样
            new_lines.extend(comments)
            new_lines.append(host_line)
            new_lines.extend(config_lines)
            skipped_count += 1
            print(f"  跳过 {alias}（已有标准注释）")
        else:
            # 添加标准注释
            standard_comments = generate_standard_comments(alias)
            new_lines.extend(standard_comments)
            new_lines.append(host_line)
            new_lines.extend(config_lines)
            processed_count += 1
            print(f"  添加注释: {alias}")

    # 写入新配置
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"\n完成:")
    print(f"  处理: {processed_count} 个")
    print(f"  跳过: {skipped_count} 个")
    print(f"  输出: {output_path}")


if __name__ == '__main__':
    config_path = os.path.expanduser('~/.ssh/config')
    add_comments_to_config(config_path)
