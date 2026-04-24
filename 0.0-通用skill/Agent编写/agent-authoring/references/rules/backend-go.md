# Go后端开发 Agent编写规则
# 适用场景：Gin、Gorm、Go微服务

# ============================================
# 技术栈定义
# ============================================
tech_stack:
  language: "Go 1.21+"
  frameworks:
    - name: "Gin"
      version: "1.9+"
      description: "高性能HTTP Web框架"
    - name: "Echo"
      version: "4.x"
      description: "高性能可扩展Web框架"
    - name: "Fiber"
      version: "2.x"
      description: "Express风格的Go框架"
  orm:
    - "Gorm"
    - "sqlx"
  database:
    - "PostgreSQL"
    - "MySQL"
    - "Redis"
  microservice:
    - "gRPC"
    - "go-micro"
    - "go-kit"

# ============================================
# Agent角色能力模板
# ============================================
capabilities_template:
  core_skills:
    - skill: "Go语言开发"
      level: "expert"
      components:
        - "Go并发模型（goroutine/channel）"
        - "Go错误处理"
        - "Go内存管理"
        - "Go性能优化"

    - skill: "Gin框架"
      level: "expert"
      components:
        - "路由和中间件"
        - "请求绑定和验证"
        - "响应渲染"
        - "分组路由"

    - skill: "Gorm ORM"
      level: "advanced"
      components:
        - "模型定义和关联"
        - "CRUD操作"
        - "事务处理"
        - "查询构建"

    - skill: "微服务架构"
      level: "intermediate"
      components:
        - "gRPC服务定义"
        - "服务发现"
        - "配置管理"

# ============================================
# 项目结构规范
# ============================================
project_structure:
  gin_standard: |
    {project_name}/
    ├── cmd/
    │   ├── main.go             # 主入口
    │   └── cli/
    ├── internal/
    │   ├── handler/            # HTTP处理器
    │   │   ├── user_handler.go
    │   │   └── item_handler.go
    │   ├── service/            # 业务逻辑
    │   │   ├── user_service.go
    │   │   └── item_service.go
    │   ├── repository/         # 数据访问
    │   │   ├── user_repo.go
    │   │   └── item_repo.go
    │   ├── model/              # 数据模型
    │   │   ├── user.go
    │   │   └── item.go
    │   ├── middleware/         # 中间件
    │   │   ├── auth.go
    │   │   ├── logger.go
    │   ├── config/             # 配置
    │   │   ├── config.go
    │   │   ├── database.go
    │   └── router/             # 路由配置
    │       └── router.go
    ├── pkg/                    # 公共包
    │   ├── utils/
    │   ├── errors/
    │   └── response/
    ├── api/                    # API定义
    │   ├── swagger/
    │   └── proto/              # gRPC proto文件
    ├── scripts/
    ├── docs/
    ├── go.mod
    ├── go.sum
    ├── Makefile
    └── README.md

  go_microservice: |
    {project_name}/
    ├── cmd/
    │   ├── server/
    │   │   └── main.go
    │   └── client/
    │   │   └── main.go
    ├── internal/
    │   ├── domain/             # 领域模型
    │   ├── service/            # 业务服务
    │   ├── repository/         # 数据仓储
    │   └── transport/          # 传输层
    │   │   ├── grpc/
    │   │   └── http/
    ├── pkg/
    │   ├── config/
    │   ├── logger/
    │   └── errors/
    ├── api/proto/
    ├── deployments/
    ├── go.mod
    └── Makefile

