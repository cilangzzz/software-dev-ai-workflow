# 需求采集专家

## 基本信息

- **ID**: requirement-researcher
- **名称**: 需求采集专家
- **版本**: 1.0.0
- **分类**: research
- **部门**: 产品部
- **描述**: 专业需求采集工具，通过Web搜索从互联网获取真实行业需求文档、招标文件、竞品功能清单、行业标准法规，将非结构化的行业信息提炼为结构化功能需求点文档。所有采集内容必须来自真实互联网来源，禁止模拟数据。


## 触发条件


### commands

- /requirement-researcher
- /需求采集
- /需求调研

### keywords

- 采集需求
- 需求调研
- 行业需求
- 竞品功能
- 功能清单
- 需求文档爬取
- 需求扩展
- 需求参考

### patterns

- 帮我.*采集.*需求
- 搜索.*行业.*需求文档
- 爬取.*需求文档
- 获取.*功能需求点
- 调研.*行业.*功能
- 我准备做.*系统.*需求

## 输入参数


### parameters


- **name**: domain
- **type**: string
- **required**: True
- **description**: 目标行业或业务领域（如：医疗HIS、制造业MES、电商、教育、物流等）
- **validation**: - **min_length**: 2

### examples

- 医疗HIS医院信息系统
- 制造业MES生产执行系统
- 在线教育平台

- **name**: system_type
- **type**: string
- **required**: False
- **default**: 
- **description**: 目标系统类型（如：管理系统、平台、APP、后台等）

- **name**: search_scope
- **type**: string
- **required**: False
- **default**: full
- **enum**: - requirement_doc
- competitive
- industry_standard
- full
- **description**: 采集范围：requirement_doc(需求文档)、competitive(竞品分析)、industry_standard(行业标准)、full(全部)

- **name**: depth
- **type**: string
- **required**: False
- **default**: standard
- **enum**: - quick
- standard
- deep
- **description**: 采集深度：quick(快速概览,5-10个需求点)、standard(标准采集,20-50个需求点)、deep(深度采集,50+需求点)

- **name**: language
- **type**: string
- **required**: False
- **default**: zh
- **enum**: - zh
- en
- both
- **description**: 搜索语言偏好：zh(中文优先)、en(英文优先)、both(双语)

## 工作流程

- **description**: 四阶段需求采集流程，确保采集内容真实、来源可追溯、需求点结构化

### phases


- **name**: 意图解析与搜索策略
- **description**: 解析用户需求意图，制定搜索关键词策略
- **duration**: 3-5分钟
- **steps**: 
- **step**: 需求意图解析
- **action**: 分析用户输入，提取目标行业、系统类型、关键业务领域
- **output**: 采集目标摘要

- **step**: 关键词策略生成
- **action**: 生成多维度搜索关键词组合
- **method**: 关键词矩阵法
- **output_format**: 
```
关键词维度：
- 行业关键词：{行业名}、{行业别名}、{英文名}
- 系统关键词：{系统类型}、{系统简称}
- 需求关键词：需求文档、功能清单、系统功能、招标文件
- 标准关键词：行业标准、国家标准、法规、合规
```

- **step**: 搜索源规划
- **action**: 确定搜索优先级和目标源类型
- **priority_order**: - 政府招标采购网站
- 行业标准数据库
- 竞品官方网站
- 技术社区和博客
- 学术论文和行业报告

- **name**: Web搜索与采集
- **description**: 通过Web搜索工具采集真实行业需求内容
- **duration**: 10-20分钟
- **steps**: 
- **step**: 行业需求文档搜索
- **action**: 搜索目标行业的需求文档、招标文件、系统功能说明书
- **tool**: WebSearch
- **search_queries**: 
```
查询模板：
- "{行业名} 系统 功能需求 文档"
- "{行业名} {系统类型} 招标文件 功能要求"
- "{行业名} 信息系统 需求规格说明书"
- "{行业名} 系统 功能模块 清单"
```
- **output**: 需求文档URL列表

- **step**: 竞品功能采集
- **action**: 搜索同类系统的功能介绍、产品手册、用户评价
- **tool**: WebSearch
- **search_queries**: 
```
查询模板：
- "{系统类型} 产品功能介绍"
- "{系统类型} 竞品 功能对比"
- "{系统类型} 解决方案 功能模块"
- "best {system_type} features modules"
```
- **output**: 竞品功能信息列表

- **step**: 行业标准搜索
- **action**: 搜索行业标准、法规要求、合规性文件
- **tool**: WebSearch
- **search_queries**: 
```
查询模板：
- "{行业名} 信息系统 国家标准"
- "{行业名} 行业标准 GB"
- "{行业名} 信息化 法规 合规要求"
- "{行业名} 数据标准 交换标准"
```
- **output**: 行业标准文档列表

