# 端到端工作流用例

> 本文档展示跨部门的端到端软件开发工作流，演示产品→研发→测试→运维→项目管理全链路如何通过 AI Skill 协作完成。
> 每个用例覆盖完整生命周期，体现"人类定义目标，AI 执行产出"的核心理念。

---

## 用例1：新功能端到端开发流程（电商订单取消功能）

### 场景描述

电商平台需要新增"用户自助取消订单"功能。产品经理收到业务需求后，需要走完从需求分析→架构设计→编码实现→测试用例→部署分析→项目跟踪的全流程。本用例演示 AI 如何在每个阶段自动衔接，产出标准化交付物。

### 技术栈

- 后端：Java / Spring Boot / MyBatis Plus
- 前端：Vue 3 + Vite
- 数据库：MySQL 8.0

### 涉及角色与Skill

| 阶段 | 角色 | Skill | 产出物 |
|------|------|-------|--------|
| 需求分析 | 产品经理 | requirement-analyzer | PRD文档 |
| 用户故事 | 产品经理 | user-story-generator | 用户故事列表 |
| 验收标准 | 产品经理 | acceptance-criteria-writer | Gherkin验收标准 |
| 需求评审 | 研发工程师 | requirement-review | 评审报告 |
| 架构设计 | 架构师 | architect | 架构设计文档 |
| 数据库设计 | 研发工程师 | db-designer | DDL脚本 |
| API设计 | 研发工程师 | api-designer | REST API规范 |
| 功能实现 | 研发工程师 | implement | 业务代码 |
| 代码审查 | 研发工程师 | code-review | 审查报告 |
| 测试用例 | 测试工程师 | test-case-generator | 测试用例集 |
| 部署分析 | 运维工程师 | deploy-analyzer | 部署方案 |
| 项目跟踪 | 项目经理 | project-status | 项目周报 |

---

### 阶段1：需求分析

#### 触发Skill
- **Skill**: requirement-analyzer
- **触发方式**: `/requirement-analyzer`

#### 完整提示词
```
/requirement-analyzer

需求来源：业务运营团队
需求描述：用户下单后希望能在发货前自助取消订单，目前取消订单需要联系客服，
处理时间长，用户满意度低。需要支持：
1. 待付款订单：直接取消，释放库存
2. 已付款待发货订单：取消后自动退款，释放库存
3. 已发货订单：不支持取消，提示用户申请退货退款
4. 取消原因选择（不想要了、买错了、价格问题、其他）
5. 取消后库存自动恢复

业务背景：B2C电商平台，日均订单量5000单
目标用户：C端购物用户
```

#### 输入参数
| 参数名 | 类型 | 必填 | 值 |
|--------|------|------|-----|
| requirement_text | string | 是 | 用户自助取消订单需求描述 |
| business_context | string | 否 | "B2C电商平台" |
| target_users | string | 否 | "C端购物用户" |

#### 执行过程

**步骤1：需求解析** — 识别5个核心需求点：
- 待付款订单直接取消
- 已付款订单取消+自动退款
- 已发货订单拦截
- 取消原因收集
- 库存自动恢复

**步骤2：实体提取**
- 实体：订单、库存、退款、取消原因
- 角色：买家、客服、仓库
- 动作：取消、退款、释放库存、选择原因

**步骤3：关系识别**
- 取消→库存恢复 存在强依赖
- 取消→退款 存在强依赖（已付款场景）
- 取消原因→数据分析 为弱依赖
- 冲突点：已付款取消与退款流程需定义超时机制

**步骤4：结构化输出** — 生成PRD框架

#### 最终产出：PRD文档
```markdown
# 产品需求文档 - 用户自助取消订单

## 需求概述
支持用户在订单发货前自助取消订单，根据订单状态执行不同的取消逻辑，
包含自动退款和库存恢复能力。

## 背景与目标
- **背景**: 取消订单需联系客服，平均处理时间2小时，用户满意度仅60%
- **目标**: 用户自助取消，处理时间<30秒，用户满意度提升至90%

## 用户故事

### US-CANCEL-001: 取消待付款订单
作为买家，我希望取消待付款的订单，以便释放商品库存。

### US-CANCEL-002: 取消已付款待发货订单
作为买家，我希望取消已付款但未发货的订单并获得退款，以便处理不需要的商品。

### US-CANCEL-003: 取消原因选择
作为运营，我希望收集用户取消原因，以便分析改进方向。

## 功能需求

### 核心功能
- 订单详情页增加"取消订单"按钮（仅待付款/待发货状态显示）
- 取消原因选择弹窗（4个选项+备注）
- 待付款订单取消：直接关闭订单，释放库存
- 已付款订单取消：发起退款→等待退款成功→关闭订单→释放库存
- 已发货订单：隐藏取消按钮，提示"请申请退货退款"

### 业务规则
- 待付款订单取消后库存立即恢复
- 已付款订单退款到账时间取决于支付渠道（微信1-3天，支付宝即时）
- 每个订单仅允许取消一次
- 取消操作不可撤回

## 非功能需求
- 取消响应时间 < 30秒
- 退款状态需异步通知用户
- 库存恢复需保证最终一致性

## 待澄清问题
1. 退款是否原路返回？
2. 已使用优惠券的订单取消后优惠券是否退回？
3. 部分取消是否支持？
4. 取消后是否需要短信/APP推送通知？

## 建议优先级
- P0: 待付款/已付款订单取消+库存恢复
- P1: 退款流程+取消原因收集
- P2: 退款通知推送+数据分析看板
```

