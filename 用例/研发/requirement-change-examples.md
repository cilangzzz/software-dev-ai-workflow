# 需求变更用例

## 用例1：新增会员等级功能

### 输入
```
change_request: 需要新增会员等级功能，根据用户消费金额自动计算等级，
等级包括：普通、铜牌、银牌、金牌，不同等级享受不同折扣。
change_type: feature
priority: high
design_docs: docs/data-model.md, docs/domain-design.md, docs/database-design.md
```

### 输出
```markdown
# 需求变更影响分析报告

## 变更概览
- 变更编号: CR-20240115-001
- 变更类型: feature
- 优先级: high
- 申请时间: 2024-01-15 10:00:00

## 变更描述
新增会员等级功能，根据用户累计消费金额自动计算会员等级，等级体系包括：
- 普通会员：累计消费 < 500元
- 铜牌会员：累计消费 >= 500元，享受95折
- 银牌会员：累计消费 >= 2000元，享受9折
- 金牌会员：累计消费 >= 5000元，享受85折

## 影响范围分析

### 数据模型影响
| 实体 | 变更类型 | 变更内容 | 影响等级 |
|------|----------|----------|----------|
| User | 修改 | 新增 memberLevel 字段 | 中 |
| Order | 修改 | 新增 discountAmount 字段 | 中 |
| MemberLevel | 新增 | 新建会员等级值对象 | 低 |
| DiscountRule | 新增 | 新建折扣规则实体 | 中 |

### 领域设计影响
| 领域对象 | 变更类型 | 变更内容 | 影响等级 |
|----------|----------|----------|----------|
| 会员聚合 | 扩展 | 新增 MemberLevel 实体 | 高 |
| 订单聚合 | 修改 | 折扣计算逻辑变更 | 高 |
| MemberService | 新增 | 会员等级计算服务 | 中 |
| MemberLevelChanged | 新增 | 会员等级变更领域事件 | 低 |

### 数据库设计影响
| 表名 | 变更类型 | DDL语句 | 数据迁移 |
|------|----------|---------|----------|
| users | ALTER | ADD COLUMN member_level | 需要，计算历史数据等级 |
| orders | ALTER | ADD COLUMN discount_amount | 否，仅影响新订单 |
| member_level_rules | CREATE | 新建等级规则配置表 | 初始数据导入 |

**DDL详情**:
```sql
-- 1. 用户表新增字段
ALTER TABLE users
ADD COLUMN member_level VARCHAR(20) DEFAULT 'NORMAL' COMMENT '会员等级',
ADD COLUMN total_spent DECIMAL(12,2) DEFAULT 0 COMMENT '累计消费金额';

-- 2. 订单表新增字段
ALTER TABLE orders
ADD COLUMN discount_amount DECIMAL(10,2) DEFAULT 0 COMMENT '折扣金额',
ADD COLUMN member_level VARCHAR(20) COMMENT '下单时会员等级';

-- 3. 新建会员等级规则表
CREATE TABLE member_level_rules (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    level_name VARCHAR(20) NOT NULL COMMENT '等级名称',
    min_amount DECIMAL(12,2) NOT NULL COMMENT '最低消费金额',
    discount_rate DECIMAL(3,2) NOT NULL COMMENT '折扣率',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_min_amount (min_amount)
);

-- 4. 初始数据
INSERT INTO member_level_rules (level_name, min_amount, discount_rate) VALUES
('NORMAL', 0, 1.00),
('BRONZE', 500, 0.95),
('SILVER', 2000, 0.90),
('GOLD', 5000, 0.85);
```

**数据迁移脚本**:
```sql
-- 计算历史用户的累计消费和等级
UPDATE users u
SET total_spent = (
    SELECT COALESCE(SUM(total_amount), 0)
    FROM orders
    WHERE user_id = u.id AND status = 'PAID'
);

UPDATE users
SET member_level = CASE
    WHEN total_spent >= 5000 THEN 'GOLD'
    WHEN total_spent >= 2000 THEN 'SILVER'
    WHEN total_spent >= 500 THEN 'BRONZE'
    ELSE 'NORMAL'
