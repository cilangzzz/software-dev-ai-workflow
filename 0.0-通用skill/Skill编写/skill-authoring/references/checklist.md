# Skill验证检查清单
# 用于验证Skill文件的完整性和质量

# ============================================
# 结构完整性检查
# ============================================
structure_check:
  yaml_format:
    - field: "skill.id"
      required: true
      check: "小写字母+连字符格式"
      example: "crud-designer"

    - field: "skill.name"
      required: true
      check: "中文或英文描述性名称"
      example: "CRUD代码生成"

    - field: "skill.version"
      required: true
      check: "语义化版本号格式"
      example: "1.0.0"

    - field: "skill.category"
      required: true
      check: "implement/design/analysis/review"
      example: "implement"

    - field: "skill.description"
      required: true
      check: "1-3句话功能描述"

    - field: "skill.priority"
      required: true
      check: "P0/P1/P2"

    - field: "trigger.keywords"
      required: true
      check: "至少3个触发关键词"

    - field: "input.parameters"
      required: true
      check: "每个参数有name/type/required/description"

    - field: "workflow.phases"
      required: true
      check: "至少2个阶段，每个阶段有steps"

    - field: "output.artifacts"
      required: true
      check: "至少1个输出产物"

    - field: "examples"
      required: true
      check: "至少1个完整示例"

  markdown_format:
    - field: "基本信息"
      required: true
      check: "包含名称、版本、所属部门、优先级"

    - field: "功能描述"
      required: true
      check: "清晰的功能描述"

    - field: "触发条件"
      required: true
      check: "包含命令触发和自然语言触发"

    - field: "输入参数"
      required: true
      check: "表格格式，包含参数名/类型/必填/描述"

    - field: "执行流程"
      required: true
      check: "步骤清晰，编号有序"

    - field: "输出格式"
      required: true
      check: "提供输出模板"

    - field: "使用示例"
      required: true
      check: "至少1个完整示例，包含输入和输出"

    - field: "质量标准"
      required: true
      check: "可度量的质量标准"

    - field: "依赖工具"
      required: true
      check: "列出使用的工具"

    - field: "注意事项"
      required: true
      check: "至少3条注意事项"

# ============================================
# 内容质量检查
# ============================================
content_check:
  description_quality:
    - rule: "功能描述无歧义"
      check: "描述中不应使用模糊词汇如'可能'、'大概'"

    - rule: "描述简洁明了"
      check: "不超过100字"

  trigger_quality:
    - rule: "关键词覆盖度高"
      check: "涵盖常见表达方式"

    - rule: "关键词互斥性好"
      check: "避免与其他Skill关键词冲突"

  parameter_quality:
    - rule: "参数类型正确"
      check: "string/number/boolean/array/object"

    - rule: "参数命名规范"
      check: "使用驼峰命名"

    - rule: "参数示例真实"
      check: "示例值真实可用"

    - rule: "枚举值完整"
      check: "enum字段列出所有选项"

  workflow_quality:
    - rule: "步骤清晰"
      check: "每个步骤有明确的action"

    - rule: "流程完整"
      check: "覆盖从输入到输出的完整流程"

    - rule: "时间估算合理"
      check: "duration字段合理"

  example_quality:
    - rule: "示例真实可用"
      check: "输入示例可直接使用"

    - rule: "输出示例完整"
      check: "输出展示完整产物"

    - rule: "示例数量足够"
      check: "至少1个完整示例"

# ============================================
# 引用关系检查
# ============================================
reference_check:
  path_validity:
    - rule: "引用路径正确"
      check: "使用Read工具验证文件存在"

    - rule: "章节引用正确"
      check: "sections字段引用章节存在"

  collaboration_validity:
    - rule: "关联Skill存在"
      check: "使用Glob工具验证Skill文件存在"

    - rule: "协作关系明确"
      check: "upstream/downstream/parallel/reference正确"

    - rule: "数据流定义清晰"
      check: "data_flow字段描述清晰"

# ============================================
# 命名规范检查
# ============================================
naming_check:
  skill_id:
    - rule: "小写字母+连字符"
      pattern: "^[a-z][a-z0-9-]*[a-z0-9]$"
      examples: ["crud-designer", "api-designer", "security-threat-model"]

    - rule: "语义清晰"
      check: "ID应能反映Skill功能"

    - rule: "唯一性"
      check: "使用Grep工具检查是否已存在"

  parameter_name:
    - rule: "驼峰命名"
      pattern: "^[a-z][a-zA-Z0-9]*$"
      examples: ["projectName", "techStack"]

  file_name:
    - rule: "Skill文件命名"
      pattern: "{skill_id}.{yaml/md}"
      examples: ["crud-designer.yaml", "security-threat-model.md"]

# ============================================
# 格式规范检查
# ============================================
format_check:
  yaml:
    - rule: "缩进一致"
      check: "使用2空格缩进"

    - rule: "层级正确"
      check: "父子关系正确"

    - rule: "注释规范"
      check: "使用#注释，注释行前有空行"

  markdown:
    - rule: "标题层级"
      check: "# ## ### #### 层级有序"

    - rule: "表格格式"
      check: "| 字段名 | 类型 | 描述 | 格式"

    - rule: "代码块"
      check: "使用```标记，指定语言"

    - rule: "链接格式"
      check: "[文本](路径)格式"

# ============================================
# 质量标准检查
# ============================================
quality_check:
  standards:
    - rule: "可度量性"
      check: "质量标准应有具体数值或检查方式"

    - rule: "合理性"
      check: "阈值设置合理"

  completeness:
    - rule: "必填字段100%"
      check: "所有required字段已填写"

    - rule: "示例覆盖率"
      threshold: ">= 80%"
      check: "关键场景有示例覆盖"

# ============================================
# 验证流程
# ============================================
validation_workflow:
  steps:
    - step: 1
      name: "结构检查"
      action: "检查必填字段完整性"
      tool: "Read"

    - step: 2
      name: "命名检查"
      action: "检查命名是否符合规范"
      tool: "Grep"

    - step: 3
      name: "引用检查"
      action: "验证引用路径和协作关系"
      tool: "Glob/Read"

    - step: 4
      name: "内容检查"
      action: "检查内容质量"
      tool: "人工审核"

    - step: 5
      name: "格式检查"
      action: "检查格式规范"
      tool: "格式解析"

    - step: 6
      name: "输出报告"
      action: "生成验证报告"

# ============================================
# 验证报告模板
# ============================================
validation_report_template: |
  # Skill验证报告

  ## 基本信息
  - Skill ID: {skill_id}
  - 验证时间: {timestamp}
  - 验证状态: {PASS/FAIL/WARNING}

  ## 结构完整性
  | 检查项 | 状态 | 说明 |
  |--------|------|------|
  | {field1} | ✓/✗ | {description} |
  | {field2} | ✓/✗ | {description} |

  ## 内容质量
  | 检查项 | 状态 | 说明 |
  |--------|------|------|
  | {item1} | ✓/✗ | {description} |

  ## 引用关系
  | 检查项 | 状态 | 说明 |
  |--------|------|------|
  | {reference1} | ✓/✗ | {description} |

  ## 问题清单
  1. {问题描述}
  2. {问题描述}

  ## 建议修改
  - {建议1}
  - {建议2}