# Skill 总目录（自动生成）

> 来源: `catalog.json`（1.0.0），生成器: `scripts/catalog-generator.py` + `scripts/skill-index-generator.py`
> 共 106 个 Skill（阶段 8 + 角色 61 + 通用 37）

## 1. 按阶段（8 阶段端到端编排）

| 阶段 | 命令 | 描述 | 调用角色 |
|------|------|------|----------|
| [stage-01-requirement-analysis](.claude/skills/stage-01-requirement-analysis.skill.md) | `/stage-01` | 需求分析阶段：多Agent爬取资料 + 产品技能需求调研 + 产出需求分析文档 | `requirement-analyzer` (产品), `user-story-generator` (产品), `acceptance-criteria-writer` (产品) |
| [stage-02-requirement-development](.claude/skills/stage-02-requirement-development.skill.md) | `/stage-02` | 需求开发阶段：理解需求 + 产出功能点清单 + BRD文档 | `user-story-generator` (产品), `acceptance-criteria-writer` (产品), `business-rule-analyzer` (产品) |
| [stage-03-requirement-understanding](.claude/skills/stage-03-requirement-understanding.skill.md) | `/stage-03` | 需求理解阶段：生成原型图、业务流程图、功能点详细描述文档（按模块/子模块/功能点分类组织） | `user-story-generator` (产品), `acceptance-criteria-writer` (产品) |
| [stage-04-system-design](.claude/skills/stage-04-system-design.skill.md) | `/stage-04` | 系统设计阶段：生成系统需求、性能指标、容量规划文档 | `system-architect` (研发) |
| [stage-05-outline-design](.claude/skills/stage-05-outline-design.skill.md) | `/stage-05` | 概要设计阶段：生成业务架构设计、数据库设计 | `system-architect` (研发), `db-designer-java` (研发), `data-model-designer` (研发) |
| [stage-06-module-scheduling](.claude/skills/stage-06-module-scheduling.skill.md) | `/stage-06` | 模块排期阶段：生成系统实现排期计划（哪个完成哪个先） | `milestone-tracker` (项目管理), `schedule-planner` (项目管理) |
| [stage-07-backend-development](.claude/skills/stage-07-backend-development.skill.md) | `/stage-07` | 后端开发阶段：同步文档 + 调用框架skill开发 + 检查错误 + 生成前端对接文档 | `entity-designer-java` (研发), `db-designer-java` (研发), `api-designer-java` (研发), `code-review` (研发) |
| [stage-08-frontend-development](.claude/skills/stage-08-frontend-development.skill.md) | `/stage-08` | 前端开发阶段：同步文档 + 调用框架skill开发 + 检查错误 | `vue-implement` (研发), `vue-best-practices` (研发), `component-designer-vue` (研发) |

## 2. 按部门（角色 Agent 技能）

### 产品（6 个 Skill）

| Skill | 分类 | 描述 |
|-------|------|------|
| [acceptance-criteria-writer](1.0-软件开发流程角色agent模型/产品/skill/acceptance-criteria-writer.skill.md) | - |  |
| [business-rule-analyzer](1.0-软件开发流程角色agent模型/产品/skill/business-rule-analyzer.skill.md) | - |  |
| [requirement-analyzer](1.0-软件开发流程角色agent模型/产品/skill/requirement-analyzer.skill.md) | - |  |
| [requirement-researcher](1.0-软件开发流程角色agent模型/产品/skill/requirement-researcher.skill.md) | - |  |
| [user-manual-writer](1.0-软件开发流程角色agent模型/产品/skill/user-manual-writer.skill.md) | - |  |
| [user-story-generator](1.0-软件开发流程角色agent模型/产品/skill/user-story-generator.skill.md) | - |  |

### 研发（31 个 Skill）

