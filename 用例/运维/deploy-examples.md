# 部署分析用例

## 用例1：生产环境部署分析

### 输入
```
版本: v2.3.0
环境: prod
变更内容:
- 新增商品评价功能
- 修复订单支付超时问题
- 升级Redis客户端版本
- 数据库Schema变更：添加评价表
- 依赖升级：log4j 2.14.1 → 2.17.1
```

### 输出
```markdown
# 部署分析报告

## 版本信息
- 版本号: v2.3.0
- 目标环境: prod (生产环境)
- 计划部署时间: 2024-01-20 00:00

## 变更摘要

| 类型 | 数量 | 详情 |
|------|------|------|
| 新功能 | 1 | 商品评价功能 |
| Bug修复 | 1 | 订单支付超时 |
| 依赖升级 | 2 | Redis客户端, log4j |
| 破坏性变更 | 1 | 数据库Schema变更 |
| 配置变更 | 1 | Redis连接参数 |

## 风险评估

### 🔴 高风险项
| 风险 | 影响 | 概率 | 缓解措施 |
|------|------|------|---------|
| 数据库Schema变更 | 服务启动失败 | 高 | 先执行DDL，再部署服务，保留回滚脚本 |
| Redis客户端升级 | 连接失败 | 中 | 提前在staging验证，准备配置回滚方案 |
| log4j版本升级 | 日志格式变化 | 低 | 已在staging验证兼容性 |

### 🟠 中风险项
| 风险 | 影响 | 概率 | 缓解措施 |
|------|------|------|---------|
| 评价功能影响性能 | 响应变慢 | 中 | 添加评价索引，开启缓存 |
| 新API未配置限流 | 系统过载 | 中 | 预先配置限流规则 |

## 部署前检查清单

### 环境检查
- [ ] 生产服务器资源充足（CPU<70%, 内存<80%）
- [ ] 数据库备份已完成
- [ ] Redis配置参数已确认
- [ ] 监控告警规则已更新
- [ ] 回滚脚本已准备

### 依赖检查
- [ ] log4j 2.17.1已在staging验证
- [ ] Redis客户端兼容性已验证
- [ ] 数据库迁移脚本已审核

### 人员准备
- [ ] DBA已确认数据库变更时间
- [ ] 运维人员已到位
- [ ] 开发人员待命支持
- [ ] 客服团队已通知新功能

## 部署计划

### 时间线

```
00:00 ─────────────────────────────────────────────────────────────
       │
00:30  │ Phase 1: 数据库变更
       │   - 执行DDL（添加评价表）
       │   - 验证表结构
       │   - 创建索引
       │
01:00  │ Phase 2: 服务部署
       │   - 灰度发布10%流量
       │   - 监控错误率
       │   - 验证评价功能
       │
01:30  │ Phase 3: 扩大灰度
       │   - 扩大到50%流量
       │   - 持续监控
       │   - 验证支付功能
       │
02:00  │ Phase 4: 全量发布
       │   - 100%流量切换
       │   - 关闭旧版本
       │   - 全量验证
       │
02:30  │ Phase 5: 部署完成
       │   - 更新部署记录
       │   - 通知相关团队
       │
