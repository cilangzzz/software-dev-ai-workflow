# entity-generator

## 基本信息
| 属性 | 值 |
|------|------|
| 名称 | entity-generator |
| 版本 | 1.0.0 |
| 部门 | 研发部 |
| 优先级 | P1 |
| 复杂度 | medium |
| 预估时间 | 10-20min |

## 描述
根据数据库表结构设计，自动生成Java实体类（Entity），支持：
- JPA注解（@Entity, @Table, @Column等）
- MyBatis Plus注解（@TableName, @TableId, @TableField等）
- Lombok注解（@Data, @Builder等）
- Swagger注解（@Schema等）
- 审计字段自动填充配置

## 触发条件

### 命令触发
```
/entity-generator
```

### 事件触发
| 事件 | 条件 |
|------|------|
| db_design_completed | 数据库设计文档完成 |
| contract_signed | 开发契约签署 |

### 自然语言触发
| 关键词 | 示例 |
|--------|------|
| 生成实体类 | "为销售管理模块生成实体类" |
| 创建Entity | "创建客户实体类" |
| 生成Java实体 | "生成订单Java实体" |

## 输入参数

| 参数名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| db_design_file | string | 是 | - | 数据库设计文档路径 |
| orm_type | string | 否 | mybatis_plus | ORM类型：mybatis_plus/jpa |
| package_name | string | 否 | com.example.module.entity | 包名 |
| use_lombok | boolean | 否 | true | 是否使用Lombok |
| use_swagger | boolean | 否 | true | 是否使用Swagger注解 |
| tables | array | 否 | [] | 指定生成的表（空则生成全部） |
| output_dir | string | 否 | 代码/backend/src/main/java | 输出目录 |

## 输出产物

| 产物 | 路径 | 类型 | 描述 |
|------|------|------|------|
| 实体类文件 | {output_dir}/{package_path}/entity/{EntityName}.java | code | Java实体类 |

## 执行流程

### Phase 1: 表结构解析（3min）
```
1. 解析数据库设计文档
   - 提取CREATE TABLE语句
   - 解析表名、字段列表、注释
   - 提取索引信息（识别主键、唯一键）

2. 提取表元数据
   | 元数据 | 来源 |
   |--------|------|
   | 表名 | CREATE TABLE `table_name` |
   | 表注释 | COMMENT='表注释' |
   | 字段名 | 列定义 |
   | 字段类型 | 数据类型 |
   | 字段注释 | COMMENT '注释' |
   | 是否可空 | NULL/NOT NULL |
   | 默认值 | DEFAULT value |

3. 识别主键和外键关系
   - PRIMARY KEY识别主键
   - FOREIGN KEY识别外键关系
```

### Phase 2: 类型映射（5min）
```
MySQL类型 -> Java类型映射表:

| MySQL类型 | Java类型 | 说明 |
|-----------|----------|------|
| BIGINT | Long | 长整型 |
| INT, INTEGER | Integer | 整型 |
| TINYINT | Integer | 小整型（枚举字段） |
| SMALLINT | Integer | 短整型 |
| DECIMAL(p,s) | BigDecimal | 精确数值 |
| FLOAT, DOUBLE | Double | 浮点数 |
| VARCHAR, CHAR, TEXT | String | 字符串 |
| DATETIME, TIMESTAMP | LocalDateTime | 日期时间 |
| DATE | LocalDate | 日期 |
| TIME | LocalTime | 时间 |
| BIT, BOOLEAN | Boolean | 布尔值 |
| BLOB, LONGBLOB | byte[] | 二进制 |
| JSON | String/Map | JSON数据 |
```

### Phase 3: 命名转换（3min）
```
1. 表名 -> 类名转换
   规则: snake_case -> PascalCase，去掉表前缀
   示例: sd_customer -> Customer
         mes_work_order -> WorkOrder

2. 字段名 -> 属性名转换
   规则: snake_case -> camelCase
   示例: customer_name -> customerName
         created_time -> createdTime
```

