# DBA（数据库管理员） Agent编写规则
# 适用场景：MySQL、PostgreSQL、Oracle、数据库管理、SQL优化

# ============================================
# 技术栈定义
# ============================================
tech_stack:
  databases:
    - name: "MySQL"
      version: "8.x"
      description: "主流关系型数据库"
    - name: "PostgreSQL"
      version: "15+"
      description: "开源高级关系型数据库"
    - name: "Oracle"
      version: "19c+"
      description: "企业级关系型数据库"
    - name: "SQL Server"
      version: "2019+"
      description: "Microsoft企业数据库"
  tools:
    - "SQL客户端工具"
    - "数据库监控工具"
    - "备份恢复工具"
    - "性能分析工具"
  skills:
    - "SQL编写与优化"
    - "数据库设计"
    - "性能调优"
    - "备份恢复"
    - "安全管理"

# ============================================
# Agent角色能力模板
# ============================================
capabilities_template:
  core_skills:
    - skill: "数据库设计"
      level: "expert"
      components:
        - "表结构设计"
        - "索引策略设计"
        - "关系模型设计"
        - "数据类型选择"
        - "分区表设计"

    - skill: "SQL优化"
      level: "expert"
      components:
        - "执行计划分析"
        - "索引优化建议"
        - "查询重写优化"
        - "慢查询分析"
        - "SQL性能监控"

    - skill: "数据库运维"
      level: "advanced"
      components:
        - "备份策略设计"
        - "恢复演练"
        - "容量规划"
        - "版本升级"
        - "迁移方案"

    - skill: "性能调优"
      level: "advanced"
      components:
        - "参数配置优化"
        - "内存管理"
        - "I/O优化"
        - "锁优化"
        - "并发控制"

    - skill: "安全管理"
      level: "advanced"
      components:
        - "权限管理"
        - "审计配置"
        - "加密策略"
        - "访问控制"
        - "漏洞修复"

# ============================================
# 项目结构规范（DBA工作产出物）
# ============================================
project_structure:
  dba_deliverables: |
    {project_name}/
    ├── docs/
    │   ├── database_design/
    │   │   ├── er_diagram.drawio    # ER图
    │   │   ├── table_spec.md        # 表结构说明
    │   │   ├── index_strategy.md    # 索引策略
    │   │   └── data_dictionary.md   # 数据字典
    │   ├── performance/
    │   │   ├── tuning_report.md     # 优化报告
    │   │   ├── slow_query_analysis.md # 慢查询分析
    │   │   ├── benchmark_report.md  # 基准测试报告
    │   ├── backup/
    │   │   ├── backup_strategy.md   # 备份策略
    │   │   ├── recovery_plan.md     # 恢复方案
    │   │   ├── drill_records.md     # 演练记录
    │   ├── security/
    │   │   ├── permission_matrix.md # 权限矩阵
    │   │   ├── audit_policy.md      # 审计策略
    │   ├── migration/
    │   │   ├── migration_plan.md    # 迁移方案
    │   │   ├── compatibility_check.md # 兼容性检查
    ├── scripts/
    │   ├── ddl/
    │   │   ├── create_tables.sql    # 建表脚本
    │   │   ├── create_indexes.sql   # 创建索引
    │   │   ├── alter_tables.sql     # 表变更脚本
    │   ├── dml/
    │   │   ├── init_data.sql        # 初始化数据
    │   │   ├── migrate_data.sql     # 数据迁移
    │   ├── maintenance/
    │   │   ├── backup.sh            # 备份脚本
    │   │   ├── restore.sh           # 恢复脚本
    │   │   ├── monitor.sh           # 监控脚本
    │   ├── performance/
    │   │   ├── analyze.sql          # 分析脚本
    │   │   ├── optimize.sql         # 优化脚本
    │   ├── security/
    │   │   ├── grant_permissions.sql # 权限授予
    │   │   ├── audit_setup.sql      # 审计配置
    ├── config/
    │   ├── my.cnf                   # MySQL配置
    │   ├── postgresql.conf          # PostgreSQL配置
    │   ├── monitoring.yaml          # 监控配置
    └── README.md

