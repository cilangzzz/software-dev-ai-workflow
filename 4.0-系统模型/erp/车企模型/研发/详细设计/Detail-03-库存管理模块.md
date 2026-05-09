# Detail-03-库存管理模块

## 文档信息

| 项目 | 内容 |
|------|------|
| 文档名称 | 库存管理模块详细设计文档 |
| 文档编号 | Detail-03 |
| 版本号 | V1.0 |
| 创建日期 | 2026-03-24 |
| 所属系统 | 汽车制造业ERP系统 |
| 模块名称 | 库存管理 (WM) |
| 技术栈 | Spring Boot 2.7 + MyBatis Plus + MySQL 8.x |

---

## 1. 系统架构设计

### 1.1 模块架构图

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              表示层 (Presentation Layer)                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  Web前端  │  移动端H5  │  PDA客户端  │  第三方系统接口                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                              接口层 (API Layer)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  StockController  │  InboundController  │  OutboundController  │            │
│  LocationController  │  AlertController  │  BarcodeController  │            │
├─────────────────────────────────────────────────────────────────────────────┤
│                              业务层 (Service Layer)                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  StockService  │  InboundService  │  OutboundService  │  LocationService   │
│  AlertService  │  BarcodeService  │  TransferService  │  StocktakeService  │
├─────────────────────────────────────────────────────────────────────────────┤
│                              领域层 (Domain Layer)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│  Stock  │  InboundOrder  │  OutboundOrder  │  Location  │  Alert  │         │
│  TransferOrder  │  Barcode  │  VinStock  │  StockLock                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                              基础设施层 (Infrastructure Layer)               │
├─────────────────────────────────────────────────────────────────────────────┤
│  MyBatis Plus  │  Redis缓存  │  消息队列  │  文件存储                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                              数据层 (Data Layer)                            │
├─────────────────────────────────────────────────────────────────────────────┤
│  MySQL 8.x  │  Redis 6.x  │  MongoDB(日志)                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 模块依赖关系

```
┌─────────────────┐
│   库存管理模块   │
└────────┬────────┘
         │
    ┌────┴────┬──────────┬──────────┬──────────┐
    │         │          │          │          │
    v         v          v          v          v
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│ 物料  │ │ 采购  │ │ 生产  │ │ 销售  │ │ 质量  │
│ 模块  │ │ 模块  │ │ 模块  │ │ 模块  │ │ 模块  │
└───────┘ └───────┘ └───────┘ └───────┘ └───────┘
```

### 1.3 技术选型

| 技术组件 | 版本 | 用途 |
|----------|------|------|
| Spring Boot | 2.7.x | 应用框架 |
| MyBatis Plus | 3.5.x | ORM框架 |
| MySQL | 8.x | 关系数据库 |
| Redis | 6.x | 缓存、分布式锁 |
| RocketMQ | 4.9.x | 消息队列 |
| XXL-Job | 2.3.x | 定时任务调度 |
| Swagger | 3.0 | API文档 |
| Lombok | 1.18.x | 代码简化 |

---

## 2. 包结构设计

### 2.1 基础包结构

```
com.autoerp.wm
├── controller                    # 控制器层
│   ├── StockController.java
│   ├── InboundController.java
│   ├── OutboundController.java
│   ├── TransferController.java
│   ├── LocationController.java
│   ├── AlertController.java
│   ├── BarcodeController.java
│   ├── StocktakeController.java
│   └── pda                       # PDA接口
│       ├── PdaInboundController.java
│       ├── PdaOutboundController.java
│       └── PdaStockController.java
├── service                       # 服务层
│   ├── StockService.java
│   ├── InboundService.java
│   ├── OutboundService.java
│   ├── TransferService.java
│   ├── LocationService.java
│   ├── AlertService.java
│   ├── BarcodeService.java
│   ├── StocktakeService.java
│   ├── VinStockService.java
│   ├── StockLockService.java
│   └── impl                      # 服务实现
│       ├── StockServiceImpl.java
│       ├── InboundServiceImpl.java
│       ├── OutboundServiceImpl.java
│       └── ...
├── mapper                        # 数据访问层
│   ├── StockMapper.java
│   ├── InboundOrderMapper.java
│   ├── OutboundOrderMapper.java
│   └── ...
├── entity                        # 实体类
│   ├── Stock.java
│   ├── InboundOrder.java
│   ├── InboundOrderLine.java
│   ├── OutboundOrder.java
│   ├── OutboundOrderLine.java
│   ├── TransferOrder.java
│   ├── Warehouse.java
│   ├── Zone.java
│   ├── Location.java
│   ├── AlertRule.java
│   ├── AlertMessage.java
│   ├── BarcodeRecord.java
│   ├── VinStock.java
│   └── StockLock.java
├── dto                           # 数据传输对象
│   ├── request
│   │   ├── StockQueryRequest.java
│   │   ├── InboundCreateRequest.java
│   │   ├── OutboundCreateRequest.java
│   │   └── ...
│   └── response
│       ├── StockResponse.java
│       ├── InboundDetailResponse.java
│       ├── OutboundDetailResponse.java
│       └── ...
├── vo                            # 视图对象
│   ├── StockVO.java
│   ├── InboundVO.java
│   └── ...
├── convert                       # 对象转换器
│   ├── StockConvert.java
│   ├── InboundConvert.java
│   └── ...
├── enums                         # 枚举类
│   ├── WarehouseTypeEnum.java
│   ├── InboundTypeEnum.java
│   ├── OutboundTypeEnum.java
│   ├── StockStatusEnum.java
│   ├── AlertTypeEnum.java
│   └── PickingStrategyEnum.java
├── event                         # 事件类
│   ├── StockChangeEvent.java
│   ├── InboundCompleteEvent.java
│   └── OutboundCompleteEvent.java
├── listener                      # 事件监听器
│   ├── StockEventListener.java
│   └── AlertEventListener.java
├── job                           # 定时任务
│   ├── AlertCheckJob.java
│   ├── StockDaysUpdateJob.java
│   └── DormantStockCheckJob.java
├── strategy                      # 策略模式
│   ├── picking
│   │   ├── PickingStrategy.java
│   │   ├── FifoPickingStrategy.java
│   │   ├── LifoPickingStrategy.java
│   │   └── FefoPickingStrategy.java
│   └── location
│       ├── LocationRecommendStrategy.java
│       └── DefaultLocationRecommendStrategy.java
├── constant                      # 常量类
│   ├── WmConstants.java
│   └── WmErrorCode.java
└── util                          # 工具类
    ├── BarcodeGenerator.java
    ├── StockCalculator.java
    └── VinValidator.java
```

---

## 3. 核心类设计

### 3.1 库存服务设计

#### 3.1.1 StockService 接口

