# 销售管理模块(SD) 详细设计文档

## 文档信息

| 项目 | 内容 |
|------|------|
| 文档编号 | Detail-01 |
| 模块名称 | 销售管理(Sales and Distribution) |
| 版本 | V1.0 |
| 创建日期 | 2026-03-24 |
| 技术栈 | Spring Boot 2.7 + MyBatis Plus + MySQL 8.x |

---

## 1. 模块架构设计

### 1.1 总体架构

```
┌─────────────────────────────────────────────────────────────────────┐
│                           表现层 (Controller)                         │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │CustomerCtrl │ │ OrderCtrl   │ │ ConfigCtrl  │ │DeliveryCtrl │   │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│                           业务层 (Service)                           │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │CustomerSvc  │ │ OrderSvc    │ │ ConfigSvc   │ │DeliverySvc  │   │
│  │             │ │             │ │             │ │             │   │
│  │ ┌─────────┐ │ │ ┌─────────┐ │ │ ┌─────────┐ │ │ ┌─────────┐ │   │
│  │ │CreditMgr│ │ │ │VinMgr   │ │ │ │PriceMgr │ │ │ │PdiMgr   │ │   │
│  │ └─────────┘ │ │ └─────────┘ │ │ └─────────┘ │ │ └─────────┘ │   │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │
│                                                                      │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                   │
│  │ApprovalSvc  │ │WorkflowSvc  │ │AnalysisSvc  │                   │
│  └─────────────┘ └─────────────┘ └─────────────┘                   │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│                           数据层 (Repository)                        │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │CustomerRepo │ │ OrderRepo   │ │ ConfigRepo  │ │DeliveryRepo │   │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│                           数据库层 (MySQL)                           │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │sd_customer  │ │ sd_order    │ │ sd_model    │ │sd_delivery  │   │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 模块依赖关系

```
┌──────────────────┐
│   销售管理模块    │
│      (SD)        │
└────────┬─────────┘
         │
    ┌────┴────┬────────────┬────────────┐
    │         │            │            │
    ▼         ▼            ▼            ▼
┌───────┐ ┌───────┐   ┌───────┐   ┌───────┐
│ 基础  │ │ 库存  │   │ 生产  │   │ 财务  │
│ 数据  │ │ 管理  │   │ 管理  │   │ 管理  │
│(Base) │ │ (WMS) │   │ (MES) │   │  (FI) │
└───────┘ └───────┘   └───────┘   └───────┘
```

### 1.3 包结构设计

```
com.autoerp.sale
├── controller              // 控制器层
│   ├── CustomerController.java
│   ├── DealerController.java
│   ├── OrderController.java
│   ├── OrderConfigController.java
│   ├── DeliveryController.java
│   └── AnalysisController.java
├── service                 // 服务层接口
│   ├── CustomerService.java
│   ├── DealerService.java
│   ├── OrderService.java
│   ├── OrderConfigService.java
│   ├── DeliveryService.java
│   └── AnalysisService.java
├── service.impl            // 服务层实现
│   ├── CustomerServiceImpl.java
│   ├── DealerServiceImpl.java
│   ├── OrderServiceImpl.java
│   ├── OrderConfigServiceImpl.java
│   ├── DeliveryServiceImpl.java
│   └── AnalysisServiceImpl.java
├── manager                 // 业务管理器
│   ├── CreditManager.java
│   ├── VinManager.java
│   ├── PriceManager.java
│   ├── PdiManager.java
│   └── WorkflowManager.java
├── repository              // 数据访问层
│   ├── CustomerRepository.java
│   ├── DealerRepository.java
│   ├── OrderRepository.java
│   └── DeliveryRepository.java
├── entity                  // 实体类
│   ├── CustomerEntity.java
│   ├── DealerEntity.java
│   ├── OrderEntity.java
│   ├── OrderItemEntity.java
│   └── DeliveryPlanEntity.java
├── dto                     // 数据传输对象
│   ├── request             // 请求DTO
│   │   ├── CustomerCreateRequest.java
│   │   ├── OrderCreateRequest.java
│   │   └── DeliveryPlanRequest.java
│   └── response            // 响应DTO
│       ├── CustomerResponse.java
│       ├── OrderResponse.java
│       └── DeliveryPlanResponse.java
├── converter               // 对象转换器
│   ├── CustomerConverter.java
│   ├── OrderConverter.java
│   └── DeliveryConverter.java
├── enums                   // 枚举类
│   ├── CustomerTypeEnum.java
│   ├── OrderStatusEnum.java
│   ├── DeliveryStatusEnum.java
│   └── VinStatusEnum.java
├── event                   // 事件类
│   ├── OrderCreatedEvent.java
│   ├── OrderApprovedEvent.java
│   └── DeliveryCompletedEvent.java
├── listener                // 事件监听器
│   └── OrderEventListener.java
├── mq                      // 消息队列
│   ├── producer
│   │   └── OrderMessageProducer.java
│   └── consumer
│       └── ProductionMessageConsumer.java
└── util                    // 工具类
    ├── OrderNoGenerator.java
    ├── VinValidator.java
    └── PriceCalculator.java
```

---

## 2. 核心类设计

### 2.1 实体类设计

#### 2.1.1 客户实体类

```java
/**
 * 客户实体类
 */
@Data
@TableName("sd_customer")
public class CustomerEntity {

    /** 主键ID */
    @TableId(type = IdType.AUTO)
    private Long id;

    /** 租户ID */
    private Long tenantId;

    /** 客户编码 */
    private String customerCode;

    /** 客户名称 */
    private String customerName;

    /** 客户类型: 1-个人, 2-企业, 3-经销商, 4-大客户 */
    private Integer customerType;

    /** 客户等级: 1-A级, 2-B级, 3-C级, 4-D级 */
    private Integer customerLevel;

    /** 手机号(加密存储) */
    private String mobile;

    /** 邮箱 */
    private String email;

    /** 身份证号(加密存储) */
    private String idCard;

    /** 性别: 1-男, 2-女 */
    private Integer gender;

    /** 年龄 */
    private Integer age;

    /** 省份 */
    private String province;

    /** 城市 */
    private String city;

    /** 详细地址 */
    private String address;

    /** 购车意向车型 */
    private String intentionModel;

    /** 预算范围 */
    private String budgetRange;

    /** 信息来源 */
    private String infoSource;

    /** 销售代表ID */
    private Long salesRepId;

    /** 销售代表姓名 */
    private String salesRepName;

    /** 信用额度 */
    private BigDecimal creditLimit;

    /** 已用信用额度 */
    private BigDecimal creditUsed;

    /** 状态: 0-禁用, 1-启用 */
    private Integer status;

    /** 标签(JSON格式) */
    private String tags;

    /** 备注 */
    private String remark;

    /** 创建人 */
    private String createdBy;

    /** 创建时间 */
    private LocalDateTime createdTime;

    /** 更新人 */
    private String updatedBy;

    /** 更新时间 */
    private LocalDateTime updatedTime;

    /** 删除标记: 0-未删除, 1-已删除 */
    @TableLogic
    private Integer deleted;
}
```

#### 2.1.2 销售订单实体类

```java
/**
 * 销售订单实体类
 */
@Data
@TableName("sd_order")
public class OrderEntity {

    /** 主键ID */
    @TableId(type = IdType.AUTO)
    private Long id;

    /** 租户ID */
    private Long tenantId;

