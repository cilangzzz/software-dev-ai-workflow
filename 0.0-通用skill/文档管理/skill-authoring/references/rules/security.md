# 安全部 Skill编写规则
# 适用场景：威胁建模、安全审计、漏洞扫描、合规检查

# ============================================
# Skill必填章节
# ============================================
required_sections:
  basic_info:
    - "基本信息：名称、版本、所属部门、优先级"
    - "优先级通常为P0或P1（安全相关通常优先级较高）"

  trigger:
    - "触发条件：命令触发和自然语言触发"
    - "关键词应包含安全相关术语"

  input:
    - "输入参数：至少包含分析目标参数"
    - "参数类型：system_description、code_path等"

  security_methodology:
    - "安全方法论：如STRIDE、OWASP Top 10等"
    - "分类框架：威胁分类、漏洞分类等"

  workflow:
    - "执行流程：分析→识别→评估→建议"
    - "包含风险评估阶段"

  output:
    - "输出格式：安全报告模板"
    - "包含风险矩阵和优先级建议"

  examples:
    - "使用示例：至少1个完整示例"
    - "示例应真实反映安全分析场景"

  quality_standards:
    - "质量标准：覆盖率、准确率等"
    - "建议优先级排序"

# ============================================
# 安全方法论规范
# ============================================
methodologies:
  stride:
    name: "STRIDE威胁建模"
    categories:
      - code: "S"
        name: "Spoofing（欺骗）"
        description: "冒充合法用户或系统"
        examples: ["身份伪造", "中间人攻击"]

      - code: "T"
        name: "Tampering（篡改）"
        description: "恶意修改数据"
        examples: ["数据篡改", "SQL注入"]

      - code: "R"
        name: "Repudiation（抵赖）"
        description: "否认执行操作"
        examples: ["操作日志缺失", "审计绕过"]

      - code: "I"
        name: "Information Disclosure（信息泄露）"
        description: "未授权访问信息"
        examples: ["敏感数据泄露", "配置暴露"]

      - code: "D"
        name: "Denial of Service（拒绝服务）"
        description: "破坏服务可用性"
        examples: ["DDoS攻击", "资源耗尽"]

      - code: "E"
        name: "Elevation of Privilege（权限提升）"
        description: "获取未授权权限"
        examples: ["提权攻击", "权限绕过"]

  owasp_top_10:
    name: "OWASP Top 10"
    categories:
      - "A01:2021 - Broken Access Control"
      - "A02:2021 - Cryptographic Failures"
      - "A03:2021 - Injection"
      - "A04:2021 - Insecure Design"
      - "A05:2021 - Security Misconfiguration"
      - "A06:2021 - Vulnerable and Outdated Components"
      - "A07:2021 - Identification and Authentication Failures"
      - "A08:2021 - Software and Data Integrity Failures"
      - "A09:2021 - Security Logging and Monitoring Failures"
      - "A10:2021 - Server-Side Request Forgery"

# ============================================
# 风险评估规范
# ============================================
risk_assessment:
  risk_levels:
    - level: "高"
      color: "red"
      criteria: "可导致数据泄露、系统被控制、业务中断"
      action: "必须立即修复"

    - level: "中"
      color: "orange"
      criteria: "可能导致信息泄露、功能异常"
      action: "需要尽快修复"

    - level: "低"
      color: "green"
      criteria: "影响有限，需关注"
      action: "建议修复"

  risk_matrix:
    dimensions:
      - "影响程度：高/中/低"
      - "发生概率：高/中/低"
    calculation: "风险等级 = 影响程度 × 发生概率"

# ============================================
# 报告模板规范
# ============================================
report_template:
  threat_model_report: |
    # 威胁建模报告

    ## 系统概述
    {系统简要描述}

    ## 信任边界
    - 边界1: {边界描述}
    - 边界2: {边界描述}

    ## 胁清单

    ### Spoofing（欺骗）
    | ID | 威胁描述 | 风险 | 缓解措施 |
    |----|----------|------|---------|
    | S-01 | {威胁} | {风险} | {缓解措施} |

    ### Tampering（篡改）
    | ID | 威胁描述 | 风险 | 缓解措施 |
    |----|----------|------|---------|
    | T-01 | {威胁} | {风险} | {缓解措施} |

    ## 风险矩阵
    | 风险等级 | 数量 | 示例 |
    |----------|------|------|
    | 高 | {n} | {examples} |
    | 中 | {n} | {examples} |
    | 低 | {n} | {examples} |

    ## 安全需求
    - {需求1}
    - {需求2}

    ## 建议优先级
    1. {优先级1}
    2. {优先级2}

  audit_report: |
    # 安全审计报告

    ## 审计概述
    - 审计范围: {范围}
    - 审计时间: {时间}
    - 审计人员: {人员}

    ## 审计结果摘要
    | 类别 | 发现数量 | 高危 | 中危 | 低危 |
    |------|---------|------|------|------|
    | {类别} | {n} | {n} | {n} | {n} |

    ## 详细发现
    ### 发现1: {标题}
    - 类型: {类型}
    - 位置: {位置}
    - 风险等级: {等级}
    - 描述: {描述}
    - 建议修复方案: {方案}

    ## 合规性检查
    | 检查项 | 状态 | 说明 |
    |--------|------|------|
    | {检查项} | ✓/✗ | {说明} |

# ============================================
# 常见Skill示例
# ============================================
skill_examples:
  threat_model:
    id: "security-threat-model"
    name: "威胁建模"
    description: "使用STRIDE方法分析系统安全威胁"

  code_review:
    id: "security-code-review"
    name: "安全代码审查"
    description: "审查代码安全漏洞和合规问题"

  vulnerability_scan:
    id: "security-scan"
    name: "安全扫描"
    description: "扫描系统漏洞和安全风险"

# ============================================
# 输入参数规范
# ============================================
input_parameters:
  threat_model:
    - name: "system_description"
      type: "string"
      required: true
      description: "系统描述或架构图"

    - name: "data_flow"
      type: "string"
      required: false
      description: "数据流描述"

    - name: "trust_boundaries"
      type: "string"
      required: false
      description: "信任边界定义"

  code_review:
    - name: "code_path"
      type: "string"
      required: true
      description: "待审查代码路径"

    - name: "review_scope"
      type: "string"
      required: false
      enum: ["full", "sensitive", "auth", "data"]
      description: "审查范围"

# ============================================
# 注意事项
# ============================================
notes:
  - "威胁建模需要开发、运维多方参与"
  - "模型需要定期更新"
  - "关注供应链安全威胁"
  - "安全建议要具体可操作"
  - "风险等级要明确优先级"
  - "合规检查要根据具体法规"