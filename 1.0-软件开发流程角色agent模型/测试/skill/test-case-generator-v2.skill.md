# 测试用例生成专家

## 基本信息

- **ID**: test-case-generator-v2
- **名称**: 测试用例生成专家
- **版本**: 2.0.0
- **分类**: testing
- **部门**: 测试部
- **描述**: 专业测试用例生成工具，基于ISTQB测试方法论，采用边界值分析、等价类划分、决策表、状态迁移等测试设计技术，生成完整可执行的测试用例。


## 触发条件


### commands

- /test-case-generator
- /测试用例
- /tcg

### keywords

- 生成测试用例
- 测试用例设计
- 编写测试用例
- 测试设计

### patterns

- 帮我生成.*测试用例
- 设计.*测试用例

## 输入参数


### parameters


- **name**: requirement_source
- **type**: string
- **required**: True
- **description**: 需求来源（PRD文档、功能规格、用户故事）
- **examples**: - 产品/产出物/订单系统/需求阶段/PRD-订单模块.md
- US-001: 用户登录功能

- **name**: test_level
- **type**: string
- **required**: False
- **default**: system
- **enum**: - unit
- integration
- system
- acceptance
- all
- **description**: 测试层级选择

- **name**: test_techniques
- **type**: array
- **required**: False
- **default**: - all
- **items**: - boundary
- equivalence
- decision_table
- state_transition
- use_case
- error_guessing
- all
- **description**: 测试设计技术选择

- **name**: coverage_target
- **type**: object
- **required**: False
- **default**: 
- **description**: 覆盖率目标
- **properties**: - **functional**: 功能覆盖率目标（默认100%）
- **boundary**: 边界覆盖率目标（默认100%）
- **exception**: 异常覆盖率目标（默认80%）

## 工作流程

- **description**: 系统化测试用例设计流程，确保测试覆盖完整

### phases


- **name**: 需求分析
- **description**: 分析需求，提取测试对象
- **duration**: 10-15分钟
- **steps**: 
- **step**: 需求文档解析
- **action**: 读取需求文档，提取功能点
- **output**: 功能清单

- **step**: 测试对象识别
- **action**: 识别需要测试的功能、接口、数据
- **output**: 测试对象清单

- **step**: 测试范围确定
- **action**: 确定测试范围和边界
- **output**: 测试范围矩阵

- **step**: 风险评估
- **action**: 识别高风险测试区域
- **method**: 风险矩阵分析
- **output**: 风险测试重点

- **name**: 测试设计
- **description**: 应用测试设计技术生成测试用例
- **duration**: 30-60分钟
- **steps**: 
- **step**: 等价类划分
- **action**: 识别有效/无效等价类
- **method**: ISTQB等价类划分
- **output**: 等价类矩阵

- **step**: 边界值分析
- **action**: 识别边界点和边界值
- **method**: 边界值分析方法
- **output**: 边界值测试用例

- **step**: 决策表设计
- **action**: 设计条件-动作组合
- **method**: 决策表技术
- **output**: 决策表测试用例

- **step**: 状态迁移设计
- **action**: 设计状态流转测试
- **method**: 状态迁移图
- **condition**: 有状态变化的功能
- **output**: 状态迁移测试用例

- **step**: 用例场景设计
- **action**: 设计用户场景测试
- **method**: 用例测试技术
- **output**: 场景测试用例

- **step**: 错误猜测
- **action**: 基于经验猜测错误场景
- **method**: 错误猜测技术
- **output**: 错误场景测试用例

- **name**: 用例优化
- **description**: 优化和整合测试用例
- **duration**: 15-30分钟
- **steps**: 
- **step**: 用例合并
- **action**: 合并重复或相似用例
- **output**: 优化后用例集

- **step**: 优先级排序
- **action**: 按风险和重要性排序
- **method**: 风险优先级排序
- **output**: 优先级用例列表

- **step**: 覆盖率验证
- **action**: 验证测试覆盖率达标
- **checklist**: 覆盖率检查清单

- **step**: 用例编号
- **action**: 分配唯一用例编号
- **format**: TC-{模块}-{功能}-{序号}

- **name**: 用例文档化
- **description**: 生成标准化测试用例文档
- **duration**: 10-20分钟
- **steps**: 
- **step**: 用例表格生成
- **action**: 生成测试用例表格
- **template**: test-case-table-template

- **step**: 前置条件编写
- **action**: 编写测试前置条件
- **output**: 前置条件清单

- **step**: 测试数据准备
- **action**: 定义测试数据需求
- **output**: 测试数据清单

- **step**: 预期结果定义
- **action**: 定义明确的预期结果
- **output**: 预期结果清单

## 输出产物