---

### 阶段2：用户故事与验收标准

#### 触发Skill
- **Skill**: user-story-generator + acceptance-criteria-writer
- **触发方式**: `/user-story-generator` → `/acceptance-criteria-writer`

#### 完整提示词
```
/user-story-generator

PRD: 用户自助取消订单
模块: 订单管理
角色: 买家、运营、客服
```

#### 最终产出：用户故事 + 验收标准
```markdown
# 用户故事列表

## US-CANCEL-001: 取消待付款订单
**作为** 买家
**我希望** 取消待付款的订单
**以便** 释放商品库存，重新选择商品

### 验收标准 (Gherkin)
Feature: 取消待付款订单

  Scenario: 成功取消待付款订单
    Given 用户有一笔待付款订单
    When 用户点击"取消订单"并选择取消原因
    Then 订单状态变为"已取消"
    And 商品库存恢复
    And 显示"订单已取消"提示

  Scenario: 非待付款状态不可取消
    Given 用户有一笔已发货订单
    When 用户查看订单详情
    Then 不显示"取消订单"按钮
    And 显示"请申请退货退款"提示

## US-CANCEL-002: 取消已付款待发货订单
**作为** 买家
**我希望** 取消已付款的订单并获得退款
**以便** 处理不需要的商品

### 验收标准 (Gherkin)
Feature: 取消已付款订单

  Scenario: 成功取消已付款订单
    Given 用户有一笔已付款待发货订单，金额100元
    When 用户点击"取消订单"并选择取消原因
    Then 发起100元退款申请
    And 订单状态变为"退款中"
    And 退款成功后订单状态变为"已取消"
    And 商品库存恢复

  Scenario: 退款失败处理
    Given 用户取消已付款订单，退款处理中
    When 退款失败（支付渠道异常）
    Then 订单状态保持"退款中"
    And 自动重试退款（最多3次）
    And 3次均失败后转人工处理
```

---

### 阶段3：需求评审

#### 触发Skill
- **Skill**: requirement-review
- **触发方式**: `/requirement-review`

#### 完整提示词
```
/requirement-review

需求文档: 用户自助取消订单PRD
评审角色: 后端研发
技术栈: Java/Spring Boot, MySQL
```

#### 最终产出：需求评审报告
```markdown
# 需求评审报告 - 用户自助取消订单

## 评审结果: 有条件通过 ✅

## 评审意见

### 完整性评估
| 维度 | 评分 | 说明 |
|------|------|------|
| 功能完整性 | 8/10 | 核心功能清晰，部分边界待补充 |
| 非功能需求 | 7/10 | 性能指标明确，安全需求待补充 |
| 数据需求 | 6/10 | 库存恢复的事务边界需明确 |
| 接口需求 | 7/10 | 退款接口依赖第三方，需确认 |

### 技术可行性
- ✅ 取消逻辑可通过状态机实现
- ✅ 库存恢复可通过消息队列保证最终一致性
- ⚠️ 退款需要对接支付渠道回调，建议增加退款状态表
- ⚠️ 并发取消场景需加分布式锁

### 建议补充
1. 增加并发取消的幂等性设计
2. 明确退款超时时间（建议30分钟）
3. 增加取消订单的日志审计
4. 优惠券退回规则需明确定义

### 遗留问题
| ID | 问题 | 责任人 | 截止日期 |
|----|------|--------|----------|
| Q1 | 退款超时如何处理？ | 产品经理 | 2026-06-10 |
| Q2 | 优惠券退回规则？ | 产品经理 | 2026-06-10 |
```

---

### 阶段4：架构设计

#### 触发Skill
- **Skill**: architect (tech_stack_aware: backend/java)
- **触发方式**: `/architect`

#### 完整提示词
```
/architect

需求：实现用户自助取消订单功能
技术栈：Java/Spring Boot, MySQL, Redis, RabbitMQ
约束：现有订单系统已有Order表，需兼容现有架构
```

#### 最终产出：架构设计文档
```markdown
# 架构设计 - 用户自助取消订单

## 1. 架构概述
在现有订单服务基础上，新增取消订单模块。采用状态机模式管理订单状态转换，
通过消息队列实现退款和库存恢复的异步处理，保证最终一致性。

## 2. 技术方案

### 2.1 状态机设计
```
待付款 ──取消──→ 已取消（直接释放库存）
   │
   └─支付──→ 待发货 ──取消──→ 退款中 ──退款成功──→ 已取消（释放库存）
                                              │
                                              └─退款失败──→ 重试（最多3次）→ 人工处理
   │
   └─发货──→ 已发货（不可取消，提示退货退款）
