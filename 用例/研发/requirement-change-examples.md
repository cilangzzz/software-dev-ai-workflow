# 需求变更用例

## 用例1：新增会员等级功能

### 场景描述
业务方提出新增会员等级功能需求，研发团队需要分析变更影响并制定实施方案。

### 使用Skill
- **Skill**: requirement-change
- **触发方式**: `/requirement-change` 或自然语言 "需求变更"

### 完整提示词
```
/requirement-change

变更请求：需要新增会员等级功能，根据用户消费金额自动计算等级，
等级包括：普通、铜牌、银牌、金牌，不同等级享受不同折扣。

变更类型：feature
优先级：high
```

### 输入参数
| 参数名 | 类型 | 必填 | 值 |
|--------|------|------|-----|
| change_request | string | 是 | "需要新增会员等级功能，根据用户消费金额自动计算等级，等级包括：普通、铜牌、银牌、金牌，不同等级享受不同折扣。" |
| change_type | string | 否 | "feature" |
| priority | string | 否 | "high" |
| design_docs | string | 否 | "docs/data-model.md, docs/domain-design.md, docs/database-design.md" |

### 执行过程

#### 步骤1：变更解析
解析变更请求，提取变更点：

**变更点**：
- 新增会员等级实体（普通/铜牌/银牌/金牌）
- 新增等级计算逻辑（基于消费金额）
- 新增折扣计算逻辑
- 新增会员等级规则配置

**等级体系**：
- 普通会员：累计消费 < 500元
- 铜牌会员：累计消费 >= 500元，享受95折
- 银牌会员：累计消费 >= 2000元，享受9折
- 金牌会员：累计消费 >= 5000元，享受85折

#### 步骤2：影响分析
分析对设计文档的影响范围：

**数据模型影响**：
| 实体 | 变更类型 | 变更内容 |
|------|----------|----------|
| User | 修改 | 新增 memberLevel、totalSpent 字段 |
| Order | 修改 | 新增 discountAmount、memberLevel 字段 |
| MemberLevel | 新增 | 新建会员等级值对象 |
| DiscountRule | 新增 | 新建折扣规则实体 |

**领域设计影响**：
- 会员聚合：扩展，新增 MemberLevel 实体
- 订单聚合：修改，折扣计算逻辑变更
- MemberService：新增，会员等级计算服务

#### 步骤3：方案设计
生成变更方案和实施步骤：

**DDL变更**：
```sql
-- 用户表新增字段
ALTER TABLE users
ADD COLUMN member_level VARCHAR(20) DEFAULT 'NORMAL',
ADD COLUMN total_spent DECIMAL(12,2) DEFAULT 0;

-- 订单表新增字段
ALTER TABLE orders
ADD COLUMN discount_amount DECIMAL(10,2) DEFAULT 0,
ADD COLUMN member_level VARCHAR(20);

-- 新建会员等级规则表
CREATE TABLE member_level_rules (...);
```

**工作量估算**：18h

#### 步骤4：风险评估
识别变更风险和缓解措施：

| 风险项 | 风险等级 | 缓解措施 |
|--------|----------|----------|
| 数据迁移失败 | 高 | 完整备份、分批迁移、回滚预案 |
| 折扣计算错误 | 高 | 详尽单元测试、灰度发布验证 |
| API不兼容 | 中 | 版本号管理、渐进式升级 |

#### 步骤5：追溯记录
生成变更追溯文档：
- 变更编号: CR-20240115-001
- 关联需求: REQ-2024-015
- 关联ADR: ADR-012（待创建）
- 关联测试: TC-2024-015-001~010

#### 步骤6：协作调度
调度相关 Skill 执行后续任务：
- 调用 `/architect` 生成会员模块详细技术方案
- 调用 `/adr` 记录会员等级关键决策

