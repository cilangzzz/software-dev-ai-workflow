---
name: stage-08-frontend-development
description: 前端开发阶段：同步文档 + 调用框架skill开发 + 检查错误
trigger:
  commands:
    - /stage-08
    - /前端开发阶段
  keywords:
    - 前端开发
    - 前端实现
---

# 前端开发阶段技能

## 功能描述

启动前端开发阶段工作流，执行以下任务：
1. 同步各阶段文档到目录
2. 调用前端框架skill完成开发
3. 调用检查工作流至项目没有error

## 输入参数

| 参数名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| project_name | string | 是 | 项目名称 | HIS系统 |
| docs_dir | string | 是 | 各阶段文档目录（绝对路径） | F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库 |
| output_dir | string | 是 | 前端项目目录（绝对路径） | F:\projects\yudao-ai-his-admin-ui\yudao-ai-his-admin-ui |
| frontend_skill_path | string | 否 | 前端框架skill路径（绝对路径） | F:\projects\yudao-ai-his-admin-ui\yudao-ai-his-admin-ui\CLAUDE.md |
| backend_doc_dir | string | 否 | 后端接口文档目录（绝对路径） | F:\projects\yudao-ai-his-backend\docs\his |

## 使用示例

### 示例1：HIS系统前端开发

```bash
/stage-08 --project_name "HIS系统" --docs_dir "F:\sandbox\workflow\2.0-用例\项目管理样例\02-开发库" --output_dir "F:\projects\yudao-ai-his-admin-ui\yudao-ai-his-admin-ui"
```

### 示例2：带自定义skill路径

```bash
/stage-08 --project_name "电商系统" --docs_dir "D:\projects\电商\docs" --output_dir "D:\projects\电商\frontend" --frontend_skill_path "D:\projects\电商\frontend\CLAUDE.md" --backend_doc_dir "D:\projects\电商\backend\docs\api"
```

## 工作流程

1. **文档同步阶段**：同步各阶段文档和接口文档
   - 需求分析文档（了解业务需求）
   - 原型设计文档（了解页面布局）
   - 后端接口文档（对接API）
   - 数据字典（枚举值）

2. **API层开发阶段**：生成API请求层代码
   - TypeScript类型定义
   - API请求函数
   - 标准CRUD接口

3. **页面开发阶段**：生成页面组件代码
   - 列表页（表格、搜索、操作）
   - 表单弹窗（新增/编辑）
   - 详情页（数据展示）
   - 路由配置

4. **错误检查阶段**：检查并修复项目错误（最多重试3次）
   - TypeScript类型检查
   - ESLint检查
   - 构建检查

## 代码规范

### 文件命名

| 类型 | 命名规则 | 示例 |
|------|---------|------|
| API文件 | 小写连字符 | patient/index.ts |
| 页面文件 | 小写连字符 | patient/index.vue |
| 组件文件 | PascalCase | PatientForm.vue |
| 组合式函数 | use前缀 | usePatientForm.ts |

### TypeScript命名

| 类型 | 命名规则 | 示例 |
|------|---------|------|
| 命名空间 | His{Module}Api | HisPatientApi |
| 实体类型 | 大驼峰 | Patient |
| 保存请求 | {Entity}SaveReqVO | PatientSaveReqVO |
| 分页请求 | {Entity}PageReqVO | PatientPageReqVO |

### 目录结构

```
apps/web-antd/src/
├── api/his/                    # API层
│   ├── patient/index.ts        # 患者管理API
│   ├── register/index.ts       # 挂号管理API
│   └── ...
├── views/his/                  # 页面层
│   ├── patient/                # 患者管理页面
│   │   ├── index.vue           # 列表页
│   │   ├── data.ts             # 表格列配置
│   │   └── modules/
│   │       └── form.vue        # 表单弹窗
│   └── ...
└── router/routes/modules/
    └── his.ts                  # HIS路由配置
```

### 页面组件规范

```vue
<script lang="ts" setup>
import type { VxeTableGridOptions } from '#/adapter/vxe-table';
import type { HisXxxApi } from '#/api/his/xxx';

import { Page, useVbenModal } from '@vben/common-ui';
import { useVbenVxeGrid } from '#/adapter/vxe-table';
import { getXxxPage } from '#/api/his/xxx';

import { useGridColumns, useGridFormSchema } from './data';
import Form from './modules/form.vue';

const [FormModal, formModalApi] = useVbenModal({
  connectedComponent: Form,
  destroyOnClose: true,
});

const [Grid, gridApi] = useVbenVxeGrid({
  formOptions: {
    schema: useGridFormSchema(),
  },
  gridOptions: {
    columns: useGridColumns(),
    proxyConfig: {
      ajax: {
        query: async ({ page }, formValues) => {
          return await getXxxPage({
            pageNo: page.currentPage,
            pageSize: page.pageSize,
            ...formValues,
          });
        },
      },
    },
  } as VxeTableGridOptions<HisXxxApi.Xxx>,
});
</script>

<template>
  <Page auto-content-height>
    <FormModal @success="gridApi.query()" />
    <Grid />
  </Page>
</template>
```

## 产出物清单

| 文档名称 | 文件格式 | 存放路径 |
|---------|---------|---------|
| API层代码 | .ts | {output_dir}/src/api/his/{module}/ |
| 页面组件 | .vue | {output_dir}/src/views/his/{module}/ |
| 表格配置 | .ts | {output_dir}/src/views/his/{module}/data.ts |
| 表单组件 | .vue | {output_dir}/src/views/his/{module}/modules/form.vue |
| 路由配置 | .ts | {output_dir}/src/router/routes/modules/his.ts |

## 注意事项

1. **必须提供前端项目目录**：output_dir必须指向实际的前端项目根目录
2. **框架skill路径**：必须提供前端框架的CLAUDE.md文件路径
3. **后端接口文档**：必须提供后端生成的API接口文档目录
4. **错误修复**：最多重试3次修复TypeScript和ESLint错误
5. **权限控制**：使用auth指令进行权限控制

## 前端框架技术栈

- Vue 3.5+
- TypeScript 5.9+
- Vite 8.0+
- Pinia 3.0+
- Ant Design Vue 4.x
- VxeTable 4.x
- Tailwind CSS 4.x
- Vben Admin框架

## 关联技能

- [vue-implement](../1.0-软件开发流程角色agent模型/研发/skill/implement/vue-implement.skill.md)
- [vue-best-practices](../1.0-软件开发流程角色agent模型/研发/skill/design/vue-best-practices.skill.md)
- [component-designer-vue](../1.0-软件开发流程角色agent模型/研发/skill/design/component-designer-vue.skill.md)