```

### 2.2 核心组件
- **OrderCancelService**: 取消订单核心服务
- **RefundService**: 退款服务（对接支付渠道）
- **InventoryRecoveryService**: 库存恢复服务
- **CancelReasonMapper**: 取消原因数据统计

### 2.3 消息队列设计
| Exchange | Queue | Routing Key | 用途 |
|----------|-------|-------------|------|
| order.cancel | refund.queue | order.cancel.refund | 退款处理 |
| order.cancel | inventory.queue | order.cancel.inventory | 库存恢复 |
| order.cancel | notify.queue | order.cancel.notify | 用户通知 |

### 2.4 数据库变更
- 新增 `order_cancel_record` 表（取消记录）
- 新增 `refund_record` 表（退款记录）
- Order表增加 `cancel_reason` 字段
```

---

### 阶段5：数据库设计 + API设计

#### 触发Skill
- **Skill**: db-designer + api-designer
- **触发方式**: `/db-designer` → `/api-designer`

#### 最终产出：DDL + API规范
```sql
-- 取消订单记录表
CREATE TABLE order_cancel_record (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    order_id BIGINT NOT NULL COMMENT '订单ID',
    order_no VARCHAR(50) NOT NULL COMMENT '订单编号',
    user_id BIGINT NOT NULL COMMENT '用户ID',
    cancel_reason VARCHAR(20) NOT NULL COMMENT '取消原因: NOT_WANT/WRONG_BUY/PRICE/OTHER',
    cancel_remark VARCHAR(500) COMMENT '取消备注',
    order_status TINYINT NOT NULL COMMENT '取消时订单状态',
    order_amount DECIMAL(10,2) NOT NULL COMMENT '订单金额',
    refund_status TINYINT DEFAULT 0 COMMENT '退款状态: 0-无需退款 1-退款中 2-退款成功 3-退款失败',
    refund_amount DECIMAL(10,2) DEFAULT 0 COMMENT '退款金额',
    refund_time DATETIME COMMENT '退款完成时间',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_order_id (order_id),
    INDEX idx_user_id (user_id),
    INDEX idx_create_time (create_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='订单取消记录表';
```

```markdown
# API设计 - 取消订单

## POST /api/v1/orders/{orderId}/cancel
取消订单接口

### 请求头
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Authorization | string | 是 | Bearer Token |

### 请求体
```json
{
  "cancelReason": "NOT_WANT",
  "cancelRemark": "不想要了"
}
```

### 响应体 (成功)
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "orderId": 10001,
    "orderNo": "ORD20260608001",
    "cancelStatus": "CANCELLED",
    "refundStatus": "PROCESSING",
    "refundAmount": 99.00,
    "message": "订单已取消，退款预计1-3个工作日到账"
  }
}
```

### 响应体 (失败)
```json
{
  "code": 40001,
  "message": "该订单状态不支持取消"
}
```

### 业务规则
- 仅待付款(PENDING_PAYMENT)和待发货(PENDING_SHIPMENT)状态可取消
- 待付款订单：直接关闭，释放库存
- 待发货订单：发起退款，异步处理
- 幂等性：同一订单重复取消返回相同结果
```

---

### 阶段6：功能实现

#### 触发Skill
- **Skill**: implement (tech_stack_aware: backend/java)
- **触发方式**: `/implement`
- **内部调用**: api-designer → entity-designer → crud-designer

#### 最终产出：核心业务代码
```java
/**
 * 订单取消服务
 */
@Service
@Slf4j
public class OrderCancelService {

    @Resource
    private OrderMapper orderMapper;
    @Resource
    private OrderCancelRecordMapper cancelRecordMapper;
    @Resource
    private RabbitTemplate rabbitTemplate;
    @Resource
    private RedissonClient redissonClient;

    /**
     * 取消订单
     */
    @Transactional(rollbackFor = Exception.class)
    public OrderCancelRespDTO cancelOrder(Long userId, Long orderId, OrderCancelReqDTO req) {
        // 1. 分布式锁保证幂等
        String lockKey = "order:cancel:" + orderId;
        RLock lock = redissonClient.getLock(lockKey);
        if (!lock.tryLock()) {
            throw new ServiceException(40001, "订单取消处理中，请勿重复操作");
        }

        try {
            // 2. 查询订单
            OrderDO order = orderMapper.selectById(orderId);
            if (order == null || !order.getUserId().equals(userId)) {
                throw new ServiceException(40002, "订单不存在");
            }

            // 3. 校验订单状态
            if (!OrderStatusEnum.PENDING_PAYMENT.equals(order.getStatus())
                && !OrderStatusEnum.PENDING_SHIPMENT.equals(order.getStatus())) {
                throw new ServiceException(40003, "该订单状态不支持取消");
            }

            // 4. 创建取消记录
            OrderCancelRecordDO cancelRecord = new OrderCancelRecordDO();
            cancelRecord.setOrderId(orderId);
            cancelRecord.setOrderNo(order.getOrderNo());
            cancelRecord.setUserId(userId);
            cancelRecord.setCancelReason(req.getCancelReason());
            cancelRecord.setCancelRemark(req.getCancelRemark());
            cancelRecord.setOrderStatus(order.getStatus().getCode());
            cancelRecord.setOrderAmount(order.getTotalAmount());
            cancelRecordMapper.insert(cancelRecord);

            // 5. 根据订单状态执行不同逻辑
            if (OrderStatusEnum.PENDING_PAYMENT.equals(order.getStatus())) {
                // 待付款：直接取消，释放库存
                order.setStatus(OrderStatusEnum.CANCELLED);
                orderMapper.updateById(order);
                // 发送库存恢复消息
                rabbitTemplate.convertAndSend("order.cancel", "order.cancel.inventory",
                    new InventoryRecoveryMsg(orderId));
                cancelRecord.setRefundStatus(RefundStatusEnum.NO_NEED.getCode());

            } else {
                // 待发货：发起退款
                order.setStatus(OrderStatusEnum.REFUNDING);
                orderMapper.updateById(order);
                // 发送退款消息
                rabbitTemplate.convertAndSend("order.cancel", "order.cancel.refund",
                    new RefundMsg(orderId, order.getTotalAmount(), order.getPayChannel()));
                cancelRecord.setRefundStatus(RefundStatusEnum.PROCESSING.getCode());
                cancelRecord.setRefundAmount(order.getTotalAmount());
            }

            // 6. 发送通知消息
            rabbitTemplate.convertAndSend("order.cancel", "order.cancel.notify",
                new NotifyMsg(userId, orderId, "订单已取消"));

            return buildResp(order, cancelRecord);

        } finally {
            lock.unlock();
        }
    }
}
```

---

### 阶段7：代码审查

#### 触发Skill
- **Skill**: code-review
- **触发方式**: `/code-review`

#### 最终产出：代码审查报告
```markdown
# 代码审查报告 - 取消订单功能

