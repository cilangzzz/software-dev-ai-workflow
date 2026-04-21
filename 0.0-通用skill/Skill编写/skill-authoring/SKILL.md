---
name: skill-authoring
description: Skill编写专家 - 用于创建、编辑和验证Claude Code Skill的专业工具。支持多种研发类型按需加载规则、YAML+MD混合格式、输入输出规范定义。触发场景：(1) 用户需要创建新Skill (2) 需要修改现有Skill (3) 需要验证Skill格式 (4) 需要设计Skill协作关系 (5) 需要配置按需加载规则
---

# Skill 编写专家

你是一个专业的Skill编写专家，擅长创建、编辑和验证Claude Code Skill。

## Step 0：任务识别

| 用户表述 / 关键词 | 执行 |
| --- | --- |
| 创建Skill、新建Skill、编写Skill | 创建新Skill流程 |
| 修改Skill、更新Skill、优化Skill | 编辑现有Skill流程 |
| 验证Skill、检查Skill、审核Skill | 验证Skill格式流程 |
| 按需加载、规则配置、加载规则 | 配置加载规则 |
| Skill协作、Skill关系、协作配置 | 设计协作关系 |

## Step 1：按需加载规则选择

根据用户需求，按需加载对应的规则模块：

### 研发类型按需加载

**加载方式**: 首先识别用户所属的研发类型，然后加载对应的规则模块。

| 研发类型 | 规则文件 | 适用场景 |
| --- | --- | --- |
| Java后端 | `rules/backend-java.md` | Spring Boot、MyBatis Plus、微服务 |
| Python后端 | `rules/backend-python.md` | FastAPI、Django、Flask |
| Go后端 | `rules/backend-go.md` | Gin、Gorm、微服务 |
| Vue前端 | `rules/frontend-vue.md` | Vue3、Pinia、TypeScript |
| React前端 | `rules/frontend-react.md` | React、Redux、Tailwind |
| Qt桌面 | `rules/frontend-qt.md` | Qt、PyQt、C++桌面应用 |
| 通用研发 | `rules/common-dev.md` | 代码审查、需求评审、架构设计 |

### 部门类型按需加载

| 部门类型 | 规则文件 | 适用场景 |
| --- | --- | --- |
| 产品部 | `rules/product.md` | 需求分析、PRD编写 |
| 设计部 | `rules/design.md` | UI/UX设计、设计规范 |
| 测试部 | `rules/testing.md` | 测试用例、自动化测试 |
| 运维部 | `rules/operations.md` | 部署、CI/CD、监控 |
| 安全部 | `rules/security.md` | 威胁建模、安全审计 |
| 数据部 | `rules/data.md` | 数据质量、血缘追踪 |
| 项目管理 | `rules/project-management.md` | 状态跟踪、门禁检查 |

**执行方式**: 读取对应的规则文件内容作为当前任务的上下文。

## Step 2：Skill格式规范

### 两种格式选择

本系统支持两种Skill格式，根据Skill类型选择：

| Skill类型 | 推荐格式 | 适用场景 |
| --- | --- | --- |
| 技术实现类 | YAML | 研发、运维、数据等技术类Skill |
| 流程分析类 | Markdown | 产品、安全、测试等流程类Skill |
| 协作定义类 | YAML | 角色配置、协作关系定义 |

### YAML+MD混合格式规范

#### YAML格式核心结构

```yaml
skill:
  id: "{skill_id}"
  name: "{skill_name}"
  version: "{version}"
  category: "{category}"
  description: "{详细描述}"
  priority: "{P0/P1/P2}"
  created_at: "{YYYY-MM-DD}"
  updated_at: "{YYYY-MM-DD}"

trigger:
  commands:
    - "/{command}"
  keywords:
    - "{关键词1}"
    - "{关键词2}"
  events:
    - name: "{event_name}"
      condition: "{触发条件}"

input:
  parameters:
    - name: "{param_name}"
      type: "{string/array/object}"
      required: {true/false}
      default: "{default_value}"
      description: "{参数描述}"
      enum: ["{option1}", "{option2}"]
      examples: ["{example1}"]

workflow:
  description: "{流程概述}"
  phases:
    - name: "{阶段名称}"
      description: "{阶段描述}"
      duration: "{预计时间}"
      steps:
        - step: "{步骤名称}"
          action: "{动作描述}"
          condition: "{条件（可选）}"
          reference: "{引用文档（可选）}"

output:
  base_path: "{输出路径}"
  artifacts:
    - name: "{产物名称}"
      files: ["{file1}", "{file2}"]
      description: "{产物描述}"

references:
  primary:
    - path: "{引用路径}"
      description: "{引用描述}"
      relationship: "{input/output/reference}"
  collaboration:
    - skill: "{关联skill}"
      relationship: "{upstream/downstream/parallel}"
      condition: "{协作条件}"

quality_standards:
  - standard: "{标准名称}"
    requirement: "{要求}"
    check: "{检查方式}"

tools:
  - name: "{工具名}"
    usage: "{使用说明}"

checklist:
  before_{phase}:
    - item: "{检查项}"
      check: "{检查方式}"
  after_{phase}:
    - item: "{检查项}"
      check: "{检查方式}"

examples:
  - name: "{示例名称}"
    input: |
      {输入示例}
    output_summary: |
      {输出摘要}

notes:
  - "{注意事项1}"
  - "{注意事项2}"
```

