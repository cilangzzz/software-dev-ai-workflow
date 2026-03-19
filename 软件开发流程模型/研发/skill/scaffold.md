# Skill: scaffold

## 基本信息
- **名称**: scaffold
- **版本**: 1.0.0
- **所属部门**: 研发部
- **优先级**: P0

## 功能描述
根据技术栈和项目类型快速生成项目脚手架代码。包含标准的项目结构、配置文件、基础代码模板，让开发者快速开始业务开发。

## 触发条件
- 命令触发: `/scaffold`
- 自然语言触发:
  - "创建项目"
  - "生成脚手架"
  - "初始化项目"
  - "创建新项目"

## 输入参数
| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| project_name | string | 是 | 项目名称 |
| tech_stack | string | 是 | 技术栈（如：spring-boot, vue3, react, next.js） |
| project_type | string | 否 | 项目类型：web/api/cli/lib |
| features | string | 否 | 需要的功能特性（逗号分隔） |

## 执行流程
1. **模板匹配** - 根据技术栈选择对应模板
2. **变量替换** - 替换模板中的项目名称等变量
3. **目录创建** - 创建标准项目结构
4. **配置生成** - 生成配置文件
5. **基础代码** - 生成示例代码和测试
6. **依赖安装** - 生成依赖文件

## 输出格式

### 项目结构示例（Spring Boot）
```
{project_name}/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── {package}/
│   │   │           ├── Application.java
│   │   │           ├── config/
│   │   │           │   └── SecurityConfig.java
│   │   │           ├── controller/
│   │   │           │   └── HealthController.java
│   │   │           ├── service/
│   │   │           ├── repository/
│   │   │           └── entity/
│   │   └── resources/
│   │       ├── application.yml
│   │       └── application-dev.yml
│   └── test/
│       └── java/
│           └── com/
│               └── {package}/
│                   └── ApplicationTests.java
├── docs/
│   └── README.md
├── .gitignore
├── pom.xml
└── README.md
```

## 支持的技术栈

| 技术栈 | 模板标识 | 特性选项 |
|--------|---------|---------|
| Spring Boot | spring-boot | mysql, redis, mongodb, security, swagger |
| Vue 3 | vue3 | typescript, pinia, router, eslint |
| React | react | typescript, redux, router, tailwind |
| Next.js | nextjs | typescript, prisma, tailwind, trpc |
| Python FastAPI | fastapi | sqlalchemy, redis, celery |
| Go Gin | gin | gorm, redis, swagger |

## 质量标准
- 项目结构符合最佳实践
- 配置文件完整可用
- 包含基础测试框架
- 包含README和开发指南
- 代码风格检查配置完整

## 使用示例

### 示例1：创建Spring Boot项目
**输入**:
```
project_name: my-shop-api
tech_stack: spring-boot
project_type: api
features: mysql, redis, security, swagger
```

**输出**:
```
✅ 项目 my-shop-api 创建成功！

📁 项目结构:
my-shop-api/
├── src/main/java/com/myshop/api/
│   ├── MyShopApiApplication.java
│   ├── config/
│   │   ├── SecurityConfig.java
│   │   ├── RedisConfig.java
│   │   └── SwaggerConfig.java
│   ├── controller/
│   ├── service/
│   ├── repository/
│   └── entity/
├── src/main/resources/
│   ├── application.yml
│   └── application-dev.yml
├── docs/
├── .gitignore
├── pom.xml
└── README.md

🚀 下一步:
1. cd my-shop-api
2. 配置数据库连接（修改 application-dev.yml）
3. 运行 mvn spring-boot:run

📚 文档:
- README.md: 项目说明
- docs/: 开发文档
```

### 示例2：创建Vue3项目
**输入**:
```
project_name: admin-dashboard
tech_stack: vue3
project_type: web
features: typescript, pinia, router, tailwind
```

**输出**:
```
✅ 项目 admin-dashboard 创建成功！

📁 项目结构:
admin-dashboard/
├── src/
│   ├── main.ts
│   ├── App.vue
│   ├── router/
│   │   └── index.ts
│   ├── stores/
│   │   └── counter.ts
│   ├── views/
│   │   └── HomeView.vue
│   ├── components/
│   ├── api/
│   └── assets/
├── public/
├── .gitignore
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.js
└── README.md

🚀 下一步:
1. cd admin-dashboard
2. npm install
3. npm run dev
```

## 依赖工具
- Bash - 执行脚手架命令
- Write - 创建项目文件
- Edit - 修改配置文件

## 注意事项
- 项目名称需符合命名规范（小写、连字符）
- 创建后需检查并修改配置文件
- 根据实际需求调整依赖版本
- 建议先查看生成的README了解项目结构
- 部分功能可能需要额外配置（如数据库连接）