## 审查结果: 有条件通过 ✅

## 审查统计
| 指标 | 数值 |
|------|------|
| 审查文件数 | 12 |
| 问题总数 | 5 |
| 严重 | 0 |
| 一般 | 2 |
| 建议 | 3 |

## 问题列表

### 一般问题
| # | 文件 | 行号 | 问题 | 建议修复 |
|---|------|------|------|---------|
| 1 | OrderCancelService.java | 45 | lock.tryLock()未设置超时时间 | 添加leaseTime参数 |
| 2 | RefundConsumer.java | 32 | 退款失败重试逻辑缺少指数退避 | 添加@Retryable注解 |

### 优化建议
| # | 文件 | 建议 |
|---|------|------|
| 1 | OrderCancelService.java | 将状态校验抽取为独立方法 |
| 2 | OrderCancelRecordDO | 建议增加逻辑删除字段 |
| 3 | 取消原因枚举 | 建议维护到数据库配置表 |

## 代码质量评分
| 维度 | 评分 |
|------|------|
| 命名规范 | 9/10 |
| 代码结构 | 8/10 |
| 异常处理 | 8/10 |
| 并发安全 | 7/10 |
| 测试覆盖 | 7/10 |
| **综合** | **8/10** |
```

---

### 阶段8：测试用例生成

#### 触发Skill
- **Skill**: test-case-generator
- **触发方式**: `/test-case-generator`

#### 完整提示词
```
/test-case-generator

功能：用户自助取消订单
- 待付款订单取消（直接关闭+释放库存）
- 已付款待发货订单取消（退款+释放库存）
- 已发货订单不可取消
- 取消原因选择
- 并发取消幂等性
- 退款失败重试

来源类型：requirement
测试类型：functional
```

#### 最终产出：测试用例集
```markdown
# 测试用例集 - 用户自助取消订单

## 概述
- 测试对象: 取消订单模块
- 用例总数: 22
- 优先级分布: P0=8, P1=10, P2=4

## P0 - 核心功能

#### TC-CANCEL-001: 取消待付款订单成功
| 属性 | 内容 |
|------|------|
| 用例ID | TC-CANCEL-001 |
| 优先级 | P0 |
| 前置条件 | 用户有待付款订单ORD001，商品A库存10件 |
| 测试步骤 | 1. 进入订单详情页<br>2. 点击"取消订单"<br>3. 选择原因"不想要了"<br>4. 确认取消 |
| 预期结果 | 1. 订单状态变为"已取消"<br>2. 商品A库存恢复为11件<br>3. 显示"订单已取消"提示 |

#### TC-CANCEL-002: 取消已付款订单-退款成功
| 属性 | 内容 |
|------|------|
| 用例ID | TC-CANCEL-002 |
| 优先级 | P0 |
| 前置条件 | 用户有已付款待发货订单ORD002，金额99元 |
| 测试步骤 | 1. 进入订单详情页<br>2. 点击"取消订单"<br>3. 选择原因"买错了"<br>4. 确认取消 |
| 预期结果 | 1. 订单状态变为"退款中"<br>2. 发起99元退款<br>3. 退款成功后状态变为"已取消"<br>4. 库存恢复 |

#### TC-CANCEL-003: 已发货订单不可取消
| 属性 | 内容 |
|------|------|
| 用例ID | TC-CANCEL-003 |
| 优先级 | P0 |
| 前置条件 | 用户有已发货订单ORD003 |
| 测试步骤 | 1. 进入订单详情页 |
| 预期结果 | 1. 不显示"取消订单"按钮<br>2. 显示"请申请退货退款"提示 |

## P1 - 边界和异常

#### TC-CANCEL-009: 并发取消幂等性
| 属性 | 内容 |
|------|------|
| 用例ID | TC-CANCEL-009 |
| 优先级 | P1 |
| 测试步骤 | 1. 同时发起2个取消请求（同一订单） |
| 预期结果 | 1个成功，1个返回"取消处理中" |