```java
package com.autoerp.wm.service;

import com.autoerp.wm.dto.request.*;
import com.autoerp.wm.dto.response.*;
import com.autoerp.wm.entity.Stock;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.IService;

import java.util.List;

/**
 * 库存服务接口
 */
public interface StockService extends IService<Stock> {

    /**
     * 分页查询库存
     */
    Page<StockResponse> queryStockPage(StockQueryRequest request);

    /**
     * 查询库存详情
     */
    StockDetailResponse queryStockDetail(Long stockId);

    /**
     * 查询物料库存汇总
     */
    StockSummaryResponse queryStockSummary(String materialCode);

    /**
     * 查询库存流水
     */
    Page<StockLogResponse> queryStockLogPage(StockLogQueryRequest request);

    /**
     * 增加库存
     */
    void increaseStock(StockOperateRequest request);

    /**
     * 减少库存
     */
    void decreaseStock(StockOperateRequest request);

    /**
     * 锁定库存
     */
    void lockStock(StockLockRequest request);

    /**
     * 解锁库存
     */
    void unlockStock(String lockNo);

    /**
     * 冻结库存
     */
    void freezeStock(Long stockId, String reason);

    /**
     * 解冻库存
     */
    void unfreezeStock(Long stockId);

    /**
     * 获取可用库存
     */
    BigDecimal getAvailableStock(Long warehouseId, Long materialId, String batchNo);

    /**
     * 批量查询库存
     */
    List<Stock> batchQueryStock(List<StockQueryItem> items);

    /**
     * 导出库存
     */
    byte[] exportStock(StockQueryRequest request);
}
```

#### 3.1.2 StockServiceImpl 实现

```java
package com.autoerp.wm.service.impl;

import com.autoerp.wm.constant.WmErrorCode;
import com.autoerp.wm.convert.StockConvert;
import com.autoerp.wm.dto.request.*;
import com.autoerp.wm.dto.response.*;
import com.autoerp.wm.entity.Stock;
import com.autoerp.wm.entity.StockLog;
import com.autoerp.wm.entity.StockLock;
import com.autoerp.wm.enums.StockStatusEnum;
import com.autoerp.wm.event.StockChangeEvent;
import com.autoerp.wm.mapper.StockLogMapper;
import com.autoerp.wm.mapper.StockMapper;
import com.autoerp.wm.service.*;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.redisson.api.RLock;
import org.redisson.api.RedissonClient;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

/**
 * 库存服务实现
 */
@Slf4j
@Service
@RequiredArgsConstructor
public class StockServiceImpl extends ServiceImpl<StockMapper, Stock>
        implements StockService {

    private final StockLogMapper stockLogMapper;
    private final StockLockService stockLockService;
    private final RedissonClient redissonClient;
    private final ApplicationEventPublisher eventPublisher;

    @Override
    public Page<StockResponse> queryStockPage(StockQueryRequest request) {
        Page<Stock> page = new Page<>(request.getCurrent(), request.getSize());

        LambdaQueryWrapper<Stock> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(request.getWarehouseId() != null, Stock::getWarehouseId, request.getWarehouseId())
               .likeRight(request.getMaterialCode() != null, Stock::getMaterialCode, request.getMaterialCode())
               .likeRight(request.getMaterialName() != null, Stock::getMaterialName, request.getMaterialName())
               .eq(request.getBatchNo() != null, Stock::getBatchNo, request.getBatchNo())
               .eq(request.getVinCode() != null, Stock::getVinCode, request.getVinCode())
               .eq(request.getStatus() != null, Stock::getStatus, request.getStatus())
               .eq(Stock::getIsDeleted, 0)
               .orderByDesc(Stock::getCreateTime);

        Page<Stock> stockPage = this.page(page, wrapper);

        return stockPage.convert(StockConvert.INSTANCE::toResponse);
    }

    @Override
    public StockDetailResponse queryStockDetail(Long stockId) {
        Stock stock = this.getById(stockId);
        if (stock == null) {
            throw new BusinessException(WmErrorCode.STOCK_NOT_FOUND);
        }
        return StockConvert.INSTANCE.toDetailResponse(stock);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void increaseStock(StockOperateRequest request) {
        // 使用分布式锁保证并发安全
        String lockKey = String.format("stock:lock:%d:%d:%s",
                request.getWarehouseId(), request.getMaterialId(), request.getBatchNo());
        RLock lock = redissonClient.getLock(lockKey);

        try {
            lock.lock();

            // 查询或创建库存记录
            Stock stock = getOrCreateStock(request);

            // 更新库存数量
            BigDecimal beforeQty = stock.getQuantity();
            stock.setQuantity(beforeQty.add(request.getQuantity()));
            stock.setAvailableQty(stock.getAvailableQty().add(request.getQuantity()));
            stock.setLastInTime(LocalDateTime.now());
            this.updateById(stock);

            // 记录库存流水
            saveStockLog(stock, request, beforeQty, 1);

            // 发布库存变更事件
            eventPublisher.publishEvent(new StockChangeEvent(this, stock, request));

        } finally {
            lock.unlock();
        }
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void decreaseStock(StockOperateRequest request) {
        String lockKey = String.format("stock:lock:%d:%d:%s",
                request.getWarehouseId(), request.getMaterialId(), request.getBatchNo());
        RLock lock = redissonClient.getLock(lockKey);

        try {
            lock.lock();

            // 查询库存记录
            Stock stock = this.getOne(new LambdaQueryWrapper<Stock>()
                    .eq(Stock::getWarehouseId, request.getWarehouseId())
                    .eq(Stock::getMaterialId, request.getMaterialId())
                    .eq(request.getBatchNo() != null, Stock::getBatchNo, request.getBatchNo())
                    .eq(Stock::getIsDeleted, 0));

            if (stock == null) {
                throw new BusinessException(WmErrorCode.STOCK_NOT_FOUND);
            }

            // 检查可用库存
            if (stock.getAvailableQty().compareTo(request.getQuantity()) < 0) {
                throw new BusinessException(WmErrorCode.STOCK_NOT_ENOUGH);
            }

            // 更新库存数量
            BigDecimal beforeQty = stock.getQuantity();
            stock.setQuantity(beforeQty.subtract(request.getQuantity()));
            stock.setAvailableQty(stock.getAvailableQty().subtract(request.getQuantity()));
            stock.setLastOutTime(LocalDateTime.now());
            this.updateById(stock);

            // 记录库存流水
            saveStockLog(stock, request, beforeQty, -1);

            // 发布库存变更事件
            eventPublisher.publishEvent(new StockChangeEvent(this, stock, request));

        } finally {
            lock.unlock();
        }
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void lockStock(StockLockRequest request) {
        String lockKey = String.format("stock:lock:%d:%d:%s",
                request.getWarehouseId(), request.getMaterialId(), request.getBatchNo());
        RLock lock = redissonClient.getLock(lockKey);

        try {
            lock.lock();

            // 查询库存
            Stock stock = getStock(request.getWarehouseId(), request.getMaterialId(), request.getBatchNo());

            if (stock == null) {
                throw new BusinessException(WmErrorCode.STOCK_NOT_FOUND);
            }

            // 检查可用库存
            if (stock.getAvailableQty().compareTo(request.getLockQty()) < 0) {
                throw new BusinessException(WmErrorCode.STOCK_NOT_ENOUGH);
            }

            // 更新锁定数量
            stock.setAvailableQty(stock.getAvailableQty().subtract(request.getLockQty()));
            stock.setLockedQty(stock.getLockedQty().add(request.getLockQty()));
            this.updateById(stock);

            // 创建锁定记录
            StockLock stockLock = new StockLock();
            stockLock.setLockNo(generateLockNo());
            stockLock.setStockId(stock.getId());
            stockLock.setWarehouseId(stock.getWarehouseId());
            stockLock.setMaterialId(stock.getMaterialId());
            stockLock.setBatchNo(stock.getBatchNo());
            stockLock.setLockQty(request.getLockQty());
            stockLock.setLockType(request.getLockType());
            stockLock.setSourceOrderNo(request.getSourceOrderNo());
            stockLock.setLockReason(request.getLockReason());
            stockLock.setStatus("LOCKED");
            stockLockService.save(stockLock);

        } finally {
            lock.unlock();
        }
    }

    /**
     * 获取或创建库存记录
     */
    private Stock getOrCreateStock(StockOperateRequest request) {
        Stock stock = this.getOne(new LambdaQueryWrapper<Stock>()
                .eq(Stock::getWarehouseId, request.getWarehouseId())
                .eq(Stock::getMaterialId, request.getMaterialId())
                .eq(request.getBatchNo() != null, Stock::getBatchNo, request.getBatchNo())
                .eq(request.getVinCode() != null, Stock::getVinCode, request.getVinCode())
                .eq(Stock::getIsDeleted, 0));

        if (stock == null) {
            stock = new Stock();
            stock.setWarehouseId(request.getWarehouseId());
            stock.setWarehouseCode(request.getWarehouseCode());
            stock.setZoneId(request.getZoneId());
            stock.setLocationId(request.getLocationId());
            stock.setMaterialId(request.getMaterialId());
            stock.setMaterialCode(request.getMaterialCode());
            stock.setMaterialName(request.getMaterialName());
            stock.setBatchNo(request.getBatchNo());
            stock.setVinCode(request.getVinCode());
            stock.setUnitId(request.getUnitId());
            stock.setUnitCode(request.getUnitCode());
            stock.setQuantity(BigDecimal.ZERO);
            stock.setAvailableQty(BigDecimal.ZERO);
            stock.setLockedQty(BigDecimal.ZERO);
            stock.setInspectQty(BigDecimal.ZERO);
            stock.setStatus(StockStatusEnum.NORMAL.getCode());
            stock.setProductionDate(request.getProductionDate());
            stock.setExpiryDate(request.getExpiryDate());
            stock.setIsVmi(request.getIsVmi() != null ? request.getIsVmi() : 0);
            this.save(stock);
        }

        return stock;
    }

    /**
     * 保存库存流水
     */
    private void saveStockLog(Stock stock, StockOperateRequest request,
                              BigDecimal beforeQty, int direction) {
        StockLog log = new StockLog();
        log.setLogNo(generateLogNo());
        log.setWarehouseId(stock.getWarehouseId());
        log.setWarehouseCode(stock.getWarehouseCode());
        log.setLocationId(stock.getLocationId());
        log.setLocationCode(stock.getLocationCode());
        log.setMaterialId(stock.getMaterialId());
        log.setMaterialCode(stock.getMaterialCode());
        log.setMaterialName(stock.getMaterialName());
        log.setBatchNo(stock.getBatchNo());
        log.setVinCode(stock.getVinCode());
        log.setTransType(request.getTransType());
        log.setTransNo(request.getTransNo());
        log.setDirection(direction);
        log.setQuantity(request.getQuantity());
        log.setBeforeQty(beforeQty);
        log.setAfterQty(stock.getQuantity());
        log.setUnitId(stock.getUnitId());
        log.setUnitCode(stock.getUnitCode());
        log.setOperTime(LocalDateTime.now());
        log.setOperUserId(request.getOperUserId());
        log.setOperUserName(request.getOperUserName());
        stockLogMapper.insert(log);
    }

    /**
     * 生成流水号
     */
    private String generateLogNo() {
        return "SL" + System.currentTimeMillis() + UUID.randomUUID().toString().substring(0, 4);
    }

    /**
     * 生成锁定单号
     */
    private String generateLockNo() {
        return "LK" + System.currentTimeMillis() + UUID.randomUUID().toString().substring(0, 4);
    }
}
```

