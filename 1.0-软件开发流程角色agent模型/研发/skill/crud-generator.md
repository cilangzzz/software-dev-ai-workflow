# crud-generator

## 基本信息
| 属性 | 值 |
|------|------|
| 名称 | crud-generator |
| 版本 | 1.0.0 |
| 部门 | 研发部 |
| 优先级 | P1 |
| 复杂度 | medium |
| 预估时间 | 15-30min |

## 描述
根据实体类和API设计，自动生成完整的CRUD代码结构，包括：
- Controller（REST接口控制器）
- Service（业务逻辑层接口）
- ServiceImpl（业务逻辑层实现）
- Mapper（MyBatis数据访问层）
- Mapper.xml（MyBatis XML映射文件）
- DTO（数据传输对象：CreateDTO, UpdateDTO, QueryDTO）
- VO（视图对象：VO, ListVO）

## 触发条件

### 命令触发
```
/crud-generator
```

### 事件触发
| 事件 | 条件 |
|------|------|
| entity_generated | 实体类生成完成 |
| api_design_completed | API设计文档完成 |
| contract_signed | 开发契约签署 |

### 自然语言触发
| 关键词 | 示例 |
|--------|------|
| 生成CRUD代码 | "为客户实体生成CRUD代码" |
| 创建增删改查 | "创建订单的增删改查功能" |
| 生成完整业务代码 | "生成销售管理的完整业务代码" |

## 输入参数

| 参数名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| entity_class | string | 是 | - | 实体类路径 |
| api_design_file | string | 是 | - | API设计文档路径 |
| module_code | string | 是 | - | 模块编码（如sd、wm、pp） |
| package_base | string | 否 | com.example.module | 基础包名 |
| use_validator | boolean | 否 | true | 是否生成参数校验 |
| use_cache | boolean | 否 | false | 是否添加缓存支持 |
| generate_batch | boolean | 否 | true | 是否生成批量操作 |
| output_dir | string | 否 | 代码/backend/src/main/java | 输出目录 |

## 输出产物

| 产物 | 路径 | 类型 | 描述 |
|------|------|------|------|
| Controller | controller/{Entity}Controller.java | code | REST控制器 |
| Service | service/{Entity}Service.java | code | 业务接口 |
| ServiceImpl | service/impl/{Entity}ServiceImpl.java | code | 业务实现 |
| Mapper | mapper/{Entity}Mapper.java | code | 数据访问接口 |
| Mapper.xml | resources/mapper/{Entity}Mapper.xml | code | MyBatis映射文件 |
| CreateDTO | dto/{Entity}CreateDTO.java | code | 创建请求DTO |
| UpdateDTO | dto/{Entity}UpdateDTO.java | code | 更新请求DTO |
| QueryDTO | dto/{Entity}QueryDTO.java | code | 查询条件DTO |
| VO | vo/{Entity}VO.java | code | 详情响应VO |
| ListVO | vo/{Entity}ListVO.java | code | 列表响应VO |

## 执行流程

### Phase 1: 结构分析（5min）
```
1. 解析实体类结构
   - 提取类名、表名、字段列表
   - 识别主键字段
   - 识别可空/必填字段（从注解读取）
   - 识别审计字段（排除在DTO外）

2. 解析API设计文档
   - 提取接口列表
   - 确定CRUD操作列表
   - 识别特殊操作（状态流转、批量等）

3. 确定生成范围
   | 操作 | 是否生成 | 条件 |
   |------|----------|------|
   | 列表查询 | 是 | 默认 |
   | 详情查询 | 是 | 默认 |
   | 创建 | 是 | 默认 |
   | 更新 | 是 | 默认 |
   | 删除 | 是 | 默认 |
   | 批量删除 | 可选 | generate_batch=true |
   | 批量创建 | 可选 | generate_batch=true |
   | 导出 | 可选 | 根据需求 |
```

### Phase 2: DTO/VO生成（5min）
```
1. CreateDTO设计
   - 包含所有可创建字段
   - 排除：id, tenant_id, 审计字段
   - 添加校验注解（@NotBlank, @NotNull, @Size等）
   - 主实体字段使用@Valid嵌套校验

2. UpdateDTO设计
   - 包含所有可更新字段
   - 排除：id, tenant_id, created_by/time, deleted
   - 字段默认可选（非必填）
   - 支持部分更新

3. QueryDTO设计
   - 包含常用查询字段
   - 支持范围查询（startTime, endTime）
   - 支持模糊查询（keyword）
   - 包含分页参数（pageNo, pageSize）

4. VO设计
   - 详情VO：包含所有展示字段
   - 列表VO：包含列表展示字段（精简）
   - 添加关联实体字段（如customerName）
   - 添加枚举值说明字段（如customerTypeName）
```

