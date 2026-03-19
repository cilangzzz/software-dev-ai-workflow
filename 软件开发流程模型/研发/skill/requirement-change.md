# Skill: requirement-change

## 基本信息
- **名称**: requirement-change
- **版本**: 1.0.0
- **所属部门**: 研发部
- **优先级**: P0

## 功能描述
管理需求变更全流程，分析变更对数据模型、领域设计、数据库设计的影响，生成变更方案和追溯记录。确保变更的一致性和可追溯性。

## 触发条件
- 命令触发: `/requirement-change`
- 自然语言触发:
  - "需求变更"
  - "分析变更影响"
  - "变更影响评估"
  - "处理需求变更"

## 输入参数
| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| change_request | string | 是 | 变更请求描述 |
| change_type | string | 否 | 变更类型：feature / fix / refactor / migration |
| priority | string | 否 | 优先级：urgent / high / normal / low |
| design_docs | string | 否 | 设计文档路径（数据模型、领域设计、数据库设计） |

## 执行流程
1. **变更解析** - 解析变更请求，提取变更点
2. **影响分析** - 分析对设计文档的影响范围
3. **方案设计** - 生成变更方案和实施步骤
4. **风险评估** - 识别变更风险和缓解措施
5. **追溯记录** - 生成变更追溯文档
6. **协作调度** - 调度相关 Skill 执行后续任务

## 影响分析维度

### 数据模型影响分析
- 实体变更（新增、修改、删除）
- 属性变更（字段类型、约束、默认值）
- 关系变更（关联关系、基数）
- 枚举值变更

### 领域设计影响分析
- 聚合边界调整
- 领域服务变更
- 业务规则修改
- 领域事件变更

### 数据库设计影响分析
- 表结构变更（DDL）
- 索引变更
- 数据迁移需求
- 存储过程/触发器变更

### 代码影响分析
- 服务层变更
- API接口变更
- 前端组件变更
- 测试用例变更

## 输出格式

### 变更影响分析报告
```markdown
# 需求变更影响分析报告

## 变更概览
- 变更编号: CR-{timestamp}-{sequence}
- 变更类型: {feature/fix/refactor/migration}
- 优先级: {urgent/high/normal/low}
- 申请时间: {timestamp}
- 申请人: {requester}

## 变更描述
{详细描述变更内容和原因}

## 影响范围分析

### 数据模型影响
| 实体 | 变更类型 | 变更内容 | 影响等级 |
|------|----------|----------|----------|
| User | 修改 | 新增会员等级字段 | 中 |

### 领域设计影响
| 领域对象 | 变更类型 | 变更内容 | 影响等级 |
|----------|----------|----------|----------|
| 会员聚合 | 扩展 | 新增等级计算规则 | 高 |

### 数据库设计影响
| 表名 | 变更类型 | DDL语句 | 数据迁移 |
|------|----------|---------|----------|
| users | ALTER | ADD COLUMN member_level | 需要 |

### 代码影响分析
| 模块 | 文件 | 变更类型 | 工作量估算 |
|------|------|----------|------------|
| 用户服务 | UserService.java | 修改 | 2h |
| 前端 | MemberLevel.vue | 新增 | 4h |

## 实施方案

### 阶段1: 数据库变更
```sql
-- DDL语句
```

### 阶段2: 代码变更
- [ ] 更新实体类
- [ ] 实现业务逻辑
- [ ] 更新 API 接口

### 阶段3: 测试变更
- [ ] 更新单元测试
- [ ] 回归测试范围确认

## 风险评估

| 风险项 | 风险等级 | 影响范围 | 缓解措施 |
|--------|----------|----------|----------|
| 数据迁移失败 | 高 | 历史数据 | 备份数据库，分批迁移 |

## 依赖关系
### 上游依赖
- 无

### 下游影响
| 系统 | 影响 | 通知负责人 |
|------|------|------------|
| 订单服务 | 需同步会员折扣 | 张三 |

## 变更追溯
- 关联需求: REQ-{id}
- 关联ADR: ADR-{id}
- 关联测试: TC-{id}
- 关联发布: REL-{id}

## 回滚方案
{回滚步骤和脚本}

## 审批建议
- [ ] 需技术负责人审批
- [ ] 需产品负责人审批
- [ ] 需DBA审批
```

## 质量标准
- 影响分析覆盖率 >= 95%
- 风险识别准确率 >= 90%
- 变更方案可执行性 100%
- 追溯记录完整性 100%

## 使用示例

### 示例1：新增会员等级功能
**输入**:
```
change_request: 需要新增会员等级功能，根据用户消费金额自动计算等级，
等级包括：普通、铜牌、银牌、金牌，不同等级享受不同折扣。
change_type: feature
priority: high
design_docs: docs/data-model.md, docs/domain-design.md, docs/database-design.md
```

**输出**:
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
```

### 示例2：字段变更 - 订单地址字段拆分
**输入**:
```
change_request: 订单的收货地址字段需要拆分，原来的address字段是完整地址字符串，
现在需要拆分为：province、city、district、detail_address四个字段，
以便于地址分析和配送优化。
change_type: refactor
priority: high
```

**输出**:
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
UPDATE orders SET
    province = SUBSTRING_INDEX(SUBSTRING_INDEX(address, '省', 1), '省', -1),
    city = SUBSTRING_INDEX(SUBSTRING_INDEX(address, '市', 1), '省', -1),
    detail_address = address
WHERE address IS NOT NULL;
```

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

## 依赖工具
- Read - 读取设计文档和代码
- Write - 输出变更报告
- Grep - 搜索代码引用
- Glob - 查找相关文件
- Bash - 执行分析脚本

## 注意事项
- 变更影响分析需基于最新的设计文档
- 大型变更建议拆分为多个小型变更
- 数据库变更需提前与DBA沟通
- 变更方案需经评审后方可执行
- 保持变更追溯记录的完整性