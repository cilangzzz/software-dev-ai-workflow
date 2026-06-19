/**
 * 模块排期阶段工作流
 *
 * 功能描述：
 * - 生成系统实现的排期计划
 * - 基于功能依赖和优先级确定开发顺序
 * - 哪个完成哪个先的原则
 *
 * 输入参数：
 * - project_name: 项目名称
 * - outline_design_dir: 概要设计文档目录（绝对路径）
 * - output_dir: 输出目录（绝对路径）
 * - team_size: 团队人数（可选）
 * - start_date: 开始日期（可选）
 */

export const meta = {
  name: 'stage-06-module-scheduling',
  description: '模块排期阶段：生成系统实现排期计划',
  phases: [
    { title: '依赖分析', detail: '分析模块间依赖关系' },
    { title: '优先级排序', detail: '基于业务价值和技术依赖排序' },
    { title: '工期估算', detail: '估算各模块开发工期' },
    { title: '排期生成', detail: '生成完整排期计划' },
  ],
};

export default async function (args) {
  const {
    project_name,
    outline_design_dir,
    output_dir = 'F:\\sandbox\\workflow\\2.0-用例\\项目管理样例\\02-开发库\\05-详细设计',
    team_size = 5,
    start_date = new Date().toISOString().split('T')[0],
  } = args;

  // Phase 1: 依赖分析
  phase('依赖分析');

  const dependencyAnalysis = await agent(
    `读取概要设计文档，分析模块依赖关系：

    目录路径：${outline_design_dir}

    请提取：
    1. 所有模块清单
    2. 模块间依赖关系
    3. 核心模块识别
    4. 可独立开发的模块`,
    {
      label: 'analyze-dependency',
      phase: '依赖分析',
      schema: {
        type: 'object',
        properties: {
          modules: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                moduleId: { type: 'string' },
                moduleName: { type: 'string' },
                moduleCode: { type: 'string' },
                isCore: { type: 'boolean' },
                dependencies: {
                  type: 'array',
                  items: { type: 'string' },
                },
                features: {
                  type: 'array',
                  items: {
                    type: 'object',
                    properties: {
                      featureId: { type: 'string' },
                      featureName: { type: 'string' },
                      priority: { type: 'string' },
                    },
                  },
                },
              },
            },
          },
          dependencyGraph: { type: 'string' },
          independentModules: {
            type: 'array',
            items: { type: 'string' },
          },
          coreModules: {
            type: 'array',
            items: { type: 'string' },
          },
        },
        required: ['modules', 'dependencyGraph'],
      },
    }
  );

  log(
    `依赖分析完成，识别 ${dependencyAnalysis.modules?.length || 0} 个模块，${dependencyAnalysis.coreModules?.length || 0} 个核心模块`
  );

  // Phase 2: 优先级排序
  phase('优先级排序');

  const priorityRanking = await agent(
    `基于依赖关系和业务价值进行优先级排序：

    模块信息：${JSON.stringify(dependencyAnalysis.modules, null, 2)}

    依赖图：${dependencyAnalysis.dependencyGraph}

    核心模块：${dependencyAnalysis.coreModules?.join(', ')}

    排序原则：
    1. 核心基础模块优先开发
    2. 被依赖模块优先于依赖模块
    3. Must-Have功能优先于Should-Have
    4. 可并行开发的模块同时开始

    请输出排序结果和并行开发建议`,
    {
      label: 'priority-ranking',
      phase: '优先级排序',
      schema: {
        type: 'object',
        properties: {
          developmentOrder: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                order: { type: 'number' },
                moduleId: { type: 'string' },
                moduleName: { type: 'string' },
                priorityLevel: { type: 'string' },
                reason: { type: 'string' },
                parallelGroup: { type: 'number' },
              },
            },
          },
          parallelGroups: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                groupNumber: { type: 'number' },
                modules: { type: 'array', items: { type: 'string' } },
                estimatedDuration: { type: 'string' },
              },
            },
          },
        },
        required: ['developmentOrder', 'parallelGroups'],
      },
    }
  );

  log(
    `优先级排序完成，共 ${priorityRanking.parallelGroups?.length || 0} 个并行组`
  );

  // Phase 3: 工期估算
  phase('工期估算');

  const durationEstimation = await agent(
    `估算各模块开发工期：

    开发顺序：${JSON.stringify(priorityRanking.developmentOrder, null, 2)}

    团队人数：${team_size}

    估算依据：
    1. 功能点数量
    2. 功能复杂度（简单/中等/复杂）
    3. 技术难度
    4. 依赖关系复杂度

    工期标准参考：
    - 简单功能：1-2人日
    - 中等功能：3-5人日
    - 复杂功能：5-10人日

    请输出各模块工期估算`,
    {
      label: 'estimate-duration',
      phase: '工期估算',
      schema: {
        type: 'object',
        properties: {
          moduleEstimations: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                moduleId: { type: 'string' },
                moduleName: { type: 'string' },
                featureCount: { type: 'number' },
                simpleFeatures: { type: 'number' },
                mediumFeatures: { type: 'number' },
                complexFeatures: { type: 'number' },
                estimatedDays: { type: 'number' },
                estimatedTeamDays: { type: 'number' },
                riskBuffer: { type: 'number' },
              },
            },
          },
          totalEstimatedDays: { type: 'number' },
          criticalPath: {
            type: 'array',
            items: { type: 'string' },
          },
        },
        required: ['moduleEstimations', 'totalEstimatedDays'],
      },
    }
  );

  log(
    `工期估算完成，总工期 ${durationEstimation.totalEstimatedDays} 人日`
  );

  // Phase 4: 排期生成
  phase('排期生成');

  const schedulePlan = await agent(
    `生成完整排期计划：

    项目：${project_name}
    开始日期：${start_date}
    团队人数：${team_size}

    模块估算：${JSON.stringify(durationEstimation.moduleEstimations, null, 2)}

    开发顺序：${JSON.stringify(priorityRanking.developmentOrder, null, 2)}

    并行组：${JSON.stringify(priorityRanking.parallelGroups, null, 2)}

    关键路径：${durationEstimation.criticalPath?.join(' → ')}

    请生成：
    1. 详细排期甘特图描述
    2. 各阶段里程碑
    3. 资源分配建议
    4. 风险缓冲安排
    5. 交付节点定义`,
    {
      label: 'generate-schedule',
      phase: '排期生成',
      schema: {
        type: 'object',
        properties: {
          milestones: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                milestoneId: { type: 'string' },
                milestoneName: { type: 'string' },
                targetDate: { type: 'string' },
                deliverables: { type: 'array', items: { type: 'string' } },
              },
            },
          },
          scheduleDetails: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                moduleId: { type: 'string' },
                moduleName: { type: 'string' },
                startDate: { type: 'string' },
                endDate: { type: 'string' },
                duration: { type: 'number' },
                assignees: { type: 'array', items: { type: 'string' } },
                dependencies: { type: 'array', items: { type: 'string' } },
                status: { type: 'string' },
              },
            },
          },
          resourceAllocation: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                role: { type: 'string' },
                count: { type: 'number' },
                modules: { type: 'array', items: { type: 'string' } },
              },
            },
          },
          totalDuration: { type: 'number' },
          estimatedEndDate: { type: 'string' },
        },
        required: ['milestones', 'scheduleDetails', 'totalDuration'],
      },
    }
  );

  log(
    `排期生成完成，预计工期 ${schedulePlan.totalDuration} 天，结束日期 ${schedulePlan.estimatedEndDate}`
  );

  return {
    projectName: project_name,
    outputDir: output_dir,
    dependencyAnalysis: dependencyAnalysis,
    priorityRanking: priorityRanking,
    durationEstimation: durationEstimation,
    schedulePlan: schedulePlan,
  };
}