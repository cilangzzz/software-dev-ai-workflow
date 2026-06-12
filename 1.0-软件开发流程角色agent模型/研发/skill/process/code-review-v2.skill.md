# 代码审查专家

## 基本信息

- **ID**: code-review-v2
- **名称**: 代码审查专家
- **版本**: 2.0.0
- **分类**: review
- **部门**: 研发部
- **描述**: 专业代码审查工具，基于OWASP安全标准、Clean Code原则、SOLID设计原则，从安全、性能、质量、可维护性四个维度审查代码变更。


## 触发条件


### commands

- /code-review
- /代码审查
- /cr

### keywords

- 代码审查
- 代码评审
- review代码
- 检查代码
- 代码质量

### patterns

- 帮我审查.*代码
- review.*变更
- 检查.*代码质量

## 输入参数


### parameters


- **name**: review_target
- **type**: string
- **required**: True
- **description**: 审查目标（文件路径、Git diff或PR编号）
- **examples**: - src/main/java/com/example/UserService.java
- PR-123
- git diff HEAD~1

- **name**: review_type
- **type**: string
- **required**: False
- **default**: full
- **enum**: - quick
- security
- performance
- quality
- full
- **description**: 审查类型选择

- **name**: focus_areas
- **type**: array
- **required**: False
- **default**: - all
- **items**: - security
- performance
- quality
- maintainability
- style
- all
- **description**: 关注领域列表

- **name**: severity_threshold
- **type**: string
- **required**: False
- **default**: warning
- **enum**: - critical
- major
- warning
- all
- **description**: 问题严重程度阈值

- **name**: tech_stack
- **type**: string
- **required**: False
- **default**: 
- **description**: 技术栈（加载特定规则）
- **examples**: - java
- python
- vue
- react

## 工作流程

- **description**: 四维度代码审查流程，确保代码质量和安全

### phases


- **name**: 代码解析
- **description**: 解析代码变更，提取关键信息
- **duration**: 1-2分钟
- **steps**: 
- **step**: 获取代码变更
- **action**: 读取文件内容或Git diff
- **output**: 代码变更列表

- **step**: 变更分类
- **action**: 分类变更类型（新增/修改/删除）
- **output**: 变更分类

- **step**: 技术栈识别
- **action**: 识别代码语言和框架
- **reference**: 按需加载规则

- **name**: 安全审查
- **description**: 基于OWASP标准的安全审查
- **duration**: 5-10分钟
- **steps**: 
- **step**: 注入漏洞检测
- **action**: 检测SQL注入、XSS、命令注入
- **rules**: OWASP Top 10
- **severity**: critical

- **step**: 认证授权检查
- **action**: 检查认证授权机制
- **rules**: 安全认证规则
- **severity**: critical

- **step**: 敏感信息检测
- **action**: 检测硬编码密码、密钥泄露
- **rules**: 敏感信息规则
- **severity**: critical

- **step**: 数据安全检查
- **action**: 检查数据加密、脱敏处理
- **rules**: 数据安全规则
- **severity**: major

- **name**: 性能审查
- **description**: 性能问题和资源效率审查
- **duration**: 5-10分钟
- **steps**: 
- **step**: 数据库性能检查
- **action**: 检测N+1查询、缺少索引
- **rules**: 数据库性能规则
- **severity**: major

- **step**: 内存效率检查
- **action**: 检测内存泄漏风险、大对象创建
- **rules**: 内存效率规则
- **severity**: warning

- **step**: 算法效率检查
- **action**: 检测不必要的循环、复杂算法
- **rules**: 算法效率规则
- **severity**: warning

- **step**: 并发安全检查
- **action**: 检测并发问题、死锁风险
- **rules**: 并发安全规则
- **severity**: critical

- **name**: 质量审查
- **description**: 代码质量、可维护性、设计原则审查
- **duration**: 5-10分钟
- **steps**: 
- **step**: Clean Code检查
- **action**: 检查命名、注释、代码组织
- **rules**: Clean Code原则
- **severity**: warning

- **step**: SOLID原则检查
- **action**: 检查设计原则遵循情况
- **rules**: SOLID原则
- **severity**: warning

- **step**: 代码重复检测
- **action**: 检测重复代码块
- **rules**: 代码重复阈值
- **severity**: warning

- **step**: 复杂度检查
- **action**: 检查圈复杂度、方法长度
- **rules**: 复杂度阈值
- **severity**: warning

