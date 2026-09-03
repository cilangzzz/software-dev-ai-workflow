# 全流程软件开发组合工作流

> 本文档定义一个完整的软件开发组合工作流，涵盖需求分析→需求开发→需求理解→系统设计→概要设计→模块排期→后端开发→前端开发全8个阶段。
> 每个阶段定义清晰的输入、输出、调用的Skill、产出物路径和验收标准。

---

## 工作流概述

### 适用场景

- 从需求文档到完整系统交付的端到端开发流程
- 多阶段、多角色协作的复杂项目开发
- 需要产出标准化文档和代码的规范化开发

### 核心理念

- **真实数据优先**：所有阶段必须基于真实的网络调研数据，禁止Mock数据
- **文档驱动开发**：每个阶段产出标准化文档，作为下游阶段的输入
- **自动化流转**：通过Skill调用实现阶段间自动衔接
- **质量门控**：每个阶段设置验收标准，确保产出质量

---

## 阶段定义

| 阶段序号 | 阶段名称 | 主要角色 | 核心Skill | 产出物目录 |
|----------|----------|----------|-----------|------------|
| 1 | 需求分析阶段 | 产品经理 | requirement-analyzer + deep-research | 02-开发库/00-需求分析 |
| 2 | 需求开发阶段 | 产品经理 | user-story-generator | 02-开发库/01-需求开发 |
| 3 | 需求理解阶段 | 产品经理 | acceptance-criteria-writer + business-rule-analyzer | 02-开发库/02-需求理解 |
| 4 | 系统设计阶段 | 系统架构师 | system-architect + deep-research | 02-开发库/03-系统设计 |
| 5 | 概要设计阶段 | 研发工程师 | system-architect + db-designer-java + api-designer | 02-开发库/04-概要设计 |
| 6 | 模块排期阶段 | 项目经理 | schedule-template | 01-管理库/02-项目管理 |
| 7 | 后端开发阶段 | 后端工程师 | implement (backend) + code-review | 03-源码库 |
| 8 | 前端开发阶段 | 前端工程师 | implement (frontend) + code-review | 03-源码库 |

---

## 目录结构

### 产出物目录

```
F:\sandbox\workflow\2.0-用例\项目管理样例\
├── 01-管理库/
│   ├── 01-项目策划/
│   ├── 02-项目管理/          ← 模块排期阶段产出
│   ├── 03-质量保证/
│   ├── 04-配置管理/
│   ├── 05-培训/
│   ├── 06-会议记录/
│   ├── 07-邮件/
│   ├── 08-项目总结/
│   └── 09-管理评审/
├── 02-开发库/
│   ├── 00-需求分析阶段/      ← 第1阶段产出
│   ├── 01-需求开发/          ← 第2阶段产出
│   ├── 02-需求理解/          ← 第3阶段产出
│   │   ├── {模块名}/
│   │   │   ├── {子模块名}/
│   │   │   │   ├── 业务流程图/
│   │   │   │   ├── 原型图/
│   │   │   │   └── 功能点详情/
│   │   │   │   └── 业务文档/
│   ├── 03-系统设计/          ← 第4阶段产出
│   ├── 04-概要设计/          ← 第5阶段产出
│   │   ├── 业务架构设计/
│   │   ├── 数据库设计/
│   │   ├── API接口设计/
│   ├── 05-详细设计/
│   ├── 06-集成测试/
│   ├── 07-系统测试/
│   ├── 08-实施与验收/
│   └── 09-用户手册/
├── 03-源码库/                ← 第7、8阶段产出
│   ├── 00-开发软件/
│   └── {模块名}/
│       ├── trunk/
│       ├── tags/
│       └── deploy/
└── 04-版本发布库/
    ├── 01-对内发布/
    └── 02-对外发布/
```

### 前端对接文档目录

```
F:\projects\yudao-ai-his-backend\docs\his\
├── 00-全局文档/
│   ├── HIS系统-产品需求文档(PRD).md
│   ├── HIS系统-业务规则文档.md
│   ├── HIS系统-模块划分文档.md
│   └── HIS系统-验收标准.md
├── {模块编号}-{模块名}/
│   ├── README.md
│   ├── api-{domain}.md      ← 后端生成的API对接文档
│   ├── 业务规则.md
│   └── 数据模型.md
```

---

## 阶段1：需求分析阶段

### 阶段目标

通过网络调研获取真实的用户需求资料，调用产品技能完成需求调研，产出需求分析文档。

### 输入

| 输入项 | 类型 | 来源 | 说明 |
|--------|------|------|------|
| 需求主题 | string | 用户输入 | 需要调研的需求主题（如"医院信息系统"、"电商平台"等） |
| 业务背景 | string | 用户输入 | 业务背景信息（行业、目标用户、业务目标） |

### 执行流程

```yaml
阶段1_需求分析:
  步骤:
    - name: 网络调研
      description: 多个Agent并行爬取网上相关需求文档资料
      skill: deep-research
      agent_count: 3-5
      critical: 禁止Mock数据，必须使用真实网络资源
      output:
        - 行业背景资料
        - 用户需求调研报告
        - 竞品分析报告
        - 相关政策法规文档

    - name: 需求调研
      description: 调用产品技能进行需求调研分析
      skill: requirement-analyzer
      skill_path: F:\sandbox\workflow\1.0-软件开发流程角色agent模型\产品\skill\requirement-analyzer.skill.md
      input:
        requirement_text: 来自网络调研的综合需求描述
        business_context: 业务背景信息
        analysis_depth: full
        output_format: prd
      output:
        - PRD文档
        - 需求清单
        - 用户故事集
        - 澄清问题清单

    - name: 产出物归档
      description: 将产出物归档到指定目录
      output_path: F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\00-需求分析阶段
      artifacts:
        - 需求调研报告-{日期}.md
        - 行业背景分析-{日期}.md
        - 竞品分析报告-{日期}.md
        - PRD-{项目名}.md
        - 需求清单-{日期}.xlsx
        - 用户故事-{项目名}.md
        - 待确认问题-{日期}.md
```

