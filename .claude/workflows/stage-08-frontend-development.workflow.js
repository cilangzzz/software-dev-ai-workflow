/**
 * 前端开发阶段工作流
 *
 * 功能描述：
 * - 同步各阶段文档到目录
 * - 调用前端框架skill完成开发
 * - 调用检查工作流至项目没有error
 *
 * 输入参数：
 * - project_name: 项目名称
 * - docs_dir: 各阶段文档目录（绝对路径）
 * - output_dir: 输出目录（绝对路径）
 * - frontend_skill_path: 前端框架skill路径（绝对路径）
 * - backend_doc_dir: 后端接口文档目录（绝对路径）
 */

export const meta = {
  name: 'stage-08-frontend-development',
  description: '前端开发阶段：同步文档 + 调用框架skill开发 + 检查错误',
  phases: [
    { title: '文档同步', detail: '同步各阶段文档和接口文档' },
    { title: 'API层开发', detail: '生成API请求层代码' },
    { title: '页面开发', detail: '生成页面组件代码' },
    { title: '错误检查', detail: '检查并修复项目错误' },
  ],
};

export default async function (args) {
  const {
    project_name,
    docs_dir,
    output_dir,
    frontend_skill_path = 'F:\\projects\\yudao-ai-his-admin-ui\\yudao-ai-his-admin-ui\\CLAUDE.md',
    backend_doc_dir = 'F:\\projects\\yudao-ai-his-backend\\docs\\his',
  } = args;

  // Phase 1: 文档同步
  phase('文档同步');

  const docSync = await agent(
    `同步文档到前端开发目录：

    需求文档目录：${docs_dir}
    后端接口文档目录：${backend_doc_dir}

    请读取并整理：
    1. 需求分析文档（了解业务需求）
    2. 原型设计文档（了解页面布局）
    3. 后端接口文档（对接API）
    4. 数据字典（枚举值）`,
    {
      label: 'sync-docs',
      phase: '文档同步',
      schema: {
        type: 'object',
        properties: {
          requirementDocs: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                docName: { type: 'string' },
                keyPoints: { type: 'array', items: { type: 'string' } },
              },
            },
          },
          apiDocs: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                moduleName: { type: 'string' },
                apiCount: { type: 'number' },
                apis: {
                  type: 'array',
                  items: {
                    type: 'object',
                    properties: {
                      apiName: { type: 'string' },
                      method: { type: 'string' },
                      path: { type: 'string' },
                    },
                  },
                },
              },
            },
          },
          dataDictionary: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                dictType: { type: 'string' },
                values: {
                  type: 'array',
                  items: {
                    type: 'object',
                    properties: {
                      label: { type: 'string' },
                      value: { type: 'string' },
                    },
                  },
                },
              },
            },
          },
        },
        required: ['apiDocs'],
      },
    }
  );

  log(
    `文档同步完成，读取 ${docSync.apiDocs?.length || 0} 个模块接口文档`
  );

  // Phase 2: API层开发
  phase('API层开发');

  const apiLayerResult = await agent(
    `调用前端框架skill生成API层代码：

    项目：${project_name}

    前端框架Skill路径：${frontend_skill_path}

    接口文档：
    ${JSON.stringify(docSync.apiDocs, null, 2)}

    请按照以下规范生成API层代码：

    目标路径：apps/web-antd/src/api/{module}/index.ts

    代码规范：
    1. 使用TypeScript定义类型
    2. 命名空间：His{Module}Api
    3. 统一使用requestClient发起请求
    4. 标准CRUD接口：getXxxPage, getXxx, createXxx, updateXxx, deleteXxx

    代码模板：
    \`\`\`typescript
    import type { PageParam, PageResult } from '@vben/request';
    import { requestClient } from '#/api/request';

    export namespace HisXxxApi {
      export interface Xxx { ... }
      export interface XxxSaveReqVO { ... }
      export interface XxxPageReqVO extends PageParam { ... }
    }

    export function getXxxPage(params: HisXxxApi.XxxPageReqVO) {
      return requestClient.get<PageResult<HisXxxApi.Xxx>>('/his/xxx/page', { params });
    }
    \`\`\``,
    {
      label: 'api-layer-dev',
      phase: 'API层开发',
      schema: {
        type: 'object',
        properties: {
          generatedFiles: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                filePath: { type: 'string' },
                moduleName: { type: 'string' },
                apiCount: { type: 'number' },
              },
            },
          },
          totalApis: { type: 'number' },
          totalFiles: { type: 'number' },
        },
        required: ['generatedFiles', 'totalApis'],
      },
    }
  );

  log(
    `API层开发完成，生成 ${apiLayerResult.totalFiles} 个文件，${apiLayerResult.totalApis} 个API`
  );

  // Phase 3: 页面开发
  phase('页面开发');

  const pageLayerResult = await agent(
    `调用前端框架skill生成页面组件代码：

    项目：${project_name}

    前端框架Skill路径：${frontend_skill_path}

    需求文档：
    ${JSON.stringify(docSync.requirementDocs, null, 2)}

    API层：
    ${JSON.stringify(apiLayerResult.generatedFiles, null, 2)}

    数据字典：
    ${JSON.stringify(docSync.dataDictionary, null, 2)}

    请按照以下规范生成页面组件：

    目标路径：apps/web-antd/src/views/his/{module}/

    标准结构：
    \`\`\`
    views/his/{module}/
    ├── index.vue           # 列表页
    ├── data.ts             # 表格列配置、表单Schema
    ├── detail/
    │   └── index.vue       # 详情页
    └── modules/
        ├── form.vue         # 表单弹窗
        └── form-schema.vue  # 表单Schema（可选）
    \`\`\`

    技术栈：
    - Vue 3.5+ / TypeScript 5.9+
    - Ant Design Vue 4.x
    - VxeTable 4.x
    - Vben Admin框架组件

    页面要素：
    1. 列表页：表格、搜索表单、操作按钮
    2. 表单弹窗：新增/编辑表单
    3. 详情页：数据展示
    4. 权限控制：auth指令`,
    {
      label: 'page-layer-dev',
      phase: '页面开发',
      schema: {
        type: 'object',
        properties: {
          generatedPages: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                moduleName: { type: 'string' },
                pages: {
                  type: 'array',
                  items: {
                    type: 'object',
                    properties: {
                      pageName: { type: 'string' },
                      pagePath: { type: 'string' },
                      description: { type: 'string' },
                    },
                  },
                },
              },
            },
          },
          totalFiles: { type: 'number' },
          routes: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                path: { type: 'string' },
                name: { type: 'string' },
                component: { type: 'string' },
              },
            },
          },
        },
        required: ['generatedPages', 'totalFiles'],
      },
    }
  );

  log(
    `页面开发完成，生成 ${pageLayerResult.totalFiles} 个页面文件`
  );

  // Phase 4: 错误检查
  phase('错误检查');

  let errorCheckResult;
  let retryCount = 0;
  const maxRetries = 3;

  while (retryCount < maxRetries) {
    errorCheckResult = await agent(
      `检查前端项目错误：

      项目路径：${output_dir}

      请执行以下检查：
      1. TypeScript类型检查（pnpm type-check）
      2. ESLint检查（pnpm lint）
      3. 构建检查（pnpm build）
      4. 依赖检查

      如有错误，请修复后重新检查`,
      {
        label: `error-check-${retryCount + 1}`,
        phase: '错误检查',
        schema: {
          type: 'object',
          properties: {
            hasErrors: { type: 'boolean' },
            errorCount: { type: 'number' },
            typeErrors: {
              type: 'array',
              items: {
                type: 'object',
                properties: {
                  file: { type: 'string' },
                  line: { type: 'number' },
                  message: { type: 'string' },
                  fixed: { type: 'boolean' },
                },
              },
            },
            lintErrors: {
              type: 'array',
              items: { type: 'string' },
            },
            buildSuccess: { type: 'boolean' },
          },
          required: ['hasErrors', 'buildSuccess'],
        },
      }
    );

    if (!errorCheckResult.hasErrors) {
      log('错误检查通过，无TypeScript错误');
      break;
    }

    retryCount++;
    log(
      `发现 ${errorCheckResult.errorCount} 个错误，尝试修复 (${retryCount}/${maxRetries})`
    );
  }

  return {
    projectName: project_name,
    outputDir: output_dir,
    docSync: docSync,
    apiLayerResult: apiLayerResult,
    pageLayerResult: pageLayerResult,
    errorCheckResult: errorCheckResult,
  };
}