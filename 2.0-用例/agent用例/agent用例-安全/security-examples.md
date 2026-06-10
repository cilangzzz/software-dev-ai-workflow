# 安全扫描用例

## 用例1：Web应用安全扫描

### 场景描述
安全工程师需要对Java Web应用进行全面的安全扫描，包括代码漏洞、依赖漏洞和密钥泄露检测。

### 使用Skill
- **Skill**: security-scan
- **触发方式**: `/security-scan` 或自然语言 "执行安全扫描"

### 完整提示词
```
/security-scan

扫描目标: src/main/java/
扫描类型: 全部
项目: Java Web应用
```

### 输入参数
| 参数名 | 类型 | 必填 | 值 |
|--------|------|------|-----|
| target | string | 是 | "src/main/java/" |
| scan_types | string | 否 | "all" |
| fail_threshold | string | 否 | 未指定 |

### 执行过程

#### 步骤1：预扫描
快速识别可疑区域：

**预扫描结果**：
- 扫描文件: 156个
- 代码行数: 23,456行
- 可疑区域: 12处
- 潜在高危: 3处

#### 步骤2：深度扫描
执行各类安全扫描：

**SAST扫描**（静态代码分析）：
- 扫描规则: 500+
- 发现漏洞: 6个

**SCA扫描**（依赖漏洞）：
- 依赖数量: 45个
- 发现漏洞: 4个

**Secrets扫描**（密钥检测）：
- 扫描文件: 156个
- 发现泄露: 3处

#### 步骤3：结果聚合
合并和去重扫描结果：

**漏洞汇总**：
| 扫描类型 | Critical | High | Medium | Low |
|----------|----------|------|--------|-----|
| SAST | 2 | 2 | 1 | 1 |
| SCA | 1 | 2 | 1 | 0 |
| Secrets | 0 | 3 | 0 | 0 |
| **总计** | **3** | **7** | **2** | **1** |

#### 步骤4：优先级排序
按风险排序：

**Critical级别漏洞**：
1. SQL注入 (SEC-001) - UserService.java:45
2. 硬编码凭据 (SEC-002) - DatabaseConfig.java:15
3. Log4j漏洞 (CVE-2021-44228) - 依赖包

**High级别漏洞**：
1. XSS漏洞 (SEC-003) - CommentController.java:67
2. 路径遍历 (SEC-004) - FileController.java:34
3. Spring漏洞 (CVE-2022-22965) - 依赖包

#### 步骤5：报告生成
生成统一报告：

**修复优先级建议**：
- 立即修复: 3个Critical漏洞
- 本周修复: 4个High漏洞
- 计划修复: 3个Medium/Low漏洞

