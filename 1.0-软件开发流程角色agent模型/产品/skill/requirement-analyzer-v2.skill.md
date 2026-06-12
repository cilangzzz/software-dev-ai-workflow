# 需求分析专家

## 基本信息

- **ID**: requirement-analyzer-v2
- **名称**: 需求分析专家
- **版本**: 2.0.0
- **分类**: analysis
- **部门**: 产品部
- **描述**: 专业需求分析工具，采用业界标准方法论（INVEST、MoSCoW、RICE优先级），将模糊需求转化为结构化PRD文档。支持业务需求、用户需求、功能需求三层分析。


## 触发条件


### commands

- /requirement-analyzer
- /需求分析

### keywords

- 分析需求
- 整理需求
- 生成PRD
- 需求文档
- 产品需求

### patterns

- 帮我分析.*需求
- 这个需求.*怎么处理
- 需求.*PRD

## 输入参数


### parameters


- **name**: requirement_text
- **type**: string
- **required**: True
- **description**: 原始需求描述文本
- **validation**: - **min_length**: 10

### examples

- 用户反馈：希望能在手机上查看订单状态
- 业务需求：实现采购审批流程自动化

- **name**: business_context
- **type**: string
- **required**: False
- **default**: 
- **description**: 业务背景信息（行业、用户群体、业务目标）

- **name**: analysis_depth
- **type**: string
- **required**: False
- **default**: full
- **enum**: - quick
- standard
- full
- **description**: 分析深度：quick(快速提取)、standard(标准分析)、full(完整分析)

- **name**: output_format
- **type**: string
- **required**: False
- **default**: prd
- **enum**: - prd
- brd
- user_story
- all
- **description**: 输出格式选择

## 工作流程

- **description**: 三层需求分析流程，确保需求完整性和可追溯性

### phases


- **name**: 需求采集
- **description**: 收集和整理原始需求信息
- **duration**: 5-10分钟
- **steps**: 
- **step**: 需求文本解析
- **action**: 分析输入文本，识别关键信息
- **output**: 需求点列表

- **step**: 需求来源标记
- **action**: 标记需求来源（用户反馈/业务目标/技术改进）
- **reference**: 需求分类标准

- **step**: 初步优先级判断
- **action**: 使用MoSCoW方法初步分类
- **checklist**: 需求完整性检查

- **name**: 需求分析
- **description**: 深入分析需求内涵和关联
- **duration**: 15-30分钟
- **steps**: 
- **step**: 业务需求提取
- **action**: 识别业务目标和价值
- **method**: 价值链分析
- **output**: BRD要点

- **step**: 用户需求转化
- **action**: 转化为用户视角的需求
- **method**: 用户故事映射
- **reference**: INVEST原则

- **step**: 功能需求分解
- **action**: 拆解为具体功能点
- **method**: 功能分解树
- **output**: 功能列表

- **step**: 需求关系分析
- **action**: 识别依赖、冲突、重复
- **output**: 需求关系图

- **name**: 需求文档化
- **description**: 生成结构化需求文档
- **duration**: 10-20分钟
- **steps**: 
- **step**: PRD框架生成
- **action**: 生成PRD文档框架
- **template**: prd-template

- **step**: 验收标准定义
- **action**: 编写Gherkin格式验收标准
- **reference**: BDD规范

- **step**: 优先级评分
- **action**: 使用RICE模型计算优先级
- **formula**: RICE = Reach × Impact × Confidence / Effort

- **step**: 澄清问题生成
- **action**: 生成待确认问题清单
- **output**: 问题清单

## 输出产物

- **base_path**: 产品/产出物/{project_name}/需求阶段/

### artifacts


- **name**: PRD文档
- **files**: - PRD-{feature_name}.md
- **format**: markdown
- **description**: 完整的产品需求文档
- **required**: True

- **name**: 需求清单
- **files**: - 需求清单-{date}.xlsx
- **format**: excel
- **description**: 需求点列表，含优先级评分
- **required**: True

- **name**: 用户故事集
- **files**: - 用户故事-{feature_name}.md
- **format**: markdown
- **description**: 符合INVEST原则的用户故事
- **required**: False

- **name**: 澄清问题清单
- **files**: - 待确认问题-{date}.md
- **format**: markdown
- **description**: 待与业务方确认的问题
- **required**: True

## templates

