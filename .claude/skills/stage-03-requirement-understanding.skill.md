---
name: stage-03-requirement-understanding
description: 需求理解阶段：生成原型图、业务流程图、功能点详细描述文档（按模块/子模块/功能点分类组织）
trigger:
  commands:
    - /stage-03
    - /需求理解阶段
  keywords:
    - 需求理解
    - 原型图
    - 业务流程图
downstream:
  - name: "user-story-generator"
    department: "产品"
    path: "产品/skill/user-story-generator.skill.md"
  - name: "acceptance-criteria-writer"
    department: "产品"
    path: "产品/skill/acceptance-criteria-writer.skill.md"
---

# 需求理解阶段技能

## 功能描述

启动需求理解阶段工作流，执行以下任务：
1. 根据业务需求和功能点文档
2. 调用产品技能生成原型图描述
3. 生成业务流程图
4. 产出详细描述文档（**按模块/子模块/功能点分类组织，不能全部塞一个文件夹**）

## 输入参数

| 参数名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| project_name | string | 是 | 项目名称 | HIS系统 |
| requirement_docs_dir | string | 是 | 需求文档目录（绝对路径） | F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\01-需求开发 |
| output_dir | string | 否 | 输出目录（绝对路径） | F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\02-需求理解 |
| skill_dir | string | 否 | 产品技能目录（绝对路径） | F:\sandbox\workflow\1.0-软件开发流程角色agent模型\产品 |

## 使用示例

### 示例1：HIS系统需求理解

```bash
/stage-03 --project_name "HIS系统" --requirement_docs_dir "F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\01-需求开发"
```

### 示例2：带自定义输出目录

```bash
/stage-03 --project_name "电商系统" --requirement_docs_dir "D:\projects\电商\docs\需求开发" --output_dir "D:\projects\电商\docs\需求理解"
```

## 工作流程

1. **文档解析阶段**：解析业务需求和功能点文档
   - 读取BRD文档
   - 提取模块结构
   - 识别用户角色

2. **模块划分阶段**：设计文档目录结构
   - 每个模块独立目录
   - 每个子模块独立子目录
   - 按功能点或业务分类

3. **原型设计阶段**：生成原型图描述（按模块并行）
   - 页面布局描述
   - 交互元素定义
   - 数据展示区域
   - 操作按钮定义

4. **流程设计阶段**：生成业务流程图（按模块并行）
   - 流程节点定义
   - 节点间流转条件
   - 角色职责标注
   - 异常处理分支
   - Mermaid格式描述

5. **文档输出阶段**：按分类输出详细文档
   - 生成README索引文件
   - 按模块组织文档

## 目录结构规范

```
{output_dir}/
├── README.md                    # 总索引
├── M01-门诊管理/                # 模块目录
│   ├── README.md               # 模块索引
│   ├── M01-01-挂号管理/        # 子模块目录
│   │   ├── 功能点清单.md
│   │   ├── 原型设计.md
│   │   └── 业务流程图.md
│   └── M01-02-处方管理/
│       ├── 功能点清单.md
│       ├── 原型设计.md
│       └── 业务流程图.md
├── M02-住院管理/
│   └── ...
└── M06-药品管理/
    └── ...
```

## 产出物清单

| 文档名称 | 文件格式 | 存放路径 |
|---------|---------|---------|
| 模块索引 | .md | {output_dir}/{模块编号}-{模块名称}/README.md |
| 功能点清单 | .md | {output_dir}/{模块}/子模块/功能点清单.md |
| 原型设计文档 | .md | {output_dir}/{模块}/子模块/原型设计.md |
| 业务流程图 | .md | {output_dir}/{模块}/子模块/业务流程图.md |

## 注意事项

1. **目录组织原则**：模块 → 子模块 → 功能点，层级分明
2. **禁止单文件夹**：所有文档不能全部塞一个文件夹
3. **并行生成**：各模块原型和流程设计并行生成
4. **Mermaid格式**：业务流程图使用Mermaid语法

## 关联技能

- [user-story-generator](../../1.0-软件开发流程角色agent模型/产品/skill/user-story-generator.skill.md)
- [acceptance-criteria-writer](../../1.0-软件开发流程角色agent模型/产品/skill/acceptance-criteria-writer.skill.md)