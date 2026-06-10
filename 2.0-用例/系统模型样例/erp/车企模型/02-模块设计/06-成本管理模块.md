# Detail-06 成本管理模块详细设计 (CO)

## 文档信息

| 项目 | 内容 |
|------|------|
| 文档编号 | Detail-06 |
| 模块名称 | 成本管理 (Controlling) |
| 版本号 | V1.0 |
| 编制日期 | 2026-03-24 |
| 编制人 | 研发架构团队 |
| 技术栈 | Spring Boot 2.7 + MyBatis Plus + MySQL 8.x |
| 状态 | 待评审 |

---

## 1. 设计概述

### 1.1 系统架构

```
┌─────────────────────────────────────────────────────────────────┐
│                         前端展示层                                │
│                    (Vue.js + Element UI)                        │
├─────────────────────────────────────────────────────────────────┤
│                         API网关层                                 │
│                    (Spring Cloud Gateway)                       │
├─────────────────────────────────────────────────────────────────┤
│                        业务服务层                                 │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌───────────┐ │
│  │ 成本核算服务 │ │ 标准成本服务 │ │ 成本分析服务 │ │利润分析服务│ │
│  └─────────────┘ └─────────────┘ └─────────────┘ └───────────┘ │
├─────────────────────────────────────────────────────────────────┤
│                        数据访问层                                 │
│                    (MyBatis Plus Mapper)                        │
├─────────────────────────────────────────────────────────────────┤
│                        数据存储层                                 │
│                         (MySQL 8.x)                             │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 模块依赖

```
成本管理模块(CO)
├── 依赖模块
│   ├── 系统管理模块(SM): 用户、组织、权限
│   ├── 财务管理模块(FI): 会计科目、凭证
│   ├── 生产管理模块(PM): 工单、工时、产量
│   ├── 物料管理模块(MM): 物料、BOM、库存
│   └── 采购管理模块(PO): 采购价格
└── 被依赖模块
    └── 经营分析模块(BI): 成本分析数据
```

### 1.3 设计原则

- **领域驱动设计(DDD)**: 按业务领域划分服务边界
- **高内聚低耦合**: 模块内部高内聚，模块间低耦合
- **可扩展性**: 支持新的成本核算方法和分析维度
- **高性能**: 成本核算批量处理优化
- **可配置性**: 成本分配规则、核算规则可配置

---

## 2. 核心类设计

### 2.1 包结构设计

```
com.autoerp.co
├── controller                 # 控制器层
│   ├── CostElementController.java
│   ├── CostCenterController.java
│   ├── CostCollectionController.java
│   ├── CostAllocationController.java
│   ├── StandardCostController.java
│   ├── CostCalculationController.java
│   ├── CostAnalysisController.java
│   └── ProfitAnalysisController.java
├── service                    # 服务层
│   ├── CostElementService.java
│   ├── CostCenterService.java
│   ├── CostCollectionService.java
│   ├── CostAllocationService.java
│   ├── StandardCostService.java
│   ├── CostCalculationService.java
│   ├── CostAnalysisService.java
│   ├── ProfitAnalysisService.java
│   └── impl                   # 服务实现
│       ├── CostElementServiceImpl.java
│       ├── CostCenterServiceImpl.java
│       ├── CostCollectionServiceImpl.java
│       ├── CostAllocationServiceImpl.java
│       ├── StandardCostServiceImpl.java
│       ├── CostCalculationServiceImpl.java
│       ├── CostAnalysisServiceImpl.java
│       └── ProfitAnalysisServiceImpl.java
├── mapper                     # 数据访问层
│   ├── CostElementMapper.java
│   ├── CostCenterMapper.java
│   ├── CostCollectionMapper.java
│   ├── CostAllocationMapper.java
│   ├── StandardCostMapper.java
│   ├── CostCalculationMapper.java
│   └── CostVarianceMapper.java
├── entity                     # 实体类
│   ├── CostElement.java
│   ├── CostCenter.java
│   ├── CostCollection.java
│   ├── CostCollectionDetail.java
│   ├── CostAllocationRule.java
│   ├── StandardCost.java
│   ├── StandardCostDetail.java
│   ├── CostCalculation.java
│   └── CostCalculationDetail.java
├── dto                        # 数据传输对象
│   ├── request
│   │   ├── CostElementQueryRequest.java
│   │   ├── CostElementCreateRequest.java
│   │   ├── CostCenterQueryRequest.java
│   │   ├── StandardCostCreateRequest.java
│   │   ├── CostCalculationExecuteRequest.java
│   │   └── ...
│   └── response
│       ├── CostElementResponse.java
│       ├── CostCenterResponse.java
│       ├── CostStructureAnalysisResponse.java
│       └── ...
├── vo                         # 视图对象
│   ├── CostElementTreeVO.java
│   ├── CostCenterTreeVO.java
│   ├── CostSummaryVO.java
│   └── ...
├── enums                      # 枚举类
│   ├── CostElementCategoryEnum.java
│   ├── CostCenterTypeEnum.java
│   ├── CalculationStatusEnum.java
│   ├── VarianceTypeEnum.java
│   └── ...
├── constants                  # 常量类
│   ├── CostConstants.java
│   └── CostMessageConstants.java
├── converter                  # 转换器
│   ├── CostElementConverter.java
│   ├── CostCenterConverter.java
│   └── ...
├── calculator                 # 成本计算器
│   ├── MaterialCostCalculator.java
│   ├── LaborCostCalculator.java
│   ├── OverheadCostCalculator.java
│   ├── WipCostCalculator.java
│   ├── StandardCostCalculator.java
│   └── VarianceCalculator.java
├── allocator                  # 成本分配器
│   ├── CostAllocator.java
│   ├── AuxiliaryCostAllocator.java
│   └── OverheadCostAllocator.java
├── analyzer                   # 成本分析器
│   ├── CostStructureAnalyzer.java
│   ├── CostTrendAnalyzer.java
│   ├── CostBehaviorAnalyzer.java
│   └── ProfitAnalyzer.java
├── integration                # 系统集成
│   ├── FiIntegrationService.java
│   ├── PmIntegrationService.java
│   ├── MmIntegrationService.java
│   └── HrIntegrationService.java
├── event                      # 事件处理
│   ├── CostCalculationCompletedEvent.java
│   └── CostCalculationEventListener.java
├── job                        # 定时任务
│   ├── CostCollectionJob.java
│   └── CostAnalysisReportJob.java
└── util                       # 工具类
    ├── CostCalculatorUtil.java
    └── CostDateUtil.java