#### TC-CANCEL-010: 退款失败自动重试
| 属性 | 内容 |
|------|------|
| 用例ID | TC-CANCEL-010 |
| 优先级 | P1 |
| 测试步骤 | 1. 模拟支付渠道返回失败<br>2. 等待自动重试 |
| 预期结果 | 自动重试3次，均失败后转人工处理 |

#### TC-CANCEL-013: 取消原因必选
| 属性 | 内容 |
|------|------|
| 用例ID | TC-CANCEL-013 |
| 优先级 | P1 |
| 测试步骤 | 1. 点击取消订单<br>2. 不选择原因直接确认 |
| 预期结果 | 提示"请选择取消原因" |

## P2 - 性能和安全

#### TC-CANCEL-019: 取消响应时间
| 属性 | 内容 |
|------|------|
| 用例ID | TC-CANCEL-019 |
| 优先级 | P2 |
| 预期结果 | 取消接口响应时间 < 1秒 |

#### TC-CANCEL-020: 非本人订单不可取消
| 属性 | 内容 |
|------|------|
| 用例ID | TC-CANCEL-020 |
| 优先级 | P2 |
| 测试步骤 | 用户A尝试取消用户B的订单 |
| 预期结果 | 返回"订单不存在" |
```

---

### 阶段9：部署分析

#### 触发Skill
- **Skill**: deploy-analyzer
- **触发方式**: `/deploy-analyzer`

#### 最终产出：部署方案
```markdown
# 部署分析报告 - 取消订单功能

## 变更概述
- 新增功能：用户自助取消订单
- 影响范围：订单服务、库存服务、支付服务
- 数据库变更：新增2张表，1个字段
- 消息队列：新增3个Queue

## 部署风险评估

| 风险项 | 等级 | 说明 | 缓解措施 |
|--------|------|------|---------|
| 数据库迁移 | 中 | 新增表和字段 | 提前执行DDL，兼容旧代码 |
| 消息队列配置 | 低 | 新增Queue | 提前创建Queue，配置死信队列 |
| 支付渠道回调 | 高 | 退款回调依赖第三方 | 灰度发布，先内部验证 |
| 库存一致性 | 中 | 库存恢复逻辑 | 增加对账脚本 |

## 部署步骤

### 阶段1：预发布准备（T-1天）
1. 执行数据库DDL（新增表和字段）
2. 创建RabbitMQ Queue和Exchange
3. 配置退款回调地址（预发布环境）
4. 部署对账脚本

### 阶段2：灰度发布（T日 10:00）
1. 部署订单服务新版本
2. 开放10%流量灰度
3. 监控取消成功率、退款成功率
4. 监控库存一致性

### 阶段3：全量发布（T日 14:00）
1. 灰度验证通过后全量发布
2. 监控各项指标
3. 准备回滚方案

## 回滚方案
1. 关闭功能开关（cancel.feature.enabled=false）
2. 回滚订单服务到上一版本
3. 手动处理进行中的退款（查询refund_record表）
4. 库存对账脚本修正

## 监控告警
| 指标 | 阈值 | 告警方式 |
|------|------|---------|
| 取消成功率 | >95% | 低于阈值告警 |
| 退款成功率 | >98% | 低于阈值告警 |
| 取消接口RT | P99<2s | 超过告警 |
| 库存不一致数 | =0 | >0立即告警 |
```

---

### 阶段10：项目跟踪

#### 触发Skill
- **Skill**: project-status
- **触发方式**: `/project-status`

#### 最终产出：项目周报
```markdown
# 项目状态周报 - 取消订单功能

## 概览
- 功能名称: 用户自助取消订单
- 报告时间: 2026-06-08 (Sprint 5 第2周)
- 整体状态: 🟢 正常
- 项目经理: AI自动生成

## 进度概览

| 指标 | 计划 | 实际 | 偏差 | 趋势 |
|------|------|------|------|------|
| 整体完成率 | 90% | 85% | -5% | → |
| 用例开发 | 10 | 9 | -1 | ↓ |
| 测试用例 | 22 | 22 | 0 | ✅ |
| Bug修复 | 5 | 4 | -1 | ↓ |

## 里程碑状态

| 里程碑 | 计划日期 | 预计日期 | 状态 |
|--------|----------|----------|------|
| 需求评审 | 06-01 | 06-01 | ✅ 已完成 |
| 设计评审 | 06-03 | 06-03 | ✅ 已完成 |
| 开发完成 | 06-07 | 06-08 | ⚠️ 延期1天 |
| 测试完成 | 06-10 | 06-10 | ✅ 按计划 |
| 上线发布 | 06-12 | 06-12 | ✅ 按计划 |

## 本周进展
- ✅ PRD评审通过
- ✅ 架构设计评审通过
- ✅ 数据库DDL执行完成
- ✅ 核心业务代码开发完成
- ✅ 代码审查通过（有条件）
- ✅ 测试用例生成完成
- 🔄 退款重试逻辑优化中（预计明天完成）
- ⏳ 部署方案待确认

