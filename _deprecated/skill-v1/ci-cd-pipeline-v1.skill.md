# CI/CD流水线设计专家

## 基本信息

- **ID**: ci-cd-pipeline-v2
- **名称**: CI/CD流水线设计专家
- **版本**: 2.0.0
- **分类**: operations
- **部门**: 运维部
- **描述**: 专业CI/CD流水线设计工具，基于DevOps和GitOps理念，支持多种CI工具（Jenkins/GitLab CI/GitHub Actions/ArgoCD），实现自动化构建、测试、部署。遵循12-Factor App原则。


## 触发条件


### commands

- /ci-cd-pipeline
- /流水线
- /cicd

### keywords

- CI/CD配置
- 流水线设计
- 自动化部署
- 构建配置
- 部署流水线

### patterns

- 帮我配置.*流水线
- 设计.*CI/CD
- 自动化.*部署

## 输入参数


### parameters


- **name**: project_info
- **type**: object
- **required**: True
- **description**: 项目基本信息
- **properties**: - **name**: 项目名称
- **tech_stack**: 技术栈（java/node/vue/python/go）
- **repo_url**: 代码仓库地址
- **branch_strategy**: 分支策略（gitflow/trunk-based）

- **name**: ci_tool
- **type**: string
- **required**: False
- **default**: auto
- **enum**: - auto
- jenkins
- gitlab-ci
- github-actions
- azure-pipelines
- all
- **description**: CI工具选择

- **name**: deployment_strategy
- **type**: string
- **required**: False
- **default**: rolling
- **enum**: - rolling
- blue-green
- canary
- recreate
- **description**: 部署策略选择

- **name**: environments
- **type**: array
- **required**: False
- **default**: - dev
- staging
- prod
- **description**: 需要配置的环境列表

- **name**: quality_gates
- **type**: object
- **required**: False
- **default**: 
- **description**: 质量门禁配置
- **properties**: - **unit_test_coverage**: 单元测试覆盖率阈值
- **code_quality_score**: 代码质量评分阈值
- **security_scan**: 是否启用安全扫描

## 工作流程

- **description**: CI/CD流水线设计流程，确保自动化部署安全可控

### phases


- **name**: 项目分析
- **description**: 分析项目结构和技术栈
- **duration**: 5-10分钟
- **steps**: 
- **step**: 项目结构解析
- **action**: 读取项目配置文件，识别构建方式
- **output**: 项目结构报告

- **step**: 技术栈识别
- **action**: 识别语言、框架、依赖管理工具
- **output**: 技术栈清单

- **step**: 分支策略分析
- **action**: 分析Git分支策略
- **reference**: Git Workflow最佳实践
- **output**: 分支策略建议

- **step**: 现有CI配置检查
- **action**: 检查现有CI配置文件
- **output**: 现有CI状态

- **name**: 流水线设计
- **description**: 设计完整的CI/CD流水线
- **duration**: 20-40分钟
- **steps**: 
- **step**: 构建阶段设计
- **action**: 设计编译/打包流程
- **checklist**: 构建阶段检查清单
- **output**: 构建配置

- **step**: 测试阶段设计
- **action**: 设计自动化测试流程
- **checklist**: 测试阶段检查清单
- **output**: 测试配置

- **step**: 质量门禁设计
- **action**: 设计质量检查和门禁
- **checklist**: 质量门禁检查清单
- **output**: 质量门禁配置

- **step**: 安全扫描设计
- **action**: 设计安全扫描流程
- **checklist**: 安全扫描检查清单
- **output**: 安全扫描配置

- **step**: 部署阶段设计
- **action**: 设计部署策略和流程
- **checklist**: 部署阶段检查清单
- **output**: 部署配置

- **step**: 回滚机制设计
- **action**: 设计回滚策略和触发条件
- **output**: 回滚配置

