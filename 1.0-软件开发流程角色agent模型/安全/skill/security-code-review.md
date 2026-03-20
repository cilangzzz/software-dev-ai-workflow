# Skill: security-code-review

## 基本信息
- **名称**: security-code-review
- **版本**: 1.0.0
- **所属部门**: 安全部
- **优先级**: P0

## 功能描述
对代码进行安全审查，检测安全漏洞和风险。覆盖OWASP Top 10、CWE Top 25等常见安全问题。

## 触发条件
- 命令触发: `/security-code-review`
- 自然语言触发:
  - "安全代码审查"
  - "检查安全漏洞"
  - "代码安全扫描"

## 输入参数
| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| target | string | 是 | 审查目标：文件路径或目录 |
| language | string | 否 | 编程语言 |
| severity | string | 否 | 最低严重级别：critical / high / medium / all |

## 执行流程
1. **代码解析** - 解析目标代码
2. **漏洞模式匹配** - 匹配已知漏洞模式
3. **数据流分析** - 分析敏感数据流
4. **风险评级** - 评估漏洞严重程度
5. **修复建议** - 提供修复方案

## 检测范围
- SQL注入
- XSS跨站脚本
- 命令注入
- 路径遍历
- 敏感信息泄露
- 不安全的反序列化
- 认证和授权问题
- 加密问题

## 输出格式

### 安全审查报告
```markdown
# 安全代码审查报告

## 摘要
- 审查文件: {count}个
- 代码行数: {lines}行
- 发现漏洞: {total}个
  - 🔴 严重: {critical}
  - 🟠 高危: {high}
  - 🟡 中危: {medium}
  - 🟢 低危: {low}

## 漏洞详情

### 🔴 严重漏洞
#### {vuln_id}: {title}
| 属性 | 内容 |
|------|------|
| 类型 | {type} |
| 位置 | {file}:{line} |
| CWE | CWE-XXX |
| 风险 | {risk} |

**问题代码**:
```{language}
{problematic_code}
```

**修复方案**:
```{language}
{fixed_code}
```

## 安全建议
- {suggestion1}
- {suggestion2}

## 合规检查
| 标准 | 状态 | 备注 |
|------|------|------|
| OWASP Top 10 | ✅/❌ | {note} |
```

## 使用示例

### 示例：Java代码安全审查
**输入**:
```
target: src/main/java/com/example/
language: java
severity: high
```

**输出**:
```markdown
# 安全代码审查报告

## 摘要
- 审查文件: 15个
- 代码行数: 2500行
- 发现漏洞: 8个
  - 🔴 严重: 2
  - 🟠 高危: 3
  - 🟡 中危: 3
  - 🟢 低危: 0

## 漏洞详情

### 🔴 严重漏洞
#### SEC-001: SQL注入漏洞
| 属性 | 内容 |
|------|------|
| 类型 | SQL Injection |
| 位置 | UserService.java:45 |
| CWE | CWE-89 |
| 风险 | 攻击者可执行任意SQL，窃取或篡改数据 |

**问题代码**:
```java
String sql = "SELECT * FROM users WHERE email = '" + email + "'";
statement.executeQuery(sql);
```

**修复方案**:
```java
String sql = "SELECT * FROM users WHERE email = ?";
PreparedStatement stmt = connection.prepareStatement(sql);
stmt.setString(1, email);
stmt.executeQuery();
```

#### SEC-002: 硬编码密码
| 属性 | 内容 |
|------|------|
| 类型 | Hardcoded Credential |
| 位置 | DatabaseConfig.java:12 |
| CWE | CWE-798 |
| 风险 | 凭据泄露风险 |

**问题代码**:
```java
private String password = "Admin@123";
```

**修复方案**:
```java
private String password = System.getenv("DB_PASSWORD");
// 或使用配置中心/密钥管理服务
```

### 🟠 高危漏洞
#### SEC-003: XSS漏洞
| 属性 | 内容 |
|------|------|
| 类型 | Cross-site Scripting |
| 位置 | CommentController.java:67 |
| CWE | CWE-79 |

**修复方案**: 对用户输入进行HTML编码，使用OWASP Java Encoder

## 安全建议
- 所有用户输入必须验证和转义
- 使用参数化查询防止SQL注入
- 敏感配置从环境变量或密钥服务获取
- 启用安全headers（CSP, X-Frame-Options等）

## 合规检查
| 标准 | 状态 | 备注 |
|------|------|------|
| OWASP Top 10 | ⚠️ | 存在注入漏洞 |
| CWE Top 25 | ⚠️ | 存在硬编码凭据 |
```

## 质量标准
- 严重漏洞检出率 ≥ 95%
- 误报率 ≤ 20%
- 修复建议有效性 ≥ 90%

## 依赖工具
- Read - 读取代码文件
- Grep - 搜索危险模式
- Write - 输出报告

## 注意事项
- 审查结果需要人工验证
- 关注业务逻辑漏洞
- 建议结合自动化SAST工具