- **name**: 报告生成
- **description**: 生成审查报告和改进建议
- **duration**: 2-5分钟
- **steps**: 
- **step**: 问题汇总
- **action**: 汇总所有问题并分级
- **output**: 问题清单

- **step**: 评分计算
- **action**: 计算代码质量评分
- **formula**: 质量得分 = 100 - Σ(问题权重)

- **step**: 修复建议生成
- **action**: 生成具体修复建议
- **output**: 修复建议清单

- **step**: 报告输出
- **action**: 生成格式化审查报告
- **template**: review-report-template

## 输出产物

- **base_path**: 研发/产出物/{project_name}/开发阶段/代码审查/

### artifacts


- **name**: 审查报告
- **files**: - 代码审查报告-{date}-{file}.md
- **format**: markdown
- **description**: 完整的代码审查报告
- **required**: True

- **name**: 问题清单
- **files**: - 问题清单-{date}.xlsx
- **format**: excel
- **description**: 问题详情和修复建议
- **required**: True

- **name**: 修复建议
- **files**: - 修复建议-{date}.md
- **format**: markdown
- **description**: 具体的代码修复建议
- **required**: False

## templates

- **review_report_template**: 
```
# 代码审查报告

## 报告信息
| 审查目标 | {target} |
| 审查类型 | {review_type} |
| 技术栈 | {tech_stack} |
| 审查时间 | {date} |
| 审查人 | {reviewer} |

---

## 审查摘要

### 统计概览
- **审查文件**: {file_count} 个
- **代码行数**: {line_count} 行
- **变更行数**: +{added} -{deleted}
- **问题总数**: {issue_count} 个
  - 🔴 **严重(Critical)**: {critical} 个 - 必须修复
  - 🟠 **重要(Major)**: {major} 个 - 应该修复
  - 🟡 **警告(Warning)**: {warning} 个 - 建议修复

### 质量评分
| 维度 | 评分 | 说明 |
|------|------|------|
| 安全性 | {score}/10 | {note} |
| 性能 | {score}/10 | {note} |
| 可读性 | {score}/10 | {note} |
| 可维护性 | {score}/10 | {note} |
| **综合评分** | {total}/10 | {note} |

### 审查结论
| 结论 | 说明 |
| {通过/需修改/需重审} | {conclusion_note} |

---

## 问题详情

### 🔴 严重问题 (Critical) - 必须修复

| # | 类型 | 文件 | 行号 | 问题描述 | OWASP分类 | 修复建议 |
|---|------|------|------|---------|-----------|---------|
| 1 | {type} | {file} | {line} | {desc} | A1-A10 | {fix} |

#### 问题1详情
**问题类型**: {type}
**问题描述**: {详细描述}
**影响**: {安全/性能影响}
**修复建议**:
```{language}
// 修复代码示例
{fix_code}
```
**参考资料**: {reference_url}

---

### 🟠 重要问题 (Major) - 应该修复

| # | 类型 | 文件 | 行号 | 问题描述 | 修复建议 |
|---|------|------|------|---------|---------|
| 1 | {type} | {file} | {line} | {desc} | {fix} |

---

### 🟡 改进建议 (Warning) - 建议修复

| # | 类型 | 文件 | 问题描述 | 建议 |
|---|------|------|---------|------|
| 1 | {type} | {file} | {desc} | {suggestion} |

---

## 安全审查详情

### OWASP Top 10 检查结果
| OWASP分类 | 检查项 | 结果 | 问题数 |
| A01:权限控制失效 | 认证授权检查 | ✅/⚠️/❌ | {count} |
| A02:加密失效 | 加密实现检查 | ✅/⚠️/❌ | {count} |
| A03:注入 | SQL/XSS/命令注入检查 | ✅/⚠️/❌ | {count} |
| A04:不安全设计 | 设计安全检查 | ✅/⚠️/❌ | {count} |
| A05:安全配置错误 | 配置安全检查 | ✅/⚠️/❌ | {count} |
| A06:脆弱组件 | 依赖安全检查 | ✅/⚠️/❌ | {count} |
| A07:身份认证失败 | 认证机制检查 | ✅/⚠️/❌ | {count} |
| A08:软件完整性失败 | 代码完整性检查 | ✅/⚠️/❌ | {count} |
| A09:日志监控失败 | 日志安全检查 | ✅/⚠️/❌ | {count} |
| A10:SSRF | SSRF检查 | ✅/⚠️/❌ | {count} |

---

## 性能审查详情

| 检查项 | 结果 | 问题数 | 说明 |
| 数据库查询 | ✅/⚠️/❌ | {count} | {note} |
| 内存使用 | ✅/⚠️/❌ | {count} | {note} |
| 算法效率 | ✅/⚠️/❌ | {count} | {note} |
| 并发安全 | ✅/⚠️/❌ | {count} | {note} |

---

## 代码质量详情

### Clean Code 检查
| 检查项 | 结果 | 问题数 |
| 命名规范 | ✅/⚠️/❌ | {count} |
| 注释完整性 | ✅/⚠️/❌ | {count} |
| 代码组织 | ✅/⚠️/❌ | {count} |

### SOLID 原则检查
| 原则 | 检查结果 | 问题 |
| S - 单一职责 | ✅/⚠️/❌ | {issue} |
| O - 开放封闭 | ✅/⚠️/❌ | {issue} |
| L - 里氏替换 | ✅/⚠️/❌ | {issue} |
| I - 接口隔离 | ✅/⚠️/❌ | {issue} |
| D - 依赖倒置 | ✅/⚠️/❌ | {issue} |

### 复杂度指标
| 文件 | 圈复杂度 | 方法数 | 最长方法行数 | 评价 |
| {file} | {cc} | {methods} | {max_lines} | {rating} |

---

## 改进建议汇总

### 高优先级（需立即修复）
1. {建议1}
2. {建议2}

### 中优先级（下个迭代修复）
1. {建议1}

### 低优先级（后续优化）
1. {建议1}

---

## 下一步行动
| 行动项 | 负责人 | 时间 | 状态 |
| 修复严重问题 | {owner} | {time} | 待处理 |
| 修复重要问题 | {owner} | {time} | 待处理 |
| 重新审查 | {reviewer} | {time} | 待安排 |

---

## 参考资料
- [OWASP Top 10](https://owasp.org/Top10/)
- [Clean Code Principles](https://www.oreilly.com/library/view/clean-code/)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)

```


