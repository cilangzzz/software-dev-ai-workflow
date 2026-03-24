# 财务管理模块(FI/CO) 详细设计文档

**文档版本**: V1.0
**创建日期**: 2026-03-24
**文档编号**: Detail-05
**关联PRD**: PRD-05-财务管理模块
**技术栈**: Spring Boot 2.7 + MyBatis Plus

---

## 1. 文档概述

### 1.1 文档目的
本文档详细描述财务管理模块的技术实现方案，包括系统架构、模块设计、类设计、核心算法和接口设计。

### 1.2 技术选型

| 技术 | 版本 | 说明 |
|------|------|------|
| Spring Boot | 2.7.x | 应用框架 |
| MyBatis Plus | 3.5.x | ORM框架 |
| MySQL | 8.x | 关系数据库 |
| Redis | 7.x | 缓存数据库 |
| Spring Security | 2.7.x | 安全框架 |
| Spring Cloud | 2021.x | 微服务框架 |

---

## 2. 系统架构设计

### 2.1 整体架构

```
┌─────────────────────────────────────────────────────────────────┐
│                         前端应用层                               │
│                    (Vue.js / React SPA)                         │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                        API网关层                                 │
│                    (Spring Cloud Gateway)                       │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                       业务服务层                                 │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐       │
│  │ 总账服务  │ │ 应收服务  │ │ 应付服务  │ │ 资产服务  │       │
│  │   (FI)   │ │   (AR)   │ │   (AP)   │ │   (FA)   │         │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘       │
│  ┌───────────┐ ┌───────────┐                                   │
│  │ 资金服务  │ │ 报表服务  │                                   │
│  │   (TR)   │ │   (FR)   │                                     │
│  └───────────┘ └───────────┘                                   │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                       基础服务层                                 │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐       │
│  │ 认证服务  │ │ 租户服务  │ │ 消息服务  │ │ 文件服务  │       │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘       │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                       数据存储层                                 │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐                     │
│  │  MySQL    │ │   Redis   │ │   OSS     │                     │
│  │  (主库)   │ │  (缓存)   │ │ (文件)    │                     │
│  └───────────┘ └───────────┘ └───────────┘                     │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 模块依赖关系

```
                    ┌───────────┐
                    │  财务报表  │
                    │   (FR)   │
                    └─────┬─────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌───────────┐      ┌───────────┐      ┌───────────┐
│  总账管理  │◄────│  应收管理  │      │  资金管理  │
│   (FI)   │◄────│   (AR)   │      │   (TR)   │
└─────┬─────┘      └───────────┘      └───────────┘
      │                                   ▲
      │           ┌───────────┐           │
      └──────────►│  应付管理  │───────────┘
                  │   (AP)   │
                  └─────┬─────┘
                        │
                        ▼
                  ┌───────────┐
                  │ 固定资产  │
                  │   (FA)   │
                  └───────────┘
```

---

## 3. 包结构设计

### 3.1 总账模块包结构

```
com.autoerp.fi
├── controller                 # 控制器层
│   ├── AccountController.java
│   ├── VoucherController.java
│   ├── LedgerController.java
│   └── PeriodController.java
├── service                    # 服务层
│   ├── AccountService.java
│   ├── VoucherService.java
│   ├── LedgerService.java
│   ├── PeriodService.java
│   └── impl
│       ├── AccountServiceImpl.java
│       ├── VoucherServiceImpl.java
│       ├── LedgerServiceImpl.java
│       └── PeriodServiceImpl.java
├── mapper                     # 数据访问层
│   ├── AccountMapper.java
│   ├── VoucherMapper.java
│   ├── VoucherDetailMapper.java
│   ├── AccountBalanceMapper.java
│   └── PeriodMapper.java
├── entity                     # 实体类
│   ├── FiAccount.java
│   ├── FiVoucher.java
│   ├── FiVoucherDetail.java
│   ├── FiAccountBalance.java
│   └── FiPeriod.java
├── dto                        # 数据传输对象
│   ├── AccountDTO.java
│   ├── VoucherDTO.java
│   ├── VoucherDetailDTO.java
│   ├── LedgerDTO.java
│   └── BalanceDTO.java
├── vo                         # 视图对象
│   ├── AccountTreeVO.java
│   ├── VoucherVO.java
│   ├── VoucherDetailVO.java
│   └── BalanceVO.java
├── converter                  # 对象转换器
│   ├── AccountConverter.java
│   └── VoucherConverter.java
├── enums                      # 枚举类
│   ├── AccountTypeEnum.java
│   ├── BalanceDirectionEnum.java
│   ├── VoucherStatusEnum.java
│   └── PeriodStatusEnum.java
├── event                      # 事件类
│   ├── VoucherAuditEvent.java
│   ├── VoucherPostEvent.java
│   └── PeriodCloseEvent.java
├── listener                   # 事件监听器
│   ├── VoucherEventListener.java
│   └── PeriodEventListener.java
├── task                       # 定时任务
│   └── PeriodCheckTask.java
└── util                       # 工具类
    ├── VoucherNoGenerator.java
    └── BalanceCalculator.java
```

---

## 4. 核心类设计

### 4.1 凭证服务类设计

#### 4.1.1 VoucherService接口

```java
package com.autoerp.fi.service;

import com.autoerp.common.dto.PageResult;
import com.autoerp.fi.dto.VoucherDTO;
import com.autoerp.fi.dto.VoucherQueryDTO;
import com.autoerp.fi.entity.FiVoucher;
import com.autoerp.fi.vo.VoucherVO;

import java.util.List;

/**
 * 凭证服务接口
 */
public interface VoucherService {

    /**
     * 分页查询凭证
     */
    PageResult<VoucherVO> queryVoucherPage(VoucherQueryDTO queryDTO);

    /**
     * 查询凭证明细
     */
    VoucherVO getVoucherDetail(Long voucherId);

    /**
     * 新增凭证
     */
    Long createVoucher(VoucherDTO voucherDTO);

    /**
     * 修改凭证
     */
    void updateVoucher(Long voucherId, VoucherDTO voucherDTO);

    /**
     * 删除凭证
     */
    void deleteVoucher(Long voucherId);

    /**
     * 审核凭证
     */
    void auditVoucher(Long voucherId, Integer auditResult, String auditRemark);

    /**
     * 批量审核凭证
     */
    void batchAuditVoucher(List<Long> voucherIds, Integer auditResult);

    /**
     * 记账凭证
     */
    void postVoucher(Long voucherId);

    /**
     * 批量记账凭证
     */
    void batchPostVoucher(List<Long> voucherIds);

    /**
     * 红冲凭证
     */
    Long redVoucher(Long voucherId, Long redAmount, String remark);

