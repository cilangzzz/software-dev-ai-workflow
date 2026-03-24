# Detail-10 工艺管理模块详细设计 (ENG)

## 文档信息

| 项目 | 内容 |
|------|------|
| 文档版本 | V1.0 |
| 创建日期 | 2026-03-24 |
| 模块名称 | 工艺管理 (Engineering Management) |
| 模块代码 | ENG |
| 技术栈 | Spring Boot 2.7 + MyBatis Plus + MySQL 8.x |

---

## 1. 模块架构设计

### 1.1 模块分层架构

```
┌────────────────────────────────────────────────────────────────┐
│                        表现层 (Controller)                      │
│  ProductController │ BomController │ RouteController │ EcrController │
└────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌────────────────────────────────────────────────────────────────┐
│                        业务层 (Service)                         │
│ ProductService │ BomService │ RouteService │ EcrService │ SyncService │
└────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌────────────────────────────────────────────────────────────────┐
│                        数据访问层 (Mapper)                      │
│  ProductMapper │ BomMapper │ RouteMapper │ EcrMapper │ SyncMapper │
└────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌────────────────────────────────────────────────────────────────┐
│                        数据库层 (MySQL)                         │
│       eng_product │ eng_bom │ eng_route │ eng_ecr │ eng_eco      │
└────────────────────────────────────────────────────────────────┘
```

### 1.2 包结构设计

```
com.autoerp.eng
├── controller                    # 控制器层
│   ├── ProductController.java
│   ├── ProductCategoryController.java
│   ├── BomController.java
│   ├── OperationController.java
│   ├── RouteController.java
│   ├── EcrController.java
│   ├── EcoController.java
│   └── SyncController.java
├── service                       # 服务接口层
│   ├── ProductService.java
│   ├── ProductCategoryService.java
│   ├── BomService.java
│   ├── OperationService.java
│   ├── RouteService.java
│   ├── EcrService.java
│   ├── EcoService.java
│   └── SyncService.java
├── service.impl                  # 服务实现层
│   ├── ProductServiceImpl.java
│   ├── ProductCategoryServiceImpl.java
│   ├── BomServiceImpl.java
│   ├── OperationServiceImpl.java
│   ├── RouteServiceImpl.java
│   ├── EcrServiceImpl.java
│   ├── EcoServiceImpl.java
│   └── SyncServiceImpl.java
├── mapper                        # 数据访问层
│   ├── ProductMapper.java
│   ├── ProductCategoryMapper.java
│   ├── BomMapper.java
│   ├── BomItemMapper.java
│   ├── OperationMapper.java
│   ├── RouteMapper.java
│   ├── RouteItemMapper.java
│   ├── EcrMapper.java
│   ├── EcoMapper.java
│   └── SyncLogMapper.java
├── entity                        # 实体类
│   ├── Product.java
│   ├── ProductCategory.java
│   ├── ProductAttribute.java
│   ├── Bom.java
│   ├── BomItem.java
│   ├── BomAlternative.java
│   ├── Operation.java
│   ├── OperationResource.java
│   ├── Route.java
│   ├── RouteItem.java
│   ├── Ecr.java
│   ├── EcrRelation.java
│   ├── EcrImpact.java
│   ├── Eco.java
│   ├── EcoExecution.java
│   ├── ApprovalRecord.java
│   └── SyncLog.java
├── dto                           # 数据传输对象
│   ├── request
│   │   ├── ProductCreateRequest.java
│   │   ├── ProductQueryRequest.java
│   │   ├── BomCreateRequest.java
│   │   ├── BomExpandRequest.java
│   │   ├── RouteCreateRequest.java
│   │   ├── EcrCreateRequest.java
│   │   └── EcoCreateRequest.java
│   └── response
│       ├── ProductDetailResponse.java
│       ├── BomExpandResponse.java
│       ├── RouteDetailResponse.java
│       └── EcrImpactResponse.java
├── vo                            # 视图对象
│   ├── ProductVo.java
│   ├── BomVo.java
│   ├── BomItemVo.java
│   ├── RouteVo.java
│   ├── OperationVo.java
│   ├── EcrVo.java
│   └── EcoVo.java
├── convert                       # 对象转换器
│   ├── ProductConvert.java
│   ├── BomConvert.java
│   ├── RouteConvert.java
│   └── EcrConvert.java
├── enums                         # 枚举类
│   ├── ProductTypeEnum.java
│   ├── ProductStatusEnum.java
│   ├── ApproveStatusEnum.java
│   ├── BomTypeEnum.java
│   ├── OperationTypeEnum.java
│   ├── ChangeTypeEnum.java
│   ├── EcrStatusEnum.java
│   └── EcoStatusEnum.java
├── event                         # 事件类
│   ├── ProductApprovedEvent.java
│   ├── BomApprovedEvent.java
│   ├── RouteApprovedEvent.java
│   └── EcoClosedEvent.java
├── listener                      # 事件监听器
│   ├── ProductEventListener.java
│   ├── BomEventListener.java
│   ├── RouteEventListener.java
│   └── EcoEventListener.java
├── util                          # 工具类
│   ├── BomExpandUtil.java
│   ├── BomValidateUtil.java
│   ├── CodeGeneratorUtil.java
│   └── ImpactAnalyzerUtil.java
├── config                        # 配置类
│   └── EngConfig.java
└── constant                      # 常量类
    └── EngConstant.java
```

---

## 2. 核心类设计

### 2.1 产品管理模块

#### 2.1.1 ProductController