### 最终输出
```markdown
# 安全扫描报告

## 扫描概要
- 扫描时间: 2024-01-15 10:30:00
- 扫描目标: src/main/java/
- 扫描类型: SAST + SCA + Secrets
- 总漏洞数: 13

## 漏洞统计
| 严重级别 | 数量 | 占比 |
|----------|------|------|
| 🔴 Critical | 3 | 23% |
| 🟠 High | 7 | 54% |
| 🟡 Medium | 2 | 15% |
| 🟢 Low | 1 | 8% |

## SAST扫描结果

### 🔴 Critical - SQL注入漏洞
| 属性 | 内容 |
|------|------|
| 漏洞ID | SEC-001 |
| 类型 | SQL Injection (CWE-89) |
| 位置 | UserService.java:45 |
| 风险 | 攻击者可执行任意SQL，窃取或篡改数据 |

**问题代码**:
```java
String sql = "SELECT * FROM users WHERE email = '" + email + "'";
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery(sql);
```

**修复方案**:
```java
String sql = "SELECT * FROM users WHERE email = ?";
PreparedStatement stmt = conn.prepareStatement(sql);
stmt.setString(1, email);
ResultSet rs = stmt.executeQuery();
```

### 🔴 Critical - 硬编码凭据
| 属性 | 内容 |
|------|------|
| 漏洞ID | SEC-002 |
| 类型 | Hardcoded Credential (CWE-798) |
| 位置 | DatabaseConfig.java:15 |
| 风险 | 凭据泄露风险，代码仓库暴露即泄露 |

**问题代码**:
```java
private String dbPassword = "Admin@123456";
```

**修复方案**:
```java
private String dbPassword = System.getenv("DB_PASSWORD");
// 或使用配置中心/密钥管理服务
```

### 🟠 High - XSS漏洞
| 属性 | 内容 |
|------|------|
| 漏洞ID | SEC-003 |
| 类型 | Cross-site Scripting (CWE-79) |
| 位置 | CommentController.java:67 |
| 风险 | 存储型XSS，窃取用户Cookie |

**问题代码**:
```java
model.addAttribute("comment", comment.getContent());
```

**修复方案**:
```java
model.addAttribute("comment", HtmlUtils.htmlEscape(comment.getContent()));
// 或使用Thymeleaf默认转义
```

### 🟠 High - 路径遍历
| 属性 | 内容 |
|------|------|
| 漏洞ID | SEC-004 |
| 类型 | Path Traversal (CWE-22) |
| 位置 | FileController.java:34 |
| 风险 | 读取任意文件 |

**问题代码**:
```java
File file = new File("/uploads/" + fileName);
```

**修复方案**:
```java
Path basePath = Paths.get("/uploads/").normalize();
Path filePath = basePath.resolve(fileName).normalize();
if (!filePath.startsWith(basePath)) {
    throw new SecurityException("非法路径");
}
```

## SCA扫描结果 - 依赖漏洞

| 包名 | 当前版本 | CVE | 严重性 | 修复版本 |
|------|----------|-----|--------|---------|
| log4j-core | 2.14.1 | CVE-2021-44228 | 🔴 Critical | 2.17.1 |
| spring-beans | 5.3.15 | CVE-2022-22965 | 🟠 High | 5.3.18 |
| jackson-databind | 2.12.3 | CVE-2022-42003 | 🟡 Medium | 2.12.7 |
| h2 | 1.4.200 | CVE-2021-42392 | 🟠 High | 2.1.214 |

## Secrets扫描结果

| 类型 | 文件 | 行号 | 状态 |
|------|------|------|------|
| AWS Access Key | application.yml | 23 | 🔴 需处理 |
| JWT Secret | SecurityConfig.java | 18 | 🔴 需处理 |
| API Key | PaymentService.java | 45 | 🔴 需处理 |

## 修复优先级

### 立即修复 (Critical)
1. SQL注入漏洞 - SEC-001
2. 硬编码凭据 - SEC-002
3. Log4j漏洞 - CVE-2021-44228

### 本周修复 (High)
1. XSS漏洞 - SEC-003
2. 路径遍历 - SEC-004
3. Spring漏洞 - CVE-2022-22965

### 计划修复 (Medium)
1. Jackson漏洞
2. H2数据库漏洞
```

---

## 用例2：API安全威胁建模

### 场景描述
安全架构师需要对移动App API系统进行威胁建模，识别潜在安全威胁并制定缓解措施。

### 使用Skill
- **Skill**: security-threat-model
- **触发方式**: `/security-threat-model` 或自然语言 "威胁建模"

### 完整提示词
```
/security-threat-model

系统：用户通过移动App访问后端API
功能：用户登录、查询订单、修改个人信息
认证：JWT Token
数据：MySQL + Redis
```

### 输入参数
| 参数名 | 类型 | 必填 | 值 |
|--------|------|------|-----|
| system_description | string | 是 | "用户通过移动App访问后端API，功能：用户登录、查询订单、修改个人信息，认证：JWT Token，数据：MySQL + Redis" |
| data_flow | string | 否 | 未指定 |
| trust_boundaries | string | 否 | 未指定 |

### 执行过程

#### 步骤1：系统分析
解析系统组件和交互：

**系统组件**：
- 移动App（客户端）
- API Gateway（网关层）
- 应用服务（业务层）
- MySQL（数据存储）
- Redis（缓存层）

**关键交互**：
- App ↔ API: HTTPS通信，JWT认证
- API ↔ MySQL: 内网通信
- API ↔ Redis: 内网通信

#### 步骤2：边界识别
识别信任边界：

**信任边界**：
- 边界1: 移动App → API服务器（不可信网络）
- 边界2: API服务器 → 数据库（可信内网）
- 边界3: API服务器 → Redis（可信内网）

#### 步骤3：威胁识别
使用STRIDE分类威胁：

**S - Spoofing (欺骗)**: 4个威胁
**T - Tampering (篡改)**: 4个威胁
**R - Repudiation (抵赖)**: 2个威胁
**I - Information Disclosure (信息泄露)**: 4个威胁
**D - Denial of Service (拒绝服务)**: 3个威胁
**E - Elevation of Privilege (权限提升)**: 3个威胁