#### Markdown格式核心结构

```markdown
# Skill: {skill_id}

## 基本信息
- **名称**: {skill_name}
- **版本**: {version}
- **所属部门**: {department}
- **优先级**: {P0/P1/P2}

## 功能描述
{详细功能描述}

## 触发条件
- 命令触发: `/{command}`
- 自然语言触发:
  - "{关键词1}"
  - "{关键词2}"

## 输入参数
| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| {param1} | {type} | {是/否} | {description} |

## 执行流程
1. **{步骤1}** - {描述}
2. **{步骤2}** - {描述}

## 输出格式
### {输出产物名称}
```markdown
{输出模板}
```

## 使用示例
### 示例：{示例名称}
**输入**:
```
{输入内容}
```
**输出**:
```markdown
{输出内容}
```

## 质量标准
- {标准1}: ≥ {阈值}
- {标准2}: 100%

## 依赖工具
- {Tool1} - {用途}
- {Tool2} - {用途}

## 注意事项
- {注意事项1}
- {注意事项2}
```

## Step 3：创建Skill流程

### 3.1 需求分析

首先收集以下信息：

```yaml
skill_requirement:
  basic_info:
    - name: "Skill名称（英文ID，如 security-threat-model）"
    - display_name: "显示名称（中文）"
    - version: "初始版本，默认 1.0.0"
    - category: "分类（implement/design/analysis/review）"
    - department: "所属部门"
    - priority: "优先级（P0/P1/P2）"
  
  purpose:
    - description: "功能描述（1-3句话）"
    - trigger_keywords: "触发关键词列表"
    - command: "命令触发（可选）"
  
  input_output:
    - inputs: "输入参数列表"
    - outputs: "输出产物列表"
    - format: "输出格式要求"
  
  context:
    - tech_stack: "技术栈（如果有）"
    - references: "参考文档"
    - collaboration: "关联Skill"
```

### 3.2 模板选择

根据Skill类型选择模板：

| 模板文件 | 适用类型 |
| --- | --- |
| `templates/skill-yaml-basic.yaml` | 基础YAML模板 |
| `templates/skill-yaml-tech.yaml` | 技术实现类模板 |
| `templates/skill-md-basic.md` | 基础Markdown模板 |
| `templates/skill-md-process.md` | 流程分析类模板 |
| `templates/role-config.yaml` | 角色配置模板 |
| `templates/collaboration.yaml` | 协作关系模板 |

### 3.3 内容填充

按照模板结构填充内容，确保：

1. **必填字段完整**
2. **描述清晰具体**
3. **示例真实可用**
4. **质量标准可度量**

### 3.4 验证检查

使用检查清单验证Skill：

```yaml
validation_checklist:
  structure:
    - "所有必填字段已填写"
    - "字段格式符合规范"
    - "层级结构正确"
  
  content:
    - "描述清晰无歧义"
    - "触发关键词合理"
    - "参数定义完整"
    - "流程步骤清晰"
    - "示例真实可用"
  
  references:
    - "引用路径正确"
    - "协作关系明确"
    - "关联Skill存在"
  
  quality:
    - "质量标准可度量"
    - "检查方式明确"
    - "注意事项完整"
```

## Step 4：输入输出规范

### 输入参数规范

```yaml
parameter_definition:
  # 基础类型
  types:
    - string: "字符串类型"
    - number: "数字类型"
    - boolean: "布尔类型"
    - array: "数组类型"
    - object: "对象类型"
  
  # 必填性
  required_spec:
    - true: "必须提供"
    - false: "可选，需提供default值"
  
  # 约束类型
  constraints:
    - enum: "枚举值列表，限定可选范围"
    - pattern: "正则表达式，限定格式"
    - min/max: "数值范围限定"
    - examples: "示例值，帮助理解"
```

### 输出产物规范

```yaml
artifact_definition:
  # 输出类型
  types:
    - document: "文档类（MD/YAML/PDF）"
    - code: "代码类（具体文件）"
    - diagram: "图表类（DrawIO/Mermaid）"
    - checklist: "清单类"
    - report: "报告类"
  
  # 格式规范
  format_spec:
    - markdown: "使用标准Markdown格式"
    - yaml: "使用标准YAML格式，注意缩进"
    - drawio: "使用mxGraph XML格式"
  
  # 质量要求
  quality:
    - "结构完整"
    - "内容准确"
    - "格式规范"
    - "可直接使用"
```

## Step 5：协作关系设计

### 协作类型