```java
package com.autoerp.eng.controller;

import com.autoerp.common.core.Result;
import com.autoerp.common.core.PageResult;
import com.autoerp.eng.dto.request.ProductCreateRequest;
import com.autoerp.eng.dto.request.ProductQueryRequest;
import com.autoerp.eng.dto.response.ProductDetailResponse;
import com.autoerp.eng.service.ProductService;
import com.autoerp.eng.vo.ProductVo;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.Valid;

/**
 * 产品管理控制器
 */
@Api(tags = "产品管理")
@RestController
@RequestMapping("/api/v1/eng/products")
public class ProductController {

    @Autowired
    private ProductService productService;

    /**
     * 分页查询产品列表
     */
    @ApiOperation("查询产品列表")
    @GetMapping
    public Result<PageResult<ProductVo>> list(ProductQueryRequest request) {
        return Result.success(productService.queryPage(request));
    }

    /**
     * 查询产品详情
     */
    @ApiOperation("查询产品详情")
    @GetMapping("/{id}")
    public Result<ProductDetailResponse> detail(@PathVariable Long id) {
        return Result.success(productService.getDetail(id));
    }

    /**
     * 创建产品
     */
    @ApiOperation("创建产品")
    @PostMapping
    public Result<Long> create(@Valid @RequestBody ProductCreateRequest request) {
        return Result.success(productService.create(request));
    }

    /**
     * 更新产品
     */
    @ApiOperation("更新产品")
    @PutMapping("/{id}")
    public Result<Void> update(@PathVariable Long id,
                               @Valid @RequestBody ProductCreateRequest request) {
        productService.update(id, request);
        return Result.success();
    }

    /**
     * 删除产品
     */
    @ApiOperation("删除产品")
    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        productService.delete(id);
        return Result.success();
    }

    /**
     * 提交审批
     */
    @ApiOperation("提交产品审批")
    @PostMapping("/{id}/submit")
    public Result<Void> submit(@PathVariable Long id) {
        productService.submit(id);
        return Result.success();
    }

    /**
     * 审批产品
     */
    @ApiOperation("审批产品")
    @PostMapping("/{id}/approve")
    public Result<Void> approve(@PathVariable Long id,
                                @RequestParam Integer approveResult,
                                @RequestParam(required = false) String approveOpinion) {
        productService.approve(id, approveResult, approveOpinion);
        return Result.success();
    }

    /**
     * 批量导入
     */
    @ApiOperation("批量导入产品")
    @PostMapping("/import")
    public Result<Object> importProducts(@RequestParam("file") MultipartFile file) {
        return Result.success(productService.importProducts(file));
    }

    /**
     * 导出产品
     */
    @ApiOperation("导出产品")
    @GetMapping("/export")
    public void export(ProductQueryRequest request, HttpServletResponse response) {
        productService.export(request, response);
    }
}
```

#### 2.1.2 ProductService

```java
package com.autoerp.eng.service;

import com.autoerp.common.core.PageResult;
import com.autoerp.eng.dto.request.ProductCreateRequest;
import com.autoerp.eng.dto.request.ProductQueryRequest;
import com.autoerp.eng.dto.response.ProductDetailResponse;
import com.autoerp.eng.entity.Product;
import com.autoerp.eng.vo.ProductVo;
import com.baomidou.mybatisplus.extension.service.IService;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletResponse;

/**
 * 产品服务接口
 */
public interface ProductService extends IService<Product> {

    /**
     * 分页查询产品
     */
    PageResult<ProductVo> queryPage(ProductQueryRequest request);

    /**
     * 获取产品详情
     */
    ProductDetailResponse getDetail(Long id);

    /**
     * 创建产品
     */
    Long create(ProductCreateRequest request);

    /**
     * 更新产品
     */
    void update(Long id, ProductCreateRequest request);

    /**
     * 删除产品
     */
    void delete(Long id);

    /**
     * 提交审批
     */
    void submit(Long id);

    /**
     * 审批产品
     */
    void approve(Long id, Integer approveResult, String approveOpinion);

    /**
     * 批量导入
     */
    Object importProducts(MultipartFile file);

    /**
     * 导出产品
     */
    void export(ProductQueryRequest request, HttpServletResponse response);

    /**
     * 检查产品编码是否存在
     */
    boolean checkCodeExists(String productCode, Long excludeId);
}
```

#### 2.1.3 ProductServiceImpl