END;
```

### 代码影响分析
| 模块 | 文件 | 变更类型 | 工作量估算 |
|------|------|----------|------------|
| 用户域 | User.java | 修改 | 0.5h |
| 用户域 | MemberLevel.java | 新增 | 1h |
| 用户域 | MemberService.java | 新增 | 3h |
| 订单域 | Order.java | 修改 | 0.5h |
| 订单域 | DiscountCalculator.java | 新增 | 2h |
| 订单域 | OrderService.java | 修改 | 2h |
| 前端 | MemberCenter.vue | 新增 | 4h |
| 前端 | OrderConfirm.vue | 修改 | 2h |
| 测试 | MemberServiceTest.java | 新增 | 2h |

**总计工作量**: 18h

## 实施方案

### 阶段1: 数据库变更 (Day 1)
1. 在测试环境执行 DDL
2. 执行数据迁移脚本
3. 验证数据迁移结果
4. 备份生产数据
5. 在生产环境执行变更

### 阶段2: 后端开发 (Day 2-3)
1. 实现会员等级值对象
2. 实现会员等级计算服务
3. 实现折扣计算逻辑
4. 更新 API 接口
5. 编写单元测试

### 阶段3: 前端开发 (Day 3-4)
1. 开发会员中心页面
2. 更新订单确认页面
3. 联调测试

### 阶段4: 测试验收 (Day 5)
1. 功能测试
2. 回归测试
3. 性能测试
4. UAT验收

## 风险评估

| 风险项 | 风险等级 | 影响范围 | 缓解措施 |
|--------|----------|----------|----------|
| 数据迁移失败 | 高 | 历史用户数据 | 1. 完整备份 2. 分批迁移 3. 回滚预案 |
| 折扣计算错误 | 高 | 订单金额 | 1. 详尽的单元测试 2. 灰度发布验证 |
| API不兼容 | 中 | 前端调用 | 版本号管理，渐进式升级 |
| 性能影响 | 中 | 订单接口 | 1. 缓存会员等级 2. 异步计算 |

## 回滚方案

### 数据库回滚
```sql
-- 回滚用户表
ALTER TABLE users
DROP COLUMN member_level,
DROP COLUMN total_spent;

-- 回滚订单表
ALTER TABLE orders
DROP COLUMN discount_amount,
DROP COLUMN member_level;

-- 删除新表
DROP TABLE IF EXISTS member_level_rules;
```

### 代码回滚
- 通过 Git 回滚到变更前版本
- 保留功能开关，可快速关闭新功能

## 依赖关系
### 上游依赖
- 无

### 下游影响
| 系统 | 影响 | 通知负责人 | 状态 |
|------|------|------------|------|
| 订单服务 | 需同步会员折扣逻辑 | 张三 | 待通知 |
| 支付服务 | 支付金额计算变更 | 李四 | 待通知 |
| BI报表 | 新增会员等级维度 | 王五 | 待通知 |
| 推荐服务 | 可基于等级优化推荐 | 赵六 | 待通知 |

## 变更追溯
- 关联需求: REQ-2024-015
- 关联ADR: ADR-012（待创建）
- 关联测试: TC-2024-015-001~010
- 关联发布: REL-2024-02

## 审批建议
- [x] 需技术负责人审批 - 王工
- [x] 需产品负责人审批 - 刘经理
- [x] 需DBA审批 - 张DBA
- [ ] 需安全审批 - 低风险，可豁免

## 下一步行动
1. 发起变更评审会议
2. 创建 ADR-012 记录架构决策
3. 通知下游系统负责人
4. 安排开发资源
```

---

## 用例2：数据模型变更 - 新增商品评价功能

### 输入
```
change_request: 需要新增商品评价功能，用户可以对已完成的订单商品进行评价，
包括评分（1-5星）、评价内容、图片上传。评价需要审核后才能展示。
change_type: feature
design_docs:
  - docs/data-model.md
  - docs/domain-design.md
  - docs/database-schema.sql
```