---

### 3.2 入库服务设计

#### 3.2.1 InboundService 接口

```java
package com.autoerp.wm.service;

import com.autoerp.wm.dto.request.*;
import com.autoerp.wm.dto.response.*;
import com.autoerp.wm.entity.InboundOrder;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.IService;

/**
 * 入库服务接口
 */
public interface InboundService extends IService<InboundOrder> {

    /**
     * 分页查询入库单
     */
    Page<InboundResponse> queryInboundPage(InboundQueryRequest request);

    /**
     * 查询入库单详情
     */
    InboundDetailResponse queryInboundDetail(Long inboundId);

    /**
     * 创建入库单
     */
    Long createInbound(InboundCreateRequest request);

    /**
     * 根据采购订单创建入库单
     */
    Long createInboundFromPO(InboundFromPORequest request);

    /**
     * 根据生产工单创建入库单
     */
    Long createInboundFromWO(InboundFromWORequest request);

    /**
     * 更新入库单
     */
    void updateInbound(Long inboundId, InboundUpdateRequest request);

    /**
     * 删除入库单
     */
    void deleteInbound(Long inboundId);

    /**
     * 提交审核
     */
    void submitInbound(Long inboundId);

    /**
     * 审核入库单
     */
    void approveInbound(Long inboundId, ApproveRequest request);

    /**
     * 确认入库
     */
    void confirmInbound(Long inboundId);

    /**
     * 取消入库单
     */
    void cancelInbound(Long inboundId);

    /**
     * 打印入库单
     */
    byte[] printInbound(Long inboundId);
}
```

#### 3.2.2 InboundServiceImpl 实现（关键方法）