```java
package com.autoerp.eng.service.impl;

import com.autoerp.common.core.PageResult;
import com.autoerp.common.exception.BusinessException;
import com.autoerp.eng.constant.EngConstant;
import com.autoerp.eng.convert.ProductConvert;
import com.autoerp.eng.dto.request.ProductCreateRequest;
import com.autoerp.eng.dto.request.ProductQueryRequest;
import com.autoerp.eng.dto.response.ProductDetailResponse;
import com.autoerp.eng.entity.Product;
import com.autoerp.eng.entity.ProductAttribute;
import com.autoerp.eng.entity.ApprovalRecord;
import com.autoerp.eng.enums.ApproveStatusEnum;
import com.autoerp.eng.enums.ProductStatusEnum;
import com.autoerp.eng.event.ProductApprovedEvent;
import com.autoerp.eng.mapper.ProductMapper;
import com.autoerp.eng.mapper.ProductAttributeMapper;
import com.autoerp.eng.service.ProductService;
import com.autoerp.eng.util.CodeGeneratorUtil;
import com.autoerp.system.entity.User;
import com.autoerp.system.service.UserService;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletResponse;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 产品服务实现
 */
@Slf4j
@Service
public class ProductServiceImpl extends ServiceImpl<ProductMapper, Product>
    implements ProductService {

    @Autowired
    private ProductAttributeMapper attributeMapper;

    @Autowired
    private ApplicationEventPublisher eventPublisher;

    @Autowired
    private UserService userService;

    @Override
    public PageResult<ProductVo> queryPage(ProductQueryRequest request) {
        Page<Product> page = new Page<>(request.getPageNum(), request.getPageSize());

        LambdaQueryWrapper<Product> wrapper = new LambdaQueryWrapper<>();
        wrapper.like(request.getProductCode() != null,
                    Product::getProductCode, request.getProductCode())
               .like(request.getProductName() != null,
                    Product::getProductName, request.getProductName())
               .eq(request.getCategoryId() != null,
                   Product::getCategoryId, request.getCategoryId())
               .eq(request.getProductType() != null,
                   Product::getProductType, request.getProductType())
               .eq(request.getStatus() != null,
                   Product::getStatus, request.getStatus())
               .eq(request.getApproveStatus() != null,
                   Product::getApproveStatus, request.getApproveStatus())
               .eq(Product::getDeleted, EngConstant.NOT_DELETED)
               .orderByDesc(Product::getCreateTime);

        Page<Product> result = this.page(page, wrapper);

        List<ProductVo> voList = result.getRecords().stream()
            .map(ProductConvert::toVo)
            .collect(Collectors.toList());

        return PageResult.of(voList, result.getTotal(),
                            request.getPageNum(), request.getPageSize());
    }

    @Override
    public ProductDetailResponse getDetail(Long id) {
        Product product = this.getById(id);
        if (product == null || product.getDeleted() == EngConstant.DELETED) {
            throw new BusinessException("产品不存在");
        }

        ProductDetailResponse response = ProductConvert.toDetailResponse(product);

        // 查询扩展属性
        List<ProductAttribute> attributes = attributeMapper.selectList(
            new LambdaQueryWrapper<ProductAttribute>()
                .eq(ProductAttribute::getProductId, id)
                .eq(ProductAttribute::getDeleted, EngConstant.NOT_DELETED)
        );
        response.setAttributes(attributes);

        return response;
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long create(ProductCreateRequest request) {
        // 检查编码唯一性
        if (checkCodeExists(request.getProductCode(), null)) {
            throw new BusinessException("产品编码已存在");
        }

        // 创建产品实体
        Product product = ProductConvert.toEntity(request);
        product.setStatus(ProductStatusEnum.DEVELOPING.getCode());
        product.setApproveStatus(ApproveStatusEnum.DRAFT.getCode());

        // 保存产品
        this.save(product);

        // 保存扩展属性
        if (request.getAttributes() != null && !request.getAttributes().isEmpty()) {
            List<ProductAttribute> attributes = request.getAttributes().stream()
                .map(attr -> {
                    ProductAttribute attribute = new ProductAttribute();
                    attribute.setProductId(product.getId());
                    attribute.setAttrName(attr.getAttrName());
                    attribute.setAttrValue(attr.getAttrValue());
                    attribute.setAttrType(attr.getAttrType());
                    return attribute;
                })
                .collect(Collectors.toList());

            attributes.forEach(attr -> attributeMapper.insert(attr));
        }

        log.info("产品创建成功, id={}, code={}", product.getId(), product.getProductCode());
        return product.getId();
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void update(Long id, ProductCreateRequest request) {
        Product product = this.getById(id);
        if (product == null || product.getDeleted() == EngConstant.DELETED) {
            throw new BusinessException("产品不存在");
        }

        // 已审批产品修改后需重新审批
        if (product.getApproveStatus() == ApproveStatusEnum.APPROVED.getCode()) {
            product.setApproveStatus(ApproveStatusEnum.DRAFT.getCode());
        }

        // 更新产品信息
        ProductConvert.updateEntity(product, request);
        this.updateById(product);

        // 更新扩展属性
        attributeMapper.delete(new LambdaQueryWrapper<ProductAttribute>()
            .eq(ProductAttribute::getProductId, id));

        if (request.getAttributes() != null && !request.getAttributes().isEmpty()) {
            request.getAttributes().forEach(attr -> {
                ProductAttribute attribute = new ProductAttribute();
                attribute.setProductId(id);
                attribute.setAttrName(attr.getAttrName());
                attribute.setAttrValue(attr.getAttrValue());
                attribute.setAttrType(attr.getAttrType());
                attributeMapper.insert(attribute);
            });
        }

        log.info("产品更新成功, id={}", id);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void delete(Long id) {
        Product product = this.getById(id);
        if (product == null || product.getDeleted() == EngConstant.DELETED) {
            throw new BusinessException("产品不存在");
        }

        // 检查是否被引用
        // TODO: 检查BOM、订单等引用关系

        // 逻辑删除
        product.setDeleted(EngConstant.DELETED);
        this.updateById(product);

        log.info("产品删除成功, id={}", id);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void submit(Long id) {
        Product product = this.getById(id);
        if (product == null || product.getDeleted() == EngConstant.DELETED) {
            throw new BusinessException("产品不存在");
        }

        if (product.getApproveStatus() != ApproveStatusEnum.DRAFT.getCode() &&
            product.getApproveStatus() != ApproveStatusEnum.REJECTED.getCode()) {
            throw new BusinessException("当前状态不允许提交审批");
        }

        product.setApproveStatus(ApproveStatusEnum.PENDING.getCode());
        this.updateById(product);

        // TODO: 发送审批通知

        log.info("产品提交审批成功, id={}", id);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void approve(Long id, Integer approveResult, String approveOpinion) {
        Product product = this.getById(id);
        if (product == null || product.getDeleted() == EngConstant.DELETED) {
            throw new BusinessException("产品不存在");
        }

        if (product.getApproveStatus() != ApproveStatusEnum.PENDING.getCode()) {
            throw new BusinessException("当前状态不允许审批");
        }

        // 更新审批状态
        if (approveResult == 1) {
            product.setApproveStatus(ApproveStatusEnum.APPROVED.getCode());
            product.setStatus(ProductStatusEnum.TRIAL.getCode());
            product.setEffectiveDate(LocalDate.now());
        } else {
            product.setApproveStatus(ApproveStatusEnum.REJECTED.getCode());
        }
        this.updateById(product);

        // 记录审批记录
        ApprovalRecord record = new ApprovalRecord();
        record.setBusinessType(EngConstant.BUSINESS_TYPE_PRODUCT);
        record.setBusinessId(id);
        record.setBusinessCode(product.getProductCode());
        record.setApproveResult(approveResult);
        record.setApproveOpinion(approveOpinion);
        // record.setApproverId(SecurityUtils.getCurrentUserId());
        // approvalRecordMapper.insert(record);

        // 发布审批通过事件
        if (approveResult == 1) {
            eventPublisher.publishEvent(new ProductApprovedEvent(id));
        }

        log.info("产品审批完成, id={}, result={}", id, approveResult);
    }

    @Override
    public boolean checkCodeExists(String productCode, Long excludeId) {
        LambdaQueryWrapper<Product> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(Product::getProductCode, productCode)
               .eq(Product::getDeleted, EngConstant.NOT_DELETED);

        if (excludeId != null) {
            wrapper.ne(Product::getId, excludeId);
        }

        return this.count(wrapper) > 0;
    }

    @Override
    public Object importProducts(MultipartFile file) {
        // TODO: 实现导入逻辑
        return null;
    }

    @Override
    public void export(ProductQueryRequest request, HttpServletResponse response) {
        // TODO: 实现导出逻辑
    }
}
```

---

### 2.2 BOM管理模块

#### 2.2.1 BomService

