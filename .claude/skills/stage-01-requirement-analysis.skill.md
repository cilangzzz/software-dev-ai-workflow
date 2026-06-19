---
name: stage-01-requirement-analysis
description: 需求分析阶段：多Agent爬取资料 + 产品技能需求调研 + 产出需求分析文档
trigger:
  commands:
    - /stage-01
    - /需求分析阶段
  keywords:
    - 需求分析
    - 开始需求分析
    - 需求调研
---

# 需求分析阶段技能

## 功能描述

启动需求分析阶段工作流，执行以下任务：
1. 多Agent并行爬取用户需求文档相关资料（**禁止Mock数据，必须使用真实网络资料**）
2. 调用产品技能进行需求调研
3. 产出需求分析文档（PRD框架、用户故事、澄清问题清单）

## 输入参数

| 参数名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| project_name | string | 是 | 项目名称 | HIS系统 |
| requirement_description | string | 是 | 用户需求描述 | 实现医院门诊管理、住院管理功能 |
| output_dir | string | 否 | 输出目录（绝对路径） | F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\00-需求分析阶段 |
| skill_dir | string | 否 | 产品技能目录（绝对路径） | F:\sandbox\workflow\1.0-软件开发流程角色agent模型\产品 |

## 使用示例

### 示例1：HIS系统需求分析

```bash
/stage-01 --project_name "HIS系统" --requirement_description "实现医院门诊管理、住院管理、药品管理三大核心功能模块"
```

### 示例2：带自定义输出目录

```bash
/stage-01 --project_name "电商系统" --requirement_description "实现商品管理、订单管理、支付功能" --output_dir "D:\projects\电商\docs\需求分析"
```

## 工作流程

1. **资料爬取阶段**：多Agent并行搜索真实网络资料
   - 搜索需求相关文档模板
   - 搜索业务流程最佳实践
   - 搜索系统设计参考资料
   - 搜索用户需求案例分析

2. **需求调研阶段**：调用产品技能深度调研
   - 解析模糊需求，识别核心业务痛点
   - 提取关键实体、角色、业务流程
   - 生成用户故事（符合INVEST原则）
   - 功能需求RICE评分

3. **文档生成阶段**：产出结构化文档
   - PRD框架文档
   - 用户故事集
   - 待澄清问题清单

4. **质量验证阶段**：验证文档质量
   - 需求覆盖率 ≥ 95%
   - INVEST原则符合度 100%
   - RICE评分完整性

## 产出物清单

| 文档名称 | 文件格式 | 存放路径 |
|---------|---------|---------|
| PRD框架文档 | .md | {output_dir}/PRD-{project_name}.md |
| 用户故事集 | .md | {output_dir}/用户故事-{project_name}.md |
| 待澄清问题 | .md | {output_dir}/待确认问题-{project_name}.md |

## 注意事项

1. **禁止Mock数据**：所有资料必须通过WebSearch从真实网络获取
2. **产品技能调用**：使用requirement-analyzer-v2.skill.md进行调研
3. **优先级评分**：功能需求必须使用RICE模型评分
4. **用户故事规范**：必须符合INVEST原则（Independent, Negotiable, Valuable, Estimable, Small, Testable）

## 关联技能

- [requirement-analyzer-v2](../1.0-软件开发流程角色agent模型/产品/skill/requirement-analyzer-v2.skill.md)
- [user-story-generator](../1.0-软件开发流程角色agent模型/产品/skill/user-story-generator.skill.md)
- [acceptance-criteria-writer](../1.0-软件开发流程角色agent模型/产品/skill/acceptance-criteria-writer.skill.md)