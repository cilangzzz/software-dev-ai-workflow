/**
 * 系统设计阶段工作流
 *
 * 功能描述：
 * - 结合需求文档和网络资料
 * - 生成系统需求文档
 * - 包含访问人数、数据增量等系统指标
 *
 * 输入参数：
 * - project_name: 项目名称
 * - requirement_docs_dir: 需求文档目录（绝对路径）
 * - output_dir: 输出目录（绝对路径）
 * - existing_framework: 已有框架描述（可选）
 */

export const meta = {
  name: 'stage-04-system-design',
  description: '系统设计阶段：生成系统需求、性能指标、容量规划文档',
  phases: [
    { title: '需求分析', detail: '分析需求文档提取系统约束' },
    { title: '资料调研', detail: '搜索系统设计最佳实践' },
    { title: '指标估算', detail: '估算访问量、数据量等指标' },
    { title: '文档生成', detail: '生成系统需求文档' },
  ],
};

export default async function (args) {
  const {
    project_name,
    requirement_docs_dir,
    output_dir = 'F:\\sandbox\\workflow\\2.0-用例\\项目管理样例\\02-开发库\\03-系统设计',
    existing_framework,
  } = args;

  // Phase 1: 需求分析
  phase('需求分析');

  const requirementAnalysis = await agent(
    `分析需求文档，提取系统设计约束：

    目录路径：${requirement_docs_dir}

    请提取：
    1. 用户规模预估
    2. 业务量预估
    3. 性能要求
    4. 安全要求
    5. 可用性要求
    6. 兼容性要求`,
    {
      label: 'analyze-requirements',
      phase: '需求分析',
      schema: {
        type: 'object',
        properties: {
          userScale: {
            type: 'object',
            properties: {
              estimated: { type: 'string' },
              peakConcurrency: { type: 'string' },
              growthRate: { type: 'string' },
            },
          },
          businessVolume: {
            type: 'object',
            properties: {
              dailyTransactions: { type: 'string' },
              monthlyData: { type: 'string' },
              yearlyGrowth: { type: 'string' },
            },
          },
          performanceRequirements: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                metric: { type: 'string' },
                requirement: { type: 'string' },
              },
            },
          },
          securityRequirements: {
            type: 'array',
            items: { type: 'string' },
          },
          availabilityRequirement: { type: 'string' },
          compatibilityRequirements: {
            type: 'array',
            items: { type: 'string' },
          },
        },
        required: ['userScale', 'businessVolume'],
      },
    }
  );

  log('需求分析完成');

  // Phase 2: 资料调研（搜索真实资料）
  phase('资料调研');

  const researchResults = await parallel([
    () =>
      agent(
        `搜索系统设计最佳实践资料：

        搜索关键词：
        1. "${project_name} 系统架构 最佳实践"
        2. "高并发系统设计 性能优化"
        3. "分布式系统 容量规划"

        请使用WebSearch获取真实资料，禁止Mock数据`,
        {
          label: 'research-architecture',
          phase: '资料调研',
          schema: {
            type: 'object',
            properties: {
              findings: {
                type: 'array',
                items: {
                  type: 'object',
                  properties: {
                    topic: { type: 'string' },
                    source: { type: 'string' },
                    keyPoints: { type: 'array', items: { type: 'string' } },
                  },
                },
              },
            },
            required: ['findings'],
          },
        }
      ),
    () =>
      agent(
        `搜索性能指标参考资料：

        搜索关键词：
        1. "系统性能指标 SLA标准"
        2. "数据库容量规划 方法"
        3. "缓存策略 性能优化"

        请使用WebSearch获取真实资料`,
        {
          label: 'research-performance',
          phase: '资料调研',
          schema: {
            type: 'object',
            properties: {
              findings: {
                type: 'array',
                items: {
                  type: 'object',
                  properties: {
                    topic: { type: 'string' },
                    recommendations: { type: 'array', items: { type: 'string' } },
                  },
                },
              },
            },
            required: ['findings'],
          },
        }
      ),
  ]);

  const allResearch = researchResults.filter(Boolean);
  log(`资料调研完成，获取 ${allResearch.length} 组资料`);

  // Phase 3: 指标估算
  phase('指标估算');

  const capacityPlanning = await agent(
    `根据需求分析和参考资料进行容量规划：

    用户规模：${JSON.stringify(requirementAnalysis.userScale, null, 2)}

    业务量：${JSON.stringify(requirementAnalysis.businessVolume, null, 2)}

    性能要求：${JSON.stringify(requirementAnalysis.performanceRequirements, null, 2)}

    已有框架：${existing_framework || '待确定'}

    参考资料：${JSON.stringify(allResearch, null, 2)}

    请估算：
    1. 系统访问量（日活、峰值QPS）
    2. 数据增量（日增量、年增量）
    3. 存储需求
    4. 带宽需求
    5. 服务器配置建议
    6. 数据库配置建议
    7. 缓存配置建议`,
    {
      label: 'capacity-planning',
      phase: '指标估算',
      schema: {
        type: 'object',
        properties: {
          accessMetrics: {
            type: 'object',
            properties: {
              dau: { type: 'string' },
              mau: { type: 'string' },
              peakQps: { type: 'string' },
              avgResponseTime: { type: 'string' },
            },
          },
          dataMetrics: {
            type: 'object',
            properties: {
              dailyIncrement: { type: 'string' },
              yearlyIncrement: { type: 'string' },
              totalEstimate: { type: 'string' },
              retentionPeriod: { type: 'string' },
            },
          },
          storageRequirements: {
            type: 'object',
            properties: {
              database: { type: 'string' },
              fileStorage: { type: 'string' },
              cache: { type: 'string' },
              backup: { type: 'string' },
            },
          },
          serverConfiguration: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                serverType: { type: 'string' },
                specification: { type: 'string' },
                quantity: { type: 'number' },
                purpose: { type: 'string' },
              },
            },
          },
          databaseConfiguration: {
            type: 'object',
            properties: {
              primary: { type: 'string' },
              replica: { type: 'string' },
              cache: { type: 'string' },
            },
          },
        },
        required: ['accessMetrics', 'dataMetrics', 'storageRequirements'],
      },
    }
  );

  log('容量规划完成');

  // Phase 4: 文档生成
  phase('文档生成');

  const systemDesignDoc = await agent(
    `生成系统设计文档：

    项目：${project_name}

    需求分析：${JSON.stringify(requirementAnalysis, null, 2)}

    容量规划：${JSON.stringify(capacityPlanning, null, 2)}

    参考资料：${JSON.stringify(allResearch, null, 2)}

    请生成完整的系统设计文档，包含：
    1. 系统概述
    2. 系统需求
    3. 性能指标
    4. 容量规划
    5. 技术选型建议
    6. 部署架构建议
    7. 监控告警建议`,
    {
      label: 'generate-doc',
      phase: '文档生成',
      schema: {
        type: 'object',
        properties: {
          documentContent: { type: 'string' },
          sections: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                sectionTitle: { type: 'string' },
                content: { type: 'string' },
              },
            },
          },
        },
        required: ['documentContent'],
      },
    }
  );

  log('系统设计文档生成完成');

  return {
    projectName: project_name,
    outputDir: output_dir,
    requirementAnalysis: requirementAnalysis,
    researchResults: allResearch,
    capacityPlanning: capacityPlanning,
    systemDesignDoc: systemDesignDoc,
  };
}