## 风险和问题
| ID | 问题 | 状态 | 负责人 |
|----|------|------|--------|
| R1 | 退款回调联调时间不足 | 关注 | 开发组 |
| R2 | 优惠券退回规则未确认 | 待处理 | 产品经理 |
```

---

### 全流程产出物清单

| # | 阶段 | 产出物 | Skill | 状态 |
|---|------|--------|-------|------|
| 1 | 需求分析 | PRD文档 | requirement-analyzer | ✅ |
| 2 | 用户故事 | 用户故事+验收标准 | user-story-generator, acceptance-criteria-writer | ✅ |
| 3 | 需求评审 | 评审报告 | requirement-review | ✅ |
| 4 | 架构设计 | 架构设计文档 | architect | ✅ |
| 5 | 数据库设计 | DDL脚本 | db-designer | ✅ |
| 6 | API设计 | REST API规范 | api-designer | ✅ |
| 7 | 功能实现 | 业务代码 | implement | ✅ |
| 8 | 代码审查 | 审查报告 | code-review | ✅ |
| 9 | 测试用例 | 测试用例集(22个) | test-case-generator | ✅ |
| 10 | 部署分析 | 部署方案 | deploy-analyzer | ✅ |
| 11 | 项目跟踪 | 项目周报 | project-status | ✅ |

### 工作流流转图

```
┌──────────────────────────────────────────────────────────────────────┐
│                     端到端工作流 - 取消订单功能                         │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐          │
│  │ 产品经理 │───→│ 产品经理 │───→│ 产品经理 │───→│ 研发评审 │          │
│  │ 需求分析 │    │ 用户故事 │    │ 验收标准 │    │ 需求评审 │          │
│  └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘          │
│       │              │              │              │                 │
│       ▼              ▼              ▼              ▼                 │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐          │
│  │  PRD    │    │ 用户故事 │    │ Gherkin │    │ 评审报告 │          │
│  │  文档   │    │  列表   │    │ 验收标准 │    │         │          │
│  └─────────┘    └─────────┘    └─────────┘    └────┬────┘          │
│                                                     │               │
│                                                     ▼               │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐          │
│  │ 架构师  │───→│ 研发    │───→│ 研发    │───→│ 研发    │          │
│  │ 架构设计 │    │ DB+API  │    │ 功能实现 │    │ 代码审查 │          │
│  └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘          │
│       │              │              │              │                 │
│       ▼              ▼              ▼              ▼                 │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐          │
│  │ 架构文档 │    │ DDL+API │    │ 业务代码 │    │ 审查报告 │          │
│  │ + ADR   │    │  规范   │    │         │    │         │          │
│  └─────────┘    └─────────┘    └─────────┘    └────┬────┘          │
│                                                     │               │
│                                                     ▼               │
│                  ┌─────────┐    ┌─────────┐    ┌─────────┐         │
│                  │ 测试    │───→│ 运维    │───→│ 项目经理 │         │
│                  │ 测试用例 │    │ 部署分析 │    │ 项目跟踪 │         │
│                  └────┬────┘    └────┬────┘    └────┬────┘         │
│                       │              │              │               │
│                       ▼              ▼              ▼               │
│                  ┌─────────┐    ┌─────────┐    ┌─────────┐         │
│                  │ 测试集  │    │ 部署方案 │    │ 项目周报 │         │
│                  │ (22个)  │    │ +回滚   │    │         │         │
│                  └─────────┘    └─────────┘    └─────────┘         │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 用例2：敏捷Sprint端到端流程（用户评价功能）

### 场景描述

敏捷团队在一个Sprint（2周）内完成"商品评价"功能的端到端开发。本用例展示敏捷模式下各Skill如何在Sprint各阶段协作。

### Sprint信息
- **Sprint**: Sprint 6
- **周期**: 2026-06-09 ~ 2026-06-22（2周）
- **目标**: 完成商品评价功能（评价发布、评价展示、评价管理）

---

### Sprint阶段1：迭代规划（Day 1）

#### 触发Skill
- **Skill**: requirement-analyzer + user-story-generator
- **触发方式**: `/requirement-analyzer` → `/user-story-generator`

#### 输入
```
Sprint目标：商品评价功能
功能列表：
1. 用户发布文字+图片评价（1-9张图）
2. 用户打星评分（1-5星）
3. 商品详情页展示评价列表
4. 评价按时间/好评率排序
5. 商家回复评价
6. 管理后台评价审核

Sprint周期：2周
团队规模：前端2人+后端2人+测试1人
```

#### 产出
```
用户故事拆分（按Sprint排期）：

Sprint 6 - Week 1:
  US-REVIEW-001: 发布评价（文字+图片+星级）     [后端3天+前端2天]
  US-REVIEW-002: 评价列表展示                    [后端2天+前端2天]

Sprint 6 - Week 2:
  US-REVIEW-003: 评价排序（时间/好评率）          [后端1天+前端1天]
  US-REVIEW-004: 商家回复评价                    [后端2天+前端1天]
  US-REVIEW-005: 管理后台评价审核                [后端2天+前端2天]

Sprint容量评估：
  总故事点：34点
  团队速率：30点/人（历史平均）
  风险：US-REVIEW-005可能溢出到下个Sprint
```

---

