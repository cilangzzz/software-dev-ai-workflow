# 数据库设计 Skill

## 基本信息

- **ID**: db-designer
- **名称**: 数据库设计 Skill
- **版本**: 1.0.0
- **分类**: design
- **描述**: 根据业务需求自动生成符合项目规范的数据库设计，包括表结构、索引、ER图等


## 触发条件


### commands

- /db-design
- /db-designer

### keywords

- 设计数据库
- 生成表结构
- 创建数据模型
- 建表
- DDL

### events


- **name**: prd_approved
- **condition**: PRD文档审核通过

- **name**: architecture_defined
- **condition**: 系统架构设计完成

## 输入参数


### parameters


- **name**: module_code
- **type**: string
- **required**: True
- **description**: 模块编码（如 mes、erp、crm、bpm 等）
- **examples**: - mes
- erp
- crm
- bpm
- pay
- fz

- **name**: table_name
- **type**: string
- **required**: True
- **description**: 表名（不含前缀）
- **examples**: - work_order
- product
- customer
- letter

- **name**: business_fields
- **type**: array
- **required**: True
- **description**: 业务字段列表

- **name**: indexes
- **type**: array
- **required**: False
- **default**: 
- **description**: 额外索引定义

- **name**: create_date
- **type**: string
- **required**: False
- **default**: today
- **description**: 创建日期（用于文件命名）

## 设计原则

- **business_position**: 数据库设计是业务建模的核心环节，将业务需求转化为可存储的数据结构

### design_principles

- 多租户隔离：所有业务表包含 tenant_id 字段，索引必须包含 tenant_id
- 审计追踪：标准化审计字段，支持数据变更追踪
- 逻辑删除：使用 deleted 字段实现软删除，避免数据物理删除
- 索引优化：根据查询场景设计索引，遵循最左匹配原则
- 命名规范：统一的表名、字段名、索引名命名规则

## directory_structure

- **base_path**: sql/master/mysql
- **layout**: 
```
sql/master/mysql/
├── table/              # 表结构定义
│   ├── create/         # 建表脚本
│   └── update/         # 表结构更新脚本
├── seq/                # 序列定义（Oracle/PostgreSQL）
├── index/              # 索引定义
├── view/               # 视图定义
├── data/               # 初始数据
└── init/               # 模块初始化脚本

```


### directories


- **name**: table/create
- **purpose**: 存放建表 SQL 脚本
- **note**: 每个表一个文件，按日期命名

- **name**: table/update
- **purpose**: 存放表结构更新 SQL 脚本
- **note**: ALTER TABLE、ADD COLUMN 等增量变更

- **name**: seq
- **purpose**: 存放序列创建脚本
- **note**: Oracle/PostgreSQL 序列，MySQL 可省略

- **name**: index
- **purpose**: 存放索引创建脚本
- **note**: 可按表名组织子目录

- **name**: view
- **purpose**: 存放视图创建脚本
- **note**: 复杂查询可封装为视图

- **name**: data
- **purpose**: 存放初始数据 SQL 脚本
- **note**: INSERT 语句，初始化字典、菜单等

- **name**: init
- **purpose**: 存放模块初始化脚本
- **note**: 按模块组织，如 bpm.sql, quartz.sql

## file_naming


### create_table

- **format**: YYYY_MM_DD_{表名}_create.sql

### examples

- 2025_08_09_fz_letter_create.sql
- 2026_03_25_mes_work_order_create.sql

### rules

- 日期前缀使用实际创建日期
- 表名使用小写字母和下划线
- 统一使用 _create.sql 后缀

### update_table

- **format**: YYYY_MM_DD_{表名}_update.sql

### examples

- 2025_08_15_fz_metaletter_update.sql
- 2026_01_07_fz_attachment_rel_update.sql

### rules

- 日期前缀使用实际更新日期
- 同一表多次更新使用不同日期
- 统一使用 _update.sql 后缀

### special_cases


- **pattern**: YYYY_MM_DD_{表名}_index_update.sql
- **purpose**: 专门用于索引更新

### sequence

- **format**: YYYY_MM_DD_{表名}_seq_create.sql

### examples