```

---

## 3. 核心实体设计

### 3.1 成本要素实体

```java
/**
 * 成本要素实体
 */
@Data
@TableName("co_cost_element")
public class CostElement extends BaseEntity {

    /** 成本要素编码 */
    private String elementCode;

    /** 成本要素名称 */
    private String elementName;

    /** 成本要素类别 */
    private String elementCategory;

    /** 要素类型(01-直接成本,02-间接成本) */
    private String elementType;

    /** 成本性态(01-变动成本,02-固定成本,03-混合成本) */
    private String costBehavior;

    /** 是否可控(0-不可控,1-可控) */
    private Integer controllable;

    /** 关联会计科目ID */
    private Long glAccountId;

    /** 会计科目编码 */
    private String glAccountCode;

    /** 父级要素ID */
    private Long parentId;

    /** 层级号 */
    private Integer levelNo;

    /** 是否叶子节点 */
    private Integer isLeaf;

    /** 排序号 */
    private Integer sortNo;

    /** 状态(0-停用,1-启用) */
    private Integer status;

    /** 备注 */
    private String remark;

    @TableField(exist = false)
    private List<CostElement> children;
}
```

### 3.2 成本中心实体

```java
/**
 * 成本中心实体
 */
@Data
@TableName("co_cost_center")
public class CostCenter extends BaseEntity {

    /** 成本中心编码 */
    private String centerCode;

    /** 成本中心名称 */
    private String centerName;

    /** 成本中心类型 */
    private String centerType;

    /** 所属部门ID */
    private Long departmentId;

    /** 部门编码 */
    private String departmentCode;

    /** 部门名称 */
    private String departmentName;

    /** 父级成本中心ID */
    private Long parentId;

    /** 层级号 */
    private Integer levelNo;

    /** 是否叶子节点 */
    private Integer isLeaf;

    /** 负责人ID */
    private Long managerId;

    /** 负责人姓名 */
    private String managerName;

    /** 关联车间ID */
    private Long workshopId;

    /** 车间编码 */
    private String workshopCode;

    /** 关联工作中心ID */
    private Long workcenterId;

    /** 产能 */
    private BigDecimal capacity;

    /** 产能单位 */
    private String capacityUnit;

    /** 排序号 */
    private Integer sortNo;

    /** 状态 */
    private Integer status;

    @TableField(exist = false)
    private List<CostCenter> children;
}
```

### 3.3 标准成本实体

```java
/**
 * 标准成本实体
 */
@Data
@TableName("co_standard_cost")
public class StandardCost extends BaseEntity {

    /** 物料ID */
    private Long materialId;

    /** 物料编码 */
    private String materialCode;

    /** 物料名称 */
    private String materialName;

    /** 版本号 */
    private String versionNo;

    /** 标准单价 */
    private BigDecimal standardPrice;

    /** 标准数量 */
    private BigDecimal standardQty;

    /** 材料成本 */
    private BigDecimal materialCost;

    /** 人工成本 */
    private BigDecimal laborCost;

    /** 制造费用 */
    private BigDecimal overheadCost;

    /** 总成本 */
    private BigDecimal totalCost;

    /** 币种 */
    private String currency;

    /** 生效日期 */
    private LocalDate effectiveDate;

    /** 失效日期 */
    private LocalDate expireDate;

    /** 状态 */
    private String status;

    /** 审核人ID */
    private Long auditBy;

    /** 审核时间 */
    private LocalDateTime auditTime;

    @TableField(exist = false)
    private List<StandardCostDetail> details;
}
```

### 3.4 成本核算实体

```java
/**
 * 成本核算实体
 */
@Data
@TableName("co_cost_calculation")
public class CostCalculation extends BaseEntity {

    /** 核算单号 */
    private String calcNo;

    /** 核算类型 */
    private String calcType;

    /** 会计年度 */
    private Integer periodYear;

    /** 会计期间 */
    private Integer periodMonth;

    /** 材料成本总额 */
    private BigDecimal totalMaterialCost;

    /** 人工成本总额 */
    private BigDecimal totalLaborCost;

    /** 制造费用总额 */
    private BigDecimal totalOverheadCost;

    /** 成本总额 */
    private BigDecimal totalCost;

    /** 在制品成本 */
    private BigDecimal wipCost;

    /** 完工产品成本 */
    private BigDecimal finishCost;

    /** 币种 */
    private String currency;

    /** 状态 */
    private String status;

    /** 核算日期 */
    private LocalDate calcDate;

    /** 开始时间 */
    private LocalDateTime startTime;

    /** 结束时间 */
    private LocalDateTime endTime;

    /** 审核人ID */
    private Long auditBy;

    /** 审核时间 */
    private LocalDateTime auditTime;

    @TableField(exist = false)
    private List<CostCalculationDetail> details;
}
```

---

## 4. 核心服务设计

### 4.1 成本核算服务

```java
/**
 * 成本核算服务接口
 */
public interface CostCalculationService {

    /**
     * 创建成本核算单
     */
    Long createCalculation(CostCalculationCreateRequest request);

    /**
     * 执行成本核算
     */
    CostCalculationResult executeCalculation(Long calcId, CostCalculationExecuteRequest request);

    /**
     * 审核成本核算
     */
    void approveCalculation(Long calcId, ApproveRequest request);

    /**
     * 执行成本结转
     */
    VoucherResult transferCost(Long calcId, CostTransferRequest request);

    /**
     * 计算材料成本
     */
    BigDecimal calculateMaterialCost(Integer periodYear, Integer periodMonth, Long costCenterId);

    /**
     * 计算人工成本
     */
    BigDecimal calculateLaborCost(Integer periodYear, Integer periodMonth, Long costCenterId);

    /**
     * 计算制造费用
     */
    BigDecimal calculateOverheadCost(Integer periodYear, Integer periodMonth, Long costCenterId);

    /**
     * 计算在制品成本
     */
    WipCostResult calculateWipCost(Long calcId);

    /**
     * 计算完工产品成本
     */
    FinishCostResult calculateFinishCost(Long calcId);
}

/**
 * 成本核算服务实现
 */
@Service
@Slf4j
public class CostCalculationServiceImpl implements CostCalculationService {

    @Autowired
    private CostCalculationMapper calculationMapper;

    @Autowired
    private MaterialCostCalculator materialCostCalculator;

    @Autowired
    private LaborCostCalculator laborCostCalculator;

