# 项目优化方案

> 本文件记录 `software-dev-ai-workflow` 仓库的结构分析与优化方案。
> 最后更新：2026-08-21

## 一、项目概览

**定位**：软件开发工作流 AI.SKILL 框架——通过 Agent（角色）+ Skill（技能）分离的结构，引导 AI 完成需求→设计→开发→测试→部署→运维的全链路工作。

**顶层架构**：

```
f:/sandbox/workflow/
├── README.md                         # 项目门户
├── LICENSE / .gitignore / .gitmodules
├── .claude/                          # Claude Code 编排层（8 阶段 workflow）
├── _deprecated/                      # 旧版 Skill 归档（阶段一新增）
├── 0.0-通用skill/                    # 27 个通用工具/元技能
├── 1.0-软件开发流程角色agent模型/    # 8 部门 Agent+Skill 定义
├── 2.0-用例/                         # 流程/系统/项目案例库
├── 3.0-基础开发系统模板/             # git submodule 真实代码框架
├── assets/outputs/                   # README 引用素材
└── output/                           # 抓取生成的临时产物（gitignored）
```

## 二、阶段一执行清单（**已完成**）

| 编号 | 动作 | 状态 |
|------|------|------|
| 1.1 | 把 6 个 `*-v2.skill.md` 移到 `_deprecated/skill-v1/` 并改名为 `*-v1.skill.md` | ✅ |
| 1.2 | 在 `_deprecated/README.md` 与 `_deprecated/skill-v1/README.md` 写明维护规则 | ✅ |
| 1.3 | 删除 `0.0-通用skill/tool-ssh-skill/references`（空目录） | ✅ |
| 1.4 | 删除 `2.0-用例/项目管理样例/02-开发库/00-需求分析阶段`（与 `00-需求分析/` 同名重复） | ✅ |
| 1.5 | 删除 `2.0-用例/系统模型样例/{erp/车企模型,vcp}/.workspace/`（AI 创作临时文件，共 8 个 md） | ✅ |
| 1.6 | 在 `.gitignore` 中加入 `.workspace/` 模式 | ✅ |
| 1.7 | 在 `2.0-用例/README.md` 中加入 `_archive/` 链接 | ✅ |
| 1.8 | **未执行**（保留中文路径、保留 `SKILL.md` 大小写、保留所有 git submodule 占位） | ⏭ |

**未执行的非破坏性动作**：
- **SKILL.md → *.skill.md 改名**：涉及 35 个文件、影响 Claude Code 加载机制，风险较高，留待阶段三 catalog 落地后统一处理。
- **目录重命名为英文**：用户已形成中文路径肌肉记忆，建议保留。

## 三、阶段二执行清单（**待执行**）

| 编号 | 动作 | 优先级 |
|------|------|--------|
| 2.1 | 修复 `1.0-软件开发流程角色agent模型/产出物映射表.md` 死链：`../2.0-软件开发流程/...` → `../2.0-用例/开发流程样例/...` | P0 |
| 2.2 | 修复 `1.0/README.md` Skill 索引：补齐缺失条目，与 v2 已删除同步 | P0 |
| 2.3 | 统一主 `README.md` 数字："21+" → "27+" | P1 |
| 2.4 | 主 `README.md` 目录树补 `.claude/` 入口 | P1 |
| 2.5 | 修复各 `产出物清单.md` 内部相对路径 | P0 |
| 2.6 | 为 `1.0/README.md` Skill 表格追加 `文件路径` 列 | P2 |

## 四、阶段三~六执行清单（**路线图**）

- **阶段三**：建立 `catalog.json` 机器可读清单 + 产出物清单单一事实源
- **阶段四**：目录命名英文化（可选，向后兼容）
- **阶段五**：可发现性增强（INDEX.md、4-quadrant 导航、补 agent 用例）
- **阶段六**：`scripts/validate-skills.py` + GitHub Actions CI

## 五、关键发现汇总

### 🔴 P0 结构性问题
- 命名风格不统一：`SKILL.md` / `*.skill.md` / `*.md` 混用
- `产出物清单.md` 重复 25 份
- 6 处 `*-v2.skill.md` 与现版本并存
- 空目录 / `.workspace/` 创作临时文件
- `_archive/` 残留未与新版 README 互链

### 🟠 P1 可发现性问题
- README 引用大量死链（路径含 `2.0-软件开发流程/`、`2.0-软件开发流程生命周期/` 等已不存在的目录）
- `0.0-通用skill` 与 `1.0` 边界模糊
- `README.md` 数字与实际不符（21+ vs 27）

### 🟡 P2 体验性细节
- `output/` 混入爬虫临时产物
- assets/outputs/ 缺少"如何绘制"说明
- 缺机器可读 catalog

## 六、变更追踪

### 阶段一 diff 摘要（待提交）

```
新增：
  _deprecated/README.md
  _deprecated/skill-v1/README.md
  OPTIMIZATION_PLAN.md            ← 本文件
修改：
  .gitignore                       (+5 行：.workspace/ 模式)
  2.0-用例/README.md               (+5 行：_archive 链接)
移动/重命名（git mv）：
  1.0/.../requirement-analyzer-v2.skill.md  → _deprecated/skill-v1/requirement-analyzer-v1.skill.md
  1.0/.../security-scan-v2.skill.md          → _deprecated/skill-v1/security-scan-v1.skill.md
  1.0/.../test-case-generator-v2.skill.md    → _deprecated/skill-v1/test-case-generator-v1.skill.md
  1.0/.../architect-v2.skill.md              → _deprecated/skill-v1/architect-v1.skill.md
  1.0/.../code-review-v2.skill.md            → _deprecated/skill-v1/code-review-v1.skill.md
  1.0/.../ci-cd-pipeline-v2.skill.md         → _deprecated/skill-v1/ci-cd-pipeline-v1.skill.md
删除：
  0.0-通用skill/tool-ssh-skill/references/                            (空)
  2.0-用例/项目管理样例/02-开发库/00-需求分析阶段/                    (空、重复)
  2.0-用例/系统模型样例/erp/车企模型/.workspace/{contract,feedback,progress,spec}.md
  2.0-用例/系统模型样例/vcp/.workspace/{contract,feedback,progress,spec}.md
```

总计：
- 新增：3 个文件
- 修改：2 个文件
- 移动：6 个文件
- 删除：10 个文件 + 2 个空目录
- **净减少约 13 项**