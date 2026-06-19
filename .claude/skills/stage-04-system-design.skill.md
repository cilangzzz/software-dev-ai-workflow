---
name: stage-04-system-design
description: 系统设计阶段：生成系统需求、性能指标、容量规划文档
trigger:
  commands:
    - /stage-04
    - /系统设计阶段
  keywords:
    - 系统设计
    - 容量规划
    - 性能指标
---

# 系统设计阶段技能

## 功能描述

启动系统设计阶段工作流，执行以下任务：
1. 结合需求文档和网络资料
2. 生成系统需求文档
3. 包含访问人数、数据增量等系统指标
4. 进行容量规划和技术选型建议

## 输入参数

| 参数名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| project_name | string | 是 | 项目名称 | HIS系统 |
| requirement_docs_dir | string | 是 | 需求文档目录（绝对路径） | F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\02-需求理解 |
| output_dir | string | 否 | 输出目录（绝对路径） | F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\03-系统设计 |
| existing_framework | string | 否 | 已有框架描述 | Spring Boot + Vue3微服务架构 |

## 使用示例

### 示例1：HIS系统设计

```bash
/stage-04 --project_name "HIS系统" --requirement_docs_dir "F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库\02-需求理解"
```

### 示例2：带已有框架描述

```bash
/stage-04 --project_name "电商系统" --requirement_docs_dir "D:\projects\电商\docs\需求理解" --existing_framework "Spring Cloud微服务 + React前端"
```

## 工作流程

1. **需求分析阶段**：分析需求文档提取系统约束
   - 用户规模预估
   - 业务量预估
   - 性能要求
   - 安全要求
   - 可用性要求

2. **资料调研阶段**：搜索真实网络资料（禁止Mock）
   - 系统架构最佳实践
   - 性能优化方案
   - 容量规划方法
   - 缓存策略

3. **指标估算阶段**：估算系统关键指标
   - 日活用户（DAU）
   - 峰值QPS
   - 数据日增量
   - 存储需求
   - 带宽需求
   - 服务器配置建议

4. **文档生成阶段**：生成系统设计文档
   - 系统概述
   - 性能指标
   - 容量规划
   - 技术选型建议
   - 部署架构建议
   - 监控告警建议

## 产出物清单

| 文档名称 | 文件格式 | 存放路径 |
|---------|---------|---------|
| 系统设计文档 | .md | {output_dir}/系统设计文档-{project_name}.md |
| 容量规划报告 | .md | {output_dir}/容量规划报告-{project_name}.md |
| 技术选型建议 | .md | {output_dir}/技术选型建议-{project_name}.md |
| 服务器配置清单 | .xlsx | {output_dir}/服务器配置清单-{project_name}.xlsx |

## 关键指标说明

| 指标类型 | 指标名称 | 说明 |
|---------|---------|------|
| 访问量 | DAU | 日活跃用户数 |
| 访问量 | 峰值QPS | 每秒最大请求数 |
| 数据量 | 日增量 | 每日新增数据量 |
| 数据量 | 年增量 | 每年新增数据量 |
| 性能 | 响应时间 | 平均响应时间要求 |
| 性能 | 可用性 | SLA可用性要求 |

## 注意事项

1. **禁止Mock数据**：所有资料必须通过WebSearch从真实网络获取
2. **容量估算依据**：基于需求分析和参考资料进行科学估算
3. **技术选型合理性**：考虑团队技术栈和项目特点
4. **风险缓冲**：容量规划需预留30%以上缓冲空间

## 关联技能

- [system-architect](../1.0-软件开发流程角色agent模型/研发/skill/architect/system-architect.skill.md)