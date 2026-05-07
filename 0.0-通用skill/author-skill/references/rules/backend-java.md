# Java后端开发 Skill编写规则
# 适用场景：Spring Boot、MyBatis Plus、微服务架构

# ============================================
# 技术栈定义
# ============================================
tech_stack:
  language: "Java 17+"
  framework: "Spring Boot 3.x"
  orm: "MyBatis Plus 3.x"
  database: "MySQL 8.x"
  cache: "Redis"
  build: "Maven/Gradle"

# ============================================
# Skill必填章节
# ============================================
required_sections:
  basic_info:
    - "skill.id: 小写字母+连字符，如 crud-designer"
    - "skill.name: 中文描述性名称"
    - "skill.version: 语义化版本号"
    - "skill.category: implement/design/review"
    - "skill.priority: P0/P1/P2"

  trigger:
    - "trigger.keywords: 至少3个触发关键词"
    - "trigger.commands: 命令触发（可选）"

  input:
    - "input.parameters: 每个参数有name/type/required/description"
    - "参数示例要真实可用"

  workflow:
    - "workflow.phases: 至少2个阶段"
    - "每个阶段有清晰的steps"

  tech_stacks:
    - "tech_stacks: 支持的技术栈列表"
    - "包含base_structure项目结构模板"

  output:
    - "output.artifacts: 输出产物列表"
    - "包含files和description"

  examples:
    - "examples: 至少1个完整示例"
    - "示例包含input和output_summary"

# ============================================
# 项目结构规范
# ============================================
project_structure:
  spring_boot_standard: |
    {project_name}/
    ├── src/main/java/com/{package}/
    │   ├── Application.java
    │   ├── config/           # 配置类
    │   │   ├── SecurityConfig.java
    │   │   ├── RedisConfig.java
    │   │   └── SwaggerConfig.java
    │   ├── controller/       # REST控制器
    │   │   └── admin/        # 管理后台接口
    │   │       └── {Module}Controller.java
    │   ├── service/          # 业务服务
    │   │   ├── {Module}Service.java
    │   │   └── {Module}ServiceImpl.java
    │   ├── dal/
    │   │   ├── dataobject/   # DO实体类
    │   │   │   └── {Module}DO.java
    │   │   └── mysql/        # Mapper接口
    │   │       └── {Module}Mapper.java
    │   ├── convert/          # 对象转换
    │   │   └── {Module}Convert.java
    │   ├── enums/            # 枚举类
    │   │   └── {Module}Enum.java
    │   └── vo/               # VO类
    │       ├── {Module}SaveReqVO.java
    │       ├── {Module}PageReqVO.java
    │       └── {Module}RespVO.java
    ├── src/main/resources/
    │   ├── application.yml
    │   └── application-dev.yml
    ├── src/test/java/
    ├── docs/
    ├── pom.xml
    └── README.md

# ============================================
# 类命名规范
# ============================================
class_naming:
  do_class:
    rule: "DO类以DO结尾，继承TenantBaseDO或BaseDO"
    examples: ["UserDO", "OrderDO", "ProductDO"]

  service_class:
    rule: "Service接口和实现类"
    examples:
      interface: "UserService"
      impl: "UserServiceImpl"

  controller_class:
    rule: "Controller以Controller结尾"
    examples: ["UserController", "OrderController"]

  vo_class:
    rule: "VO类以VO结尾，区分请求和响应"
    examples:
      - "UserSaveReqVO - 创建/更新请求"
      - "UserPageReqVO - 分页查询请求"
      - "UserRespVO - 响应"

  mapper_class:
    rule: "Mapper以Mapper结尾，继承BaseMapperX"
    examples: ["UserMapper", "OrderMapper"]

# ============================================
# 方法命名规范
# ============================================
method_naming:
  crud_methods:
    - prefix: "create"
      description: "创建方法"
      example: "createUser(UserSaveReqVO reqVO)"

    - prefix: "update"
      description: "更新方法"
      example: "updateUser(UserSaveReqVO reqVO)"

    - prefix: "delete"
      description: "删除方法"
      example: "deleteUser(Long id)"

    - prefix: "get"
      description: "单个查询"
      example: "getUser(Long id)"

    - prefix: "list"
      description: "列表查询"
      example: "listUserIds()"

    - prefix: "page"
      description: "分页查询"
      example: "pageUser(UserPageReqVO reqVO)"