- **name**: 配置生成
- **description**: 生成CI/CD配置文件
- **duration**: 15-30分钟
- **steps**: 
- **step**: CI配置生成
- **action**: 生成CI工具配置文件
- **template**: ci-config-template
- **output**: CI配置文件

- **step**: 部署配置生成
- **action**: 生成部署工具配置
- **template**: deploy-config-template
- **output**: 部署配置文件

- **step**: 环境配置生成
- **action**: 生成环境差异化配置
- **output**: 环境配置文件集

- **step**: 通知配置生成
- **action**: 生成通知和告警配置
- **output**: 通知配置

- **name**: 文档编写
- **description**: 编写CI/CD文档和操作指南
- **duration**: 10-20分钟
- **steps**: 
- **step**: 流水线文档生成
- **action**: 生成流水线说明文档
- **template**: pipeline-doc-template
- **output**: 流水线文档

- **step**: 操作手册生成
- **action**: 生成操作手册
- **output**: 操作手册

- **step**: 故障排查指南生成
- **action**: 生成常见问题排查指南
- **output**: 故障排查指南

## 输出产物

- **base_path**: 运维/产出物/{project_name}/部署阶段/

### artifacts


- **name**: CI配置文件
- **files**: - ci/Jenkinsfile
- ci/.gitlab-ci.yml
- ci/.github/workflows/build.yml
- **format**: yaml/groovy
- **description**: CI工具配置文件
- **required**: True

- **name**: 部署配置文件
- **files**: - deploy/kubernetes/base/
- deploy/kubernetes/overlays/
- deploy/helm/
- **format**: yaml
- **description**: 部署工具配置文件
- **required**: True

- **name**: 流水线文档
- **files**: - CI-CD流水线文档-{project}.md
- **format**: markdown
- **description**: 流水线说明文档
- **required**: True

- **name**: 操作手册
- **files**: - CI-CD操作手册-{project}.md
- **format**: markdown
- **description**: 日常操作手册
- **required**: True

## templates

