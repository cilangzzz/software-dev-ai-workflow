# Skill: ci-pipeline-assistant

## 基本信息
- **名称**: ci-pipeline-assistant
- **版本**: 1.0.0
- **所属部门**: 运维部
- **优先级**: P0

## 功能描述
CI/CD流水线故障诊断和优化建议。分析流水线失败原因，提供修复建议，并优化构建性能。

## 触发条件
- 命令触发: `/ci-pipeline-assistant`
- 自然语言触发:
  - "CI构建失败了"
  - "分析流水线错误"
  - "优化构建速度"

## 输入参数
| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| pipeline_log | string | 是 | 流水线日志或错误信息 |
| pipeline_type | string | 否 | 流水线类型：github / gitlab / jenkins |
| focus | string | 否 | 关注点：debug / optimize |

## 执行流程
1. **日志解析** - 解析流水线日志
2. **错误识别** - 识别失败阶段和原因
3. **根因分析** - 分析问题根因
4. **修复建议** - 提供修复方案
5. **优化建议** - 提供性能优化建议

## 输出格式

### CI诊断报告
```markdown
# CI流水线诊断报告

## 问题摘要
- 失败阶段: {stage}
- 错误类型: {type}
- 严重程度: {severity}

## 错误详情
### 错误信息
```
{error_message}
```

### 失败原因
{failure_reason}

## 根因分析
{root_cause_analysis}

## 修复建议
### 立即修复
```{language}
{fix_code}
```

### 长期方案
- {solution1}
- {solution2}

## 构建优化建议
| 优化项 | 当前耗时 | 优化后预计 | 建议 |
|--------|----------|------------|------|
| {item} | {time} | {optimized} | {suggestion} |

## 预防措施
- {measure1}
- {measure2}
```

## 使用示例

### 示例：构建失败诊断
**输入**:
```
pipeline_log: |
  [ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.8.1:compile
  [ERROR] Failed to compile: /src/main/java/com/example/UserService.java:[45,30]
  cannot find symbol: method getEmail()
```

**输出**:
```markdown
# CI流水线诊断报告

## 问题摘要
- 失败阶段: compile
- 错误类型: 编译错误
- 严重程度: 高

## 错误详情
### 错误信息
```
[ERROR] Failed to compile: /src/main/java/com/example/UserService.java:[45,30]
cannot find symbol: method getEmail()
```

### 失败原因
UserService.java第45行调用了不存在的getEmail()方法。

## 根因分析
1. User类可能缺少getEmail()方法
2. 或者方法名拼写错误（可能是getEmailAddress()）
3. 可能是合并代码冲突导致的方法缺失

## 修复建议
### 立即修复
检查User类，确认邮件获取方法的正确名称：
```java
// 检查User类中的方法定义
public class User {
    private String email;
    // 确认是getEmail()还是其他名称
    public String getEmail() {
        return email;
    }
}
```

### 长期方案
- 使用IDE的编译检查，本地提交前确保编译通过
- 添加pre-commit hook进行编译检查

## 构建优化建议
| 优化项 | 当前耗时 | 优化后预计 | 建议 |
|--------|----------|------------|------|
| Maven依赖下载 | 2m30s | 30s | 配置本地缓存镜像 |
| 编译阶段 | 1m20s | 45s | 开启并行编译 |

## 预防措施
- 在CI中添加增量编译检查
- 使用maven-enforcer-plugin检查依赖冲突
```

## 质量标准
- 错误识别准确率 ≥ 95%
- 修复建议有效性 ≥ 85%
- 诊断响应时间 < 30秒

## 依赖工具
- Read - 读取配置文件
- Grep - 搜索错误模式
- Bash - 执行诊断命令

## 注意事项
- 分析前确保日志完整
- 关注构建环境的差异
- 优化建议需要结合实际资源情况