```java
package com.autoerp.wm.service.impl;

import com.autoerp.wm.constant.WmErrorCode;
import com.autoerp.wm.convert.InboundConvert;
import com.autoerp.wm.dto.request.*;
import com.autoerp.wm.dto.response.*;
import com.autoerp.wm.entity.*;
import com.autoerp.wm.enums.InboundStatusEnum;
import com.autoerp.wm.enums.InboundTypeEnum;
import com.autoerp.wm.event.InboundCompleteEvent;
import com.autoerp.wm.mapper.*;
import com.autoerp.wm.service.*;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.util.List;

/**
 * 入库服务实现
 */
@Slf4j
@Service
@RequiredArgsConstructor
public class InboundServiceImpl extends ServiceImpl<InboundOrderMapper, InboundOrder>
        implements InboundService {

    private final InboundOrderLineMapper lineMapper;
    private final StockService stockService;
    private final VinStockService vinStockService;
    private final ApplicationEventPublisher eventPublisher;
    private final SequenceService sequenceService;

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long createInbound(InboundCreateRequest request) {
        // 校验仓库
        validateWarehouse(request.getWarehouseId());

        // 创建入库单头
        InboundOrder inboundOrder = InboundConvert.INSTANCE.toEntity(request);
        inboundOrder.setOrderNo(sequenceService.generateInboundNo(request.getOrderType()));
        inboundOrder.setStatus(InboundStatusEnum.DRAFT.getCode());
        inboundOrder.setTotalQty(calculateTotalQty(request.getLines()));
        inboundOrder.setTotalLine(request.getLines().size());
        this.save(inboundOrder);

        // 创建入库单明细
        List<InboundOrderLine> lines = InboundConvert.INSTANCE.toLineEntities(request.getLines());
        for (int i = 0; i < lines.size(); i++) {
            lines.get(i).setOrderId(inboundOrder.getId());
            lines.get(i).setOrderNo(inboundOrder.getOrderNo());
            lines.get(i).setLineNo(i + 1);
        }
        lineMapper.insertBatch(lines);

        return inboundOrder.getId();
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void confirmInbound(Long inboundId) {
        InboundOrder inboundOrder = this.getById(inboundId);
        if (inboundOrder == null) {
            throw new BusinessException(WmErrorCode.INBOUND_NOT_FOUND);
        }

        // 检查状态
        if (!InboundStatusEnum.APPROVED.getCode().equals(inboundOrder.getStatus())) {
            throw new BusinessException(WmErrorCode.INBOUND_STATUS_ERROR);
        }

        // 查询明细
        List<InboundOrderLine> lines = lineMapper.selectList(
                new LambdaQueryWrapper<InboundOrderLine>()
                        .eq(InboundOrderLine::getOrderId, inboundId));

        // 更新库存
        for (InboundOrderLine line : lines) {
            StockOperateRequest stockRequest = new StockOperateRequest();
            stockRequest.setWarehouseId(inboundOrder.getWarehouseId());
            stockRequest.setWarehouseCode(inboundOrder.getWarehouseCode());
            stockRequest.setMaterialId(line.getMaterialId());
            stockRequest.setMaterialCode(line.getMaterialCode());
            stockRequest.setMaterialName(line.getMaterialName());
            stockRequest.setBatchNo(line.getBatchNo());
            stockRequest.setLocationId(line.getLocationId());
            stockRequest.setLocationCode(line.getLocationCode());
            stockRequest.setQuantity(line.getThisQty());
            stockRequest.setTransType(inboundOrder.getOrderType());
            stockRequest.setTransNo(inboundOrder.getOrderNo());
            stockRequest.setProductionDate(line.getProductionDate());
            stockRequest.setExpiryDate(line.getExpiryDate());

            stockService.increaseStock(stockRequest);

            // 处理VIN码
            if (line.getVinCode() != null) {
                processVinInbound(line, inboundOrder);
            }
        }

        // 更新入库单状态
        inboundOrder.setStatus(InboundStatusEnum.COMPLETED.getCode());
        this.updateById(inboundOrder);

        // 发布入库完成事件
        eventPublisher.publishEvent(new InboundCompleteEvent(this, inboundOrder));
    }

    /**
     * 处理整车VIN入库
     */
    private void processVinInbound(InboundOrderLine line, InboundOrder inboundOrder) {
        VinStock vinStock = new VinStock();
        vinStock.setVinCode(line.getVinCode());
        vinStock.setModelId(line.getModelId());
        vinStock.setModelCode(line.getModelCode());
        vinStock.setModelName(line.getModelName());
        vinStock.setConfigId(line.getConfigId());
        vinStock.setConfigCode(line.getConfigCode());
        vinStock.setConfigName(line.getConfigName());
        vinStock.setExteriorColor(line.getExteriorColor());
        vinStock.setInteriorColor(line.getInteriorColor());
        vinStock.setEngineNo(line.getEngineNo());
        vinStock.setMotorNo(line.getMotorNo());
        vinStock.setProductionDate(line.getProductionDate());
        vinStock.setWarehouseId(inboundOrder.getWarehouseId());
        vinStock.setWarehouseCode(inboundOrder.getWarehouseCode());
        vinStock.setInTime(inboundOrder.getCreateTime());
        vinStock.setStockStatus("NORMAL");
        vinStock.setSalesStatus("UNSALE");

        vinStockService.save(vinStock);
    }

    /**
     * 计算总数量
     */
    private BigDecimal calculateTotalQty(List<InboundLineRequest> lines) {
        return lines.stream()
                .map(InboundLineRequest::getThisQty)
                .reduce(BigDecimal.ZERO, BigDecimal::add);
    }

    /**
     * 校验仓库
     */
    private void validateWarehouse(Long warehouseId) {
        // 实现仓库校验逻辑
    }
}
```

---

### 3.3 出库服务设计

#### 3.3.1 OutboundService 接口

```java
package com.autoerp.wm.service;

import com.autoerp.wm.dto.request.*;
import com.autoerp.wm.dto.response.*;
import com.autoerp.wm.entity.OutboundOrder;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.IService;

import java.util.List;

/**
 * 出库服务接口
 */
public interface OutboundService extends IService<OutboundOrder> {

    /**
     * 分页查询出库单
     */
    Page<OutboundResponse> queryOutboundPage(OutboundQueryRequest request);

    /**
     * 查询出库单详情
     */
    OutboundDetailResponse queryOutboundDetail(Long outboundId);

    /**
     * 创建出库单
     */
    Long createOutbound(OutboundCreateRequest request);

    /**
     * 创建领料申请
     */
    Long createMaterialRequisition(MaterialRequisitionRequest request);

    /**
     * 根据销售订单创建出库单
     */
    Long createOutboundFromSO(OutboundFromSORequest request);

    /**
     * 更新出库单
     */
    void updateOutbound(Long outboundId, OutboundUpdateRequest request);

    /**
     * 删除出库单
     */
    void deleteOutbound(Long outboundId);

    /**
     * 提交审核
     */
    void submitOutbound(Long outboundId);

    /**
     * 审核出库单
     */
    void approveOutbound(Long outboundId, ApproveRequest request);

    /**
     * 生成拣货任务
     */
    List<PickingTaskResponse> generatePickingTask(Long outboundId);

    /**
     * 确认拣货
     */
    void confirmPicking(PickingConfirmRequest request);

    /**
     * 确认出库
     */
    void confirmOutbound(Long outboundId);

    /**
     * 取消出库单
     */
    void cancelOutbound(Long outboundId);

    /**
     * 绑定VIN
     */
    void bindVin(Long outboundId, Long lineId, List<String> vinCodes);
}
```

#### 3.3.2 拣货策略实现