- **jenkinsfile_template**: 
```
// ============================================
// Jenkinsfile - {project_name}
// 版本: {version}
// 更新日期: {date}
// ============================================

pipeline {
    agent any

    environment {
        // 项目配置
        PROJECT_NAME = '{project_name}'
        DOCKER_REGISTRY = '{registry_url}'
        DOCKER_IMAGE = "${DOCKER_REGISTRY}/${PROJECT_NAME}"

        // 版本管理
        VERSION = "${env.BUILD_NUMBER}"
        GIT_COMMIT_SHORT = "${env.GIT_COMMIT.substring(0, 8)}"

        // 环境配置
        DEV_NAMESPACE = 'dev-{project_name}'
        STAGING_NAMESPACE = 'staging-{project_name}'
        PROD_NAMESPACE = 'prod-{project_name}'
    }

    options {
        // 构建选项
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 30, unit: 'MINUTES')
        disableConcurrentBuilds()

        // Git配置
        gitLabConnection('gitlab-connection')
    }

    stages {
        // ============================================
        // 阶段1: 代码检出
        // ============================================
        stage('Checkout') {
            steps {
                script {
                    echo "🔍 检出代码: ${env.GIT_BRANCH}"
                    checkout scm

                    // 记录Git信息
                    env.GIT_COMMIT = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()
                    env.GIT_COMMIT_SHORT = env.GIT_COMMIT.substring(0, 8)
                    env.GIT_AUTHOR = sh(script: 'git log -1 --pretty=format:"%an"', returnStdout: true).trim()
                }
            }
        }

        // ============================================
        // 阶段2: 代码质量检查
        // ============================================
        stage('Code Quality') {
            parallel {
                stage('Lint') {
                    steps {
                        script {
                            echo "📝 代码风格检查"
                            // {language_specific_lint_command}
                        }
                    }
                }
                stage('SonarQube') {
                    steps {
                        script {
                            echo "📊 SonarQube代码质量分析"
                            withSonarQubeEnv('sonar-server') {
                                sh './gradlew sonarqube -Dsonar.projectKey=${PROJECT_NAME} -Dsonar.branch.name=${env.GIT_BRANCH}'
                            }
                        }
                    }
                }
            }
        }

        // ============================================
        // 阶段3: 单元测试
        // ============================================
        stage('Unit Test') {
            steps {
                script {
                    echo "🧪 执行单元测试"
                    // {language_specific_test_command}
                    sh './gradlew test'
                }
            }
            post {
                always {
                    // 发布测试报告
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'build/reports/tests/test',
                        reportFiles: 'index.html',
                        reportName: 'Unit Test Report'
                    ])

                    // 测试覆盖率检查
                    jacoco execPattern: 'build/jacoco/*.exec', classPattern: 'build/classes', sourcePattern: 'src'
                }
            }
        }

        // ============================================
        // 阶段4: 安全扫描
        // ============================================
        stage('Security Scan') {
            parallel {
                stage('Dependency Check') {
                    steps {
                        script {
                            echo "🔒 依赖安全检查"
                            dependencyCheckAdditionalArguments: '''
                                --scan build/libs
                                --format HTML
                                --format JSON
                            '''
                            dependencyCheckPublisher pattern: '**/dependency-check-report.html'
                        }
                    }
                }
                stage('SAST') {
                    steps {
                        script {
                            echo "🔍 静态应用安全测试"
                            // 使用SonarQube或Checkmarx
                        }
                    }
                }
            }
        }

        // ============================================
        // 阶段5: 构建应用
        // ============================================
        stage('Build') {
            steps {
                script {
                    echo "🔨 构建应用"
                    // {language_specific_build_command}
                    sh './gradlew build -x test'

                    // 构建产物验证
                    def artifacts = sh(script: 'ls -la build/libs/*.jar', returnStdout: true).trim()
                    echo "构建产物: ${artifacts}"
                }
            }
        }

        // ============================================
        // 阶段6: Docker镜像构建
        // ============================================
        stage('Docker Build') {
            steps {
                script {
                    echo "🐳 构建Docker镜像"

                    // 镜像标签策略
                    def imageTags = [
                        "${VERSION}",
                        "${GIT_COMMIT_SHORT}",
                        "latest"
                    ]

                    // 多阶段构建
                    sh "docker build -f docker/Dockerfile -t ${DOCKER_IMAGE}:${VERSION} -t ${DOCKER_IMAGE}:${GIT_COMMIT_SHORT} ."

                    // 镜像安全扫描
                    sh "docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image ${DOCKER_IMAGE}:${VERSION}"
                }
            }
        }

        // ============================================
        // 阶段7: 推送镜像
        // ============================================
        stage('Docker Push') {
            steps {
                script {
                    echo "📤 推送镜像到仓库"

                    withCredentials([usernamePassword(
                        credentialsId: 'docker-registry-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASS} ${DOCKER_REGISTRY}"
                        sh "docker push ${DOCKER_IMAGE}:${VERSION}"
                        sh "docker push ${DOCKER_IMAGE}:${GIT_COMMIT_SHORT}"
                    }
                }
            }
        }

        // ============================================
        // 阶段8: 部署到开发环境
        // ============================================
        stage('Deploy Dev') {
            when {
                anyOf {
                    branch 'develop'
                    branch 'feature/*'
                }
            }
            steps {
                script {
                    echo "🚀 部署到开发环境"
                    deployToEnvironment('dev', env.VERSION)
                }
            }
        }

        // ============================================
        // 阶段9: 部署到测试环境
        // ============================================
        stage('Deploy Staging') {
            when {
                branch 'develop'
            }
            steps {
                script {
                    echo "🧪 部署到测试环境"
                    deployToEnvironment('staging', env.VERSION)
                }
            }

            post {
                success {
                    // 自动化测试
                    echo "执行自动化测试"
                    // triggerAutomatedTests('staging')
                }
            }
        }

        // ============================================
        // 阶段10: 部署到生产环境（需审批）
        // ============================================
        stage('Deploy Prod') {
            when {
                branch 'main'
            }
            steps {
                script {
                    echo "🚀 部署到生产环境（需要审批）"
                }
            }

            // 部署审批
            input {
                message "确认部署到生产环境？"
                ok "确认部署"
                submitter "release-team,ops-team"
                submitterParameter "APPROVER"
            }

            steps {
                script {
                    echo "审批人: ${env.APPROVER}"
                    deployToEnvironment('prod', env.VERSION)
                }
            }
        }
    }

    // ============================================
    // 部署函数
    // ============================================
    def deployToEnvironment(envName, version) {
        def namespace = env."${envName.toUpperCase()}_NAMESPACE"

        // 使用Helm部署
        sh """
            helm upgrade --install ${PROJECT_NAME} \
                deploy/helm/${PROJECT_NAME} \
                --namespace ${namespace} \
                --set image.tag=${version} \
                --set environment=${envName} \
                --values deploy/helm/${PROJECT_NAME}/values-${envName}.yaml \
                --atomic \
                --timeout 5m
        """

        // 部署验证
        sh """
            kubectl rollout status deployment/${PROJECT_NAME} \
                -n ${namespace} \
                --timeout 3m
        """

        // 健康检查
        sh """
            kubectl wait --for=condition=ready pod -l app=${PROJECT_NAME} \
                -n ${namespace} \
                --timeout 2m
        """
    }

    // ============================================
    // 后置处理
    // ============================================
    post {
        always {
            // 清理工作空间
            cleanWs()
        }

        success {
            // 成功通知
            slackSend(
                color: 'good',
                message: """
                ✅ 构建成功
                - 项目: ${PROJECT_NAME}
                - 版本: ${VERSION}
                - 分支: ${env.GIT_BRANCH}
                - 提交: ${GIT_COMMIT_SHORT} by ${GIT_AUTHOR}
                - 链接: ${env.BUILD_URL}
                """
            )
        }

        failure {
            // 失败通知
            slackSend(
                color: 'danger',
                message: """
                ❌ 构建失败
                - 项目: ${PROJECT_NAME}
                - 分支: ${env.GIT_BRANCH}
                - 链接: ${env.BUILD_URL}
                请及时检查并修复！
                """
            )

            // 自动回滚（生产环境）
            if (env.GIT_BRANCH == 'main') {
                script {
                    echo "⚠️ 触发自动回滚"
                    rollback('prod')
                }
            }
        }

        unstable {
            // 不稳定通知
            slackSend(
                color: 'warning',
                message: """
                ⚠️ 构建不稳定
                - 项目: ${PROJECT_NAME}
                - 原因: 测试失败或质量门禁未通过
                """
            )
        }
    }
}

```