- **base_path**: 测试/产出物/{project_name}/测试阶段/

### artifacts


- **name**: 测试用例文档
- **files**: - 测试用例-{module_name}.xlsx
- **format**: excel
- **description**: 完整的测试用例表格
- **required**: True

- **name**: 测试设计文档
- **files**: - 测试设计-{module_name}.md
- **format**: markdown
- **description**: 测试设计方法和分析过程
- **required**: True

- **name**: 测试数据清单
- **files**: - 测试数据-{module_name}.xlsx
- **format**: excel
- **description**: 测试所需的数据准备清单
- **required**: False

- **name**: 覆盖率报告
- **files**: - 覆盖率报告-{module_name}.md
- **format**: markdown
- **description**: 测试覆盖率分析报告
- **required**: True

## templates

- **test_case_table_template**: 
```
# 测试用例文档

## 文档信息
| 项目名称 | {project_name} |
| 模块名称 | {module_name} |
| 文档编号 | TC-{module}-{number} |
| 版本 | v1.0 |
| 创建日期 | {date} |
| 创建人 | {author} |
| 状态 | 草稿/评审中/已批准 |

---

## 1. 测试范围
| 功能编号 | 功能名称 | 测试层级 | 优先级 | 用例数 |
| F-001 | {name} | {level} | P0/P1/P2 | {count} |

---

## 2. 测试设计方法
| 方法 | 应用功能 | 生成用例数 | 说明 |
| 等价类划分 | {feature} | {count} | {note} |
| 边界值分析 | {feature} | {count} | {note} |
| 决策表 | {feature} | {count} | {note} |
| 状态迁移 | {feature} | {count} | {note} |

---

## 3. 测试用例列表

### 3.1 功能测试用例

| 用例编号 | 用例名称 | 优先级 | 前置条件 | 测试步骤 | 测试数据 | 预期结果 | 设计方法 |
| TC-001-001 | {name} | P0 | {precondition} | {steps} | {data} | {expected} | {method} |

#### 用例详情: TC-001-001
**用例名称**: {完整用例名称}

**优先级**: P0 - 核心功能，必须通过

**前置条件**:
1. {前置条件1}
2. {前置条件2}

**测试步骤**:
| 步骤 | 操作 | 输入 | 预期结果 |
| 1 | {action} | {input} | {expected} |
| 2 | {action} | {input} | {expected} |

**测试数据**:
| 数据项 | 值 | 说明 |
| {field} | {value} | {note} |

**预期结果**:
- 界面结果: {界面预期}
- 数据结果: {数据预期}
- 系统状态: {状态预期}

**设计方法**: 等价类划分 - 有效等价类

---

### 3.2 边界值测试用例

| 用例编号 | 用例名称 | 边界类型 | 边界值 | 测试步骤 | 预期结果 |
| TC-001-BV-001 | {name} | 最小值/最大值/刚好边界/刚好超出 | {value} | {steps} | {expected} |

---

### 3.3 异常测试用例

| 用例编号 | 用例名称 | 异常类型 | 测试场景 | 预期处理 |
| TC-001-EX-001 | {name} | 输入异常/业务异常/系统异常 | {scenario} | {handling} |

---

### 3.4 状态迁移测试用例

| 用例编号 | 用例名称 | 起始状态 | 触发动作 | 预期状态 | 验证点 |
| TC-001-ST-001 | {name} | {from_state} | {action} | {to_state} | {verify} |

---

## 4. 测试数据需求

| 数据编号 | 数据名称 | 数据类型 | 数据值 | 来源 | 准备方式 |
| TD-001 | {name} | 正常/边界/异常 | {values} | 手动/自动 | {method} |

---

## 5. 覆盖率分析

| 覆盖类型 | 覆盖项 | 用例覆盖数 | 覆盖率 | 达标情况 |
| 功能覆盖 | {feature} | {count} | {rate} | ✅/❌ |
| 边界覆盖 | {boundary} | {count} | {rate} | ✅/❌ |
| 异常覆盖 | {exception} | {count} | {rate} | ✅/❌ |

---

## 6. 测试环境需求

| 环境类型 | 配置要求 | 说明 |
| 测试环境 | {config} | {note} |
| 数据库 | {config} | {note} |
| 测试工具 | {tool} | {note} |

---

## 7. 附录

### 7.1 等价类划分表
| 输入项 | 有效等价类 | 无效等价类 | 用例覆盖 |
| {field} | {valid} | {invalid} | TC-{number} |

### 7.2 决策表
| 条件1 | 条件2 | 条件3 | 动作 | 用例编号 |
| Y/N | Y/N | Y/N | {action} | TC-{number} |

### 7.3 状态迁移图
{状态迁移图描述}

```

