# Agent 配置验证检查清单
# 用于验证 Agent 配置文件的完整性和正确性

# ============================================
# 结构完整性检查
# ============================================

structure_check:
  basic_fields:
    - item: "role.id 已填写"
      check: "检查是否存在 role.id 字段"
      format: "小写字母+连字符，如 java-developer"

    - item: "role.name 已填写"
      check: "检查是否存在 role.name 字段"
      format: "中文描述性名称"

    - item: "role.category 已填写"
      check: "检查是否存在 role.category 字段"
      valid_values: ["backend", "frontend", "data", "ops", "test", "product", "design", "security"]

    - item: "role.tech_stack 已填写"
      check: "检查是否存在 role.tech_stack 字段"
      format: "技术栈标识，如 java/vue/qt"

    - item: "role.version 已填写"
      check: "检查是否存在 role.version 字段"
      format: "语义化版本号，如 1.0.0"

    - item: "role.description 已填写"
      check: "检查是否存在 role.description 字段"
      requirement: "描述清晰，1-3句话"

    - item: "role.created_at 已填写"
      check: "检查是否存在 role.created_at 字段"
      format: "YYYY-MM-DD 格式"

  yaml_syntax:
    - item: "YAML 格式正确"
      check: "使用 YAML 解析器验证"
      common_errors:
        - "缩进错误（使用空格而非制表符）"
        - "冒号后缺少空格"
        - "字符串未正确引用"

    - item: "层级结构正确"
      check: "检查 YAML 层级是否符合模板"

# ============================================
# 能力定义检查
# ============================================

capabilities_check:
  core_skills:
    - item: "core_skills 存在且非空"
      check: "检查 capabilities.core_skills 字段"
      requirement: "至少定义 2 个核心技能"

    - item: "每个技能包含 skill 字段"
      check: "检查每个技能的 skill 名称"

    - item: "每个技能包含 level 字段"
      check: "检查能力等级"
      valid_values: ["expert", "advanced", "intermediate", "beginner"]

    - item: "每个技能包含 components 字段"
      check: "检查具体能力项"
      requirement: "至少包含 2 个具体能力项"

    - item: "能力等级分布合理"
      check: "分析能力等级分布"
      recommendation: "核心技能 expert，相关技能 advanced/intermediate"

  tech_stack:
    - item: "tech_stack 定义存在"
      check: "检查 capabilities.tech_stack 字段"

    - item: "语言定义明确"
      check: "检查 language 字段"
      format: "语言名称 + 版本，如 Java 17+"

    - item: "框架定义明确"
      check: "检查 framework 字段（如适用）"

    - item: "其他技术栈定义合理"
      check: "检查 database/build/orm 等字段"

# ============================================
# Skill 配置检查
# ============================================

skills_config_check:
  skills_to_load:
    - item: "skills_to_load 存在"
      check: "检查 skills_to_load 字段"

    - item: "tech_specific 或 common 至少存在一个"
      check: "检查技能加载分类"

    - item: "每个 skill 包含 path"
      check: "检查 skill 路径"
      format: "相对路径，如 backend/java/scaffold.yaml"

    - item: "每个 skill 包含 description"
      check: "检查 skill 描述"

    - item: "优先级设置合理"
      check: "检查 priority 字段（如存在）"
      valid_values: ["P0", "P1", "P2"]

    - item: "skill 路径引用正确"
      check: "验证 skill 文件是否存在"
      action: "使用 Glob 工具搜索对应文件"

  skills_to_exclude:
    - item: "skills_to_exclude 结构正确"
      check: "检查排除配置结构"

    - item: "每个排除包含 pattern"
      check: "检查排除模式"

    - item: "每个排除包含 reason"
      check: "检查排除原因"
      requirement: "排除原因清晰合理"

# ============================================
# 规范定义检查
# ============================================

