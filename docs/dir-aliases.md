# Directory Alias Mapping (English → Chinese)

Reference table only. No directories have been renamed.

| 中文目录 | English Alias | 用途 |
|---|---|---|
| 0.0-通用skill | `00-general-skills/` | 通用通用 Skill 库(文档生成 / Agent / 项目分析 / 设计 / 管理 / 报告 / 工具 等) |
| 0.0-通用skill/author-README生成 | `author-readme-gen/` | 自动生成 README 文档 |
| 0.0-通用skill/author-agent | `author-agent/` | 创建自定义 Agent 配置 |
| 0.0-通用skill/author-skill | `author-skill/` | 创建自定义 Skill 脚本 |
| 0.0-通用skill/design-ui-animation | `design-ui-animation/` | UI 交互动效设计素材与示例 |
| 0.0-通用skill/design-前端组件 | `design-frontend-components/` | 前端组件设计规范与素材 |
| 0.0-通用skill/manage-项目管理 | `manage-project/` | 项目管理辅助 Skill |
| 0.0-通用skill/tool-web-fetch | `tool-web-fetch/` | 本地搜索引擎与网页内容抓取 |
| 0.0-通用skill/tool-ssh-skill | `tool-ssh-skill/` | 高性能 SSH 管理工具 |
| 0.0-通用skill/tool-Notion | `tool-notion/` | Notion 文档集成工具 |
| 0.0-通用skill/tool-接口导出 | `tool-api-export/` | 接口文档导出工具 |
| 1.0-软件开发流程角色agent模型 | `10-sdlc-role-agent-model/` | 按角色组织的开发流程 Agent 模型(产品/研发/设计/测试/数据/安全/运维/项目管理) |
| 1.0-软件开发流程角色agent模型/产品 | `roles/product/` | 产品角色 Agent 与 Skill |
| 1.0-软件开发流程角色agent模型/研发 | `roles/engineering/` | 研发角色 Agent、Skill 与技术选型 |
| 1.0-软件开发流程角色agent模型/设计 | `roles/design/` | 设计角色 Skill |
| 1.0-软件开发流程角色agent模型/测试 | `roles/qa/` | 测试角色 Skill |
| 1.0-软件开发流程角色agent模型/数据 | `roles/data/` | 数据角色 Skill |
| 1.0-软件开发流程角色agent模型/安全 | `roles/security/` | 安全角色 Skill |
| 1.0-软件开发流程角色agent模型/运维 | `roles/ops/` | 运维角色 Skill |
| 1.0-软件开发流程角色agent模型/项目管理 | `roles/project-mgmt/` | 项目管理角色 Agent 与 Skill |
| 2.0-用例 | `20-use-cases/` | 端到端用例与样例集合 |
| 2.0-用例/agent用例 | `agent-use-cases/` | 各角色的 Agent 调用样例 |
| 2.0-用例/工作流 | `workflows/` | 全栈 / 端到端工作流示例文档 |
| 2.0-用例/开发流程样例 | `dev-process-samples/` | 瀑布 / 敏捷 / 跨阶段 等开发流程样例 |
| 2.0-用例/系统模型样例 | `system-model-samples/` | ERP / MES / VCP 等系统模型参考 |
| 2.0-用例/项目管理样例 | `project-mgmt-samples/` | 项目管理库示例(管理 / 开发 / 源码 / 版本发布) |
| 3.0-基础开发系统模板 | `30-base-system-templates/` | **git submodule** — 基础系统模板(不重命名) |
| 3.0-基础开发系统模板/backend | `30-base-system-templates/backend` | **git submodule** — 后端基础模板(yudao-skill-pro) |
| 3.0-基础开发系统模板/frontend | `30-base-system-templates/frontend` | **git submodule** — 前端基础模板(yudao-skills-ui-admin-vben) |
| output | `output/` | 抓取 / 转换 / 渲染等脚本与产物输出目录 |
| output/minimax-docs | `output/minimax-docs/` | MiniMax 官方文档抓取与合并产物 |
| output/ui-design-skills | `output/ui-design-skills/` | UI 设计相关 Skill 输出 |
| _deprecated | `_deprecated/` | 已废弃的历史目录归档 |
| _deprecated/skill-v1 | `_deprecated/skill-v1/` | 旧版 Skill v1 归档 |

> 说明:`3.0-*` 为外部 git submodule,保留原名以避免破坏 `.gitmodules`。所有别名仅作文档参考,磁盘上的目录未做任何变更。