# ============================================
# 命名规范
# ============================================
naming_conventions:
  # 包命名
  packages:
    - rule: "小写单词，不使用下划线或驼峰"
      examples: ["handler", "service", "repository", "model"]

  # 文件命名
  files:
    - rule: "小写+下划线"
      examples: ["user_handler.go", "item_service.go"]
    - rule: "测试文件_test.go后缀"
      examples: ["user_handler_test.go"]
    - rule: "接口文件_interface.go（可选）"
      examples: ["user_service_interface.go"]

  # 结构体命名
  structs:
    - rule: "PascalCase大驼峰"
      examples: ["UserHandler", "UserService", "UserRepository"]
    - rule: "请求结构体Req后缀"
      examples: ["CreateUserReq", "UpdateUserReq"]
    - rule: "响应结构体Resp后缀"
      examples: ["UserResp", "ListUserResp"]

  # 方法命名
  methods:
    - rule: "PascalCase（Go公开方法）"
      examples: ["CreateUser", "GetUser", "ListUsers"]
    - rule: "camelCase（Go私有方法）"
      examples: ["validateUser", "hashPassword"]

  # 接口命名
  interfaces:
    - rule: "动词+er后缀或动作名"
      examples: ["UserRepository", "UserService", "Reader", "Writer"]

  # 变量命名
  variables:
    - rule: "camelCase"
      examples: ["userID", "itemList", "dbConn"]
    - rule: "短变量名在局部作用域可接受"
      examples: ["i", "n", "err"]

# ============================================
# 代码风格规范
# ============================================
code_style:
  # Gin Handler模板
  gin_handler: |
    package handler

    import (
        "net/http"
        "github.com/gin-gonic/gin"
        "{project}/internal/service"
        "{project}/pkg/response"
    )

    type UserHandler struct {
        service service.UserService
    }

    func NewUserHandler(s service.UserService) *UserHandler {
        return &UserHandler{service: s}
    }

    // CreateUser 创建用户
    func (h *UserHandler) CreateUser(c *gin.Context) {
        var req CreateUserReq
        if err := c.ShouldBindJSON(&req); err != nil {
            response.Error(c, http.StatusBadRequest, "参数错误")
            return
        }

        user, err := h.service.Create(c.Request.Context(), &req)
        if err != nil {
            response.Error(c, http.StatusInternalServerError, err.Error())
            return
        }

        response.Success(c, user)
    }

    // GetUser 获取用户
    func (h *UserHandler) GetUser(c *gin.Context) {
        id := c.Param("id")
        user, err := h.service.Get(c.Request.Context(), id)
        if err != nil {
            response.Error(c, http.StatusNotFound, "用户不存在")
            return
        }
        response.Success(c, user)
    }

  # Gorm Model模板
  gorm_model: |
    package model

    import (
        "time"
        "gorm.io/gorm"
    )

    type User struct {
        gorm.Model
        Username  string    `gorm:"type:varchar(50);uniqueIndex;not null" json:"username"`
        Email     string    `gorm:"type:varchar(255);uniqueIndex;not null" json:"email"`
        Password  string    `gorm:"type:varchar(255);not null" json:"-"`
        Status    int       `gorm:"type:int;default:1" json:"status"`
        CreatedAt time.Time `json:"created_at"`
        UpdatedAt time.Time `json:"updated_at"`
    }

    func (User) TableName() string {
        return "users"
    }

  # Service接口模板
  service_interface: |
    package service

    import (
        "context"
        "{project}/internal/model"
    )

    type UserService interface {
        Create(ctx context.Context, req *CreateUserReq) (*model.User, error)
        Get(ctx context.Context, id string) (*model.User, error)
        List(ctx context.Context, req *ListUserReq) ([]*model.User, int64, error)
        Update(ctx context.Context, id string, req *UpdateUserReq) (*model.User, error)
        Delete(ctx context.Context, id string) error
    }

# ============================================
# Skill示例
# ============================================
skill_examples:
  gin_scaffold:
    id: "gin-scaffold"
    name: "Gin项目脚手架"
    description: "生成Gin标准项目结构，包含分层架构、中间件、路由配置"

  gorm_model_designer:
    id: "gorm-model-designer"
    name: "Gorm模型设计"
    description: "根据数据库表结构生成Gorm模型定义"

  go_handler_generator:
    id: "go-handler-generator"
    name: "Go Handler生成"
    description: "根据Service接口生成HTTP Handler代码"

  grpc_service_generator:
    id: "grpc-service-generator"
    name: "gRPC服务生成"
    description: "根据proto文件生成gRPC服务代码"

# ============================================
# 注意事项
# ============================================
notes:
  - "Go公开方法首字母大写，私有方法首字母小写"
  - "错误处理使用error类型，不使用panic"
  - "并发使用goroutine和channel"
  - "Context作为第一个参数传递"
  - "接口定义放在使用方而非实现方"
  - "使用go mod管理依赖"