**总计**: 20个威胁

#### 步骤4：风险评估
评估威胁风险等级：

**高风险威胁**: 10个
- JWT Token被窃取
- 中间人攻击
- 修改他人订单
- SQL注入
- 敏感数据未加密存储
- API请求泛洪
- 越权访问他人数据
- 普通用户执行管理操作
- IDOR

**中风险威胁**: 8个
**低风险威胁**: 2个

#### 步骤5：缓解建议
提供安全控制建议：

**认证与授权**：
- JWT Token有效期<2小时
- 关键操作需要二次验证
- 实现RBAC权限模型

**数据安全**：
- 所有通信使用TLS 1.2+
- 密码使用bcrypt存储
- 敏感字段AES-256加密

### 最终输出
```markdown
# 威胁建模报告

## 系统概述
移动App + API后端 + MySQL + Redis，支持用户认证和订单管理。

## 信任边界
```
┌─────────────────────────────────────────────────────────────┐
│                      不可信区域                              │
│  ┌─────────────┐                                            │
│  │  移动App    │                                            │
│  └──────┬──────┘                                            │
│         │ HTTPS                                             │
│  ───────┼────────────────── 信任边界1 ──────────────────    │
│         │                                                   │
├─────────┼───────────────────────────────────────────────────┤
│         ▼              可信区域                              │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐   │
│  │ API Gateway │────▶│ 应用服务    │────▶│   MySQL     │   │
│  └─────────────┘     └──────┬──────┘     └─────────────┘   │
│                             │                               │
│                             │                               │
│                      ┌──────▼──────┐                       │
│                      │    Redis    │                       │
│                      └─────────────┘                       │
└─────────────────────────────────────────────────────────────┘
```

## STRIDE威胁分析

### S - Spoofing (欺骗)

| ID | 威胁 | 风险 | 缓解措施 |
|----|------|------|---------|
| S-01 | JWT Token被窃取 | 🔴 高 | 使用HTTPS，设置合理过期时间，刷新Token机制 |
| S-02 | 中间人攻击 | 🔴 高 | 强制HTTPS，证书固定(Pinning) |
| S-03 | 重放攻击 | 🟠 中 | JWT添加jti，Redis记录已使用Token |
| S-04 | 设备伪造 | 🟡 中 | 设备指纹验证，异常登录提醒 |

### T - Tampering (篡改)

| ID | 威胁 | 风险 | 缓解措施 |
|----|------|------|---------|
| T-01 | 修改他人订单 | 🔴 高 | API权限校验，用户ID与Token匹配验证 |
| T-02 | SQL注入 | 🔴 高 | 参数化查询，ORM框架 |
| T-03 | 请求参数篡改 | 🟠 中 | 参数签名验证 |
| T-04 | 数据库直接篡改 | 🟠 中 | 数据库访问控制，操作审计 |

### R - Repudiation (抵赖)

| ID | 威胁 | 风险 | 缓解措施 |
|----|------|------|---------|
| R-01 | 用户否认操作 | 🟠 中 | 关键操作日志记录，不可篡改 |
| R-02 | 管理员滥用权限 | 🟠 中 | 管理操作审计，双人确认 |

### I - Information Disclosure (信息泄露)

| ID | 威胁 | 风险 | 缓解措施 |
|----|------|------|---------|
| I-01 | 敏感数据未加密存储 | 🔴 高 | 密码bcrypt，敏感数据AES加密 |
| I-02 | API返回过多信息 | 🟠 中 | 响应脱敏，最小化返回字段 |
| I-03 | 日志泄露敏感信息 | 🟠 中 | 日志脱敏处理 |
| I-04 | 错误信息泄露技术细节 | 🟡 低 | 统一错误页面，隐藏堆栈信息 |

### D - Denial of Service (拒绝服务)

| ID | 威胁 | 风险 | 缓解措施 |
|----|------|------|---------|
| D-01 | API请求泛洪 | 🔴 高 | 限流(每用户/每IP)，熔断 |
| D-02 | 大文件上传耗尽存储 | 🟠 中 | 文件大小限制，存储配额 |
| D-03 | 慢速攻击 | 🟡 低 | 连接超时设置 |

### E - Elevation of Privilege (权限提升)

| ID | 威胁 | 风险 | 缓解措施 |
|----|------|------|---------|
| E-01 | 越权访问他人数据 | 🔴 高 | 每个API验证用户权限 |
| E-02 | 普通用户执行管理操作 | 🔴 高 | 角色权限控制，管理接口独立认证 |
| E-03 | IDOR (不安全的直接对象引用) | 🔴 高 | 避免使用自增ID，使用UUID |

## 安全需求清单

### 认证与授权
- [ ] JWT Token有效期<2小时
- [ ] Refresh Token有效期<7天
- [ ] 关键操作需要二次验证
- [ ] 实现RBAC权限模型

### 数据安全
- [ ] 所有通信使用TLS 1.2+
- [ ] 密码使用bcrypt存储(cost≥10)
- [ ] 敏感字段AES-256加密
- [ ] 数据库字段级加密

### API安全
- [ ] 实现请求限流(100次/分钟/用户)
- [ ] 参数签名验证
- [ ] 响应数据脱敏
- [ ] 错误信息统一处理

### 审计与监控
- [ ] 登录日志记录
- [ ] 敏感操作审计
- [ ] 异常行为告警
- [ ] 安全事件追溯

## 风险矩阵

| 风险等级 | 数量 | 占比 | 处理时限 |
|----------|------|------|---------|
| 🔴 高风险 | 10 | 50% | 立即处理 |
| 🟠 中风险 | 8 | 40% | 1周内处理 |
| 🟡 低风险 | 2 | 10% | 迭代中处理 |
```