    /** 订单编号 */
    private String orderNo;

    /** 订单类型: 1-标准订单, 2-紧急订单, 3-经销商订单, 4-大客户订单 */
    private Integer orderType;

    /** 订单来源: 1-手工录入, 2-经销商系统, 3-官网, 4-移动端 */
    private Integer orderSource;

    /** 客户ID */
    private Long customerId;

    /** 客户编码 */
    private String customerCode;

    /** 客户名称 */
    private String customerName;

    /** 客户类型 */
    private Integer customerType;

    /** 销售代表ID */
    private Long salesRepId;

    /** 销售代表姓名 */
    private String salesRepName;

    /** 订单日期 */
    private LocalDate orderDate;

    /** 要求交付日期 */
    private LocalDate requiredDate;

    /** 承诺交付日期 */
    private LocalDate promiseDate;

    /** 车型ID */
    private Long modelId;

    /** 车型编码 */
    private String modelCode;

    /** 车型名称 */
    private String modelName;

    /** VIN码 */
    private String vinCode;

    /** VIN状态: 0-未分配, 1-预占, 2-已绑定 */
    private Integer vinStatus;

    /** 订单数量 */
    private Integer orderQty;

    /** 基础价格 */
    private BigDecimal basePrice;

    /** 配置加价 */
    private BigDecimal optionPrice;

    /** 总价 */
    private BigDecimal totalPrice;

    /** 折扣率(%) */
    private BigDecimal discountRate;

    /** 折扣金额 */
    private BigDecimal discountAmount;

    /** 优惠金额 */
    private BigDecimal promotionAmount;

    /** 最终金额 */
    private BigDecimal finalAmount;

    /** 交付方式: 1-到店自提, 2-送车上门, 3-物流配送 */
    private Integer deliveryMethod;

    /** 交付地址 */
    private String deliveryAddress;

    /** 收货人 */
    private String receiverName;

    /** 收货电话 */
    private String receiverPhone;

    /** 付款方式: 1-全款, 2-分期, 3-混合 */
    private Integer paymentMethod;

    /** 订单状态: 10-待确认, 20-已确认, 30-生产中, 50-待交付, 60-交付中, 70-已完成, 80-已取消, 85-异常, 90-已关闭 */
    private Integer orderStatus;

    /** 审批状态: 0-待审批, 1-已通过, 2-已驳回 */
    private Integer approvalStatus;

    /** 审批人 */
    private String approvalBy;

    /** 审批时间 */
    private LocalDateTime approvalTime;

    /** 审批备注 */
    private String approvalRemark;

    /** 备注 */
    private String remark;

    /** 创建人 */
    private String createdBy;

    /** 创建时间 */
    private LocalDateTime createdTime;

    /** 更新人 */
    private String updatedBy;

    /** 更新时间 */
    private LocalDateTime updatedTime;

    /** 删除标记 */
    @TableLogic
    private Integer deleted;
}
```

#### 2.1.3 订单明细实体类

```java
/**
 * 销售订单明细实体类
 */
@Data
@TableName("sd_order_item")
public class OrderItemEntity {

    /** 主键ID */
    @TableId(type = IdType.AUTO)
    private Long id;

    /** 租户ID */
    private Long tenantId;

    /** 订单ID */
    private Long orderId;

    /** 订单编号 */
    private String orderNo;

    /** 行号 */
    private Integer lineNo;

    /** 车型ID */
    private Long modelId;

    /** 车型编码 */
    private String modelCode;

    /** 车型名称 */
    private String modelName;

    /** 配置代码 */
    private String configCode;

    /** 外观颜色 */
    private String colorExt;

    /** 内饰颜色 */
    private String colorInt;

    /** 轮毂 */
    private String wheel;

    /** 选装配置(JSON) */
    private String options;

    /** 订单数量 */
    private Integer orderQty;

    /** 基础价格 */
    private BigDecimal basePrice;

    /** 配置加价 */
    private BigDecimal optionPrice;

    /** 单价 */
    private BigDecimal unitPrice;

    /** 折扣率 */
    private BigDecimal discountRate;

    /** 折扣金额 */
    private BigDecimal discountAmount;

    /** 行金额 */
    private BigDecimal lineAmount;

    /** 备注 */
    private String remark;

    /** 创建时间 */
    private LocalDateTime createdTime;

    /** 更新时间 */
    private LocalDateTime updatedTime;

    /** 删除标记 */
    @TableLogic
    private Integer deleted;
}
```

---

### 2.2 服务层设计

#### 2.2.1 客户服务接口

```java
/**
 * 客户服务接口
 */
public interface CustomerService {

    /**
     * 分页查询客户列表
     */
    PageResult<CustomerResponse> queryCustomerPage(CustomerQueryRequest request);

    /**
     * 查询客户详情
     */
    CustomerDetailResponse getCustomerDetail(Long id);

    /**
     * 创建客户
     */
    Long createCustomer(CustomerCreateRequest request);

    /**
     * 更新客户
     */
    void updateCustomer(Long id, CustomerUpdateRequest request);

    /**
     * 删除客户
     */
    void deleteCustomer(Long id);

    /**
     * 设置信用额度
     */
    Long setCreditLimit(Long id, CreditLimitRequest request);

    /**
     * 调整信用额度
     */
    Long adjustCreditLimit(Long id, CreditAdjustRequest request);

    /**
     * 查询信用额度使用情况
     */
    CreditUsageResponse getCreditUsage(Long id);

    /**
     * 更新客户标签
     */
    void updateTags(Long id, List<String> tags);

    /**
     * 添加联系记录
     */
    Long addContactRecord(Long id, ContactRecordRequest request);

    /**
     * 查询联系记录
     */
    List<ContactRecordResponse> getContactRecords(Long id);
}
```

#### 2.2.2 客户服务实现类

```java
/**
 * 客户服务实现类
 */
@Service
@Slf4j
@RequiredArgsConstructor
public class CustomerServiceImpl implements CustomerService {

    private final CustomerRepository customerRepository;
    private final CustomerConverter customerConverter;
    private final CreditManager creditManager;
    private final ApprovalService approvalService;

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long createCustomer(CustomerCreateRequest request) {
        // 1. 参数校验
        validateCustomerRequest(request);

        // 2. 检查手机号唯一性
        if (StringUtils.isNotBlank(request.getMobile())) {
            CustomerEntity existCustomer = customerRepository.findByMobile(
                request.getMobile(), TenantContext.getTenantId());
            if (existCustomer != null) {
                throw new BusinessException(20003, "客户手机号已存在");
            }
        }

        // 3. 构建实体
        CustomerEntity entity = customerConverter.toEntity(request);
        entity.setTenantId(TenantContext.getTenantId());
        entity.setCustomerCode(generateCustomerCode());
        entity.setStatus(1);
        entity.setCreditLimit(BigDecimal.ZERO);
        entity.setCreditUsed(BigDecimal.ZERO);
        entity.setCreatedBy(UserContext.getCurrentUserName());
        entity.setCreatedTime(LocalDateTime.now());

        // 4. 敏感信息加密
        if (StringUtils.isNotBlank(entity.getMobile())) {
            entity.setMobile(EncryptUtils.encrypt(entity.getMobile()));
        }
        if (StringUtils.isNotBlank(entity.getIdCard())) {
            entity.setIdCard(EncryptUtils.encrypt(entity.getIdCard()));
        }

        // 5. 保存
        customerRepository.save(entity);

        log.info("创建客户成功, customerCode={}", entity.getCustomerCode());
        return entity.getId();
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long setCreditLimit(Long id, CreditLimitRequest request) {
        // 1. 查询客户
        CustomerEntity customer = customerRepository.getById(id);
        if (customer == null) {
            throw new BusinessException(20001, "客户不存在");
        }

        // 2. 调用信用管理器
        return creditManager.setCreditLimit(id, request);
    }

    // ... 其他方法实现
}
```

#### 2.2.3 订单服务接口

```java
/**
 * 订单服务接口
 */
public interface OrderService {