- 2025_07_24_fz_metaletter_seq_create.sql

### rules

- 与建表日期保持一致
- 序列名通常为 表名_seq

### initial_data

- **format**: 模块名.sql

### examples

- fazhi.sql
- bpm.sql
- quartz.sql
- ruoyi-vue-pro.sql

### rules

- 按模块或功能命名
- 包含该模块的初始数据

## table_naming


### prefixes


- **prefix**: sys_
- **usage**: 系统核心表
- **examples**: - sys_user
- sys_role
- sys_menu
- sys_dict_data

- **prefix**: mes_
- **usage**: 制造执行系统表
- **examples**: - mes_work_order
- mes_product
- mes_workshop

- **prefix**: erp_
- **usage**: 企业资源计划表
- **examples**: - erp_purchase
- erp_sale
- erp_inventory

- **prefix**: crm_
- **usage**: 客户关系管理表
- **examples**: - crm_customer
- crm_contract
- crm_clue

- **prefix**: bpm_
- **usage**: 工作流表
- **examples**: - bpm_process_definition
- bpm_process_instance

- **prefix**: pay_
- **usage**: 支付模块表
- **examples**: - pay_order
- pay_refund
- pay_channel

- **prefix**: member_
- **usage**: 会员模块表
- **examples**: - member_user
- member_level
- member_address

- **prefix**: infra_
- **usage**: 基础设施表
- **examples**: - infra_file
- infra_config

- **prefix**: fz_
- **usage**: 法制业务表
- **examples**: - fz_letter
- fz_replay
- fz_handle_unit

### rules

- 使用小写字母，单词间用下划线分隔
- 使用名词，表示实体或关系
- 避免使用 MySQL 保留字
- 长度不超过 64 个字符
- 关联表命名：主表_关联表_rel，如 fz_letter_label_rel

### column_rules

- 使用小写字母和下划线
- 布尔类型使用 is_ 前缀，如 is_deleted, is_enabled
- 时间类型使用 _time 或 _date 后缀
- 外键使用 关联表_id 格式，如 user_id, dept_id
- 主键统一命名为 id

## required_columns


### columns


- **name**: id
- **type**: BIGINT
- **constraint**: NOT NULL AUTO_INCREMENT PRIMARY KEY
- **comment**: 主键ID
- **position**: 1

- **name**: tenant_id
- **type**: BIGINT
- **default**: 0
- **constraint**: NOT NULL
- **comment**: 租户编号
- **position**: 2
- **note**: 所有业务表必须包含，位于 id 之后

- **name**: creator
- **type**: VARCHAR(64)
- **default**: ''
- **comment**: 创建者

- **name**: create_time
- **type**: DATETIME
- **default**: CURRENT_TIMESTAMP
- **constraint**: NOT NULL
- **comment**: 创建时间

- **name**: updater
- **type**: VARCHAR(64)
- **default**: ''
- **comment**: 更新者

- **name**: update_time
- **type**: DATETIME
- **default**: CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
- **constraint**: NOT NULL
- **comment**: 更新时间

- **name**: deleted
- **type**: BIT(1)
- **default**: b'0'
- **constraint**: NOT NULL
- **comment**: 是否删除

### remark

- **name**: remark
- **type**: VARCHAR(500)
- **default**: NULL
- **comment**: 备注
- **position**: before_audit

## index_standards


### naming

- **primary_key**: PRIMARY KEY (`id`)
- **unique_key**: uk_{字段名} 或 uk_{字段1_字段2}
- **normal_index**: idx_{字段名} 或 idx_{字段1_字段2}

### principles

- 所有索引必须包含 tenant_id 作为第一列
- 唯一索引必须包含 deleted 字段（软删除场景）
- 外键字段必须建立索引
- 经常用于查询条件的字段建立索引
- 唯一约束字段建立唯一索引
- 组合索引注意字段顺序（最左匹配）
- 避免过多索引，影响写入性能

### templates


### unique_with_tenant

- **pattern**: UNIQUE KEY `uk_tenant_{col}` (`tenant_id`, `{col}`, `deleted`)
- **example**: UNIQUE KEY `uk_tenant_order` (`tenant_id`, `order_no`, `deleted`)

