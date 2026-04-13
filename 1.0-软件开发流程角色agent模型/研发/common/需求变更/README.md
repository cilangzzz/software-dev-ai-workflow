# 需求变更 Skill 目录

本目录包含需求变更管理相关的 Skill 定义和配置文件。

## 文件列表

| 文件 | 类型 | 描述 |
|------|------|------|
| [requirement-change.md](requirement-change.md) | Skill 定义 | 需求变更管理 Skill 的完整定义文档 |
| [role-config.yaml](role-config.yaml) | 配置文件 | 需求变更角色配置和参数说明 |

## 快速使用

### 触发命令
```
/requirement-change
```

### 自然语言触发
- "需求变更"
- "分析变更影响"
- "变更影响评估"
- "处理需求变更"

### 常用参数
```yaml
change_request: 变更请求描述内容
change_type: feature          # feature / fix / refactor / migration
priority: high                # urgent / high / normal / low
design_docs: docs/design/     # 设计文档路径
```

## 变更类型说明

| 类型 | 描述 | 适用场景 |
|------|------|----------|
| feature | 新功能 | 新增业务功能开发 |
| fix | 问题修复 | Bug修复、缺陷处理 |
| refactor | 重构优化 | 代码重构、结构优化 |
| migration | 数据迁移 | 数据结构调整、系统迁移 |

## 输出产物
- 变更影响分析报告
- DDL变更脚本
- 数据迁移脚本
- 回滚方案
- 变更追溯记录

## 影响分析维度
1. 数据模型影响 - 实体、属性、关系变更
2. 领域设计影响 - 聚合边界、领域服务变更
3. 数据库设计影响 - 表结构、索引、数据迁移
4. 代码影响 - 服务层、API、前端组件变更