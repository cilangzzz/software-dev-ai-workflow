/**
 * 需求理解阶段工作流
 *
 * 功能描述：
 * - 根据业务需求和功能点文档
 * - 调用产品技能生成原型图、业务流程图
 * - 产出详细描述文档，按模块/子模块/功能点分类组织
 *
 * 输入参数：
 * - project_name: 项目名称
 * - requirement_docs_dir: 需求文档目录（绝对路径）
 * - output_dir: 输出目录（绝对路径）
 * - skill_dir: 产品技能目录（绝对路径）
 */

export const meta = {
  name: 'stage-03-requirement-understanding',
  description: '需求理解阶段：生成原型图、业务流程图、功能点详细描述文档',
  phases: [
    { title: '文档解析', detail: '解析业务需求和功能点文档' },
    { title: '模块划分', detail: '按模块/子模块组织功能结构' },
    { title: '原型设计', detail: '生成原型图描述' },
    { title: '流程设计', detail: '生成业务流程图' },
    { title: '文档输出', detail: '按分类输出详细文档' },
  ],
};

export default async function (args) {
  const {
    project_name,
    requirement_docs_dir,
    output_dir = 'F:\\sandbox\\workflow\\2.0-用例\\项目管理样例\\02-开发库\\02-需求理解',
    skill_dir = 'F:\\sandbox\\workflow\\1.0-软件开发流程角色agent模型\\产品',
  } = args;

  // Phase 1: 文档解析
  phase('文档解析');

  const docsAnalysis = await agent(
    `解析需求文档目录中的所有文档：

    目录路径：${requirement_docs_dir}

    请读取并分析：
    1. BRD业务需求文档
    2. 功能点清单
    3. 用户故事

    提取关键信息用于后续原型和流程设计`,
    {
      label: 'parse-docs',
      phase: '文档解析',
      schema: {
        type: 'object',
        properties: {
          businessContext: { type: 'string' },
          modules: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                moduleId: { type: 'string' },
                moduleName: { type: 'string' },
                moduleCode: { type: 'string' },
                description: { type: 'string' },
                subModules: {
                  type: 'array',
                  items: {
                    type: 'object',
                    properties: {
                      subModuleId: { type: 'string' },
                      subModuleName: { type: 'string' },
                      features: {
                        type: 'array',
                        items: {
                          type: 'object',
                          properties: {
                            featureId: { type: 'string' },
                            featureName: { type: 'string' },
                            description: { type: 'string' },
                            userRole: { type: 'string' },
                          },
                        },
                      },
                    },
                  },
                },
              },
            },
          },
          userRoles: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                roleId: { type: 'string' },
                roleName: { type: 'string' },
                permissions: { type: 'array', items: { type: 'string' } },
              },
            },
          },
        },
        required: ['modules', 'userRoles'],
      },
    }
  );

  log(
    `文档解析完成，识别 ${docsAnalysis.modules?.length || 0} 个模块`
  );

  // Phase 2: 模块划分（构建目录结构）
  phase('模块划分');

  const moduleStructure = await agent(
    `根据模块信息设计文档目录结构：

    模块信息：${JSON.stringify(docsAnalysis.modules, null, 2)}

    要求：
    1. 每个模块独立目录
    2. 每个子模块独立子目录
    3. 按功能点或业务分类
    4. 不能全部塞一个文件夹

    输出目录结构设计`,
    {
      label: 'design-structure',
      phase: '模块划分',
      schema: {
        type: 'object',
        properties: {
          directoryStructure: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                path: { type: 'string' },
                description: { type: 'string' },
                documents: {
                  type: 'array',
                  items: { type: 'string' },
                },
              },
            },
          },
        },
        required: ['directoryStructure'],
      },
    }
  );

  log('目录结构设计完成');

  // Phase 3: 原型设计（按模块并行）
  phase('原型设计');

  const prototypeDesigns = await pipeline(
    docsAnalysis.modules || [],
    async (moduleInfo) => {
      return agent(
        `为模块设计原型图描述：

        模块：${moduleInfo.moduleName} (${moduleInfo.moduleCode})
        描述：${moduleInfo.description}

        子模块：
        ${moduleInfo.subModules?.map((s) => `- ${s.subModuleName}`).join('\n') || '无'}

        请生成原型图描述文档，包含：
        1. 页面布局描述
        2. 交互元素定义
        3. 数据展示区域
        4. 操作按钮定义

        注意：这是原型描述，不是实际UI代码`,
        {
          label: `prototype-${moduleInfo.moduleCode}`,
          phase: '原型设计',
          schema: {
            type: 'object',
            properties: {
              moduleId: { type: 'string' },
              moduleName: { type: 'string' },
              pages: {
                type: 'array',
                items: {
                  type: 'object',
                  properties: {
                    pageName: { type: 'string' },
                    pageCode: { type: 'string' },
                    layout: { type: 'string' },
                    elements: {
                      type: 'array',
                      items: {
                        type: 'object',
                        properties: {
                          elementType: { type: 'string' },
                          elementName: { type: 'string' },
                          position: { type: 'string' },
                          description: { type: 'string' },
                        },
                      },
                    },
                    interactions: {
                      type: 'array',
                      items: { type: 'string' },
                    },
                  },
                },
              },
            },
            required: ['moduleId', 'pages'],
          },
        }
      );
    }
  );

  log(`原型设计完成，共 ${prototypeDesigns.filter(Boolean).length} 个模块`);

  // Phase 4: 流程设计（按模块并行）
  phase('流程设计');

  const flowDesigns = await pipeline(
    docsAnalysis.modules || [],
    async (moduleInfo) => {
      return agent(
        `为模块设计业务流程图：

        模块：${moduleInfo.moduleName}
        子模块功能点：
        ${JSON.stringify(moduleInfo.subModules, null, 2)}

        用户角色：
        ${docsAnalysis.userRoles?.map((r) => `- ${r.roleName}`).join('\n') || '未定义'}

        请生成业务流程图描述，包含：
        1. 流程节点定义
        2. 节点间的流转条件
        3. 角色职责标注
        4. 异常处理分支

        使用Mermaid格式描述流程`,
        {
          label: `flow-${moduleInfo.moduleCode}`,
          phase: '流程设计',
          schema: {
            type: 'object',
            properties: {
              moduleId: { type: 'string' },
              moduleName: { type: 'string' },
              flows: {
                type: 'array',
                items: {
                  type: 'object',
                  properties: {
                    flowName: { type: 'string' },
                    flowCode: { type: 'string' },
                    description: { type: 'string' },
                    mermaidCode: { type: 'string' },
                    nodes: {
                      type: 'array',
                      items: {
                        type: 'object',
                        properties: {
                          nodeId: { type: 'string' },
                          nodeName: { type: 'string' },
                          nodeType: { type: 'string' },
                          responsibleRole: { type: 'string' },
                        },
                      },
                    },
                  },
                },
              },
            },
            required: ['moduleId', 'flows'],
          },
        }
      );
    }
  );

  log(`流程设计完成，共 ${flowDesigns.filter(Boolean).length} 个模块`);

  // Phase 5: 文档输出
  phase('文档输出');

  const outputDocs = await agent(
    `生成最终文档结构，按模块/子模块/功能点组织：

    目录结构：${JSON.stringify(moduleStructure.directoryStructure, null, 2)}

    原型设计：${JSON.stringify(prototypeDesigns.filter(Boolean), null, 2)}

    流程设计：${JSON.stringify(flowDesigns.filter(Boolean), null, 2)}

    请生成完整的文档内容，确保：
    1. 每个模块有独立目录
    2. 每个子模块有独立子目录
    3. 功能点按分类存放
    4. 包含README索引文件`,
    {
      label: 'output-docs',
      phase: '文档输出',
      schema: {
        type: 'object',
        properties: {
          totalDirectories: { type: 'number' },
          totalDocuments: { type: 'number' },
          documentList: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                path: { type: 'string' },
                title: { type: 'string' },
                type: { type: 'string' },
              },
            },
          },
        },
        required: ['totalDirectories', 'totalDocuments', 'documentList'],
      },
    }
  );

  log(
    `文档输出完成，共 ${outputDocs.totalDocuments} 个文档，${outputDocs.totalDirectories} 个目录`
  );

  return {
    projectName: project_name,
    outputDir: output_dir,
    moduleStructure: moduleStructure,
    prototypeDesigns: prototypeDesigns.filter(Boolean),
    flowDesigns: flowDesigns.filter(Boolean),
    outputDocs: outputDocs,
  };
}