    /**
     * 分页查询订单列表
     */
    PageResult<OrderResponse> queryOrderPage(OrderQueryRequest request);

    /**
     * 查询订单详情
     */
    OrderDetailResponse getOrderDetail(Long id);

    /**
     * 创建订单
     */
    Long createOrder(OrderCreateRequest request);

    /**
     * 更新订单
     */
    void updateOrder(Long id, OrderUpdateRequest request);

    /**
     * 提交订单
     */
    OrderSubmitResult submitOrder(Long id);

    /**
     * 审批订单
     */
    void approveOrder(Long id, OrderApproveRequest request);

    /**
     * 取消订单
     */
    void cancelOrder(Long id, OrderCancelRequest request);

    /**
     * 预分配VIN码
     */
    VinAllocateResult allocateVin(Long id);

    /**
     * 绑定VIN码
     */
    void bindVin(Long id, VinBindRequest request);

    /**
     * 查询VIN码信息
     */
    VinInfoResponse queryVinInfo(String vinCode);

    /**
     * 更新订单状态
     */
    void updateOrderStatus(Long id, Integer status, String remark);
}
```

#### 2.2.4 订单服务实现类

```java
/**
 * 订单服务实现类
 */
@Service
@Slf4j
@RequiredArgsConstructor
public class OrderServiceImpl implements OrderService {