```java
package com.autoerp.eng.service;

import com.autoerp.common.core.PageResult;
import com.autoerp.eng.dto.request.BomCreateRequest;
import com.autoerp.eng.dto.request.BomQueryRequest;
import com.autoerp.eng.dto.request.BomExpandRequest;
import com.autoerp.eng.dto.response.BomDetailResponse;
import com.autoerp.eng.dto.response.BomExpandResponse;
import com.autoerp.eng.dto.response.BomCompareResponse;
import com.autoerp.eng.dto.response.BomWhereUsedResponse;
import com.autoerp.eng.entity.Bom;
import com.autoerp.eng.vo.BomVo;
import com.baomidou.mybatisplus.extension.service.IService;

import java.util.List;

/**
 * BOM服务接口
 */
public interface BomService extends IService<Bom> {

    /**
     * 分页查询BOM
     */
    PageResult<BomVo> queryPage(BomQueryRequest request);

    /**
     * 获取BOM详情
     */
    BomDetailResponse getDetail(Long id);

    /**
     * 创建BOM
     */
    Long create(BomCreateRequest request);

    /**
     * 更新BOM
     */
    void update(Long id, BomCreateRequest request);

    /**
     * 删除BOM
     */
    void delete(Long id);

    /**
     * BOM展开
     */
    BomExpandResponse expand(Long id, BomExpandRequest request);

    /**
     * BOM反查
     */
    BomWhereUsedResponse whereUsed(Long materialId, String level);

    /**
     * BOM版本对比
     */
    BomCompareResponse compare(Long bomId1, Long bomId2);

    /**
     * 审批BOM
     */
    void approve(Long id, Integer approveResult, String approveOpinion);

    /**
     * 检查循环引用
     */
    boolean checkCircularReference(Long productId, Long materialId);

    /**
     * 计算BOM成本
     */
    BigDecimal calculateCost(Long id);
}
```

#### 2.2.2 BomServiceImpl (核心方法)

```java
package com.autoerp.eng.service.impl;

import com.autoerp.common.core.PageResult;
import com.autoerp.common.exception.BusinessException;
import com.autoerp.eng.constant.EngConstant;
import com.autoerp.eng.convert.BomConvert;
import com.autoerp.eng.dto.request.BomCreateRequest;
import com.autoerp.eng.dto.request.BomExpandRequest;
import com.autoerp.eng.dto.response.BomExpandResponse;
import com.autoerp.eng.entity.Bom;
import com.autoerp.eng.entity.BomItem;
import com.autoerp.eng.enums.ApproveStatusEnum;
import com.autoerp.eng.event.BomApprovedEvent;
import com.autoerp.eng.mapper.BomMapper;
import com.autoerp.eng.mapper.BomItemMapper;
import com.autoerp.eng.service.BomService;
import com.autoerp.eng.util.BomExpandUtil;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * BOM服务实现
 */
@Slf4j
@Service
public class BomServiceImpl extends ServiceImpl<BomMapper, Bom> implements BomService {

    @Autowired
    private BomItemMapper bomItemMapper;

    @Autowired
    private ApplicationEventPublisher eventPublisher;

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long create(BomCreateRequest request) {
        // 检查版本唯一性
        if (checkVersionExists(request.getProductId(), request.getVersion(), null)) {
            throw new BusinessException("该产品已存在相同版本的BOM");
        }

        // 检查循环引用
        for (BomCreateRequest.BomItemRequest item : request.getItems()) {
            if (checkCircularReference(request.getProductId(), item.getMaterialId())) {
                throw new BusinessException("存在循环引用，物料ID: " + item.getMaterialId());
            }
        }

        // 创建BOM头
        Bom bom = BomConvert.toEntity(request);
        bom.setBomCode(generateBomCode());
        bom.setApproveStatus(ApproveStatusEnum.DRAFT.getCode());
        this.save(bom);

        // 保存BOM明细
        saveBomItems(bom.getId(), request.getItems());

        log.info("BOM创建成功, id={}, code={}", bom.getId(), bom.getBomCode());
        return bom.getId();
    }

    @Override
    public BomExpandResponse expand(Long id, BomExpandRequest request) {
        Bom bom = this.getById(id);
        if (bom == null || bom.getDeleted() == EngConstant.DELETED) {
            throw new BusinessException("BOM不存在");
        }

        // 获取BOM明细
        List<BomItem> items = bomItemMapper.selectList(
            new LambdaQueryWrapper<BomItem>()
                .eq(BomItem::getBomId, id)
                .eq(BomItem::getDeleted, EngConstant.NOT_DELETED)
                .orderByAsc(BomItem::getSeqNo)
        );

        BomExpandResponse response = new BomExpandResponse();
        response.setBomId(id);
        response.setExpandType(request.getExpandType());

        switch (request.getExpandType()) {
            case "single":
                // 单级展开
                response.setTree(buildSingleLevelTree(items));
                break;
            case "multi":
                // 多级展开
                response.setTree(buildMultiLevelTree(items, 1));
                break;
            case "end":
                // 末级展开
                response.setTree(buildEndLevelTree(items));
                break;
        }

        return response;
    }

    /**
     * 构建多级展开树
     */
    private List<BomExpandResponse.BomTreeNode> buildMultiLevelTree(
            List<BomItem> items, int level) {
        List<BomExpandResponse.BomTreeNode> tree = new ArrayList<>();

        for (BomItem item : items) {
            BomExpandResponse.BomTreeNode node = new BomExpandResponse.BomTreeNode();
            node.setLevel(level);
            node.setMaterialId(item.getMaterialId());
            node.setMaterialCode(item.getMaterialCode());
            node.setMaterialName(item.getMaterialName());
            node.setQuantity(item.getQuantity());

            // 查找子BOM
            List<Bom> childBoms = this.list(
                new LambdaQueryWrapper<Bom>()
                    .eq(Bom::getProductId, item.getMaterialId())
                    .eq(Bom::getApproveStatus, ApproveStatusEnum.APPROVED.getCode())
                    .eq(Bom::getDeleted, EngConstant.NOT_DELETED)
            );

            if (!childBoms.isEmpty()) {
                Bom childBom = childBoms.get(0); // 取默认版本
                List<BomItem> childItems = bomItemMapper.selectList(
                    new LambdaQueryWrapper<BomItem>()
                        .eq(BomItem::getBomId, childBom.getId())
                        .eq(BomItem::getDeleted, EngConstant.NOT_DELETED)
                );
                node.setChildren(buildMultiLevelTree(childItems, level + 1));
            }

            tree.add(node);
        }

        return tree;
    }

    @Override
    public BomWhereUsedResponse whereUsed(Long materialId, String level) {
        BomWhereUsedResponse response = new BomWhereUsedResponse();
        response.setMaterialId(materialId);

        List<BomWhereUsedResponse.UsedInBom> usedList = new ArrayList<>();

        // 查询使用该物料的BOM明细
        List<BomItem> items = bomItemMapper.selectList(
            new LambdaQueryWrapper<BomItem>()
                .eq(BomItem::getMaterialId, materialId)
                .eq(BomItem::getDeleted, EngConstant.NOT_DELETED)
        );

        for (BomItem item : items) {
            Bom bom = this.getById(item.getBomId());
            if (bom != null && bom.getDeleted() == EngConstant.NOT_DELETED) {
                BomWhereUsedResponse.UsedInBom used = new BomWhereUsedResponse.UsedInBom();
                used.setBomId(bom.getId());
                used.setBomCode(bom.getBomCode());
                used.setProductName(bom.getProductName());
                used.setQuantity(item.getQuantity());
                used.setLevel(1);
                usedList.add(used);
            }
        }

        response.setUsedIn(usedList);
        return response;
    }

    @Override
    public boolean checkCircularReference(Long productId, Long materialId) {
        // 递归检查是否存在循环引用
        return checkCircularRefRecursive(productId, materialId, new ArrayList<>());
    }

    private boolean checkCircularRefRecursive(Long productId, Long materialId,
                                               List<Long> visited) {
        if (productId.equals(materialId)) {
            return true;
        }

        if (visited.contains(materialId)) {
            return false;
        }
        visited.add(materialId);

        // 查询materialId的子物料
        List<Bom> boms = this.list(
            new LambdaQueryWrapper<Bom>()
                .eq(Bom::getProductId, materialId)
                .eq(Bom::getDeleted, EngConstant.NOT_DELETED)
        );

        for (Bom bom : boms) {
            List<BomItem> items = bomItemMapper.selectList(
                new LambdaQueryWrapper<BomItem>()
                    .eq(BomItem::getBomId, bom.getId())
                    .eq(BomItem::getDeleted, EngConstant.NOT_DELETED)
            );

            for (BomItem item : items) {
                if (checkCircularRefRecursive(productId, item.getMaterialId(), visited)) {
                    return true;
                }
            }
        }

        return false;
    }

    private void saveBomItems(Long bomId, List<BomCreateRequest.BomItemRequest> items) {
        for (BomCreateRequest.BomItemRequest itemRequest : items) {
            BomItem item = new BomItem();
            item.setBomId(bomId);
            item.setSeqNo(itemRequest.getSeqNo());
            item.setMaterialId(itemRequest.getMaterialId());
            item.setQuantity(itemRequest.getQuantity());
            item.setLossRate(itemRequest.getLossRate());
            item.setIsFixed(itemRequest.getIsFixed());
            item.setValidFlag(itemRequest.getValidFlag());
            bomItemMapper.insert(item);
        }
    }

    private boolean checkVersionExists(Long productId, String version, Long excludeId) {
        LambdaQueryWrapper<Bom> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(Bom::getProductId, productId)
               .eq(Bom::getVersion, version)
               .eq(Bom::getDeleted, EngConstant.NOT_DELETED);

        if (excludeId != null) {
            wrapper.ne(Bom::getId, excludeId);
        }

        return this.count(wrapper) > 0;
    }

    private String generateBomCode() {
        return "BOM-" + System.currentTimeMillis();
    }
}
```