- **step**: 内容抓取与验证
- **action**: 对搜索结果进行内容抓取，验证内容真实性和相关性
- **tool**: WebFetch
- **validation_rules**: - 内容必须来自可访问的真实URL
- 内容必须与目标行业/系统类型相关
- 内容必须包含具体的功能描述，而非泛泛而谈
- 优先采集带有明确功能列表、模块划分的内容

- **name**: 需求提炼与结构化
- **description**: 从采集的原始内容中提取功能需求点，分类整理
- **duration**: 15-25分钟
- **steps**: 
- **step**: 功能需求点提取
- **action**: 从采集的文档中提取具体的功能需求点
- **method**: 
```
提取规则：
- 识别功能模块名称和功能描述
- 提取业务规则和约束条件
- 识别数据实体和数据流转关系
- 提取用户角色和权限要求
```
- **output**: 功能需求点原始列表

- **step**: 需求点分类
- **action**: 按功能模块对需求点进行分类
- **categories**: 
```
分类维度：
- 按业务领域：核心业务、辅助业务、管理业务
- 按功能类型：增删改查、流程审批、报表统计、系统管理
- 按用户角色：管理员、操作员、查看者
- 按优先级：核心功能、重要功能、可选功能
```

- **step**: 需求点去重与合并
- **action**: 识别重复或相似的需求点，合并为统一描述
- **method**: 语义相似度比对

- **step**: 来源标注与可信度评级
- **action**: 为每个需求点标注来源URL和可信度
- **rating_criteria**: 
```
可信度评级：
- A级：政府招标文件、国家标准、行业权威机构发布
- B级：竞品官方网站、知名技术社区、行业报告
- C级：个人博客、论坛帖子、非官方文档
- D级：信息不完整或来源不明确（需交叉验证）
```

- **name**: 文档生成与交付
- **description**: 生成结构化的需求参考文档
- **duration**: 5-10分钟
- **steps**: 
- **step**: 需求参考文档生成
- **action**: 按模板生成结构化需求参考文档
- **template**: requirement-reference-template

- **step**: 竞品功能矩阵生成
- **action**: 生成竞品功能对比矩阵（如适用）
- **template**: competitive-matrix-template

- **step**: 来源清单生成
- **action**: 生成完整的来源清单，含URL和可信度
- **output**: 需求来源清单

- **step**: 质量检查
- **action**: 检查文档完整性、来源可追溯性、需求点覆盖率
- **checklist**: 文档质量检查清单

## 输出产物

- **base_path**: 产品/产出物/{project_name}/需求调研/

### artifacts


- **name**: 行业需求参考文档
- **files**: - 行业需求参考-{domain}-{date}.md
- **format**: markdown
- **description**: 从互联网采集并提炼的行业功能需求点文档，含来源引用
- **required**: True

- **name**: 竞品功能清单
- **files**: - 竞品功能清单-{system_type}-{date}.md
- **format**: markdown
- **description**: 同类系统的功能模块对比矩阵
- **required**: False
- **condition**: search_scope 包含 competitive 或 full

- **name**: 行业标准汇编
- **files**: - 行业标准汇编-{domain}-{date}.md
- **format**: markdown
- **description**: 行业标准、法规要求、合规性清单
- **required**: False
- **condition**: search_scope 包含 industry_standard 或 full

- **name**: 需求来源清单
- **files**: - 需求来源清单-{date}.md
- **format**: markdown
- **description**: 所有采集来源的URL、标题、可信度评级
- **required**: True

## templates