### Phase 3: Mapper生成（3min）
```
1. Mapper接口
   - 继承BaseMapper<Entity>（MyBatis Plus）
   - 自定义查询方法
   - 批量操作方法

2. Mapper.xml
   - ResultMap定义
   - 自定义SQL查询
   - 关联查询（如有）
```

### Phase 4: Service生成（5min）
```
1. Service接口
   - CRUD方法声明
   - 分页查询方法
   - 业务方法声明

2. ServiceImpl实现
   - CRUD方法实现
   - 分页查询实现
   - 事务注解配置
   - 缓存配置（如有）
```

### Phase 5: Controller生成（7min）
```
1. Controller类
   - REST注解配置
   - 鉴权注解配置
   - Swagger注解配置

2. 接口方法
   - 列表查询：GET /list
   - 详情查询：GET /{id}
   - 创建：POST
   - 更新：PUT /{id}
   - 删除：DELETE /{id}
   - 批量删除：DELETE /batch

3. 参数校验
   - @Valid注解
   - @PathVariable注解
   - @RequestParam注解
```

## 代码模板

### Controller模板
```java
package {package_base}.controller;

import {package_base}.dto.*;
import {package_base}.vo.*;
import {package_base}.service.{Entity}Service;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

/**
 * {Entity}管理控制器
 */
@RestController
@RequestMapping("/{api_prefix}/{entity_lower}")
@Tag(name = "{Entity}管理")
@Validated
public class {Entity}Controller {

    @Autowired
    private {Entity}Service {entity}Service;

    @PostMapping
    @Operation(summary = "创建{Entity}")
    public Result<Long> create(@RequestBody @Valid {Entity}CreateDTO dto) {
        return Result.success({entity}Service.create(dto));
    }

    @PutMapping("/{id}")
    @Operation(summary = "更新{Entity}")
    public Result<Boolean> update(
            @Parameter(description = "ID") @PathVariable Long id,
            @RequestBody @Valid {Entity}UpdateDTO dto) {
        return Result.success({entity}Service.update(id, dto));
    }

    @DeleteMapping("/{id}")
    @Operation(summary = "删除{Entity}")
    public Result<Boolean> delete(@Parameter(description = "ID") @PathVariable Long id) {
        return Result.success({entity}Service.delete(id));
    }

    @DeleteMapping("/batch")
    @Operation(summary = "批量删除{Entity}")
    public Result<Boolean> deleteBatch(@RequestBody List<Long> ids) {
        return Result.success({entity}Service.deleteBatch(ids));
    }

    @GetMapping("/{id}")
    @Operation(summary = "获取{Entity}详情")
    public Result<{Entity}VO> get(@Parameter(description = "ID") @PathVariable Long id) {
        return Result.success({entity}Service.getById(id));
    }

    @GetMapping("/list")
    @Operation(summary = "获取{Entity}列表")
    public Result<PageResult<{Entity}ListVO>> list({Entity}QueryDTO dto) {
        return Result.success({entity}Service.listPage(dto));
    }
}
```

### Service模板
```java
package {package_base}.service;

import {package_base}.dto.*;
import {package_base}.vo.*;
import com.baomidou.mybatisplus.extension.service.IService;

/**
 * {Entity}服务接口
 */
public interface {Entity}Service extends IService<{Entity}> {

    /**
     * 创建{Entity}
     */
    Long create({Entity}CreateDTO dto);

    /**
     * 更新{Entity}
     */
    Boolean update(Long id, {Entity}UpdateDTO dto);

    /**
     * 删除{Entity}
     */
    Boolean delete(Long id);

    /**
     * 批量删除
     */
    Boolean deleteBatch(List<Long> ids);

    /**
     * 获取详情
     */
    {Entity}VO getById(Long id);

    /**
     * 分页查询
     */
    PageResult<{Entity}ListVO> listPage({Entity}QueryDTO dto);
}
```

