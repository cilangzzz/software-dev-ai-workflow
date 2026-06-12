# Skill: test-executor

## 基本信息
- **名称**: test-executor
- **版本**: 1.0.0
- **所属部门**: 测试部
- **优先级**: P0

## 功能描述
执行自动化测试并生成测试报告。支持单元测试、集成测试、E2E测试等多种测试类型的执行和结果分析。

## 触发条件
- 命令触发: `/test-executor`
- 自然语言触发:
  - "执行测试"
  - "运行测试"
  - "跑测试用例"

## 输入参数
| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| test_path | string | 是 | 测试文件或目录路径 |
| test_type | string | 否 | 测试类型：unit / integration / e2e / all |
| coverage | boolean | 否 | 是否收集覆盖率，默认true |

## 执行流程
1. **测试发现** - 扫描测试文件
2. **依赖检查** - 确认测试环境就绪
3. **测试执行** - 运行测试用例
4. **结果收集** - 收集测试结果和日志
5. **报告生成** - 生成测试报告

## 输出格式

### 测试报告
```markdown
# 测试执行报告

## 执行概要
- 执行时间: {timestamp}
- 总耗时: {duration}
- 测试用例数: {total}
- 通过: {passed} ✅
- 失败: {failed} ❌
- 跳过: {skipped} ⏭️
- 通过率: {rate}%

## 覆盖率报告
| 类型 | 覆盖率 | 详情 |
|------|--------|------|
| 行覆盖率 | {line}% | {lines_covered}/{lines_total} |
| 分支覆盖率 | {branch}% | {branches_covered}/{branches_total} |
| 函数覆盖率 | {func}% | {funcs_covered}/{funcs_total} |

## 失败用例
### {test_name}
- 失败原因: {reason}
- 错误信息:
```
{error_message}
```

## 执行详情
| 测试套件 | 用例数 | 通过 | 失败 | 耗时 |
|----------|--------|------|------|------|
| {suite} | {n} | {p} | {f} | {t} |
```

## 使用示例

### 示例：执行单元测试
**输入**:
```
test_path: src/test/java/com/example/
test_type: unit
coverage: true
```

**输出**:
```markdown
# 测试执行报告

## 执行概要
- 执行时间: 2024-01-15 14:30:00
- 总耗时: 45.2s
- 测试用例数: 128
- 通过: 125 ✅
- 失败: 3 ❌
- 跳过: 0 ⏭️
- 通过率: 97.6%

## 覆盖率报告
| 类型 | 覆盖率 | 详情 |
|------|--------|------|
| 行覆盖率 | 85.3% | 2340/2743 |
| 分支覆盖率 | 78.2% | 456/583 |
| 函数覆盖率 | 92.1% | 245/266 |

## 失败用例
### UserServiceTest.testRegisterWithDuplicateEmail
- 失败原因: 断言失败
- 错误信息:
```
AssertionError: Expected exception BusinessException
but no exception was thrown
```

## 执行详情
| 测试套件 | 用例数 | 通过 | 失败 | 耗时 |
|----------|--------|------|------|------|
| UserServiceTest | 15 | 14 | 1 | 2.3s |
| OrderServiceTest | 22 | 22 | 0 | 5.1s |
| PaymentServiceTest | 18 | 16 | 2 | 8.2s |
```

## 质量标准
- 测试执行成功率 ≥ 95%
- 覆盖率报告准确性 100%
- 失败原因定位准确率 ≥ 90%

## 依赖工具
- Bash - 执行测试命令
- Read - 读取测试配置
- Write - 输出报告文件

## 注意事项
- 确保测试环境隔离
- 大型测试套件建议并行执行
- 关注测试执行时间，超时用例需优化