## 检查清单


### before_review


- **item**: 审查目标已明确
- **check**: 检查review_target参数

- **item**: 技术栈规则已加载
- **check**: 检查tech_stack规则文件

- **item**: 审查范围已确定
- **check**: 检查review_type和focus_areas

### during_review


- **item**: 安全检查完整
- **check**: OWASP Top 10全覆盖

- **item**: 性能检查完整
- **check**: 数据库/内存/并发全覆盖

- **item**: 质量检查完整
- **check**: Clean Code/SOLID全覆盖

- **item**: 问题分级正确
- **check**: severity分级符合规范

### after_review


- **item**: 报告结构完整
- **check**: 所有章节已填写

- **item**: 修复建议具体
- **check**: 每个问题有修复建议

- **item**: 评分计算准确
- **check**: 评分公式验证

- **item**: 审查结论明确
- **check**: 通过/需修改/需重审

## 质量标准


- **standard**: 安全审查覆盖率
- **requirement**: OWASP Top 10 100%覆盖
- **check**: 检查OWASP检查项

- **standard**: 问题检出准确率
- **requirement**: ≥ 85%
- **check**: 人工抽样验证

- **standard**: 修复建议有效性
- **requirement**: ≥ 90%
- **check**: 开发者反馈

- **standard**: 审查报告完整性
- **requirement**: 100%
- **check**: 检查所有章节

## rules


### security


### critical


- **id**: SEC-001
- **name**: SQL注入
- **pattern**: (SELECT|INSERT|UPDATE|DELETE).*\+.*request
- **description**: 检测SQL拼接导致的注入风险
- **fix**: 使用参数化查询或ORM框架
- **reference**: OWASP A03

- **id**: SEC-002
- **name**: XSS跨站脚本
- **pattern**: response\.write.*request|innerHTML.*request
- **description**: 检测未转义的输出导致的XSS风险
- **fix**: 使用HTML转义函数处理输出
- **reference**: OWASP A03

- **id**: SEC-003
- **name**: 硬编码密码
- **pattern**: password.*=.*".*"|secret.*=.*".*"
- **description**: 检测硬编码的密码或密钥
- **fix**: 使用环境变量或密钥管理服务
- **reference**: OWASP A02

### major


- **id**: SEC-004
- **name**: 缺少权限检查
- **pattern**: @GetMapping.*public.*void
- **description**: 检测公开接口缺少权限注解
- **fix**: 添加权限注解或权限检查逻辑
- **reference**: OWASP A01