### 输出
```markdown
# 需求变更影响分析报告

## 变更概览
- 变更编号: CR-20240116-001
- 变更类型: feature
- 优先级: normal
- 申请时间: 2024-01-16 14:00:00

## 变更描述
新增商品评价功能，具体需求：
1. 用户可对已完成的订单商品进行评价
2. 评价包含：评分（1-5星）、评价内容（最长500字）、图片（最多9张）
3. 评价需经过审核才能公开展示
4. 商品详情页展示评价统计和列表

## 影响范围分析

### 数据模型影响
| 实体 | 变更类型 | 变更内容 | 影响等级 |
|------|----------|----------|----------|
| Review | 新增 | 评价聚合根 | 高 |
| ReviewImage | 新增 | 评价图片实体 | 中 |
| Product | 修改 | 新增评价统计属性 | 中 |
| Order | 修改 | 新增评价状态属性 | 低 |

**领域模型变更**:
```
┌─────────────────────────────────────────────────────────────────────┐
│                         评价聚合 (Review)                            │
├─────────────────────────────────────────────────────────────────────┤
│  Review (聚合根)                                                     │
│  - id: ReviewId                                                      │
│  - orderId: OrderId                                                  │
│  - productId: ProductId                                              │
│  - userId: UserId                                                    │
│  - rating: Rating (1-5)                                              │
│  - content: ReviewContent                                            │
│  - images: List<ReviewImage>                                         │
│  - status: ReviewStatus (PENDING/APPROVED/REJECTED)                  │
│  - createdAt: DateTime                                               │
│  - approvedAt: DateTime                                              │
│                                                                      │
│  ReviewImage (实体)                                                   │
│  - id: ImageId                                                       │
│  - url: URL                                                          │
│  - order: int                                                        │
│                                                                      │
│  值对象:                                                              │
│  - Rating: 1-5的整数                                                 │
│  - ReviewContent: 最长500字的文本                                    │
│  - ReviewStatus: 枚举 (PENDING/APPROVED/REJECTED)                        │
└─────────────────────────────────────────────────────────────────────┘
```

### 数据库设计影响
| 表名 | 变更类型 | 说明 | 数据迁移 |
|------|----------|------|----------|
| reviews | CREATE | 评价主表 | 否 |
| review_images | CREATE | 评价图片表 | 否 |
| products | ALTER | 新增评价统计字段 | 需要计算历史数据 |

**DDL详情**:
```sql
-- 1. 评价主表
CREATE TABLE reviews (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    order_id BIGINT NOT NULL COMMENT '订单ID',
    product_id BIGINT NOT NULL COMMENT '商品ID',
    user_id BIGINT NOT NULL COMMENT '用户ID',
    rating TINYINT NOT NULL COMMENT '评分1-5',
    content VARCHAR(500) COMMENT '评价内容',
    status VARCHAR(20) DEFAULT 'PENDING' COMMENT '状态',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    approved_at DATETIME COMMENT '审核时间',
    approved_by BIGINT COMMENT '审核人',

    INDEX idx_product (product_id),
    INDEX idx_user (user_id),
    INDEX idx_order (order_id),
    UNIQUE KEY uk_order_product (order_id, product_id)
) COMMENT '商品评价表';

-- 2. 评价图片表
CREATE TABLE review_images (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    review_id BIGINT NOT NULL COMMENT '评价ID',
    image_url VARCHAR(500) NOT NULL COMMENT '图片URL',
    sort_order INT DEFAULT 0 COMMENT '排序',

    INDEX idx_review (review_id)
) COMMENT '评价图片表';

-- 3. 商品表新增统计字段
ALTER TABLE products
ADD COLUMN avg_rating DECIMAL(2,1) DEFAULT 0 COMMENT '平均评分',
ADD COLUMN review_count INT DEFAULT 0 COMMENT '评价数量';
```

### 代码影响分析
| 模块 | 文件 | 变更类型 | 工作量 |
|------|------|----------|--------|
| 评价域 | Review.java | 新增 | 2h |
| 评价域 | ReviewRepository.java | 新增 | 1h |
| 评价域 | ReviewService.java | 新增 | 4h |
| 评价域 | ReviewController.java | 新增 | 2h |
| 商品域 | Product.java | 修改 | 0.5h |
| 商品域 | ProductService.java | 修改 | 1h |
| 订单域 | Order.java | 修改 | 0.5h |
| 前端 | ReviewForm.vue | 新增 | 4h |
| 前端 | ProductReviews.vue | 新增 | 4h |
| 前端 | ReviewManagement.vue | 新增 | 6h |
| 测试 | ReviewServiceTest.java | 新增 | 3h |

**总计工作量**: 28h (约4人天)

## 下游影响
| 系统 | 影响 | 负责人 |
|------|------|--------|
| 搜索服务 | 需索引评价数据 | 张三 |
| 推荐服务 | 可利用评价优化推荐 | 李四 |
| BI系统 | 新增评价分析维度 | 王五 |
```