### normal_with_tenant

- **pattern**: KEY `idx_tenant_{col}` (`tenant_id`, `{col}`)
- **example**: KEY `idx_tenant_status` (`tenant_id`, `status`)

### foreign_key

- **pattern**: KEY `idx_tenant_{fk}` (`tenant_id`, `{fk}`)
- **example**: KEY `idx_tenant_line` (`tenant_id`, `line_id`)

## create_table_template

- **structure**: 
```
-- ============================================
-- 文件名：{filename}
-- 描述：{table_comment}
-- 作者：{author}
-- 日期：{date}
-- ============================================

CREATE TABLE `{table_name}` (
    `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
    `tenant_id` BIGINT NOT NULL DEFAULT 0 COMMENT '租户编号',
    -- 业务字段
    {business_columns}
    -- 通用字段
    `remark` VARCHAR(500) DEFAULT NULL COMMENT '备注',
    `creator` VARCHAR(64) DEFAULT '' COMMENT '创建者',
    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updater` VARCHAR(64) DEFAULT '' COMMENT '更新者',
    `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    `deleted` BIT(1) NOT NULL DEFAULT b'0' COMMENT '是否删除',
    PRIMARY KEY (`id`),
    {indexes}
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='{table_comment}';

```


### column_types

- **string_short**: VARCHAR(64)
- **string_medium**: VARCHAR(255)
- **string_long**: VARCHAR(500)
- **text**: TEXT
- **integer**: INT
- **bigint**: BIGINT
- **decimal_amount**: DECIMAL(18,2)
- **decimal_quantity**: DECIMAL(10,4)
- **boolean**: TINYINT
- **datetime**: DATETIME
- **date**: DATE
- **status**: TINYINT

## update_standards

- **naming**: YYYY_MM_DD_{表名}_update.sql

### operations

- **add_column**: 
```
-- 新增字段
ALTER TABLE `{table}` ADD COLUMN `{column}` {type} COMMENT '{comment}';
-- 示例
ALTER TABLE `fz_letter` ADD COLUMN `priority` TINYINT DEFAULT 0 COMMENT '优先级';

```

- **modify_column**: 
```
-- 修改字段类型
ALTER TABLE `{table}` MODIFY COLUMN `{column}` {new_type} COMMENT '{comment}';
-- 示例
ALTER TABLE `fz_letter` MODIFY COLUMN `content` TEXT COMMENT '信件内容';

```

- **drop_column**: 
```
-- 删除字段（确保无业务依赖）
ALTER TABLE `{table}` DROP COLUMN `{column}`;

```

- **add_index**: 
```
-- 添加普通索引
ALTER TABLE `{table}` ADD INDEX `idx_tenant_{col}` (`tenant_id`, `{col}`);
-- 添加唯一索引
ALTER TABLE `{table}` ADD UNIQUE INDEX `uk_tenant_{col}` (`tenant_id`, `{col}`, `deleted`);

```

- **header**: 
```
-- ============================================
-- 更新说明：{更新目的}
-- 更新日期：{YYYY-MM-DD}
-- 更新人：{姓名}
-- ============================================

```


### comment_standards

- 文件头部说明更新目的
- 每个变更语句添加注释
- 危险操作（删除字段、删除数据）添加警告注释

## data_standards

- **insert_format**: 
```
-- 插入菜单数据
INSERT INTO `sys_menu` (`id`, `name`, `permission`, `type`, `sort`, `parent_id`, `path`, `icon`, `component`, `status`)
VALUES
(1001, '信件管理', '', 2, 1, 0, 'letter', 'ep:document', 'fazhi/letter/index', 0),
(1002, '信件查询', 'fz:letter:query', 3, 1, 1001, '', '', '', 0);

```

- **dict_data**: 
```
-- 字典类型
INSERT INTO `sys_dict_type` (`name`, `type`, `status`, `remark`)
VALUES ('信件状态', 'fz_letter_status', 0, '信件流转状态');

-- 字典数据
INSERT INTO `sys_dict_data` (`sort`, `label`, `value`, `dict_type`, `status`)
VALUES
(1, '待处理', '0', 'fz_letter_status', 0),
(2, '处理中', '1', 'fz_letter_status', 0),
(3, '已完成', '2', 'fz_letter_status', 0);