```java
package com.autoerp.wm.strategy.picking;

import com.autoerp.wm.entity.Stock;
import java.math.BigDecimal;
import java.util.List;

/**
 * 拣货策略接口
 */
public interface PickingStrategy {

    /**
     * 获取策略编码
     */
    String getCode();

    /**
     * 获取策略名称
     */
    String getName();

    /**
     * 执行拣货推荐
     * @param warehouseId 仓库ID
     * @param materialId 物料ID
     * @param quantity 需求数量
     * @return 拣货推荐列表
     */
    List<PickingRecommend> recommend(Long warehouseId, Long materialId, BigDecimal quantity);
}

/**
 * 拣货推荐
 */
@Data
public class PickingRecommend {
    private Long stockId;
    private String batchNo;
    private String locationCode;
    private BigDecimal quantity;
    private BigDecimal priority;
    private LocalDateTime inTime;
}

/**
 * 先进先出策略
 */
@Component
public class FifoPickingStrategy implements PickingStrategy {

    @Autowired
    private StockMapper stockMapper;

    @Override
    public String getCode() {
        return "FIFO";
    }

    @Override
    public String getName() {
        return "先进先出";
    }

    @Override
    public List<PickingRecommend> recommend(Long warehouseId, Long materialId, BigDecimal quantity) {
        // 查询可用库存，按入库时间升序
        List<Stock> stocks = stockMapper.selectList(
                new LambdaQueryWrapper<Stock>()
                        .eq(Stock::getWarehouseId, warehouseId)
                        .eq(Stock::getMaterialId, materialId)
                        .gt(Stock::getAvailableQty, BigDecimal.ZERO)
                        .eq(Stock::getStatus, "NORMAL")
                        .orderByAsc(Stock::getLastInTime));

        List<PickingRecommend> result = new ArrayList<>();
        BigDecimal remainQty = quantity;

        for (Stock stock : stocks) {
            if (remainQty.compareTo(BigDecimal.ZERO) <= 0) {
                break;
            }

            PickingRecommend recommend = new PickingRecommend();
            recommend.setStockId(stock.getId());
            recommend.setBatchNo(stock.getBatchNo());
            recommend.setLocationCode(stock.getLocationCode());
            recommend.setInTime(stock.getLastInTime());

            BigDecimal pickQty = stock.getAvailableQty().min(remainQty);
            recommend.setQuantity(pickQty);

            result.add(recommend);
            remainQty = remainQty.subtract(pickQty);
        }

        return result;
    }
}

/**
 * 拣货策略工厂
 */
@Component
public class PickingStrategyFactory {

    @Autowired
    private List<PickingStrategy> strategies;

    private Map<String, PickingStrategy> strategyMap;

    @PostConstruct
    public void init() {
        strategyMap = strategies.stream()
                .collect(Collectors.toMap(PickingStrategy::getCode, Function.identity()));
    }

    public PickingStrategy getStrategy(String code) {
        PickingStrategy strategy = strategyMap.get(code);
        if (strategy == null) {
            throw new BusinessException("拣货策略不存在: " + code);
        }
        return strategy;
    }
}
```

---

### 3.4 库存预警服务设计

#### 3.4.1 AlertService 接口

```java
package com.autoerp.wm.service;

import com.autoerp.wm.dto.request.*;
import com.autoerp.wm.dto.response.*;
import com.autoerp.wm.entity.AlertMessage;
import com.autoerp.wm.entity.AlertRule;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.IService;

import java.util.List;

/**
 * 预警服务接口
 */
public interface AlertService extends IService<AlertRule> {

    /**
     * 分页查询预警规则
     */
    Page<AlertRuleResponse> queryAlertRulePage(AlertRuleQueryRequest request);

    /**
     * 创建预警规则
     */
    Long createAlertRule(AlertRuleCreateRequest request);

    /**
     * 更新预警规则
     */
    void updateAlertRule(Long ruleId, AlertRuleUpdateRequest request);

    /**
     * 启用/停用预警规则
     */
    void toggleAlertRule(Long ruleId, Integer status);

    /**
     * 分页查询预警消息
     */
    Page<AlertMessageResponse> queryAlertMessagePage(AlertMessageQueryRequest request);

    /**
     * 处理预警消息
     */
    void handleAlertMessage(Long messageId, AlertHandleRequest request);

    /**
     * 关闭预警消息
     */
    void closeAlertMessage(Long messageId);

    /**
     * 执行预警检测
     */
    void executeAlertCheck();

    /**
     * 检测指定类型的预警
     */
    List<AlertMessage> checkAlert(String alertType, AlertRule rule);
}
```

#### 3.4.2 AlertServiceImpl 实现