### performance


### major


- **id**: PERF-001
- **name**: N+1查询
- **pattern**: for.*\{.*repository\.find.*\}
- **description**: 检测循环中的数据库查询
- **fix**: 使用批量查询或JOIN
- **reference**: 数据库优化指南

- **id**: PERF-002
- **name**: 缺少事务
- **pattern**: @Transactional.*missing
- **description**: 检测多数据库操作缺少事务
- **fix**: 添加@Transactional注解
- **reference**: 事务管理指南

### warning


- **id**: PERF-003
- **name**: 大对象创建
- **pattern**: new.*\[.*100000.*\]|ArrayList.*100000
- **description**: 检测大数组或集合创建
- **fix**: 考虑分批处理或流式处理
- **reference**: 内存优化指南

### quality


### warning


- **id**: QUAL-001
- **name**: 过长方法
- **pattern**: method.*lines.*>.*50
- **description**: 检测超过50行的方法
- **fix**: 拆分为多个小方法
- **reference**: Clean Code原则

- **id**: QUAL-002
- **name**: 高圈复杂度
- **pattern**: cyclomatic.*>.*10
- **description**: 检测圈复杂度超过10的方法
- **fix**: 简化条件逻辑或提取方法
- **reference**: 复杂度控制指南

- **id**: QUAL-003
- **name**: 代码重复
- **pattern**: duplicate.*block.*>.*10.*lines
- **description**: 检测10行以上重复代码
- **fix**: 提取公共方法或组件
- **reference**: DRY原则

## 参考文档


### methodology


- **name**: OWASP Top 10
- **description**: Web应用安全风险标准
- **url**: https://owasp.org/Top10/

- **name**: Clean Code
- **description**: 代码质量原则

- **name**: SOLID原则
- **description**: 面向对象设计原则

- **name**: ISO 25010
- **description**: 软件产品质量模型

### primary


- **path**: 研发/references/代码评审/code-review.md
- **description**: 代码审查标准

- **path**: 安全/references/安全审查/checklist.md
- **description**: 安全审查检查清单

## 协作关系


### upstream


- **skill**: implement
- **relationship**: 提供代码变更
- **condition**: 代码实现完成后

### downstream


- **skill**: security-code-review
- **relationship**: 深度安全审查
- **condition**: 发现安全问题时

- **skill**: test-executor
- **relationship**: 测试验证
- **condition**: 代码修改后

## 使用示例


- **name**: Java代码审查
- **input_summary**: UserService.java - 新增用户注册功能
- **output_summary**: 
```
## 审查摘要
- 审查文件: UserService.java
- 代码行数: 120行
- 问题总数: 5个
  - 🔴 严重: 1个
  - 🟠 重要: 2个
  - 🟡 警告: 2个

## 质量评分
| 维度 | 评分 |
| 安全性 | 6/10 |
| 性能 | 8/10 |
| 可读性 | 9/10 |
| 综合评分 | 7.5/10 |

## 严重问题
🔴 SEC-003: 硬编码密码
- 文件: UserService.java
- 行号: 15
- 问题: String password = "admin123"
- 修复: 使用环境变量 PASSWORD_ENV
- 参考: OWASP A02

## 重要问题
🟠 PERF-001: N+1查询
- 文件: UserService.java
- 行号: 45-50
- 问题: 循环中调用findById
- 修复: 使用findAllById批量查询

🟠 SEC-004: 缺少权限检查
- 文件: UserService.java
- 行号: 25
- 问题: deleteUser方法缺少权限注解
- 修复: 添加@PreAuthorize("hasRole('ADMIN')")

## 审查结论
⚠️ 需修改 - 严重安全问题必须修复后方可合并

```


## 注意事项

- 审查报告需开发者在24小时内响应
- 严重问题必须修复后方可合并代码
- 审查规则需定期更新以适应新威胁
- 建议使用自动化工具辅助审查
- 审查需关注代码变更的整体影响

## metadata

- **created_at**: 2026-06-11
- **updated_at**: 2026-06-11
- **author**: Claude Agent

### version_history


- **version**: 1.0.0
- **date**: 2026-03-20
- **changes**: 初始版本

- **version**: 2.0.0
- **date**: 2026-06-11
- **changes**: 基于OWASP/Clean Code/SOLID重构，新增四维度审查