    private final OrderRepository orderRepository;
    private final OrderItemRepository orderItemRepository;
    private final CustomerRepository customerRepository;
    private final OrderConverter orderConverter;
    private final VinManager vinManager;
    private final PriceManager priceManager;
    private final CreditManager creditManager;
    private final WorkflowManager workflowManager;
    private final ApplicationEventPublisher eventPublisher;

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long createOrder(OrderCreateRequest request) {
        // 1. 参数校验
        validateOrderRequest(request);

        // 2. 查询客户信息
        CustomerEntity customer = customerRepository.getById(request.getCustomerId());
        if (customer == null) {
            throw new BusinessException(20001, "客户不存在");
        }

        // 3. 构建订单主表
        OrderEntity order = buildOrderEntity(request, customer);

        // 4. 计算价格
        BigDecimal totalPrice = priceManager.calculateOrderPrice(request.getModelId(),
            request.getOptions());
        order.setTotalPrice(totalPrice);
        order.setFinalAmount(totalPrice.subtract(request.getDiscountAmount()));

        // 5. 校验折扣权限
        if (request.getDiscountRate() != null &&
            request.getDiscountRate().compareTo(BigDecimal.ZERO) > 0) {
            validateDiscountPermission(request.getDiscountRate());
        }

        // 6. 校验信用额度
        creditManager.validateCreditLimit(customer.getId(), order.getFinalAmount());

        // 7. 保存订单
        orderRepository.save(order);

        // 8. 保存订单明细
        List<OrderItemEntity> items = buildOrderItems(order, request);
        orderItemRepository.saveBatch(items);

        log.info("创建订单成功, orderNo={}", order.getOrderNo());
        return order.getId();
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public OrderSubmitResult submitOrder(Long id) {
        // 1. 查询订单
        OrderEntity order = orderRepository.getById(id);
        if (order == null) {
            throw new BusinessException(21001, "订单不存在");
        }

        // 2. 校验订单状态
        if (!OrderStatusEnum.DRAFT.getCode().equals(order.getOrderStatus())) {
            throw new BusinessException(21003, "订单状态不允许提交");
        }

        // 3. 判断是否需要审批
        boolean needApproval = workflowManager.checkNeedApproval(order);

        if (needApproval) {
            // 创建审批流程
            Long approvalId = workflowManager.createApproval(order);
            order.setOrderStatus(OrderStatusEnum.PENDING_APPROVAL.getCode());
            orderRepository.updateById(order);

            return OrderSubmitResult.builder()
                .needApproval(true)
                .approvalId(approvalId)
                .build();
        } else {
            // 直接确认
            order.setOrderStatus(OrderStatusEnum.CONFIRMED.getCode());
            orderRepository.updateById(order);

            // 发布订单创建事件
            eventPublisher.publishEvent(new OrderCreatedEvent(order.getId()));

            return OrderSubmitResult.builder()
                .needApproval(false)
                .orderStatus(order.getOrderStatus())
                .build();
        }
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public VinAllocateResult allocateVin(Long id) {
        // 1. 查询订单
        OrderEntity order = orderRepository.getById(id);
        if (order == null) {
            throw new BusinessException(21001, "订单不存在");
        }

        // 2. 校验订单状态
        if (!OrderStatusEnum.CONFIRMED.getCode().equals(order.getOrderStatus())) {
            throw new BusinessException(21003, "订单状态不允许预分配VIN");
        }

        // 3. 调用VIN管理器分配
        return vinManager.allocateVin(order);
    }

    // ... 其他方法实现
}
```

---

### 2.3 管理器设计

#### 2.3.1 信用管理器

```java
/**
 * 客户信用管理器
 */
@Component
@Slf4j
@RequiredArgsConstructor
public class CreditManager {

    private final CustomerRepository customerRepository;
    private final CreditRecordRepository creditRecordRepository;
    private final ApprovalService approvalService;

    /**
     * 设置信用额度
     */
    @Transactional(rollbackFor = Exception.class)
    public Long setCreditLimit(Long customerId, CreditLimitRequest request) {
        CustomerEntity customer = customerRepository.getById(customerId);

        // 判断是否需要审批
        if (request.getCreditLimit().compareTo(new BigDecimal("500000")) > 0) {
            // 需要审批
            ApprovalCreateRequest approvalRequest = ApprovalCreateRequest.builder()
                .bizType("CREDIT_LIMIT")
                .bizId(customerId)
                .title("客户信用额度设置")
                .content("设置客户[" + customer.getCustomerName() + "]信用额度为"
                    + request.getCreditLimit() + "元")
                .build();
            return approvalService.createApproval(approvalRequest);
        } else {
            // 直接设置
            customer.setCreditLimit(request.getCreditLimit());
            customerRepository.updateById(customer);

            // 记录信用变更
            saveCreditRecord(customer, "SET", request.getCreditLimit(), "设置信用额度");

            return null;
        }
    }

    /**
     * 校验信用额度
     */
    public void validateCreditLimit(Long customerId, BigDecimal orderAmount) {
        CustomerEntity customer = customerRepository.getById(customerId);
        if (customer == null) {
            return;
        }

        BigDecimal availableCredit = customer.getCreditLimit()
            .subtract(customer.getCreditUsed());

        if (orderAmount.compareTo(availableCredit) > 0) {
            throw new BusinessException(20005,
                "订单金额超出可用信用额度，可用额度：" + availableCredit);
        }
    }

    /**
     * 占用信用额度
     */
    @Transactional(rollbackFor = Exception.class)
    public void occupyCredit(Long customerId, Long orderId, BigDecimal amount) {
        CustomerEntity customer = customerRepository.getById(customerId);

        BigDecimal beforeUsed = customer.getCreditUsed();
        BigDecimal afterUsed = beforeUsed.add(amount);

        customer.setCreditUsed(afterUsed);
        customerRepository.updateById(customer);

        // 记录信用变更
        CreditRecordEntity record = new CreditRecordEntity();
        record.setTenantId(customer.getTenantId());
        record.setCustomerId(customerId);
        record.setRecordType("OCCUPY");
        record.setRecordNo(orderId.toString());
        record.setBeforeAmount(customer.getCreditLimit());
        record.setChangeAmount(BigDecimal.ZERO);
        record.setAfterAmount(customer.getCreditLimit());
        record.setBeforeUsed(beforeUsed);
        record.setChangeUsed(amount);
        record.setAfterUsed(afterUsed);
        record.setRemark("订单占用信用额度");
        record.setCreatedTime(LocalDateTime.now());
        creditRecordRepository.save(record);
    }

    /**
     * 释放信用额度
     */
    @Transactional(rollbackFor = Exception.class)
    public void releaseCredit(Long customerId, Long orderId, BigDecimal amount) {
        CustomerEntity customer = customerRepository.getById(customerId);

        BigDecimal beforeUsed = customer.getCreditUsed();
        BigDecimal afterUsed = beforeUsed.subtract(amount);
        if (afterUsed.compareTo(BigDecimal.ZERO) < 0) {
            afterUsed = BigDecimal.ZERO;
        }

        customer.setCreditUsed(afterUsed);
        customerRepository.updateById(customer);

        // 记录信用变更
        CreditRecordEntity record = new CreditRecordEntity();
        record.setTenantId(customer.getTenantId());
        record.setCustomerId(customerId);
        record.setRecordType("RELEASE");
        record.setRecordNo(orderId.toString());
        record.setBeforeUsed(beforeUsed);
        record.setChangeUsed(amount.negate());
        record.setAfterUsed(afterUsed);
        record.setRemark("订单释放信用额度");
        record.setCreatedTime(LocalDateTime.now());
        creditRecordRepository.save(record);
    }
}
```

#### 2.3.2 VIN码管理器

```java
/**
 * VIN码管理器
 */
@Component
@Slf4j
@RequiredArgsConstructor
public class VinManager {

    private final VehicleInventoryRepository inventoryRepository;
    private final OrderRepository orderRepository;
    private final VinRecordRepository vinRecordRepository;

    /**
     * 预分配VIN码
     */
    @Transactional(rollbackFor = Exception.class)
    public VinAllocateResult allocateVin(OrderEntity order) {
        // 1. 查询匹配的库存车辆
        List<VehicleInventoryEntity> vehicles = inventoryRepository.findAvailableVehicles(
            order.getModelId(),
            order.getConfigCode(),
            TenantContext.getTenantId()
        );

        if (CollectionUtils.isEmpty(vehicles)) {
            log.warn("未找到匹配的库存车辆, orderId={}", order.getId());
            return VinAllocateResult.builder()
                .success(false)
                .message("未找到匹配的库存车辆")
                .build();
        }

        // 2. 选择第一辆匹配的车辆
        VehicleInventoryEntity vehicle = vehicles.get(0);

        // 3. 更新车辆状态为预占
        vehicle.setStatus(VinStatusEnum.PREOCCUPIED.getCode());
        vehicle.setPreoccupyOrderId(order.getId());
        vehicle.setPreoccupyExpireDate(LocalDate.now().plusDays(30));
        inventoryRepository.updateById(vehicle);

        // 4. 更新订单VIN信息
        order.setVinCode(vehicle.getVinCode());
        order.setVinStatus(VinStatusEnum.PREOCCUPIED.getCode());
        order.setOrderStatus(OrderStatusEnum.IN_PRODUCTION.getCode());
        orderRepository.updateById(order);

        // 5. 记录VIN分配日志
        saveVinRecord(order, vehicle, "ALLOCATE", "VIN码预分配");

        log.info("VIN码预分配成功, orderId={}, vinCode={}", order.getId(), vehicle.getVinCode());

        return VinAllocateResult.builder()
            .success(true)
            .vinCode(vehicle.getVinCode())
            .vinStatus(VinStatusEnum.PREOCCUPIED.getCode())
            .preoccupyExpireDate(vehicle.getPreoccupyExpireDate())
            .build();
    }

    /**
     * 绑定VIN码
     */
    @Transactional(rollbackFor = Exception.class)
    public void bindVin(Long orderId, String vinCode, boolean confirmed) {
        // 1. 查询订单
        OrderEntity order = orderRepository.getById(orderId);
        if (order == null) {
            throw new BusinessException(21001, "订单不存在");
        }

        // 2. 查询车辆
        VehicleInventoryEntity vehicle = inventoryRepository.findByVinCode(vinCode);
        if (vehicle == null) {
            throw new BusinessException(21008, "VIN码不存在");
        }

        // 3. 校验VIN码与订单匹配
        if (!vinCode.equals(order.getVinCode())) {
            // VIN码变更，需要特殊处理
            handleVinChange(order, vinCode, vehicle);
            return;
        }

        // 4. 确认绑定
        vehicle.setStatus(VinStatusEnum.BOUND.getCode());
        inventoryRepository.updateById(vehicle);

        order.setVinStatus(VinStatusEnum.BOUND.getCode());
        order.setOrderStatus(OrderStatusEnum.PENDING_DELIVERY.getCode());
        orderRepository.updateById(order);

        // 5. 记录VIN绑定日志
        saveVinRecord(order, vehicle, "BIND", "VIN码绑定确认");

        log.info("VIN码绑定成功, orderId={}, vinCode={}", orderId, vinCode);
    }

    /**
     * VIN码变更处理
     */
    private void handleVinChange(OrderEntity order, String newVinCode, VehicleInventoryEntity newVehicle) {
        // 1. 检查原VIN码状态
        if (VinStatusEnum.BOUND.getCode().equals(order.getVinStatus())) {
            throw new BusinessException(21009, "VIN码已绑定，如需变更请提交变更申请");
        }

        // 2. 释放原VIN码
        if (StringUtils.isNotBlank(order.getVinCode())) {
            VehicleInventoryEntity oldVehicle = inventoryRepository.findByVinCode(order.getVinCode());
            if (oldVehicle != null) {
                oldVehicle.setStatus(VinStatusEnum.AVAILABLE.getCode());
                oldVehicle.setPreoccupyOrderId(null);
                oldVehicle.setPreoccupyExpireDate(null);
                inventoryRepository.updateById(oldVehicle);
            }
        }

        // 3. 占用新VIN码
        newVehicle.setStatus(VinStatusEnum.BOUND.getCode());
        newVehicle.setPreoccupyOrderId(order.getId());
        inventoryRepository.updateById(newVehicle);

        // 4. 更新订单
        order.setVinCode(newVinCode);
        order.setVinStatus(VinStatusEnum.BOUND.getCode());
        order.setOrderStatus(OrderStatusEnum.PENDING_DELIVERY.getCode());
        orderRepository.updateById(order);
    }

    /**
     * VIN码校验
     */
    public boolean validateVin(String vinCode) {
        if (StringUtils.isBlank(vinCode) || vinCode.length() != 17) {
            return false;
        }

        // VIN码校验算法
        // ...

        return true;
    }
}
```

#### 2.3.3 价格管理器

```java
/**
 * 价格管理器
 */
@Component
@Slf4j
@RequiredArgsConstructor
public class PriceManager {

    private final PriceListRepository priceListRepository;
    private final PriceItemRepository priceItemRepository;
    private final ModelOptionRepository modelOptionRepository;
    private final PromotionRepository promotionRepository;

    /**
     * 计算订单价格
     */
    public BigDecimal calculateOrderPrice(Long modelId, List<OrderOption> options) {
        // 1. 获取车型基础价格
        BigDecimal basePrice = getBasePrice(modelId);

        // 2. 计算配置加价
        BigDecimal optionPrice = BigDecimal.ZERO;
        if (!CollectionUtils.isEmpty(options)) {
            for (OrderOption option : options) {
                ModelOptionEntity optionEntity = modelOptionRepository.findByCode(option.getOptionCode());
                if (optionEntity != null) {
                    optionPrice = optionPrice.add(optionEntity.getOptionPrice());
                }
            }
        }

        return basePrice.add(optionPrice);
    }

    /**
     * 获取客户价格
     */
    public PriceResult getCustomerPrice(Long customerId, Long modelId) {
        PriceResult result = new PriceResult();

        // 1. 查询客户专属价格
        PriceListEntity customerPrice = priceListRepository.findCustomerPrice(customerId, modelId);
        if (customerPrice != null) {
            result.setPriceType("CUSTOMER");
            result.setPrice(customerPrice.getListPrice());
            return result;
        }

        // 2. 查询促销价格
        PriceListEntity promotionPrice = priceListRepository.findPromotionPrice(modelId);
        if (promotionPrice != null) {
            result.setPriceType("PROMOTION");
            result.setPrice(promotionPrice.getListPrice());
            return result;
        }

        // 3. 查询标准价格
        PriceListEntity standardPrice = priceListRepository.findStandardPrice(modelId);
        if (standardPrice != null) {
            result.setPriceType("STANDARD");
            result.setPrice(standardPrice.getListPrice());
            return result;
        }

        throw new BusinessException("未找到有效价格");
    }

    /**
     * 校验折扣权限
     */
    public DiscountValidationResult validateDiscount(Long userId, BigDecimal discountRate) {
        // 获取用户折扣权限
        BigDecimal maxDiscount = getUserMaxDiscount(userId);

        if (discountRate.compareTo(maxDiscount) > 0) {
            return DiscountValidationResult.builder()
                .valid(false)
                .needApproval(true)
                .maxAllowedDiscount(maxDiscount)
                .message("折扣超出权限，需要审批")
                .build();
        }

        return DiscountValidationResult.builder()
            .valid(true)
            .needApproval(false)
            .build();
    }
}
```

#### 2.3.4 PDI检查管理器

```java
/**
 * PDI检查管理器
 */
@Component
@Slf4j
@RequiredArgsConstructor
public class PdiManager {

    private final PdiCheckRepository pdiCheckRepository;
    private final PdiItemRepository pdiItemRepository;
    private final VehicleInventoryRepository inventoryRepository;

    /**
     * 获取PDI检查项目
     */
    public List<PdiCategoryVo> getPdiCheckItems() {
        // 查询所有PDI检查项目，按类别分组
        List<PdiItemEntity> items = pdiItemRepository.findAllActive();

        return items.stream()
            .collect(Collectors.groupingBy(PdiItemEntity::getCategory))
            .entrySet().stream()
            .map(entry -> PdiCategoryVo.builder()
                .category(entry.getKey())
                .items(entry.getValue().stream()
                    .map(this::convertToItemVo)
                    .collect(Collectors.toList()))
                .build())
            .collect(Collectors.toList());
    }

    /**
     * 提交PDI检查结果
     */
    @Transactional(rollbackFor = Exception.class)
    public PdiCheckResult submitPdiCheck(PdiCheckRequest request) {
        // 1. 创建PDI检查记录
        PdiCheckEntity pdiCheck = new PdiCheckEntity();
        pdiCheck.setTenantId(TenantContext.getTenantId());
        pdiCheck.setVinCode(request.getVinCode());
        pdiCheck.setDeliveryPlanId(request.getDeliveryPlanId());
        pdiCheck.setCheckTime(LocalDateTime.now());
        pdiCheck.setCheckBy(UserContext.getCurrentUserName());
        pdiCheck.setCreatedTime(LocalDateTime.now());

        // 2. 处理检查项结果
        List<PdiCheckItemEntity> checkItems = new ArrayList<>();
        boolean allPassed = true;
        List<PdiFailedItemVo> failedItems = new ArrayList<>();

        for (PdiCheckItemRequest itemRequest : request.getCheckResults()) {
            PdiCheckItemEntity checkItem = new PdiCheckItemEntity();
            checkItem.setItemCode(itemRequest.getItemCode());
            checkItem.setItemName(itemRequest.getItemName());
            checkItem.setResult(itemRequest.getResult());
            checkItem.setRemark(itemRequest.getRemark());
            checkItem.setPhotos(JsonUtils.toJson(itemRequest.getPhotos()));
            checkItems.add(checkItem);

            if (itemRequest.getResult() != 1) { // 不合格
                allPassed = false;
                failedItems.add(PdiFailedItemVo.builder()
                    .itemCode(itemRequest.getItemCode())
                    .itemName(itemRequest.getItemName())
                    .remark(itemRequest.getRemark())
                    .build());
            }
        }

        // 3. 设置PDI状态
        pdiCheck.setPdiStatus(allPassed ? 1 : 2); // 1-通过, 2-不合格
        pdiCheckRepository.save(pdiCheck);

        // 4. 保存检查项明细
        for (PdiCheckItemEntity item : checkItems) {
            item.setPdiCheckId(pdiCheck.getId());
        }
        pdiCheckRepository.saveItems(checkItems);

        // 5. 更新车辆状态
        VehicleInventoryEntity vehicle = inventoryRepository.findByVinCode(request.getVinCode());
        if (vehicle != null) {
            if (allPassed) {
                vehicle.setPdiStatus(1);
                vehicle.setStatus(VinStatusEnum.READY_FOR_DELIVERY.getCode());
            } else {
                vehicle.setPdiStatus(2);
                vehicle.setStatus(VinStatusEnum.PENDING_REPAIR.getCode());
            }
            inventoryRepository.updateById(vehicle);
        }

        log.info("PDI检查完成, vinCode={}, result={}", request.getVinCode(),
            allPassed ? "通过" : "不合格");

        return PdiCheckResult.builder()
            .pdiId(pdiCheck.getId())
            .pdiStatus(pdiCheck.getPdiStatus())
            .pdiStatusName(allPassed ? "通过" : "不合格")
            .failedItems(failedItems)
            .build();
    }
}
```

---

### 2.4 数据访问层设计

#### 2.4.1 客户Repository

```java
/**
 * 客户数据访问接口
 */
public interface CustomerRepository extends BaseMapper<CustomerEntity> {

    /**
     * 根据手机号查询客户
     */
    @Select("SELECT * FROM sd_customer WHERE mobile = #{mobile} AND tenant_id = #{tenantId} AND deleted = 0")
    CustomerEntity findByMobile(@Param("mobile") String mobile, @Param("tenantId") Long tenantId);

    /**
     * 根据编码查询客户
     */
    @Select("SELECT * FROM sd_customer WHERE customer_code = #{customerCode} AND tenant_id = #{tenantId} AND deleted = 0")
    CustomerEntity findByCode(@Param("customerCode") String customerCode, @Param("tenantId") Long tenantId);

    /**
     * 分页查询客户
     */
    IPage<CustomerEntity> queryPage(IPage<CustomerEntity> page,
        @Param("customerName") String customerName,
        @Param("customerType") Integer customerType,
        @Param("customerLevel") Integer customerLevel,
        @Param("status") Integer status);

    /**
     * 更新信用额度
     */
    @Update("UPDATE sd_customer SET credit_limit = #{creditLimit}, credit_used = #{creditUsed}, " +
            "updated_time = NOW() WHERE id = #{id}")
    int updateCredit(@Param("id") Long id,
        @Param("creditLimit") BigDecimal creditLimit,
        @Param("creditUsed") BigDecimal creditUsed);
}
```

#### 2.4.2 订单Repository

```java
/**
 * 订单数据访问接口
 */
public interface OrderRepository extends BaseMapper<OrderEntity> {

    /**
     * 根据订单号查询
     */
    @Select("SELECT * FROM sd_order WHERE order_no = #{orderNo} AND tenant_id = #{tenantId} AND deleted = 0")
    OrderEntity findByOrderNo(@Param("orderNo") String orderNo, @Param("tenantId") Long tenantId);

    /**
     * 分页查询订单
     */
    IPage<OrderEntity> queryPage(IPage<OrderEntity> page,
        @Param("orderNo") String orderNo,
        @Param("customerId") Long customerId,
        @Param("orderStatus") Integer orderStatus,
        @Param("orderType") Integer orderType,
        @Param("startDate") LocalDate startDate,
        @Param("endDate") LocalDate endDate,
        @Param("salesRepId") Long salesRepId);

    /**
     * 统计订单状态分布
     */
    @Select("SELECT order_status, COUNT(*) as count FROM sd_order " +
            "WHERE tenant_id = #{tenantId} AND deleted = 0 " +
            "GROUP BY order_status")
    List<Map<String, Object>> countByStatus(@Param("tenantId") Long tenantId);

    /**
     * 统计日期范围内的订单
     */
    @Select("SELECT COUNT(*) as count, SUM(final_amount) as amount FROM sd_order " +
            "WHERE tenant_id = #{tenantId} AND order_date BETWEEN #{startDate} AND #{endDate} " +
            "AND order_status NOT IN (80, 90) AND deleted = 0")
    Map<String, Object> countByDateRange(@Param("tenantId") Long tenantId,
        @Param("startDate") LocalDate startDate,
        @Param("endDate") LocalDate endDate);

    /**
     * 更新订单状态
     */
    @Update("UPDATE sd_order SET order_status = #{status}, updated_time = NOW(), " +
            "updated_by = #{updatedBy} WHERE id = #{id}")
    int updateStatus(@Param("id") Long id,
        @Param("status") Integer status,
        @Param("updatedBy") String updatedBy);
}
```

---

## 3. 时序图描述

### 3.1 创建销售订单时序图

```
用户                Controller              Service               Manager              Repository
 |                      |                      |                     |                     |
 |-- 创建订单请求 ----->|                      |                     |                     |
 |                      |-- 创建订单 -------->|                     |                     |
 |                      |                      |-- 查询客户 -------->|                     |
 |                      |                      |                     |--> 查询客户 -------->|
 |                      |                      |                     |<-- 客户信息 ---------|
 |                      |                      |<-- 客户信息 --------|                     |
 |                      |                      |                     |                     |
 |                      |                      |-- 计算价格 -------->|                     |
 |                      |                      |                     |--> 查询价格 -------->|
 |                      |                      |                     |<-- 价格信息 ---------|
 |                      |                      |<-- 订单总价 --------|                     |
 |                      |                      |                     |                     |
 |                      |                      |-- 校验信用额度 ---->|                     |
 |                      |                      |                     |--> 查询信用额度 ---->|
 |                      |                      |                     |<-- 额度信息 ---------|
 |                      |                      |<-- 校验结果 --------|                     |
 |                      |                      |                     |                     |
 |                      |                      |-- 保存订单 -------->|                     |
 |                      |                      |                     |--> 插入订单 -------->|
 |                      |                      |                     |<-- 订单ID ----------|
 |                      |                      |<-- 保存成功 --------|                     |
 |                      |                      |                     |                     |
 |                      |<-- 返回订单号 -------|                     |                     |
 |<-- 返回结果 ---------|                      |                     |                     |
```

### 3.2 订单审批流程时序图

```
用户              Controller          OrderService       WorkflowService      ApprovalService
 |                    |                     |                   |                   |
 |-- 提交订单 ------->|                     |                   |                   |
 |                    |-- 提交订单 -------->|                   |                   |
 |                    |                     |-- 检查是否需审批 ->|                   |
 |                    |                     |                   |-- 查询审批规则 --->|
 |                    |                     |                   |<-- 规则信息 -------|
 |                    |                     |<-- 审批结果 ------|                   |
 |                    |                     |                   |                   |
 |                    |                     | [需要审批]         |                   |
 |                    |                     |-- 创建审批流程 --->|                   |
 |                    |                     |                   |-- 创建审批任务 --->|
 |                    |                     |                   |<-- 任务ID ---------|
 |                    |                     |<-- 审批ID --------|                   |
 |                    |                     |                   |                   |
 |                    |                     |-- 更新订单状态 --->|                   |
 |                    |<-- 返回审批ID ------|                   |                   |
 |<-- 等待审批 -------|                     |                   |                   |
 |                    |                     |                   |                   |
 |---------------- 审批人审批 --------------|                   |                   |
 |                    |                     |                   |                   |
 |-- 审批通过 ------->|                     |                   |                   |
 |                    |-- 审批订单 -------->|                   |                   |
 |                    |                     |-- 完成审批 ------->|                   |
 |                    |                     |                   |-- 更新审批状态 --->|
 |                    |                     |                   |<-- 更新结果 -------|
 |                    |                     |<-- 审批完成 ------|                   |
 |                    |                     |                   |                   |
 |                    |                     |-- 更新订单状态 --->|                   |
 |                    |                     |-- 发布事件 ------->|                   |
 |                    |<-- 返回结果 -------|                   |                   |
 |<-- 审批完成 -------|                     |                   |                   |
```

### 3.3 VIN码分配时序图

```
用户            Controller         OrderService          VinManager          InventoryRepo
 |                  |                    |                   |                   |
 |-- 分配VIN ------->|                    |                   |                   |
 |                  |-- 分配VIN -------->|                   |                   |
 |                  |                    |-- 查询订单 ------->|                   |
 |                  |                    |                   |                   |
 |                  |                    |-- 分配VIN -------->|                   |
 |                  |                    |                   |-- 查询可用车辆 --->|
 |                  |                    |                   |<-- 车辆列表 -------|
 |                  |                    |                   |                   |
 |                  |                    |                   |-- 更新车辆状态 --->|
 |                  |                    |                   |<-- 更新结果 -------|
 |                  |                    |                   |                   |
 |                  |                    |<-- VIN信息 --------|                   |
 |                  |                    |                   |                   |
 |                  |                    |-- 更新订单 --------|                   |
 |                  |<-- 返回VIN --------|                   |                   |
 |<-- VIN分配成功 --|                    |                   |                   |
```

### 3.4 交付确认时序图

```
用户           Controller        DeliveryService        PdiManager        OrderService
 |                 |                    |                  |                  |
 |-- 交付确认 ---->|                    |                  |                  |
 |                 |-- 确认交付 ------->|                  |                  |
 |                 |                    |-- 校验PDI状态 -->|                  |
 |                 |                    |<-- PDI通过 ------|                  |
 |                 |                    |                  |                  |
 |                 |                    |-- 更新交付状态 -->|                  |
 |                 |                    |                  |                  |
 |                 |                    |-- 更新订单状态 ------------------>|
 |                 |                    |                  |                  |
 |                 |                    |-- 触发后续流程 -->|                  |
 |                 |                    |  [发票开具]       |                  |
 |                 |                    |  [售后建档]       |                  |
 |                 |<-- 返回结果 -------|                  |                  |
 |<-- 交付完成 ----|                    |                  |                  |
```

---

## 4. 关键业务逻辑说明

### 4.1 订单状态流转

```
         ┌─────────────────────────────────────────────────────────────┐
         │                                                              │
         ▼                                                              │
    ┌─────────┐    提交     ┌─────────┐    审批通过   ┌─────────┐       │
    │  草稿   │ ─────────> │ 待确认  │ ───────────> │ 已确认  │       │
    │   10   │            │   20    │              │   30    │       │
    └─────────┘            └─────────┘              └────┬────┘       │
         │                      │                       │             │
         │                      │ 审批不通过            │             │
         │                      ▼                       │             │
         │                 ┌─────────┐                  │             │
         │                 │ 已驳回  │                  │             │
         │                 │   25   │                  │             │
         │                 └─────────┘                  │             │
         │                                              │             │
         │ 取消                                         │             │
         ▼                                              ▼             │
    ┌─────────┐                                 ┌─────────┐          │
    │ 已取消  │ <───────────────────────────    │ 生产中  │          │
    │   80   │                                 │   40    │          │
    └─────────┘                                 └────┬────┘          │
                                                     │               │
                                                     │ 生产完成       │
                                                     ▼               │
                                                ┌─────────┐          │
                                                │ 待交付  │          │
                                                │   50    │          │
                                                └────┬────┘          │
                                                     │               │
                                                     │ 出库          │
                                                     ▼               │
                                                ┌─────────┐          │
                                                │ 交付中  │          │
                                                │   60    │          │
                                                └────┬────┘          │
                                                     │               │
                                                     │ 签收确认       │
                                                     ▼               │
                                                ┌─────────┐          │
                                                │ 已完成  │          │
                                                │   70    │──────────┘
                                                └─────────┘    异常处理
                                                     │
                                                     │ 退款完成
                                                     ▼
                                                ┌─────────┐
                                                │ 已关闭  │
                                                │   90    │
                                                └─────────┘
```

### 4.2 VIN码生命周期管理

```
                    ┌──────────────────────────────────────────┐
                    │              VIN码生命周期               │
                    └──────────────────────────────────────────┘
                                        │
                                        ▼
                    ┌──────────────────────────────────────────┐
                    │  1. VIN码生成 (生产计划确定)             │
                    │     状态: 待入库                         │
                    │     来源: MES系统                        │
                    └──────────────────────────────────────────┘
                                        │
                                        ▼
                    ┌──────────────────────────────────────────┐
                    │  2. 车辆入库                             │
                    │     状态: 在库可用                       │
                    │     仓库: WMS系统                        │
                    └──────────────────────────────────────────┘
                                        │
                        ┌───────────────┼───────────────┐
                        │               │               │
                        ▼               ▼               ▼
              ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
              │ 3A. 预分配   │   │ 3B. 直接销售 │   │ 3C. 库存销售 │
              │ 状态: 预占   │   │ 状态: 绑定   │   │ 状态: 可用   │
              │ 场景: 订单确认│   │ 场景: 现车销售│   │ 场景: 经销商 │
              └─────────────┘   └─────────────┘   └─────────────┘
                        │               │
                        ▼               │
              ┌─────────────┐           │
              │ 4. 正式绑定  │ <─────────┘
              │ 状态: 已绑定 │
              │ 场景: 车辆下线│
              └─────────────┘
                        │
                        ▼
              ┌─────────────┐
              │ 5. 出库     │
              │ 状态: 已出库 │
              └─────────────┘
                        │
                        ▼
              ┌─────────────┐
              │ 6. 交付确认  │
              │ 状态: 已交付 │
              │ 关联: 客户信息│
              └─────────────┘
                        │
                        ▼
              ┌─────────────┐
              │ 7. 售后追溯  │
              │ 用于: 维修记录│
              │ 用于: 召回管理│
              └─────────────┘
```

### 4.3 信用额度管理逻辑

```java
/**
 * 信用额度管理规则
 *
 * 1. 信用额度设置
 *    - 新客户默认信用额度为0
 *    - 额度 <= 50万: 销售主管审批
 *    - 额度 <= 200万: 销售经理审批
 *    - 额度 > 200万: 财务总监审批
 *
 * 2. 信用额度占用
 *    - 订单提交时自动占用
 *    - 占用金额 = 订单最终金额
 *    - 已用额度 + 占用金额 <= 信用额度
 *
 * 3. 信用额度释放
 *    - 订单取消: 全额释放
 *    - 订单完成: 转为应收账款
 *    - 收款确认: 释放信用额度
 *
 * 4. 信用额度预警
 *    - 额度使用率 >= 80%: 黄色预警
 *    - 额度使用率 >= 95%: 红色预警
 *    - 额度超限: 阻止新订单
 */
```

### 4.4 PDI检查规则

```java
/**
 * PDI检查业务规则
 *
 * 1. 检查时机
 *    - 车辆出库前必须完成PDI检查
 *    - PDI检查结果有效期为7天
 *    - 超过有效期需重新检查
 *
 * 2. 检查项目
 *    - 外观检查: 车漆、玻璃、轮胎、轮毂
 *    - 内饰检查: 座椅、仪表盘、电子设备
 *    - 发动机舱: 发动机、变速箱、油液
 *    - 底盘检查: 悬挂、制动、排气管
 *    - 电气系统: 灯光、音响、空调
 *    - 随车物品: 备胎、工具、证件
 *
 * 3. 结果判定
 *    - 全部合格: PDI通过，可出库
 *    - 存在不合格: PDI不通过，需返修
 *    - 返修后重新PDI
 *
 * 4. 问题处理
 *    - 轻微问题: 现场处理，记录备案
 *    - 一般问题: 返修处理后重新PDI
 *    - 严重问题: 上报质量部门，安排换车
 */
```

### 4.5 价格计算规则

```java
/**
 * 价格计算规则
 *
 * 1. 价格优先级
 *    客户专属价格 > 促销价格 > 经销商价格 > 标准价格
 *
 * 2. 配置价格计算
 *    订单总价 = 车型基础价 + Σ(配置项价格)
 *
 * 3. 折扣规则
 *    - 折扣率 = (标准价 - 实际价) / 标准价 * 100%
 *    - 折扣权限:
 *      销售代表: 最大2%
 *      销售主管: 最大5%
 *      销售经理: 最大8%
 *      销售总监: 最大12%
 *    - 超出权限需审批
 *
 * 4. 促销应用
 *    - 自动应用有效促销
 *    - 促销可与折扣叠加
 *    - 促销不可与其他促销叠加
 *
 * 5. 最终价格
 *    最终价格 = 订单总价 - 折扣金额 - 促销优惠
 */
```

---

## 5. 扩展设计

### 5.1 事件驱动设计

```java
/**
 * 订单事件定义
 */
public class OrderEvents {

    /** 订单创建事件 */
    @Data
    @Builder
    public static class OrderCreatedEvent {
        private Long orderId;
        private String orderNo;
        private Long customerId;
        private BigDecimal amount;
        private LocalDateTime eventTime;
    }

    /** 订单审批通过事件 */
    @Data
    @Builder
    public static class OrderApprovedEvent {
        private Long orderId;
        private String orderNo;
        private Integer orderStatus;
        private String approvedBy;
        private LocalDateTime eventTime;
    }

    /** 订单状态变更事件 */
    @Data
    @Builder
    public static class OrderStatusChangedEvent {
        private Long orderId;
        private String orderNo;
        private Integer oldStatus;
        private Integer newStatus;
        private LocalDateTime eventTime;
    }

    /** 交付完成事件 */
    @Data
    @Builder
    public static class DeliveryCompletedEvent {
        private Long orderId;
        private String orderNo;
        private String vinCode;
        private LocalDateTime deliveryTime;
        private LocalDateTime eventTime;
    }
}

/**
 * 事件监听器
 */
@Component
@Slf4j
@RequiredArgsConstructor
public class OrderEventListener {

    private final InvoiceService invoiceService;
    private final AfterSaleService afterSaleService;
    private final NotificationService notificationService;

    @EventListener
    @Async
    public void onOrderCreated(OrderCreatedEvent event) {
        log.info("订单创建事件, orderNo={}", event.getOrderNo());

        // 发送通知
        notificationService.sendOrderNotification(event.getOrderId());
    }

    @EventListener
    @Async
    public void onDeliveryCompleted(DeliveryCompletedEvent event) {
        log.info("交付完成事件, orderNo={}", event.getOrderNo());

        // 触发开票
        invoiceService.createInvoice(event.getOrderId());

        // 建立售后档案
        afterSaleService.createVehicleRecord(event.getVinCode());

        // 发送满意度调查
        notificationService.sendSatisfactionSurvey(event.getOrderId());
    }
}
```

### 5.2 消息队列设计

```java
/**
 * 消息生产者
 */
@Component
@Slf4j
@RequiredArgsConstructor
public class OrderMessageProducer {

    private final RabbitTemplate rabbitTemplate;

    /**
     * 发送订单消息到生产系统
     */
    public void sendOrderToProduction(OrderEntity order) {
        OrderMessage message = OrderMessage.builder()
            .orderId(order.getId())
            .orderNo(order.getOrderNo())
            .modelId(order.getModelId())
            .modelCode(order.getModelCode())
            .configCode(order.getConfigCode())
            .quantity(order.getOrderQty())
            .requiredDate(order.getRequiredDate())
            .build();

        rabbitTemplate.convertAndSend(
            "erp.exchange",
            "erp.order.production",
            message
        );

        log.info("发送订单到生产系统, orderNo={}", order.getOrderNo());
    }
}

/**
 * 消息消费者
 */
@Component
@Slf4j
@RequiredArgsConstructor
public class ProductionMessageConsumer {

    private final OrderService orderService;

    @RabbitListener(queues = "erp.production.order")
    public void handleProductionComplete(ProductionCompleteMessage message) {
        log.info("收到生产完成消息, orderNo={}", message.getOrderNo());

        // 更新订单状态
        orderService.updateOrderStatus(
            message.getOrderId(),
            OrderStatusEnum.PENDING_DELIVERY.getCode(),
            "车辆生产完成，VIN:" + message.getVinCode()
        );
    }
}
```

---

## 6. 性能优化设计

### 6.1 缓存设计

```java
/**
 * 缓存配置
 */
@Configuration
@EnableCaching
public class CacheConfig {

    @Bean
    public CacheManager cacheManager(RedisConnectionFactory factory) {
        RedisCacheConfiguration config = RedisCacheConfiguration.defaultCacheConfig()
            .entryTtl(Duration.ofMinutes(30))
            .serializeKeysWith(RedisSerializationContext.SerializationPair
                .fromSerializer(new StringRedisSerializer()))
            .serializeValuesWith(RedisSerializationContext.SerializationPair
                .fromSerializer(new GenericJackson2JsonRedisSerializer()));

        return RedisCacheManager.builder(factory)
            .cacheDefaults(config)
            .build();
    }
}

/**
 * 缓存使用示例
 */
@Service
public class PriceCacheService {

    @Cacheable(value = "price", key = "#modelId + ':' + #customerType")
    public BigDecimal getCustomerPrice(Long modelId, Integer customerType) {
        // 查询数据库
        return priceRepository.findPrice(modelId, customerType);
    }

    @CacheEvict(value = "price", key = "#modelId + ':' + #customerType")
    public void evictPriceCache(Long modelId, Integer customerType) {
        // 清除缓存
    }
}
```

### 6.2 批量处理优化

```java
/**
 * 批量处理配置
 */
@Configuration
public class BatchConfig {

    @Bean
    public Step orderImportStep(ItemReader<OrderImportDto> reader,
                                ItemProcessor<OrderImportDto, OrderEntity> processor,
                                ItemWriter<OrderEntity> writer) {
        return stepBuilderFactory.get("orderImportStep")
            .<OrderImportDto, OrderEntity>chunk(100)
            .reader(reader)
            .processor(processor)
            .writer(writer)
            .build();
    }
}
```

---

## 7. 安全设计

### 7.1 数据权限控制

```java
/**
 * 数据权限拦截器
 */
@Component
public class DataPermissionInterceptor implements Interceptor {

    @Override
    public Object intercept(Invocation invocation) throws Throwable {
        // 获取当前用户的数据权限范围
        Long userId = UserContext.getCurrentUserId();
        DataPermission permission = dataPermissionService.getUserPermission(userId);

        // 根据权限范围过滤数据
        // ...

        return invocation.proceed();
    }
}
```

### 7.2 敏感数据加密

```java
/**
 * 敏感数据处理
 */
@Component
public class SensitiveDataHandler {

    private static final String AES_KEY = "xxx";

    /**
     * 加密
     */
    public String encrypt(String plainText) {
        if (StringUtils.isBlank(plainText)) {
            return plainText;
        }
        return AESUtils.encrypt(plainText, AES_KEY);
    }

    /**
     * 解密
     */
    public String decrypt(String cipherText) {
        if (StringUtils.isBlank(cipherText)) {
            return cipherText;
        }
        return AESUtils.decrypt(cipherText, AES_KEY);
    }

    /**
     * 脱敏显示
     */
    public String mask(String data, SensitiveType type) {
        if (StringUtils.isBlank(data)) {
            return data;
        }
        switch (type) {
            case MOBILE:
                return data.replaceAll("(\\d{3})\\d{4}(\\d{4})", "$1****$2");
            case ID_CARD:
                return data.replaceAll("(\\d{4})\\d{10}(\\d{4})", "$1**********$2");
            default:
                return data;
        }
    }
}
```

---

**文档修订历史**

| 版本 | 修订日期 | 修订人 | 修订内容 |
|------|----------|--------|----------|
| V1.0 | 2026-03-24 | 系统生成 | 初始版本 |