#!/bin/bash
# 获取系统信息脚本

# 操作系统
if [ -f /etc/os-release ]; then
    OS=$(grep PRETTY_NAME /etc/os-release | cut -d'"' -f2)
else
    OS=$(uname -s)
fi

# CPU核心数
CPU=$(nproc 2>/dev/null || grep -c processor /proc/cpuinfo 2>/dev/null || echo "?")

# 内存（GB）
if [ -f /proc/meminfo ]; then
    MEM_KB=$(grep MemTotal /proc/meminfo | grep -o '[0-9]*')
    MEM_GB=$(echo "scale=1; $MEM_KB/1024/1024" | bc 2>/dev/null || echo "?")
    MEM="${MEM_GB}G"
else
    MEM="?"
fi

# 磁盘总空间
DISK=$(df -h / | tail -1 | tr -s ' ' | cut -d' ' -f2)

# 输出格式化信息
echo "$OS/$CPU核/${MEM}内存/${DISK}磁盘"