- **prd_template**: 
```
# 产品需求文档 (PRD)

## 文档信息
| 项目名称 | {project_name} |
| 文档编号 | PRD-{number} |
| 版本 | v1.0 |
| 创建日期 | {date} |
| 创建人 | {author} |
| 状态 | 草稿/评审中/已批准 |

---

## 1. 需求概述
### 1.1 需求背景
{需求来源、业务背景、问题描述}

### 1.2 需求目标
| 目标类型 | 目标描述 | 衡量指标 |
| 业务目标 | {goal} | {metric} |
| 用户目标 | {goal} | {metric} |

### 1.3 预期收益
- **直接收益**: {收益描述}
- **间接收益**: {收益描述}

---

## 2. 用户分析
### 2.1 目标用户
| 用户角色 | 用户特征 | 使用场景 | 占比 |
| {role} | {特征} | {场景} | {percent}% |

### 2.2 用户痛点
| 痛点编号 | 痛点描述 | 影响程度 | 当前解决方案 |
| P1 | {痛点} | 高/中/低 | {方案} |

### 2.3 用户故事 (User Stories)
格式：作为 {角色}，我想要 {功能}，以便于 {价值}

| 故事编号 | 用户故事 | 验收条件 | 优先级 |
| US-001 | {story} | {criteria} | MoSCoW |

---

## 3. 功能需求
### 3.1 功能概览
| 功能编号 | 功能名称 | 功能描述 | 优先级 | RICE评分 |
| F-001 | {name} | {desc} | Must | {score} |

### 3.2 功能详情

#### F-001: {功能名称}
**功能描述**: {详细描述}

**业务规则**:
- 规则1: {规则描述}
- 规则2: {规则描述}

**输入输出**:
| 输入 | 输出 | 说明 |
| {input} | {output} | {note} |

**边界条件**:
- 条件1: {边界描述}
- 条件2: {边界描述}

**异常处理**:
| 异常场景 | 处理方式 | 用户提示 |
| {场景} | {处理} | {提示} |

---

## 4. 非功能需求
### 4.1 性能需求
| 指标 | 要求 | 测试方法 |
| 响应时间 | < {n}ms | {method} |
| 并发用户 | ≥ {n} | {method} |
| 数据量 | ≤ {n}条 | {method} |

### 4.2 安全需求
- 认证要求: {要求描述}
- 权限控制: {要求描述}
- 数据安全: {要求描述}

### 4.3 兼容性需求
- 浏览器: {支持的浏览器版本}
- 设备: {支持的设备类型}
- 系统: {支持的系统版本}

---

## 5. 验收标准
### 5.1 功能验收
采用Gherkin格式 (Given-When-Then):

```gherkin
场景: {场景名称}
  Given {前置条件}
  When {触发动作}
  Then {预期结果}
  And {附加条件}
```

### 5.2 验收检查清单
| 检查项 | 验收标准 | 检查方式 |
| 功能完整性 | 100%功能实现 | 功能测试 |
| 性能达标 | 符合性能要求 | 性能测试 |

---

## 6. 待澄清问题
| 问题编号 | 问题描述 | 提问对象 | 优先级 | 状态 |
| Q-001 | {问题} | {对象} | 高 | 待确认 |

---

## 7. 附录
### 7.1 参考资料
- {参考文档链接}

### 7.2 术语表
| 术语 | 定义 |
| {term} | {definition} |

```

- **user_story_template**: 
```
# 用户故事集

## 故事编号: US-{number}

### 基本信息
- **优先级**: MoSCoW - {Must/Should/Could/Won't}
- **故事点**: {估算值}
- **所属Epic**: {Epic名称}

### 用户故事
**作为** {用户角色}
**我想要** {功能/操作}
**以便于** {业务价值}

### 验收条件 (Acceptance Criteria)
采用Gherkin格式:

```gherkin
场景: {场景名称}
  Given {前置条件}
  When {用户操作}
  Then {预期结果}
```

### INVEST检查
| 检查项 | 是否符合 | 说明 |
| Independent | ✓/✗ | {说明} |
| Negotiable | ✓/✗ | {说明} |
| Valuable | ✓/✗ | {说明} |
| Estimable | ✓/✗ | {说明} |
| Small | ✓/✗ | {说明} |
| Testable | ✓/✗ | {说明} |

### 依赖关系
- 上游依赖: {依赖故事编号}
- 下游影响: {影响故事编号}

```


## 检查清单


### before_analysis


- **item**: 需求来源已明确
- **check**: 检查是否标注来源类型

- **item**: 业务背景已收集
- **check**: 检查business_context参数

- **item**: 分析深度已确定
- **check**: 检查analysis_depth参数

### during_analysis


- **item**: 所有需求点已识别
- **check**: 需求覆盖率 ≥ 95%

- **item**: 优先级已评估
- **check**: 使用RICE模型评分

- **item**: 依赖关系已分析
- **check**: 绘制需求关系图

