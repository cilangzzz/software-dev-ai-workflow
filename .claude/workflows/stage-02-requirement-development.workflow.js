/**
 * 需求开发阶段工作流
 *
 * 功能描述：
 * - 阅读需求分析文档，深度理解需求
 * - 调用产品技能产出功能点清单
 * - 产出业务需求文档（BRD）
 *
 * 输入参数：
 * - project_name: 项目名称
 * - requirement_analysis_dir: 需求分析文档目录（绝对路径）
 * - output_dir: 输出目录（绝对路径）
 * - skill_dir: 产品技能目录（绝对路径）
 */

export const meta = {
  name: 'stage-02-requirement-development',
  description: '需求开发阶段：理解需求 + 产出功能点清单 + BRD文档',
  phases: [
    { title: '需求理解', detail: '深度阅读理解需求分析文档' },
    { title: '功能点提取', detail: '调用产品技能提取功能点' },
    { title: 'BRD生成', detail: '生成业务需求文档' },
    { title: '验证确认', detail: '验证功能点完整性' },
  ],
};

export default async function (args) {
  const {
    project_name,
    requirement_analysis_dir,
    output_dir = 'F:\\sandbox\\workflow\\2.0-用例\\项目管理样例\\02-开发库\\01-需求开发',
    skill_dir = 'F:\\sandbox\\workflow\\1.0-软件开发流程角色agent模型\\产品',
  } = args;

  // Phase 1: 需求理解
  phase('需求理解');

  // 读取需求分析文档
  const requirementDocs = await agent(
    `读取以下目录中的需求分析文档：

    目录路径：${requirement_analysis_dir}

    请读取所有相关文档，并提取：
    1. 核心需求点
    2. 业务目标
    3. 用户角色
    4. 业务流程
    5. 约束条件`,
    {
      label: 'read-requirement-docs',
      phase: '需求理解',
      schema: {
        type: 'object',
        properties: {
          coreRequirements: {
            type: 'array',
            items: { type: 'string' },
          },
          businessGoals: {
            type: 'array',
            items: { type: 'string' },
          },
          userRoles: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                role: { type: 'string' },
                responsibilities: { type: 'string' },
              },
            },
          },
          businessProcesses: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                name: { type: 'string' },
                description: { type: 'string' },
              },
            },
          },
          constraints: {
            type: 'array',
            items: { type: 'string' },
          },
        },
        required: [
          'coreRequirements',
          'businessGoals',
          'userRoles',
          'constraints',
        ],
      },
    }
  );

  log(
    `需求理解完成，识别 ${requirementDocs.coreRequirements?.length || 0} 个核心需求`
  );

  // Phase 2: 功能点提取
  phase('功能点提取');

  const featureExtraction = await agent(
    `基于需求理解结果，使用产品技能提取功能点：

    项目：${project_name}
    核心需求：${requirementDocs.coreRequirements?.join(', ')}
    业务目标：${requirementDocs.businessGoals?.join(', ')}

    用户角色：
    ${requirementDocs.userRoles?.map((r) => `- ${r.role}: ${r.responsibilities}`).join('\n') || '未定义'}

    约束条件：
    ${requirementDocs.constraints?.join('\n') || '无'}

    请使用以下技能文件进行功能点提取：
    ${skill_dir}\\skill\\user-story-generator.skill.md
    ${skill_dir}\\skill\\acceptance-criteria-writer.skill.md

    要求：
    1. 将需求分解为具体功能点
    2. 每个功能点定义清晰的输入输出
    3. 标注功能依赖关系
    4. 使用MoSCoW优先级分类
    5. 估算功能复杂度`,
    {
      label: 'extract-features',
      phase: '功能点提取',
      schema: {
        type: 'object',
        properties: {
          modules: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                moduleName: { type: 'string' },
                moduleCode: { type: 'string' },
                description: { type: 'string' },
                features: {
                  type: 'array',
                  items: {
                    type: 'object',
                    properties: {
                      featureId: { type: 'string' },
                      featureName: { type: 'string' },
                      description: { type: 'string' },
                      inputs: { type: 'array', items: { type: 'string' } },
                      outputs: { type: 'array', items: { type: 'string' } },
                      dependencies: { type: 'array', items: { type: 'string' } },
                      priority: { type: 'string' },
                      complexity: { type: 'string' },
                      userRole: { type: 'string' },
                    },
                  },
                },
              },
            },
          },
          totalFeatures: { type: 'number' },
          mustHave: { type: 'number' },
          shouldHave: { type: 'number' },
          couldHave: { type: 'number' },
        },
        required: ['modules', 'totalFeatures'],
      },
    }
  );

  log(
    `功能点提取完成，共 ${featureExtraction.totalFeatures} 个功能点，其中 Must-Have ${featureExtraction.mustHave} 个`
  );

  // Phase 3: BRD生成
  phase('BRD生成');

  const brdContent = await agent(
    `生成业务需求文档（BRD）：

    项目：${project_name}
    模块信息：${JSON.stringify(featureExtraction.modules, null, 2)}

    请使用以下技能模板：
    ${skill_dir}\\references\\brd-template.md

    要求：
    1. 按模块组织功能点
    2. 包含业务背景、目标、范围
    3. 定义业务规则和约束
    4. 包含验收标准
    5. 标注风险和假设`,
    {
      label: 'generate-brd',
      phase: 'BRD生成',
      schema: {
        type: 'object',
        properties: {
          documentContent: { type: 'string' },
          businessRules: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                ruleId: { type: 'string' },
                ruleName: { type: 'string' },
                description: { type: 'string' },
              },
            },
          },
          risks: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                riskId: { type: 'string' },
                riskDescription: { type: 'string' },
                mitigation: { type: 'string' },
              },
            },
          },
          assumptions: {
            type: 'array',
            items: { type: 'string' },
          },
        },
        required: ['documentContent'],
      },
    }
  );

  log('BRD文档生成完成');

  // Phase 4: 验证确认
  phase('验证确认');

  const validation = await agent(
    `验证功能点和BRD文档完整性：

    功能模块数：${featureExtraction.modules?.length || 0}
    功能点总数：${featureExtraction.totalFeatures}
    业务规则数：${brdContent.businessRules?.length || 0}

    验证标准：
    1. 所有需求都有对应功能点
    2. 功能点有明确优先级
    3. 业务规则完整
    4. 风险已识别`,
    {
      label: 'validate-brd',
      phase: '验证确认',
      schema: {
        type: 'object',
        properties: {
          completeness: { type: 'number' },
          coverageRate: { type: 'number' },
          issues: { type: 'array', items: { type: 'string' } },
          passed: { type: 'boolean' },
        },
        required: ['completeness', 'coverageRate', 'passed'],
      },
    }
  );

  log(`验证完成，完整度 ${validation.completeness}%`);

  return {
    projectName: project_name,
    outputDir: output_dir,
    requirementUnderstanding: requirementDocs,
    featureExtraction: featureExtraction,
    brdDocument: brdContent,
    validation: validation,
  };
}