### Skill调用示例

```
/deep-research

研究主题：医院信息系统(HIS)需求分析
研究范围：
1. HIS系统核心功能模块（门诊、住院、药品、收费）
2. 医院用户痛点调研（医生、护士、患者、管理员）
3. 国内主流HIS系统竞品分析
4. 医疗信息化政策法规
5. HIS系统技术架构趋势

要求：禁止使用Mock数据，所有资料必须来自真实网络来源，提供来源链接
```

```
/requirement-analyzer

需求来源：网络调研综合报告
需求描述：[来自deep-research的调研结果]

业务背景：
- 行业：医疗信息化
- 目标用户：医院医生、护士、管理员、患者
- 业务目标：提升医院运营效率、改善患者就医体验

分析深度：full
输出格式：all（PRD + BRD + User Story）
```

### 产出物清单

| 序号 | 产出物 | 格式 | 必需 | 说明 |
|------|--------|------|------|------|
| 1 | 需求调研报告 | markdown | 是 | 综合网络调研的需求分析 |
| 2 | 行业背景分析 | markdown | 是 | 医疗行业背景、政策法规分析 |
| 3 | 竞品分析报告 | markdown | 是 | 主流HIS系统功能对比分析 |
| 4 | PRD文档 | markdown | 是 | 产品需求文档（符合prd-template） |
| 5 | 需求清单 | excel | 是 | 需求点列表，含RICE优先级评分 |
| 6 | 用户故事集 | markdown | 是 | 符合INVEST原则的用户故事 |
| 7 | 待确认问题清单 | markdown | 是 | 待与业务方确认的问题 |

### 验收标准

```markdown
## 需求分析阶段验收清单

### 数据来源检查
- [ ] 所有调研资料有明确来源链接
- [ ] 无Mock数据，全部为真实网络资源
- [ ] 竞品分析至少覆盖3个主流产品
- [ ] 政策法规引用最新版本

### PRD质量检查
- [ ] PRD结构完整（需求概述、用户分析、功能需求、非功能需求、验收标准）
- [ ] 用户故事符合INVEST原则
- [ ] 验收标准采用Gherkin格式
- [ ] RICE优先级评分合理

### 完整性检查
- [ ] 所有必需产出物已生成
- [ ] 文档已归档到正确目录
- [ ] 待确认问题清单完整
```

---

## 阶段2：需求开发阶段

### 阶段目标

阅读需求分析阶段产出的PRD文档，理解需求，调用产品技能产出功能点列表和业务需求文档。

### 输入

| 输入项 | 类型 | 来源 | 说明 |
|--------|------|------|------|
| PRD文档 | markdown | 阶段1产出 | 产品需求文档 |
| 需求清单 | excel | 阶段1产出 | 需求点列表 |
| 用户故事集 | markdown | 阶段1产出 | 用户故事列表 |

### 执行流程

```yaml
阶段2_需求开发:
  步骤:
    - name: 需求阅读理解
      description: 阅读PRD文档，理解核心需求
      action: Read PRD文档，提取核心功能模块和业务规则
      output: 需求理解摘要

    - name: 功能点分解
      description: 将用户需求分解为具体功能点
      skill: user-story-generator
      skill_path: F:\sandbox\workflow\1.0-软件开发流程角色agent模型\产品\skill\user-story-generator.skill.md
      input:
        requirement_content: PRD内容
        story_format: standard
        detail_level: detailed
      output:
        - 功能点列表（按模块分类）
        - 功能点描述文档

    - name: 业务需求文档编写
      description: 编写BRD业务需求文档
      template: brd-template
      template_path: F:\sandbox\workflow\1.0-软件开发流程角色agent模型\产品\references\brd-template.md
      output:
        - BRD业务需求文档

    - name: 产出物归档
      description: 将产出物归档到指定目录
      output_path: F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\01-需求开发
      artifacts:
        - 功能点列表-{模块名}.xlsx
        - 功能点详情-{模块名}.md
        - BRD-{项目名}.md
```

### Skill调用示例

```
/user-story-generator

PRD内容：[读取阶段1产出的PRD文档]
模块：HIS系统
角色：医生、护士、管理员、患者

详细程度：detailed
格式：standard
```

### 产出物清单

| 序号 | 产出物 | 格式 | 必需 | 说明 |
|------|--------|------|------|------|
| 1 | 功能点列表 | excel | 是 | 按模块分类的功能点清单 |
| 2 | 功能点详情 | markdown | 是 | 每个功能点的详细描述 |
| 3 | BRD文档 | markdown | 是 | 业务需求文档 |

### 验收标准

```markdown
## 需求开发阶段验收清单

### 功能点完整性
- [ ] 功能点覆盖PRD所有需求
- [ ] 功能点按模块分类清晰
- [ ] 功能点粒度合理（1-8故事点范围）
- [ ] 功能点有明确的验收条件

### BRD质量
- [ ] BRD结构完整（业务背景、业务目标、业务规则、业务流程）
- [ ] 业务规则清晰可执行
- [ ] 业务流程图完整

### 一致性检查
- [ ] 功能点与PRD需求一致
- [ ] BRD与PRD需求一致
```

---

## 阶段3：需求理解阶段

### 阶段目标

根据业务需求和功能点文档，调用产品技能生成原型图、业务流程图、功能点详细描述文档，产出文档需按模块→子模块→功能点/业务分类存放。

### 输入