- **github_actions_template**: 
```
# ============================================
# GitHub Actions Workflow - {project_name}
# 版本: {version}
# 更新日期: {date}
# ============================================

name: CI/CD Pipeline

on:
  push:
    branches:
      - main
      - develop
      - 'feature/**'
  pull_request:
    branches:
      - main
      - develop
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deployment environment'
        required: true
        default: 'staging'
        type: choice
        options:
          - dev
          - staging
          - prod

env:
  PROJECT_NAME: {project_name}
  DOCKER_REGISTRY: {registry_url}
  DOCKER_IMAGE: ${{ env.DOCKER_REGISTRY }}/${{ env.PROJECT_NAME }}

jobs:
  # ============================================
  # Job 1: 代码质量检查
  # ============================================
  code-quality:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup {language}
        uses: actions/setup-{language}@v4
        with:
          {language}-version: '{version}'

      - name: Lint
        run: |
          echo "📝 代码风格检查"
          {lint_command}

      - name: SonarQube Scan
        uses: sonarsource/sonarqube-scan-action@master
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}

  # ============================================
  # Job 2: 单元测试
  # ============================================
  unit-test:
    runs-on: ubuntu-latest
    needs: code-quality
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup {language}
        uses: actions/setup-{language}@v4
        with:
          {language}-version: '{version}'

      - name: Run Tests
        run: |
          echo "🧪 执行单元测试"
          {test_command}

      - name: Upload Coverage
        uses: codecov/codecov-action@v4
        with:
          files: ./coverage.xml
          fail_ci_if_error: true

      - name: Test Coverage Gate
        run: |
          coverage=$(cat coverage.txt)
          if [ $coverage -lt {coverage_threshold} ]; then
            echo "❌ 测试覆盖率不达标: ${coverage}% < {coverage_threshold}%"
            exit 1
          fi

  # ============================================
  # Job 3: 安全扫描
  # ============================================
  security-scan:
    runs-on: ubuntu-latest
    needs: unit-test
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Dependency Check
        uses: dependency-check/Dependency-Check_Action@main
        with:
          project: ${{ env.PROJECT_NAME }}
          path: '.'
          format: 'HTML'
          out: 'reports'
        env:
          NVD_API_KEY: ${{ secrets.NVD_API_KEY }}

      - name: Upload Security Report
        uses: actions/upload-artifact@v4
        with:
          name: security-report
          path: reports/

      - name: Trivy Scan
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          format: 'table'
          exit-code: '1'
          severity: 'CRITICAL,HIGH'

  # ============================================
  # Job 4: 构建
  # ============================================
  build:
    runs-on: ubuntu-latest
    needs: [unit-test, security-scan]
    outputs:
      version: ${{ steps.version.outputs.version }}
      commit_short: ${{ steps.version.outputs.commit_short }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Generate Version
        id: version
        run: |
          echo "version=${{ github.run_number }}" >> $GITHUB_OUTPUT
          echo "commit_short=${{ github.sha }}" | cut -c1-8 >> $GITHUB_OUTPUT

      - name: Build Application
        run: |
          echo "🔨 构建应用"
          {build_command}

      - name: Upload Artifact
        uses: actions/upload-artifact@v4
        with:
          name: build-artifact
          path: {artifact_path}

  # ============================================
  # Job 5: Docker构建和推送
  # ============================================
  docker:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Download Artifact
        uses: actions/download-artifact@v4
        with:
          name: build-artifact
          path: {artifact_path}

      - name: Setup Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.DOCKER_REGISTRY }}
          username: ${{ secrets.DOCKER_USER }}
          password: ${{ secrets.DOCKER_PASS }}

      - name: Build and Push
        uses: docker/build-push-action@v5
        with:
          context: .
          file: docker/Dockerfile
          push: true
          tags: |
            ${{ env.DOCKER_IMAGE }}:${{ needs.build.outputs.version }}
            ${{ env.DOCKER_IMAGE }}:${{ needs.build.outputs.commit_short }}
          cache-from: type=registry,ref=${{ env.DOCKER_IMAGE }}:buildcache
          cache-to: type=registry,ref=${{ env.DOCKER_IMAGE }}:buildcache,mode=max

      - name: Scan Image
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.DOCKER_IMAGE }}:${{ needs.build.outputs.version }}
          format: 'table'
          exit-code: '1'
          severity: 'CRITICAL,HIGH'

  # ============================================
  # Job 6: 部署到开发环境
  # ============================================
  deploy-dev:
    runs-on: ubuntu-latest
    needs: docker
    if: github.ref == 'refs/heads/develop' || startsWith(github.ref, 'refs/heads/feature/')
    environment:
      name: dev
      url: https://dev.{project_domain}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Deploy to Dev
        run: |
          echo "🚀 部署到开发环境"
          ./scripts/deploy.sh dev ${{ needs.build.outputs.version }}

      - name: Health Check
        run: |
          echo "🏥 健康检查"
          curl -f https://dev.{project_domain}/health || exit 1

  # ============================================
  # Job 7: 部署到测试环境
  # ============================================
  deploy-staging:
    runs-on: ubuntu-latest
    needs: docker
    if: github.ref == 'refs/heads/develop'
    environment:
      name: staging
      url: https://staging.{project_domain}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Deploy to Staging
        run: |
          echo "🧪 部署到测试环境"
          ./scripts/deploy.sh staging ${{ needs.build.outputs.version }}

      - name: Run E2E Tests
        run: |
          echo "🧪 执行E2E测试"
          npm run test:e2e

      - name: Health Check
        run: |
          curl -f https://staging.{project_domain}/health || exit 1

  # ============================================
  # Job 8: 部署到生产环境（需审批）
  # ============================================
  deploy-prod:
    runs-on: ubuntu-latest
    needs: docker
    if: github.ref == 'refs/heads/main'
    environment:
      name: prod
      url: https://{project_domain}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Deploy to Prod
        run: |
          echo "🚀 部署到生产环境"
          ./scripts/deploy.sh prod ${{ needs.build.outputs.version }}

      - name: Health Check
        run: |
          curl -f https://{project_domain}/health || exit 1

      - name: Verify Deployment
        run: |
          echo "✅ 验证部署成功"
          ./scripts/verify-deployment.sh prod

  # ============================================
  # Job 9: 回滚（失败时触发）
  # ============================================
  rollback:
    runs-on: ubuntu-latest
    needs: deploy-prod
    if: failure() && github.ref == 'refs/heads/main'
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Rollback
        run: |
          echo "⚠️ 触发回滚"
          ./scripts/rollback.sh prod

      - name: Notify Rollback
        uses: slackapi/slack-github-action@v1
        with:
          channel-id: '{slack_channel}'
          slack-message: |
            ⚠️ 生产环境回滚
            - 项目: ${{ env.PROJECT_NAME }}
            - 原因: 部署失败
        env:
          SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}

```