---

## 用例3：代码安全审查

### 场景描述
安全工程师需要对UserController.java进行代码安全审查，检测安全漏洞并提供修复建议。

### 使用Skill
- **Skill**: security-code-review
- **触发方式**: `/security-code-review` 或自然语言 "安全代码审查"

### 完整提示词
```
/security-code-review

目标代码:
// UserController.java
@RestController
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/user/{id}")
    public User getUser(@PathVariable Long id) {
        return userService.findById(id);
    }

    @PostMapping("/user/login")
    public String login(@RequestBody LoginRequest request) {
        User user = userService.findByEmail(request.getEmail());
        if (user.getPassword().equals(request.getPassword())) {
            return generateToken(user);
        }
        return "登录失败";
    }

    @PutMapping("/user/profile")
    public void updateProfile(@RequestBody User user, HttpServletRequest request) {
        userService.update(user);
    }

    private String generateToken(User user) {
        return "token_" + user.getId() + "_" + System.currentTimeMillis();
    }
}
```

### 输入参数
| 参数名 | 类型 | 必填 | 值 |
|--------|------|------|-----|
| target | string | 是 | "UserController.java" |
| language | string | 否 | "java" |
| severity | string | 否 | "all" |

### 执行过程

#### 步骤1：代码解析
解析目标代码：

**代码结构**：
- 类: UserController
- 方法: getUser, login, updateProfile, generateToken
- 注解: @RestController, @GetMapping, @PostMapping, @PutMapping
- 行数: 约25行

#### 步骤2：漏洞模式匹配
匹配已知漏洞模式：

**检测到的漏洞模式**：
| 模式 | 位置 | 匹配度 |
|------|------|--------|
| 明文密码比较 | 第16行 | 100% |
| 弱Token生成 | 第24行 | 100% |
| 缺少权限检查 | 第10-12行 | 95% |
| 缺少输入验证 | 第21-23行 | 90% |

#### 步骤3：数据流分析
分析敏感数据流：

**敏感数据流追踪**：
- 密码: request.getPassword() → equals() → 未使用安全比较
- Token: generateToken() → 返回值 → 可预测
- 用户数据: userService.findById(id) → 直接返回 → 信息泄露风险

#### 步骤4：风险评级
评估漏洞严重程度：

**漏洞评级**：
| 漏洞 | 严重性 | 依据 |
|------|--------|------|
| 明文密码比较 | 🔴 Critical | CWE-798, 密码存储安全风险 |
| 弱Token生成 | 🔴 Critical | CWE-384, 认证绕过风险 |
| 越权访问风险 | 🟠 High | CWE-639, IDOR漏洞 |
| 缺少输入验证 | 🟠 High | CWE-20, 数据完整性风险 |
| 返回过多信息 | 🟡 Medium | CWE-200, 信息泄露 |
| 缺少异常处理 | 🟡 Medium | CWE-209, 信息泄露 |

#### 步骤5：修复建议
提供修复方案：

**修复优先级**：
1. 密码验证改用BCrypt
2. Token改用JWT
3. 添加权限校验
4. 添加输入验证