# ============================================
# 注解规范
# ============================================
annotation_rules:
  controller:
    required:
      - "@Tag(name = '管理后台 - {模块名}')"
      - "@RestController"
      - "@RequestMapping('/{module}/{entity}')"
      - "@Validated"
    permission:
      - "@PreAuthorize('@ss.hasPermission('{module}:{entity}:{operation}')')"

  service:
    required:
      - "@Service"

  do_class:
    required:
      - "@TableName('{table_name}')"
    tenant:
      - "继承TenantBaseDO时自动支持多租户"

# ============================================
# 权限标识规范
# ============================================
permission_format:
  format: "{模块}:{功能}:{操作}"
  examples:
    - "system:user:create"
    - "system:user:update"
    - "system:user:delete"
    - "system:user:query"

# ============================================
# 错误码规范
# ============================================
error_code_format:
  format: "1_模块编号_功能编号_序号"
  example: "1_002_001_000"
  description: |
    1 - 固定前缀
    002 - 模块编号（如用户模块）
    001 - 功能编号（如用户管理）
    000 - 具体错误序号

# ============================================
# 数据库命名规范
# ============================================
database_naming:
  table:
    rule: "小写下划线格式"
    examples: ["system_user", "pay_order", "product_category"]

  field:
    rule: "小写下划线格式"
    examples:
      - "create_time"
      - "update_time"
      - "creator"
      - "updater"
      - "deleted"

  required_fields:
    - "id BIGINT AUTO_INCREMENT PRIMARY KEY"
    - "creator VARCHAR(64)"
    - "create_time DATETIME"
    - "updater VARCHAR(64)"
    - "update_time DATETIME"
    - "deleted BIT DEFAULT 0"

# ============================================
# 常见Skill示例
# ============================================
skill_examples:
  crud_designer:
    id: "crud-designer"
    name: "CRUD代码生成"
    description: "根据DO类生成完整的CRUD代码，包括Controller、Service、Mapper、VO"

  api_designer:
    id: "api-designer"
    name: "REST API设计"
    description: "根据业务需求设计REST API接口规范"

  entity_designer:
    id: "entity-designer"
    name: "实体类设计"
    description: "根据数据库表结构生成MyBatis Plus实体类"

  db_designer:
    id: "db-designer"
    name: "数据库设计"
    description: "根据业务需求设计数据库表结构和索引"

# ============================================
# 代码示例模板
# ============================================
code_templates:
  controller_example: |
    @Tag(name = "管理后台 - 用户")
    @RestController
    @RequestMapping("/system/user")
    @Validated
    public class UserController {

        @PostMapping("/create")
        @PreAuthorize("@ss.hasPermission('system:user:create')")
        public CommonResult<Long> createUser(@Valid @RequestBody UserSaveReqVO reqVO) {
            return success(userService.createUser(reqVO));
        }

        @PutMapping("/update")
        @PreAuthorize("@ss.hasPermission('system:user:update')")
        public CommonResult<Boolean> updateUser(@Valid @RequestBody UserSaveReqVO reqVO) {
            userService.updateUser(reqVO);
            return success(true);
        }

        @DeleteMapping("/delete")
        @PreAuthorize("@ss.hasPermission('system:user:delete')")
        public CommonResult<Boolean> deleteUser(@RequestParam("id") Long id) {
            userService.deleteUser(id);
            return success(true);
        }

        @GetMapping("/get")
        @PreAuthorize("@ss.hasPermission('system:user:query')")
        public CommonResult<UserRespVO> getUser(@RequestParam("id") Long id) {
            return success(userService.getUser(id));
        }

        @GetMapping("/page")
        @PreAuthorize("@ss.hasPermission('system:user:query')")
        public CommonResult<PageResult<UserRespVO>> pageUser(@Valid UserPageReqVO reqVO) {
            return success(userService.pageUser(reqVO));
        }
    }

  do_example: |
    @TableName("system_user")
    public class UserDO extends TenantBaseDO {
        @TableId
        private Long id;
        private String username;
        private String password;
        private String nickname;
        private String email;
        private Integer status;
        // getter/setter
    }

# ============================================
# 注意事项
# ============================================
notes:
  - "DO类继承TenantBaseDO（多租户）或BaseDO（单租户）"
  - "Mapper继承BaseMapperX，使用LambdaQueryWrapperX"
  - "权限标识格式：模块:功能:操作"
  - "错误码格式：1_模块编号_功能编号_序号"
  - "统一响应使用CommonResult包装"
  - "分页查询返回PageResult"
  - "使用@Valid进行参数校验"