### Sprint阶段2：迭代执行（Day 2-9）

#### 每日工作流

**Day 2-3**: 后端开发 US-REVIEW-001
```
/implement
功能：商品评价发布接口
技术栈：Java/Spring Boot
包含：图片上传（OSS）、评价内容校验、评分计算
```

**Day 3-4**: 前端开发 US-REVIEW-001
```
/implement vue
功能：评价发布页面
包含：星级选择组件、图片上传组件、文字输入、表单校验
```

**Day 5**: 代码审查
```
/code-review
目标：US-REVIEW-001 全部代码变更
```

**Day 6-7**: 开发 US-REVIEW-002（评价列表）
```
后端：分页查询、评价聚合接口
前端：评价列表组件、图片预览、评分展示
```

**Day 8-9**: 测试 US-REVIEW-001 + US-REVIEW-002
```
/test-case-generator
功能：商品评价
- 发布评价（文字、图片、星级）
- 评价列表展示
- 评价排序
```

#### 测试用例产出（节选）
```markdown
#### TC-REVIEW-001: 发布纯文字评价
| 前置条件 | 用户已购买商品且确认收货 |
| 测试步骤 | 1. 进入订单详情<br>2. 点击"评价"<br>3. 输入评价文字<br>4. 选择5星<br>5. 提交 |
| 预期结果 | 评价发布成功，商品评分更新 |

#### TC-REVIEW-005: 上传9张图片评价
| 前置条件 | 用户已购买商品 |
| 测试步骤 | 1. 选择9张图片<br>2. 输入文字<br>3. 提交 |
| 预期结果 | 9张图片上传成功，评价展示正确 |

#### TC-REVIEW-008: 评价列表分页
| 前置条件 | 商品有50条评价 |
| 测试步骤 | 1. 查看评价列表<br>2. 下拉加载更多 |
| 预期结果 | 首页显示20条，下拉加载下一页 |
```

---

### Sprint阶段3：迭代评审（Day 10）

#### 触发Skill
- **Skill**: project-status (report_type: milestone)

#### 产出
```markdown
# Sprint 6 评审报告

## 完成情况
| 用户故事 | 计划 | 实际 | 状态 |
|----------|------|------|------|
| US-REVIEW-001: 发布评价 | 5天 | 5天 | ✅ 完成 |
| US-REVIEW-002: 评价列表 | 4天 | 4天 | ✅ 完成 |
| US-REVIEW-003: 评价排序 | 2天 | 2天 | ✅ 完成 |
| US-REVIEW-004: 商家回复 | 3天 | 3天 | ✅ 完成 |
| US-REVIEW-005: 后台审核 | 4天 | 5天 | ⚠️ 延期1天 |

## Sprint指标
- 计划故事点：34
- 完成故事点：32
- 完成率：94%
- 遗留Bug：2个（P2级）

## Demo反馈
1. 评价图片加载需优化（懒加载）
2. 评价排序默认改为"最新优先"
3. 商家回复需支持富文本
```

---

### Sprint阶段4：迭代回顾（Day 10）

#### 产出
```markdown
# Sprint 6 回顾

## 做得好的
1. ✅ 前后端并行开发效率高
2. ✅ 测试用例提前生成，测试覆盖率95%
3. ✅ 代码审查发现3个潜在Bug

## 需改进的
1. ⚠️ 图片上传接口性能需优化（大图压缩）
2. ⚠️ US-REVIEW-005估算不足，需改进复杂度评估
3. ⚠️ 评价审核与内容安全扫描需联动

## 行动项
| # | 改进项 | 负责人 | 截止日期 |
|---|--------|--------|----------|
| 1 | 图片压缩方案调研 | 前端 | Sprint 7 |
| 2 | 引入故事点校准会议 | SM | Sprint 7 Planning |
| 3 | 集成内容安全API | 后端 | Sprint 7 |
```

---

## 用例3：需求变更端到端流程

### 场景描述

在取消订单功能开发过程中，产品经理提出需求变更：增加"取消订单后优惠券退回"功能。本用例展示变更请求从提出→评审→实现→验证的全流程。

---

### 步骤1：变更请求

#### 触发Skill
- **Skill**: requirement-change
- **触发方式**: `/requirement-change`

#### 输入
```
变更请求：取消订单后优惠券退回
变更原因：用户投诉取消订单后优惠券丢失
影响范围：取消订单模块、优惠券模块
紧急程度：高（影响用户体验）
```

#### 产出：变更影响分析
```markdown
# 需求变更影响分析

## 变更概述
在取消订单流程中，增加优惠券退回逻辑。

## 影响范围

### 文档影响
| 文档 | 变更内容 | 工作量 |
|------|----------|--------|
| PRD | 增加优惠券退回规则 | 0.5天 |
| 用户故事 | 新增US-CANCEL-006 | 0.5天 |
| 验收标准 | 新增Gherkin场景 | 0.5天 |

### 代码影响
| 模块 | 变更内容 | 工作量 |
|------|----------|--------|
| OrderCancelService | 增加优惠券退回调用 | 1天 |
| CouponService | 新增退回接口 | 1天 |
| 数据库 | coupon_record增加退回状态 | 0.5天 |
| 前端 | 取消成功提示增加优惠券说明 | 0.5天 |

### 测试影响
| 测试类型 | 变更内容 | 工作量 |
|----------|----------|--------|
| 单元测试 | 新增退回场景测试 | 0.5天 |
| 集成测试 | 取消→退回联调 | 0.5天 |

## 总影响评估
- 总工作量：5.5天
- 影响Sprint：当前Sprint延期1天
- 风险：优惠券退回与库存恢复的一致性

## 建议
- ✅ 接受变更（用户投诉较多）
- ⚠️ 退回逻辑需保证与订单取消的事务一致性
- ⚠️ 建议增加优惠券退回对账脚本
```