    @Autowired
    private OverheadCostCalculator overheadCostCalculator;

    @Autowired
    private WipCostCalculator wipCostCalculator;

    @Autowired
    private CostAllocator costAllocator;

    @Autowired
    private FiIntegrationService fiIntegrationService;

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long createCalculation(CostCalculationCreateRequest request) {
        // 1. 校验期间是否已核算
        checkPeriodNotCalculated(request.getPeriodYear(), request.getPeriodMonth());

        // 2. 创建核算单
        CostCalculation calculation = new CostCalculation();
        calculation.setCalcNo(generateCalcNo());
        calculation.setCalcType(request.getCalcType());
        calculation.setPeriodYear(request.getPeriodYear());
        calculation.setPeriodMonth(request.getPeriodMonth());
        calculation.setCalcDate(LocalDate.now());
        calculation.setStatus(CalculationStatusEnum.DRAFT.getCode());
        calculation.setTotalMaterialCost(BigDecimal.ZERO);
        calculation.setTotalLaborCost(BigDecimal.ZERO);
        calculation.setTotalOverheadCost(BigDecimal.ZERO);
        calculation.setTotalCost(BigDecimal.ZERO);

        calculationMapper.insert(calculation);

        return calculation.getId();
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public CostCalculationResult executeCalculation(Long calcId, CostCalculationExecuteRequest request) {
        log.info("开始执行成本核算, calcId: {}", calcId);

        CostCalculation calculation = calculationMapper.selectById(calcId);
        if (calculation == null) {
            throw new BusinessException("核算单不存在");
        }

        calculation.setStatus(CalculationStatusEnum.CALCULATING.getCode());
        calculation.setStartTime(LocalDateTime.now());
        calculationMapper.updateById(calculation);

        try {
            // 1. 执行成本归集
            executeCostCollection(calculation);

            // 2. 执行成本分配
            executeCostAllocation(calculation);

            // 3. 计算在制品成本
            WipCostResult wipResult = calculateWipCost(calcId);

            // 4. 计算完工产品成本
            FinishCostResult finishResult = calculateFinishCost(calcId);

            // 5. 计算成本差异
            calculateCostVariance(calculation);

            // 6. 更新核算单状态
            calculation.setStatus(CalculationStatusEnum.PENDING_APPROVAL.getCode());
            calculation.setEndTime(LocalDateTime.now());
            calculation.setTotalMaterialCost(finishResult.getTotalMaterialCost());
            calculation.setTotalLaborCost(finishResult.getTotalLaborCost());
            calculation.setTotalOverheadCost(finishResult.getTotalOverheadCost());
            calculation.setTotalCost(finishResult.getTotalCost());
            calculation.setWipCost(wipResult.getWipCost());
            calculation.setFinishCost(finishResult.getFinishCost());

            calculationMapper.updateById(calculation);

            log.info("成本核算执行完成, calcId: {}", calcId);

            return buildCalculationResult(calculation);

        } catch (Exception e) {
            log.error("成本核算执行失败", e);
            calculation.setStatus(CalculationStatusEnum.DRAFT.getCode());
            calculationMapper.updateById(calculation);
            throw new BusinessException("成本核算执行失败: " + e.getMessage());
        }
    }

    /**
     * 执行成本归集
     */
    private void executeCostCollection(CostCalculation calculation) {
        // 1. 归集材料成本
        List<CostCenter> costCenters = getProductionCostCenters();
        for (CostCenter center : costCenters) {
            BigDecimal materialCost = materialCostCalculator.calculate(
                calculation.getPeriodYear(),
                calculation.getPeriodMonth(),
                center.getId()
            );
            saveCollectionRecord(center.getId(), "01", materialCost, calculation);
        }

        // 2. 归集人工成本
        for (CostCenter center : costCenters) {
            BigDecimal laborCost = laborCostCalculator.calculate(
                calculation.getPeriodYear(),
                calculation.getPeriodMonth(),
                center.getId()
            );
            saveCollectionRecord(center.getId(), "02", laborCost, calculation);
        }

        // 3. 归集制造费用
        for (CostCenter center : costCenters) {
            BigDecimal overheadCost = overheadCostCalculator.calculate(
                calculation.getPeriodYear(),
                calculation.getPeriodMonth(),
                center.getId()
            );
            saveCollectionRecord(center.getId(), "03", overheadCost, calculation);
        }
    }

    /**
     * 执行成本分配
     */
    private void executeCostAllocation(CostCalculation calculation) {
        // 1. 获取分配规则
        List<CostAllocationRule> rules = getActiveAllocationRules();

        // 2. 按分配顺序执行
        rules.stream()
            .sorted(Comparator.comparing(CostAllocationRule::getAllocationOrder))
            .forEach(rule -> costAllocator.allocate(rule, calculation));
    }
}
```

### 4.2 标准成本服务

```java
/**
 * 标准成本服务接口
 */
public interface StandardCostService {

    /**
     * 创建标准成本
     */
    Long createStandardCost(StandardCostCreateRequest request);

    /**
     * BOM成本滚算
     */
    StandardCostResult bomRollup(BomRollupRequest request);

    /**
     * 审批标准成本
     */
    void approveStandardCost(Long id, ApproveRequest request);

    /**
     * 获取物料当前生效的标准成本
     */
    StandardCost getEffectiveStandardCost(Long materialId);

    /**
     * 比较标准成本版本
     */
    StandardCostCompareResult compareVersions(Long materialId, String version1, String version2);
}

/**
 * 标准成本服务实现
 */
@Service
@Slf4j
public class StandardCostServiceImpl implements StandardCostService {

    @Autowired
    private StandardCostMapper standardCostMapper;

    @Autowired
    private StandardCostCalculator standardCostCalculator;

    @Autowired
    private BomService bomService;

    @Autowired
    private RoutingService routingService;

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long createStandardCost(StandardCostCreateRequest request) {
        // 1. 校验物料是否存在
        validateMaterial(request.getMaterialId());

        // 2. 校验版本号是否已存在
        validateVersionNotExists(request.getMaterialId(), request.getVersionNo());

        // 3. 创建标准成本
        StandardCost standardCost = new StandardCost();
        BeanUtils.copyProperties(request, standardCost);
        standardCost.setStatus(StandardCostStatusEnum.DRAFT.getCode());
        standardCost.setTotalCost(
            request.getMaterialCost()
                .add(request.getLaborCost())
                .add(request.getOverheadCost())
        );

        standardCostMapper.insert(standardCost);

        return standardCost.getId();
    }