---

### 2.3 工艺路线模块

#### 2.3.1 RouteService

```java
package com.autoerp.eng.service;

import com.autoerp.common.core.PageResult;
import com.autoerp.eng.dto.request.RouteCreateRequest;
import com.autoerp.eng.dto.request.RouteQueryRequest;
import com.autoerp.eng.dto.response.RouteDetailResponse;
import com.autoerp.eng.entity.Route;
import com.autoerp.eng.vo.RouteVo;
import com.baomidou.mybatisplus.extension.service.IService;

/**
 * 工艺路线服务接口
 */
public interface RouteService extends IService<Route> {

    /**
     * 分页查询工艺路线
     */
    PageResult<RouteVo> queryPage(RouteQueryRequest request);

    /**
     * 获取工艺路线详情
     */
    RouteDetailResponse getDetail(Long id);

    /**
     * 创建工艺路线
     */
    Long create(RouteCreateRequest request);

    /**
     * 更新工艺路线
     */
    void update(Long id, RouteCreateRequest request);

    /**
     * 删除工艺路线
     */
    void delete(Long id);

    /**
     * 审批工艺路线
     */
    void approve(Long id, Integer approveResult, String approveOpinion);

    /**
     * 复制工艺路线
     */
    Long copy(Long id, String routeName, Long productId);

    /**
     * 获取产品默认工艺路线
     */
    Route getDefaultRoute(Long productId);

    /**
     * 计算总工时
     */
    Double calculateTotalTime(Long id);
}
```

---

### 2.4 工程变更模块

#### 2.4.1 EcrService

```java
package com.autoerp.eng.service;

import com.autoerp.common.core.PageResult;
import com.autoerp.eng.dto.request.EcrCreateRequest;
import com.autoerp.eng.dto.request.EcrQueryRequest;
import com.autoerp.eng.dto.response.EcrDetailResponse;
import com.autoerp.eng.dto.response.EcrImpactResponse;
import com.autoerp.eng.entity.Ecr;
import com.autoerp.eng.vo.EcrVo;
import com.baomidou.mybatisplus.extension.service.IService;

/**
 * 工程变更请求服务接口
 */
public interface EcrService extends IService<Ecr> {

    /**
     * 分页查询ECR
     */
    PageResult<EcrVo> queryPage(EcrQueryRequest request);

    /**
     * 获取ECR详情
     */
    EcrDetailResponse getDetail(Long id);

    /**
     * 创建ECR
     */
    Long create(EcrCreateRequest request);

    /**
     * 提交审批
     */
    void submit(Long id);

    /**
     * 影响分析
     */
    EcrImpactResponse analyzeImpact(Long id);

    /**
     * 审批ECR
     */
    void approve(Long id, Integer approveResult, String approveOpinion);
}
```

#### 2.4.2 EcoService