# ============================================
# 命名规范
# ============================================
naming_conventions:
  # 表命名
  tables:
    - rule: "小写下划线格式"
      examples: ["system_user", "pay_order", "product_category"]
    - rule: "模块前缀区分业务域"
      examples: ["sys_user", "pay_transaction", "product_item"]
    - rule: "避免使用MySQL保留字"
      examples: ["user_account而非user", "order_record而非order"]

  # 字段命名
  columns:
    - rule: "小写下划线格式"
      examples: ["user_name", "create_time", "order_amount"]
    - rule: "布尔字段is_前缀"
      examples: ["is_active", "is_deleted", "is_enabled"]
    - rule: "时间字段_time后缀"
      examples: ["create_time", "update_time", "expire_time"]
    - rule: "外键字段_id后缀"
      examples: ["user_id", "order_id", "category_id"]

  # 索引命名
  indexes:
    - rule: "idx_表名_字段名"
      examples: ["idx_user_email", "idx_order_status", "idx_product_category"]
    - rule: "唯一索引uk_前缀"
      examples: ["uk_user_email", "uk_order_number"]
    - rule: "复合索引包含所有字段"
      examples: ["idx_order_user_status"]

  # 脚本文件命名
  scripts:
    - rule: "SQL脚本.sql后缀"
      examples: ["create_tables.sql", "init_data.sql"]
    - rule: "Shell脚本.sh后缀"
      examples: ["backup.sh", "monitor.sh"]
    - rule: "操作类型前缀"
      examples: ["create_xxx.sql", "alter_xxx.sql", "backup_xxx.sh"]

  # 文档命名
  documents:
    - rule: "小写下划线.md格式"
      examples: ["database_design.md", "backup_strategy.md"]
    - rule: "版本号后缀（可选）"
      examples: ["schema_v1.0.md", "migration_v2.0.md"]