    /**
     * 校验借贷平衡
     */
    boolean validateBalance(VoucherDTO voucherDTO);

    /**
     * 生成凭证号
     */
    Integer generateVoucherNo(String voucherWord, Integer fiscalYear, Integer periodNum);
}
```

---

#### 4.1.2 VoucherServiceImpl实现类

```java
package com.autoerp.fi.service.impl;

import com.autoerp.common.constant.Constants;
import com.autoerp.common.exception.BusinessException;
import com.autoerp.common.utils.SecurityUtils;
import com.autoerp.fi.converter.VoucherConverter;
import com.autoerp.fi.dto.VoucherDTO;
import com.autoerp.fi.dto.VoucherDetailDTO;
import com.autoerp.fi.dto.VoucherQueryDTO;
import com.autoerp.fi.entity.FiAccount;
import com.autoerp.fi.entity.FiPeriod;
import com.autoerp.fi.entity.FiVoucher;
import com.autoerp.fi.entity.FiVoucherDetail;
import com.autoerp.fi.enums.VoucherStatusEnum;
import com.autoerp.fi.enums.PeriodStatusEnum;
import com.autoerp.fi.mapper.*;
import com.autoerp.fi.service.*;
import com.autoerp.fi.vo.VoucherVO;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.context.ApplicationEventPublisher;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Objects;

/**
 * 凭证服务实现类
 */
