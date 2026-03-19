# Skill: implement

## 基本信息
- **名称**: implement
- **版本**: 1.0.0
- **所属部门**: 研发部
- **优先级**: P0

## 功能描述
根据设计文档和用户故事，实现功能代码。AI辅助生成业务逻辑代码、数据模型、API接口等，并同步生成单元测试。

## 触发条件
- 命令触发: `/implement`
- 自然语言触发:
  - "实现这个功能"
  - "写代码"
  - "开发功能"
  - "实现用户故事"

## 输入参数
| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| specification | string | 是 | 功能规格描述或用户故事 |
| target_file | string | 否 | 目标文件路径 |
| language | string | 否 | 编程语言（默认根据项目检测） |
| style | string | 否 | 代码风格：clean / enterprise |

## 执行流程
1. **需求理解** - 解析功能规格和用户故事
2. **上下文分析** - 分析现有代码结构和模式
3. **设计实现** - 设计代码结构和逻辑
4. **代码生成** - 生成业务代码
5. **测试生成** - 同步生成单元测试
6. **文档注释** - 添加必要的代码注释

## 输出格式

### 功能实现报告
```markdown
# 功能实现报告

## 实现概述
{功能描述和实现方案}

## 生成的文件
| 文件路径 | 说明 | 行数 |
|----------|------|------|
| {path1} | {说明} | {lines} |
| {path2} | {说明} | {lines} |

## 核心代码片段
### 1. {模块名}
```{language}
{关键代码}
```

## API接口
| 方法 | 路径 | 描述 |
|------|------|------|
| POST | /api/users | 创建用户 |

## 数据模型
{新增的数据模型说明}

## 测试覆盖
- 单元测试文件: {test_file}
- 测试覆盖率: {coverage}%
- 测试用例数: {count}

## 依赖变更
- 新增依赖: {dependencies}

## 待办事项
- [ ] 配置数据库迁移
- [ ] 添加权限控制
- [ ] 完善错误处理

## 注意事项
- {注意事项1}
- {注意事项2}
```

## 质量标准
- 代码符合项目既有风格
- 单元测试覆盖率 ≥ 80%
- 无明显的安全漏洞
- 包含必要的错误处理
- 遵循SOLID原则

## 使用示例

### 示例1：实现用户注册功能
**输入**:
```
用户故事：作为新用户，我希望能够注册账号，以便使用系统功能。
验收标准：
- 支持邮箱注册
- 密码需要加密存储
- 注册成功发送欢迎邮件
- 用户名不能重复
```

**输出**:
```markdown
# 功能实现报告：用户注册

## 实现概述
实现了用户注册功能，包含邮箱验证、密码加密、唯一性检查和欢迎邮件发送。

## 生成的文件
| 文件路径 | 说明 | 行数 |
|----------|------|------|
| src/main/java/com/example/user/UserController.java | 用户控制器 | 85 |
| src/main/java/com/example/user/UserService.java | 用户服务 | 120 |
| src/main/java/com/example/user/UserRepository.java | 用户仓库 | 25 |
| src/main/java/com/example/user/User.java | 用户实体 | 45 |
| src/main/java/com/example/user/dto/RegisterRequest.java | 注册请求DTO | 30 |
| src/test/java/com/example/user/UserServiceTest.java | 单元测试 | 150 |

## 核心代码片段
### 1. 用户服务
```java
@Service
@Transactional
public class UserService {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Autowired
    private EmailService emailService;

    public User register(RegisterRequest request) {
        // 检查邮箱唯一性
        if (userRepository.existsByEmail(request.getEmail())) {
            throw new BusinessException("邮箱已被注册");
        }

        // 创建用户
        User user = new User();
        user.setEmail(request.getEmail());
        user.setUsername(request.getUsername());
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        user.setStatus(UserStatus.ACTIVE);

        user = userRepository.save(user);

        // 发送欢迎邮件
        emailService.sendWelcomeEmail(user.getEmail(), user.getUsername());

        return user;
    }
}
```

## API接口
| 方法 | 路径 | 描述 |
|------|------|------|
| POST | /api/users/register | 用户注册 |

## 数据模型
User实体新增字段：
- id: Long (主键)
- email: String (邮箱，唯一)
- username: String (用户名，唯一)
- password: String (加密密码)
- status: UserStatus (状态)

## 测试覆盖
- 单元测试文件: UserServiceTest.java
- 测试覆盖率: 92%
- 测试用例数: 8

## 依赖变更
- 无新增依赖

## 待办事项
- [ ] 添加邮箱验证码功能
- [ ] 完善密码强度校验
- [ ] 添加注册频率限制

## 注意事项
- 密码使用BCrypt加密，强度已设置为10轮
- 邮件发送为异步操作，不阻塞注册流程
- 需要配置SMTP邮件服务器
```

### 示例2：实现商品搜索功能
**输入**:
```
功能需求：实现商品搜索功能
- 支持关键词搜索
- 支持分类筛选
- 支持价格区间筛选
- 支持排序（价格、销量、上架时间）
- 分页展示
```

**输出**:
```markdown
# 功能实现报告：商品搜索

## 实现概述
实现商品多条件搜索功能，使用Specification动态构建查询条件，支持关键词、分类、价格区间筛选和多字段排序。

## 生成的文件
| 文件路径 | 说明 | 行数 |
|----------|------|------|
| src/main/java/com/example/goods/GoodsController.java | 商品控制器 | 65 |
| src/main/java/com/example/goods/GoodsService.java | 商品服务 | 95 |
| src/main/java/com/example/goods/GoodsSpecification.java | 查询条件构建 | 80 |
| src/main/java/com/example/goods/dto/GoodsSearchRequest.java | 搜索请求DTO | 40 |
| src/main/java/com/example/goods/dto/GoodsSearchResponse.java | 搜索响应DTO | 35 |

## API接口
| 方法 | 路径 | 描述 |
|------|------|------|
| GET | /api/goods/search | 商品搜索 |

## 请求参数
```
GET /api/goods/search?keyword=手机&categoryId=1&minPrice=100&maxPrice=5000&sort=price&order=asc&page=0&size=20
```

## 测试覆盖
- 单元测试文件: GoodsServiceTest.java
- 测试覆盖率: 88%
- 测试用例数: 12

## 待办事项
- [ ] 接入Elasticsearch提升搜索性能
- [ ] 添加搜索日志记录
- [ ] 实现搜索建议功能
```

## 依赖工具
- Read - 读取现有代码结构
- Write - 创建新文件
- Edit - 修改现有文件
- Grep - 搜索相关代码
- Glob - 查找文件

## 注意事项
- 生成的代码需要人工Review后才能合并
- 复杂业务逻辑建议先做技术设计
- 注意SQL注入、XSS等安全问题
- 遵循项目既有的命名规范和代码风格
- 测试用例需要覆盖边界条件