```java
package com.autoerp.eng.service;

import com.autoerp.common.core.PageResult;
import com.autoerp.eng.dto.request.EcoCreateRequest;
import com.autoerp.eng.dto.request.EcoQueryRequest;
import com.autoerp.eng.dto.response.EcoDetailResponse;
import com.autoerp.eng.dto.response.EcoProgressResponse;
import com.autoerp.eng.entity.Eco;
import com.autoerp.eng.vo.EcoVo;
import com.baomidou.mybatisplus.extension.service.IService;

/**
 * 工程变更指令服务接口
 */
public interface EcoService extends IService<Eco> {

    /**
     * 分页查询ECO
     */
    PageResult<EcoVo> queryPage(EcoQueryRequest request);

    /**
     * 获取ECO详情
     */
    EcoDetailResponse getDetail(Long id);

    /**
     * 创建ECO
     */
    Long create(EcoCreateRequest request);

    /**
     * 开始执行
     */
    void startExecute(Long id);

    /**
     * 执行变更操作
     */
    void executeAction(Long id, Integer actionType, String actionDesc,
                       Long targetId, Map<String, Object> changes);

    /**
     * 查询执行进度
     */
    EcoProgressResponse getProgress(Long id);

    /**
     * 关闭ECO
     */
    void close(Long id);
}
```

---

### 2.5 MES集成模块

#### 2.5.1 SyncService

```java
package com.autoerp.eng.service;

import com.autoerp.eng.dto.response.SyncLogResponse;
import com.autoerp.eng.entity.SyncLog;

import java.util.List;

/**
 * MES同步服务接口
 */
public interface SyncService {

    /**
     * 同步BOM到MES
     */
    void syncBom(Long bomId);

    /**
     * 同步工艺路线到MES
     */
    void syncRoute(Long routeId);

    /**
     * 同步工程变更到MES
     */
    void syncEco(Long ecoId);

    /**
     * 查询同步日志
     */
    List<SyncLogResponse> querySyncLogs(Integer syncType, Integer syncStatus,
                                         String startTime, String endTime);

    /**
     * 重试同步
     */
    void retrySync(Long logId);
}
```

#### 2.5.2 SyncServiceImpl