---

## 用例3：字段变更 - 订单地址字段拆分

### 输入
```
change_request: 订单的收货地址字段需要拆分，原来的address字段是完整地址字符串，
现在需要拆分为：province、city、district、detail_address四个字段，
以便于地址分析和配送优化。
change_type: refactor
priority: high
```

### 输出
```markdown
# 需求变更影响分析报告

## 变更概览
- 变更编号: CR-20240117-001
- 变更类型: refactor
- 优先级: high
- 申请时间: 2024-01-17 09:00:00

## 变更描述
订单收货地址字段重构：
- 原字段: address (VARCHAR 500) - 完整地址字符串
- 新字段:
  - province (VARCHAR 50) - 省
  - city (VARCHAR 50) - 市
  - district (VARCHAR 50) - 区
  - detail_address (VARCHAR 300) - 详细地址

## 影响范围分析

### 数据模型影响
| 实体 | 变更类型 | 变更内容 | 影响等级 |
|------|----------|----------|----------|
| Order | 修改 | address 字段拆分为4个字段 | 高 |
| Address | 修改 | 值对象属性变更 | 高 |

### 数据库设计影响
| 表名 | 变更类型 | 影响等级 | 数据迁移 |
|------|----------|----------|----------|
| orders | ALTER | 高 | 需要 - 解析历史地址 |
| order_history | ALTER | 中 | 需要 - 同步变更 |

**DDL详情**:
```sql
-- 1. 新增字段
ALTER TABLE orders
ADD COLUMN province VARCHAR(50) COMMENT '省',
ADD COLUMN city VARCHAR(50) COMMENT '市',
ADD COLUMN district VARCHAR(50) COMMENT '区',
ADD COLUMN detail_address VARCHAR(300) COMMENT '详细地址';

-- 2. 数据迁移（使用地址解析服务）
-- 注意：此为示意，实际需要调用地址解析API
UPDATE orders SET
    province = SUBSTRING_INDEX(SUBSTRING_INDEX(address, '省', 1), '省', -1),
    city = SUBSTRING_INDEX(SUBSTRING_INDEX(address, '市', 1), '省', -1),
    detail_address = address
WHERE address IS NOT NULL;

-- 3. 验证迁移结果
SELECT COUNT(*) as unmigrated_count
FROM orders
WHERE address IS NOT NULL
  AND (province IS NULL OR city IS NULL);

-- 4. 保留原字段一段时间后删除
-- ALTER TABLE orders DROP COLUMN address;
```

### 代码影响分析
| 模块 | 文件 | 变更类型 | 影响说明 |
|------|------|----------|----------|
| 订单域 | Order.java | 修改 | 字段变更 |
| 订单域 | Address.java | 重构 | 值对象属性变更 |
| 订单域 | OrderRepository.java | 修改 | 查询语句变更 |
| 订单域 | OrderService.java | 修改 | 业务逻辑适配 |
| 前端 | OrderConfirm.vue | 修改 | 地址表单组件 |
| 前端 | AddressSelector.vue | 修改 | 地址选择组件 |
| 报表 | RegionReport.java | 修改 | 区域统计适配 |

## 兼容性策略

### 过渡期方案
1. **双写阶段**: 新旧字段同时写入
2. **双读阶段**: 优先读新字段，降级读旧字段
3. **清理阶段**: 确认无问题后删除旧字段

```java
// 过渡期代码示例
public class Order {
    private String address;           // 旧字段，标记 @Deprecated
    private String province;          // 新字段
    private String city;
    private String district;
    private String detailAddress;