    @Override
    public StandardCostResult bomRollup(BomRollupRequest request) {
        log.info("开始BOM成本滚算, materialId: {}", request.getMaterialId());

        // 1. 获取BOM结构
        List<BomNode> bomTree = bomService.getBomTree(
            request.getMaterialId(),
            request.getBomVersion()
        );

        // 2. 递归计算成本
        StandardCostResult result = new StandardCostResult();
        result.setMaterialId(request.getMaterialId());

        BigDecimal totalMaterialCost = BigDecimal.ZERO;
        BigDecimal totalLaborCost = BigDecimal.ZERO;
        BigDecimal totalOverheadCost = BigDecimal.ZERO;
        List<StandardCostDetail> details = new ArrayList<>();

        for (BomNode node : bomTree) {
            // 获取子件标准成本
            StandardCost componentCost = getEffectiveStandardCost(node.getMaterialId());

            if (componentCost == null) {
                // 如果子件没有标准成本，递归计算
                componentCost = calculateComponentCost(node);
            }

            // 计算用量成本
            BigDecimal quantity = node.getQuantity().multiply(
                BigDecimal.ONE.add(node.getScrapRate())
            );

            BigDecimal materialCost = componentCost.getMaterialCost()
                .multiply(quantity);
            BigDecimal laborCost = componentCost.getLaborCost()
                .multiply(quantity);
            BigDecimal overheadCost = componentCost.getOverheadCost()
                .multiply(quantity);

            totalMaterialCost = totalMaterialCost.add(materialCost);
            totalLaborCost = totalLaborCost.add(laborCost);
            totalOverheadCost = totalOverheadCost.add(overheadCost);

            // 添加明细
            StandardCostDetail detail = new StandardCostDetail();
            detail.setMaterialId(node.getMaterialId());
            detail.setMaterialCode(node.getMaterialCode());
            detail.setMaterialName(node.getMaterialName());
            detail.setQuantity(quantity);
            detail.setUnit(node.getUnit());
            detail.setUnitPrice(componentCost.getTotalCost().divide(quantity, 4, RoundingMode.HALF_UP));
            detail.setAmount(materialCost.add(laborCost).add(overheadCost));
            detail.setBomLevel(node.getLevel());
            details.add(detail);
        }

        // 3. 计算本层加工成本
        if (request.getIncludeLabor() || request.getIncludeOverhead()) {
            Routing routing = routingService.getRouting(
                request.getMaterialId(),
                request.getRoutingVersion()
            );

            if (routing != null) {
                LaborOverheadCost loCost = calculateLaborOverheadCost(routing);
                totalLaborCost = totalLaborCost.add(loCost.getLaborCost());
                totalOverheadCost = totalOverheadCost.add(loCost.getOverheadCost());
            }
        }

        result.setMaterialCost(totalMaterialCost);
        result.setLaborCost(totalLaborCost);
        result.setOverheadCost(totalOverheadCost);
        result.setTotalCost(totalMaterialCost.add(totalLaborCost).add(totalOverheadCost));
        result.setDetails(details);

        log.info("BOM成本滚算完成, totalCost: {}", result.getTotalCost());

        return result;
    }
}
```

### 4.3 成本分析服务

```java
/**
 * 成本分析服务接口
 */
public interface CostAnalysisService {

    /**
     * 成本结构分析
     */
    CostStructureResult analyzeCostStructure(CostStructureRequest request);

    /**
     * 成本趋势分析
     */
    CostTrendResult analyzeCostTrend(CostTrendRequest request);

    /**
     * 变动固定成本分析
     */
    CostBehaviorResult analyzeCostBehavior(CostBehaviorRequest request);

    /**
     * 车间成本对比分析
     */
    WorkshopCompareResult compareWorkshopCost(WorkshopCompareRequest request);

    /**
     * 产品成本分析
     */
    ProductCostResult analyzeProductCost(ProductCostRequest request);
}

/**
 * 成本分析服务实现
 */
@Service
public class CostAnalysisServiceImpl implements CostAnalysisService {

    @Autowired
    private CostCalculationMapper calculationMapper;

    @Autowired
    private CostStructureAnalyzer costStructureAnalyzer;

    @Autowired
    private CostTrendAnalyzer costTrendAnalyzer;

    @Autowired
    private CostBehaviorAnalyzer costBehaviorAnalyzer;

    @Override
    public CostStructureResult analyzeCostStructure(CostStructureRequest request) {
        // 获取核算数据
        CostCalculation calculation = calculationMapper.selectByPeriod(
            request.getPeriodYear(),
            request.getPeriodMonth()
        );

        if (calculation == null) {
            throw new BusinessException("该期间未进行成本核算");
        }

        CostStructureResult result = new CostStructureResult();
        result.setPeriodYear(request.getPeriodYear());
        result.setPeriodMonth(request.getPeriodMonth());
        result.setTotalCost(calculation.getTotalCost());

        // 根据分析类型进行分析
        switch (request.getAnalysisType()) {
            case "element":
                result.setStructure(analyzeByElement(calculation));
                break;
            case "center":
                result.setStructure(analyzeByCostCenter(calculation));
                break;
            case "product":
                result.setStructure(analyzeByProduct(calculation));
                break;
            case "behavior":
                result.setStructure(analyzeByBehavior(calculation));
                break;
            default:
                throw new BusinessException("不支持的分析类型");
        }

        return result;
    }

    /**
     * 按成本要素分析
     */
    private List<CostStructureItem> analyzeByElement(CostCalculation calculation) {
        List<CostStructureItem> structure = new ArrayList<>();
        BigDecimal totalCost = calculation.getTotalCost();

        // 材料成本
        structure.add(createStructureItem(
            "01", "材料成本",
            calculation.getTotalMaterialCost(),
            totalCost
        ));

        // 人工成本
        structure.add(createStructureItem(
            "02", "人工成本",
            calculation.getTotalLaborCost(),
            totalCost
        ));

        // 制造费用
        structure.add(createStructureItem(
            "03", "制造费用",
            calculation.getTotalOverheadCost(),
            totalCost
        ));

        return structure;
    }