03:00 ─────────────────────────────────────────────────────────────
```

### 部署步骤

#### Phase 1: 数据库变更 (00:00-01:00)
```sql
-- 1. 创建评价表
CREATE TABLE product_reviews (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    product_id BIGINT NOT NULL,
    user_id BIGINT NOT NULL,
    rating TINYINT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    content TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_product_id (product_id),
    INDEX idx_user_id (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. 验证表结构
DESC product_reviews;

-- 3. 回滚脚本（备份）
DROP TABLE IF EXISTS product_reviews;
```

#### Phase 2: 服务部署 (01:00-01:30)
```bash
# 1. 拉取新版本镜像
docker pull registry.example.com/shop-api:v2.3.0

# 2. 灰度部署（10%流量）
kubectl set image deployment/shop-api \
  shop-api=registry.example.com/shop-api:v2.3.0 \
  --record

# 3. 验证健康状态
kubectl rollout status deployment/shop-api

# 4. 检查日志
kubectl logs -f deployment/shop-api --tail=100
```

## 验证步骤

### 功能验证
| 功能 | 验证方法 | 预期结果 |
|------|----------|----------|
| 商品评价 | 提交一条评价 | 评价成功，评分统计正确 |
| 支付功能 | 发起支付 | 支付成功，无超时 |
| 订单查询 | 查询历史订单 | 数据正确，响应<1s |
| 用户登录 | 登录测试账号 | 登录成功 |

### 性能验证
| 指标 | 正常值 | 告警阈值 |
|------|--------|----------|
| API响应时间 | <500ms | >2s |
| 错误率 | <0.1% | >1% |
| CPU使用率 | <60% | >80% |
| 内存使用率 | <70% | >85% |
| 数据库连接数 | <100 | >200 |

## 回滚方案

### 回滚条件
满足以下任一条件立即回滚：
1. 错误率 > 1% 持续5分钟
2. 核心功能不可用
3. 数据一致性问题
4. 响应时间 > 5秒

### 回滚步骤
```bash
# 1. 服务回滚
kubectl rollout undo deployment/shop-api

# 2. 验证回滚成功
kubectl rollout status deployment/shop-api

# 3. 数据库回滚（如需要）
mysql -u root -p < /backup/rollback_v2.3.0.sql

# 4. 通知团队
curl -X POST $WEBHOOK_URL -d '{"msg": "v2.3.0 已回滚"}'
```

### 回滚时间要求
- 服务回滚: < 5分钟
- 数据库回滚: < 15分钟
- 完整恢复: < 30分钟

## 监控配置

### 新增告警规则
```yaml
# 商品评价相关
- alert: ReviewSubmitHighErrorRate
  expr: rate(review_submit_errors[5m]) > 0.01
  for: 5m
  labels:
    severity: warning
  annotations:
    summary: "评价提交错误率过高"

- alert: ReviewApiLatencyHigh
  expr: histogram_quantile(0.99, rate(review_api_duration_bucket[5m])) > 2
  for: 5m
  labels:
    severity: warning
  annotations:
    summary: "评价API响应延迟过高"
```

## 值班安排

| 时间段 | 值班人员 | 联系方式 |
|--------|----------|----------|
| 00:00-03:00 | 张三 | 138xxxx1234 |
| 03:00-06:00 | 李四 | 138xxxx5678 |
| 06:00-09:00 | 王五 | 138xxxx9012 |

## 建议与注意事项

1. **部署时间**: 建议在业务低峰期（凌晨）执行
2. **沟通**: 提前通知客服团队新功能上线
3. **功能开关**: 建议为评价功能添加开关，必要时可快速关闭
4. **数据迁移**: 评价表初始为空，无需数据迁移
5. **测试账号**: 准备测试账号用于功能验证
```

---

## 用例2：CI/CD故障诊断

### 输入
```
CI日志:
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.22.2:test
[ERROR] There are test failures.
[ERROR]
[ERROR] com.example.UserServiceTest > testRegisterUser FAILED
[ERROR]     java.lang.AssertionError: Expected: 200 Actual: 500
[ERROR]     at com.example.UserServiceTest.testRegisterUser(UserServiceTest.java:45)
[ERROR]
[ERROR] Please refer to /home/runner/work/myapp/target/surefire-reports for the individual test results.
[ERROR]
[ERROR] -> [Help 1]
[ERROR]
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR]
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
```

### 输出
```markdown
# CI流水线诊断报告

## 问题摘要
- 失败阶段: test (测试阶段)
- 错误类型: 测试用例失败
- 严重程度: 🔴 高（阻塞构建）

## 错误详情

### 失败测试
```
com.example.UserServiceTest > testRegisterUser FAILED
java.lang.AssertionError: Expected: 200 Actual: 500
```

### 分析结论
测试用例 `testRegisterUser` 期望HTTP状态码200，但实际返回500（服务器内部错误）。

## 根因分析

### 可能原因（按概率排序）

| # | 原因 | 概率 | 验证方法 |
|---|------|------|---------|
| 1 | 测试环境数据库未启动/连接失败 | 高 | 检查CI环境变量和数据库配置 |
| 2 | 代码改动引入bug | 中 | 查看最近提交的代码变更 |
| 3 | 测试数据准备问题 | 中 | 检查测试前置条件 |
| 4 | 依赖服务不可用 | 低 | 检查外部服务状态 |

## 修复建议

### 立即检查
```bash
# 1. 查看详细测试日志
mvn test -Dtest=UserServiceTest#testRegisterUser -X

# 2. 检查CI环境数据库配置
echo $DATABASE_URL
echo $DATABASE_USERNAME

# 3. 本地重现测试
mvn test -Dtest=UserServiceTest
```

### 可能的修复方案

#### 场景1: 数据库连接问题
```yaml
# 检查CI配置中的数据库设置
# .github/workflows/ci.yml
services:
  mysql:
    image: mysql:8.0
    env:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: test_db
    ports:
      - 3306:3306
    options: --health-cmd="mysqladmin ping" --health-interval=10s --health-timeout=5s --health-retries=3
```

#### 场景2: 代码bug
```java
// 检查 UserServiceTest.java:45
// 可能的问题：
// 1. 注册接口返回500
// 2. Mock数据不完整
// 3. 测试用户已存在

@Test
void testRegisterUser() {
    // 确保测试数据正确
    RegisterRequest request = new RegisterRequest();
    request.setEmail("test" + UUID.randomUUID() + "@example.com"); // 使用唯一邮箱
    request.setPassword("Test@123");

    ResponseEntity<Response> response = userService.register(request);
    assertEquals(200, response.getStatusCodeValue()); // 第45行
}
```

## 构建优化建议

### 当前性能问题
| 阶段 | 耗时 | 可优化点 |
|------|------|---------|
| 依赖下载 | 3m20s | 配置本地Maven仓库缓存 |
| 编译 | 1m15s | 开启并行编译 |
| 测试 | 4m30s | 排除不必要的集成测试 |
| 打包 | 0m45s | - |

### 优化方案
```yaml
# CI配置优化
- name: Cache Maven packages
  uses: actions/cache@v3
  with:
    path: ~/.m2
    key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
    restore-keys: ${{ runner.os }}-m2

- name: Build with Maven
  run: mvn -B package --file pom.xml -T 4  # 并行编译
```

## 下一步行动

1. **立即**: 检查CI环境的数据库服务状态
2. **本地重现**: 在本地运行失败的测试用例
3. **查看代码变更**: `git log --oneline -5` 查看最近提交
4. **修复后**: 确保所有测试通过再重新提交
```

---

## 用例3：多服务部署协调

### 输入
```
部署需求：
- 前端服务: user-web v1.2.0
- 后端API: user-api v2.0.0
- 网关服务: gateway v1.5.0
依赖关系：前端依赖网关，网关依赖后端API
```

### 输出
```markdown
# 多服务部署协调报告

## 服务依赖图

```
                  ┌─────────────┐
                  │  user-web   │ v1.2.0
                  │   (前端)    │
                  └──────┬──────┘
                         │ 依赖
                         ▼
                  ┌─────────────┐
                  │   gateway   │ v1.5.0
                  │   (网关)    │
                  └──────┬──────┘
                         │ 依赖
                         ▼
                  ┌─────────────┐
                  │  user-api   │ v2.0.0
                  │  (后端API)  │
                  └─────────────┘
```

## 部署顺序

### 推荐顺序: 自底向上
1. user-api (后端API) - 最底层，无依赖
2. gateway (网关) - 依赖API
3. user-web (前端) - 依赖网关

## 部署计划

| 阶段 | 服务 | 版本 | 时间窗口 | 验证要点 |
|------|------|------|----------|----------|
| 1 | user-api | v2.0.0 | 00:00-00:30 | API健康检查、功能验证 |
| 2 | gateway | v1.5.0 | 00:30-01:00 | 路由配置、限流验证 |
| 3 | user-web | v1.2.0 | 01:00-01:30 | 页面访问、端到端测试 |

## 兼容性检查

### API变更检查
| 变更类型 | 影响范围 | 处理方案 |
|----------|----------|----------|
| 新增接口 | 无破坏性 | 正常部署 |
| 接口废弃 | 需确认调用方 | 保留旧版本1个月 |
| 参数变更 | gateway需同步更新 | 协调更新 |

### 版本兼容矩阵
| user-web | gateway | user-api | 兼容性 |
|----------|---------|----------|--------|
| v1.2.0 | v1.5.0 | v2.0.0 | ✅ 目标版本 |
| v1.1.0 | v1.4.0 | v1.9.0 | ✅ 当前版本 |
| v1.2.0 | v1.4.0 | v1.9.0 | ⚠️ 部分功能不可用 |

## 部署步骤

### Phase 1: 部署 user-api v2.0.0
```bash
# 1. 备份当前版本
kubectl get deployment user-api -o yaml > backup-user-api.yaml

# 2. 部署新版本
kubectl set image deployment/user-api user-api=user-api:v2.0.0

# 3. 验证部署
kubectl rollout status deployment/user-api
kubectl logs -f deployment/user-api --tail=50

# 4. API健康检查
curl -f http://user-api:8080/health || exit 1
```

### Phase 2: 部署 gateway v1.5.0
```bash
# 1. 更新路由配置
kubectl apply -f gateway-config-v1.5.yaml

# 2. 部署新版本
kubectl set image deployment/gateway gateway=gateway:v1.5.0

# 3. 验证路由
curl -f http://gateway:8080/api/users/health

# 4. 验证限流
ab -n 100 -c 10 http://gateway:8080/api/test
```

### Phase 3: 部署 user-web v1.2.0
```bash
# 1. 部署新版本
kubectl set image deployment/user-web user-web=user-web:v1.2.0

# 2. 清除CDN缓存
curl -X PURGE http://cdn.example.com/static/*

# 3. 端到端测试
playwright test e2e/user-flow.spec.ts
```

## 回滚预案

### 单服务回滚
```bash
# 回滚单个服务
kubectl rollout undo deployment/user-api
```

### 全链路回滚
```bash
# 按逆序回滚所有服务
kubectl rollout undo deployment/user-web
kubectl rollout undo deployment/gateway
kubectl rollout undo deployment/user-api
```

## 监控验证

### 关键指标
| 服务 | 指标 | 阈值 |
|------|------|------|
| user-api | 错误率 | <0.1% |
| user-api | 响应时间 | P99<500ms |
| gateway | 请求成功率 | >99.9% |
| gateway | 路由延迟 | <10ms |
| user-web | 页面加载时间 | <2s |

### 告警配置
```yaml
groups:
- name: deployment-alerts
  rules:
  - alert: ServiceUnavailable
    expr: up{job="user-api"} == 0
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "user-api服务不可用"
```