### Phase 4: 注解生成（5min）
```
1. 类级注解生成

MyBatis Plus模式:
@TableName("sd_customer")
@Schema(description = "客户主数据表")

JPA模式:
@Entity
@Table(name = "sd_customer")
@Schema(description = "客户主数据表")

2. 字段级注解生成

主键字段:
MyBatis Plus: @TableId(type = IdType.AUTO)
JPA: @Id @GeneratedValue(strategy = GenerationType.IDENTITY)

普通字段:
MyBatis Plus: @TableField("customer_name")
JPA: @Column(name = "customer_name", length = 200)

逻辑删除:
MyBatis Plus: @TableLogic
JPA: @SQLDelete(sql = "UPDATE sd_customer SET deleted = 1 WHERE id = ?")

3. Swagger注解
所有字段添加: @Schema(description = "字段描述")

4. Lombok注解
类级别: @Data, @Builder, @NoArgsConstructor, @AllArgsConstructor
```

### Phase 5: 文件生成（4min）
```
1. 生成目录结构
   {output_dir}/{package_path}/entity/

2. 生成Java文件
   - 文件名: {EntityName}.java
   - 编码: UTF-8
   - 格式化: Google Java Format

3. 生成包声明和导入
   - 包声明
   - 导入语句（按类型分组排序）
```

## 代码模板

### MyBatis Plus模板
```java
package {package_name};

import com.baomidou.mybatisplus.annotation.*;
import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;
import lombok.Builder;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

import java.io.Serializable;
import java.math.BigDecimal;
import java.time.LocalDateTime;

/**
 * {table_comment}
 *
 * @author auto-generated
 * @since {date}
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@TableName("{table_name}")
@Schema(description = "{table_comment}")
public class {EntityName} implements Serializable {

    private static final long serialVersionUID = 1L;

    @TableId(type = IdType.AUTO)
    @Schema(description = "主键ID")
    private Long id;

    @TableField("tenant_id")
    @Schema(description = "租户ID")
    private Long tenantId;

    // ========== 业务字段 ==========

    {业务字段列表}

    // ========== 审计字段 ==========

    @TableField(fill = FieldFill.INSERT)
    @Schema(description = "创建人")
    private String createdBy;

    @TableField(fill = FieldFill.INSERT)
    @Schema(description = "创建时间")
    private LocalDateTime createdTime;

    @TableField(fill = FieldFill.UPDATE)
    @Schema(description = "更新人")
    private String updatedBy;

    @TableField(fill = FieldFill.UPDATE)
    @Schema(description = "更新时间")
    private LocalDateTime updatedTime;

    @TableLogic
    @Schema(description = "删除标记:0-未删除,1-已删除")
    private Integer deleted;
}
```

### JPA模板
```java
package {package_name};

import javax.persistence.*;
import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;
import lombok.Builder;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

import java.io.Serializable;
import java.math.BigDecimal;
import java.time.LocalDateTime;

/**
 * {table_comment}
 *
 * @author auto-generated
 * @since {date}
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "{table_name}")
@Schema(description = "{table_comment}")
public class {EntityName} implements Serializable {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Schema(description = "主键ID")
    private Long id;

    @Column(name = "tenant_id", nullable = false)
    @Schema(description = "租户ID")
    private Long tenantId;

    // ========== 业务字段 ==========

    {业务字段列表}

    // ========== 审计字段 ==========

    @Column(name = "created_by", updatable = false)
    @Schema(description = "创建人")
    private String createdBy;

    @Column(name = "created_time", updatable = false)
    @Schema(description = "创建时间")
    private LocalDateTime createdTime;

    @Column(name = "updated_by")
    @Schema(description = "更新人")
    private String updatedBy;

    @Column(name = "updated_time")
    @Schema(description = "更新时间")
    private LocalDateTime updatedTime;

    @Column(name = "deleted")
    @Schema(description = "删除标记:0-未删除,1-已删除")
    private Integer deleted;
}
```

## 质量标准