| Skill | 分类 | 描述 |
|-------|------|------|
| [adr](1.0-软件开发流程角色agent模型/研发/skill/process/adr.skill.md) | - |  |
| [api-designer](1.0-软件开发流程角色agent模型/研发/skill/design/api-designer.skill.md) | - |  |
| [api-designer-java](1.0-软件开发流程角色agent模型/研发/skill/design/api-designer-java.skill.md) | - |  |
| [code-review](1.0-软件开发流程角色agent模型/研发/skill/process/code-review.skill.md) | - |  |
| [component-designer-vue](1.0-软件开发流程角色agent模型/研发/skill/design/component-designer-vue.skill.md) | - |  |
| [crud-designer-java](1.0-软件开发流程角色agent模型/研发/skill/design/crud-designer-java.skill.md) | - |  |
| [data-model-designer](1.0-软件开发流程角色agent模型/研发/skill/design/data-model-designer.skill.md) | - |  |
| [db-designer-java](1.0-软件开发流程角色agent模型/研发/skill/design/db-designer-java.skill.md) | - |  |
| [entity-designer-java](1.0-软件开发流程角色agent模型/研发/skill/design/entity-designer-java.skill.md) | - |  |
| [frontend-developer](1.0-软件开发流程角色agent模型/研发/skill/implement/frontend-developer.skill.md) | - | Build React components, implement responsive layouts, and handle client-side sta |
| [java-architect](1.0-软件开发流程角色agent模型/研发/skill/architect/java-architect.skill.md) | - |  |
| [java-implement](1.0-软件开发流程角色agent模型/研发/skill/implement/java-implement.skill.md) | - |  |
| [java-scaffold](1.0-软件开发流程角色agent模型/研发/skill/implement/java-scaffold.skill.md) | - |  |
| [model-view-qt](1.0-软件开发流程角色agent模型/研发/skill/design/model-view-qt.skill.md) | - |  |
| [module-designer](1.0-软件开发流程角色agent模型/研发/skill/design/module-designer.skill.md) | - |  |
| [qt-architect](1.0-软件开发流程角色agent模型/研发/skill/architect/qt-architect.skill.md) | - |  |
| [qt-implement](1.0-软件开发流程角色agent模型/研发/skill/implement/qt-implement.skill.md) | - |  |
| [qt-scaffold](1.0-软件开发流程角色agent模型/研发/skill/implement/qt-scaffold.skill.md) | - |  |
| [react-patterns](1.0-软件开发流程角色agent模型/研发/skill/design/react-patterns.skill.md) | - | React 18/19 patterns including hooks discipline, server/client component boundar |
| [requirement-change](1.0-软件开发流程角色agent模型/研发/skill/process/requirement-change.skill.md) | - |  |
| [requirement-review](1.0-软件开发流程角色agent模型/研发/skill/process/requirement-review.skill.md) | - |  |
| [signal-slot-qt](1.0-软件开发流程角色agent模型/研发/skill/design/signal-slot-qt.skill.md) | - |  |
| [spring-boot-engineer](1.0-软件开发流程角色agent模型/研发/skill/implement/spring-boot-engineer.skill.md) | - | Generates Spring Boot 3.x configurations, creates REST controllers, implements S |
| [spring-boot-testing](1.0-软件开发流程角色agent模型/研发/skill/process/spring-boot-testing.skill.md) | - | Expert Spring Boot 4 testing specialist that selects the best Spring Boot testin |
| [state-machine-designer](1.0-软件开发流程角色agent模型/研发/skill/design/state-machine-designer.skill.md) | - |  |
| [system-architect](1.0-软件开发流程角色agent模型/研发/skill/architect/system-architect.skill.md) | - |  |
| [ui-designer-qt](1.0-软件开发流程角色agent模型/研发/skill/design/ui-designer-qt.skill.md) | - |  |
| [vue](1.0-软件开发流程角色agent模型/研发/skill/implement/vue.skill.md) | - | Vue 3 Composition API, script setup macros, reactivity system, and built-in comp |
| [vue-best-practices](1.0-软件开发流程角色agent模型/研发/skill/design/vue-best-practices.skill.md) | - | MUST be used for Vue.js tasks. Strongly recommends Composition API with `<script |
| [vue-implement](1.0-软件开发流程角色agent模型/研发/skill/implement/vue-implement.skill.md) | - |  |
| [vue-scaffold](1.0-软件开发流程角色agent模型/研发/skill/implement/vue-scaffold.skill.md) | - |  |

### 测试（6 个 Skill）

| Skill | 分类 | 描述 |
|-------|------|------|
| [bug-analyzer](1.0-软件开发流程角色agent模型/测试/skill/bug-analyzer.skill.md) | - |  |
| [react-testing](1.0-软件开发流程角色agent模型/测试/skill/react-testing.skill.md) | - | React component testing with React Testing Library, Vitest/Jest, MSW for network |
| [studio-testing](1.0-软件开发流程角色agent模型/测试/skill/testing.skill.md) | - | Testing strategy for Supabase Studio. Use when writing tests, deciding what |
| [test-case-generator](1.0-软件开发流程角色agent模型/测试/skill/test-case-generator.skill.md) | - |  |
| [test-executor](1.0-软件开发流程角色agent模型/测试/skill/test-executor.skill.md) | - |  |
| [testing-patterns](1.0-软件开发流程角色agent模型/测试/skill/testing-patterns.skill.md) | - | Jest testing patterns, factory functions, mocking strategies, and TDD workflow.  |

### 运维（4 个 Skill）

| Skill | 分类 | 描述 |
|-------|------|------|
| [ci-pipeline-assistant](1.0-软件开发流程角色agent模型/运维/skill/ci-pipeline-assistant.skill.md) | - |  |
| [deploy-analyzer](1.0-软件开发流程角色agent模型/运维/skill/deploy-analyzer.skill.md) | - |  |
| [devops-deploy](1.0-软件开发流程角色agent模型/运维/skill/devops-deploy.skill.md) | - | DevOps e deploy de aplicacoes — Docker, CI/CD com GitHub Actions, AWS Lambda, SA |
| [playwright-devops](1.0-软件开发流程角色agent模型/运维/skill/devops.skill.md) | - | DevOps workflows for Playwright - CI failure analysis, workflow debugging, and r |

### 安全（4 个 Skill）

| Skill | 分类 | 描述 |
|-------|------|------|
| [security-code-review](1.0-软件开发流程角色agent模型/安全/skill/security-code-review.skill.md) | - |  |
| [security-review](1.0-软件开发流程角色agent模型/安全/skill/security-review.skill.md) | - | Use this skill when adding authentication, handling user input, working with sec |
| [security-scan](1.0-软件开发流程角色agent模型/安全/skill/security-scan.skill.md) | - |  |
| [security-threat-model](1.0-软件开发流程角色agent模型/安全/skill/security-threat-model.skill.md) | - |  |

### 数据（2 个 Skill）

| Skill | 分类 | 描述 |
|-------|------|------|
| [data-lineage-trace](1.0-软件开发流程角色agent模型/数据/skill/data-lineage-trace.skill.md) | - |  |
| [data-quality-check](1.0-软件开发流程角色agent模型/数据/skill/data-quality-check.skill.md) | - |  |

### 设计（2 个 Skill）

| Skill | 分类 | 描述 |
|-------|------|------|
| [design-system-analyzer](1.0-软件开发流程角色agent模型/设计/skill/design-system-analyzer.skill.md) | - |  |
| [design-to-code](1.0-软件开发流程角色agent模型/设计/skill/design-to-code.skill.md) | - |  |

### 项目管理（6 个 Skill）

| Skill | 分类 | 描述 |
|-------|------|------|
| [change-handler](1.0-软件开发流程角色agent模型/项目管理/skill/change-handler.skill.md) | - |  |
| [milestone-tracker](1.0-软件开发流程角色agent模型/项目管理/skill/milestone-tracker.skill.md) | - |  |
| [risk-manager](1.0-软件开发流程角色agent模型/项目管理/skill/risk-manager.skill.md) | - |  |
| [schedule-planner](1.0-软件开发流程角色agent模型/项目管理/skill/schedule-planner.skill.md) | - |  |
| [status-reporter](1.0-软件开发流程角色agent模型/项目管理/skill/status-reporter.skill.md) | - |  |
| [workload-analyzer](1.0-软件开发流程角色agent模型/项目管理/skill/workload-analyzer.skill.md) | - |  |

## 3. 按通用能力（0.0-通用skill）

| Skill | 触发词 | 描述 |
|-------|--------|------|
| [author-agent](0.0-通用skill/author-agent/SKILL.md) | - "{关键词1}" | Agent编写专家 - 用于创建、编辑和验证研发Agent角色配置的专业工具。支持后端Java/Python/Go、前端Vue/React/Qt、DBA等多种研 |
| [author-analyzing-projects](0.0-通用skill/author-analyzing-projects/SKILL.md) | - | Analyzes codebases to understand structure, tech stack, patterns, and convention |
| [author-build-project-docs](0.0-通用skill/author-build-project-docs/SKILL.md) | - | 为项目构建分层式LLM友好文档体系。已有项目：扫描项目结构→架构分类→生成CLAUDE.md主索引→基础模块文档→业务模块API/数据模型/坑点文档→配置文档→ |
| [author-skill](0.0-通用skill/author-skill/SKILL.md) | - "{关键词1}" | Skill编写专家 - 用于创建、编辑和验证Claude Code Skill的专业工具。支持多种研发类型按需加载规则、YAML+MD混合格式、输入输出规范定义 |
| [remotion](0.0-通用skill/design-remotion/SKILL.md) | - | Generate walkthrough videos from Stitch projects using Remotion with smooth tran |
| [design-md](0.0-通用skill/design-Stitch设计/design-md/SKILL.md) | - | Analyze Stitch projects and synthesize a semantic design system into DESIGN.md f |
| [enhance-prompt](0.0-通用skill/design-Stitch设计/enhance-prompt/SKILL.md) | - | Transforms vague UI ideas into polished, Stitch-optimized prompts. Enhances spec |
| [stitch-design](0.0-通用skill/design-Stitch设计/stitch-design/SKILL.md) | - | Unified entry point for Stitch design work. Handles prompt enhancement (UI/UX ke |
| [stitch-loop](0.0-通用skill/design-Stitch设计/stitch-loop/SKILL.md) | - | Teaches agents to iteratively build websites using Stitch with an autonomous bat |
| [taste-design](0.0-通用skill/design-Stitch设计/taste-design/SKILL.md) | - | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN. |
| [gsap-core](0.0-通用skill/design-ui-animation/gsap-skills/skills/gsap-core/SKILL.md) | - | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, dura |
| [gsap-frameworks](0.0-通用skill/design-ui-animation/gsap-skills/skills/gsap-frameworks/SKILL.md) | - | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, |
| [gsap-performance](0.0-通用skill/design-ui-animation/gsap-skills/skills/gsap-performance/SKILL.md) | - | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, |
| [gsap-plugins](0.0-通用skill/design-ui-animation/gsap-skills/skills/gsap-plugins/SKILL.md) | - | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoot |
| [gsap-react](0.0-通用skill/design-ui-animation/gsap-skills/skills/gsap-react/SKILL.md) | - | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use |
| [gsap-scrolltrigger](0.0-通用skill/design-ui-animation/gsap-skills/skills/gsap-scrolltrigger/SKILL.md) | - | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub |
| [gsap-timeline](0.0-通用skill/design-ui-animation/gsap-skills/skills/gsap-timeline/SKILL.md) | - | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting |
| [gsap-utils](0.0-通用skill/design-ui-animation/gsap-skills/skills/gsap-utils/SKILL.md) | - | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, ra |
| [motion-design](0.0-通用skill/design-ui-animation/motion-design-skill/SKILL.md) | - | > |
| [flutter-tdesign](0.0-通用skill/design-前端组件/flutter-tdesign/SKILL.md) | - | TDesign Flutter 组件库开发专家 - 基于腾讯 TDesign 设计体系的 Flutter UI 组件库，支持50+预制组件、主题定制、深色模式、 |
| [react:components](0.0-通用skill/design-前端组件/react-components/SKILL.md) | - | Converts Stitch designs into modular Vite and React components using system-leve |
| [shadcn-ui](0.0-通用skill/design-前端组件/shadcn-ui/SKILL.md) | - | Expert guidance for integrating and building applications with shadcn/ui compone |
| [guizang-ppt-skill](0.0-通用skill/report-ppt-html/guizang-ppt-skill/SKILL.md) | - | 生成"电子杂志 × 电子墨水"风格的横向翻页网页 PPT（单 HTML 文件），含 WebGL 流体背景、衬线标题 + 非衬线正文、章节幕封、数据大字报、图片网 |
| [html-ppt](0.0-通用skill/report-ppt-html-teacher/SKILL.md) | - | HTML PPT Studio — author professional static HTML presentations in many styles,  |
| [aliyun-qwen-image](0.0-通用skill/tool-aliyun-qwen-image/SKILL.md) | - | 阿里云百炼Qwen-Image文生图API调用助手 - 用于通过阿里云百炼平台调用Qwen-Image系列模型生成高质量图像。支持同步和异步调用方式、提示词智能 |
| [atlassian-readonly-skills](0.0-通用skill/tool-Atlassian/atlassian-skills/atlassian-readonly-skills/SKILL.md) | - | Read-only Python utilities for Jira, Confluence, and Bitbucket integration. Prov |
| [atlassian-skills](0.0-通用skill/tool-Atlassian/atlassian-skills/atlassian-skills/SKILL.md) | - | Python utilities for Jira, Confluence, and Bitbucket integration. Provides issue |
| [confluence-expert](0.0-通用skill/tool-Atlassian/confluence-expert/SKILL.md) | - | Atlassian Confluence expert for creating and managing spaces, knowledge bases, a |
| [codegen-diagram](0.0-通用skill/tool-Draw.io/codegen-diagram/SKILL.md) | - | 基于当前项目/代码生成 Draw.io 图表，支持技术栈图、系统架构图、数据结构图、E-R 图四种类型。输出符合 Draw.io 语法的 .drawio 文件（ |
| [drawio](0.0-通用skill/tool-Draw.io/drawio/SKILL.md) | - | Generate draw.io diagrams as .drawio files, optionally export to PNG/SVG/PDF wit |
| [notion](0.0-通用skill/tool-Notion/SKILL.md) | - | Read, search, create, and update content in shared Notion pages and databases th |
| [notion-next-format](0.0-通用skill/tool-NotionNext-Format/SKILL.md) | - | NotionNext博客格式专家 - 用于创建、编辑、修改和验证NotionNext博客系统内容。支持文章(Post)的创建、查询、更新、删除；页面(Page) |
| [SkillsMP API](0.0-通用skill/tool-skillmp-api/skillmp-api-master/SKILL.md) | - | Search and discover AI skills from the SkillsMP marketplace |
| [ssh-skill](0.0-通用skill/tool-ssh-skill/SKILL.md) | SSH,服务器,远程,连接,命令,上传,下载,文件传输,跳板机,批量,集群,deploy,部署,运维,登录,执行,查看,检查,管理,操作,访问,传输,迁移,服务器间,tunnel,隧道,端口转发,数据库,内网 | CRITICAL: Use this skill for ALL SSH/server operations. NEVER run raw ssh/scp di |
| [tool-web-fetch](0.0-通用skill/tool-web-fetch/SKILL.md) | - | 本地搜索引擎与网页内容获取工具 - 绕过WebSearch/WebFetch域名限制，支持多API搜索、代理抓取、反爬处理。触发场景：(1) WebSearch |
| [docx](0.0-通用skill/tool-Word文档/docx/docx/SKILL.md) | - | Use this skill whenever the user wants to create, read, edit, or manipulate Word |
| [zentao-api](0.0-通用skill/tool-禅道/SKILL.md) | - | 调用禅道（ZenTao）RESTful API v2.0 完成用户请求，覆盖项目集、产品、项目、执行、需求（Story/Epic/Requirement）、Bu |

## 4. 阶段→角色 调用关系

```
需求分析(stage-01) ─┬─ 产品/requirement-analyzer
                    ├─ 产品/user-story-generator
                    └─ 产品/acceptance-criteria-writer
...
```

完整数据见 [`catalog.json`](../catalog.json) 各 stage skill 的 `downstream` 字段。