---

### 步骤2：变更评审

#### 触发Skill
- **Skill**: requirement-review
- **触发方式**: `/requirement-review`

#### 产出
```markdown
# 变更评审报告

## 评审结果: 通过 ✅

## 技术方案确认
1. 优惠券退回与订单取消在同一事务中处理
2. 退回失败不阻塞取消流程（异步重试）
3. 增加对账脚本，每日校验退回一致性

## 排期调整
| 原计划 | 调整后 |
|--------|--------|
| Sprint 6 结束06-22 | 延期至06-23 |
| US-REVIEW-005 溢出 | 移至Sprint 7 |
```

---

### 步骤3：变更实现

#### 流程
```
requirement-change (变更分析)
  → requirement-review (变更评审)
    → architect (技术方案更新)
      → implement (代码实现)
        → code-review (代码审查)
          → test-case-generator (补充测试用例)
            → deploy-analyzer (部署评估)
```

#### 关键代码变更
```java
// OrderCancelService.java - 增加优惠券退回
@Transactional(rollbackFor = Exception.class)
public void cancelOrder(...) {
    // ... 原有逻辑 ...

    // 新增：优惠券退回
    if (order.getCouponId() != null) {
        try {
            couponService.returnCoupon(order.getCouponId(), userId);
        } catch (Exception e) {
            log.error("优惠券退回失败，转入异步重试", e);
            rabbitTemplate.convertAndSend("order.cancel", "order.cancel.coupon",
                new CouponReturnMsg(order.getCouponId(), userId));
        }
    }
}
```

#### 补充测试用例
```markdown
#### TC-CANCEL-021: 使用优惠券的订单取消后优惠券退回
| 前置条件 | 用户使用了10元优惠券下单 |
| 测试步骤 | 1. 取消订单<br>2. 查看优惠券列表 |
| 预期结果 | 1. 订单取消成功<br>2. 10元优惠券退回至账户<br>3. 优惠券状态恢复为"可用" |

#### TC-CANCEL-022: 优惠券退回失败异步重试
| 前置条件 | 模拟优惠券服务异常 |
| 测试步骤 | 1. 取消订单<br>2. 优惠券退回失败 |
| 预期结果 | 1. 订单取消不受影响<br>2. 优惠券异步重试<br>3. 最终退回成功 |
```

---

## 附录：工作流触发命令速查

| 命令 | Skill | 阶段 | 说明 |
|------|-------|------|------|
| `/requirement-analyzer` | 需求分析器 | 产品 | 分析需求生成PRD |
| `/user-story-generator` | 用户故事生成器 | 产品 | 生成用户故事 |
| `/acceptance-criteria-writer` | 验收标准编写 | 产品 | Gherkin格式验收标准 |
| `/requirement-review` | 需求评审 | 研发 | 需求完整性和可行性评审 |
| `/requirement-change` | 需求变更 | 研发 | 变更影响分析 |
| `/architect` | 架构设计 | 研发 | 系统架构设计 |
| `/db-designer` | 数据库设计 | 研发 | DDL和表结构设计 |
| `/api-designer` | API设计 | 研发 | REST API规范 |
| `/implement` | 功能实现 | 研发 | 业务代码生成 |
| `/code-review` | 代码审查 | 研发 | 代码质量审查 |
| `/test-case-generator` | 测试用例生成 | 测试 | 生成测试用例集 |
| `/deploy-analyzer` | 部署分析 | 运维 | 部署风险评估和方案 |
| `/project-status` | 项目状态 | 项目管理 | 周报/里程碑报告 |
| `/gate-check` | 质量门控 | 项目管理 | 阶段质量检查 |

## 附录：工作流自动化流转规则

```yaml
# 自动流转规则（摘自 skill-collaboration.yaml）
auto_flow:
  requirement-analyzer:
    next: user-story-generator
    condition: "PRD生成完成"

  user-story-generator:
    next: acceptance-criteria-writer
    condition: "用户故事列表生成完成"

  acceptance-criteria-writer:
    next: requirement-review
    condition: "验收标准编写完成"

  requirement-review:
    next: architect
    condition: "评审通过(review_result == 'passed')"
    on_failure: "返回产品补充需求"

  architect:
    next: [db-designer, api-designer]
    condition: "架构设计完成"
    parallel: true  # DB和API可并行设计

  implement:
    next: code-review
    condition: "代码开发完成"
    uses: [api-designer, entity-designer, crud-designer]

  code-review:
    next: test-case-generator
    condition: "审查通过"

  test-case-generator:
    next: deploy-analyzer
    condition: "测试用例生成完成"
```