### 最终输出
```markdown
# 代码安全审查报告

## 审查结果摘要
- 审查文件: UserController.java
- 发现问题: 6个
- 🔴 严重: 2个 | 🟠 高危: 2个 | 🟡 中危: 2个

## 问题详情

### 🔴 SEC-CODE-001: 明文密码比较
| 属性 | 内容 |
|------|------|
| 位置 | 第16行 |
| 类型 | 弱密码验证 |
| 风险 | 密码未使用安全哈希比较 |

**问题代码**:
```java
if (user.getPassword().equals(request.getPassword())) {
```

**问题分析**:
- 直接使用明文比较，说明密码存储可能也是明文
- 缺少防时序攻击保护

**修复方案**:
```java
// 使用BCrypt
if (BCrypt.checkpw(request.getPassword(), user.getPassword())) {
```

### 🔴 SEC-CODE-002: 弱Token生成
| 属性 | 内容 |
|------|------|
| 位置 | 第24行 |
| 类型 | 不安全的Token |
| 风险 | Token可预测，容易被伪造 |

**问题代码**:
```java
return "token_" + user.getId() + "_" + System.currentTimeMillis();
```

**问题分析**:
- Token格式可预测
- 没有签名验证
- 用户ID直接暴露

**修复方案**:
```java
// 使用JWT
String token = Jwts.builder()
    .setSubject(user.getId().toString())
    .setIssuedAt(new Date())
    .setExpiration(new Date(System.currentTimeMillis() + EXPIRE_TIME))
    .signWith(SignatureAlgorithm.HS256, SECRET_KEY)
    .compact();
```

### 🟠 SEC-CODE-003: 越权访问风险
| 属性 | 内容 |
|------|------|
| 位置 | 第10-12行 |
| 类型 | IDOR |
| 风险 | 任意用户可查看他人信息 |

**问题代码**:
```java
@GetMapping("/user/{id}")
public User getUser(@PathVariable Long id) {
    return userService.findById(id);
}
```

**问题分析**:
- 没有验证当前用户是否有权限查看该ID
- 通过修改URL中的ID可查看任意用户信息

**修复方案**:
```java
@GetMapping("/user/{id}")
public User getUser(@PathVariable Long id, Authentication auth) {
    Long currentUserId = getCurrentUserId(auth);
    if (!id.equals(currentUserId) && !isAdmin(auth)) {
        throw new AccessDeniedException("无权访问");
    }
    return userService.findById(id);
}
```

### 🟠 SEC-CODE-004: 缺少输入验证
| 属性 | 内容 |
|------|------|
| 位置 | 第21-23行 |
| 类型 | 缺少验证 |
| 风险 | 恶意数据入库 |

**问题分析**:
- updateProfile方法直接接收User对象
- 没有验证用户只能修改自己的信息
- 可能被利用修改他人信息或提权

**修复方案**:
```java
@PutMapping("/user/profile")
public void updateProfile(@RequestBody @Valid UserUpdateRequest request,
                          Authentication auth) {
    Long userId = getCurrentUserId(auth);
    userService.update(userId, request); // 只能更新自己的信息
}
```

### 🟡 SEC-CODE-005: 返回过多信息
| 属性 | 内容 |
|------|------|
| 位置 | 第11行 |
| 类型 | 信息泄露 |
| 风险 | 返回用户完整信息包括敏感字段 |

**修复方案**:
```java
// 使用DTO只返回必要字段
@GetMapping("/user/{id}")
public UserDTO getUser(@PathVariable Long id) {
    return userService.findUserDTOById(id);
}
```

### 🟡 SEC-CODE-006: 缺少异常处理
| 属性 | 内容 |
|------|------|
| 位置 | 多处 |
| 类型 | 缺少异常处理 |
| 风险 | 敏感信息可能通过异常泄露 |

**修复方案**:
```java
@ExceptionHandler(Exception.class)
public ResponseEntity<ErrorResponse> handleException(Exception e) {
    log.error("Error: ", e);
    return ResponseEntity.status(500)
        .body(new ErrorResponse("系统错误，请稍后重试"));
}
```

## 安全改进建议

### 认证安全
1. 实现标准JWT认证
2. 密码使用BCrypt存储和验证
3. 实现Token刷新机制

### 授权安全
1. 实现方法级权限控制
2. 验证资源所有权
3. 记录访问日志

### 数据安全
1. 敏感字段加密存储
2. API响应脱敏
3. 添加数据验证注解
```