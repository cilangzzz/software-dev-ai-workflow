# 汽车整车装配MES系统模型

## 项目概述

本目录包含汽车整车装配MES（制造执行系统）的完整系统模型，通过AI Agent工作流框架自动生成。该模型覆盖需求分析、模块设计、架构设计、测试用例、用户文档和运维文档等全生命周期产出物。

## 目录结构

```
车企模型/
├── README.md                    # 本文档
├── AI工作流程总结.md             # AI Agent工作流程说明
├── 01-需求分析/                  # 需求阶段产出物
│   ├── 00-MES系统需求总览.md     # 系统需求总览
│   ├── PRD-汽车整车装配MES系统.md # 产品需求文档
│   └── UserStory-汽车整车装配MES系统.md # 用户故事
├── 02-模块设计/                  # 功能模块详细设计
│   ├── 01-生产工单管理模块.md    # 工单管理模块
│   ├── 02-工艺路线管理模块.md    # 工艺路线模块
│   ├── 03-工作站管理模块.md      # 工作站管理
│   ├── 04-装配作业执行模块.md    # 作业执行核心
│   ├── 05-物料管理模块.md        # 物料管理
│   ├── 06-质量管理模块.md        # 质量管理
│   ├── 07-生产追溯模块.md        # 生产追溯
│   ├── 08-生产看板模块.md        # 生产看板
│   ├── 09-设备集成模块.md        # 设备集成
│   └── 10-移动终端模块.md        # 移动终端
├── 03-架构设计/                  # 技术架构产出物
│   ├── 11-ERP系统需求与架构设计.md # ERP集成设计
│   ├── 系统架构设计.md           # 整体架构设计
│   ├── 数据库设计文档.md         # 数据库设计
│   └── API设计文档.md            # API接口设计
├── 04-测试用例/                  # 测试阶段产出物
│   └── 功能测试用例.md           # 功能测试用例
├── 05-用户文档/                  # 用户文档
│   ├── 用户手册.md               # 用户操作手册
│   └── 快速入门指南.md           # 快速入门
├── 06-运维文档/                  # 运维阶段产出物
│   ├── 运维手册.md               # 运维操作手册
│   └── 故障处理手册.md           # 故障处理指南
└──── 代码/                       # 源代码目录
    ├── backend/                  # 后端代码
    ├── frontend/                 # 前端代码
    └── tests/                    # 测试代码
```

---

## 如何使用Agent模型生成系统文档

### 一、Agent模型框架概述

Agent模型位于 `../../../1.0-软件开发流程角色agent模型/` 目录，包含以下角色Agent：

| 部门 | Agent角色 | 主要职责 | Skill数量 |
|------|----------|----------|-----------|
| 产品部 | requirement-analyzer, user-story-generator | 需求分析、用户故事生成 | 4 |
| 研发部 | architect, implement, code-review | 架构设计、代码实现 | 7 |
| 测试部 | test-case-generator, test-executor | 测试用例生成、测试执行 | 3 |
| 运维部 | ci-cd-pipeline, deployment-analyzer | CI/CD配置、部署分析 | 2 |
| 安全部 | security-scan, security-code-review | 安全扫描、代码安全审查 | 3 |
| 数据部 | data-lineage, data-quality-check | 数据血缘追踪、数据质量检查 | 2 |

### 二、生成流程

#### 步骤1：需求探讨（产品部Agent）

**触发方式**：
```
/requirement-analyzer
```

或自然语言：
```
"帮我分析这个需求：需要一个汽车整车装配MES系统"
```

**Agent位置**：`1.0-软件开发流程角色agent模型/产品/skill/requirement-analyzer.skill.md`

**执行流程**：
1. Agent解析需求描述，识别核心需求点
2. 提取关键实体、角色、动作
3. 生成PRD框架文档
4. 输出待澄清问题清单

**产出物示例**：
- `01-需求分析/PRD-汽车整车装配MES系统.md`
- `01-需求分析/00-MES系统需求总览.md`

---

#### 步骤2：用户故事生成（产品部Agent）

**触发方式**：
```
/user-story-generator
```

**Agent位置**：`1.0-软件开发流程角色agent模型/产品/skill/user-story-generator.skill.md`

**执行流程**：
1. 根据PRD文档生成用户故事
2. 定义验收标准（Given-When-Then格式）
3. 按优先级排序用户故事

**产出物示例**：
- `01-需求分析/UserStory-汽车整车装配MES系统.md`

---

#### 步骤3：架构设计（研发部Agent）

**触发方式**：
```
/architect
```

**Agent位置**：`1.0-软件开发流程角色agent模型/研发/backend/java/architect.md`

**执行流程**：
1. 分析需求文档，设计系统架构
2. 定义技术栈和组件划分
3. 设计数据库模型
4. 设计API接口规范

**产出物示例**：
- `03-架构设计/系统架构设计.md`
- `03-架构设计/数据库设计文档.md`
- `03-架构设计/API设计文档.md`

---

#### 步骤4：模块详细设计（研发部Agent）

**触发方式**：
```
/implement
```

**Agent位置**：`1.0-软件开发流程角色agent模型/研发/backend/java/implement.md`