```


## coding_standards


### formatting

- 关键字使用大写：SELECT, FROM, WHERE, JOIN, ORDER BY
- 表名、字段名使用小写和反引号
- 每个字段占一行，逗号放在行尾
- 复杂查询使用缩进和换行提高可读性

### comments

- **file_header**: 
```
-- ============================================
-- 文件名：{文件名}
-- 描述：{功能描述}
-- 作者：{作者}
-- 日期：{YYYY-MM-DD}
-- ============================================

```

- **table_comment**: CREATE TABLE 语句必须包含 COMMENT
- **column_comment**: 每个字段必须包含 COMMENT
- **index_comment**: 复杂索引添加注释说明用途

### transaction

- 多条关联语句使用事务包裹
- DDL 语句（部分数据库）自动提交，注意顺序
- 大数据量操作分批执行

## version_control


### principles

- 建表后表结构变更使用 update 脚本，不修改原文件
- 每个变更独立文件，便于追踪和回滚
- 日期前缀确保文件顺序和变更时间线
- 版本升级时按日期顺序执行所有脚本

### change_log

- **format**: 
```
-- 变更记录：
-- 2025-08-09：创建表
-- 2025-11-11：新增 priority 字段
-- 2026-01-07：新增 category 字段，添加索引

```


## 工作流程


### phases


- **name**: 需求分析
- **description**: 解析业务需求，提取实体和关系
- **steps**: - 识别核心业务实体
- 分析实体间关系（一对多、多对多）
- 确定实体属性列表
- 确定表名前缀（模块编码）

- **name**: 实体设计
- **description**: 设计实体属性和字段
- **steps**: - 设计业务属性字段
- 添加系统必需字段（审计字段）
- 定义主键策略（BIGINT AUTO_INCREMENT）
- 设置外键关系

- **name**: 多租户设计
- **description**: 添加租户隔离字段和索引
- **steps**: - 添加 tenant_id 字段（第二位置）
- 确保所有索引包含 tenant_id
- 唯一索引包含 deleted 字段

- **name**: 索引设计
- **description**: 根据查询场景设计索引
- **steps**: - 分析查询场景（列表、详情、关联、搜索）
- 设计主键索引
- 设计唯一索引（业务唯一键）
- 设计普通索引（查询优化）
- 设计外键索引

- **name**: 文件生成
- **description**: 生成符合规范的 SQL 文件
- **steps**: - 确定文件命名（日期前缀）
- 生成文件头部注释
- 生成 CREATE TABLE 语句
- 生成索引定义
- 添加表注释

## quality_check


### before_create

- 确认表名符合命名规范
- 确认包含所有必需字段
- 确认字段类型和长度合理
- 确认添加了必要的索引
- 确认添加了表注释和字段注释
- 确认文件命名符合规范

### after_create

- 测试建表脚本可正常执行
- 确认所有索引包含 tenant_id
- 确认唯一索引包含 deleted
- 确认外键字段有索引
- 检查索引是否生效
- 更新相关文档

### before_update

- 确认变更的必要性
- 评估对现有数据的影响
- 准备回滚方案
- 选择低峰期执行

## 快速参考


### table_prefixes

- **sys_**: 系统表
- **mes_**: 制造执行系统表
- **erp_**: 企业资源计划表
- **crm_**: 客户关系管理表
- **bpm_**: 工作流表
- **pay_**: 支付表
- **member_**: 会员表
- **infra_**: 基础设施表
- **fz_**: 法制业务表

### file_suffixes

- **_create.sql**: 建表脚本
- **_update.sql**: 更新脚本
- **_seq_create.sql**: 序列脚本

### common_columns

- **id**: 主键ID（BIGINT）
- **tenant_id**: 租户编号（BIGINT）
- **creator**: 创建者（VARCHAR(64)）
- **create_time**: 创建时间（DATETIME）
- **updater**: 更新者（VARCHAR(64)）
- **update_time**: 更新时间（DATETIME）
- **deleted**: 逻辑删除（BIT(1)）
- **remark**: 备注（VARCHAR(500)）

## 使用示例


### work_order


### input

- **module_code**: mes
- **table_name**: mes_work_order
- **table_comment**: 生产工单表

### business_fields


- **name**: order_no
- **type**: VARCHAR(64)
- **required**: True
- **comment**: 工单编号
- **unique**: True

- **name**: product_id
- **type**: BIGINT
- **required**: True
- **comment**: 产品ID

- **name**: status
- **type**: TINYINT
- **required**: True
- **default**: 0
- **comment**: 状态:0-待下发,1-已下发,2-生产中,3-已完成,4-已关闭
- **output_file**: 2026_03_25_mes_work_order_create.sql
- **output_sql**: 
```
-- ============================================
-- 文件名：2026_03_25_mes_work_order_create.sql
-- 描述：生产工单表
-- 作者：AI Assistant
-- 日期：2026-03-25
-- ============================================