    /**
     * 按成本性态分析
     */
    private List<CostStructureItem> analyzeByBehavior(CostCalculation calculation) {
        // 获取成本要素的性态分类
        List<CostElement> elements = costElementMapper.selectList(
            new LambdaQueryWrapper<CostElement>()
                .eq(CostElement::getTenantId, TenantContext.getTenantId())
                .eq(CostElement::getStatus, 1)
        );

        Map<String, BigDecimal> behaviorCosts = new HashMap<>();
        behaviorCosts.put("variable", BigDecimal.ZERO);
        behaviorCosts.put("fixed", BigDecimal.ZERO);
        behaviorCosts.put("mixed", BigDecimal.ZERO);

        // 统计各性态成本
        List<CostCollectionDetail> details = getCollectionDetails(calculation.getId());
        for (CostCollectionDetail detail : details) {
            CostElement element = findElement(elements, detail.getElementId());
            if (element != null) {
                String behavior = element.getCostBehavior();
                behaviorCosts.merge(behavior, detail.getAmount(), BigDecimal::add);
            }
        }

        // 构建结果
        List<CostStructureItem> structure = new ArrayList<>();
        BigDecimal totalCost = calculation.getTotalCost();

        structure.add(createStructureItem(
            "01", "变动成本",
            behaviorCosts.get("01"),
            totalCost
        ));

        structure.add(createStructureItem(
            "02", "固定成本",
            behaviorCosts.get("02"),
            totalCost
        ));

        structure.add(createStructureItem(
            "03", "混合成本",
            behaviorCosts.get("03"),
            totalCost
        ));

        return structure;
    }

    private CostStructureItem createStructureItem(
        String code, String name, BigDecimal amount, BigDecimal total) {
        CostStructureItem item = new CostStructureItem();
        item.setCategoryCode(code);
        item.setCategoryName(name);
        item.setAmount(amount);
        item.setRatio(amount.multiply(new BigDecimal("100"))
            .divide(total, 2, RoundingMode.HALF_UP));
        return item;
    }
}
```

---

## 5. 成本计算器设计

### 5.1 材料成本计算器

```java
/**
 * 材料成本计算器
 */
@Component
@Slf4j
public class MaterialCostCalculator {

    @Autowired
    private MmIntegrationService mmIntegrationService;

    @Autowired
    private CostCollectionMapper collectionMapper;

    /**
     * 计算材料成本
     *
     * @param periodYear 会计年度
     * @param periodMonth 会计期间
     * @param costCenterId 成本中心ID
     * @return 材料成本
     */
    public BigDecimal calculate(Integer periodYear, Integer periodMonth, Long costCenterId) {
        log.info("计算材料成本, period: {}-{}, costCenterId: {}",
            periodYear, periodMonth, costCenterId);

        // 1. 从物料系统获取领料单数据
        List<MaterialRequisition> requisitions = mmIntegrationService.getMaterialRequisitions(
            periodYear, periodMonth, costCenterId
        );

        // 2. 计算材料成本
        BigDecimal totalCost = BigDecimal.ZERO;
        List<CostCollectionDetail> details = new ArrayList<>();

        for (MaterialRequisition req : requisitions) {
            // 按移动加权平均法计算成本
            BigDecimal cost = calculateMaterialCostByMovingAverage(req);
            totalCost = totalCost.add(cost);

            // 创建归集明细
            CostCollectionDetail detail = createCollectionDetail(req, cost);
            details.add(detail);
        }

        // 3. 保存归集记录
        saveCollectionRecords(costCenterId, "01", details, periodYear, periodMonth);

        log.info("材料成本计算完成, costCenterId: {}, totalCost: {}",
            costCenterId, totalCost);

        return totalCost;
    }

    /**
     * 按移动加权平均法计算材料成本
     */
    private BigDecimal calculateMaterialCostByMovingAverage(MaterialRequisition req) {
        // 获取物料的移动加权平均单价
        BigDecimal avgPrice = mmIntegrationService.getMovingAveragePrice(
            req.getMaterialId(),
            req.getWarehouseId()
        );

        // 计算成本
        return avgPrice.multiply(req.getQuantity());
    }
}
```

### 5.2 在制品成本计算器

```java
/**
 * 在制品成本计算器
 */
@Component
@Slf4j
public class WipCostCalculator {

    @Autowired
    private PmIntegrationService pmIntegrationService;

    @Autowired
    private CostCalculationDetailMapper detailMapper;

    /**
     * 计算在制品成本
     *
     * @param calcId 核算单ID
     * @return 在制品成本结果
     */
    public WipCostResult calculate(Long calcId) {
        log.info("计算在制品成本, calcId: {}", calcId);

        CostCalculation calculation = calculationMapper.selectById(calcId);

        // 1. 获取期末在制品数据
        List<WipInfo> wipList = pmIntegrationService.getWipInfo(
            calculation.getPeriodYear(),
            calculation.getPeriodMonth()
        );

        BigDecimal totalWipCost = BigDecimal.ZERO;
        List<CostCalculationDetail> details = new ArrayList<>();

        for (WipInfo wip : wipList) {
            // 2. 计算约当产量
            BigDecimal equivalentQty = calculateEquivalentQuantity(wip);

            // 3. 计算在制品成本
            WipCostDetail costDetail = calculateWipCostDetail(wip, equivalentQty, calculation);

            totalWipCost = totalWipCost.add(costDetail.getWipCost());
            details.add(costDetail.getDetail());
        }

        WipCostResult result = new WipCostResult();
        result.setWipCost(totalWipCost);
        result.setDetails(details);

        log.info("在制品成本计算完成, totalWipCost: {}", totalWipCost);

        return result;
    }

    /**
     * 计算约当产量
     */
    private BigDecimal calculateEquivalentQuantity(WipInfo wip) {
        // 材料约当产量 = 在制品数量 x 材料完工率
        BigDecimal materialEquivalent = wip.getWipQty()
            .multiply(wip.getMaterialCompleteRate());

        // 加工约当产量 = 在制品数量 x 加工完工率
        BigDecimal laborEquivalent = wip.getWipQty()
            .multiply(wip.getLaborCompleteRate());

        return materialEquivalent.max(laborEquivalent);
    }
}
```

### 5.3 成本差异计算器

```java
/**
 * 成本差异计算器
 */
@Component
@Slf4j
public class VarianceCalculator {

    @Autowired
    private StandardCostMapper standardCostMapper;

    @Autowired
    private CostVarianceMapper varianceMapper;