- **pipeline_doc_template**: 
```
# CI/CD流水线文档

## 文档信息
| 项目名称 | {project_name} |
| 技术栈 | {tech_stack} |
| CI工具 | {ci_tool} |
| 创建日期 | {date} |
| 创建人 | {author} |

---

## 1. 流水线概览

### 1.1 流水线架构图
```
[代码提交] → [代码检出] → [质量检查] → [单元测试] → [安全扫描]
                                                 ↓
[部署审批] ← [镜像推送] ← [镜像构建] ← [应用构建] ← [通过]
     ↓
[部署环境] → [健康检查] → [验收测试] → [完成]
```

### 1.2 流水线阶段
| 阶段 | 说明 | 工具 | 预计时间 |
| 代码检出 | 从Git仓库检出代码 | Git | 30秒 |
| 质量检查 | Lint和SonarQube | ESLint/SonarQube | 2分钟 |
| 单元测试 | 执行单元测试和覆盖率检查 | Jest/JUnit | 3分钟 |
| 安全扫描 | 依赖检查和SAST | Trivy/OWASP | 2分钟 |
| 构建 | 构建应用和Docker镜像 | Gradle/Docker | 5分钟 |
| 部署 | 部署到目标环境 | Helm/Kubectl | 3分钟 |

### 1.3 总执行时间
- 开发环境: ~12分钟
- 生产环境（含审批）: ~15分钟

---

## 2. 分支策略

### 2.1 分支模型
采用 **{branch_strategy}** 分支策略

| 分支 | 说明 | 自动部署目标 |
| main | 生产分支 | 生产环境（需审批） |
| develop | 开发分支 | 测试环境 |
| feature/* | 功能分支 | 开发环境 |
| hotfix/* | 紧急修复分支 | 开发→生产 |

### 2.2 分支规则
- main分支合并需要PR审批
- develop分支允许直接推送
- feature分支完成后合并到develop

---

## 3. 部署策略

### 3.1 部署策略类型
采用 **{deployment_strategy}** 部署策略

| 策略 | 适用环境 | 说明 |
| Rolling Update | 生产环境 | 逐步替换，零停机 |
| Blue-Green | 生产环境（可选） | 双环境切换，快速回滚 |
| Canary | 生产环境（可选） | 小流量验证，渐进发布 |
| Recreate | 开发/测试环境 | 全量替换，简单快速 |

### 3.2 部署流程
1. 部署新版本到目标环境
2. 执行健康检查验证
3. 运行验收测试
4. 确认部署成功或触发回滚

---

## 4. 质量门禁

### 4.1 门禁规则
| 门禁项 | 阈值 | 不通过后果 |
| 单元测试覆盖率 | ≥ {coverage_threshold}% | 阻止部署 |
| 代码质量评分 | ≥ B级 | 阻止部署 |
| 安全漏洞 | 无CRITICAL | 阻止部署 |
| 测试通过率 | 100% | 阻止部署 |

### 4.2 门禁配置
```yaml
quality_gates:
  unit_test_coverage: {coverage_threshold}
  sonarqube_quality_gate: true
  security_scan_critical: 0
  test_pass_rate: 100