| 输入项 | 类型 | 来源 | 说明 |
|--------|------|------|------|
| BRD文档 | markdown | 阶段2产出 | 业务需求文档 |
| 功能点列表 | excel | 阶段2产出 | 功能点清单 |
| 功能点详情 | markdown | 阶段2产出 | 功能点描述 |

### 执行流程

```yaml
阶段3_需求理解:
  步骤:
    - name: 模块结构分析
      description: 分析功能模块结构，确定子模块划分
      action: 根据功能点列表，划分模块→子模块→功能点层级
      output: 模块结构树

    - name: 验收标准编写
      description: 为每个功能点编写Gherkin格式验收标准
      skill: acceptance-criteria-writer
      skill_path: F:\sandbox\workflow\1.0-软件开发流程角色agent模型\产品\skill\acceptance-criteria-writer.skill.md
      output:
        - 验收标准文档（按模块分类）

    - name: 业务规则分析
      description: 分析复杂业务规则
      skill: business-rule-analyzer
      skill_path: F:\sandbox\workflow\1.0-软件开发流程角色agent模型\产品\skill\business-rule-analyzer.skill.md
      output:
        - 业务规则文档（按模块分类）

    - name: 原型图生成
      description: 生成UI原型图描述文档
      template: view-dashboard-template
      template_path: F:\sandbox\workflow\1.0-软件开发流程角色agent模型\产品\references\view-dashboard-template.md
      output:
        - 原型图描述文档（含页面布局、交互流程）

    - name: 业务流程图生成
      description: 生成业务流程图描述文档
      output:
        - 业务流程图描述文档（Mermaid格式）

    - name: 产出物归档（按模块分类）
      description: 按模块→子模块→功能点分类存放
      output_path: F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\02-需求理解
      structure:
        - {模块名}/
          - {子模块名}/
            - 业务流程图/
              - {流程名}-流程图.md
            - 原型图/
              - {页面名}-原型描述.md
            - 功能点详情/
              - {功能名}-详情.md
              - {功能名}-验收标准.md
            - 业务文档/
              - {业务名}-规则.md
```

### 目录结构示例

```
02-需求理解/
├── M01-门诊管理/
│   ├── 01-挂号管理/
│   │   ├── 业务流程图/
│   │   │   ├── 挂号流程图.md
│   │   │   ├── 退号流程图.md
│   │   ├── 原型图/
│   │   │   ├── 挂号页面原型.md
│   │   │   ├── 挂号列表原型.md
│   │   ├── 功能点详情/
│   │   │   ├── 挂号创建-详情.md
│   │   │   ├── 挂号创建-验收标准.md
│   │   │   ├── 挂号查询-详情.md
│   │   │   ├── 挂号查询-验收标准.md
│   │   ├── 业务文档/
│   │   │   ├── 挂号规则.md
│   │   │   ├── 挂号类型字典.md
│   ├── 02-就诊管理/
│   │   ├── ...
├── M02-住院管理/
│   ├── 01-入院管理/
│   │   ├── ...
│   ├── 02-在院管理/
│   │   ├── ...
├── M06-药品管理/
│   ├── ...
```

### Skill调用示例

```
/acceptance-criteria-writer

功能模块：HIS系统-门诊管理-挂号管理
功能点列表：
- 挂号创建
- 挂号查询
- 挂号修改
- 挂号取消（退号）
- 挂号排队

输出格式：Gherkin
```

```
/business-rule-analyzer

业务场景：HIS系统门诊挂号
业务规则：
1. 挂号类型：普通、专家、急诊
2. 挂号费用按类型收取
3. 同一患者同一天同一科室只能挂一次号
4. 急诊挂号不限号，普通和专家限号
5. 退号需在就诊前，就诊后不可退号
```

### 产出物清单

| 序号 | 产出物 | 格式 | 必需 | 路径说明 |
|------|--------|------|------|----------|
| 1 | 业务流程图 | markdown | 是 | 模块/子模块/业务流程图/ |
| 2 | 原型图描述 | markdown | 是 | 模块/子模块/原型图/ |
| 3 | 功能点详情 | markdown | 是 | 模块/子模块/功能点详情/ |
| 4 | 验收标准 | markdown | 是 | 模块/子模块/功能点详情/ |
| 5 | 业务规则文档 | markdown | 是 | 模块/子模块/业务文档/ |

### 验收标准

```markdown
## 需求理解阶段验收清单

### 目录结构检查
- [ ] 文档按模块→子模块→功能点分类存放
- [ ] 目录结构清晰，层级不超过4层
- [ ] 同类文档集中在同一目录

### 原型图质量
- [ ] 原型图描述包含页面布局、字段、交互
- [ ] 原型图覆盖所有核心功能页面
- [ ] 原型图有明确的交互流程说明

### 业务流程图质量
- [ ] 业务流程图使用Mermaid格式
- [ ] 流程图包含开始、结束、判断节点
- [ ] 流程图覆盖主流程和异常流程

### 验收标准质量
- [ ] 验收标准采用Gherkin格式
- [ ] 每个功能点有验收标准
- [ ] 验收标准可测试、可执行

### 业务规则质量
- [ ] 业务规则描述清晰
- [ ] 业务规则有明确的触发条件
- [ ] 业务规则有明确的处理逻辑
```

---

## 阥段4：系统设计阶段

### 阶段目标

结合需求和网络调研资料，生成系统需求、访问人数预估、数据增量预估等系统文档。

### 输入

| 输入项 | 类型 | 来源 | 说明 |
|--------|------|------|------|
| PRD文档 | markdown | 阶段1产出 | 产品需求文档 |
| BRD文档 | markdown | 阶段2产出 | 业务需求文档 |
| 功能点详情 | markdown | 阶段3产出 | 功能点详细描述 |
| 现有架构 | markdown | 项目文档 | 已有系统架构框架（如有） |