    /**
     * 计算成本差异
     */
    public void calculateVariance(CostCalculation calculation) {
        log.info("计算成本差异, calcId: {}", calculation.getId());

        // 获取核算明细
        List<CostCalculationDetail> details = detailMapper.selectByCalcId(calculation.getId());

        for (CostCalculationDetail detail : details) {
            // 获取标准成本
            StandardCost standardCost = standardCostMapper.selectEffective(
                detail.getMaterialId(),
                calculation.getCalcDate()
            );

            if (standardCost == null) {
                log.warn("物料{}没有标准成本", detail.getMaterialCode());
                continue;
            }

            // 计算材料价格差异
            calculateMaterialPriceVariance(detail, standardCost);

            // 计算材料数量差异
            calculateMaterialQtyVariance(detail, standardCost);

            // 计算人工工资率差异
            calculateLaborRateVariance(detail, standardCost);

            // 计算人工效率差异
            calculateLaborEfficiencyVariance(detail, standardCost);

            // 计算制造费用差异
            calculateOverheadVariance(detail, standardCost);
        }
    }

    /**
     * 计算材料价格差异
     * 材料价格差异 = (实际价格 - 标准价格) x 实际数量
     */
    private void calculateMaterialPriceVariance(
        CostCalculationDetail detail, StandardCost standardCost) {

        BigDecimal actualPrice = detail.getMaterialCost()
            .divide(detail.getFinishQty().add(detail.getWipQty()), 4, RoundingMode.HALF_UP);
        BigDecimal standardPrice = standardCost.getMaterialCost()
            .divide(standardCost.getStandardQty(), 4, RoundingMode.HALF_UP);

        BigDecimal actualQty = detail.getFinishQty().add(detail.getWipQty());
        BigDecimal variance = actualPrice.subtract(standardPrice)
            .multiply(actualQty);

        saveVarianceRecord(detail, "01", variance, standardCost.getMaterialCost(),
            detail.getMaterialCost());
    }

    /**
     * 计算材料数量差异
     * 材料数量差异 = (实际数量 - 标准数量) x 标准价格
     */
    private void calculateMaterialQtyVariance(
        CostCalculationDetail detail, StandardCost standardCost) {

        BigDecimal actualQty = detail.getFinishQty().add(detail.getWipQty());
        BigDecimal standardQty = standardCost.getStandardQty()
            .multiply(detail.getFinishQty().add(detail.getWipQty()));

        BigDecimal standardPrice = standardCost.getMaterialCost()
            .divide(standardCost.getStandardQty(), 4, RoundingMode.HALF_UP);

        BigDecimal variance = actualQty.subtract(standardQty)
            .multiply(standardPrice);

        saveVarianceRecord(detail, "02", variance,
            standardPrice.multiply(standardQty),
            standardPrice.multiply(actualQty));
    }

    private void saveVarianceRecord(
        CostCalculationDetail detail,
        String varianceType,
        BigDecimal variance,
        BigDecimal standardAmount,
        BigDecimal actualAmount) {

        CostVariance varianceRecord = new CostVariance();
        varianceRecord.setPeriodYear(detail.getPeriodYear());
        varianceRecord.setPeriodMonth(detail.getPeriodMonth());
        varianceRecord.setMaterialId(detail.getMaterialId());
        varianceRecord.setMaterialCode(detail.getMaterialCode());
        varianceRecord.setVarianceType(varianceType);
        varianceRecord.setStandardAmount(standardAmount);
        varianceRecord.setActualAmount(actualAmount);
        varianceRecord.setVarianceAmount(variance);
        varianceRecord.setVarianceRate(
            variance.multiply(new BigDecimal("100"))
                .divide(standardAmount, 2, RoundingMode.HALF_UP)
        );
        varianceRecord.setStatus("10");

        varianceMapper.insert(varianceRecord);
    }
}
```

---

## 6. 成本分配器设计

### 6.1 成本分配器接口

```java
/**
 * 成本分配器接口
 */
public interface CostAllocator {

    /**
     * 执行成本分配
     */
    AllocationResult allocate(CostAllocationRule rule, CostCalculation calculation);
}

/**
 * 辅助生产成本分配器
 */
@Component
public class AuxiliaryCostAllocator implements CostAllocator {

    @Override
    public AllocationResult allocate(CostAllocationRule rule, CostCalculation calculation) {
        // 1. 获取待分配成本
        BigDecimal amountToAllocate = getAmountToAllocate(rule, calculation);

        // 2. 获取分配基数
        Map<Long, BigDecimal> baseValues = getAllocationBaseValues(rule, calculation);

        // 3. 计算分配比例
        BigDecimal totalBase = baseValues.values().stream()
            .reduce(BigDecimal.ZERO, BigDecimal::add);

        // 4. 执行分配
        List<AllocationDetail> details = new ArrayList<>();
        for (Map.Entry<Long, BigDecimal> entry : baseValues.entrySet()) {
            BigDecimal ratio = entry.getValue()
                .multiply(new BigDecimal("100"))
                .divide(totalBase, 4, RoundingMode.HALF_UP);

            BigDecimal allocatedAmount = amountToAllocate
                .multiply(ratio)
                .divide(new BigDecimal("100"), 2, RoundingMode.HALF_UP);

            AllocationDetail detail = new AllocationDetail();
            detail.setTargetCenterId(entry.getKey());
            detail.setBaseValue(entry.getValue());
            detail.setAllocationRatio(ratio);
            detail.setAllocatedAmount(allocatedAmount);
            details.add(detail);

            // 5. 更新目标成本中心的成本
            updateTargetCenterCost(entry.getKey(), rule.getSourceElementId(), allocatedAmount);
        }

        AllocationResult result = new AllocationResult();
        result.setRuleId(rule.getId());
        result.setTotalAmount(amountToAllocate);
        result.setDetails(details);

        return result;
    }
}
```

---

## 7. 系统集成设计

### 7.1 财务系统集成服务

```java
/**
 * 财务系统集成服务
 */
@Service
@Slf4j
public class FiIntegrationServiceImpl implements FiIntegrationService {

    @Value("${integration.fi.url}")
    private String fiUrl;

    @Autowired
    private RestTemplate restTemplate;

    @Override
    public List<OverheadData> fetchOverheadData(Integer periodYear, Integer periodMonth) {
        log.info("从财务系统获取制造费用数据, period: {}-{}", periodYear, periodMonth);

        String url = fiUrl + "/api/v1/vouchers/overhead";

        Map<String, Object> params = new HashMap<>();
        params.put("periodYear", periodYear);
        params.put("periodMonth", periodMonth);

        try {
            ResponseEntity<ApiResponse<List<OverheadData>>> response =
                restTemplate.exchange(
                    url,
                    HttpMethod.POST,
                    new HttpEntity<>(params),
                    new ParameterizedTypeReference<ApiResponse<List<OverheadData>>>() {}
                );

            if (response.getStatusCode() == HttpStatus.OK && response.getBody() != null) {
                return response.getBody().getData();
            }
        } catch (Exception e) {
            log.error("获取制造费用数据失败", e);
            throw new BusinessException("获取制造费用数据失败: " + e.getMessage());
        }

        return Collections.emptyList();
    }