```java
package com.autoerp.wm.service.impl;

import com.autoerp.wm.constant.WmErrorCode;
import com.autoerp.wm.dto.request.*;
import com.autoerp.wm.dto.response.*;
import com.autoerp.wm.entity.*;
import com.autoerp.wm.enums.AlertTypeEnum;
import com.autoerp.wm.event.AlertEvent;
import com.autoerp.wm.mapper.*;
import com.autoerp.wm.service.*;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.*;

/**
 * 预警服务实现
 */
@Slf4j
@Service
@RequiredArgsConstructor
public class AlertServiceImpl extends ServiceImpl<AlertRuleMapper, AlertRule>
        implements AlertService {

    private final AlertMessageMapper alertMessageMapper;
    private final StockMapper stockMapper;
    private final ApplicationEventPublisher eventPublisher;
    private final NotifyService notifyService;

    @Override
    @Async
    public void executeAlertCheck() {
        log.info("开始执行库存预警检测...");

        // 查询所有启用的预警规则
        List<AlertRule> rules = this.list(new LambdaQueryWrapper<AlertRule>()
                .eq(AlertRule::getStatus, 1));

        for (AlertRule rule : rules) {
            try {
                List<AlertMessage> messages = checkAlert(rule.getAlertType(), rule);

                // 保存预警消息
                for (AlertMessage message : messages) {
                    alertMessageMapper.insert(message);

                    // 发送通知
                    sendNotification(rule, message);
                }
            } catch (Exception e) {
                log.error("预警检测失败, 规则: {}", rule.getRuleCode(), e);
            }
        }

        log.info("库存预警检测完成");
    }

    @Override
    public List<AlertMessage> checkAlert(String alertType, AlertRule rule) {
        List<AlertMessage> messages = new ArrayList<>();

        switch (alertType) {
            case "UPPER_LIMIT":
                messages.addAll(checkUpperLimit(rule));
                break;
            case "LOWER_LIMIT":
                messages.addAll(checkLowerLimit(rule));
                break;
            case "SAFETY_STOCK":
                messages.addAll(checkSafetyStock(rule));
                break;
            case "DORMANT":
                messages.addAll(checkDormant(rule));
                break;
            case "EXPIRY":
                messages.addAll(checkExpiry(rule));
                break;
            case "EXPIRED":
                messages.addAll(checkExpired(rule));
                break;
            default:
                log.warn("未知的预警类型: {}", alertType);
        }

        return messages;
    }

    /**
     * 检测库存上限预警
     */
    private List<AlertMessage> checkUpperLimit(AlertRule rule) {
        List<AlertMessage> messages = new ArrayList<>();

        LambdaQueryWrapper<Stock> wrapper = buildStockWrapper(rule);
        wrapper.gt(Stock::getQuantity, rule.getThresholdValue());

        List<Stock> stocks = stockMapper.selectList(wrapper);

        for (Stock stock : stocks) {
            AlertMessage message = createAlertMessage(rule, stock);
            message.setCurrentValue(stock.getQuantity());
            messages.add(message);
        }

        return messages;
    }

    /**
     * 检测库存下限预警
     */
    private List<AlertMessage> checkLowerLimit(AlertRule rule) {
        List<AlertMessage> messages = new ArrayList<>();

        LambdaQueryWrapper<Stock> wrapper = buildStockWrapper(rule);
        wrapper.lt(Stock::getQuantity, rule.getThresholdValue());

        List<Stock> stocks = stockMapper.selectList(wrapper);

        for (Stock stock : stocks) {
            AlertMessage message = createAlertMessage(rule, stock);
            message.setCurrentValue(stock.getQuantity());
            messages.add(message);
        }

        return messages;
    }

    /**
     * 检测安全库存预警
     */
    private List<AlertMessage> checkSafetyStock(AlertRule rule) {
        List<AlertMessage> messages = new ArrayList<>();

        LambdaQueryWrapper<Stock> wrapper = buildStockWrapper(rule);
        wrapper.lt(Stock::getAvailableQty, rule.getThresholdValue());

        List<Stock> stocks = stockMapper.selectList(wrapper);

        for (Stock stock : stocks) {
            AlertMessage message = createAlertMessage(rule, stock);
            message.setCurrentValue(stock.getAvailableQty());
            messages.add(message);
        }

        return messages;
    }

    /**
     * 检测呆滞库存预警
     */
    private List<AlertMessage> checkDormant(AlertRule rule) {
        List<AlertMessage> messages = new ArrayList<>();

        Integer dormantDays = rule.getThresholdValue().intValue();
        LocalDateTime thresholdTime = LocalDateTime.now().minusDays(dormantDays);

        LambdaQueryWrapper<Stock> wrapper = buildStockWrapper(rule);
        wrapper.lt(Stock::getLastOutTime, thresholdTime)
               .or()
               .isNull(Stock::getLastOutTime)
               .lt(Stock::getLastInTime, thresholdTime);

        List<Stock> stocks = stockMapper.selectList(wrapper);

        for (Stock stock : stocks) {
            AlertMessage message = createAlertMessage(rule, stock);
            // 计算库龄
            if (stock.getLastOutTime() != null) {
                message.setCurrentValue(BigDecimal.valueOf(
                        ChronoUnit.DAYS.between(stock.getLastOutTime(), LocalDateTime.now())));
            } else {
                message.setCurrentValue(BigDecimal.valueOf(
                        ChronoUnit.DAYS.between(stock.getLastInTime(), LocalDateTime.now())));
            }
            messages.add(message);
        }

        return messages;
    }

    /**
     * 检测有效期预警
     */
    private List<AlertMessage> checkExpiry(AlertRule rule) {
        List<AlertMessage> messages = new ArrayList<>();

        Integer warningDays = rule.getThresholdValue().intValue();
        LocalDate warningDate = LocalDate.now().plusDays(warningDays);

        LambdaQueryWrapper<Stock> wrapper = buildStockWrapper(rule);
        wrapper.isNotNull(Stock::getExpiryDate)
               .le(Stock::getExpiryDate, warningDate)
               .gt(Stock::getExpiryDate, LocalDate.now());

        List<Stock> stocks = stockMapper.selectList(wrapper);

        for (Stock stock : stocks) {
            AlertMessage message = createAlertMessage(rule, stock);
            // 计算剩余天数
            long remainingDays = ChronoUnit.DAYS.between(LocalDate.now(), stock.getExpiryDate());
            message.setCurrentValue(BigDecimal.valueOf(remainingDays));
            messages.add(message);
        }

        return messages;
    }

    /**
     * 检测过期预警
     */
    private List<AlertMessage> checkExpired(AlertRule rule) {
        List<AlertMessage> messages = new ArrayList<>();

        LambdaQueryWrapper<Stock> wrapper = buildStockWrapper(rule);
        wrapper.isNotNull(Stock::getExpiryDate)
               .lt(Stock::getExpiryDate, LocalDate.now());

        List<Stock> stocks = stockMapper.selectList(wrapper);

        for (Stock stock : stocks) {
            AlertMessage message = createAlertMessage(rule, stock);
            message.setCurrentValue(BigDecimal.ZERO);
            messages.add(message);
        }

        return messages;
    }

    /**
     * 构建库存查询条件
     */
    private LambdaQueryWrapper<Stock> buildStockWrapper(AlertRule rule) {
        LambdaQueryWrapper<Stock> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(Stock::getStatus, "NORMAL")
               .eq(Stock::getIsDeleted, 0);

        if ("WAREHOUSE".equals(rule.getWarehouseScope())) {
            wrapper.eq(Stock::getWarehouseId, rule.getWarehouseId());
        }

        if ("MATERIAL".equals(rule.getMaterialScope())) {
            wrapper.eq(Stock::getMaterialId, rule.getMaterialId());
        } else if ("CATEGORY".equals(rule.getMaterialScope())) {
            // 根据物料类别查询
            wrapper.inSql(Stock::getMaterialId,
                    "SELECT id FROM md_material WHERE category_id = " + rule.getMaterialCategoryId());
        }

        return wrapper;
    }

    /**
     * 创建预警消息
     */
    private AlertMessage createAlertMessage(AlertRule rule, Stock stock) {
        AlertMessage message = new AlertMessage();
        message.setMessageNo(generateMessageNo());
        message.setRuleId(rule.getId());
        message.setRuleCode(rule.getRuleCode());
        message.setAlertType(rule.getAlertType());
        message.setAlertLevel(rule.getAlertLevel());
        message.setWarehouseId(stock.getWarehouseId());
        message.setWarehouseCode(stock.getWarehouseCode());
        message.setMaterialId(stock.getMaterialId());
        message.setMaterialCode(stock.getMaterialCode());
        message.setMaterialName(stock.getMaterialName());
        message.setBatchNo(stock.getBatchNo());
        message.setThresholdValue(rule.getThresholdValue());
        message.setGenerateTime(LocalDateTime.now());
        message.setStatus("PENDING");
        return message;
    }

    /**
     * 发送预警通知
     */
    private void sendNotification(AlertRule rule, AlertMessage message) {
        if (rule.getNotifyType() != null) {
            String[] notifyTypes = rule.getNotifyType().split(",");
            for (String type : notifyTypes) {
                switch (type.trim()) {
                    case "MESSAGE":
                        notifyService.sendSiteMessage(rule.getNotifyUsers(), message);
                        break;
                    case "EMAIL":
                        notifyService.sendEmail(rule.getNotifyUsers(), message);
                        break;
                    case "SMS":
                        notifyService.sendSms(rule.getNotifyUsers(), message);
                        break;
                }
            }
        }
    }

    /**
     * 生成预警消息编号
     */
    private String generateMessageNo() {
        return "AM" + System.currentTimeMillis();
    }
}
```

---

### 3.5 定时任务设计

#### 3.5.1 预警检测任务