    // 兼容读取
    public String getFullAddress() {
        if (province != null) {
            return province + city + district + detailAddress;
        }
        return address; // 降级读旧字段
    }
}
```

## 风险评估

| 风险项 | 风险等级 | 缓解措施 |
|--------|----------|----------|
| 历史地址解析失败 | 高 | 人工核对 + 地址解析服务兜底 |
| 下游系统不兼容 | 中 | 提前通知 + 兼容层 |
| 性能影响 | 低 | 索引优化 |

## 回滚方案
```sql
-- 回滚：删除新增字段
ALTER TABLE orders
DROP COLUMN province,
DROP COLUMN city,
DROP COLUMN district,
DROP COLUMN detail_address;
```
```

---

## 用例4：业务规则变更 - 优惠券使用规则调整

### 输入
```
change_request: 优惠券使用规则变更：
1. 原规则：全场通用券无门槛
2. 新规则：每张优惠券指定适用商品分类，满100元可用
change_type: feature
```

### 输出
```markdown
# 需求变更影响分析报告

## 变更概览
- 变更编号: CR-20240118-001
- 变更类型: feature
- 变更范围: 营销域

## 变更描述
优惠券使用规则扩展：
- 新增适用商品分类限制
- 新增使用门槛金额（满X元可用）

## 影响范围分析

### 领域设计影响
| 领域对象 | 变更内容 | 影响等级 |
|----------|----------|----------|
| Coupon | 新增 applicableCategories 属性 | 高 |
| Coupon | 新增 minOrderAmount 属性 | 高 |
| CouponService | 新增规则校验逻辑 | 高 |
| OrderService | 修改优惠券计算逻辑 | 高 |

### 业务规则变更
```gherkin
Feature: 优惠券使用规则

Background:
  Given 用户已选择商品

Scenario: 使用分类限制优惠券
  Given 优惠券限定"数码"分类商品
  When 用户购物车包含数码商品200元、服装商品100元
  Then 优惠券仅适用于数码商品的200元部分

Scenario: 使用门槛限制优惠券
  Given 优惠券设置满100元可用
  When 用户购物车商品总价为80元
  Then 用户无法使用该优惠券
  And 提示"差20元可用"
```

### 数据库设计影响
| 表名 | 变更类型 | DDL |
|------|----------|-----|
| coupons | ALTER | 新增字段 |
| coupon_categories | CREATE | 关联表 |

```sql
-- 1. 优惠券表新增字段
ALTER TABLE coupons
ADD COLUMN min_order_amount DECIMAL(10,2) DEFAULT 0 COMMENT '最低订单金额';

-- 2. 新建优惠券分类关联表
CREATE TABLE coupon_categories (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    coupon_id BIGINT NOT NULL,
    category_id BIGINT NOT NULL,
    UNIQUE KEY uk_coupon_category (coupon_id, category_id)
);
```

## 实施步骤
1. 数据库变更（低峰期执行）
2. 后端规则引擎开发
3. 管理后台配置界面
4. 前端展示适配
5. 历史优惠券数据处理
```

---

## 用例5：紧急变更 - 安全漏洞修复

### 输入
```
change_request: 发现用户查询接口存在SQL注入漏洞，需要紧急修复
change_type: fix
priority: urgent
```

### 输出
```markdown
# 需求变更影响分析报告

## 变更概览
- 变更编号: CR-20240119-001
- 变更类型: fix
- 优先级: urgent
- 申请时间: 2024-01-19 08:00:00

## 变更描述
紧急修复用户查询接口SQL注入漏洞：
- 漏洞位置: UserService.java findByEmail方法
- 风险等级: 高危
- 影响范围: 用户数据安全

## 影响范围分析

### 代码影响
| 文件 | 变更内容 | 工作量 |
|------|----------|--------|
| UserService.java | 修复SQL注入 | 0.5h |
| UserServiceTest.java | 新增安全测试 | 1h |

### 修复方案
```java
// 问题代码
String sql = "SELECT * FROM users WHERE email = '" + email + "'";

// 修复方案
@Query("SELECT u FROM User u WHERE u.email = :email")
User findByEmail(@Param("email") String email);
```

## 实施计划
1. 立即修复代码 (30分钟内)
2. 代码审查 (15分钟)
3. 部署测试环境验证 (30分钟)
4. 紧急发布生产 (1小时内)

## 验证方案
```bash
# 安全测试
sqlmap -u "http://api.example.com/users?email=test@example.com" --level=5
```

## 回归测试范围
- 用户登录接口
- 用户注册接口
- 用户信息查询接口
```