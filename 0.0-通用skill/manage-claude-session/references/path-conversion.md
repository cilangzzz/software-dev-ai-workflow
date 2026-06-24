# 路径转换规则

## 概述

Claude Code 将项目路径转换为目录名，用于存储会话数据。本文档说明转换规则。

## 转换规则

### 基本规则

```
原始路径 → 目录名
```

1. **替换路径分隔符**: 将 `\` 或 `/` 替换为 `--`
2. **去除驱动器冒号**: 将 `C:` 转换为 `C` 或 `c`
3. **统一小写**: 驱动器字母转为小写
4. **处理特殊字符**: 保留字母、数字、连字符

### Windows 路径转换

| 原始路径 | 转换后目录名 |
|----------|--------------|
| `f:\sandbox\workflow` | `f--sandbox-workflow` |
| `C:\Users\admin` | `C--Users-admin` 或 `c--Users-admin` |
| `D:\projects\my-app` | `d--projects-my-app` |

### Linux/macOS 路径转换

| 原始路径 | 转换后目录名 |
|----------|--------------|
| `/home/user/project` | `-home-user-project` |
| `/Users/dev/workspace` | `-Users-dev-workspace` |

## 转换算法

### JavaScript 实现

```javascript
function pathToHashPath(projectPath) {
  // 统一使用正斜杠
  let normalized = projectPath.replace(/\\/g, '/');

  // 去除开头的驱动器格式 (如 C:/)
  normalized = normalized.replace(/^([a-zA-Z]):/, '$1');

  // 将路径分隔符替换为双连字符
  let hashPath = normalized.replace(/\//g, '--');

  // 处理开头的连字符
  if (hashPath.startsWith('--')) {
    hashPath = hashPath.substring(2);
  }

  return hashPath;
}

// 示例
console.log(pathToHashPath('f:\\sandbox\\workflow'));
// 输出: f--sandbox-workflow
```

### Python 实现

```python
import re

def path_to_hash_path(project_path: str) -> str:
    # 统一使用正斜杠
    normalized = project_path.replace('\\', '/')

    # 去除驱动器格式
    normalized = re.sub(r'^([a-zA-Z]):', r'\1', normalized)

    # 替换路径分隔符
    hash_path = normalized.replace('/', '--')

    # 处理开头的连字符
    if hash_path.startswith('--'):
        hash_path = hash_path[2:]

    return hash_path

# 示例
print(path_to_hash_path('f:\\sandbox\\workflow'))
# 输出: f--sandbox-workflow
```

### Bash 实现

```bash
path_to_hash() {
    local path="$1"
    # 替换反斜杠为双连字符
    echo "$path" | sed 's/\\/--/g' | sed 's/:/-/g' | sed 's/^--//'
}

# 示例
path_to_hash "f:\\sandbox\\workflow"
# 输出: f--sandbox-workflow
```

## 反向转换

从目录名还原原始路径（需要上下文信息）：

```javascript
function hashPathToPath(hashPath, os = 'windows') {
  if (os === 'windows') {
    // 假设第一个字符是驱动器
    const driveLetter = hashPath.charAt(0).toUpperCase();
    const rest = hashPath.substring(1).replace(/--/g, '\\');
    return `${driveLetter}:${rest}`;
  } else {
    return '/' + hashPath.replace(/--/g, '/');
  }
}

// 示例
console.log(hashPathToPath('f--sandbox-workflow'));
// 输出: F:\sandbox\workflow
```

## 常见项目路径映射

| 项目路径 | Hash 目录名 |
|----------|-------------|
| `f:\sandbox\workflow` | `f--sandbox-workflow` |
| `f:\projects\yudao-ai-his` | `f--projects-yudao-ai-his` |
| `f:\projects\yudao-ai-his-admin-ui` | `f--projects-yudao-ai-his-admin-ui` |
| `C:\Users\admin\Desktop` | `C--Users-admin-Desktop` |
| `c:\Users\admin` | `c--Users-admin` |

## 验证方法

```bash
# 列出所有项目目录
ls ~/.claude/projects/

# 查看特定项目的会话
ls ~/.claude/projects/f--sandbox-workflow/
```

## 特殊情况处理

### 1. 包含空格的路径

```
C:\Program Files\MyApp → C--Program Files--MyApp
```

注意：空格会被保留，但在某些系统中可能被处理为其他形式。

### 2. 网络路径

```
\\server\share\project → --server--share--project
```

### 3. 相对路径

相对路径通常会被转换为绝对路径后再处理。

### 4. 符号链接

符号链接会被解析为实际路径后处理。

## 在会话文件中的路径表示

在 `.jsonl` 文件中，路径使用双反斜杠转义：

```json
{
  "cwd": "f:\\\\sandbox\\\\workflow",
  "project": "C:\\\\Users\\\\admin\\\\Desktop"
}
```

解析时需要注意：

```javascript
// JSON.parse 会自动处理转义
const obj = JSON.parse(line);
console.log(obj.cwd); // f:\sandbox\workflow
```

---
**版本**: 1.0.0
**最后更新**: 2026-06-24