- **item**: 冲突已识别
- **check**: 列出冲突需求清单

### after_analysis


- **item**: PRD结构完整
- **check**: 检查所有章节已填写

- **item**: 用户故事符合INVEST
- **check**: 逐项验证INVEST原则

- **item**: 验收标准可执行
- **check**: Gherkin格式验证

- **item**: 澄清问题已生成
- **check**: 问题清单完整性

## 质量标准


- **standard**: 需求覆盖率
- **requirement**: ≥ 95%
- **check**: 统计需求点 vs 输入文本关键信息

- **standard**: INVEST符合度
- **requirement**: 100%
- **check**: 逐项检查用户故事

- **standard**: 歧义检测准确率
- **requirement**: ≥ 80%
- **check**: 人工抽样验证

- **standard**: 澄清问题相关性
- **requirement**: ≥ 90%
- **check**: 业务方确认比例

- **standard**: 优先级评分合理性
- **requirement**: 与业务方共识 ≥ 80%
- **check**: 评审会议确认

## 参考文档


### primary


- **path**: 产品/references/prd-template.md
- **description**: PRD标准模板

- **path**: 产品/references/user-story-guide.md
- **description**: 用户故事编写指南

### methodology


- **name**: INVEST原则
- **description**: 用户故事质量评估标准
- **url**: https://www.agilealliance.org/

- **name**: MoSCoW优先级
- **description**: 需求优先级分类方法

- **name**: RICE评分模型
- **description**: Reach × Impact × Confidence / Effort

## 协作关系


### upstream


- **skill**: business-rule-analyzer
- **relationship**: 输入业务规则
- **condition**: 涉及复杂业务逻辑时

### downstream


- **skill**: user-story-generator
- **relationship**: 提供需求基础
- **condition**: 需求分析完成后

- **skill**: acceptance-criteria-writer
- **relationship**: 提供功能需求
- **condition**: PRD生成后

- **skill**: requirement-review
- **relationship**: 评审需求文档
- **condition**: 文档完成后

## 使用示例


- **name**: 用户反馈分析
- **input**: 
```
用户反馈：希望能在手机上查看订单状态，有时候在外面也需要确认订单走到哪一步了，
还有就是支付的时候老是报错，特别是用微信支付的时候。

```

- **output_summary**: 
```
## 需求概述
用户需要在移动端查看订单状态，并解决微信支付报错问题。

## 用户故事 (符合INVEST)
US-001: 作为外出用户，我希望能在手机上查看订单状态，以便随时了解订单进度
US-002: 作为支付用户，我希望微信支付能正常工作，以便顺利完成订单

## 功能需求
F-001: 移动端订单状态查询页面 [Must] RICE=8.5
F-002: 订单进度实时更新功能 [Should] RICE=6.2
F-003: 微信支付异常修复 [Must] RICE=12.0

## 优先级排序 (RICE)
1. 微信支付异常修复 (RICE=12.0) - 影响交易，优先处理
2. 移动端订单查询 (RICE=8.5)
3. 实时进度更新 (RICE=6.2)

## 待澄清问题
Q-001: 订单状态具体包含哪些节点？
Q-002: 微信支付报错的具体错误信息是什么？
Q-003: 是否需要推送通知功能？

```


- **name**: 业务需求分析
- **input**: 
```
业务需求：实现采购审批流程自动化。当前采购审批需要人工流转，
审批周期长，容易出错，需要实现多级审批、自动流转、超时提醒功能。

```

- **output_summary**: 
```
## 需求概述
实现采购审批流程自动化，提升审批效率，减少人为错误。

## 业务目标
- 审批周期缩短50%
- 审批错误率降低90%
- 审批可追溯性100%

## 功能需求
F-001: 多级审批配置 [Must]
F-002: 自动流转引擎 [Must]
F-003: 超时提醒机制 [Should]
F-004: 审批记录追溯 [Must]

## 业务规则
- BR-001: 采购金额<5000元，一级审批
- BR-002: 采购金额5000-50000元，二级审批
- BR-003: 采购金额>50000元，三级审批
- BR-004: 审批超时24小时，自动提醒
- BR-005: 审批超时48小时，自动升级

```


## 注意事项

- AI生成的PRD需要人工审核和补充
- 澄清问题必须与业务方确认后再进入开发
- 优先级建议仅供参考，需结合业务实际情况调整
- 用户故事需符合INVEST原则
- 验收标准采用Gherkin格式，便于自动化测试
- 复杂业务规则需调用 business-rule-analyzer
- 需求变更需记录版本历史

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
- **changes**: 基于业界最佳实践重构，新增INVEST检查、RICE评分、完整检查清单