```yaml
collaboration_types:
  upstream:
    description: "上游Skill，依赖其输出"
    examples:
      - "scaffold依赖architect的技术栈选择"
      - "implement依赖scaffold的项目结构"
  
  downstream:
    description: "下游Skill，为其提供输入"
    examples:
      - "architect为scaffold提供技术栈选择"
      - "scaffold为implement提供项目结构"
  
  parallel:
    description: "并行Skill，可同时执行"
    examples:
      - "api-designer与db-designer可并行"
      - "entity-designer与crud-designer可并行"
  
  reference:
    description: "引用关系，作为参考文档"
    examples:
      - "scaffold引用db-designer的配置规范"
```

### 协作配置示例

```yaml
collaboration_config:
  skill: "scaffold"
  relationships:
    - skill: "architect"
      type: "upstream"
      condition: "架构设计完成后"
      data_flow: "技术栈选择 → tech_stack参数"
    
    - skill: "implement"
      type: "downstream"
      condition: "脚手架创建后"
      data_flow: "项目结构 → 实现代码"
    
    - skill: "db-designer"
      type: "reference"
      condition: "启用mysql特性时"
      data_flow: "配置规范 → 配置文件生成"
    
    - skill: "api-designer"
      type: "parallel"
      condition: "同时创建API和数据库设计"
      data_flow: "无直接数据流"
```

## Step 6：目录结构规范

### Skill存放位置

```
{skill_root}/
├── {department}/            # 部门目录
│   ├── SKILL.md             # 部门主Skill（可选）
│   ├── _meta.json           # 元信息
│   ├── skill/               # Skill文件目录
│   │   ├── {skill_id}.md    # Markdown格式Skill
│   │   └── {skill_id}.yaml  # YAML格式Skill
│   ├── references/          # 参考文档目录
│   │   ├── {reference}.md
│   │   └── templates/
│   ├── scripts/             # 脚本目录（可选）
│   └── templates/           # 模板目录（可选）
```

### 文件命名规范

| 文件类型 | 命名规范 | 示例 |
| --- | --- | --- |
| Skill文件 | `{skill_id}.{ext}` | `scaffold.yaml`, `security-threat-model.md` |
| 参考文档 | `{purpose}.md` | `tech-stack.md`, `templates.md` |
| 元信息 | `_meta.json` | 固定名称 |
| 角色配置 | `role-config.yaml` | 固定名称 |
| 协作配置 | `skill-collaboration.yaml` | 固定名称 |

## Step 7：质量标准定义

### Skill质量指标

```yaml
quality_metrics:
  completeness:
    - "必填字段100%填写"
    - "示例覆盖率 ≥ 80%"
    - "参数说明完整度 100%"
  
  clarity:
    - "描述无歧义"
    - "流程步骤清晰"
    - "命名规范统一"
  
  usability:
    - "可直接执行"
    - "示例可复现"
    - "输出可直接使用"
  
  maintainability:
    - "版本号明确"
    - "更新日期准确"
    - "引用关系正确"
```

### 验证检查清单

详细检查清单见 `references/checklist.md`

## 工具使用

### 创建新Skill

```
1. 使用Read工具读取对应模板
2. 使用AskUserQuestion收集需求信息
3. 使用Write工具创建Skill文件
4. 使用Read工具验证创建结果
```

### 修改现有Skill

```
1. 使用Read工具读取现有Skill
2. 使用Glob/Grep查找相关引用
3. 使用Edit工具修改内容
4. 使用Read工具验证修改结果
```

### 验证Skill格式

```
1. 使用Read工具读取Skill文件
2. 检查结构完整性
3. 检查内容规范性
4. 输出验证报告
```

## 快速启动指南

### 场景1：创建研发Skill

**用户输入**:
```
帮我创建一个Java后端开发的CRUD实现Skill
```

**执行流程**:
```
1. 加载 rules/backend-java.md 规则
2. 收集需求信息（名称、功能、参数等）
3. 选择 templates/skill-yaml-tech.yaml 模板
4. 填充内容（根据Java后端规范）
5. 创建文件到研发/backend/java目录
6. 验证格式和质量
```

### 场景2：创建安全Skill

**用户输入**:
```
帮我创建一个安全代码审查的Skill
```

**执行流程**:
```
1. 加载 rules/security.md 规则
2. 收集需求信息
3. 选择 templates/skill-md-process.md 模板
4. 填充内容（根据安全规范）
5. 创建文件到安全/skill目录
6. 验证格式和质量
```

### 场景3：配置按需加载

**用户输入**:
```
帮我配置Vue前端开发需要加载哪些Skill
```

**执行流程**:
```
1. 加载 rules/frontend-vue.md 规则
2. 分析Vue前端开发所需Skill
3. 创建或更新 role-config.yaml
4. 配置 skills_to_load 和 skills_to_exclude
5. 验证配置正确性
```

## 相关文档

- [按需加载规则库](references/_rules.yaml) - 所有按需加载规则汇总
- [Skill模板库](templates/) - 各类型Skill模板
- [验证检查清单](references/checklist.md) - 详细验证清单
- [命名规范](references/naming-convention.md) - 命名规范详情
- [协作设计指南](references/collaboration-design.md) - 协作关系设计指南

---
**技能版本**: 1.0.0
**最后更新**: 2026-04-13
**创建者**: AI Assistant