```java
package com.autoerp.wm.job;

import com.autoerp.wm.service.AlertService;
import com.xxl.job.core.handler.annotation.XxlJob;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

/**
 * 库存预警检测任务
 */
@Slf4j
@Component
@RequiredArgsConstructor
public class AlertCheckJob {

    private final AlertService alertService;

    /**
     * 库存预警检测
     * 每小时执行一次
     */
    @XxlJob("alertCheckJob")
    public void execute() {
        log.info("====== 开始执行库存预警检测任务 ======");
        long startTime = System.currentTimeMillis();

        try {
            alertService.executeAlertCheck();
        } catch (Exception e) {
            log.error("库存预警检测任务执行失败", e);
        }

        long endTime = System.currentTimeMillis();
        log.info("====== 库存预警检测任务执行完成，耗时: {}ms ======", endTime - startTime);
    }
}
```

#### 3.5.2 库龄更新任务

```java
package com.autoerp.wm.job;

import com.autoerp.wm.mapper.VinStockMapper;
import com.xxl.job.core.handler.annotation.XxlJob;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

/**
 * 库龄更新任务
 */
@Slf4j
@Component
@RequiredArgsConstructor
public class StockDaysUpdateJob {

    private final VinStockMapper vinStockMapper;

    /**
     * 更新整车库龄
     * 每天凌晨执行
     */
    @XxlJob("stockDaysUpdateJob")
    public void execute() {
        log.info("====== 开始执行库龄更新任务 ======");

        // 更新所有未销售车辆的库龄
        vinStockMapper.updateStockDays();

        log.info("====== 库龄更新任务执行完成 ======");
    }
}
```

---

## 4. 数据访问层设计

### 4.1 Mapper接口设计

```java
package com.autoerp.wm.mapper;

import com.autoerp.wm.entity.Stock;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.*;

import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

/**
 * 库存Mapper
 */
@Mapper
public interface StockMapper extends BaseMapper<Stock> {

    /**
     * 查询物料库存汇总
     */
    @Select("SELECT material_id, material_code, material_name, " +
            "SUM(quantity) as total_qty, SUM(available_qty) as total_available_qty " +
            "FROM wm_stock " +
            "WHERE tenant_id = #{tenantId} AND material_code = #{materialCode} " +
            "AND is_deleted = 0 " +
            "GROUP BY material_id, material_code, material_name")
    Map<String, Object> selectMaterialSummary(@Param("tenantId") Long tenantId,
                                               @Param("materialCode") String materialCode);

    /**
     * 批量更新库存数量
     */
    @Update("<script>" +
            "<foreach collection='list' item='item' separator=';'>" +
            "UPDATE wm_stock SET " +
            "quantity = quantity + #{item.changeQty}, " +
            "available_qty = available_qty + #{item.changeQty}, " +
            "update_time = NOW() " +
            "WHERE id = #{item.stockId} AND tenant_id = #{item.tenantId}" +
            "</foreach>" +
            "</script>")
    int batchUpdateQuantity(@Param("list") List<StockUpdateDTO> list);

    /**
     * 锁定库存
     */
    @Update("UPDATE wm_stock SET " +
            "available_qty = available_qty - #{lockQty}, " +
            "locked_qty = locked_qty + #{lockQty}, " +
            "update_time = NOW() " +
            "WHERE id = #{stockId} AND available_qty >= #{lockQty} " +
            "AND tenant_id = #{tenantId}")
    int lockStock(@Param("stockId") Long stockId,
                  @Param("lockQty") BigDecimal lockQty,
                  @Param("tenantId") Long tenantId);

    /**
     * 查询库存明细用于导出
     */
    @Select("SELECT s.*, w.warehouse_name, l.location_name " +
            "FROM wm_stock s " +
            "LEFT JOIN wm_warehouse w ON s.warehouse_id = w.id " +
            "LEFT JOIN wm_location l ON s.location_id = l.id " +
            "WHERE s.tenant_id = #{tenantId} " +
            "AND s.is_deleted = 0 " +
            "ORDER BY s.warehouse_code, s.material_code")
    List<Map<String, Object>> selectStockForExport(@Param("tenantId") Long tenantId);
}
```