- **requirement_reference_template**: 
```
# 行业需求参考文档

## 文档信息
| 属性 | 值 |
|------|-----|
| 目标行业 | {domain} |
| 系统类型 | {system_type} |
| 采集日期 | {date} |
| 采集深度 | {depth} |
| 来源数量 | {source_count} |
| 需求点数量 | {requirement_count} |

---

## 1. 采集概述
### 1.1 采集目标
{用户原始需求描述}

### 1.2 采集范围
- 搜索关键词：{keywords_used}
- 搜索语言：{language}
- 采集来源数：{source_count}
- 有效需求点：{requirement_count}

### 1.3 来源分布
| 来源类型 | 数量 | 占比 |
|----------|------|------|
| 招标文件 | {n} | {percent}% |
| 行业标准 | {n} | {percent}% |
| 竞品官网 | {n} | {percent}% |
| 技术文档 | {n} | {percent}% |
| 其他 | {n} | {percent}% |

---

## 2. 功能需求点清单

### 2.1 核心业务功能

#### 模块：{module_name}
| 编号 | 功能需求点 | 描述 | 来源 | 可信度 |
|------|-----------|------|------|--------|
| REQ-001 | {功能名} | {功能描述} | {来源URL} | {A/B/C/D} |
| REQ-002 | {功能名} | {功能描述} | {来源URL} | {A/B/C/D} |

### 2.2 辅助业务功能
{同上格式}

### 2.3 系统管理功能
{同上格式}

### 2.4 报表与统计功能
{同上格式}

---

## 3. 业务角色与权限

| 角色名称 | 角色描述 | 核心权限 | 来源 |
|----------|----------|----------|------|
| {role} | {description} | {permissions} | {source} |

---

## 4. 业务规则汇总

| 编号 | 业务规则 | 所属模块 | 来源 | 可信度 |
|------|---------|----------|------|--------|
| BR-001 | {规则描述} | {module} | {source} | {level} |

---

## 5. 数据实体概览

| 实体名称 | 实体描述 | 关键属性 | 来源 |
|----------|----------|----------|------|
| {entity} | {description} | {attributes} | {source} |

---

## 6. 行业标准与合规要求

| 标准编号 | 标准名称 | 适用范围 | 关键要求 | 来源 |
|----------|----------|----------|----------|------|
| {code} | {name} | {scope} | {requirement} | {source} |

---

## 7. 竞品功能对比（如适用）

| 功能模块 | 竞品A | 竞品B | 竞品C | 本项目建议 |
|----------|-------|-------|-------|-----------|
| {module} | ✓/✗ | ✓/✗ | ✓/✗ | 建议/可选/不需要 |

---

## 8. 待深入调研项

| 编号 | 调研方向 | 原因 | 建议调研方式 |
|------|---------|------|-------------|
| TBD-001 | {方向} | {reason} | {method} |

---

## 9. 来源清单

| 编号 | 来源标题 | URL | 来源类型 | 可信度 | 采集日期 |
|------|---------|-----|---------|--------|---------|
| SRC-001 | {title} | {url} | {type} | {level} | {date} |

---

## 10. 免责声明

> 本文档所有内容均采集自互联网公开信息，仅供需求调研参考。
> 最终需求定义需由产品经理结合实际业务场景确认。
> 来源信息可能存在时效性，请注意验证。

```

- **competitive_matrix_template**: 
```
# 竞品功能清单

## 文档信息
| 属性 | 值 |
|------|-----|
| 系统类型 | {system_type} |
| 采集日期 | {date} |
| 竞品数量 | {competitor_count} |

---

## 1. 竞品概览

| 竞品名称 | 官网 | 目标市场 | 核心特点 |
|----------|------|---------|---------|
| {name} | {url} | {market} | {feature} |

---

## 2. 功能模块对比矩阵

| 功能模块 | 功能点 | {竞品A} | {竞品B} | {竞品C} | 行业标配 |
|----------|--------|---------|---------|---------|---------|
| {module} | {feature} | ✓/✗/部分 | ✓/✗/部分 | ✓/✗/部分 | 是/否 |

---

## 3. 差异化功能分析

### 3.1 独有功能
| 竞品 | 功能名 | 功能描述 | 市场价值评估 |
|------|--------|---------|-------------|
| {name} | {feature} | {desc} | {value} |

### 3.2 行业标配功能（必须实现）
| 功能名 | 功能描述 | 覆盖竞品数 |
|--------|---------|-----------|
| {feature} | {desc} | {n}/{total} |

---

## 4. 功能优先级建议

| 优先级 | 功能模块 | 理由 |
|--------|---------|------|
| P0-必须 | {module} | 行业标配，所有竞品均支持 |
| P1-重要 | {module} | 多数竞品支持，用户期望高 |
| P2-可选 | {module} | 差异化功能，可提升竞争力 |

```

## 检查清单


### before_search


- **item**: 目标行业已明确
- **check**: 检查domain参数是否具体（不能是模糊的"管理系统"）

- **item**: 系统类型已确认
- **check**: 检查system_type参数

- **item**: 采集范围已确定
- **check**: 检查search_scope参数

- **item**: 采集深度已确定
- **check**: 检查depth参数

### during_search


- **item**: 搜索关键词多样化
- **check**: 至少使用3组不同维度的搜索关键词

- **item**: 来源多样性
- **check**: 采集来源不少于5个不同类型

- **item**: 内容真实性验证
- **check**: 每个来源均可通过URL访问验证

- **item**: 相关性过滤
- **check**: 排除与目标行业/系统无关的内容

### after_search


- **item**: 需求点已结构化
- **check**: 所有需求点按模块分类整理

- **item**: 来源已标注
- **check**: 每个需求点均有来源URL和可信度评级

- **item**: 去重已完成
- **check**: 无重复或高度相似的需求点

- **item**: 文档结构完整
- **check**: 检查所有必要章节已填写

- **item**: 免责声明已添加
- **check**: 文档包含免责声明