### 最终输出
```markdown
# 需求变更影响分析报告

## 变更概览
- 变更编号: CR-20240115-001
- 变更类型: feature
- 优先级: high
- 申请时间: 2024-01-15 10:00:00

## 变更描述
新增会员等级功能，根据用户累计消费金额自动计算会员等级。

## 影响范围分析

### 数据模型影响
| 实体 | 变更类型 | 变更内容 | 影响等级 |
|------|----------|----------|----------|
| User | 修改 | 新增 memberLevel 字段 | 中 |
| Order | 修改 | 新增 discountAmount 字段 | 中 |
| MemberLevel | 新增 | 新建会员等级值对象 | 低 |

### 数据库设计影响
| 表名 | 变更类型 | DDL语句 | 数据迁移 |
|------|----------|---------|----------|
| users | ALTER | ADD COLUMN member_level | 需要 |
| orders | ALTER | ADD COLUMN discount_amount | 否 |
| member_level_rules | CREATE | 新建等级规则配置表 | 初始数据导入 |

## 风险评估
| 风险项 | 风险等级 | 影响范围 | 缓解措施 |
|--------|----------|----------|----------|
| 数据迁移失败 | 高 | 历史用户数据 | 完整备份、分批迁移 |
| 折扣计算错误 | 高 | 订单金额 | 详尽单元测试、灰度验证 |

## 实施方案
- 阶段1: 数据库变更 (Day 1)
- 阶段2: 后端开发 (Day 2-3)
- 阶段3: 前端开发 (Day 3-4)
- 阶段4: 测试验收 (Day 5)

## 回滚方案
```sql
ALTER TABLE users DROP COLUMN member_level, DROP COLUMN total_spent;
ALTER TABLE orders DROP COLUMN discount_amount, DROP COLUMN member_level;
DROP TABLE IF EXISTS member_level_rules;
```

## 审批建议
- [x] 需技术负责人审批
- [x] 需产品负责人审批
- [x] 需DBA审批
```

---

## 用例2：数据模型变更 - 新增商品评价功能

### 场景描述
需要新增商品评价功能，涉及新的实体和表结构。

### 使用Skill
- **Skill**: requirement-change
- **触发方式**: `/requirement-change` 或自然语言 "变更影响评估"

### 完整提示词
```
/requirement-change

变更请求：需要新增商品评价功能，用户可以对已完成的订单商品进行评价，
包括评分（1-5星）、评价内容、图片上传。评价需要审核后才能展示。

变更类型：feature
```

### 输入参数
| 参数名 | 类型 | 必填 | 值 |
|--------|------|------|-----|
| change_request | string | 是 | "需要新增商品评价功能，用户可以对已完成的订单商品进行评价，包括评分（1-5星）、评价内容、图片上传。评价需要审核后才能展示。" |
| change_type | string | 否 | "feature" |

### 执行过程

#### 步骤1：变更解析
提取变更点：
- 新增Review实体（评价聚合根）
- 新增ReviewImage实体（评价图片）
- 修改Product实体（新增评价统计属性）
- 修改Order实体（新增评价状态属性）

#### 步骤2：影响分析
**新增实体**：Review、ReviewImage
**修改实体**：Product（新增avgRating、reviewCount）、Order（新增reviewStatus）
**数据库变更**：新建reviews、review_images表

#### 步骤3：方案设计
生成DDL和数据模型设计。

#### 步骤4：风险评估
- 🟠 中风险：评价图片存储
- 🟢 低风险：新功能，无历史包袱

#### 步骤5：追溯记录
变更编号: CR-20240116-001

#### 步骤6：协作调度
下游影响：搜索服务、推荐服务、BI系统

### 最终输出
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

## 下游影响
| 系统 | 影响 | 负责人 |
|------|------|--------|
| 搜索服务 | 需索引评价数据 | 张三 |
| 推荐服务 | 可利用评价优化推荐 | 李四 |
| BI系统 | 新增评价分析维度 | 王五 |

**总计工作量**: 28h (约4人天)
```

---

## 用例3：字段变更 - 订单地址字段拆分

### 场景描述
需要对现有字段进行重构，涉及历史数据迁移。

### 使用Skill
- **Skill**: requirement-change
- **触发方式**: `/requirement-change` 或自然语言 "处理需求变更"

### 完整提示词
```
/requirement-change

变更请求：订单的收货地址字段需要拆分，原来的address字段是完整地址字符串，
现在需要拆分为：province、city、district、detail_address四个字段，
以便于地址分析和配送优化。

