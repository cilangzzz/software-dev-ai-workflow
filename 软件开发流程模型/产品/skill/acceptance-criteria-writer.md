# Skill: acceptance-criteria-writer

## 基本信息
- **名称**: acceptance-criteria-writer
- **版本**: 1.0.0
- **所属部门**: 产品部
- **优先级**: P0

## 功能描述
为用户故事自动生成验收标准（Acceptance Criteria）。使用Gherkin语法（Given-When-Then）生成可被自动化测试框架直接使用的验收条件。

## 触发条件
- 命令触发: `/acceptance-criteria-writer`
- 自然语言触发:
  - "生成验收标准"
  - "写验收条件"
  - "生成AC"
  - "创建测试场景"

## 输入参数
| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| user_story | string | 是 | 用户故事内容 |
| output_format | string | 否 | 输出格式：gherkin / checklist / table |
| include_edge_cases | boolean | 否 | 是否包含边界用例，默认true |

## 执行流程
1. **故事解析** - 解析用户故事的关键元素
2. **场景识别** - 识别正常流程、异常流程、边界场景
3. **前置条件推导** - 确定每个场景的前置条件
4. **行为定义** - 定义用户的具体操作步骤
5. **预期结果** - 明确系统的预期响应
6. **格式输出** - 按指定格式输出验收标准

## 输出格式

### Gherkin格式（推荐）
```gherkin
Feature: [功能名称]

  Scenario: [场景名称]
    Given [前置条件]
    When [用户行为]
    Then [预期结果]

  Scenario: [异常场景]
    Given [前置条件]
    When [异常操作]
    Then [错误处理]
```

### 检查清单格式
```markdown
## 验收标准检查清单

### 正常流程
- [ ] 验收条件1
- [ ] 验收条件2

### 异常流程
- [ ] 异常处理1
- [ ] 异常处理2

### 边界条件
- [ ] 边界条件1
- [ ] 边界条件2
```

## 质量标准
- 场景覆盖率 ≥ 90%（覆盖正常+异常+边界）
- Gherkin语法正确率 100%
- 可测试性 100%（所有AC可转化为测试用例）
- 步骤清晰度：每个场景步骤数3-7步

## 使用示例

### 示例1：登录功能验收标准
**输入**:
```
用户故事：作为注册用户，我希望能够使用手机号和密码登录系统，
以便于访问我的个人账户。
```

**输出**:
```gherkin
Feature: 用户登录

  Scenario: 使用正确的手机号和密码登录成功
    Given 用户在登录页面
    And 用户已注册手机号 "13800138000"
    When 用户输入手机号 "13800138000"
    And 用户输入密码 "correctPassword123"
    And 用户点击登录按钮
    Then 用户登录成功
    And 页面跳转到首页
    And 顶部显示用户信息

  Scenario: 使用错误的密码登录失败
    Given 用户在登录页面
    And 用户已注册手机号 "13800138000"
    When 用户输入手机号 "13800138000"
    And 用户输入密码 "wrongPassword"
    And 用户点击登录按钮
    Then 显示错误提示 "手机号或密码错误"
    And 用户保持在登录页面
    And 登录表单内容保持不变

  Scenario: 手机号格式错误
    Given 用户在登录页面
    When 用户输入手机号 "12345"
    And 用户输入密码 "password123"
    And 用户点击登录按钮
    Then 显示错误提示 "请输入正确的手机号格式"
    And 登录按钮保持禁用状态

  Scenario: 必填字段为空
    Given 用户在登录页面
    When 用户输入手机号 ""
    And 用户输入密码 ""
    And 用户点击登录按钮
    Then 显示错误提示 "请输入手机号"
    And 显示错误提示 "请输入密码"

  Scenario: 连续登录失败锁定账户
    Given 用户在登录页面
    And 用户已连续登录失败4次
    When 用户再次输入错误密码登录
    Then 显示错误提示 "登录失败次数过多，账户已锁定30分钟"
    And 登录按钮禁用

  Scenario: 记住登录状态
    Given 用户在登录页面
    When 用户勾选"记住我"选项
    And 用户输入正确凭据登录成功
    Then 用户关闭浏览器后重新打开
    And 用户保持登录状态

  Scenario Outline: 边界值密码验证
    Given 用户在登录页面
    When 用户输入密码 "<password>"
    Then 密码验证结果为 "<result>"

    Examples:
      | password | result |
      | 12345    | 无效（少于6位）|
      | 123456   | 有效 |
      | abcdefghijklmnopqrst | 无效（超过20位）|
```

### 示例2：购物车验收标准
**输入**:
```
用户故事：作为购物用户，我希望能够在购物车中修改商品数量，
以便于调整我要购买的商品。
```

**输出**:
```gherkin
Feature: 购物车商品数量修改

  Scenario: 增加商品数量
    Given 购物车中有商品"iPhone 15"数量为1
    When 用户点击数量增加按钮
    Then 商品数量变为2
    And 商品小计金额更新
    And 购物车总金额更新

  Scenario: 减少商品数量
    Given 购物车中有商品"iPhone 15"数量为2
    When 用户点击数量减少按钮
    Then 商品数量变为1
    And 商品小计金额更新
    And 购物车总金额更新

  Scenario: 手动输入数量
    Given 购物车中有商品"iPhone 15"数量为1
    When 用户在数量输入框输入"5"
    Then 商品数量变为5
    And 商品小计金额更新
    And 购物车总金额更新

  Scenario: 数量减少到0时删除商品
    Given 购物车中有商品"iPhone 15"数量为1
    When 用户点击数量减少按钮
    Then 弹出确认删除提示
    When 用户确认删除
    Then 商品从购物车移除
    And 购物车总金额更新

  Scenario: 输入非法数量值
    Given 购物车中有商品"iPhone 15"
    When 用户在数量输入框输入"-1"
    Then 数量自动恢复为原值
    And 显示提示"数量必须大于0"

  Scenario: 超过库存限制
    Given 商品"iPhone 15"库存为10件
    And 购物车中有商品"iPhone 15"数量为10
    When 用户尝试增加数量
    Then 显示提示"已达到最大库存数量"

  Scenario: 达到购买上限
    Given 商品"iPhone 15"每人限购5件
    And 购物车中有商品"iPhone 15"数量为5
    When 用户尝试增加数量
    Then 显示提示"每人限购5件"

  Scenario Outline: 数量边界值验证
    Given 购物车中有商品"iPhone 15"
    When 用户输入数量 "<quantity>"
    Then 处理结果为 "<result>"

    Examples:
      | quantity | result |
      | 0        | 触发删除确认 |
      | 1        | 正常更新 |
      | 99       | 正常更新 |
      | 100      | 提示超过最大限制 |
      | abc      | 忽略非法输入 |
      | 1.5      | 忽略小数 |
```

## 依赖工具
- Read - 读取用户故事
- Write - 输出验收标准文档
- Grep - 搜索相关功能定义

## 注意事项
- 验收标准应该具体、可测量
- 避免使用模糊词汇如"快速"、"友好"等
- 异常场景和边界条件同样重要
- 验收标准是开发、测试、产品的共识基础
- 建议每个场景有独立的测试用例对应