conventions_check:
  naming_conventions:
    - item: "命名规范存在"
      check: "检查 naming_conventions 字段"

    - item: "至少定义一种命名规范"
      check: "检查 classes/files/methods/variables 等字段"

    - item: "每个规范包含 rule"
      check: "检查规则描述"

    - item: "每个规范包含 examples"
      check: "检查示例"
      requirement: "至少提供 2 个示例"

  project_structure:
    - item: "项目结构模板存在"
      check: "检查 project_structure 字段"

    - item: "结构描述清晰"
      check: "检查 description 字段"

    - item: "结构示例完整"
      check: "检查 structure 字段"
      requirement: "包含主要目录结构"

  code_style:
    - item: "代码风格定义存在"
      check: "检查 code_style 字段"

    - item: "风格规则有示例"
      check: "检查是否包含 example"

# ============================================
# 工作流检查
# ============================================

workflow_check:
  - item: "workflow 存在"
    check: "检查 workflow 字段"

  - item: "典型工作流存在"
    check: "检查 typical_flow 字段"

  - item: "工作流步骤完整"
    check: "检查步骤数量"
    recommendation: "至少包含 3 个步骤"

  - item: "每个步骤包含名称"
    check: "检查 step.name 字段"

  - item: "每个步骤包含 skill 引用"
    check: "检查 step.skill 字段"

  - item: "skill 引用正确"
    check: "验证 skill 是否在 skills_to_load 中定义"

# ============================================
# 内容质量检查
# ============================================

content_quality_check:
  clarity:
    - item: "角色描述清晰无歧义"
      check: "审查 role.description 内容"

    - item: "技能名称清晰"
      check: "审查 skill 名称是否专业准确"

    - item: "能力项具体可操作"
      check: "审查 components 是否具体"

  completeness:
    - item: "核心技能覆盖主要职责"
      check: "对比角色定位和技能定义"

    - item: "技术栈覆盖核心工具"
      check: "检查技术栈是否完整"

    - item: "注意事项覆盖常见问题"
      check: "检查 notes 字段"
      recommendation: "至少 3 条注意事项"

  correctness:
    - item: "技术栈版本合理"
      check: "对比当前主流版本"

    - item: "能力等级合理"
      check: "对比角色定位和能力等级"

    - item: "skill 路径正确"
      check: "验证路径文件存在"

# ============================================
# 协作关系检查（可选）
# ============================================

collaboration_check:
  - item: "协作关系定义（可选）"
    check: "检查 collaboration 字段"

  - item: "上游角色合理"
    check: "检查 upstream 定义"

  - item: "下游角色合理"
    check: "检查 downstream 定义"

  - item: "并行角色合理"
    check: "检查 parallel 定义"

# ============================================
# 验证报告模板
# ============================================

validation_report_template: |
  # Agent 配置验证报告
  
  ## 基本信息
  - 角色 ID: {role.id}
  - 角色名称: {role.name}
  - 验证时间: {timestamp}
  
  ## 检查结果
  
  | 类别 | 检查项数 | 通过数 | 失败数 | 状态 |
  |------|---------|--------|--------|------|
  | 结构完整性 | {count} | {pass} | {fail} | ✅/⚠️/❌ |
  | 能力定义 | {count} | {pass} | {fail} | ✅/⚠️/❌ |
  | Skill配置 | {count} | {pass} | {fail} | ✅/⚠️/❌ |
  | 规范定义 | {count} | {pass} | {fail} | ✅/⚠️/❌ |
  | 工作流 | {count} | {pass} | {fail} | ✅/⚠️/❌ |
  | 内容质量 | {count} | {pass} | {fail} | ✅/⚠️/❌ |
  
  ## 问题详情
  
  ### 🔴 必须修复
  {critical_issues}
  
  ### 🟡 建议改进
  {suggestion_issues}
  
  ## 总体评价
  {overall_assessment}
  
  ## 下一步建议
  {next_steps}