---
name: stage-02-requirement-development
description: 需求开发阶段：理解需求 + 产出功能点清单 + BRD文档
trigger:
  commands:
    - /stage-02
    - /需求开发阶段
  keywords:
    - 需求开发
    - 功能点清单
    - BRD文档
---

# 需求开发阶段技能

## 功能描述

启动需求开发阶段工作流，执行以下任务：
1. 阅读需求分析文档，深度理解需求
2. 调用产品技能产出功能点清单
3. 产出业务需求文档（BRD）

## 输入参数

| 参数名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| project_name | string | 是 | 项目名称 | HIS系统 |
| requirement_analysis_dir | string | 是 | 需求分析文档目录（绝对路径） | F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\00-需求分析阶段 |
| output_dir | string | 否 | 输出目录（绝对路径） | F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\01-需求开发 |
| skill_dir | string | 否 | 产品技能目录（绝对路径） | F:\sandbox\workflow\1.0-软件开发流程角色agent模型\产品 |

## 使用示例

### 示例1：HIS系统需求开发

```bash
/stage-02 --project_name "HIS系统" --requirement_analysis_dir "F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\00-需求分析阶段"
```

### 示例2：带自定义输出目录

```bash
/stage-02 --project_name "电商系统" --requirement_analysis_dir "D:\projects\电商\docs\需求分析" --output_dir "D:\projects\电商\docs\需求开发"
```

## 工作流程

1. **需求理解阶段**：深度阅读需求分析文档
   - 读取PRD文档
   - 提取核心需求点
   - 识别业务目标
   - 理解用户角色

2. **功能点提取阶段**：调用产品技能提取功能点
   - 将需求分解为具体功能点
   - 定义输入输出边界
   - 标注功能依赖关系
   - MoSCoW优先级分类
   - 估算功能复杂度

3. **BRD生成阶段**：生成业务需求文档
   - 按模块组织功能点
   - 定义业务规则
   - 标注风险和假设
   - 制定验收标准

4. **验证确认阶段**：验证功能点完整性
   - 需求覆盖验证
   - 功能点完整性检查

## 产出物清单

| 文档名称 | 文件格式 | 存放路径 |
|---------|---------|---------|
| 功能点清单 | .xlsx | {output_dir}/功能点清单-{project_name}.xlsx |
| BRD业务需求文档 | .md | {output_dir}/BRD-{project_name}.md |
| 业务规则文档 | .md | {output_dir}/业务规则-{project_name}.md |

## 注意事项

1. **依赖前阶段**：必须先完成需求分析阶段
2. **功能点分类**：使用MoSCoW方法（Must/Should/Could/Won't）
3. **复杂度估算**：简单/中等/复杂三级估算
4. **模块化组织**：功能点按模块分组

## 关联技能

- [user-story-generator](../1.0-软件开发流程角色agent模型/产品/skill/user-story-generator.skill.md)
- [acceptance-criteria-writer](../1.0-软件开发流程角色agent模型/产品/skill/acceptance-criteria-writer.skill.md)
- [business-rule-analyzer](../1.0-软件开发流程角色agent模型/产品/skill/business-rule-analyzer.skill.md)