CREATE TABLE `mes_work_order` (
    `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
    `tenant_id` BIGINT NOT NULL DEFAULT 0 COMMENT '租户ID',
    `order_no` VARCHAR(64) NOT NULL COMMENT '工单编号(WO+年月日+4位流水)',
    `erp_order_no` VARCHAR(64) DEFAULT NULL COMMENT 'ERP订单编号',
    `product_id` BIGINT NOT NULL COMMENT '产品ID',
    `product_code` VARCHAR(64) NOT NULL COMMENT '产品编码',
    `product_name` VARCHAR(255) NOT NULL COMMENT '产品名称',
    `plan_qty` INT NOT NULL COMMENT '计划数量',
    `actual_qty` INT NOT NULL DEFAULT 0 COMMENT '实际数量',
    `routing_id` BIGINT NOT NULL COMMENT '工艺路线ID',
    `routing_name` VARCHAR(255) DEFAULT NULL COMMENT '工艺路线名称',
    `status` TINYINT NOT NULL DEFAULT 0 COMMENT '状态:0-待下发,1-已下发,2-生产中,3-已完成,4-已关闭',
    `priority` INT NOT NULL DEFAULT 5 COMMENT '优先级(1-10)',
    `plan_start_time` DATETIME NOT NULL COMMENT '计划开始时间',
    `plan_end_time` DATETIME NOT NULL COMMENT '计划结束时间',
    `actual_start_time` DATETIME DEFAULT NULL COMMENT '实际开始时间',
    `actual_end_time` DATETIME DEFAULT NULL COMMENT '实际结束时间',
    `workshop_id` BIGINT DEFAULT NULL COMMENT '车间ID',
    `workshop_name` VARCHAR(100) DEFAULT NULL COMMENT '车间名称',
    `line_id` BIGINT NOT NULL COMMENT '产线ID',
    `line_name` VARCHAR(100) DEFAULT NULL COMMENT '产线名称',
    `remark` VARCHAR(500) DEFAULT NULL COMMENT '备注',
    `creator` VARCHAR(64) DEFAULT '' COMMENT '创建者',
    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updater` VARCHAR(64) DEFAULT '' COMMENT '更新者',
    `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    `deleted` BIT(1) NOT NULL DEFAULT b'0' COMMENT '是否删除',
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_tenant_order` (`tenant_id`, `order_no`, `deleted`),
    KEY `idx_tenant_status` (`tenant_id`, `status`),
    KEY `idx_tenant_line` (`tenant_id`, `line_id`),
    KEY `idx_tenant_time` (`tenant_id`, `plan_start_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='生产工单表';

```


## error_handling


### errors


- **code**: DB001
- **message**: 表名不符合命名规范
- **solution**: 检查表名前缀和格式

- **code**: DB002
- **message**: 缺少必需字段
- **solution**: 确保包含 id, tenant_id, 审计字段

- **code**: DB003
- **message**: 索引缺少 tenant_id
- **solution**: 所有索引必须包含 tenant_id 作为第一列

- **code**: DB004
- **message**: 文件命名不符合规范
- **solution**: 使用 YYYY_MM_DD_{表名}_create.sql 格式

- **code**: DB005
- **message**: 唯一索引缺少 deleted
- **solution**: 唯一索引必须包含 deleted 字段