### 执行流程

```yaml
阶段4_系统设计:
  步骤:
    - name: 系统需求调研
      description: 网络调研同类系统的技术架构、性能数据
      skill: deep-research
      critical: 禁止Mock数据，必须使用真实网络资源
      output:
        - 同类系统技术架构分析
        - 性能指标参考数据
        - 访问量行业数据

    - name: 系统需求分析
      description: 分析系统级需求（性能、安全、可用性等）
      skill: system-architect
      skill_path: F:\sandbox\workflow\1.0-软件开发流程角色agent模型\研发\skill\architect\system-architect.skill.md
      input:
        prd_document: PRD内容
        architecture_type: auto
        tech_constraints:
          existing_stack: [现有技术栈]
          compliance: [合规要求]
      output:
        - 系统需求文档
        - 架构目标定义

    - name: 性能指标估算
      description: 估算访问人数、并发量、数据增量
      method: 根据业务目标和行业数据估算
      output:
        - 性能需求估算文档
        - 数据增量预估文档

    - name: 产出物归档
      description: 将产出物归档到指定目录
      output_path: F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\03-系统设计
      artifacts:
        - 系统需求文档-{项目名}.md
        - 性能需求估算-{项目名}.md
        - 数据增量预估-{项目名}.md
        - 技术架构调研-{日期}.md
```

### Skill调用示例

```
/deep-research

研究主题：HIS系统技术架构和性能指标
研究范围：
1. 医院信息系统典型访问量数据（门诊量、住院量）
2. HIS系统性能指标参考（响应时间、并发量）
3. HIS系统技术架构最佳实践
4. 医疗数据安全合规要求
5. 医疗系统可用性要求

要求：禁止使用Mock数据，所有数据需有行业来源引用
```

```
/architect

PRD内容：[读取阶段1产出的PRD文档]
架构类型：auto

技术约束：
- 现有技术栈：Spring Boot 3.x / Vue 3 / MySQL 8
- 合规要求：医疗数据安全规范、个人信息保护法
- 预算限制：中型医院信息化预算

输出：系统需求文档 + 架构目标
```

### 产出物清单

| 序号 | 产出物 | 格式 | 必需 | 说明 |
|------|--------|------|------|------|
| 1 | 系统需求文档 | markdown | 是 | 系统级需求（性能、安全、可用性） |
| 2 | 性能需求估算 | markdown | 是 | 访问人数、并发量、响应时间要求 |
| 3 | 数据增量预估 | markdown | 是 | 数据量增长预估、存储规划 |
| 4 | 技术架构调研 | markdown | 是 | 行业技术架构分析（真实数据来源） |

### 验收标准

```markdown
## 系统设计阶段验收清单

### 数据真实性检查
- [ ] 性能指标有行业数据来源引用
- [ ] 访问量估算有业务依据
- [ ] 技术架构调研有真实案例参考
- [ ] 无Mock数据

### 系统需求完整性
- [ ] 性能需求明确（响应时间、并发量、吞吐量）
- [ ] 安全需求明确（认证、授权、数据安全）
- [ ] 可用性需求明确（SLA、备份策略）
- [ ] 兼容性需求明确（浏览器、设备）

### 估算合理性
- [ ] 访问量估算与业务规模匹配
- [ ] 数据增量预估有计算依据
- [ ] 性能指标符合行业实践
```

---

## 阥段5：概要设计阶段

### 阶段目标

根据业务需求调用研发技能生成业务架构设计和数据库设计。

### 输入

| 输入项 | 类型 | 来源 | 说明 |
|--------|------|------|------|
| 系统需求文档 | markdown | 阶段4产出 | 系统级需求 |
| 功能点详情 | markdown | 阶段3产出 | 功能点详细描述 |
| 业务规则文档 | markdown | 阶段3产出 | 业务规则描述 |

### 执行流程

```yaml
阶段5_概要设计:
  步骤:
    - name: 业务架构设计
      description: 设计业务模块架构和模块间关系
      skill: system-architect
      skill_path: F:\sandbox\workflow\1.0-软件开发流程角色agent模型\研发\skill\architect\system-architect.skill.md
      input:
        prd_document: PRD + 功能点详情
        architecture_type: modular-monolith  # HIS系统推荐模块化单体架构
      output:
        - 业务架构设计文档
        - 模块划分图
        - 模块依赖关系图

    - name: 数据库设计
      description: 设计数据库表结构
      skill: db-designer-java
      skill_path: F:\sandbox\workflow\1.0-软件开发流程角色agent模型\研发\skill\design\db-designer-java.skill.md
      input:
        module_code: his  # HIS系统模块编码
        table_name: [各业务表名]
        business_fields: [业务字段列表]
      output:
        - DDL脚本（按模块分类）
        - ER图描述
        - 数据字典

    - name: API接口设计
      description: 设计RESTful API接口
      skill: api-designer
      skill_path: F:\sandbox\workflow\1.0-软件开发流程角色agent模型\研发\skill\design\api-designer.skill.md
      input:
        module_doc: 功能点详情 + 业务规则
        api_version: v1
        base_path: /his
      output:
        - API接口设计文档
        - 请求/响应结构定义
        - 错误码定义

    - name: 产出物归档
      description: 将产出物归档到指定目录
      output_path: F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\04-概要设计
      structure:
        - 业务架构设计/
          - 业务架构文档.md
          - 模块划分图.md
          - 模块依赖图.md
        - 数据库设计/
          - DDL/
            - {模块名}/
              - {表名}_create.sql
          - ER图/
            - {模块名}-ER图.md
          - 数据字典/
            - {模块名}-数据字典.md
        - API接口设计/
          - {模块名}-API设计.md
          - 错误码定义.md
```

