---
name: stage-06-module-scheduling
description: 模块排期阶段：生成系统实现排期计划（哪个完成哪个先）
trigger:
  commands:
    - /stage-06
    - /模块排期阶段
  keywords:
    - 模块排期
    - 开发排期
    - 项目排期
---

# 模块排期阶段技能

## 功能描述

启动模块排期阶段工作流，执行以下任务：
1. 分析模块间依赖关系
2. 基于业务价值和技术依赖进行优先级排序
3. 估算各模块开发工期
4. 生成完整排期计划（**哪个完成哪个先**）

## 输入参数

| 参数名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| project_name | string | 是 | 项目名称 | HIS系统 |
| outline_design_dir | string | 是 | 概要设计文档目录（绝对路径） | F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\04-概要设计 |
| output_dir | string | 否 | 输出目录（绝对路径） | F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\05-详细设计 |
| team_size | number | 否 | 团队人数 | 5 |
| start_date | string | 否 | 开始日期（YYYY-MM-DD） | 2026-06-19 |

## 使用示例

### 示例1：HIS系统排期

```bash
/stage-06 --project_name "HIS系统" --outline_design_dir "F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\04-概要设计" --team_size 5
```

### 示例2：带自定义参数

```bash
/stage-06 --project_name "电商系统" --outline_design_dir "D:\projects\电商\docs\概要设计" --team_size 10 --start_date "2026-07-01"
```

## 工作流程

1. **依赖分析阶段**：分析模块间依赖关系
   - 识别所有模块
   - 构建依赖图
   - 标记核心模块
   - 识别可独立开发的模块

2. **优先级排序阶段**：基于业务价值和技术依赖排序
   - **核心基础模块优先**
   - **被依赖模块优先于依赖模块**
   - **Must-Have功能优先于Should-Have**
   - **可并行开发的模块同时开始**

3. **工期估算阶段**：估算各模块开发工期
   - 功能点数量统计
   - 功能复杂度估算
   - 人日估算计算
   - 风险缓冲预留

4. **排期生成阶段**：生成完整排期计划
   - 详细排期甘特图描述
   - 各阶段里程碑定义
   - 资源分配建议
   - 交付节点定义

## 排期原则

| 原则 | 说明 |
|-----|------|
| 依赖优先 | 被依赖的模块必须先完成 |
| 核心优先 | 核心基础模块优先开发 |
| 并行开发 | 无依赖的模块可并行开发 |
| 业务价值 | 高业务价值模块优先 |

## 工期估算标准

| 复杂度 | 人日估算 | 说明 |
|-------|---------|------|
| 简单 | 1-2人日 | 简单CRUD、查询页面 |
| 中等 | 3-5人日 | 带业务逻辑的功能 |
| 复杂 | 5-10人日 | 涉及流程、算法、集成 |

## 产出物清单

| 文档名称 | 文件格式 | 存放路径 |
|---------|---------|---------|
| 开发排期计划 | .md | {output_dir}/开发排期计划-{project_name}.md |
| 里程碑清单 | .md | {output_dir}/里程碑清单-{project_name}.md |
| 模块工期估算 | .xlsx | {output_dir}/模块工期估算-{project_name}.xlsx |
| 甘特图描述 | .md | {output_dir}/甘特图描述-{project_name}.md |
| 资源分配建议 | .md | {output_dir}/资源分配建议-{project_name}.md |

## 排期文档模板

```markdown
# 开发排期计划

## 项目信息
- 项目名称：{project_name}
- 开始日期：{start_date}
- 团队人数：{team_size}
- 预计工期：{total_duration} 天
- 结束日期：{estimated_end_date}

## 里程碑
| 里程碑 | 目标日期 | 交付物 |
|-------|---------|--------|
| M1-基础模块完成 | {date} | {deliverables} |
| M2-核心功能完成 | {date} | {deliverables} |

## 模块排期
| 模块 | 开始 | 结束 | 工期 | 依赖 | 状态 |
|-----|------|------|------|------|------|
| {module} | {date} | {date} | {days} | {deps} | 待开始 |
```

## 注意事项

1. **依赖关系准确**：必须准确识别模块间依赖
2. **并行组划分**：合理划分可并行开发的模块组
3. **关键路径识别**：标记影响整体工期的关键路径
4. **风险缓冲**：预留30%以上风险缓冲时间

## 关联技能

- [milestone-tracker](../1.0-软件开发流程角色agent模型/项目管理/skill/milestone-tracker.skill.md)
- [schedule-planner](../1.0-软件开发流程角色agent模型/项目管理/skill/schedule-planner.skill.md)