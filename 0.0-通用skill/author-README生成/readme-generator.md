# Skill: readme-generator

## 基本信息
- **名称**: readme-generator
- **版本**: 1.0.0
- **所属部门**: 文档管理
- **优先级**: P0

## 功能描述
根据项目代码自动生成高质量README文档。分析项目结构、依赖、入口文件，生成完整的项目说明文档。

## 触发条件
- 命令触发: `/readme-generator`
- 自然语言触发:
  - "生成README"
  - "创建项目文档"
  - "生成项目说明"

## 输入参数
| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| project_path | string | 否 | 项目路径，默认当前目录 |
| language | string | 否 | 文档语言：zh / en |
| template | string | 否 | 模板类型：standard / minimal / full |

## 执行流程
1. **项目分析** - 分析项目类型、技术栈
2. **依赖提取** - 提取项目依赖信息
3. **结构解析** - 解析项目目录结构
4. **代码扫描** - 扫描入口文件和配置
5. **文档生成** - 生成README文档

## 输出格式

### README模板
```markdown
# {项目名称}

{项目简介描述}

## 特性

- 特性1
- 特性2

## 快速开始

### 环境要求

- Node.js >= 16
- npm >= 8

### 安装

```bash
# 克隆项目
git clone {repo_url}

# 安装依赖
npm install
```

### 运行

```bash
npm run dev
```

### 构建

```bash
npm run build
```

## 项目结构

```
{project_structure}
```

## 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| {tech} | {version} | {usage} |

## 配置说明

{configuration}

## API文档

{api_docs_link}

## 测试

```bash
npm test
```

## 部署

{deployment_instructions}

## 贡献指南

{contributing}

## 许可证

{license}

## 联系方式

{contact}
```

## 使用示例

### 示例：生成Vue项目README
**输入**:
```
project_path: ./
language: zh
template: standard
```

**输出**:
```markdown
# Shop Admin

电商平台后台管理系统，基于 Vue 3 + TypeScript 开发。

## 特性

- 🚀 基于 Vue 3 + Vite，开发体验优秀
- 📦 组件库使用 Element Plus
- 🎨 支持 Sass 样式预处理
- 📊 集成 ECharts 图表
- 🔐 完整的权限管理系统

## 快速开始

### 环境要求

- Node.js >= 16.0.0
- npm >= 8.0.0
- pnpm >= 8.0.0 (推荐)

### 安装

```bash
# 克隆项目
git clone https://github.com/example/shop-admin.git

# 进入项目目录
cd shop-admin

# 安装依赖
pnpm install
```

### 运行

```bash
# 开发模式
pnpm dev

# 访问 http://localhost:5173
```

### 构建

```bash
# 生产构建
pnpm build

# 预览构建结果
pnpm preview
```

## 项目结构

```
shop-admin/
├── src/
│   ├── api/          # API接口
│   ├── assets/       # 静态资源
│   ├── components/   # 公共组件
│   ├── layouts/      # 布局组件
│   ├── router/       # 路由配置
│   ├── stores/       # 状态管理
│   ├── styles/       # 全局样式
│   ├── utils/        # 工具函数
│   └── views/        # 页面组件
├── public/           # 公共资源
├── .env              # 环境变量
└── vite.config.ts    # Vite配置
```

## 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| Vue | 3.3.x | 前端框架 |
| TypeScript | 5.0.x | 类型支持 |
| Vite | 4.4.x | 构建工具 |
| Element Plus | 2.3.x | UI组件库 |
| Pinia | 2.1.x | 状态管理 |
| Vue Router | 4.2.x | 路由管理 |
| Axios | 1.4.x | HTTP客户端 |
| ECharts | 5.4.x | 图表库 |

## 配置说明

创建 `.env.local` 文件配置本地环境：

```env
VITE_API_BASE_URL=http://localhost:8080/api
VITE_APP_TITLE=电商管理后台
```

## 测试

```bash
# 运行单元测试
pnpm test

# 运行测试并生成覆盖率
pnpm test:coverage
```

## 部署

```bash
# 构建生产版本
pnpm build

# dist 目录部署到静态服务器
```

Docker部署：
```bash
docker build -t shop-admin .
docker run -p 80:80 shop-admin
```

## 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

## 许可证

[MIT](LICENSE)

## 联系方式

- 作者: Your Name
- 邮箱: your.email@example.com
- 项目地址: https://github.com/example/shop-admin
```

## 质量标准
- 信息完整性 ≥ 90%
- 准确性 ≥ 95%
- 可读性良好

## 依赖工具
- Read - 读取项目文件
- Glob - 查找项目文件
- Write - 输出README

## 注意事项
- 生成的内容需要人工审核
- 根据项目实际情况调整内容
- 保持README更新与项目同步