### Skill调用示例

```
/architect

PRD内容：[读取阶段3产出的功能点详情]
架构类型：modular-monolith  # HIS系统推荐模块化单体架构

技术约束：
- 后端框架：Spring Boot 3.x (yudao-vue-pro)
- 前端框架：Vue 3 + Vite (vben-admin)
- 数据库：MySQL 8.0
- 多租户：支持医院多院区

输出：业务架构设计 + C4架构图
```

```
/db-designer

模块编码：his
表名：his_register（挂号表）
表注释：门诊挂号记录表

业务字段：
- patient_id: 患者ID（BIGINT，必填）
- patient_name: 患者姓名（VARCHAR64，必填）
- dept_id: 科室ID（BIGINT，必填）
- doctor_id: 医生ID（BIGINT）
- register_type: 挂号类型（TINYINT，字典）
- register_fee: 挂号费用（DECIMAL102）
- status: 挂号状态（TINYINT，字典）
- queue_no: 排队号（VARCHAR20）
- register_time: 挂号时间（DATETIME）
```

```
/api-designer

模块文档：HIS系统门诊管理模块
API版本：v1
基础路径：/his

功能列表：
- 挂号管理：创建、查询、修改、退号
- 就诊管理：开始就诊、结束就诊
- 处方管理：开处方、查询、审核

输出格式：markdown
```

### 产出物清单

| 序号 | 产出物 | 格式 | 必需 | 路径说明 |
|------|--------|------|------|----------|
| 1 | 业务架构文档 | markdown | 是 | 业务架构设计/ |
| 2 | 模块划分图 | markdown | 是 | 业务架构设计/ |
| 3 | DDL脚本 | sql | 是 | 数据库设计/DDL/{模块}/ |
| 4 | ER图描述 | markdown | 是 | 数据库设计/ER图/ |
| 5 | 数据字典 | markdown | 是 | 数据库设计/数据字典/ |
| 6 | API接口设计 | markdown | 是 | API接口设计/ |
| 7 | 错误码定义 | markdown | 是 | API接口设计/ |

### 验收标准

```markdown
## 概要设计阶段验收清单

### 业务架构质量
- [ ] 业务架构覆盖所有功能模块
- [ ] 模块划分合理，职责清晰
- [ ] 模块依赖关系明确

### 数据库设计质量
- [ ] DDL符合项目规范（多租户、审计字段）
- [ ] 表名符合命名规范（his_前缀）
- [ ] 索引设计合理（tenant_id包含）
- [ ] ER图完整

### API设计质量
- [ ] API符合RESTful规范
- [ ] 请求/响应结构完整
- [ ] 错误码定义清晰
- [ ] 权限标识完整（his:xxx:xxx）
```

---

## 阥段6：模块排期阶段

### 阥段目标

生成系统实现的排期计划，确定模块开发顺序和优先级。

### 输入

| 输入项 | 类型 | 来源 | 说明 |
|--------|------|------|------|
| 功能点列表 | excel | 阶段2产出 | 功能点清单（含优先级） |
| 业务架构文档 | markdown | 阥段5产出 | 模块划分和依赖关系 |
| 数据库设计 | sql | 阥段5产出 | DDL脚本（工作量参考） |

### 执行流程

```yaml
阶段6_模块排期:
  步骤:
    - name: 模块优先级分析
      description: 分析模块优先级和依赖关系
      method:
        - 根据RICE优先级排序
        - 根据模块依赖关系确定先后顺序
        - 核心模块优先开发
      output: 模块优先级列表

    - name: 工作量估算
      description: 估算各模块工作量
      method:
        - 按功能点数量估算
        - 按表数量估算
        - 按API数量估算
      output: 模块工作量估算表

    - name: 排期计划生成
      description: 生成模块开发排期计划
      template: schedule-template
      template_path: F:\sandbox\workflow\1.0-软件开发流程角色agent模型\项目管理\references\schedule-template.md
      output:
        - 模块排期计划
        - 里程碑计划

    - name: 产出物归档
      description: 将产出物归档到指定目录
      output_path: F:\sandbox\workflow\2.0-用例\项目管理样例\01-管理库\02-项目管理
      artifacts:
        - 模块排期计划-{项目名}.xlsx
        - 里程碑计划-{项目名}.md
        - 工作量估算-{项目名}.xlsx
```

### 排期规则

```markdown
## 模块排期规则

### 优先级规则
1. 基础模块优先：用户、权限、字典模块最先开发
2. 核心业务优先：门诊管理作为核心业务优先
3. 依赖模块优先：被依赖模块先开发
4. 高优先级功能优先：RICE评分高的功能优先

### HIS系统推荐排期顺序
| 优先级 | 模块 | 依赖关系 | 开发周期 |
|--------|------|----------|----------|
| P0 | 基础数据（科室、医生、患者） | 无依赖 | 1周 |
| P0 | 门诊挂号 | 依赖基础数据 | 2周 |
| P1 | 门诊就诊 | 依赖挂号 | 1周 |
| P1 | 处方管理 | 依赖就诊 | 2周 |
| P1 | 门诊收费 | 依赖处方 | 2周 |
| P2 | 住院入院 | 依赖基础数据 | 2周 |
| P2 | 住院管理 | 依赖入院 | 2周 |
| P2 | 药品管理 | 无依赖（可并行） | 1周 |
```

### Skill调用示例

```
根据功能点列表和模块依赖关系，生成排期计划：

模块列表：
- M00-基础数据模块（科室、医生、患者）
- M01-门诊管理（挂号、就诊、处方、收费）
- M02-住院管理（入院、在院、出院、结算）
- M06-药品管理（药品目录、库存）

依赖关系：
- M01依赖M00
- M02依赖M00
- M06独立

排期原则：
- 基础模块优先
- 高优先级功能优先
- 可并行模块尽量并行
```