```java
package com.autoerp.eng.service.impl;

import com.autoerp.common.exception.BusinessException;
import com.autoerp.eng.dto.response.SyncLogResponse;
import com.autoerp.eng.entity.*;
import com.autoerp.eng.enums.SyncStatusEnum;
import com.autoerp.eng.mapper.*;
import com.autoerp.eng.service.SyncService;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.client.RestTemplate;

import java.time.LocalDateTime;
import java.util.*;

/**
 * MES同步服务实现
 */
@Slf4j
@Service
public class SyncServiceImpl implements SyncService {

    @Value("${mes.api.url}")
    private String mesApiUrl;

    @Autowired
    private BomMapper bomMapper;

    @Autowired
    private BomItemMapper bomItemMapper;

    @Autowired
    private RouteMapper routeMapper;

    @Autowired
    private RouteItemMapper routeItemMapper;

    @Autowired
    private SyncLogMapper syncLogMapper;

    @Autowired
    private RestTemplate restTemplate;

    @Autowired
    private ObjectMapper objectMapper;

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void syncBom(Long bomId) {
        Bom bom = bomMapper.selectById(bomId);
        if (bom == null) {
            throw new BusinessException("BOM不存在");
        }

        // 构建同步数据
        Map<String, Object> syncData = buildBomSyncData(bom);

        // 调用MES接口
        SyncLog syncLog = new SyncLog();
        syncLog.setSyncType(2); // BOM类型
        syncLog.setBusinessId(bomId);
        syncLog.setBusinessCode(bom.getBomCode());
        syncLog.setSyncDirection(1); // ERP到MES

        try {
            String requestData = objectMapper.writeValueAsString(syncData);
            syncLog.setRequestData(requestData);

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            HttpEntity<String> entity = new HttpEntity<>(requestData, headers);

            ResponseEntity<String> response = restTemplate.postForEntity(
                mesApiUrl + "/api/bom/receive", entity, String.class);

            if (response.getStatusCode() == HttpStatus.OK) {
                syncLog.setSyncStatus(SyncStatusEnum.SUCCESS.getCode());
                bom.setSyncStatus(SyncStatusEnum.SUCCESS.getCode());
                bom.setSyncTime(LocalDateTime.now());
            } else {
                syncLog.setSyncStatus(SyncStatusEnum.FAILED.getCode());
                syncLog.setErrorMsg("MES返回错误: " + response.getStatusCode());
                bom.setSyncStatus(SyncStatusEnum.FAILED.getCode());
            }

            syncLog.setResponseData(response.getBody());

        } catch (Exception e) {
            log.error("同步BOM到MES失败", e);
            syncLog.setSyncStatus(SyncStatusEnum.FAILED.getCode());
            syncLog.setErrorMsg(e.getMessage());
            bom.setSyncStatus(SyncStatusEnum.FAILED.getCode());
        }

        syncLog.setSyncTime(LocalDateTime.now());
        syncLogMapper.insert(syncLog);
        bomMapper.updateById(bom);

        if (syncLog.getSyncStatus() != SyncStatusEnum.SUCCESS.getCode()) {
            throw new BusinessException("同步MES失败: " + syncLog.getErrorMsg());
        }
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void syncRoute(Long routeId) {
        Route route = routeMapper.selectById(routeId);
        if (route == null) {
            throw new BusinessException("工艺路线不存在");
        }

        // 构建同步数据
        Map<String, Object> syncData = buildRouteSyncData(route);

        // 调用MES接口
        SyncLog syncLog = new SyncLog();
        syncLog.setSyncType(3); // 工艺路线类型
        syncLog.setBusinessId(routeId);
        syncLog.setBusinessCode(route.getRouteCode());
        syncLog.setSyncDirection(1);

        try {
            String requestData = objectMapper.writeValueAsString(syncData);
            syncLog.setRequestData(requestData);

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            HttpEntity<String> entity = new HttpEntity<>(requestData, headers);

            ResponseEntity<String> response = restTemplate.postForEntity(
                mesApiUrl + "/api/route/receive", entity, String.class);

            if (response.getStatusCode() == HttpStatus.OK) {
                syncLog.setSyncStatus(SyncStatusEnum.SUCCESS.getCode());
                route.setSyncStatus(SyncStatusEnum.SUCCESS.getCode());
                route.setSyncTime(LocalDateTime.now());
            } else {
                syncLog.setSyncStatus(SyncStatusEnum.FAILED.getCode());
                syncLog.setErrorMsg("MES返回错误: " + response.getStatusCode());
                route.setSyncStatus(SyncStatusEnum.FAILED.getCode());
            }

            syncLog.setResponseData(response.getBody());

        } catch (Exception e) {
            log.error("同步工艺路线到MES失败", e);
            syncLog.setSyncStatus(SyncStatusEnum.FAILED.getCode());
            syncLog.setErrorMsg(e.getMessage());
            route.setSyncStatus(SyncStatusEnum.FAILED.getCode());
        }

        syncLog.setSyncTime(LocalDateTime.now());
        syncLogMapper.insert(syncLog);
        routeMapper.updateById(route);

        if (syncLog.getSyncStatus() != SyncStatusEnum.SUCCESS.getCode()) {
            throw new BusinessException("同步MES失败: " + syncLog.getErrorMsg());
        }
    }

    private Map<String, Object> buildBomSyncData(Bom bom) {
        Map<String, Object> data = new HashMap<>();
        data.put("bomCode", bom.getBomCode());
        data.put("productCode", bom.getProductCode());
        data.put("productName", bom.getProductName());
        data.put("version", bom.getVersion());
        data.put("effectiveDate", bom.getEffectiveDate());

        // 获取BOM明细
        List<BomItem> items = bomItemMapper.selectList(
            new LambdaQueryWrapper<BomItem>()
                .eq(BomItem::getBomId, bom.getId())
                .eq(BomItem::getDeleted, 0));

        List<Map<String, Object>> itemData = new ArrayList<>();
        for (BomItem item : items) {
            Map<String, Object> itemMap = new HashMap<>();
            itemMap.put("seqNo", item.getSeqNo());
            itemMap.put("materialCode", item.getMaterialCode());
            itemMap.put("quantity", item.getQuantity());
            itemMap.put("lossRate", item.getLossRate());
            itemData.add(itemMap);
        }
        data.put("items", itemData);

        return data;
    }

    private Map<String, Object> buildRouteSyncData(Route route) {
        Map<String, Object> data = new HashMap<>();
        data.put("routeCode", route.getRouteCode());
        data.put("routeName", route.getRouteName());
        data.put("productCode", route.getProductCode());
        data.put("version", route.getVersion());
        data.put("effectiveDate", route.getEffectiveDate());

        // 获取工艺路线明细
        List<RouteItem> items = routeItemMapper.selectList(
            new LambdaQueryWrapper<RouteItem>()
                .eq(RouteItem::getRouteId, route.getId())
                .eq(RouteItem::getDeleted, 0)
                .orderByAsc(RouteItem::getSeqNo));

        List<Map<String, Object>> itemData = new ArrayList<>();
        for (RouteItem item : items) {
            Map<String, Object> itemMap = new HashMap<>();
            itemMap.put("seqNo", item.getSeqNo());
            itemMap.put("operationCode", item.getOperationCode());
            itemMap.put("operationName", item.getOperationName());
            itemMap.put("stdTime", item.getStdTime());
            itemMap.put("setupTime", item.getSetupTime());
            itemMap.put("workCenterCode", item.getWorkCenterCode());
            itemData.add(itemMap);
        }
        data.put("items", itemData);

        return data;
    }

    @Override
    public List<SyncLogResponse> querySyncLogs(Integer syncType, Integer syncStatus,
                                                String startTime, String endTime) {
        // TODO: 实现查询逻辑
        return new ArrayList<>();
    }

    @Override
    public void syncEco(Long ecoId) {
        // TODO: 实现ECO同步逻辑
    }

    @Override
    public void retrySync(Long logId) {
        SyncLog log = syncLogMapper.selectById(logId);
        if (log == null || log.getSyncStatus() == SyncStatusEnum.SUCCESS.getCode()) {
            return;
        }

        switch (log.getSyncType()) {
            case 2:
                syncBom(log.getBusinessId());
                break;
            case 3:
                syncRoute(log.getBusinessId());
                break;
            case 4:
                syncEco(log.getBusinessId());
                break;
        }
    }
}
```

---

## 3. 事件处理设计

### 3.1 事件定义

```java
package com.autoerp.eng.event;

import org.springframework.context.ApplicationEvent;

/**
 * 产品审批通过事件
 */
public class ProductApprovedEvent extends ApplicationEvent {

    private Long productId;

    public ProductApprovedEvent(Long productId) {
        super(productId);
        this.productId = productId;
    }

    public Long getProductId() {
        return productId;
    }
}

/**
 * BOM审批通过事件
 */
public class BomApprovedEvent extends ApplicationEvent {
    private Long bomId;

    public BomApprovedEvent(Long bomId) {
        super(bomId);
        this.bomId = bomId;
    }

    public Long getBomId() {
        return bomId;
    }
}

/**
 * ECO关闭事件
 */
public class EcoClosedEvent extends ApplicationEvent {
    private Long ecoId;

    public EcoClosedEvent(Long ecoId) {
        super(ecoId);
        this.ecoId = ecoId;
    }

    public Long getEcoId() {
        return ecoId;
    }
}
```

### 3.2 事件监听器

```java
package com.autoerp.eng.listener;

import com.autoerp.eng.event.BomApprovedEvent;
import com.autoerp.eng.event.EcoClosedEvent;
import com.autoerp.eng.event.RouteApprovedEvent;
import com.autoerp.eng.service.SyncService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.event.EventListener;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Component;

/**
 * 工程事件监听器
 */
@Slf4j
@Component
public class EngineeringEventListener {

    @Autowired
    private SyncService syncService;

    /**
     * 监听BOM审批通过事件
     */
    @Async
    @EventListener
    public void onBomApproved(BomApprovedEvent event) {
        log.info("BOM审批通过，自动同步到MES, bomId={}", event.getBomId());
        try {
            syncService.syncBom(event.getBomId());
        } catch (Exception e) {
            log.error("同步BOM到MES失败", e);
        }
    }

    /**
     * 监听工艺路线审批通过事件
     */
    @Async
    @EventListener
    public void onRouteApproved(RouteApprovedEvent event) {
        log.info("工艺路线审批通过，自动同步到MES, routeId={}", event.getRouteId());
        try {
            syncService.syncRoute(event.getRouteId());
        } catch (Exception e) {
            log.error("同步工艺路线到MES失败", e);
        }
    }

    /**
     * 监听ECO关闭事件
     */
    @Async
    @EventListener
    public void onEcoClosed(EcoClosedEvent event) {
        log.info("ECO关闭，通知MES变更, ecoId={}", event.getEcoId());
        try {
            syncService.syncEco(event.getEcoId());
        } catch (Exception e) {
            log.error("同步ECO到MES失败", e);
        }
    }
}
```