- **test_design_doc_template**: 
```
# 测试设计文档

## 1. 测试对象分析

### 1.1 功能分解
| 功能编号 | 功能名称 | 子功能 | 输入项 | 输出项 | 风险等级 |
| F-001 | {name} | {sub} | {inputs} | {outputs} | 高/中/低 |

### 1.2 输入输出分析
| 输入项 | 数据类型 | 取值范围 | 必填性 | 来源 |
| {field} | {type} | {range} | 必填/可选 | {source} |

### 1.3 业务规则分析
| 规则编号 | 规则描述 | 影响功能 | 测试影响 |
| BR-001 | {rule} | {feature} | {impact} |

---

## 2. 等价类划分分析

### 2.1 输入等价类
| 输入项 | 有效等价类（编号） | 无效等价类（编号） |
| 用户名 | EC1: 6-20字符 | EC2: <6字符, EC3: >20字符, EC4: 特殊字符 |

### 2.2 等价类测试用例映射
| 用例编号 | 等价类覆盖 | 测试数据 |
| TC-001 | EC1 | username="testuser" |
| TC-002 | EC2 | username="abc" |

---

## 3. 边界值分析

### 3.1 边界识别
| 输入项 | 最小边界 | 最大边界 | 边界类型 |
| 用户名长度 | 6 | 20 | 长度边界 |

### 3.2 边界值测试点
| 输入项 | 边界点 | 测试值 | 用例编号 |
| 用户名长度 | 最小值-1 | 5字符 | TC-BV-001 |
| 用户名长度 | 最小值 | 6字符 | TC-BV-002 |
| 用户名长度 | 最小值+1 | 7字符 | TC-BV-003 |
| 用户名长度 | 最大值-1 | 19字符 | TC-BV-004 |
| 用户名长度 | 最大值 | 20字符 | TC-BV-005 |
| 用户名长度 | 最大值+1 | 21字符 | TC-BV-006 |

---

## 4. 决策表分析

### 4.1 条件识别
| 条件编号 | 条件名称 | 取值 |
| C1 | 用户类型 | 普通/VIP/企业 |
| C2 | 订单金额 | <1000/1000-5000/>5000 |

### 4.2 动作识别
| 动作编号 | 动作名称 |
| A1 | 无折扣 |
| A2 | 5%折扣 |
| A3 | 10%折扣 |

### 4.3 决策表
| 规则 | C1 | C2 | 动作 |
| R1 | 普通 | <1000 | A1 |
| R2 | 普通 | 1000-5000 | A2 |
| R3 | VIP | 任意 | A2 |
| R4 | 企业 | >5000 | A3 |

---

## 5. 状态迁移分析

### 5.1 状态识别
| 状态编号 | 状态名称 | 状态描述 |
| S1 | 待支付 | 订单创建，等待支付 |
| S2 | 已支付 | 支付完成，等待发货 |
| S3 | 已发货 | 商品已发出 |
| S4 | 已完成 | 用户已签收 |
| S5 | 已取消 | 订单取消 |

### 5.2 状态迁移表
| 起始状态 | 触发事件 | 目标状态 | 前置条件 | 用例编号 |
| S1 | 支付成功 | S2 | 支付金额正确 | TC-ST-001 |
| S1 | 取消订单 | S5 | 未支付 | TC-ST-002 |
| S2 | 发货 | S3 | 有库存 | TC-ST-003 |
| S3 | 签收 | S4 | 配送完成 | TC-ST-004 |

---

## 6. 测试覆盖矩阵

| 测试对象 | 等价类 | 边界值 | 决策表 | 状态迁移 | 异常场景 | 合计 |
| 登录功能 | 3 | 4 | - | - | 2 | 9 |
| 订单功能 | 5 | 6 | 4 | 5 | 3 | 23 |

```


## 检查清单


### before_design


- **item**: 需求文档已评审
- **check**: 确认需求状态为已批准

- **item**: 测试范围已确定
- **check**: 检查test_level参数

- **item**: 测试技术已选择
- **check**: 检查test_techniques参数

### during_design


- **item**: 等价类划分完整
- **check**: 所有输入项都有等价类

- **item**: 边界值识别准确
- **check**: 边界点正确识别

- **item**: 决策表覆盖完整
- **check**: 所有条件组合覆盖

- **item**: 状态迁移覆盖完整
- **check**: 所有状态流转覆盖

- **item**: 异常场景考虑充分
- **check**: 异常覆盖率 ≥ 80%

### after_design


- **item**: 用例编号规范
- **check**: TC-{模块}-{功能}-{序号}格式

- **item**: 前置条件明确
- **check**: 每个用例有前置条件