### ServiceImpl模板
```java
package {package_base}.service.impl;

import {package_base}.dto.*;
import {package_base}.entity.*;
import {package_base}.mapper.*;
import {package_base}.service.*;
import {package_base}.vo.*;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.beans.BeanUtils;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

/**
 * {Entity}服务实现
 */
@Service
public class {Entity}ServiceImpl extends ServiceImpl<{Entity}Mapper, {Entity}>
        implements {Entity}Service {

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long create({Entity}CreateDTO dto) {
        {Entity} entity = new {Entity}();
        BeanUtils.copyProperties(dto, entity);
        // TODO: 设置租户ID等
        save(entity);
        return entity.getId();
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Boolean update(Long id, {Entity}UpdateDTO dto) {
        {Entity} entity = getById(id);
        if (entity == null) {
            throw new BusinessException("{Entity}不存在");
        }
        BeanUtils.copyProperties(dto, entity);
        return updateById(entity);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Boolean delete(Long id) {
        return removeById(id);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Boolean deleteBatch(List<Long> ids) {
        return removeByIds(ids);
    }

    @Override
    public {Entity}VO getById(Long id) {
        {Entity} entity = super.getById(id);
        if (entity == null) {
            return null;
        }
        {Entity}VO vo = new {Entity}VO();
        BeanUtils.copyProperties(entity, vo);
        return vo;
    }

    @Override
    public PageResult<{Entity}ListVO> listPage({Entity}QueryDTO dto) {
        Page<{Entity}> page = new Page<>(dto.getPageNo(), dto.getPageSize());
        LambdaQueryWrapper<{Entity}> wrapper = new LambdaQueryWrapper<>();
        // TODO: 添加查询条件
        IPage<{Entity}> result = page(page, wrapper);

        // 转换为VO
        List<{Entity}ListVO> voList = result.getRecords().stream()
                .map(entity -> {
                    {Entity}ListVO vo = new {Entity}ListVO();
                    BeanUtils.copyProperties(entity, vo);
                    return vo;
                })
                .collect(Collectors.toList());

        return PageResult.of(voList, result.getTotal(), dto.getPageNo(), dto.getPageSize());
    }
}
```

## 质量标准

### 必须满足
| 标准 | 描述 | 验证方式 |
|------|------|----------|
| Swagger注解 | Controller所有方法有@Operation | 代码检查 |
| 参数校验 | DTO有@Valid，字段有校验注解 | 代码检查 |
| 事务注解 | 写操作有@Transactional | 代码检查 |
| 分页支持 | 列表查询使用分页 | 代码检查 |
| 逻辑删除 | 使用MyBatis Plus逻辑删除 | 配置检查 |
| 命名规范 | 类名、方法名遵循规范 | 代码检查 |

### 建议满足
| 标准 | 描述 |
|------|------|
| 异常处理 | 有完善的异常处理逻辑 |
| 日志记录 | 关键操作有日志记录 |
| 缓存支持 | 查询方法支持缓存 |
| 参数默认值 | 分页参数有合理默认值 |

## 示例

### 输入
```yaml
entity_class: 代码/backend/src/main/java/com/example/erp/sd/entity/Customer.java
api_design_file: 研发/API设计/API-01-销售管理模块.md
module_code: sd
package_base: com.example.erp.sd
generate_batch: true
```

### 输出
生成文件：
```
代码/backend/src/main/java/com/example/erp/sd/
├── controller/
│   └── CustomerController.java
├── service/
│   ├── CustomerService.java
│   └── impl/
│       └── CustomerServiceImpl.java
├── mapper/
│   └── CustomerMapper.java
├── dto/
│   ├── CustomerCreateDTO.java
│   ├── CustomerUpdateDTO.java
│   └── CustomerQueryDTO.java
└── vo/
    ├── CustomerVO.java
    └── CustomerListVO.java

代码/backend/src/main/resources/mapper/
└── CustomerMapper.xml
```

## 错误处理

| 错误代码 | 错误描述 | 处理方式 |
|----------|----------|----------|
| CRUD001 | 实体类不存在 | 返回错误，提示正确路径 |
| CRUD002 | API设计文件不存在 | 使用默认CRUD模板生成 |
| CRUD003 | 字段类型不支持 | 使用Object类型，记录警告 |
| CRUD004 | 包路径无效 | 使用默认包路径 |

## 与其他Skill的关系

### 上游依赖
| Skill | 依赖内容 |
|------|----------|
| entity-generator | 实体类定义 |
| api-designer | API接口定义 |

### 下游输出
| Skill | 输出内容 |
|------|----------|
| test-case-generator | 代码生成单元测试 |
| code-review | 生成的代码进行审查 |