---

## 4. 枚举类设计

```java
package com.autoerp.eng.enums;

import lombok.AllArgsConstructor;
import lombok.Getter;

/**
 * 产品类型枚举
 */
@Getter
@AllArgsConstructor
public enum ProductTypeEnum {

    SELF_MADE(1, "自制件"),
    PURCHASED(2, "外购件"),
    OUTSOURCED(3, "外协件"),
    PHANTOM(4, "虚拟件");

    private final Integer code;
    private final String name;

    public static ProductTypeEnum getByCode(Integer code) {
        for (ProductTypeEnum e : values()) {
            if (e.getCode().equals(code)) {
                return e;
            }
        }
        return null;
    }
}

/**
 * 产品状态枚举
 */
@Getter
@AllArgsConstructor
public enum ProductStatusEnum {

    DEVELOPING(1, "研发中"),
    TRIAL(2, "试产"),
    MASS_PRODUCTION(3, "量产"),
    DISCONTINUED(4, "停产"),
    OBSOLETE(5, "淘汰");

    private final Integer code;
    private final String name;
}

/**
 * 审批状态枚举
 */
@Getter
@AllArgsConstructor
public enum ApproveStatusEnum {

    DRAFT(0, "草稿"),
    PENDING(1, "待审"),
    APPROVED(2, "已审"),
    REJECTED(3, "驳回");

    private final Integer code;
    private final String name;
}

/**
 * 同步状态枚举
 */
@Getter
@AllArgsConstructor
public enum SyncStatusEnum {

    NOT_SYNCED(0, "未同步"),
    SUCCESS(1, "已同步"),
    FAILED(2, "同步失败");

    private final Integer code;
    private final String name;
}

/**
 * ECR状态枚举
 */
@Getter
@AllArgsConstructor
public enum EcrStatusEnum {

    DRAFT(1, "草稿"),
    PENDING(2, "待审"),
    REVIEWING(3, "评审中"),
    APPROVED(4, "已批准"),
    REJECTED(5, "已驳回"),
    CLOSED(6, "已关闭");

    private final Integer code;
    private final String name;
}

/**
 * ECO状态枚举
 */
@Getter
@AllArgsConstructor
public enum EcoStatusEnum {

    PENDING(1, "待执行"),
    EXECUTING(2, "执行中"),
    COMPLETED(3, "已完成"),
    CLOSED(4, "已关闭");

    private final Integer code;
    private final String name;
}
```

---

## 5. 配置类设计

```java
package com.autoerp.eng.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

/**
 * 工程模块配置
 */
@Configuration
public class EngConfig {

    /**
     * RestTemplate用于调用MES接口
     */
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}
```

```yaml
# application.yml配置
mes:
  api:
    url: http://mes-server:8080
    timeout: 30000

eng:
  bom:
    max-level: 10  # BOM最大层级
  code:
    product-prefix: PROD
    bom-prefix: BOM
    route-prefix: RT
    ecr-prefix: ECR
    eco-prefix: ECO
```

---

## 6. 常量类设计

```java
package com.autoerp.eng.constant;

/**
 * 工程模块常量
 */
public class EngConstant {

    /** 删除标记 - 未删除 */
    public static final int NOT_DELETED = 0;

    /** 删除标记 - 已删除 */
    public static final int DELETED = 1;

    /** 业务类型 - 产品 */
    public static final int BUSINESS_TYPE_PRODUCT = 1;

    /** 业务类型 - BOM */
    public static final int BUSINESS_TYPE_BOM = 2;

    /** 业务类型 - 工艺路线 */
    public static final int BUSINESS_TYPE_ROUTE = 3;

    /** 业务类型 - ECR */
    public static final int BUSINESS_TYPE_ECR = 4;

    /** 业务类型 - ECO */
    public static final int BUSINESS_TYPE_ECO = 5;

    /** 审批结果 - 通过 */
    public static final int APPROVE_PASS = 1;

    /** 审批结果 - 驳回 */
    public static final int APPROVE_REJECT = 2;

    /** 变更动作 - 新增 */
    public static final int CHANGE_ACTION_ADD = 1;

    /** 变更动作 - 修改 */
    public static final int CHANGE_ACTION_MODIFY = 2;

    /** 变更动作 - 删除 */
    public static final int CHANGE_ACTION_DELETE = 3;
}
```

---

## 7. 设计要点总结

### 7.1 核心设计原则

1. **分层架构**: Controller -> Service -> Mapper 清晰分层
2. **领域驱动**: 实体类与业务逻辑紧密结合
3. **事件驱动**: 使用Spring事件机制解耦业务流程
4. **多租户隔离**: 所有查询自动添加tenant_id条件
5. **逻辑删除**: 保留历史数据，支持数据恢复

### 7.2 关键技术实现

| 技术点 | 实现方式 |
|--------|----------|
| BOM展开 | 递归算法实现多级展开 |
| 循环引用检测 | 递归检测+访问标记 |
| 版本控制 | 快照存储+版本号递增 |
| 审批流程 | 状态机+事件发布 |
| MES同步 | RestTemplate调用+重试机制 |
| 影响分析 | 图遍历算法分析关联对象 |

### 7.3 性能优化策略

1. **BOM展开缓存**: 使用Redis缓存展开结果
2. **批量查询优化**: 使用IN查询减少数据库交互
3. **异步处理**: MES同步、通知发送使用异步处理
4. **索引优化**: 根据查询条件建立合适索引

---

## 8. 版本历史

| 版本 | 日期 | 修改人 | 修改内容 |
|------|------|--------|----------|
| V1.0 | 2026-03-24 | 研发组 | 初始版本 |

---

*文档结束*