- **item**: 预期结果明确
- **check**: 预期结果可验证

- **item**: 覆盖率达标
- **check**: 覆盖率检查清单

- **item**: 用例评审通过
- **check**: 测试评审会议

## 质量标准


- **standard**: 功能覆盖率
- **requirement**: 100%
- **check**: 所有功能点有测试用例

- **standard**: 边界覆盖率
- **requirement**: 100%
- **check**: 所有边界点有测试用例

- **standard**: 异常覆盖率
- **requirement**: ≥ 80%
- **check**: 异常场景测试比例

- **standard**: 用例质量
- **requirement**: 预期结果100%可验证
- **check**: 每个用例有明确预期

## 参考文档


### methodology


- **name**: ISTQB
- **description**: 国际软件测试认证委员会标准
- **url**: https://www.istqb.org/

- **name**: 边界值分析
- **description**: 边界测试设计技术

- **name**: 等价类划分
- **description**: 等价类测试设计技术

- **name**: 决策表测试
- **description**: 条件组合测试技术

### primary


- **path**: 测试/references/test-design-guide.md
- **description**: 测试设计指南

- **path**: 测试/references/test-case-template.xlsx
- **description**: 测试用例模板

## 协作关系


### upstream


- **skill**: requirement-analyzer
- **relationship**: 提供PRD文档
- **condition**: 需求分析完成后

- **skill**: acceptance-criteria-writer
- **relationship**: 提供验收标准
- **condition**: 验收标准定义后

### downstream


- **skill**: test-executor
- **relationship**: 执行测试用例
- **condition**: 用例生成后

- **skill**: bug-analyzer
- **relationship**: 分析发现的Bug
- **condition**: 测试执行后

## 使用示例


- **name**: 用户登录功能测试用例
- **input_summary**: US-001: 用户登录功能，用户名6-20字符，密码8-16字符
- **output_summary**: 
```
## 测试用例总数: 15个

### 等价类划分（6个）
| 用例编号 | 用例名称 | 测试数据 | 预期结果 |
| TC-LOGIN-001 | 有效登录 | username="testuser", password="testpass123" | 登录成功 |
| TC-LOGIN-002 | 用户名过短 | username="abc", password="testpass123" | 提示用户名长度错误 |
| TC-LOGIN-003 | 用户名过长 | username="abcdefghijklmnopqrst", password="testpass123" | 提示用户名长度错误 |
| TC-LOGIN-004 | 密码过短 | username="testuser", password="abc" | 提示密码长度错误 |
| TC-LOGIN-005 | 密码过长 | username="testuser", password="abcdefghijklmnop" | 提示密码长度错误 |
| TC-LOGIN-006 | 用户名不存在 | username="notexist", password="testpass123" | 提示用户不存在 |

### 边界值测试（8个）
| 用例编号 | 边界类型 | 测试数据 | 预期结果 |
| TC-LOGIN-BV-001 | 用户名最小值-1 | username="abcde"(5字符) | 登录失败 |
| TC-LOGIN-BV-002 | 用户名最小值 | username="abcdef"(6字符) | 登录成功 |
| TC-LOGIN-BV-003 | 用户名最大值 | username="abcdefghijklmnopqrst"(20字符) | 登录成功 |
| TC-LOGIN-BV-004 | 用户名最大值+1 | username="abcdefghijklmnopqrstu"(21字符) | 登录失败 |
| TC-LOGIN-BV-005 | 密码最小值-1 | password="abcdefg"(7字符) | 登录失败 |
| TC-LOGIN-BV-006 | 密码最小值 | password="abcdefgh"(8字符) | 登录成功 |
| TC-LOGIN-BV-007 | 密码最大值 | password="abcdefghijklmnop"(16字符) | 登录成功 |
| TC-LOGIN-BV-008 | 密码最大值+1 | password="abcdefghijklmnopq"(17字符) | 登录失败 |

### 异常场景（1个）
| 用例编号 | 异常类型 | 测试场景 | 预期结果 |
| TC-LOGIN-EX-001 | 系统异常 | 数据库连接失败 | 提示系统繁忙，请稍后重试 |

## 覆盖率分析
- 功能覆盖: 100%（登录功能）
- 边界覆盖: 100%（用户名/密码长度边界）
- 异常覆盖: 80%（网络异常、数据库异常）

```


## 注意事项

- 测试用例需经测试评审会议审核
- 边界值测试必须覆盖所有边界点
- 异常场景测试需要考虑系统异常
- 测试数据需提前准备
- 测试用例需持续维护和更新
- 复杂业务规则使用决策表设计

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
- **changes**: 基于ISTQB方法论重构，新增多种测试设计技术