### 产出物清单

| 序号 | 产出物 | 格式 | 必需 | 说明 |
|------|--------|------|------|------|
| 1 | 模块排期计划 | excel | 是 | 模块开发顺序和时间计划 |
| 2 | 里程碑计划 | markdown | 是 | 关键里程碑时间节点 |
| 3 | 工作量估算 | excel | 是 | 各模块工作量估算明细 |

### 验收标准

```markdown
## 模块排期阶段验收清单

### 排期合理性
- [ ] 基础模块优先开发
- [ ] 依赖关系正确（上游模块先开发）
- [ ] 高优先级功能安排在前
- [ ] 可并行模块合理安排并行

### 工作量估算
- [ ] 工作量估算有依据（功能点/表/API数量）
- [ ] 工作量估算合理（参考历史数据）
- [ ] 预留缓冲时间

### 里程碑定义
- [ ] 里程碑节点清晰
- [ ] 里程碑有明确的交付物
- [ ] 里程碑时间合理
```

---

## 阥段7：后端开发阶段

### 阥段目标

同步各阶段文档到目录，调用后端框架Skill完成开发，执行检查工作流直至无Error，生成前端对接文档。

### 输入

| 输入项 | 类型 | 来源 | 说明 |
|--------|------|------|------|
| DDL脚本 | sql | 阥段5产出 | 数据库表结构 |
| API接口设计 | markdown | 阥段5产出 | API接口规范 |
| 业务规则文档 | markdown | 阥段3产出 | 业务规则描述 |
| 验收标准 | markdown | 阥段3产出 | Gherkin验收标准 |

### 后端项目路径

```
F:\projects\yudao-ai-his-backend\
├── CLAUDE.md                    # 后端开发规范（Skill索引）
├── skills/                      # Skill文档
├── yudao-module-his/            # HIS模块
│   ├── yudao-module-his-biz/
│   │   ├── src/main/java/cn/iocoder/yudao/module/his/
│   │   │   ├── controller/admin/
│   │   │   │   ├── service/
│   │   │   │   ├── dal/
│   │   │   ├── enums/
│   │   ├── src/test/java/
│   ├── yudao-module-his-api/
├── docs/his/                    # 前端对接文档输出目录
```

### 执行流程

```yaml
阶段7_后端开发:
  步骤:
    - name: 文档同步
      description: 同步各阶段文档到后端项目目录
      action:
        - 复制需求理解阶段文档到docs/his/
        - 复制概要设计阶段文档到docs/his/
        - 复制API接口设计到docs/his/
      output_path: F:\projects\yudao-ai-his-backend\docs\his

    - name: 数据库脚本执行
      description: 执行DDL脚本创建表结构
      action: 执行阶段5产出的DDL脚本
      critical: 按模块顺序执行，处理依赖关系

    - name: 后端代码开发
      description: 调用后端框架Skill生成代码
      skill_path: F:\projects\yudao-ai-his-backend\CLAUDE.md
      workflow:
        - /entity-implementation  # 实体类实现
        - /extend-module          # 扩展模块开发
        - /new-module             # 新模块开发
      input:
        module_code: his
        table_name: [表名列表]
        api_design: [API设计文档]
      output:
        - DO实体类
        - Mapper接口
        - Service接口和实现
        - Controller
        - VO类

    - name: 代码检查工作流
      description: 执行检查工作流直至项目无Error
      workflow: /code-review
      loop_condition: 存在Error时循环修复
      max_retry: 5
      output: 代码审查报告

    - name: 前端对接文档生成
      description: 生成前端对接文档
      action: 根据API设计生成前端对接文档
      output_path: F:\projects\yudao-ai-his-backend\docs\his\{模块名}
      artifacts:
        - api-{domain}.md        # API接口文档
        - data-model.md          # 数据模型文档
        - pitfalls.md            # 踩坑点文档

    - name: 产出物归档
      description: 将源码归档到项目管理样例目录
      output_path: F:\sandbox\workflow\2.0-用例\项目管理样例\03-源码库\{模块名}\trunk
```

### Skill调用示例

```
# 后端开发调用示例（基于CLAUDE.md）

/entity-implementation

模块：HIS系统-门诊管理
表名：his_register
功能：挂号管理CRUD

步骤：
1. 建表SQL → his_register
2. DO实体 → HisRegisterDO
3. Mapper → HisRegisterMapper
4. Service → HisRegisterService / HisRegisterServiceImpl
5. Controller → HisRegisterController
6. VO → HisRegisterSaveReqVO / HisRegisterPageReqVO / HisRegisterRespVO
```

```
/code-review

审查范围：HIS模块新增代码
审查类型：全量审查

审查维度：
- 命名规范
- 代码结构
- 异常处理
- 事务管理
- 安全检查
- 性能检查

循环修复直至无Error
```

### 产出物清单

| 序号 | 产出物 | 格式 | 必需 | 路径说明 |
|------|--------|------|------|----------|
| 1 | DO实体类 | java | 是 | yudao-module-his-biz/dal/dataobject/ |
| 2 | Mapper接口 | java | 是 | yudao-module-his-biz/dal/mysql/ |
| 3 | Service接口 | java | 是 | yudao-module-his-biz/service/ |
| 4 | Service实现 | java | 是 | yudao-module-his-biz/service/ |
| 5 | Controller | java | 是 | yudao-module-his-biz/controller/admin/ |
| 6 | VO类 | java | 是 | yudao-module-his-biz/controller/admin/vo/ |
| 7 | 前端对接文档 | markdown | 是 | docs/his/{模块}/api-{domain}.md |
| 8 | 代码审查报告 | markdown | 是 | 01-管理库/03-质量保证/ |