```

---

## 5. 回滚机制

### 5.1 回滚触发条件
| 条件 | 触发回滚 |
| 部署失败 | ✅ |
| 健康检查失败 | ✅ |
| 验收测试失败 | ✅ |
| 手动触发 | ✅ |

### 5.2 回滚流程
1. 识别当前版本问题
2. 回滚到上一稳定版本
3. 验证回滚成功
4. 发送回滚通知

### 5.3 回滚命令
```bash
# Helm回滚
helm rollback {project_name} -n {namespace}

# Kubernetes回滚
kubectl rollout undo deployment/{project_name} -n {namespace}
```

---

## 6. 环境配置

### 6.1 环境列表
| 环境 | Namespace | 配置文件 | URL |
| 开发 | dev-{project} | values-dev.yaml | dev.{domain} |
| 测试 | staging-{project} | values-staging.yaml | staging.{domain} |
| 生产 | prod-{project} | values-prod.yaml | {domain} |

### 6.2 环境差异
| 配置项 | 开发 | 测试 | 生产 |
| replicas | 1 | 2 | 3 |
| resources.cpu | 100m | 200m | 500m |
| resources.memory | 128Mi | 256Mi | 512Mi |
| auto_scaling | 禁用 | 禁用 | 启用 |

---

## 7. 通知配置

### 7.1 通知渠道
- Slack: #{slack_channel}
- Email: {email_list}

### 7.2 通知事件
| 事件 | 通知内容 |
| 构建成功 | ✅ 版本、分支、提交信息 |
| 构建失败 | ❌ 失败原因、链接 |
| 部署成功 | 🚀 环境、版本、URL |
| 部署失败/回滚 | ⚠️ 回滚原因、影响 |

---

## 8. 常见问题排查

### 8.1 构建失败
| 问题 | 排查方法 |
| 编译错误 | 检查代码变更和依赖版本 |
| 测试失败 | 查看测试报告，定位失败用例 |
| 质量门禁 | 检查SonarQube报告 |

### 8.2 部署失败
| 问题 | 排查方法 |
| 镜像拉取失败 | 检查镜像仓库和凭证 |
| 资源不足 | 检查K8s资源配额 |
| 健康检查失败 | 检查应用日志 |

### 8.3 排查命令
```bash
# 查看Pod状态
kubectl get pods -n {namespace} -l app={project_name}

