# 需求评审 Skill 目录

本目录包含需求评审相关的 Skill 定义和配置文件。

## 文件列表

| 文件 | 类型 | 描述 |
|------|------|------|
| [requirement-review.md](requirement-review.md) | Skill 定义 | 需求评审 Skill 的完整定义文档 |
| [role-config.yaml](role-config.yaml) | 配置文件 | 需求评审角色配置和参数说明 |

## 快速使用

### 触发命令
```
/requirement-review
```

### 自然语言触发
- "评审需求"
- "需求评审"
- "分析这个需求的影响"
- "检查需求与现有设计的兼容性"

### 常用参数
```yaml
requirement_doc: docs/requirements/xxx.md  # 需求文档路径
review_depth: standard                      # quick / standard / deep
focus_areas: all                            # data / api / performance / all
```

## 输出产物
- 需求评审报告
- 实体影响分析表
- 数据库影响分析
- 风险识别清单
- 待澄清问题列表

## 相关协作
- 上游：产品需求文档、用户故事
- 下游：架构设计（adr）、项目脚手架（scaffold）