### 验收标准

```markdown
## 后端开发阶段验收清单

### 代码质量
- [ ] 代码符合项目命名规范
- [ ] 代码结构符合分层架构
- [ ] 异常处理完整
- [ ] 事务管理正确
- [ ] 无编译Error
- [ ] 无代码审查Error

### 功能完整性
- [ ] CRUD功能完整
- [ ] 业务规则实现正确
- [ ] 权限控制完整
- [ ] 数据校验完整

### 文档输出
- [ ] 前端对接文档生成完整
- [ ] API文档包含请求/响应示例
- [ ] 数据模型文档完整

### 源码归档
- [ ] 源码已归档到项目管理样例目录
```

---

## 阥段8：前端开发阶段

### 阥段目标

同步各阶段文档到目录，调用前端框架Skill完成开发，执行检查工作流直至无Error。

### 输入

| 输入项 | 类型 | 来源 | 说明 |
|--------|------|------|------|
| 前端对接文档 | markdown | 阶段7产出 | API接口文档 |
| 原型图描述 | markdown | 阶段3产出 | UI原型描述 |
| 验收标准 | markdown | 阶段3产出 | Gherkin验收标准 |

### 前端项目路径

```
F:\projects\yudao-ai-his-admin-ui\yudao-ai-his-admin-ui\
├── CLAUDE.md                    # 前端开发规范（Skill索引）
├── skills/                      # Skill文档
├── apps/web-antd/src/
│   ├── api/his/                 # HIS API层
│   │   ├── patient/index.ts
│   │   ├── register/index.ts
│   │   ├── prescription/index.ts
│   │   └── ...
│   ├── views/his/               # HIS页面层
│   │   ├── patient/
│   │   ├── register/
│   │   ├── prescription/
│   │   └── ...
│   ├── router/routes/modules/
│   │   └── his.ts               # HIS路由配置
```

### 执行流程

```yaml
阶段8_前端开发:
  步骤:
    - name: 文档同步
      description: 同步各阶段文档到前端项目目录
      action:
        - 复制前端对接文档到docs/his/
        - 复制原型图描述到docs/his/
        - 复制验收标准到docs/his/
      output_path: F:\projects\yudao-ai-his-admin-ui\yudao-ai-his-admin-ui\docs\his

    - name: API层开发
      description: 开发前端API层
      skill_path: F:\projects\yudao-ai-his-admin-ui\yudao-ai-his-admin-ui\CLAUDE.md
      workflow: /his-module-development
      input:
        module_id: M01
        api_docs: [前端对接文档]
      output:
        - api/his/{模块}/index.ts

    - name: 页面组件开发
      description: 开发前端页面组件
      workflow:
        - 列表页面开发（index.vue + data.ts）
        - 表单弹窗开发（modules/form.vue）
        - 详情页面开发（detail/index.vue）
      output:
        - views/his/{模块}/index.vue
        - views/his/{模块}/data.ts
        - views/his/{模块}/modules/form.vue

    - name: 路由配置
      description: 配置前端路由
      action: 添加HIS模块路由配置
      output:
        - router/routes/modules/his.ts

    - name: 代码检查工作流
      description: 执行检查工作流直至项目无Error
      workflow: /his-error-fix
      loop_condition: 存在TypeScript Error时循环修复
      max_retry: 5
      output: TypeScript错误修复报告

    - name: 产出物归档
      description: 将源码归档到项目管理样例目录
      output_path: F:\sandbox\workflow\2.0-用例\项目管理样例\03-源码库\{模块名}-ui\trunk
```

### Skill调用示例

```
# 前端开发调用示例（基于CLAUDE.md）

/his-module-development

模块ID：M01
模块名：门诊管理
功能列表：
- 挂号管理（挂号创建、查询、修改、退号）
- 就诊管理（开始就诊、结束就诊）
- 处方管理（开处方、查询、审核）

API文档：docs/his/M01-门诊管理/api-register.md
原型图：docs/his/M01-门诊管理/原型图/

生成内容：
1. API层：api/his/register/index.ts
2. 列表页：views/his/register/index.vue + data.ts
3. 表单弹窗：views/his/register/modules/form.vue
4. 详情页：views/his/register/detail/index.vue
```

```
/his-error-fix

检查范围：HIS模块前端代码
检查类型：TypeScript类型检查

循环修复：
1. 检查TypeScript错误
2. 分析错误类型
3. 修复类型定义
4. 重新检查
5. 重复直至无Error
```

### 产出物清单

| 序号 | 产出物 | 格式 | 必需 | 路径说明 |
|------|--------|------|------|----------|
| 1 | API层 | typescript | 是 | apps/web-antd/src/api/his/{模块}/ |
| 2 | 列表页面 | vue | 是 | apps/web-antd/src/views/his/{模块}/ |
| 3 | 表格配置 | typescript | 是 | apps/web-antd/src/views/his/{模块}/data.ts |
| 4 | 表单弹窗 | vue | 是 | apps/web-antd/src/views/his/{模块}/modules/ |
| 5 | 详情页面 | vue | 是 | apps/web-antd/src/views/his/{模块}/detail/ |
| 6 | 路由配置 | typescript | 是 | apps/web-antd/src/router/routes/modules/his.ts |
| 7 | TypeScript错误报告 | markdown | 是 | 01-管理库/03-质量保证/ |

### 验收标准

