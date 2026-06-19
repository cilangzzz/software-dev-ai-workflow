/**
 * 后端开发阶段工作流
 *
 * 功能描述：
 * - 同步各阶段文档到目录
 * - 调用后端框架skill完成开发
 * - 调用检查工作流至项目没有error
 * - 生成前端对接文档
 *
 * 输入参数：
 * - project_name: 项目名称
 * - docs_dir: 各阶段文档目录（绝对路径）
 * - output_dir: 输出目录（绝对路径）
 * - backend_skill_path: 后端框架skill路径（绝对路径）
 * - frontend_doc_dir: 前端对接文档目录（绝对路径）
 */

export const meta = {
  name: 'stage-07-backend-development',
  description: '后端开发阶段：同步文档 + 调用框架skill开发 + 检查错误 + 生成前端对接文档',
  phases: [
    { title: '文档同步', detail: '同步各阶段文档到开发目录' },
    { title: '代码开发', detail: '调用后端框架skill完成开发' },
    { title: '错误检查', detail: '检查并修复项目错误' },
    { title: '接口文档', detail: '生成前端对接文档' },
  ],
};

export default async function (args) {
  const {
    project_name,
    docs_dir,
    output_dir,
    backend_skill_path = 'F:\\projects\\yudao-ai-his-backend\\CLAUDE.md',
    frontend_doc_dir = 'F:\\projects\\yudao-ai-his-backend\\docs\\his',
  } = args;

  // Phase 1: 文档同步
  phase('文档同步');

  const docSync = await agent(
    `同步各阶段文档到开发目录：

    文档来源目录：${docs_dir}

    请读取以下阶段的文档：
    1. 需求分析阶段文档
    2. 需求开发阶段文档
    3. 概要设计阶段文档
    4. 数据库设计文档
    5. 排期计划文档

    整理并提取开发所需信息`,
    {
      label: 'sync-docs',
      phase: '文档同步',
      schema: {
        type: 'object',
        properties: {
          syncedDocuments: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                docName: { type: 'string' },
                docPath: { type: 'string' },
                keyPoints: { type: 'array', items: { type: 'string' } },
              },
            },
          },
          developmentRequirements: {
            type: 'object',
            properties: {
              modules: { type: 'array', items: { type: 'string' } },
              apis: { type: 'array', items: { type: 'string' } },
              entities: { type: 'array', items: { type: 'string' } },
            },
          },
        },
        required: ['syncedDocuments'],
      },
    }
  );

  log(
    `文档同步完成，同步 ${docSync.syncedDocuments?.length || 0} 份文档`
  );

  // Phase 2: 代码开发
  phase('代码开发');

  const developmentResult = await agent(
    `调用后端框架skill完成开发：

    项目：${project_name}

    后端框架Skill路径：${backend_skill_path}

    开发需求：
    ${JSON.stringify(docSync.developmentRequirements, null, 2)}

    请按照以下流程开发：
    1. 阅读后端框架skill文档
    2. 根据数据库设计生成实体类
    3. 生成Mapper接口
    4. 生成Service层代码
    5. 生成Controller层代码

    技术栈：Spring Boot 3.x / MyBatis-Plus / Swagger v3

    命名规范：
    - DO类：XxxDO
    - Mapper：XxxMapper
    - Service：XxxService / XxxServiceImpl
    - Controller：XxxController
    - VO：XxxSaveReqVO / XxxPageReqVO / XxxRespVO`,
    {
      label: 'backend-dev',
      phase: '代码开发',
      schema: {
        type: 'object',
        properties: {
          generatedFiles: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                filePath: { type: 'string' },
                fileType: { type: 'string' },
                moduleName: { type: 'string' },
                description: { type: 'string' },
              },
            },
          },
          totalFiles: { type: 'number' },
          modules: { type: 'array', items: { type: 'string' } },
          apis: { type: 'array', items: { type: 'string' } },
        },
        required: ['generatedFiles', 'totalFiles'],
      },
    }
  );

  log(
    `代码开发完成，生成 ${developmentResult.totalFiles} 个文件`
  );

  // Phase 3: 错误检查
  phase('错误检查');

  let errorCheckResult;
  let retryCount = 0;
  const maxRetries = 3;

  while (retryCount < maxRetries) {
    errorCheckResult = await agent(
      `检查项目错误：

      项目路径：${output_dir}

      请执行以下检查：
      1. 编译检查（mvn compile 或 gradle build）
      2. 代码规范检查
      3. 依赖检查
      4. 单元测试（如有）

      如有错误，请修复后重新检查`,
      {
        label: `error-check-${retryCount + 1}`,
        phase: '错误检查',
        schema: {
          type: 'object',
          properties: {
            hasErrors: { type: 'boolean' },
            errorCount: { type: 'number' },
            errors: {
              type: 'array',
              items: {
                type: 'object',
                properties: {
                  file: { type: 'string' },
                  line: { type: 'number' },
                  errorType: { type: 'string' },
                  message: { type: 'string' },
                  fixed: { type: 'boolean' },
                },
              },
            },
            warnings: {
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
      log('错误检查通过，无编译错误');
      break;
    }

    retryCount++;
    log(
      `发现 ${errorCheckResult.errorCount} 个错误，尝试修复 (${retryCount}/${maxRetries})`
    );
  }

  // Phase 4: 接口文档
  phase('接口文档');

  const apiDocumentation = await agent(
    `生成前端对接文档：

    项目：${project_name}

    开发结果：
    ${JSON.stringify(developmentResult, null, 2)}

    输出目录：${frontend_doc_dir}

    请生成以下文档：
    1. API接口文档（按模块组织）
    2. 请求参数说明
    3. 响应数据结构
    4. 错误码说明
    5. 接口调用示例

    文档格式：
    - Markdown格式
    - 包含Swagger注解信息
    - 按模块分文件组织`,
    {
      label: 'api-doc',
      phase: '接口文档',
      schema: {
        type: 'object',
        properties: {
          generatedDocs: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                docName: { type: 'string' },
                docPath: { type: 'string' },
                apiCount: { type: 'number' },
              },
            },
          },
          totalApis: { type: 'number' },
          modules: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                moduleName: { type: 'string' },
                apiCount: { type: 'number' },
                docPath: { type: 'string' },
              },
            },
          },
        },
        required: ['generatedDocs', 'totalApis'],
      },
    }
  );

  log(
    `接口文档生成完成，共 ${apiDocumentation.totalApis} 个API`
  );

  return {
    projectName: project_name,
    outputDir: output_dir,
    frontendDocDir: frontend_doc_dir,
    docSync: docSync,
    developmentResult: developmentResult,
    errorCheckResult: errorCheckResult,
    apiDocumentation: apiDocumentation,
  };
}