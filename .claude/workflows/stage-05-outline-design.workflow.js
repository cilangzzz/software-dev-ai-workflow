/**
 * 概要设计阶段工作流
 *
 * 功能描述：
 * - 根据业务需求调用研发技能
 * - 生成业务架构设计
 * - 生成数据库设计
 *
 * 输入参数：
 * - project_name: 项目名称
 * - requirement_docs_dir: 需求文档目录（绝对路径）
 * - system_design_dir: 系统设计文档目录（绝对路径）
 * - output_dir: 输出目录（绝对路径）
 * - skill_dir: 研发技能目录（绝对路径）
 */

export const meta = {
  name: 'stage-05-outline-design',
  description: '概要设计阶段：生成业务架构设计、数据库设计',
  phases: [
    { title: '需求理解', detail: '理解业务需求和系统约束' },
    { title: '架构设计', detail: '生成业务架构设计文档' },
    { title: '数据库设计', detail: '生成数据库设计文档' },
    { title: '评审验证', detail: '评审设计文档质量' },
  ],
};

export default async function (args) {
  const {
    project_name,
    requirement_docs_dir,
    system_design_dir,
    output_dir = 'F:\\sandbox\\workflow\\2.0-用例\\项目管理样例\\02-开发库\\04-概要设计',
    skill_dir = 'F:\\sandbox\\workflow\\1.0-软件开发流程角色agent模型\\研发',
  } = args;

  // Phase 1: 需求理解
  phase('需求理解');

  const requirements = await agent(
    `读取需求文档和系统设计文档：

    需求文档目录：${requirement_docs_dir}
    系统设计文档目录：${system_design_dir}

    请提取：
    1. 业务模块清单
    2. 功能点清单
    3. 数据实体清单
    4. 系统约束条件
    5. 性能指标要求`,
    {
      label: 'understand-requirements',
      phase: '需求理解',
      schema: {
        type: 'object',
        properties: {
          businessModules: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                moduleId: { type: 'string' },
                moduleName: { type: 'string' },
                moduleCode: { type: 'string' },
                description: { type: 'string' },
              },
            },
          },
          dataEntities: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                entityName: { type: 'string' },
                entityCode: { type: 'string' },
                attributes: { type: 'array', items: { type: 'string' } },
                relationships: { type: 'array', items: { type: 'string' } },
              },
            },
          },
          systemConstraints: {
            type: 'array',
            items: { type: 'string' },
          },
          performanceTargets: {
            type: 'object',
            properties: {
              responseTime: { type: 'string' },
              throughput: { type: 'string' },
              availability: { type: 'string' },
            },
          },
        },
        required: ['businessModules', 'dataEntities'],
      },
    }
  );

  log(
    `需求理解完成，识别 ${requirements.businessModules?.length || 0} 个业务模块，${requirements.dataEntities?.length || 0} 个数据实体`
  );

  // Phase 2: 架构设计
  phase('架构设计');

  const architectureDesign = await agent(
    `使用研发技能进行业务架构设计：

    项目：${project_name}

    业务模块：
    ${JSON.stringify(requirements.businessModules, null, 2)}

    系统约束：
    ${requirements.systemConstraints?.join('\n') || '无'}

    性能目标：
    ${JSON.stringify(requirements.performanceTargets, null, 2)}

    请使用以下技能进行架构设计：
    ${skill_dir}\\skill\\architect\\system-architect.skill.md

    要求：
    1. 使用C4模型进行架构设计
    2. 生成Context层、Container层、Component层设计
    3. 编写ADR决策记录
    4. 评估技术选型
    5. 识别架构风险`,
    {
      label: 'architecture-design',
      phase: '架构设计',
      schema: {
        type: 'object',
        properties: {
          c4Model: {
            type: 'object',
            properties: {
              context: {
                type: 'object',
                properties: {
                  description: { type: 'string' },
                  externalSystems: {
                    type: 'array',
                    items: {
                      type: 'object',
                      properties: {
                        name: { type: 'string' },
                        type: { type: 'string' },
                        interaction: { type: 'string' },
                      },
                    },
                  },
                },
              },
              containers: {
                type: 'array',
                items: {
                  type: 'object',
                  properties: {
                    containerName: { type: 'string' },
                    containerType: { type: 'string' },
                    technology: { type: 'string' },
                    description: { type: 'string' },
                  },
                },
              },
              components: {
                type: 'array',
                items: {
                  type: 'object',
                  properties: {
                    containerName: { type: 'string' },
                    componentName: { type: 'string' },
                    description: { type: 'string' },
                    interfaces: { type: 'array', items: { type: 'string' } },
                  },
                },
              },
            },
          },
          adrRecords: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                adrId: { type: 'string' },
                title: { type: 'string' },
                decision: { type: 'string' },
                rationale: { type: 'string' },
              },
            },
          },
          techStack: {
            type: 'object',
            properties: {
              frontend: { type: 'string' },
              backend: { type: 'string' },
              database: { type: 'string' },
              cache: { type: 'string' },
              messageQueue: { type: 'string' },
            },
          },
          risks: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                riskId: { type: 'string' },
                description: { type: 'string' },
                impact: { type: 'string' },
                mitigation: { type: 'string' },
              },
            },
          },
        },
        required: ['c4Model', 'techStack'],
      },
    }
  );

  log('架构设计完成');

  // Phase 3: 数据库设计
  phase('数据库设计');

  const databaseDesign = await agent(
    `使用研发技能进行数据库设计：

    数据实体：
    ${JSON.stringify(requirements.dataEntities, null, 2)}

    业务模块：
    ${JSON.stringify(requirements.businessModules, null, 2)}

    技术栈：
    ${JSON.stringify(architectureDesign.techStack, null, 2)}

    请使用以下技能进行数据库设计：
    ${skill_dir}\\skill\\design\\db-designer-java.skill.md
    ${skill_dir}\\skill\\design\\data-model-designer.skill.md

    要求：
    1. 设计表结构（符合多租户、审计追踪、逻辑删除规范）
    2. 定义索引策略
    3. 设计ER关系图
    4. 编写建表SQL脚本
    5. 定义数据字典`,
    {
      label: 'database-design',
      phase: '数据库设计',
      schema: {
        type: 'object',
        properties: {
          tables: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                tableName: { type: 'string' },
                tableComment: { type: 'string' },
                moduleCode: { type: 'string' },
                columns: {
                  type: 'array',
                  items: {
                    type: 'object',
                    properties: {
                      columnName: { type: 'string' },
                      columnType: { type: 'string' },
                      nullable: { type: 'boolean' },
                      comment: { type: 'string' },
                    },
                  },
                },
                indexes: {
                  type: 'array',
                  items: {
                    type: 'object',
                    properties: {
                      indexName: { type: 'string' },
                      columns: { type: 'array', items: { type: 'string' } },
                      isUnique: { type: 'boolean' },
                    },
                  },
                },
              },
            },
          },
          erDiagram: { type: 'string' },
          dataDictionary: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                dictType: { type: 'string' },
                dictName: { type: 'string' },
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
          ddlScripts: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                fileName: { type: 'string' },
                content: { type: 'string' },
              },
            },
          },
        },
        required: ['tables', 'erDiagram'],
      },
    }
  );

  log(
    `数据库设计完成，共 ${databaseDesign.tables?.length || 0} 张表`
  );

  // Phase 4: 评审验证
  phase('评审验证');

  const reviewResult = await agent(
    `评审概要设计文档质量：

    架构设计：
    - C4模型完整性：${architectureDesign.c4Model ? '✓' : '✗'}
    - ADR记录数：${architectureDesign.adrRecords?.length || 0}
    - 风险识别数：${architectureDesign.risks?.length || 0}

    数据库设计：
    - 表数量：${databaseDesign.tables?.length || 0}
    - 数据字典完整性：${databaseDesign.dataDictionary?.length || 0} 项

    验证标准：
    1. C4模型Level 1-3完整
    2. 关键决策有ADR记录
    3. 表结构符合规范（多租户、审计字段）
    4. 索引设计合理

    请输出评审报告`,
    {
      label: 'review-design',
      phase: '评审验证',
      schema: {
        type: 'object',
        properties: {
          architectureScore: { type: 'number' },
          databaseScore: { type: 'number' },
          overallScore: { type: 'number' },
          issues: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                category: { type: 'string' },
                issue: { type: 'string' },
                severity: { type: 'string' },
                suggestion: { type: 'string' },
              },
            },
          },
          passed: { type: 'boolean' },
        },
        required: ['overallScore', 'passed'],
      },
    }
  );

  log(`评审完成，综合评分 ${reviewResult.overallScore}/10`);

  return {
    projectName: project_name,
    outputDir: output_dir,
    requirements: requirements,
    architectureDesign: architectureDesign,
    databaseDesign: databaseDesign,
    reviewResult: reviewResult,
  };
}