# 查看Pod日志
kubectl logs -n {namespace} -l app={project_name}

# 查看部署事件
kubectl describe deployment {project_name} -n {namespace}
```

---

## 9. 操作指南

### 9.1 手动触发构建
```bash
# Jenkins手动构建
# 在Jenkins界面点击"Build Now"

# GitHub Actions手动触发
# 在Actions页面选择workflow，点击"Run workflow"
```

### 9.2 手动部署
```bash
./scripts/deploy.sh {environment} {version}
```

### 9.3 手动回滚
```bash
./scripts/rollback.sh {environment}
```

```


## 检查清单


### before_design


- **item**: 项目结构已了解
- **check**: 读取项目配置文件

- **item**: 技术栈已识别
- **check**: 检查tech_stack参数

- **item**: CI工具已选择
- **check**: 检查ci_tool参数

### during_design


- **item**: 构建阶段完整
- **check**: 编译/打包/镜像构建完整

- **item**: 测试阶段完整
- **check**: 单元测试/集成测试完整

- **item**: 质量门禁配置
- **check**: 覆盖率/质量评分门禁设置

- **item**: 安全扫描配置
- **check**: 依赖检查/SAST配置

- **item**: 部署策略选择
- **check**: 部署策略与环境匹配

- **item**: 回滚机制设计
- **check**: 回滚触发条件和流程