    @Override
    public VoucherResult sendVoucher(VoucherCreateRequest request) {
        log.info("向财务系统传递凭证, voucherType: {}", request.getVoucherType());

        String url = fiUrl + "/api/v1/vouchers";

        try {
            ResponseEntity<ApiResponse<VoucherResult>> response =
                restTemplate.exchange(
                    url,
                    HttpMethod.POST,
                    new HttpEntity<>(request),
                    new ParameterizedTypeReference<ApiResponse<VoucherResult>>() {}
                );

            if (response.getStatusCode() == HttpStatus.OK && response.getBody() != null) {
                return response.getBody().getData();
            }
        } catch (Exception e) {
            log.error("传递凭证失败", e);
            throw new BusinessException("传递凭证失败: " + e.getMessage());
        }

        return null;
    }

    /**
     * 生成成本结转凭证
     */
    public VoucherCreateRequest buildCostTransferVoucher(CostCalculation calculation) {
        VoucherCreateRequest voucher = new VoucherCreateRequest();
        voucher.setVoucherDate(calculation.getCalcDate());
        voucher.setVoucherType("结转凭证");

        List<VoucherLine> lines = new ArrayList<>();

        // 借：生产成本-完工产品
        VoucherLine debitLine = new VoucherLine();
        debitLine.setAccountCode("1405"); // 库存商品
        debitLine.setDebitAmount(calculation.getFinishCost());
        debitLine.setCreditAmount(BigDecimal.ZERO);
        lines.add(debitLine);

        // 贷：生产成本-直接材料
        VoucherLine creditMaterialLine = new VoucherLine();
        creditMaterialLine.setAccountCode("500101"); // 生产成本-直接材料
        creditMaterialLine.setDebitAmount(BigDecimal.ZERO);
        creditMaterialLine.setCreditAmount(calculation.getTotalMaterialCost());
        lines.add(creditMaterialLine);

        // 贷：生产成本-直接人工
        VoucherLine creditLaborLine = new VoucherLine();
        creditLaborLine.setAccountCode("500102"); // 生产成本-直接人工
        creditLaborLine.setDebitAmount(BigDecimal.ZERO);
        creditLaborLine.setCreditAmount(calculation.getTotalLaborCost());
        lines.add(creditLaborLine);

        // 贷：制造费用
        VoucherLine creditOverheadLine = new VoucherLine();
        creditOverheadLine.setAccountCode("5101"); // 制造费用
        creditOverheadLine.setDebitAmount(BigDecimal.ZERO);
        creditOverheadLine.setCreditAmount(calculation.getTotalOverheadCost());
        lines.add(creditOverheadLine);

        voucher.setLines(lines);

        return voucher;
    }
}
```

### 7.2 生产系统集成服务

```java
/**
 * 生产系统集成服务
 */
@Service
@Slf4j
public class PmIntegrationServiceImpl implements PmIntegrationService {

    @Value("${integration.pm.url}")
    private String pmUrl;

    @Autowired
    private RestTemplate restTemplate;

    @Override
    public List<WorkOrderInfo> fetchWorkOrders(Integer periodYear, Integer periodMonth) {
        log.info("从生产系统获取工单数据");

        String url = pmUrl + "/api/v1/workorders";

        Map<String, Object> params = new HashMap<>();
        params.put("periodYear", periodYear);
        params.put("periodMonth", periodMonth);

        try {
            ResponseEntity<ApiResponse<List<WorkOrderInfo>>> response =
                restTemplate.exchange(
                    url + "?periodYear=" + periodYear + "&periodMonth=" + periodMonth,
                    HttpMethod.GET,
                    null,
                    new ParameterizedTypeReference<ApiResponse<List<WorkOrderInfo>>>() {}
                );

            if (response.getStatusCode() == HttpStatus.OK && response.getBody() != null) {
                return response.getBody().getData();
            }
        } catch (Exception e) {
            log.error("获取工单数据失败", e);
            throw new BusinessException("获取工单数据失败: " + e.getMessage());
        }

        return Collections.emptyList();
    }

    @Override
    public List<TimeRecord> fetchTimeRecords(Integer periodYear, Integer periodMonth) {
        log.info("从生产系统获取工时数据");
        // 类似实现...
        return Collections.emptyList();
    }
}
```

---

## 8. 定时任务设计

### 8.1 成本归集定时任务

```java
/**
 * 成本归集定时任务
 */
@Component
@Slf4j
public class CostCollectionJob {

    @Autowired
    private CostCollectionService costCollectionService;

    /**
     * 每日凌晨1点执行前一天的自动归集
     */
    @Scheduled(cron = "0 0 1 * * ?")
    public void executeDailyCollection() {
        log.info("开始执行每日成本归集任务");

        try {
            LocalDate yesterday = LocalDate.now().minusDays(1);

            CostCollectionRequest request = new CostCollectionRequest();
            request.setPeriodYear(yesterday.getYear());
            request.setPeriodMonth(yesterday.getMonthValue());
            request.setAutoCreate(true);

            // 执行材料成本归集
            costCollectionService.collectMaterialCost(request);

            // 执行人工成本归集
            costCollectionService.collectLaborCost(request);

            log.info("每日成本归集任务执行完成");

        } catch (Exception e) {
            log.error("每日成本归集任务执行失败", e);
            // 发送告警通知
            sendAlertNotification("成本归集任务失败", e.getMessage());
        }
    }
}
```

---

## 9. 异常处理设计

### 9.1 异常类定义

```java
/**
 * 成本管理业务异常
 */
public class CostBusinessException extends RuntimeException {

    private String errorCode;

    public CostBusinessException(String message) {
        super(message);
    }

    public CostBusinessException(String errorCode, String message) {
        super(message);
        this.errorCode = errorCode;
    }
}

/**
 * 成本核算异常
 */
public class CostCalculationException extends CostBusinessException {

    public CostCalculationException(String message) {
        super("COST_CALC_ERROR", message);
    }
}
```

### 9.2 全局异常处理

```java
/**
 * 全局异常处理器
 */
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(CostBusinessException.class)
    public ApiResponse<Void> handleCostBusinessException(CostBusinessException e) {
        log.error("成本管理业务异常: {}", e.getMessage());
        return ApiResponse.error(e.getErrorCode(), e.getMessage());
    }