### 必须满足
| 标准 | 描述 | 验证方式 |
|------|------|----------|
| 类注释存在 | 所有实体类必须有类级别注释 | 代码检查 |
| 字段注释存在 | 所有字段必须有@Schema注释 | 代码检查 |
| 主键注解正确 | 主键使用@TableId/@Id注解 | 代码检查 |
| 多租户字段 | 包含tenant_id字段 | 字段检查 |
| 审计字段完整 | 包含created_by/time, updated_by/time, deleted | 字段检查 |
| 逻辑删除配置 | deleted字段使用@TableLogic | 代码检查 |
| Serializable | 实现Serializable接口 | 代码检查 |
| serialVersionUID | 包含serialVersionUID常量 | 代码检查 |

### 建议满足
| 标准 | 描述 |
|------|------|
| 字段排序合理 | 业务字段在前，审计字段在后 |
| 导入语句有序 | 按包名分组排序 |
| 命名规范一致 | 遵循Java命名规范 |

## 示例

### 输入
```yaml
db_design_file: 研发/数据库设计/DB-01-销售管理模块.md
orm_type: mybatis_plus
package_name: com.example.erp.sd.entity
tables:
  - sd_customer
```

### 输出

**文件路径**: `代码/backend/src/main/java/com/example/erp/sd/entity/Customer.java`

```java
package com.example.erp.sd.entity;

import com.baomidou.mybatisplus.annotation.*;
import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;
import lombok.Builder;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

import java.io.Serializable;
import java.math.BigDecimal;
import java.time.LocalDateTime;

/**
 * 客户主数据表
 *
 * @author auto-generated
 * @since 2026-03-30
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@TableName("sd_customer")
@Schema(description = "客户主数据表")
public class Customer implements Serializable {

    private static final long serialVersionUID = 1L;

    @TableId(type = IdType.AUTO)
    @Schema(description = "主键ID")
    private Long id;

    @TableField("tenant_id")
    @Schema(description = "租户ID")
    private Long tenantId;

    @TableField("customer_code")
    @Schema(description = "客户编码")
    private String customerCode;

    @TableField("customer_name")
    @Schema(description = "客户名称")
    private String customerName;

    @TableField("customer_short_name")
    @Schema(description = "客户简称")
    private String customerShortName;

    @TableField("customer_type")
    @Schema(description = "客户类型:1-整车厂,2-一级供应商,3-经销商,4-零售商")
    private Integer customerType;

    @TableField("customer_level")
    @Schema(description = "客户等级:1-A级,2-B级,3-C级")
    private Integer customerLevel;

    @TableField("credit_limit")
    @Schema(description = "信用额度")
    private BigDecimal creditLimit;

    @TableField("credit_used")
    @Schema(description = "已用信用额度")
    private BigDecimal creditUsed;

    @TableField("status")
    @Schema(description = "状态:0-禁用,1-启用")
    private Integer status;

    @TableField("remark")
    @Schema(description = "备注")
    private String remark;

    @TableField(fill = FieldFill.INSERT)
    @Schema(description = "创建人")
    private String createdBy;

    @TableField(fill = FieldFill.INSERT)
    @Schema(description = "创建时间")
    private LocalDateTime createdTime;

    @TableField(fill = FieldFill.UPDATE)
    @Schema(description = "更新人")
    private String updatedBy;

    @TableField(fill = FieldFill.UPDATE)
    @Schema(description = "更新时间")
    private LocalDateTime updatedTime;

    @TableLogic
    @Schema(description = "删除标记:0-未删除,1-已删除")
    private Integer deleted;
}
```

## 错误处理

| 错误代码 | 错误描述 | 处理方式 |
|----------|----------|----------|
| ENT001 | DB设计文件不存在 | 返回错误，提示正确路径 |
| ENT002 | 表结构解析失败 | 分析文档格式，提供修复建议 |
| ENT003 | 类型映射失败 | 使用默认String类型，记录警告 |
| ENT004 | 命名冲突 | 自动添加后缀解决冲突 |

## 与其他Skill的关系

### 上游依赖
| Skill | 依赖内容 |
|------|----------|
| db-designer | 表结构定义 |

### 下游输出
| Skill | 输出内容 |
|------|----------|
| crud-generator | 实体类生成Controller/Service/Mapper |
| test-case-generator | 实体类生成测试数据 |