### after_design


- **item**: 配置文件生成
- **check**: CI/CD配置文件完整

- **item**: 环境配置完整
- **check**: 所有环境配置文件

- **item**: 文档编写完整
- **check**: 流水线文档和操作手册

- **item**: 测试验证
- **check**: 触发测试构建验证

## 质量标准


- **standard**: 构建成功率
- **requirement**: ≥ 95%
- **check**: 统计构建成功比例

- **standard**: 部署成功率
- **requirement**: ≥ 99%
- **check**: 统计部署成功比例

- **standard**: 构建时间
- **requirement**: < 15分钟
- **check**: 监控构建执行时间

- **standard**: 回滚成功率
- **requirement**: 100%
- **check**: 测试回滚流程

## 参考文档


### methodology


- **name**: DevOps
- **description**: 开发运维一体化方法论

- **name**: GitOps
- **description**: Git驱动的运维模式

- **name**: 12-Factor App
- **description**: 云原生应用最佳实践
- **url**: https://12factor.net/

### primary


- **path**: 运维/references/ci-cd-guide.md
- **description**: CI/CD最佳实践指南

## 协作关系


### upstream


- **skill**: implement
- **relationship**: 提供构建产物
- **condition**: 代码开发完成后

- **skill**: test-executor
- **relationship**: 提供测试用例
- **condition**: 测试设计完成后

### downstream


- **skill**: deploy-analyzer
- **relationship**: 部署分析
- **condition**: 部署完成后

## 使用示例


- **name**: Java Spring Boot项目CI/CD
- **input_summary**: 项目: order-service, 技术栈: Java/Spring Boot, CI: Jenkins
- **output_summary**: 
```
## Jenkins流水线设计

### 流水线阶段（共10个）
1. Checkout - Git检出代码
2. Code Quality - SonarQube扫描
3. Unit Test - JUnit测试（覆盖率≥80%）
4. Security Scan - OWASP依赖检查
5. Build - Gradle构建
6. Docker Build - 多阶段构建
7. Docker Push - 推送到Harbor
8. Deploy Dev - 自动部署
9. Deploy Staging - 自动部署
10. Deploy Prod - 审批后部署

### 质量门禁
- 单元测试覆盖率: ≥80%
- SonarQube质量门禁: 通过
- 安全漏洞: 0个CRITICAL

### 部署策略
- 生产环境: Rolling Update
- 开发/测试: Recreate

### 回滚机制
- 自动回滚触发条件: 健康检查失败
- 手动回滚: helm rollback order-service

```


## 注意事项

- 生产部署必须经过审批
- 安全扫描发现CRITICAL漏洞阻止部署
- 回滚机制必须测试验证
- 构建失败需及时处理
- 流水线配置需版本控制
- 定期更新依赖安全检查规则

## metadata

- **created_at**: 2026-06-11
- **updated_at**: 2026-06-11
- **author**: Claude Agent

### version_history


- **version**: 1.0.0
- **date**: 2026-03-20
- **changes**: 初始版本

- **version**: 2.0.0
- **date**: 2026-06-11
- **changes**: 基于DevOps/GitOps/12-Factor重构，支持多种CI工具