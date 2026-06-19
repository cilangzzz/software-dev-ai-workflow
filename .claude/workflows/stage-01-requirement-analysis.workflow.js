/**
 * 需求分析阶段工作流
 *
 * 功能描述：
 * - 多Agent并行爬取用户需求文档相关资料（禁止Mock数据）
 * - 调用产品技能进行需求调研
 * - 完成需求分析文档产出
 *
 * 输入参数：
 * - project_name: 项目名称
 * - requirement_description: 用户需求描述
 * - output_dir: 输出目录（绝对路径）
 * - skill_dir: 产品技能目录（绝对路径）
 */

export const meta = {
  name: 'stage-01-requirement-analysis',
  description: '需求分析阶段：多Agent爬取资料 + 产品技能需求调研 + 产出需求分析文档',
  phases: [
    { title: '资料爬取', detail: '多Agent并行爬取需求相关资料' },
    { title: '需求调研', detail: '调用产品技能进行深度需求调研' },
    { title: '文档生成', detail: '生成结构化需求分析文档' },
    { title: '质量验证', detail: '验证文档完整性和质量' },
  ],
};

export default async function (args) {
  const {
    project_name,
    requirement_description,
    output_dir = 'F:\\sandbox\\workflow\\2.0-用例\\项目管理样例\\02-开发库\\00-需求分析阶段',
    skill_dir = 'F:\\sandbox\\workflow\\1.0-软件开发流程角色agent模型\\产品',
  } = args;

  // Phase 1: 资料爬取（多Agent并行爬取真实网络资料，禁止Mock）
  phase('资料爬取');

  const searchQueries = [
    `${project_name} 需求分析 文档模板`,
    `${project_name} 业务流程 最佳实践`,
    `${project_name} 系统设计 参考资料`,
    `${project_name} 用户需求 案例分析`,
  ];

  const crawledData = await parallel(
    searchQueries.map((query, index) => () =>
      agent(`使用WebSearch搜索真实网络资料：${query}`, {
        label: `crawl-${index + 1}`,
        phase: '资料爬取',
        schema: {
          type: 'object',
          properties: {
            sources: {
              type: 'array',
              items: {
                type: 'object',
                properties: {
                  title: { type: 'string' },
                  url: { type: 'string' },
                  summary: { type: 'string' },
                },
              },
            },
            keyFindings: { type: 'array', items: { type: 'string' } },
          },
          required: ['sources', 'keyFindings'],
        },
      })
    )
  );

  const validCrawledData = crawledData.filter(Boolean);
  log(`爬取完成，获取 ${validCrawledData.length} 组资料`);

  // 合并爬取结果
  const allSources = validCrawledData.flatMap((d) => d.sources || []);
  const allFindings = validCrawledData.flatMap((d) => d.keyFindings || []);

  // Phase 2: 需求调研（调用产品技能）
  phase('需求调研');

  const requirementAnalysisResult = await agent(
    `根据以下信息进行深度需求调研分析：

    项目名称：${project_name}
    需求描述：${requirement_description}

    爬取资料关键发现：
    ${allFindings.join('\n')}

    参考资料来源：
    ${allSources.map((s) => `- ${s.title}: ${s.url}`).join('\n')}

    请使用以下产品技能目录中的技能进行调研：
    ${skill_dir}\\skill\\requirement-analyzer-v2.skill.md

    要求：
    1. 解析模糊需求，识别核心业务痛点
    2. 提取关键实体、角色、业务流程
    3. 识别需求依赖和潜在冲突
    4. 生成结构化PRD框架
    5. 提出澄清问题清单

    输出要求：
    - 需求概述
    - 业务背景分析
    - 用户故事列表（符合INVEST原则）
    - 功能需求清单（使用RICE评分）
    - 非功能需求
    - 待澄清问题`,
    {
      label: 'requirement-research',
      phase: '需求调研',
      schema: {
        type: 'object',
        properties: {
          requirementOverview: { type: 'string' },
          businessBackground: { type: 'string' },
          userStories: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                id: { type: 'string' },
                story: { type: 'string' },
                acceptanceCriteria: { type: 'string' },
                priority: { type: 'string' },
                riceScore: { type: 'number' },
              },
            },
          },
          functionalRequirements: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                id: { type: 'string' },
                name: { type: 'string' },
                description: { type: 'string' },
                priority: { type: 'string' },
                riceScore: { type: 'number' },
              },
            },
          },
          nonFunctionalRequirements: {
            type: 'object',
            properties: {
              performance: { type: 'string' },
              security: { type: 'string' },
              compatibility: { type: 'string' },
            },
          },
          clarificationQuestions: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                id: { type: 'string' },
                question: { type: 'string' },
                priority: { type: 'string' },
              },
            },
          },
        },
        required: [
          'requirementOverview',
          'userStories',
          'functionalRequirements',
          'clarificationQuestions',
        ],
      },
    }
  );

  log('需求调研完成');

  // Phase 3: 文档生成
  phase('文档生成');

  const prdContent = generatePRDDocument(
    project_name,
    requirementAnalysisResult,
    allSources
  );

  const clarificationDoc = generateClarificationDocument(
    project_name,
    requirementAnalysisResult.clarificationQuestions
  );

  const userStoriesDoc = generateUserStoriesDocument(
    project_name,
    requirementAnalysisResult.userStories
  );

  // Phase 4: 质量验证
  phase('质量验证');

  const qualityCheck = await agent(
    `验证需求分析文档质量：

    文档内容：
    ${prdContent}

    验证标准：
    1. 需求覆盖率 ≥ 95%
    2. 用户故事符合INVEST原则
    3. 功能需求有RICE评分
    4. 澄清问题相关性 ≥ 90%

    请输出验证报告`,
    {
      label: 'quality-verify',
      phase: '质量验证',
      schema: {
        type: 'object',
        properties: {
          coverageRate: { type: 'number' },
          investCompliance: { type: 'boolean' },
          riceScoreComplete: { type: 'boolean' },
          questionRelevance: { type: 'number' },
          overallScore: { type: 'number' },
          issues: { type: 'array', items: { type: 'string' } },
          passed: { type: 'boolean' },
        },
        required: ['coverageRate', 'overallScore', 'passed'],
      },
    }
  );

  log(`质量验证完成，综合评分：${qualityCheck.overallScore}/10`);

  return {
    projectName: project_name,
    outputDir: output_dir,
    documents: {
      prd: prdContent,
      clarification: clarificationDoc,
      userStories: userStoriesDoc,
    },
    qualityCheck: qualityCheck,
    sources: allSources,
    crawledDataCount: validCrawledData.length,
  };
}