@Slf4j
@Service
@RequiredArgsConstructor
public class VoucherServiceImpl extends ServiceImpl<VoucherMapper, FiVoucher>
        implements VoucherService {

    private final VoucherDetailMapper voucherDetailMapper;
    private final AccountMapper accountMapper;
    private final PeriodMapper periodMapper;
    private final AccountBalanceService accountBalanceService;
    private final VoucherConverter voucherConverter;
    private final ApplicationEventPublisher eventPublisher;

    @Override
    public PageResult<VoucherVO> queryVoucherPage(VoucherQueryDTO queryDTO) {
        Page<FiVoucher> page = new Page<>(queryDTO.getPageNum(), queryDTO.getPageSize());

        LambdaQueryWrapper<FiVoucher> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(queryDTO.getFiscalYear() != null, FiVoucher::getFiscalYear, queryDTO.getFiscalYear())
               .eq(queryDTO.getPeriodNum() != null, FiVoucher::getPeriodNum, queryDTO.getPeriodNum())
               .eq(queryDTO.getStatus() != null, FiVoucher::getStatus, queryDTO.getStatus())
               .like(queryDTO.getVoucherNo() != null, FiVoucher::getVoucherNo, queryDTO.getVoucherNo())
               .between(queryDTO.getVoucherDateStart() != null, FiVoucher::getVoucherDate,
                        queryDTO.getVoucherDateStart(), queryDTO.getVoucherDateEnd())
               .orderByDesc(FiVoucher::getCreateTime);

        Page<FiVoucher> result = this.page(page, wrapper);

        List<VoucherVO> voList = voucherConverter.toVOList(result.getRecords());
        return new PageResult<>(voList, result.getTotal(), result.getCurrent(), result.getSize());
    }

    @Override
    public VoucherVO getVoucherDetail(Long voucherId) {
        FiVoucher voucher = this.getById(voucherId);
        if (voucher == null) {
            throw new BusinessException("凭证不存在");
        }

        VoucherVO vo = voucherConverter.toVO(voucher);

        // 查询凭证分录
        LambdaQueryWrapper<FiVoucherDetail> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(FiVoucherDetail::getVoucherId, voucherId)
               .orderByAsc(FiVoucherDetail::getEntryNo);
        List<FiVoucherDetail> details = voucherDetailMapper.selectList(wrapper);

        vo.setEntries(voucherConverter.toDetailVOList(details));
        return vo;
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long createVoucher(VoucherDTO voucherDTO) {
        // 1. 校验借贷平衡
        if (!validateBalance(voucherDTO)) {
            throw new BusinessException("借贷不平衡，请检查凭证金额");
        }

        // 2. 校验会计期间
        FiPeriod period = periodMapper.selectById(voucherDTO.getPeriodId());
        if (period == null || period.getStatus() != PeriodStatusEnum.OPEN.getCode()) {
            throw new BusinessException("会计期间未开放或已结账");
        }

        // 3. 校验科目是否存在且启用
        validateAccounts(voucherDTO.getEntries());

        // 4. 生成凭证号
        Integer voucherNo = generateVoucherNo(voucherDTO.getVoucherWord(),
                voucherDTO.getFiscalYear(), voucherDTO.getPeriodNum());

        // 5. 创建凭证头
        FiVoucher voucher = voucherConverter.toEntity(voucherDTO);
        voucher.setVoucherNo(voucherNo);
        voucher.setStatus(VoucherStatusEnum.DRAFT.getCode());
        voucher.setMakeBy(SecurityUtils.getUserId());
        voucher.setMakeTime(LocalDateTime.now());
        voucher.setTenantId(SecurityUtils.getTenantId());

        // 计算借贷金额
        BigDecimal debitAmount = BigDecimal.ZERO;
        BigDecimal creditAmount = BigDecimal.ZERO;
        for (VoucherDetailDTO detail : voucherDTO.getEntries()) {
            debitAmount = debitAmount.add(detail.getDebitAmount() != null ? detail.getDebitAmount() : BigDecimal.ZERO);
            creditAmount = creditAmount.add(detail.getCreditAmount() != null ? detail.getCreditAmount() : BigDecimal.ZERO);
        }
        voucher.setDebitAmount(debitAmount);
        voucher.setCreditAmount(creditAmount);
        voucher.setEntryCount(voucherDTO.getEntries().size());

        this.save(voucher);

        // 6. 保存凭证明细
        saveVoucherDetails(voucher.getId(), voucherDTO.getEntries());

        log.info("凭证创建成功，凭证ID: {}, 凭证号: {}", voucher.getId(), voucherNo);
        return voucher.getId();
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void updateVoucher(Long voucherId, VoucherDTO voucherDTO) {
        FiVoucher voucher = this.getById(voucherId);
        if (voucher == null) {
            throw new BusinessException("凭证不存在");
        }

        // 校验状态，只有制单状态可修改
        if (voucher.getStatus() != VoucherStatusEnum.DRAFT.getCode()) {
            throw new BusinessException("凭证已审核，不可修改");
        }

        // 校验借贷平衡
        if (!validateBalance(voucherDTO)) {
            throw new BusinessException("借贷不平衡，请检查凭证金额");
        }

        // 更新凭证头
        voucherConverter.updateEntity(voucher, voucherDTO);

        BigDecimal debitAmount = BigDecimal.ZERO;
        BigDecimal creditAmount = BigDecimal.ZERO;
        for (VoucherDetailDTO detail : voucherDTO.getEntries()) {
            debitAmount = debitAmount.add(detail.getDebitAmount() != null ? detail.getDebitAmount() : BigDecimal.ZERO);
            creditAmount = creditAmount.add(detail.getCreditAmount() != null ? detail.getCreditAmount() : BigDecimal.ZERO);
        }
        voucher.setDebitAmount(debitAmount);
        voucher.setCreditAmount(creditAmount);
        voucher.setEntryCount(voucherDTO.getEntries().size());

        this.updateById(voucher);

        // 删除原明细，保存新明细
        voucherDetailMapper.deleteByVoucherId(voucherId);
        saveVoucherDetails(voucherId, voucherDTO.getEntries());

        log.info("凭证修改成功，凭证ID: {}", voucherId);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void deleteVoucher(Long voucherId) {
        FiVoucher voucher = this.getById(voucherId);
        if (voucher == null) {
            throw new BusinessException("凭证不存在");
        }

        // 只有制单状态可删除
        if (voucher.getStatus() != VoucherStatusEnum.DRAFT.getCode()) {
            throw new BusinessException("凭证已审核，不可删除");
        }

        // 删除明细
        voucherDetailMapper.deleteByVoucherId(voucherId);

        // 删除凭证
        this.removeById(voucherId);

        log.info("凭证删除成功，凭证ID: {}", voucherId);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void auditVoucher(Long voucherId, Integer auditResult, String auditRemark) {
        FiVoucher voucher = this.getById(voucherId);
        if (voucher == null) {
            throw new BusinessException("凭证不存在");
        }

        // 只有待审核状态可审核
        if (voucher.getStatus() != VoucherStatusEnum.DRAFT.getCode()) {
            throw new BusinessException("凭证状态不正确");
        }

        // 制单人不能审核自己的凭证
        if (Objects.equals(voucher.getMakeBy(), SecurityUtils.getUserId())) {
            throw new BusinessException("制单人不能审核自己的凭证");
        }

        if (auditResult == 1) {
            // 审核通过
            voucher.setStatus(VoucherStatusEnum.AUDITED.getCode());
            voucher.setAuditBy(SecurityUtils.getUserId());
            voucher.setAuditTime(LocalDateTime.now());
        } else {
            // 审核驳回
            voucher.setStatus(VoucherStatusEnum.REJECTED.getCode());
        }

        this.updateById(voucher);

        // 发布审核事件
        eventPublisher.publishEvent(new VoucherAuditEvent(voucherId, auditResult, auditRemark));

        log.info("凭证审核完成，凭证ID: {}, 结果: {}", voucherId, auditResult);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void postVoucher(Long voucherId) {
        FiVoucher voucher = this.getById(voucherId);
        if (voucher == null) {
            throw new BusinessException("凭证不存在");
        }

        // 只有已审核状态可记账
        if (voucher.getStatus() != VoucherStatusEnum.AUDITED.getCode()) {
            throw new BusinessException("凭证未审核，不可记账");
        }

        // 更新科目余额
        accountBalanceService.updateBalanceByVoucher(voucherId);

        // 更新凭证状态
        voucher.setStatus(VoucherStatusEnum.POSTED.getCode());
        voucher.setPostBy(SecurityUtils.getUserId());
        voucher.setPostTime(LocalDateTime.now());

        this.updateById(voucher);

        // 发布记账事件
        eventPublisher.publishEvent(new VoucherPostEvent(voucherId));

        log.info("凭证记账成功，凭证ID: {}", voucherId);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long redVoucher(Long voucherId, Long redAmount, String remark) {
        FiVoucher originalVoucher = this.getById(voucherId);
        if (originalVoucher == null) {
            throw new BusinessException("原凭证不存在");
        }

        // 只有已记账凭证可红冲
        if (originalVoucher.getStatus() != VoucherStatusEnum.POSTED.getCode()) {
            throw new BusinessException("凭证未记账，不可红冲");
        }

        // 查询原凭证明细
        LambdaQueryWrapper<FiVoucherDetail> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(FiVoucherDetail::getVoucherId, voucherId);
        List<FiVoucherDetail> originalDetails = voucherDetailMapper.selectList(wrapper);

        // 创建红冲凭证
        FiVoucher redVoucher = new FiVoucher();
        redVoucher.setVoucherWord(originalVoucher.getVoucherWord());
        redVoucher.setVoucherDate(LocalDateTime.now().toLocalDate());
        redVoucher.setFiscalYear(originalVoucher.getFiscalYear());
        redVoucher.setPeriodNum(originalVoucher.getPeriodNum());
        redVoucher.setPeriodId(originalVoucher.getPeriodId());
        redVoucher.setDebitAmount(originalVoucher.getDebitAmount().negate());
        redVoucher.setCreditAmount(originalVoucher.getCreditAmount().negate());
        redVoucher.setEntryCount(originalVoucher.getEntryCount());
        redVoucher.setStatus(VoucherStatusEnum.DRAFT.getCode());
        redVoucher.setRedVoucherId(voucherId);
        redVoucher.setIsRed(1);
        redVoucher.setRemark(remark);
        redVoucher.setMakeBy(SecurityUtils.getUserId());
        redVoucher.setMakeTime(LocalDateTime.now());
        redVoucher.setTenantId(SecurityUtils.getTenantId());

        // 生成凭证号
        Integer voucherNo = generateVoucherNo(originalVoucher.getVoucherWord(),
                originalVoucher.getFiscalYear(), originalVoucher.getPeriodNum());
        redVoucher.setVoucherNo(voucherNo);

        this.save(redVoucher);

        // 创建红冲明细（金额取负）
        int entryNo = 1;
        for (FiVoucherDetail originalDetail : originalDetails) {
            FiVoucherDetail redDetail = new FiVoucherDetail();
            redDetail.setVoucherId(redVoucher.getId());
            redDetail.setEntryNo(entryNo++);
            redDetail.setAccountId(originalDetail.getAccountId());
            redDetail.setAccountCode(originalDetail.getAccountCode());
            redDetail.setAccountName(originalDetail.getAccountName());
            redDetail.setSummary("红冲-" + originalDetail.getSummary());
            redDetail.setDebitAmount(originalDetail.getDebitAmount() != null ?
                    originalDetail.getDebitAmount().negate() : BigDecimal.ZERO);
            redDetail.setCreditAmount(originalDetail.getCreditAmount() != null ?
                    originalDetail.getCreditAmount().negate() : BigDecimal.ZERO);
            redDetail.setTenantId(SecurityUtils.getTenantId());

            voucherDetailMapper.insert(redDetail);
        }

        log.info("凭证红冲成功，原凭证ID: {}, 红冲凭证ID: {}", voucherId, redVoucher.getId());
        return redVoucher.getId();
    }

    @Override
    public boolean validateBalance(VoucherDTO voucherDTO) {
        BigDecimal totalDebit = BigDecimal.ZERO;
        BigDecimal totalCredit = BigDecimal.ZERO;

        for (VoucherDetailDTO detail : voucherDTO.getEntries()) {
            if (detail.getDebitAmount() != null) {
                totalDebit = totalDebit.add(detail.getDebitAmount());
            }
            if (detail.getCreditAmount() != null) {
                totalCredit = totalCredit.add(detail.getCreditAmount());
            }
        }

        return totalDebit.compareTo(totalCredit) == 0;
    }

    @Override
    public Integer generateVoucherNo(String voucherWord, Integer fiscalYear, Integer periodNum) {
        return baseMapper.selectMaxVoucherNo(SecurityUtils.getTenantId(),
                fiscalYear, periodNum, voucherWord) + 1;
    }

    /**
     * 保存凭证明细
     */
    private void saveVoucherDetails(Long voucherId, List<VoucherDetailDTO> details) {
        int entryNo = 1;
        for (VoucherDetailDTO detailDTO : details) {
            FiVoucherDetail detail = voucherConverter.toDetailEntity(detailDTO);
            detail.setVoucherId(voucherId);
            detail.setEntryNo(entryNo++);
            detail.setTenantId(SecurityUtils.getTenantId());
            voucherDetailMapper.insert(detail);
        }
    }

    /**
     * 校验科目
     */
    private void validateAccounts(List<VoucherDetailDTO> details) {
        for (VoucherDetailDTO detail : details) {
            FiAccount account = accountMapper.selectByCode(detail.getAccountCode());
            if (account == null) {
                throw new BusinessException("科目不存在: " + detail.getAccountCode());
            }
            if (account.getIsEnabled() != 1) {
                throw new BusinessException("科目已停用: " + detail.getAccountCode());
            }
            if (account.getIsLeaf() != 1) {
                throw new BusinessException("科目不是末级科目: " + detail.getAccountCode());
            }
        }
    }
}
```

---

### 4.2 科目余额服务类设计

#### 4.2.1 AccountBalanceService接口

```java
package com.autoerp.fi.service;

import com.autoerp.fi.dto.BalanceDTO;
import com.autoerp.fi.dto.BalanceQueryDTO;
import com.autoerp.fi.vo.BalanceVO;

import java.math.BigDecimal;
import java.util.List;

/**
 * 科目余额服务接口
 */
public interface AccountBalanceService {

    /**
     * 查询科目余额表
     */
    List<BalanceVO> queryBalanceList(BalanceQueryDTO queryDTO);

    /**
     * 查询科目余额
     */
    BalanceVO getBalance(Long accountId, Integer fiscalYear, Integer periodNum);

    /**
     * 更新科目余额（凭证记账时调用）
     */
    void updateBalanceByVoucher(Long voucherId);

    /**
     * 初始化科目余额
     */
    void initBalance(Long accountId, Integer fiscalYear, BigDecimal beginDebit, BigDecimal beginCredit);

    /**
     * 结转余额到下一期间
     */
    void carryForwardBalance(Integer fiscalYear, Integer periodNum);

    /**
     * 试算平衡检查
     */
    boolean checkTrialBalance(Integer fiscalYear, Integer periodNum);
}
```

---

#### 4.2.2 AccountBalanceServiceImpl实现类

```java
package com.autoerp.fi.service.impl;

import com.autoerp.common.exception.BusinessException;
import com.autoerp.common.utils.SecurityUtils;
import com.autoerp.fi.dto.BalanceDTO;
import com.autoerp.fi.dto.BalanceQueryDTO;
import com.autoerp.fi.entity.FiAccount;
import com.autoerp.fi.entity.FiAccountBalance;
import com.autoerp.fi.entity.FiVoucher;
import com.autoerp.fi.entity.FiVoucherDetail;
import com.autoerp.fi.mapper.AccountBalanceMapper;
import com.autoerp.fi.mapper.AccountMapper;
import com.autoerp.fi.mapper.VoucherDetailMapper;
import com.autoerp.fi.mapper.VoucherMapper;
import com.autoerp.fi.service.AccountBalanceService;
import com.autoerp.fi.vo.BalanceVO;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * 科目余额服务实现类
 */
@Slf4j
@Service
@RequiredArgsConstructor
public class AccountBalanceServiceImpl implements AccountBalanceService {

    private final AccountBalanceMapper accountBalanceMapper;
    private final AccountMapper accountMapper;
    private final VoucherMapper voucherMapper;
    private final VoucherDetailMapper voucherDetailMapper;

    @Override
    public List<BalanceVO> queryBalanceList(BalanceQueryDTO queryDTO) {
        return accountBalanceMapper.selectBalanceList(
                SecurityUtils.getTenantId(),
                queryDTO.getFiscalYear(),
                queryDTO.getPeriodNum(),
                queryDTO.getAccountCodeStart(),
                queryDTO.getAccountCodeEnd(),
                queryDTO.getAccountLevel(),
                queryDTO.getShowLeaf()
        );
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void updateBalanceByVoucher(Long voucherId) {
        // 1. 查询凭证
        FiVoucher voucher = voucherMapper.selectById(voucherId);
        if (voucher == null) {
            throw new BusinessException("凭证不存在");
        }

        // 2. 查询凭证分录
        LambdaQueryWrapper<FiVoucherDetail> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(FiVoucherDetail::getVoucherId, voucherId);
        List<FiVoucherDetail> details = voucherDetailMapper.selectList(wrapper);

        // 3. 按科目+辅助核算分组汇总
        Map<String, List<FiVoucherDetail>> groupedDetails = details.stream()
                .collect(Collectors.groupingBy(this::getBalanceKey));

        // 4. 更新各科目余额
        for (Map.Entry<String, List<FiVoucherDetail>> entry : groupedDetails.entrySet()) {
            List<FiVoucherDetail> detailList = entry.getValue();

            // 计算借贷金额
            BigDecimal debitAmount = detailList.stream()
                    .map(d -> d.getDebitAmount() != null ? d.getDebitAmount() : BigDecimal.ZERO)
                    .reduce(BigDecimal.ZERO, BigDecimal::add);

            BigDecimal creditAmount = detailList.stream()
                    .map(d -> d.getCreditAmount() != null ? d.getCreditAmount() : BigDecimal.ZERO)
                    .reduce(BigDecimal.ZERO, BigDecimal::add);

            FiVoucherDetail firstDetail = detailList.get(0);

            // 更新余额
            updateBalance(
                    firstDetail.getAccountId(),
                    voucher.getFiscalYear(),
                    voucher.getPeriodNum(),
                    debitAmount,
                    creditAmount,
                    firstDetail.getAuxCustomerId(),
                    firstDetail.getAuxSupplierId(),
                    firstDetail.getAuxDepartmentId(),
                    firstDetail.getAuxProjectId(),
                    firstDetail.getAuxEmployeeId(),
                    firstDetail.getAuxItemId()
            );
        }

        log.info("凭证余额更新完成，凭证ID: {}", voucherId);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void initBalance(Long accountId, Integer fiscalYear, BigDecimal beginDebit, BigDecimal beginCredit) {
        FiAccount account = accountMapper.selectById(accountId);
        if (account == null) {
            throw new BusinessException("科目不存在");
        }

        // 检查是否已存在
        FiAccountBalance existBalance = accountBalanceMapper.selectByAccount(
                SecurityUtils.getTenantId(), fiscalYear, 1, accountId);

        if (existBalance != null) {
            throw new BusinessException("科目余额已初始化");
        }

        // 创建第1期余额记录
        FiAccountBalance balance = new FiAccountBalance();
        balance.setTenantId(SecurityUtils.getTenantId());
        balance.setFiscalYear(fiscalYear);
        balance.setPeriodNum(1);
        balance.setAccountId(accountId);
        balance.setAccountCode(account.getAccountCode());
        balance.setBeginDebit(beginDebit);
        balance.setBeginCredit(beginCredit);
        balance.setEndDebit(beginDebit);
        balance.setEndCredit(beginCredit);
        balance.setYearDebit(beginDebit);
        balance.setYearCredit(beginCredit);

        accountBalanceMapper.insert(balance);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public void carryForwardBalance(Integer fiscalYear, Integer periodNum) {
        // 查询本期余额
        List<FiAccountBalance> currentBalances = accountBalanceMapper.selectList(
                new LambdaQueryWrapper<FiAccountBalance>()
                        .eq(FiAccountBalance::getTenantId, SecurityUtils.getTenantId())
                        .eq(FiAccountBalance::getFiscalYear, fiscalYear)
                        .eq(FiAccountBalance::getPeriodNum, periodNum)
        );

        // 计算下一期间
        int nextPeriodNum = periodNum + 1;
        int nextFiscalYear = fiscalYear;
        if (nextPeriodNum > 12) {
            nextPeriodNum = 1;
            nextFiscalYear = fiscalYear + 1;
        }

        // 创建下一期间余额
        for (FiAccountBalance current : currentBalances) {
            FiAccountBalance next = new FiAccountBalance();
            next.setTenantId(current.getTenantId());
            next.setFiscalYear(nextFiscalYear);
            next.setPeriodNum(nextPeriodNum);
            next.setAccountId(current.getAccountId());
            next.setAccountCode(current.getAccountCode());
            next.setBeginDebit(current.getEndDebit());
            next.setBeginCredit(current.getEndCredit());
            next.setEndDebit(current.getEndDebit());
            next.setEndCredit(current.getEndCredit());
            next.setYearDebit(current.getYearDebit());
            next.setYearCredit(current.getYearCredit());
            next.setAuxCustomerId(current.getAuxCustomerId());
            next.setAuxSupplierId(current.getAuxSupplierId());
            next.setAuxDepartmentId(current.getAuxDepartmentId());
            next.setAuxProjectId(current.getAuxProjectId());
            next.setAuxEmployeeId(current.getAuxEmployeeId());
            next.setAuxItemId(current.getAuxItemId());

            accountBalanceMapper.insert(next);
        }

        log.info("余额结转完成，期间: {}-{}", fiscalYear, periodNum);
    }

    @Override
    public boolean checkTrialBalance(Integer fiscalYear, Integer periodNum) {
        // 查询所有科目余额
        List<FiAccountBalance> balances = accountBalanceMapper.selectList(
                new LambdaQueryWrapper<FiAccountBalance>()
                        .eq(FiAccountBalance::getTenantId, SecurityUtils.getTenantId())
                        .eq(FiAccountBalance::getFiscalYear, fiscalYear)
                        .eq(FiAccountBalance::getPeriodNum, periodNum)
                        .isNull(FiAccountBalance::getAuxCustomerId)
                        .isNull(FiAccountBalance::getAuxSupplierId)
                        .isNull(FiAccountBalance::getAuxDepartmentId)
                        .isNull(FiAccountBalance::getAuxProjectId)
                        .isNull(FiAccountBalance::getAuxEmployeeId)
                        .isNull(FiAccountBalance::getAuxItemId)
        );

        // 计算借贷合计
        BigDecimal totalDebit = balances.stream()
                .map(FiAccountBalance::getEndDebit)
                .reduce(BigDecimal.ZERO, BigDecimal::add);

        BigDecimal totalCredit = balances.stream()
                .map(FiAccountBalance::getEndCredit)
                .reduce(BigDecimal.ZERO, BigDecimal::add);

        return totalDebit.compareTo(totalCredit) == 0;
    }

    /**
     * 更新科目余额
     */
    private void updateBalance(Long accountId, Integer fiscalYear, Integer periodNum,
                               BigDecimal debitAmount, BigDecimal creditAmount,
                               Long auxCustomerId, Long auxSupplierId, Long auxDepartmentId,
                               Long auxProjectId, Long auxEmployeeId, Long auxItemId) {
        // 查询余额记录
        FiAccountBalance balance = accountBalanceMapper.selectByAccountAndAux(
                SecurityUtils.getTenantId(), fiscalYear, periodNum, accountId,
                auxCustomerId, auxSupplierId, auxDepartmentId, auxProjectId, auxEmployeeId, auxItemId);

        if (balance == null) {
            // 新建余额记录
            FiAccount account = accountMapper.selectById(accountId);
            balance = new FiAccountBalance();
            balance.setTenantId(SecurityUtils.getTenantId());
            balance.setFiscalYear(fiscalYear);
            balance.setPeriodNum(periodNum);
            balance.setAccountId(accountId);
            balance.setAccountCode(account.getAccountCode());
            balance.setBeginDebit(BigDecimal.ZERO);
            balance.setBeginCredit(BigDecimal.ZERO);
            balance.setAuxCustomerId(auxCustomerId);
            balance.setAuxSupplierId(auxSupplierId);
            balance.setAuxDepartmentId(auxDepartmentId);
            balance.setAuxProjectId(auxProjectId);
            balance.setAuxEmployeeId(auxEmployeeId);
            balance.setAuxItemId(auxItemId);

            accountBalanceMapper.insert(balance);
        }

        // 更新余额
        balance.setCurrentDebit(balance.getCurrentDebit().add(debitAmount));
        balance.setCurrentCredit(balance.getCurrentCredit().add(creditAmount));
        balance.setEndDebit(balance.getBeginDebit().add(balance.getCurrentDebit()));
        balance.setEndCredit(balance.getBeginCredit().add(balance.getCurrentCredit()));
        balance.setYearDebit(balance.getYearDebit().add(debitAmount));
        balance.setYearCredit(balance.getYearCredit().add(creditAmount));

        accountBalanceMapper.updateById(balance);
    }

    /**
     * 获取余额分组Key
     */
    private String getBalanceKey(FiVoucherDetail detail) {
        return String.format("%d_%d_%d_%d_%d_%d_%d",
                detail.getAccountId(),
                detail.getAuxCustomerId() != null ? detail.getAuxCustomerId() : 0,
                detail.getAuxSupplierId() != null ? detail.getAuxSupplierId() : 0,
                detail.getAuxDepartmentId() != null ? detail.getAuxDepartmentId() : 0,
                detail.getAuxProjectId() != null ? detail.getAuxProjectId() : 0,
                detail.getAuxEmployeeId() != null ? detail.getAuxEmployeeId() : 0,
                detail.getAuxItemId() != null ? detail.getAuxItemId() : 0
        );
    }
}
```

---

### 4.3 固定资产折旧计算类设计

#### 4.3.1 DepreciationCalculator折旧计算器

```java
package com.autoerp.fa.util;

import com.autoerp.fa.entity.FaAsset;
import com.autoerp.fa.enums.DeprMethodEnum;

import java.math.BigDecimal;
import java.math.RoundingMode;

/**
 * 固定资产折旧计算器
 */
public class DepreciationCalculator {

    /**
     * 计算月折旧额
     *
     * @param asset 资产信息
     * @return 月折旧额
     */
    public static BigDecimal calculateMonthlyDepreciation(FaAsset asset) {
        DeprMethodEnum method = DeprMethodEnum.getByCode(asset.getDeprMethod());

        switch (method) {
            case STRAIGHT_LINE:
                return calculateStraightLine(asset);
            case WORKLOAD:
                return calculateWorkload(asset);
            case DOUBLE_DECLINING:
                return calculateDoubleDeclining(asset);
            case SUM_OF_YEARS:
                return calculateSumOfYears(asset);
            default:
                return BigDecimal.ZERO;
        }
    }

    /**
     * 直线法折旧
     * 月折旧额 = (原值 - 残值) / 使用月数
     */
    private static BigDecimal calculateStraightLine(FaAsset asset) {
        BigDecimal depreciableAmount = asset.getOriginalValue().subtract(asset.getResidualValue());
        int useMonths = asset.getUseMonths();

        if (useMonths <= 0) {
            return BigDecimal.ZERO;
        }

        return depreciableAmount.divide(BigDecimal.valueOf(useMonths), 2, RoundingMode.HALF_UP);
    }

    /**
     * 工作量法折旧
     * 单位折旧额 = (原值 - 残值) / 预计总工作量
     * 月折旧额 = 单位折旧额 * 本月工作量
     */
    private static BigDecimal calculateWorkload(FaAsset asset) {
        // 工作量法需要额外的工作量数据
        // 简化处理，按直线法计算
        return calculateStraightLine(asset);
    }

    /**
     * 双倍余额递减法
     * 年折旧率 = 2 / 预计使用年限
     * 月折旧率 = 年折旧率 / 12
     * 月折旧额 = (原值 - 累计折旧) * 月折旧率
     */
    private static BigDecimal calculateDoubleDeclining(FaAsset asset) {
        BigDecimal netValue = asset.getOriginalValue().subtract(asset.getAccumDepreciation());

        // 最后两年按直线法折旧
        int remainingMonths = asset.getUseMonths() - asset.getUsedMonths();
        if (remainingMonths <= 24) {
            BigDecimal residualValue = asset.getResidualValue();
            BigDecimal remainingDepr = netValue.subtract(residualValue);
            if (remainingMonths <= 0) {
                return BigDecimal.ZERO;
            }
            return remainingDepr.divide(BigDecimal.valueOf(remainingMonths), 2, RoundingMode.HALF_UP);
        }

        // 双倍余额递减
        int useYears = asset.getUseYears();
        BigDecimal yearlyRate = BigDecimal.valueOf(2.0).divide(BigDecimal.valueOf(useYears), 6, RoundingMode.HALF_UP);
        BigDecimal monthlyRate = yearlyRate.divide(BigDecimal.valueOf(12), 8, RoundingMode.HALF_UP);

        return netValue.multiply(monthlyRate).setScale(2, RoundingMode.HALF_UP);
    }

    /**
     * 年数总和法
     * 年折旧率 = 剩余使用年限 / 年数总和
     * 月折旧率 = 年折旧率 / 12
     * 月折旧额 = (原值 - 残值) * 月折旧率
     */
    private static BigDecimal calculateSumOfYears(FaAsset asset) {
        int useYears = asset.getUseYears();
        int usedYears = asset.getUsedMonths() / 12;
        int remainingYears = useYears - usedYears;

        // 年数总和 = 1 + 2 + ... + n = n(n+1)/2
        int sumOfYears = useYears * (useYears + 1) / 2;

        if (remainingYears <= 0 || sumOfYears <= 0) {
            return BigDecimal.ZERO;
        }

        BigDecimal depreciableAmount = asset.getOriginalValue().subtract(asset.getResidualValue());
        BigDecimal yearlyRate = BigDecimal.valueOf(remainingYears).divide(BigDecimal.valueOf(sumOfYears), 6, RoundingMode.HALF_UP);
        BigDecimal monthlyRate = yearlyRate.divide(BigDecimal.valueOf(12), 8, RoundingMode.HALF_UP);

        return depreciableAmount.multiply(monthlyRate).setScale(2, RoundingMode.HALF_UP);
    }

    /**
     * 计算净值
     */
    public static BigDecimal calculateNetValue(FaAsset asset) {
        return asset.getOriginalValue().subtract(asset.getAccumDepreciation());
    }

    /**
     * 检查是否已提足折旧
     */
    public static boolean isFullyDepreciated(FaAsset asset) {
        BigDecimal netValue = calculateNetValue(asset);
        return netValue.compareTo(asset.getResidualValue()) <= 0;
    }
}
```

---

### 4.4 经销商返利计算类设计

#### 4.4.1 DealerRebateCalculator返利计算器

```java
package com.autoerp.ap.util;

import com.autoerp.ap.dto.DealerRebateCalcDTO;
import com.autoerp.ap.dto.RebateRuleDTO;
import com.autoerp.ap.entity.ApDealerRebate;
import com.autoerp.ap.enums.RebateTypeEnum;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.List;

/**
 * 经销商返利计算器
 */
public class DealerRebateCalculator {

    /**
     * 计算经销商返利
     *
     * @param salesData 销量数据
     * @param rules 返利规则
     * @return 返利明细列表
     */
    public static List<ApDealerRebate> calculateRebate(
            List<DealerRebateCalcDTO> salesData,
            List<RebateRuleDTO> rules) {

        List<ApDealerRebate> rebateList = new ArrayList<>();

        for (DealerRebateCalcDTO sales : salesData) {
            for (RebateRuleDTO rule : rules) {
                ApDealerRebate rebate = calculateSingleRebate(sales, rule);
                if (rebate != null && rebate.getRebateAmount().compareTo(BigDecimal.ZERO) > 0) {
                    rebateList.add(rebate);
                }
            }
        }

        return rebateList;
    }

    /**
     * 计算单项返利
     */
    private static ApDealerRebate calculateSingleRebate(DealerRebateCalcDTO sales, RebateRuleDTO rule) {
        RebateTypeEnum rebateType = RebateTypeEnum.getByCode(rule.getRebateType());

        BigDecimal rebateAmount = BigDecimal.ZERO;

        switch (rebateType) {
            case SALES_VOLUME:
                rebateAmount = calculateVolumeRebate(sales, rule);
                break;
            case ANNUAL:
                rebateAmount = calculateAnnualRebate(sales, rule);
                break;
            case TARGET:
                rebateAmount = calculateTargetRebate(sales, rule);
                break;
            case STORE_BUILDING:
                rebateAmount = rule.getFixedAmount();
                break;
            case ADVERTISING:
                rebateAmount = sales.getAdAmount().multiply(rule.getRebateRate()).divide(BigDecimal.valueOf(100), 2, RoundingMode.HALF_UP);
                break;
            case FINANCE:
                rebateAmount = calculateFinanceRebate(sales, rule);
                break;
            default:
                break;
        }

        if (rebateAmount.compareTo(BigDecimal.ZERO) <= 0) {
            return null;
        }

        ApDealerRebate rebate = new ApDealerRebate();
        rebate.setCustomerId(sales.getCustomerId());
        rebate.setCustomerCode(sales.getCustomerCode());
        rebate.setCustomerName(sales.getCustomerName());
        rebate.setRebateType(rule.getRebateType());
        rebate.setSalesQuantity(sales.getSalesQuantity());
        rebate.setRebateRate(rule.getRebateRate());
        rebate.setRebateAmount(rebateAmount);

        return rebate;
    }

    /**
     * 计算销量返利（阶梯式）
     */
    private static BigDecimal calculateVolumeRebate(DealerRebateCalcDTO sales, RebateRuleDTO rule) {
        int quantity = sales.getSalesQuantity();
        BigDecimal salesAmount = sales.getSalesAmount();

        // 根据销量阶梯计算返利比例
        BigDecimal rebateRate = getRebateRateByQuantity(quantity, rule);

        // 返利金额 = 销售金额 * 返利比例
        return salesAmount.multiply(rebateRate).divide(BigDecimal.valueOf(100), 2, RoundingMode.HALF_UP);
    }

    /**
     * 根据销量获取返利比例（阶梯式）
     */
    private static BigDecimal getRebateRateByQuantity(int quantity, RebateRuleDTO rule) {
        // 阶梯规则示例：
        // 0-50台：1%
        // 51-100台：1.5%
        // 101-200台：2%
        // 200台以上：2.5%

        if (quantity > 200) {
            return new BigDecimal("2.5");
        } else if (quantity > 100) {
            return new BigDecimal("2.0");
        } else if (quantity > 50) {
            return new BigDecimal("1.5");
        } else {
            return new BigDecimal("1.0");
        }
    }

    /**
     * 计算年度返利
     */
    private static BigDecimal calculateAnnualRebate(DealerRebateCalcDTO sales, RebateRuleDTO rule) {
        // 年度销量达标返利
        int annualQuantity = sales.getAnnualSalesQuantity();
        int targetQuantity = rule.getTargetQuantity();

        if (annualQuantity >= targetQuantity) {
            return sales.getAnnualSalesAmount()
                    .multiply(rule.getRebateRate())
                    .divide(BigDecimal.valueOf(100), 2, RoundingMode.HALF_UP);
        }

        return BigDecimal.ZERO;
    }

    /**
     * 计算达成返利
     */
    private static BigDecimal calculateTargetRebate(DealerRebateCalcDTO sales, RebateRuleDTO rule) {
        // 目标达成奖励
        int targetQuantity = rule.getTargetQuantity();
        int actualQuantity = sales.getSalesQuantity();

        if (actualQuantity >= targetQuantity) {
            return rule.getFixedAmount();
        }

        return BigDecimal.ZERO;
    }

    /**
     * 计算金融贴息
     */
    private static BigDecimal calculateFinanceRebate(DealerRebateCalcDTO sales, RebateRuleDTO rule) {
        // 金融贴息 = 贷款金额 * 贴息率 * 贴息期限
        BigDecimal loanAmount = sales.getLoanAmount();
        BigDecimal subsidyRate = rule.getSubsidyRate();
        int months = rule.getSubsidyMonths();

        return loanAmount.multiply(subsidyRate)
                .divide(BigDecimal.valueOf(100), 2, RoundingMode.HALF_UP)
                .multiply(BigDecimal.valueOf(months))
                .divide(BigDecimal.valueOf(12), 2, RoundingMode.HALF_UP);
    }
}
```

---

## 5. 核心流程设计

### 5.1 凭证处理流程

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   凭证录入   │────>│   凭证保存   │────>│   凭证审核   │────>│   凭证记账   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │                   │
       v                   v                   v                   v
 ┌───────────┐       ┌───────────┐       ┌───────────┐       ┌───────────┐
 │ 校验期间  │       │ 校验平衡  │       │ 制单人检查│       │ 更新余额  │
 │ 校验科目  │       │ 生成凭证号│       │ 状态变更  │       │ 状态变更  │
 │ 校验金额  │       │ 保存明细  │       │ 记录审核人│       │ 记录记账人│
 └───────────┘       └───────────┘       └───────────┘       └───────────┘
```

### 5.2 期末结账流程

```
┌───────────────────────────────────────────────────────────────────────┐
│                           期末结账流程                                 │
└───────────────────────────────────────────────────────────────────────┘
                                │
                                v
                   ┌─────────────────────────┐
                   │   检查凭证是否全部记账   │
                   └────────────┬────────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
                   是                      否
                    │                       │
                    v                       v
         ┌─────────────────┐      ┌─────────────────┐
         │   检查子模块结账  │      │   提示未记账凭证 │
         └────────┬────────┘      └─────────────────┘
                  │
      ┌───────────┴───────────┐
      │                       │
     是                      否
      │                       │
      v                       v
┌─────────────────┐  ┌─────────────────┐
│  检查试算平衡   │  │ 提示子模块未结账 │
└────────┬────────┘  └─────────────────┘
         │
     ┌───┴───┐
     │       │
    是      否
     │       │
     v       v
┌─────────────────┐
│  检查损益结转   │
└────────┬────────┘
         │
     ┌───┴───┐
     │       │
    是      否
     │       │
     v       v
┌─────────────────┐ ┌─────────────────┐
│   执行期末结账   │ │ 提示损益未结转  │
└────────┬────────┘ └─────────────────┘
         │
         v
┌─────────────────┐
│ 期间状态变更为  │
│   "已结账"     │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ 开放下一会计期间│
└─────────────────┘
```

---

## 6. 性能优化设计

### 6.1 缓存策略

| 缓存对象 | 缓存键 | 过期时间 | 说明 |
|----------|--------|----------|------|
| 科目信息 | account:{tenantId}:{accountCode} | 24小时 | 科目基础信息 |
| 科目树 | account:tree:{tenantId} | 24小时 | 科目树形结构 |
| 会计期间 | period:{tenantId}:{year}:{period} | 永久 | 期间状态 |
| 科目余额 | balance:{tenantId}:{year}:{period}:{accountId} | 1小时 | 科目余额 |
| 凭证号 | voucher:no:{tenantId}:{year}:{period}:{word} | 当期 | 凭证号序列 |

### 6.2 索引优化

```sql
-- 科目余额表优化索引
CREATE INDEX idx_balance_period_account ON fi_account_balance(tenant_id, fiscal_year, period_num, account_id);
CREATE INDEX idx_balance_aux ON fi_account_balance(tenant_id, fiscal_year, period_num, aux_customer_id, aux_supplier_id);

-- 凭证表优化索引
CREATE INDEX idx_voucher_period ON fi_voucher(tenant_id, fiscal_year, period_num, status);
CREATE INDEX idx_voucher_date ON fi_voucher(tenant_id, voucher_date);

-- 凭证明细表优化索引
CREATE INDEX idx_voucher_detail_account ON fi_voucher_detail(tenant_id, account_id, voucher_id);
```

### 6.3 分页查询优化

- 使用MyBatis Plus分页插件
- 避免全表扫描，使用索引字段查询
- 大数据量导出使用流式查询

---

## 7. 安全设计

### 7.1 权限控制

```java
/**
 * 权限注解示例
 */
@RestController
@RequestMapping("/api/v1/fi/vouchers")
public class VoucherController {

    @GetMapping
    @PreAuthorize("hasAuthority('fi:voucher:list')")
    public Result<PageResult<VoucherVO>> list(VoucherQueryDTO queryDTO) {
        // ...
    }

    @PostMapping
    @PreAuthorize("hasAuthority('fi:voucher:add')")
    public Result<Long> add(@RequestBody VoucherDTO voucherDTO) {
        // ...
    }
}
```

### 7.2 数据权限

```java
/**
 * 数据权限拦截器
 */
@Component
public class DataPermissionInterceptor implements InnerInterceptor {

    @Override
    public void beforeQuery(Executor executor, MappedStatement ms,
                           Object parameter, RowBounds rowBounds,
                           ResultHandler resultHandler, BoundSql boundSql) {
        // 根据用户数据权限过滤SQL
        String sql = boundSql.getSql();
        String filteredSql = addDataPermissionFilter(sql);
        // ...
    }
}
```

---

## 8. 异常处理设计

### 8.1 异常体系

```
BusinessException
├── FiException (总账异常)
│   ├── AccountException (科目异常)
│   ├── VoucherException (凭证异常)
│   └── PeriodException (期间异常)
├── ArException (应收异常)
├── ApException (应付异常)
├── FaException (资产异常)
└── TrException (资金异常)
```

### 8.2 全局异常处理

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(BusinessException.class)
    public Result<Void> handleBusinessException(BusinessException e) {
        log.warn("业务异常: {}", e.getMessage());
        return Result.fail(e.getCode(), e.getMessage());
    }

    @ExceptionHandler(Exception.class)
    public Result<Void> handleException(Exception e) {
        log.error("系统异常", e);
        return Result.fail(500, "系统异常，请联系管理员");
    }
}
```

---

## 9. 日志设计

### 9.1 操作日志

```java
/**
 * 操作日志注解
 */
@Target({ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
public @interface OperateLog {
    String module();
    String operation();
}

/**
 * 操作日志切面
 */
@Aspect
@Component
public class OperateLogAspect {

    @AfterReturning(pointcut = "@annotation(operateLog)", returning = "result")
    public void recordLog(JoinPoint joinPoint, OperateLog operateLog, Object result) {
        // 记录操作日志
    }
}
```

### 9.2 审计日志

- 记录关键业务操作
- 记录数据变更前后值
- 记录操作人和时间

---

## 10. 附录

### 10.1 枚举类定义

```java
/**
 * 凭证状态枚举
 */
public enum VoucherStatusEnum {
    DRAFT(0, "制单"),
    AUDITED(1, "已审核"),
    POSTED(2, "已记账"),
    REJECTED(3, "已驳回");

    private final Integer code;
    private final String name;

    // getter, constructor, getByCode...
}

/**
 * 会计期间状态枚举
 */
public enum PeriodStatusEnum {
    CLOSED(0, "未开放"),
    OPEN(1, "已开放"),
    SETTLED(2, "已结账");

    private final Integer code;
    private final String name;
}

/**
 * 折旧方法枚举
 */
public enum DeprMethodEnum {
    STRAIGHT_LINE(1, "直线法"),
    WORKLOAD(2, "工作量法"),
    DOUBLE_DECLINING(3, "双倍余额递减法"),
    SUM_OF_YEARS(4, "年数总和法");

    private final Integer code;
    private final String name;
}

/**
 * 返利类型枚举
 */
public enum RebateTypeEnum {
    SALES_VOLUME(1, "销量返利"),
    ANNUAL(2, "年度返利"),
    TARGET(3, "达成返利"),
    STORE_BUILDING(4, "建店补贴"),
    ADVERTISING(5, "广告补贴"),
    FINANCE(6, "金融贴息");

    private final Integer code;
    private final String name;
}
```

### 10.2 修订历史
| 版本 | 日期 | 修订人 | 修订内容 |
|------|------|--------|----------|
| V1.0 | 2026-03-24 | 研发团队 | 初始版本 |

---

**文档结束**