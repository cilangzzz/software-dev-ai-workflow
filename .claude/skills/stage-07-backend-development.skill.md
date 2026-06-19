---
name: stage-07-backend-development
description: 后端开发阶段：同步文档 + 调用框架skill开发 + 检查错误 + 生成前端对接文档
trigger:
  commands:
    - /stage-07
    - /后端开发阶段
  keywords:
    - 后端开发
    - 后端实现
---

# 后端开发阶段技能

## 功能描述

启动后端开发阶段工作流，执行以下任务：
1. 同步各阶段文档到开发目录
2. 调用后端框架skill完成开发
3. 调用检查工作流至项目没有error
4. 生成前端对接文档

## 输入参数

| 参数名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| project_name | string | 是 | 项目名称 | HIS系统 |
| docs_dir | string | 是 | 各阶段文档目录（绝对路径） | F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库 |
| output_dir | string | 是 | 后端项目目录（绝对路径） | F:\projects\yudao-ai-his-backend |
| backend_skill_path | string | 否 | 后端框架skill路径（绝对路径） | F:\projects\yudao-ai-his-backend\CLAUDE.md |
| frontend_doc_dir | string | 否 | 前端对接文档目录（绝对路径） | F:\projects\yudao-ai-his-backend\docs\his |

## 使用示例

### 示例1：HIS系统后端开发

```bash
/stage-07 --project_name "HIS系统" --docs_dir "F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库" --output_dir "F:\projects\yudao-ai-his-backend"
```

### 示例2：带自定义skill路径

```bash
/stage-07 --project_name "电商系统" --docs_dir "D:\projects\电商\docs" --output_dir "D:\projects\电商\backend" --backend_skill_path "D:\projects\电商\backend\CLAUDE.md" --frontend_doc_dir "D:\projects\电商\backend\docs\api"
```

## 工作流程

1. **文档同步阶段**：同步各阶段文档到开发目录
   - 需求分析文档
   - 概要设计文档
   - 数据库设计文档
   - 排期计划文档

2. **代码开发阶段**：调用后端框架skill完成开发
   - 阅读后端框架skill文档
   - 根据数据库设计生成实体类（DO）
   - 生成Mapper接口
   - 生成Service层代码
   - 生成Controller层代码
   - 生成VO类

3. **错误检查阶段**：检查并修复项目错误（最多重试3次）
   - 编译检查（mvn compile）
   - 代码规范检查
   - 依赖检查
   - 单元测试

4. **接口文档阶段**：生成前端对接文档
   - API接口文档（按模块组织）
   - 请求参数说明
   - 响应数据结构
   - 错误码说明
   - 接口调用示例

## 代码规范

### 命名规范

| 类型 | 命名规则 | 示例 |
|------|---------|------|
| DO类 | XxxDO | PatientDO |
| Mapper | XxxMapper | PatientMapper |
| Service接口 | XxxService | PatientService |
| Service实现 | XxxServiceImpl | PatientServiceImpl |
| Controller | XxxController | PatientController |
| 保存VO | XxxSaveReqVO | PatientSaveReqVO |
| 分页VO | XxxPageReqVO | PatientPageReqVO |
| 响应VO | XxxRespVO | PatientRespVO |

### 分层架构

```
cn.iocoder.yudao.module.{模块}
├── controller/admin/{功能}/     # Controller + VO
├── service/{功能}/              # Service 接口 + 实现
├── dal/dataobject/{功能}/       # DO 实体
├── dal/mysql/{功能}/            # Mapper
└── enums/                       # 错误码 + 枚举
```

### 权限标识

格式：`{模块}:{功能}:{操作}`

| 操作 | 权限示例 |
|-----|---------|
| 查询 | his:patient:query |
| 新增 | his:patient:create |
| 修改 | his:patient:update |
| 删除 | his:patient:delete |

## 产出物清单

| 文档名称 | 文件格式 | 存放路径 |
|---------|---------|---------|
| 实体类 | .java | {output_dir}/dal/dataobject/ |
| Mapper接口 | .java | {output_dir}/dal/mysql/ |
| Service接口 | .java | {output_dir}/service/ |
| Service实现 | .java | {output_dir}/service/ |
| Controller | .java | {output_dir}/controller/admin/ |
| VO类 | .java | {output_dir}/controller/admin/{功能}/vo/ |
| API接口文档 | .md | {frontend_doc_dir}/ |

## 注意事项

1. **必须提供后端项目目录**：output_dir必须指向实际的后端项目根目录
2. **框架skill路径**：必须提供后端框架的CLAUDE.md文件路径
3. **错误修复**：最多重试3次修复错误
4. **文档同步**：确保开发目录有最新的设计文档

## 后端框架技术栈

- Spring Boot 3.x
- MyBatis-Plus
- Swagger v3
- Spring AI
- Flowable（工作流）

## 关联技能

- [entity-designer-java](../1.0-软件开发流程角色agent模型/研发/skill/design/entity-designer-java.skill.md)
- [db-designer-java](../1.0-软件开发流程角色agent模型/研发/skill/design/db-designer-java.skill.md)
- [api-designer-java](../1.0-软件开发流程角色agent模型/研发/skill/design/api-designer-java.skill.md)
- [code-review-v2](../1.0-软件开发流程角色agent模型/研发/skill/process/code-review-v2.skill.md)