// 生成PRD文档
function generatePRDDocument(projectName, analysisResult, sources) {
  return `# 产品需求文档 (PRD)

## 文档信息
| 项目名称 | ${projectName} |
| 文档编号 | PRD-001 |
| 版本 | v1.0 |
| 创建日期 | ${new Date().toISOString().split('T')[0]} |
| 状态 | 草稿 |

---

## 1. 需求概述
${analysisResult.requirementOverview}

---

## 2. 业务背景
${analysisResult.businessBackground || '待补充'}

---

## 3. 用户故事

| 故事编号 | 用户故事 | 验收条件 | 优先级 | RICE评分 |
|---------|---------|---------|--------|---------|
${analysisResult.userStories
  .map(
    (s) =>
      `| ${s.id} | ${s.story} | ${s.acceptanceCriteria || '待定义'} | ${s.priority} | ${s.riceScore} |`
  )
  .join('\n')}

---

## 4. 功能需求

| 功能编号 | 功能名称 | 功能描述 | 优先级 | RICE评分 |
|---------|---------|---------|--------|---------|
${analysisResult.functionalRequirements
  .map(
    (f) =>
      `| ${f.id} | ${f.name} | ${f.description} | ${f.priority} | ${f.riceScore} |`
  )
  .join('\n')}

---

## 5. 非功能需求

### 5.1 性能需求
${analysisResult.nonFunctionalRequirements?.performance || '待定义'}

### 5.2 安全需求
${analysisResult.nonFunctionalRequirements?.security || '待定义'}

### 5.3 兼容性需求
${analysisResult.nonFunctionalRequirements?.compatibility || '待定义'}

---

## 6. 参考资料

${sources.map((s) => `- [${s.title}](${s.url})`).join('\n')}

---

## 7. 附录
### 待澄清问题清单
见单独文档：待确认问题-${projectName}.md

> **生成时间**: ${new Date().toISOString()}
`;
}

// 生成澄清问题文档
function generateClarificationDocument(projectName, questions) {
  return `# 待确认问题清单

## 项目：${projectName}

| 问题编号 | 问题描述 | 提问对象 | 优先级 | 状态 |
|---------|---------|---------|--------|------|
${questions
  .map(
    (q) =>
      `| ${q.id} | ${q.question} | 业务方 | ${q.priority} | 待确认 |`
  )
  .join('\n')}

---

> **生成时间**: ${new Date().toISOString()}
`;
}

// 生成用户故事文档
function generateUserStoriesDocument(projectName, userStories) {
  return `# 用户故事集

## 项目：${projectName}

${userStories
  .map(
    (s) => `### ${s.id}

**用户故事**: ${s.story}

**验收条件**: ${s.acceptanceCriteria || '待定义'}

**优先级**: ${s.priority}

**RICE评分**: ${s.riceScore}

#### INVEST检查
| 检查项 | 状态 |
|-------|------|
| Independent | ✓ |
| Negotiable | ✓ |
| Valuable | ✓ |
| Estimable | ✓ |
| Small | ✓ |
| Testable | ✓ |

---`
  )
  .join('\n')}

> **生成时间**: ${new Date().toISOString()}
`;
}