# ============================================
# 代码风格规范
# ============================================
code_style:
  # DDL脚本模板
  ddl_template: |
    -- ============================================
    -- 表名：system_user
    -- 描述：系统用户表
    -- 作者：DBA Team
    -- 创建时间：2026-04-24
    -- ============================================

    CREATE TABLE IF NOT EXISTS `system_user` (
        `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
        `username` VARCHAR(50) NOT NULL COMMENT '用户名',
        `email` VARCHAR(255) NOT NULL COMMENT '邮箱',
        `phone` VARCHAR(20) NULL COMMENT '手机号',
        `password_hash` VARCHAR(255) NOT NULL COMMENT '密码哈希',
        `salt` VARCHAR(64) NOT NULL COMMENT '密码盐值',
        `status` TINYINT NOT NULL DEFAULT 1 COMMENT '状态：1启用 0禁用',
        `is_deleted` BIT NOT NULL DEFAULT 0 COMMENT '删除标记',
        `creator` VARCHAR(64) NULL COMMENT '创建人',
        `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
        `updater` VARCHAR(64) NULL COMMENT '更新人',
        `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
        PRIMARY KEY (`id`),
        UNIQUE KEY `uk_user_email` (`email`),
        UNIQUE KEY `uk_user_username` (`username`),
        KEY `idx_user_status` (`status`),
        KEY `idx_user_create_time` (`create_time`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='系统用户表';

    -- ============================================
    -- 索引说明：
    -- uk_user_email: 邮箱唯一索引，用于登录和查询
    -- uk_user_username: 用户名唯一索引，用于登录和查询
    -- idx_user_status: 状态索引，用于筛选活跃用户
    -- idx_user_create_time: 创建时间索引，用于时间范围查询
    -- ============================================

  # 查询优化模板
  query_optimization: |
    -- 优化前：慢查询（执行时间 > 500ms）
    SELECT * FROM orders 
    WHERE user_id = 123 
    AND status IN (1, 2, 3)
    AND create_time > '2024-01-01'
    ORDER BY create_time DESC;

    -- 问题分析：
    -- 1. SELECT * 获取所有字段，包括不需要的大字段
    -- 2. 缺少复合索引，导致全表扫描
    -- 3. IN 子查询可能导致多次索引查找

    -- 优化后：
    SELECT id, order_number, amount, status, create_time 
    FROM orders 
    WHERE user_id = 123 
    AND status IN (1, 2, 3)
    AND create_time > '2024-01-01'
    ORDER BY create_time DESC
    LIMIT 100;

    -- 建议添加索引：
    CREATE INDEX idx_orders_user_status_time 
    ON orders(user_id, status, create_time);

    -- 执行计划检查：
    EXPLAIN SELECT id, order_number, amount, status, create_time 
    FROM orders 
    WHERE user_id = 123 
    AND status IN (1, 2, 3)
    AND create_time > '2024-01-01'
    ORDER BY create_time DESC;

  # 备份脚本模板
  backup_script: |
    #!/bin/bash
    # ============================================
    # MySQL数据库备份脚本
    # 作者：DBA Team
    # 创建时间：2026-04-24
    # ============================================

    # 配置参数
    DB_HOST="localhost"
    DB_PORT="3306"
    DB_USER="backup_user"
    DB_PASS="******"  # 建议使用配置文件存储密码
    BACKUP_DIR="/data/backup/mysql"
    DATE=$(date +%Y%m%d_%H%M%S)

    # 日志函数
    log_info() {
        echo "[INFO] $(date '+%Y-%m-%d %H:%M:%S') $1"
    }
    log_error() {
        echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') $1"
    }

    # 创建备份目录
    mkdir -p ${BACKUP_DIR}/${DATE}

    # 全库备份
    log_info "开始全库备份..."
    mysqldump -h${DB_HOST} -P${DB_PORT} -u${DB_USER} -p${DB_PASS} \
        --single-transaction \
        --routines \
        --triggers \
        --events \
        --all-databases \
        | gzip > ${BACKUP_DIR}/${DATE}/full_backup.sql.gz

    if [ $? -eq 0 ]; then
        log_info "全库备份完成: ${BACKUP_DIR}/${DATE}/full_backup.sql.gz"
    else
        log_error "全库备份失败"
        exit 1
    fi

    # 清理旧备份（保留30天）
    find ${BACKUP_DIR} -type f -mtime +30 -delete
    log_info "清理完成"

# ============================================
# Skill示例
# ============================================
skill_examples:
  db_designer:
    id: "db-designer"
    name: "数据库设计"
    description: "根据业务需求设计数据库表结构、索引策略、ER图"

  sql_optimizer:
    id: "sql-optimizer"
    name: "SQL优化"
    description: "分析慢查询，提供优化建议和索引方案"

  backup_designer:
    id: "backup-designer"
    name: "备份策略设计"
    description: "设计数据库备份策略，生成备份恢复脚本"

  migration_planner:
    id: "migration-planner"
    name: "迁移方案设计"
    description: "设计数据库迁移方案，兼容性检查"

  security_auditor:
    id: "security-auditor"
    name: "数据库安全审计"
    description: "审计数据库安全配置，权限检查"

# ============================================
# 注意事项
# ============================================
notes:
  - "表名小写下划线格式，避免使用数据库保留字"
  - "字段名小写下划线格式，统一注释规范"
  - "索引命名规范：idx_/uk_前缀"
  - "DDL脚本需要包含详细注释"
  - "变更脚本需要包含回滚脚本"
  - "备份脚本密码不要硬编码"
  - "定期执行恢复演练验证备份有效性"
  - "性能优化前先分析执行计划"
  - "大表变更需要分批执行避免锁表"