**执行流程**：
1. 解析功能规格和用户故事
2. 设计每个模块的数据模型
3. 定义业务规则和状态流转
4. 设计接口和权限配置

**产出物示例**：
- `02-模块设计/01-生产工单管理模块.md`
- `02-模块设计/04-装配作业执行模块.md`
- ...（其他模块文档）

---

#### 步骤5：测试用例生成（测试部Agent）

**触发方式**：
```
/test-case-generator
```

**Agent位置**：`1.0-软件开发流程角色agent模型/测试/skill/test-case-generator.skill.md`

**执行流程**：
1. 根据用户故事生成测试用例
2. 定义测试步骤和预期结果
3. 覆盖正向和异常场景

**产出物示例**：
- `04-测试用例/功能测试用例.md`

---

#### 步骤6：用户文档生成（产品部Agent）

**触发方式**：
```
/user-manual-writer
```

**Agent位置**：`1.0-软件开发流程角色agent模型/产品/skill/user-manual-writer.skill.md`

**执行流程**：
1. 根据功能设计生成用户手册
2. 编写操作步骤说明
3. 配置界面截图说明

**产出物示例**：
- `05-用户文档/用户手册.md`
- `05-用户文档/快速入门指南.md`

---

#### 步骤7：运维文档生成（运维部Agent）

**触发方式**：
```
/deployment-analyzer
```

**Agent位置**：`1.0-软件开发流程角色agent模型/运维/skill/deployment-analyzer.md  # TODO: Skill 未实现 (阶段三 catalog 收口)`

**执行流程**：
1. 分析系统部署需求
2. 生成部署脚本和配置
3. 编写运维操作手册
4. 编写故障处理指南

**产出物示例**：
- `06-运维文档/运维手册.md`
- `06-运维文档/故障处理手册.md`

---

### 三、Agent协作配置

Agent之间通过 `skill-collaboration.yaml` 配置协作关系：

**配置文件位置**：`1.0-软件开发流程角色agent模型/研发/skill-collaboration.yaml`

```yaml
# Agent协作配置示例
workflows:
  - name: requirement-to-design
    sequence:
      - agent: requirement-analyzer
        phase: 需求分析
        outputs:
          - PRD文档
          - 需求澄清清单
      - agent: architect
        phase: 架构设计
        inputs:
          - PRD文档
        outputs:
          - 系统架构设计
          - 数据库设计

  - name: design-to-implementation
    sequence:
      - agent: implement
        phase: 模块设计
        inputs:
          - 系统架构设计
          - 数据库设计
        outputs:
          - 模块设计文档
          - 数据模型
```

---

### 四、完整生成示例

#### 场景：生成新的MES模块文档

```bash
# 1. 首先分析需求
用户: "我需要一个新的设备维护管理模块"

# 2. AI触发产品部Agent
AI执行: /requirement-analyzer
产出: 设备维护模块需求框架

# 3. 生成用户故事
AI执行: /user-story-generator
产出: 设备维护模块用户故事

# 4. 架构设计
AI执行: /architect
产出: 设备维护模块数据模型和API设计

# 5. 详细设计
AI执行: /implement
产出: 02-模块设计/11-设备维护管理模块.md

# 6. 测试用例
AI执行: /test-case-generator
产出: 设备维护模块测试用例

# 7. 用户文档
AI执行: /user-manual-writer
产出: 设备维护模块用户手册章节
```

---

### 五、产出物模板参考

Agent模型提供了标准化的产出物模板：

| 模板名称 | 位置 | 用途 |
|----------|------|------|
| PRD模板 | `产品/references/prd-template.md` | PRD文档结构参考 |
| SRS模板 | `产品/references/srs-template.md` | 软件需求规格模板 |
| TRD模板 | `产品/references/trd-template.md` | 技术需求文档模板 |
| 高质量标准 | `产品/references/high-quality-standard.md` | 文档质量标准 |

---

### 六、质量门控标准

每个阶段的产出物需通过质量门控检查：

| 阶段 | 检查项 | 通过标准 |
|------|--------|----------|
| 需求就绪 | PRD完整性、用户故事覆盖度 | 100%需求覆盖 |
| 设计就绪 | 架构设计评审通过、数据库设计完整 | 技术评审通过 |
| 开发就绪 | 代码审查通过、单元测试覆盖率 | 覆盖率≥80% |
| 测试就绪 | 测试用例执行完成、无P0/P1 Bug | Bug修复率100% |

---

## 相关文档

- [AI工作流程总结](AI工作流程总结.md) - 完整工作流程说明
- [Agent模型目录](../../../1.0-软件开发流程角色agent模型/) - Agent角色定义
- 产出物映射表 <!-- TODO: ../../../1.0-软件开发流程角色agent模型/产出物映射表.md 链接待修复 --> - 阶段产出物映射

---

## 更新记录

| 日期 | 更新内容 | 更新人 |
|------|----------|--------|
| 2026-03-24 | 初始化系统模型，生成核心模块文档 | AI Agent |
| 2026-06-10 | 优化目录结构，添加README文档 | Claude Agent |