    @ExceptionHandler(Exception.class)
    public ApiResponse<Void> handleException(Exception e) {
        log.error("系统异常", e);
        return ApiResponse.error("500", "系统异常，请联系管理员");
    }
}
```

---

## 10. 性能优化设计

### 10.1 批量处理优化

```java
/**
 * 批量成本计算优化
 */
@Service
public class BatchCostCalculator {

    @Autowired
    private CostCalculationDetailMapper detailMapper;

    /**
     * 批量计算完工产品成本
     */
    public void batchCalculateFinishCost(Long calcId) {
        // 使用分页处理大量数据
        int pageSize = 1000;
        int pageNum = 1;
        int total;

        do {
            Page<CostCalculationDetail> page = new Page<>(pageNum, pageSize);
            Page<CostCalculationDetail> detailPage = detailMapper.selectPageByCalcId(page, calcId);

            total = detailPage.getRecords().size();

            // 批量计算
            List<CostCalculationDetail> updateList = new ArrayList<>();
            for (CostCalculationDetail detail : detailPage.getRecords()) {
                calculateDetailCost(detail);
                updateList.add(detail);
            }

            // 批量更新
            if (!updateList.isEmpty()) {
                detailMapper.batchUpdateById(updateList);
            }

            pageNum++;

        } while (total == pageSize);
    }
}
```

### 10.2 缓存设计

```java
/**
 * 标准成本缓存
 */
@Component
public class StandardCostCache {

    private static final String CACHE_KEY_PREFIX = "standard_cost:";

    @Autowired
    private RedisTemplate<String, Object> redisTemplate;

    @Autowired
    private StandardCostMapper standardCostMapper;

    /**
     * 获取物料的标准成本(带缓存)
     */
    public StandardCost getEffectiveStandardCost(Long materialId) {
        String cacheKey = CACHE_KEY_PREFIX + materialId;

        // 先从缓存获取
        StandardCost cached = (StandardCost) redisTemplate.opsForValue().get(cacheKey);
        if (cached != null) {
            return cached;
        }

        // 从数据库查询
        StandardCost standardCost = standardCostMapper.selectEffectiveByMaterialId(materialId);
        if (standardCost != null) {
            // 写入缓存，过期时间1小时
            redisTemplate.opsForValue().set(cacheKey, standardCost, 1, TimeUnit.HOURS);
        }

        return standardCost;
    }

    /**
     * 清除缓存
     */
    public void evictCache(Long materialId) {
        String cacheKey = CACHE_KEY_PREFIX + materialId;
        redisTemplate.delete(cacheKey);
    }
}
```

---

## 11. 安全设计

### 11.1 数据权限控制

```java
/**
 * 成本数据权限拦截器
 */
@Component
@Intercepts({
    @Signature(type = StatementHandler.class, method = "prepare", args = {Connection.class, Integer.class})
})
public class CostDataPermissionInterceptor implements Interceptor {

    @Override
    public Object intercept(Invocation invocation) throws Throwable {
        StatementHandler statementHandler = (StatementHandler) invocation.getTarget();

        // 获取SQL
        String sql = statementHandler.getBoundSql().getSql();

        // 判断是否是成本相关表的查询
        if (isCostTable(sql)) {
            // 添加租户和数据权限条件
            String newSql = addPermissionCondition(sql);
            Field field = statementHandler.getBoundSql().getClass().getDeclaredField("sql");
            field.setAccessible(true);
            field.set(statementHandler.getBoundSql(), newSql);
        }

        return invocation.proceed();
    }

    private boolean isCostTable(String sql) {
        return sql.toLowerCase().contains("co_");
    }

    private String addPermissionCondition(String sql) {
        Long tenantId = TenantContext.getTenantId();
        Long userId = UserContext.getUserId();

        // 添加租户条件
        String tenantCondition = " tenant_id = " + tenantId;

        // 根据用户权限添加数据权限条件
        String permissionCondition = getDataPermissionCondition(userId);

        // 重构SQL
        return refactorSql(sql, tenantCondition, permissionCondition);
    }
}
```

---

## 12. 日志与审计

### 12.1 操作日志记录

```java
/**
 * 成本操作日志切面
 */
@Aspect
@Component
@Slf4j
public class CostOperationLogAspect {

    @Autowired
    private OperationLogService operationLogService;

    @Pointcut("@annotation(com.autoerp.co.annotation.CostOperationLog)")
    public void costOperationPointcut() {}

    @Around("costOperationPointcut()")
    public Object around(ProceedingJoinPoint point) throws Throwable {
        // 获取方法注解
        MethodSignature signature = (MethodSignature) point.getSignature();
        Method method = signature.getMethod();
        CostOperationLog annotation = method.getAnnotation(CostOperationLog.class);

        // 记录操作前数据
        Object beforeData = null;
        if (annotation.recordBefore()) {
            beforeData = getBeforeData(point);
        }

        // 执行方法
        Object result = point.proceed();

        // 记录操作日志
        OperationLog log = new OperationLog();
        log.setModule("成本管理");
        log.setOperation(annotation.operation());
        log.setOperationDesc(annotation.description());
        log.setBeforeData(JSON.toJSONString(beforeData));
        log.setAfterData(JSON.toJSONString(result));
        log.setOperator(UserContext.getUserId());
        log.setOperationTime(LocalDateTime.now());

        operationLogService.save(log);

        return result;
    }
}
```

---

## 13. 配置管理

### 13.1 成本核算配置

```java
/**
 * 成本核算配置
 */
@Data
@Configuration
@ConfigurationProperties(prefix = "cost.calculation")
public class CostCalculationProperties {

    /** 是否启用并行计算 */
    private Boolean enableParallel = true;

    /** 并行计算线程数 */
    private Integer parallelThreads = 4;

    /** 成本核算精度 */
    private Integer costScale = 2;

    /** 舍入模式 */
    private RoundingMode roundingMode = RoundingMode.HALF_UP;

    /** 自动归集时间(cron表达式) */
    private String autoCollectionCron = "0 0 1 * * ?";

    /** BOM成本滚算最大层级 */
    private Integer maxBomLevel = 10;
}
```

---

**文档修订历史**

| 版本 | 日期 | 修订人 | 修订内容 |
|-----|------|-------|---------|
| V1.0 | 2026-03-24 | 研发架构团队 | 初始版本 |