### 4.2 Mapper XML设计

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.autoerp.wm.mapper.StockMapper">

    <!-- 库存结果映射 -->
    <resultMap id="StockResultMap" type="com.autoerp.wm.entity.Stock">
        <id column="id" property="id"/>
        <result column="warehouse_id" property="warehouseId"/>
        <result column="warehouse_code" property="warehouseCode"/>
        <result column="zone_id" property="zoneId"/>
        <result column="zone_code" property="zoneCode"/>
        <result column="location_id" property="locationId"/>
        <result column="location_code" property="locationCode"/>
        <result column="material_id" property="materialId"/>
        <result column="material_code" property="materialCode"/>
        <result column="material_name" property="materialName"/>
        <result column="batch_no" property="batchNo"/>
        <result column="vin_code" property="vinCode"/>
        <result column="quantity" property="quantity"/>
        <result column="available_qty" property="availableQty"/>
        <result column="locked_qty" property="lockedQty"/>
        <result column="inspect_qty" property="inspectQty"/>
        <result column="status" property="status"/>
        <result column="production_date" property="productionDate"/>
        <result column="expiry_date" property="expiryDate"/>
        <result column="tenant_id" property="tenantId"/>
        <result column="create_time" property="createTime"/>
        <result column="update_time" property="updateTime"/>
    </resultMap>

    <!-- 分页查询库存 -->
    <select id="selectStockPage" resultMap="StockResultMap">
        SELECT s.*, w.warehouse_name, z.zone_name, l.location_name
        FROM wm_stock s
        LEFT JOIN wm_warehouse w ON s.warehouse_id = w.id AND w.is_deleted = 0
        LEFT JOIN wm_zone z ON s.zone_id = z.id AND z.is_deleted = 0
        LEFT JOIN wm_location l ON s.location_id = l.id AND l.is_deleted = 0
        WHERE s.tenant_id = #{tenantId}
        AND s.is_deleted = 0
        <if test="warehouseId != null">
            AND s.warehouse_id = #{warehouseId}
        </if>
        <if test="materialCode != null and materialCode != ''">
            AND s.material_code LIKE CONCAT('%', #{materialCode}, '%')
        </if>
        <if test="materialName != null and materialName != ''">
            AND s.material_name LIKE CONCAT('%', #{materialName}, '%')
        </if>
        <if test="batchNo != null and batchNo != ''">
            AND s.batch_no = #{batchNo}
        </if>
        <if test="status != null and status != ''">
            AND s.status = #{status}
        </if>
        ORDER BY s.update_time DESC
    </select>

    <!-- 查询库存流水统计 -->
    <select id="selectStockLogStats" resultType="map">
        SELECT
            trans_type,
            COUNT(*) as trans_count,
            SUM(quantity) as total_qty
        FROM wm_stock_log
        WHERE tenant_id = #{tenantId}
        AND oper_time BETWEEN #{startTime} AND #{endTime}
        GROUP BY trans_type
    </select>

</mapper>
```

---

## 5. 缓存设计

### 5.1 缓存策略

| 缓存类型 | Key格式 | 过期时间 | 说明 |
|----------|---------|----------|------|
| 仓库信息 | warehouse:{id} | 24小时 | 仓库基础信息 |
| 库位信息 | location:{id} | 24小时 | 库位基础信息 |
| 物料库存 | stock:{warehouseId}:{materialId}:{batchNo} | 5分钟 | 实时库存 |
| 库存汇总 | stock:summary:{materialCode} | 5分钟 | 物料库存汇总 |
| 条码信息 | barcode:{barcode} | 1小时 | 条码解析结果 |

### 5.2 缓存实现

```java
package com.autoerp.wm.service.impl;

import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Component;
import lombok.RequiredArgsConstructor;

import java.util.concurrent.TimeUnit;

/**
 * 库存缓存服务
 */
@Component
@RequiredArgsConstructor
public class StockCacheService {

    private final RedisTemplate<String, Object> redisTemplate;

    private static final String STOCK_KEY_PREFIX = "stock:";
    private static final String STOCK_SUMMARY_KEY_PREFIX = "stock:summary:";
    private static final long STOCK_CACHE_EXPIRE = 5; // 5分钟

    /**
     * 获取库存（带缓存）
     */
    public Stock getStockWithCache(Long warehouseId, Long materialId, String batchNo) {
        String key = buildStockKey(warehouseId, materialId, batchNo);

        Stock stock = (Stock) redisTemplate.opsForValue().get(key);
        if (stock == null) {
            // 从数据库查询
            stock = stockMapper.selectOne(...);
            if (stock != null) {
                redisTemplate.opsForValue().set(key, stock, STOCK_CACHE_EXPIRE, TimeUnit.MINUTES);
            }
        }
        return stock;
    }

    /**
     * 清除库存缓存
     */
    public void evictStockCache(Long warehouseId, Long materialId, String batchNo) {
        String key = buildStockKey(warehouseId, materialId, batchNo);
        redisTemplate.delete(key);

        // 同时清除汇总缓存
        String summaryKey = STOCK_SUMMARY_KEY_PREFIX + materialId;
        redisTemplate.delete(summaryKey);
    }

    /**
     * 构建库存缓存Key
     */
    private String buildStockKey(Long warehouseId, Long materialId, String batchNo) {
        return STOCK_KEY_PREFIX + warehouseId + ":" + materialId + ":" +
               (batchNo != null ? batchNo : "null");
    }
}
```

---

## 6. 事务设计

### 6.1 事务边界

| 操作类型 | 事务范围 | 隔离级别 |
|----------|----------|----------|
| 入库确认 | 入库单更新 + 库存更新 + 流水记录 | READ_COMMITTED |
| 出库确认 | 出库单更新 + 库存扣减 + 流水记录 | READ_COMMITTED |
| 库存盘点 | 盘点单更新 + 库存调整 | READ_COMMITTED |
| 调拨执行 | 调出扣减 + 调入增加 | READ_COMMITTED |

### 6.2 分布式事务

对于跨服务的操作（如入库后更新采购订单状态），使用消息队列实现最终一致性。

```java
/**
 * 入库完成事件监听
 */
@Component
@RequiredArgsConstructor
public class InboundEventListener {

    private final PurchaseOrderClient purchaseOrderClient;
    private final RocketMQTemplate rocketMQTemplate;

    @EventListener
    @Async
    public void onInboundComplete(InboundCompleteEvent event) {
        InboundOrder inboundOrder = event.getInboundOrder();

        // 如果是采购入库，更新采购订单入库状态
        if ("RK01".equals(inboundOrder.getOrderType())) {
            // 发送消息到采购服务
            InboundMessage message = new InboundMessage();
            message.setPoOrderId(inboundOrder.getSourceOrderId());
            message.setPoOrderNo(inboundOrder.getSourceOrderNo());
            message.setInboundOrderNo(inboundOrder.getOrderNo());
            message.setInboundDate(inboundOrder.getInboundDate());

            rocketMQTemplate.asyncSend("purchase-inbound-topic", message, new SendCallback() {
                @Override
                public void onSuccess(SendResult sendResult) {
                    log.info("入库消息发送成功: {}", message);
                }

                @Override
                public void onException(Throwable e) {
                    log.error("入库消息发送失败: {}", message, e);
                }
            });
        }
    }
}
```

---

## 7. 性能优化设计

### 7.1 数据库优化

1. **索引优化**
   - 所有查询条件字段建立索引
   - 组合索引遵循最左匹配原则
   - 定期分析索引使用情况

2. **分库分表**
   - 流水表按月分表
   - 历史数据归档

3. **读写分离**
   - 主库负责写操作
   - 从库负责读操作

### 7.2 应用优化

1. **批量操作**
   - 入库明细批量插入
   - 库存流水批量记录

2. **异步处理**
   - 预警检测异步执行
   - 消息通知异步发送

3. **缓存使用**
   - 热点数据缓存
   - 查询结果缓存

---

## 8. 安全设计

### 8.1 权限控制

| 权限编码 | 说明 |
|----------|------|
| wm:stock:list | 库存查询 |
| wm:stock:export | 库存导出 |
| wm:inbound:create | 入库创建 |
| wm:inbound:approve | 入库审核 |
| wm:outbound:create | 出库创建 |
| wm:outbound:approve | 出库审核 |
| wm:location:manage | 库位管理 |
| wm:alert:manage | 预警管理 |

### 8.2 数据权限

- 用户只能查看有权限的仓库数据
- 操作日志记录所有关键操作
- 敏感数据加密存储

---

## 附录

### 附录A：类图

```
┌─────────────────────┐
│   StockController   │
└──────────┬──────────┘
           │
           v
┌─────────────────────┐     ┌─────────────────────┐
│    StockService     │────>│    StockMapper      │
└──────────┬──────────┘     └─────────────────────┘
           │
           v
┌─────────────────────┐
│     Stock实体       │
└─────────────────────┘
```

### 附录B：时序图

```
入库流程时序图:

用户          Controller       Service          Mapper          数据库
 │               │               │               │               │
 │──创建入库单──>│               │               │               │
 │               │──create()────>│               │               │
 │               │               │──insert()────>│               │
 │               │               │               │──INSERT─────>│
 │               │               │               │<───────OK────│
 │               │               │<─────OK───────│               │
 │               │<─────id───────│               │               │
 │<─────成功─────│               │               │               │
 │               │               │               │               │
 │──确认入库────>│               │               │               │
 │               │──confirm()───>│               │               │
 │               │               │──更新库存────>│               │
 │               │               │               │──UPDATE─────>│
 │               │               │               │<───────OK────│
 │               │               │──记录流水────>│               │
 │               │               │               │──INSERT─────>│
 │               │               │               │<───────OK────│
 │               │               │<─────OK───────│               │
 │               │<─────OK───────│               │               │
 │<─────成功─────│               │               │               │
```

---

**文档审批**

| 角色 | 姓名 | 审批日期 | 签名 |
|------|------|----------|------|
| 架构师 | | | |
| 技术负责人 | | | |
| 开发负责人 | | | |