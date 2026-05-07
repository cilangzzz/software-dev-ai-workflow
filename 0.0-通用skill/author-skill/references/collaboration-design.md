# Skill协作关系设计指南
# 定义Skill之间的上下游关系、数据流和同步点

# ============================================
# 协作关系类型
# ============================================
relationship_types:
  upstream:
    definition: "上游依赖 - 本Skill依赖上游Skill的输出作为输入"
    characteristics:
      - "必须等待上游Skill完成"
      - "数据单向流动：上游→本Skill"
      - "required字段标识是否必须"
    examples:
      - skill: "scaffold"
        upstream: "architect"
        data_flow: "技术栈选择 → tech_stack参数"

      - skill: "implement"
        upstream: "scaffold"
        data_flow: "项目结构 → 代码文件位置"

  downstream:
    definition: "下游输出 - 本Skill的输出供下游Skill使用"
    characteristics:
      - "本Skill完成后触发下游"
      - "数据单向流动：本Skill→下游"
      - "可定义触发条件"
    examples:
      - skill: "architect"
        downstream: "scaffold"
        data_flow: "架构设计 → 项目创建"

      - skill: "scaffold"
        downstream: "implement"
        data_flow: "脚手架 → 功能实现"

  parallel:
    definition: "并行执行 - 多个Skill可同时执行"
    characteristics:
      - "无数据依赖"
      - "在同步点汇聚"
      - "提高执行效率"
    examples:
      - skills: ["api-designer", "db-designer"]
        condition: "同时设计API和数据库"
        sync_point: "设计完成后统一评审"

      - skills: ["entity-designer", "crud-designer"]
        condition: "同时生成实体和CRUD代码"
        sync_point: "代码生成完成后统一检查"

  reference:
    definition: "引用关系 - 本Skill引用其他Skill作为参考文档"
    characteristics:
      - "非执行依赖"
      - "引用规范或模板"
      - "按需引用"
    examples:
      - skill: "scaffold"
        reference: "db-designer"
        sections: ["数据库配置规范"]

# ============================================
# 数据流定义规范
# ============================================
data_flow_definition:
  structure: |
    - name: "{数据流名称}"
      source_skill: "{源Skill}"
      source_output: "{源Skill的输出字段}"
      target_skill: "{目标Skill}"
      target_input: "{目标Skill的输入参数}"
      transformation: "{数据转换规则（可选）}"

  examples:
    - name: "技术栈传递"
      source_skill: "architect"
      source_output: "tech_stacks.selected"
      target_skill: "scaffold"
      target_input: "tech_stack"
      transformation: "直接传递"

    - name: "实体类映射"
      source_skill: "db-designer"
      source_output: "tables"
      target_skill: "entity-designer"
      target_input: "table_definitions"
      transformation: "表结构 → DO类字段映射"

# ============================================
# 同步点定义规范
# ============================================
sync_point_definition:
  structure: |
    - name: "{同步点名称}"
      skills: ["{Skill1}", "{Skill2}", ...]
      condition: "{同步条件}"
      action: "{同步后动作}"
      timeout: "{超时时间（可选）}"

  examples:
    - name: "设计评审同步点"
      skills: ["api-designer", "db-designer", "ui-designer"]
      condition: "所有设计Skill完成"
      action: "触发design-review Skill"
      timeout: "30分钟"

# ============================================
# 协作流程设计
# ============================================
workflow_design:
  principles:
    - principle: "最小依赖"
      description: "减少Skill间的强依赖，提高独立性"

    - principle: "清晰边界"
      description: "每个Skill有明确的输入输出边界"

    - principle: "可追溯性"
      description: "数据流要有清晰的来源记录"

    - principle: "容错处理"
      description: "定义异常情况的处理流程"

  design_steps:
    - step: 1
      name: "识别Skill"
      action: "确定参与协作的Skill列表"

    - step: 2
      name: "分析依赖"
      action: "分析Skill间的数据依赖关系"

    - step: 3
      name: "定义数据流"
      action: "明确每个依赖的数据流"

    - step: 4
      name: "识别并行点"
      action: "识别可并行执行的Skill"

    - step: 5
      name: "定义同步点"
      action: "定义并行Skill的同步点"

    - step: 6
      name: "绘制流程图"
      action: "绘制协作流程图"

# ============================================
# 协作流程图规范
# ============================================
flow_diagram:
  format: "Mermaid或DrawIO"

  mermaid_example: |
    ```mermaid
    graph TD
      A[architect] -->|tech_stack| B[scaffold]
      B -->|project_structure| C[implement]
      C --> D[code-review]

      E[api-designer] -.->|reference| B
      F[db-designer] -.->|reference| B

      G[entity-designer] --> H[crud-designer]

      E --> I{设计评审}
      F --> I
      G --> I
      I --> C
    ```

  symbols:
    - symbol: "实线箭头 (-->)"
      meaning: "上游→下游强依赖"

    - symbol: "虚线箭头 (-.->)"
      meaning: "引用关系"

    - symbol: "菱形节点 ({})"
      meaning: "同步点"

    - symbol: "方框节点 ([])"
      meaning: "Skill节点"

# ============================================
# 条件触发规范
# ============================================
condition_triggers:
  event_based:
    - event: "skill_completed"
      description: "Skill完成时触发下游"

    - event: "artifact_generated"
      description: "特定产物生成时触发"

    - event: "quality_check_passed"
      description: "质量检查通过后触发"

  state_based:
    - state: "architecture_completed"
      description: "架构设计完成"

    - state: "project_initialized"
      description: "项目初始化完成"

    - state: "design_reviewed"
      description: "设计评审完成"

  custom:
    - condition: "features contains 'mysql'"
      description: "启用mysql特性时触发"

    - condition: "tech_stack == 'spring-boot'"
      description: "Spring Boot技术栈时触发"

# ============================================
# 协作配置示例
# ============================================
config_example:
  skill: "scaffold"
  relationships:
    upstream:
      - skill: "architect"
        condition: "架构设计完成且为新项目"
        required: true
        data_flow:
          from: "tech_stacks.selected.identifier"
          to: "input.parameters.tech_stack"

    downstream:
      - skill: "implement"
        condition: "脚手架创建成功"
        data_flow:
          from: "output.base_path"
          to: "input.parameters.project_path"

      - skill: "code-review"
        condition: "代码文件生成后"
        data_flow:
          from: "output.artifacts[code_files]"
          to: "input.parameters.review_paths"

    parallel:
      - skill: "api-designer"
        condition: "同时创建API设计"
        sync_point: "设计完成后"

      - skill: "db-designer"
        condition: "同时创建数据库设计"
        sync_point: "设计完成后"

    reference:
      - skill: "db-designer"
        condition: "启用mysql特性时"
        sections: ["数据库配置规范", "必需字段规范"]

# ============================================
# 协作冲突处理
# ============================================
conflict_handling:
  data_conflict:
    scenario: "多个上游Skill输出同一参数"
    resolution: "定义优先级规则或合并策略"

  timing_conflict:
    scenario: "并行Skill完成时间差异大"
    resolution: "定义超时和默认值策略"

  version_conflict:
    scenario: "引用Skill版本不一致"
    resolution: "明确版本兼容性要求"

# ============================================
# 注意事项
# ============================================
notes:
  - "协作关系要清晰明确，避免循环依赖"
  - "数据流要可追溯，便于调试"
  - "并行执行要定义明确的同步点"
  - "条件触发要具体可判断"
  - "引用关系要在引用文档中明确标注"
  - "定期检查协作关系是否需要更新"