```markdown
## 前端开发阶段验收清单

### API层质量
- [ ] API层命名符合规范（HisXxxApi命名空间）
- [ ] 请求/响应类型定义完整
- [ ] API方法覆盖所有接口

### 页面组件质量
- [ ] 页面布局符合原型图描述
- [ ] 表格列配置完整
- [ ] 表单字段配置完整
- [ ] 权限标识正确

### 路由配置质量
- [ ] 路由配置完整
- [ ] 权限配置正确
- [ ] 菜单图标和标题正确

### 类型检查
- [ ] 无TypeScript Error
- [ ] 类型定义完整
- [ ] 无类型警告

### 源码归档
- [ ] 源码已归档到项目管理样例目录
```

---

## 工作流自动化流转规则

```yaml
# 自动流转规则
workflow_flow:
  需求分析阶段:
    next: 需求开发阶段
    trigger: PRD文档生成完成
    condition: 验收清单全部通过

  需求开发阶段:
    next: 需求理解阶段
    trigger: 功能点列表生成完成
    condition: 验收清单全部通过

  需求理解阶段:
    next: 系统设计阶段
    trigger: 原型图、业务流程图生成完成
    condition: 验收清单全部通过

  系统设计阶段:
    next: 概要设计阶段
    trigger: 系统需求文档生成完成
    condition: 验收清单全部通过

  概要设计阶段:
    next: 模块排期阶段
    trigger: 业务架构、数据库设计完成
    condition: 验收清单全部通过

  模块排期阶段:
    next: 后端开发阶段
    trigger: 排期计划生成完成
    condition: 验收清单全部通过

  后端开发阶段:
    next: 前端开发阶段
    trigger: 前端对接文档生成完成
    condition: 代码无Error，验收清单通过

  前端开发阶段:
    next: 项目验收
    trigger: 前端代码开发完成
    condition: TypeScript无Error，验收清单通过
```

---

## 全流程产出物总览

| 阶段 | 产出物 | 数量 | 归档路径 |
|------|--------|------|----------|
| 需求分析 | 调研报告、PRD、需求清单、用户故事、问题清单 | 7+ | 02-开发库/00-需求分析阶段/ |
| 需求开发 | 功能点列表、功能点详情、BRD | 3+ | 02-开发库/01-需求开发/ |
| 需求理解 | 业务流程图、原型图、验收标准、业务规则（按模块分类） | 20+ | 02-开发库/02-需求理解/{模块}/{子模块}/ |
| 系统设计 | 系统需求文档、性能估算、数据增量预估 | 4+ | 02-开发库/03-系统设计/ |
| 概要设计 | 业务架构、DDL脚本、ER图、数据字典、API设计、错误码 | 10+ | 02-开发库/04-概要设计/ |
| 模块排期 | 排期计划、里程碑计划、工作量估算 | 3+ | 01-管理库/02-项目管理/ |
| 后端开发 | DO、Mapper、Service、Controller、VO、前端对接文档 | 50+ | 03-源码库/ + docs/his/ |
| 前端开发 | API层、页面组件、路由配置 | 30+ | 03-源码库/ |

---

## 附录：Skill文档路径索引

| Skill名称 | 文档路径 | 适用阶段 |
|-----------|----------|----------|
| requirement-analyzer | `1.0-软件开发流程角色agent模型\产品\skill\requirement-analyzer.skill.md` | 阶段1 |
| user-story-generator | `1.0-软件开发流程角色agent模型\产品\skill\user-story-generator.skill.md` | 阶段2 |
| acceptance-criteria-writer | `1.0-软件开发流程角色agent模型\产品\skill\acceptance-criteria-writer.skill.md` | 阶段3 |
| business-rule-analyzer | `1.0-软件开发流程角色agent模型\产品\skill\business-rule-analyzer.skill.md` | 阶段3 |
| system-architect | `1.0-软件开发流程角色agent模型\研发\skill\architect\system-architect.skill.md` | 阶段4、5 |
| db-designer-java | `1.0-软件开发流程角色agent模型\研发\skill\design\db-designer-java.skill.md` | 阶段5 |
| api-designer | `1.0-软件开发流程角色agent模型\研发\skill\design\api-designer.skill.md` | 阶段5 |
| schedule-template | `1.0-软件开发流程角色agent模型\项目管理\references\schedule-template.md` | 阶段6 |
| 后端开发Skill | `F:\projects\yudao-ai-his-backend\CLAUDE.md` | 阶段7 |
| 前端开发Skill | `F:\projects\yudao-ai-his-admin-ui\yudao-ai-his-admin-ui\CLAUDE.md` | 阥段8 |
| deep-research | 系统内置Skill | 阶段1、4 |
| code-review | 系统内置Skill | 阥段7、8 |

---

## 附录：模板文档路径索引

| 模板名称 | 文档路径 | 适用产出物 |
|-----------|----------|----------|
| prd-template | `1.0-软件开发流程角色agent模型\产品\references\prd-template.md` | PRD文档 |
| brd-template | `1.0-软件开发流程角色agent模型\产品\references\brd-template.md` | BRD文档 |
| srs-template | `1.0-软件开发流程角色agent模型\产品\references\srs-template.md` | 系统需求文档 |
| view-dashboard-template | `1.0-软件开发流程角色agent模型\产品\references\view-dashboard-template.md` | 原型图描述 |
| permission-matrix-template | `1.0-软件开发流程角色agent模型\产品\references\permission-matrix-template.md` | 权限矩阵 |
| schedule-template | `1.0-软件开发流程角色agent模型\项目管理\references\schedule-template.md` | 排期计划 |
| milestone-template | `1.0-软件开发流程角色agent模型\项目管理\references\milestone-template.md` | 里程碑计划 |
| workload-template | `1.0-软件开发流程角色agent模型\项目管理\references\workload-template.md` | 工作量估算 |

---

> **文档版本**: v1.0
> **创建日期**: 2026-06-19
> **适用项目**: 全流程软件开发组合工作流