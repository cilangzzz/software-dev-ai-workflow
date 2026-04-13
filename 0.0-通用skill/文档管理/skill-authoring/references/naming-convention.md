# Skill命名规范
# 定义Skill、参数、文件等的命名规范

# ============================================
# Skill ID命名规范
# ============================================
skill_id_rules:
  format:
    pattern: "^[a-z][a-z0-9-]*[a-z0-9]$"
    description: "小写字母开头，小写字母或数字结尾，中间可包含连字符"
    examples:
      valid:
        - "crud-designer"
        - "api-designer"
        - "security-threat-model"
        - "user-story-generator"
        - "code-review"
        - "scaffold"
      invalid:
        - "CRUD-Designer"  # 大写字母
        - "crud_designer"  # 下划线
        - "-crud-designer" # 连字符开头
        - "crud-designer-" # 连字符结尾
        - "1crud-designer" # 数字开头

  naming_principles:
    - principle: "语义清晰"
      description: "ID应能直接反映Skill功能"
      examples:
        - "crud-designer → CRUD代码生成"
        - "security-threat-model → 安全威胁模型"

    - principle: "避免过长"
      description: "建议不超过30个字符"
      examples:
        - "valid: security-scan"
        - "invalid: security-vulnerability-scan-and-analysis"

    - principle: "避免缩写歧义"
      description: "使用通用缩写或全称"
      examples:
        - "valid: api-designer"
        - "ambiguous: apid"  # 不明确

  category_prefix:
    description: "可选的类别前缀"
    categories:
      implement: "实现类，如 crud-, api-, entity-"
      design: "设计类，如 arch-, db-, ui-"
      analysis: "分析类，如 threat-, risk-, quality-"
      review: "审查类，如 code-, requirement-, design-review"

# ============================================
# Skill显示名称规范
# ============================================
display_name_rules:
  format:
    chinese: "中文描述性名称，如 'CRUD代码生成器'"
    english: "英文描述性名称，如 'CRUD Code Generator'"

  principles:
    - "简洁明了"
    - "易于理解"
    - "避免技术术语堆砌"

# ============================================
# 参数命名规范
# ============================================
parameter_rules:
  format:
    snake_case:
      pattern: "^[a-z][a-z0-9_]*$"
      description: "小写字母开头，可包含下划线"
      examples: ["project_name", "tech_stack", "feature_list"]
      preferred: "YAML格式Skill"

    camel_case:
      pattern: "^[a-z][a-zA-Z0-9]*$"
      description: "小写字母开头，驼峰命名"
      examples: ["projectName", "techStack", "featureList"]
      preferred: "代码中使用"

  naming_principles:
    - principle: "语义明确"
      description: "参数名应能反映参数用途"
      examples:
        - "valid: project_name"
        - "invalid: pn"  # 缩写不明确

    - principle: "避免歧义"
      description: "避免使用多义词汇"
      examples:
        - "valid: output_directory"
        - "ambiguous: path"

  common_parameters:
    - name: "project_name"
      description: "项目名称"
      type: "string"

    - name: "tech_stack"
      description: "技术栈"
      type: "string"

    - name: "output_path"
      description: "输出路径"
      type: "string"

    - name: "features"
      description: "功能特性列表"
      type: "array"

# ============================================
# 文件命名规范
# ============================================
file_rules:
  skill_file:
    yaml: "{skill_id}.yaml"
    markdown: "{skill_id}.md"
    examples:
      - "crud-designer.yaml"
      - "security-threat-model.md"

  reference_file:
    format: "{purpose}.md"
    examples:
      - "tech-stack.md"
      - "templates.md"
      - "checklist.md"

  template_file:
    format: "skill-{type}-{variant}.{ext}"
    examples:
      - "skill-yaml-tech.yaml"
      - "skill-md-process.md"
      - "role-config.yaml"

  meta_file:
    format: "_meta.json"
    description: "固定名称"

  config_file:
    format: "_{config_type}.{ext}"
    examples:
      - "_rules.yaml"
      - "role-config.yaml"
      - "skill-collaboration.yaml"

# ============================================
# 目录命名规范
# ============================================
directory_rules:
  skill_directory:
    format: "{department}/{category}/"
    examples:
      - "研发/backend/java/"
      - "安全/skill/"
      - "产品/skill/"

  template_directory:
    format: "templates/"
    description: "固定名称"

  reference_directory:
    format: "references/"
    description: "固定名称"

  scripts_directory:
    format: "scripts/"
    description: "可选，存放脚本"

# ============================================
# 命名冲突检测
# ============================================
conflict_detection:
  steps:
    - step: 1
      name: "Skill ID检测"
      action: "使用Grep搜索现有Skill ID"
      command: "Grep pattern: 'skill_id: {new_id}'"

    - step: 2
      name: "关键词检测"
      action: "检查触发关键词是否冲突"
      command: "Grep pattern: 'keywords:.*{keyword}'"

    - step: 3
      name: "命令检测"
      action: "检查命令是否冲突"
      command: "Grep pattern: '/{command}'"

# ============================================
# 命名变更规范
# ============================================
renaming_rules:
  when_to_rename:
    - "功能范围发生变化"
    - "ID语义不清晰"
    - "与其他Skill冲突"

  rename_process:
    - step: 1
      name: "创建新Skill"
      action: "使用新ID创建Skill"

    - step: 2
      name: "更新引用"
      action: "更新所有引用此Skill的文件"

    - step: 3
      name: "标记旧Skill废弃"
      action: "在旧Skill添加deprecated标记"

    - step: 4
      name: "更新文档"
      action: "更新产出物清单等文档"

  deprecated_marking:
    yaml: |
      skill:
        id: "{old_id}"
        deprecated: true
        deprecated_reason: "{废弃原因}"
        replaced_by: "{new_id}"

    markdown: |
      > **注意**: 此Skill已废弃，请使用 [{new_id}](skill/{new_id}.md) 替代。
      > 废弃原因: {废弃原因}