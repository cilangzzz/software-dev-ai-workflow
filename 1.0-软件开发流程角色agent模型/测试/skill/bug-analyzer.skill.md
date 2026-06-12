# Skill: bug-analyzer

## 基本信息
- **名称**: bug-analyzer
- **版本**: 1.0.0
- **所属部门**: 测试部
- **优先级**: P0

## 功能描述
分析软件缺陷，定位根因，提供修复建议。通过分析错误日志、堆栈信息、代码上下文，帮助开发者快速定位和修复Bug。

## 触发条件
- 命令触发: `/bug-analyzer`
- 自然语言触发:
  - "分析这个Bug"
  - "定位问题原因"
  - "分析缺陷"

## 输入参数
| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| error_info | string | 是 | 错误信息/堆栈/日志 |
| code_context | string | 否 | 相关代码路径 |
| reproduce_steps | string | 否 | 复现步骤 |

## 执行流程
1. **错误解析** - 解析错误信息和堆栈
2. **代码定位** - 定位问题代码位置
3. **根因分析** - 分析问题根本原因
4. **影响评估** - 评估问题影响范围
5. **修复建议** - 提供修复方案

## 输出格式

### Bug分析报告
```markdown
# 缺陷分析报告

## 缺陷概述
- 问题类型: {类型}
- 严重程度: {严重程度}
- 影响范围: {范围}

## 根因分析
### 直接原因
{直接原因描述}

### 根本原因
{根本原因描述}

### 代码定位
- 文件: {file_path}
- 行号: {line_number}
- 代码片段:
```{language}
{problematic_code}
```

## 影响评估
- 功能影响: {描述}
- 用户影响: {描述}
- 数据影响: {描述}

## 修复建议
### 方案1（推荐）
{修复方案描述}
```{language}
// 修复代码
{fixed_code}
```

### 方案2（备选）
{备选方案描述}

## 预防措施
- {措施1}
- {措施2}
```

## 使用示例

### 示例：NullPointerException分析
**输入**:
```
error_info: |
  java.lang.NullPointerException
    at com.example.order.OrderService.calculateTotal(OrderService.java:45)
    at com.example.order.OrderService.createOrder(OrderService.java:78)
reproduce_steps: 用户订单中有商品被删除后下单
```

**输出**:
```markdown
# 缺陷分析报告

## 缺陷概述
- 问题类型: 空指针异常
- 严重程度: 高
- 影响范围: 订单创建功能

## 根因分析
### 直接原因
代码未对订单项中的商品进行空值检查，直接访问商品价格属性。

### 根本原因
购物车商品被删除后，订单项仍保留商品引用，但商品对象为null。

### 代码定位
- 文件: OrderService.java
- 行号: 45
- 代码片段:
```java
// 问题代码
for (OrderItem item : items) {
    total += item.getProduct().getPrice() * item.getQuantity();  // NPE
}
```

## 影响评估
- 功能影响: 订单创建失败，用户无法下单
- 用户影响: 购物流程中断，用户体验受损
- 数据影响: 无数据损坏风险

## 修复建议
### 方案1（推荐）
添加空值检查，过滤无效商品项
```java
// 修复代码
for (OrderItem item : items) {
    Product product = item.getProduct();
    if (product != null) {
        total += product.getPrice() * item.getQuantity();
    }
}
```

### 方案2（备选）
在购物车阶段清理无效商品，从源头避免问题

## 预防措施
- 添加单元测试覆盖商品为空的场景
- 使用Optional包装可能为空的对象
- 在数据层面添加外键约束保证数据一致性
```

## 质量标准
- 根因定位准确率 ≥ 85%
- 修复建议有效性 ≥ 90%
- 分析响应时间 < 30秒

## 依赖工具
- Read - 读取相关代码
- Grep - 搜索相关定义
- Bash - 执行诊断命令

## 注意事项
- 复杂问题可能需要多次分析迭代
- 建议结合日志和监控数据综合分析
- 修复后需补充回归测试用例