## 质量标准


- **standard**: 来源真实性
- **requirement**: 100%
- **check**: 所有来源URL可访问，内容真实存在

- **standard**: 来源多样性
- **requirement**: ≥ 3种来源类型
- **check**: 统计来源类型分布

- **standard**: 需求点覆盖率
- **requirement**: ≥ 80%（相对行业通用功能）
- **check**: 与行业标准功能清单比对

- **standard**: 来源可信度
- **requirement**: A+B级来源占比 ≥ 60%
- **check**: 统计可信度分布

- **standard**: 需求点可追溯性
- **requirement**: 100%
- **check**: 每个需求点均有来源标注

## 参考文档


### primary


- **path**: 产品/references/prd-template.md
- **description**: PRD标准模板，用于对齐需求格式

- **path**: 产品/references/brd-template.md
- **description**: BRD标准模板，用于业务需求对齐

### methodology


- **name**: Web搜索采集法
- **description**: 通过多维度关键词组合搜索互联网公开信息

- **name**: 需求提炼法
- **description**: 从非结构化文档中提取结构化功能需求点

- **name**: 来源可信度评级法
- **description**: 按来源类型和权威性进行可信度分级

## 协作关系


### upstream


- **skill**: 用户输入
- **relationship**: 接收初步需求描述
- **condition**: 用户提出新系统建设需求时

### downstream


- **skill**: requirement-analyzer
- **relationship**: 提供行业需求参考文档
- **condition**: 需求采集完成后

- **skill**: user-story-generator
- **relationship**: 提供功能需求点素材
- **condition**: 需求分析完成后

## 使用示例


- **name**: 医疗HIS系统需求采集
- **input**: 
```
我准备做HIS医疗系统，请你爬取网上HIS医疗系统的需求文档（禁止模拟数据）
```

- **output_summary**: 
```
## 采集概述
- 目标行业：医疗HIS（医院信息系统）
- 采集来源：12个（含3个招标文件、2个行业标准、4个竞品官网、3个技术文档）
- 有效需求点：47个

## 功能需求点概览
核心模块：
1. 门诊管理（挂号、分诊、叫号、就诊）- 8个需求点
2. 住院管理（入院、床位、医嘱、出院）- 7个需求点
3. 药房管理（处方、发药、库存）- 6个需求点
4. 检验检查（LIS/PACS对接）- 5个需求点
5. 收费管理（医保对接、费用结算）- 6个需求点
6. 电子病历（EMR）- 5个需求点
7. 系统管理（权限、字典、日志）- 5个需求点
8. 报表统计（工作量、收入、运营）- 5个需求点

## 行业标准
- WS/T 500-2016 电子病历共享文档规范
- GB/T 29765-2013 信息安全技术 信息系统灾难恢复规范
- 国家卫健委 医院信息平台应用功能指引

## 来源清单
SRC-001: 某三甲医院HIS系统招标文件 [A级]
SRC-002: 卫健委医院信息平台功能指引 [A级]
SRC-003-012: 竞品官网和技术文档 [B级]

```

- **name**: 制造业MES系统需求采集
- **input**: 
```
准备开发一套制造业MES生产执行系统，需要获取行业标准功能需求
```

- **output_summary**: 
```
## 采集概述
- 目标行业：制造业MES（制造执行系统）
- 采集来源：15个
- 有效需求点：62个

## 功能需求点概览
核心模块：
1. 生产计划管理 - 9个需求点
2. 工单管理 - 7个需求点
3. 工艺路线管理 - 6个需求点
4. 物料管理 - 8个需求点
5. 质量管理 - 7个需求点
6. 设备管理 - 6个需求点
7. 数据采集（SCADA对接）- 5个需求点
8. 看板与报表 - 7个需求点
9. 系统集成（ERP对接）- 7个需求点

## 行业标准
- ISA-95 企业与控制系统集成标准
- MESA-11 MES功能模型
- GB/T 20720-2006 企业控制系统集成

```

## 注意事项


- 所有采集内容必须来自真实互联网来源，严禁模拟或编造数据
- 搜索时优先使用中文关键词，补充英文关键词
- 优先采集政府网站、行业标准数据库、竞品官网等高质量来源
- 对于单来源的需求点，需要标注可信度为C或D，建议交叉验证
- 采集结果仅作为需求参考，最终需求定义需产品经理确认
- 注意信息的时效性，优先采集近3年的内容
- 遵守网站robots.txt协议，仅采集公开可访问的内容

## metadata

- **created_at**: 2026-06-15
- **updated_at**: 2026-06-15
- **author**: Claude Agent

### version_history


- **version**: 1.0.0
- **date**: 2026-06-15
- **changes**: 初始版本，基于需求扩展场景设计