变更类型：refactor
优先级：high
```

### 输入参数
| 参数名 | 类型 | 必填 | 值 |
|--------|------|------|-----|
| change_request | string | 是 | "订单的收货地址字段需要拆分，原来的address字段是完整地址字符串，现在需要拆分为：province、city、district、detail_address四个字段" |
| change_type | string | 否 | "refactor" |
| priority | string | 否 | "high" |

### 执行过程

#### 步骤1：变更解析
提取变更点：
- 原字段: address (VARCHAR 500) - 完整地址字符串
- 新字段: province、city、district、detail_address

#### 步骤2：影响分析
**实体影响**：
- Order: address字段拆分为4个字段
- Address值对象: 属性变更

**数据库影响**：
- orders表: 新增4个字段
- order_history表: 同步变更

#### 步骤3：方案设计
**兼容性策略**：
1. 双写阶段：新旧字段同时写入
2. 双读阶段：优先读新字段，降级读旧字段
3. 清理阶段：确认无问题后删除旧字段

#### 步骤4：风险评估
| 风险项 | 风险等级 | 缓解措施 |
|--------|----------|----------|
| 历史地址解析失败 | 高 | 人工核对 + 地址解析服务兜底 |
| 下游系统不兼容 | 中 | 提前通知 + 兼容层 |

#### 步骤5：追溯记录
变更编号: CR-20240117-001

#### 步骤6：协作调度
通知下游系统：报表、物流系统

### 最终输出
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

## 兼容性策略

### 过渡期方案
1. **双写阶段**: 新旧字段同时写入
2. **双读阶段**: 优先读新字段，降级读旧字段
3. **清理阶段**: 确认无问题后删除旧字段

## 风险评估
| 风险项 | 风险等级 | 缓解措施 |
|--------|----------|----------|
| 历史地址解析失败 | 高 | 人工核对 + 地址解析服务兜底 |
| 下游系统不兼容 | 中 | 提前通知 + 兼容层 |

## 回滚方案
```sql
ALTER TABLE orders
DROP COLUMN province,
DROP COLUMN city,
DROP COLUMN district,
DROP COLUMN detail_address;
```
```

---

## 用例4：业务规则变更 - 优惠券使用规则调整

### 场景描述
业务规则变更，影响现有功能逻辑。

### 使用Skill
- **Skill**: requirement-change
- **触发方式**: `/requirement-change`

### 完整提示词
```
/requirement-change

变更请求：优惠券使用规则变更：
1. 原规则：全场通用券无门槛
2. 新规则：每张优惠券指定适用商品分类，满100元可用

变更类型：feature
```

### 执行过程

#### 步骤1：变更解析
提取变更点：
- 新增适用商品分类限制
- 新增使用门槛金额（满X元可用）

#### 步骤2：影响分析
**领域对象影响**：
- Coupon: 新增 applicableCategories、minOrderAmount 属性
- CouponService: 新增规则校验逻辑
- OrderService: 修改优惠券计算逻辑

#### 步骤3：方案设计
生成业务规则变更和数据库DDL。

#### 步骤4：风险评估
🟠 中风险：规则版本化管理、历史优惠券数据处理

#### 步骤5：追溯记录
变更编号: CR-20240118-001

#### 步骤6：协作调度
影响系统：订单服务、营销服务、前端

### 最终输出
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

## 业务规则变更
```gherkin
Feature: 优惠券使用规则

Scenario: 使用分类限制优惠券
  Given 优惠券限定"数码"分类商品
  When 用户购物车包含数码商品200元、服装商品100元
  Then 优惠券仅适用于数码商品的200元部分

Scenario: 使用门槛限制优惠券
  Given 优惠券设置满100元可用
  When 用户购物车商品总价为80元
  Then 用户无法使用该优惠券
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

### 场景描述
发现安全漏洞，需要紧急修复。

### 使用Skill
- **Skill**: requirement-change
- **触发方式**: `/requirement-change` 或自然语言 "紧急变更"

### 完整提示词
```
/requirement-change

变更请求：发现用户查询接口存在SQL注入漏洞，需要紧急修复

变更类型：fix
优先级：urgent
```

### 输入参数
| 参数名 | 类型 | 必填 | 值 |
|--------|------|------|-----|
| change_request | string | 是 | "发现用户查询接口存在SQL注入漏洞，需要紧急修复" |
| change_type | string | 否 | "fix" |
| priority | string | 否 | "urgent" |

### 执行过程

#### 步骤1：变更解析
提取变更点：
- 漏洞位置: UserService.java findByEmail方法
- 风险等级: 高危
- 影响范围: 用户数据安全

#### 步骤2：影响分析
**代码影响**：
- UserService.java: 修复SQL注入
- UserServiceTest.java: 新增安全测试

**工作量**: 1.5h

#### 步骤3：方案设计
```java
// 问题代码
String sql = "SELECT * FROM users WHERE email = '" + email + "'";

// 修复方案
@Query("SELECT u FROM User u WHERE u.email = :email")
User findByEmail(@Param("email") String email);
```

#### 步骤4：风险评估
🔴 高风险：需立即修复，影响用户数据安全

#### 步骤5：追溯记录
变更编号: CR-20240119-001

#### 步骤6：协作调度
紧急发布流程，无需常规审批

### 最终输出
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

## 修复方案
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