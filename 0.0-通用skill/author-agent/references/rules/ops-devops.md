# DevOps运维开发 Agent编写规则
# 适用场景：Docker、Kubernetes、CI/CD、Jenkins、监控

# ============================================
# 技术栈定义
# ============================================
tech_stack:
  containerization:
    - "Docker"
    - "Docker Compose"
    - "containerd"
  orchestration:
    - "Kubernetes (K8s)"
    - "Helm"
    - "Kustomize"
  ci_cd:
    - "Jenkins"
    - "GitLab CI"
    - "GitHub Actions"
    - "ArgoCD"
  monitoring:
    - "Prometheus"
    - "Grafana"
    - "ELK Stack"
    - "Datadog"
  infrastructure:
    - "Terraform"
    - "Ansible"
    - "Pulumi"
  cloud_providers:
    - "AWS"
    - "Azure"
    - "GCP"
    - "阿里云"

# ============================================
# Agent角色能力模板
# ============================================
capabilities_template:
  core_skills:
    - skill: "容器化"
      level: "expert"
      components:
        - "Docker镜像构建"
        - "Docker Compose编排"
        - "镜像优化"
        - "多阶段构建"
        - "安全扫描"

    - skill: "Kubernetes"
      level: "expert"
      components:
        - "Pod/Deployment/Service配置"
        - "Ingress/ConfigMap/Secret"
        - "Helm Charts开发"
        - "资源调度优化"
        - "故障排查"

    - skill: "CI/CD流水线"
      level: "expert"
      components:
        - "Jenkins Pipeline"
        - "GitLab CI配置"
        - "GitHub Actions"
        - "ArgoCD GitOps"
        - "自动化测试集成"

    - skill: "基础设施管理"
      level: "advanced"
      components:
        - "Terraform模块开发"
        - "Ansible Playbook"
        - "云资源配置"
        - "版本控制"

    - skill: "监控告警"
      level: "advanced"
      components:
        - "Prometheus指标采集"
        - "Grafana仪表盘"
        - "告警规则配置"
        - "日志收集分析"

# ============================================
# 项目结构规范
# ============================================
project_structure:
  devops_standard: |
    {project_name}/
    ├── docker/
    │   ├── Dockerfile              # 主镜像
    │   ├── Dockerfile.dev          # 开发镜像
    │   ├── docker-compose.yml      # 本地开发编排
    │   ├── docker-compose.prod.yml # 生产编排
    │   └── .dockerignore
    ├── kubernetes/
    │   ├── base/
    │   │   ├── deployment.yaml
    │   │   ├── service.yaml
    │   │   ├── configmap.yaml
    │   │   ├── secret.yaml
    │   │   ├── ingress.yaml
    │   │   └── kustomization.yaml
    │   ├── overlays/
    │   │   ├── dev/
    │   │   ├── staging/
    │   │   ├── prod/
    │   ├── helm/
    │   │   ├── chart/
    │   │   │   ├── Chart.yaml
    │   │   │   ├── values.yaml
    │   │   │   ├── values-dev.yaml
    │   │   │   ├── values-prod.yaml
    │   │   │   ├── templates/
    │   │   │   │   ├── deployment.yaml
    │   │   │   │   ├── service.yaml
    │   │   │   │   ├── configmap.yaml
    ├── ci/
    │   ├── jenkins/
    │   │   ├── Jenkinsfile
    │   │   ├── pipeline.groovy
    │   ├── gitlab/
    │   │   ├── .gitlab-ci.yml
    │   ├── github/
    │   │   ├── workflows/
    │   │   │   ├── build.yml
    │   │   │   ├── deploy.yml
    │   │   │   ├── test.yml
    │   ├── argocd/
    │   │   ├── application.yaml
    ├── terraform/
    │   ├── modules/
    │   │   ├── vpc/
    │   │   ├── ecs/
    │   │   ├── rds/
    │   ├── environments/
    │   │   ├── dev/
    │   │   ├── staging/
    │   │   ├── prod/
    │   ├── main.tf
    │   ├── variables.tf
    │   ├── outputs.tf
    ├── ansible/
    │   ├── playbooks/
    │   │   ├── deploy.yml
    │   │   ├── configure.yml
    │   ├── roles/
    │   │   ├── app/
    │   │   ├── nginx/
    │   ├── inventory/
    │   │   ├── dev.yml
    │   │   ├── prod.yml
    ├── monitoring/
    │   ├── prometheus/
    │   │   ├── prometheus.yml
    │   │   ├── rules/
    │   │   │   ├── alerts.yml
    │   ├── grafana/
    │   │   ├── dashboards/
    │   │   │   ├── app.json
    │   │   ├── provisioning/
    │   ├── alertmanager/
    │   │   ├── alertmanager.yml
    ├── scripts/
    │   ├── deploy.sh
    │   ├── rollback.sh
    │   ├── health-check.sh
    ├── docs/
    │   ├── deployment-guide.md
    │   ├── troubleshooting.md
    │   ├── monitoring-guide.md
    └ README.md

# ============================================
# 命名规范
# ============================================
naming_conventions:
  # Kubernetes资源命名
  k8s_resources:
    - rule: "小写字母+连字符"
      examples: ["my-app-deployment", "api-server-service"]
    - rule: "资源类型后缀（可选）"
      examples: ["app-deployment", "api-service", "web-ingress"]

  # Docker镜像命名
  docker_images:
    - rule: "registry/namespace/image:tag"
      examples: ["docker.io/myorg/my-app:v1.0.0", "ghcr.io/team/api:latest"]
    - rule: "标签使用语义化版本"
      examples: ["v1.0.0", "v1.0.0-beta", "latest"]

  # Helm Chart命名
  helm_charts:
    - rule: "Chart名称小写+连字符"
      examples: ["my-app", "api-server"]
    - rule: "values文件区分环境"
      examples: ["values.yaml", "values-dev.yaml", "values-prod.yaml"]

  # CI/CD文件命名
  cicd_files:
    - rule: "Jenkinsfile固定名称"
      examples: ["Jenkinsfile"]
    - rule: "GitLab CI固定名称"
      examples: [".gitlab-ci.yml"]
    - rule: "GitHub Actions按功能命名"
      examples: ["build.yml", "deploy.yml", "test.yml"]

  # Terraform文件命名
  terraform_files:
    - rule: "固定名称"
      examples: ["main.tf", "variables.tf", "outputs.tf"]
    - rule: "模块目录按资源类型命名"
      examples: ["vpc/", "ecs/", "rds/"]

  # 脚本文件命名
  scripts:
    - rule: "小写+连字符或下划线"
      examples: ["deploy.sh", "rollback.sh", "health_check.sh"]
    - rule: "操作类型前缀"
      examples: ["deploy_", "backup_", "monitor_"]

# ============================================
# 代码风格规范
# ============================================
code_style:
  # Dockerfile模板
  dockerfile: |
    # ============================================
    # 多阶段构建 - 生产优化镜像
    # ============================================
    
    # 构建阶段
    FROM node:18-alpine AS builder
    WORKDIR /app
    COPY package*.json ./
    RUN npm ci --only=production
    COPY . .
    RUN npm run build

    # 运行阶段
    FROM node:18-alpine AS runner
    WORKDIR /app
    
    # 安全：非root用户
    RUN addgroup --system --gid 1001 appgroup \
        && adduser --system --uid 1001 appuser
    
    # 复制构建产物
    COPY --from=builder --chown=appuser:appgroup /app/dist ./dist
    COPY --from=builder --chown=appuser:appgroup /app/node_modules ./node_modules
    COPY --chown=appuser:appgroup package.json ./
    
    # 健康检查
    HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
        CMD curl -f http://localhost:3000/health || exit 1
    
    USER appuser
    EXPOSE 3000
    CMD ["node", "dist/main.js"]

  # Kubernetes Deployment模板
  k8s_deployment: |
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
      labels:
        app: my-app
        version: v1.0.0
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: my-app
      strategy:
        type: RollingUpdate
        rollingUpdate:
          maxSurge: 1
          maxUnavailable: 0
      template:
        metadata:
          labels:
            app: my-app
            version: v1.0.0
        spec:
          containers:
          - name: my-app
            image: myorg/my-app:v1.0.0
            ports:
            - containerPort: 3000
            resources:
              requests:
                cpu: "100m"
                memory: "128Mi"
              limits:
                cpu: "500m"
                memory: "512Mi"
            env:
            - name: NODE_ENV
              value: "production"
            envFrom:
            - configMapRef:
                name: my-app-config
            - secretRef:
                name: my-app-secret
            livenessProbe:
              httpGet:
                path: /health
                port: 3000
              initialDelaySeconds: 10
              periodSeconds: 30
            readinessProbe:
              httpGet:
                path: /ready
                port: 3000
              initialDelaySeconds: 5
              periodSeconds: 10
          affinity:
            podAntiAffinity:
              preferredDuringSchedulingIgnoredDuringExecution:
              - weight: 100
                podAffinityTerm:
                  labelSelector:
                    matchLabels:
                      app: my-app
                  topologyKey: kubernetes.io/hostname

  # Jenkins Pipeline模板
  jenkins_pipeline: |
    pipeline {
        agent any
        
        environment {
            DOCKER_IMAGE = 'myorg/my-app'
            DOCKER_TAG = "${env.BUILD_NUMBER}"
        }
        
        stages {
            stage('Checkout') {
                steps {
                    checkout scm
                }
            }
            
            stage('Test') {
                steps {
                    sh 'npm ci'
                    sh 'npm run test'
                    sh 'npm run lint'
                }
            }
            
            stage('Build') {
                steps {
                    sh 'npm run build'
                }
            }
            
            stage('Docker Build') {
                steps {
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
            
            stage('Docker Push') {
                steps {
                    withCredentials([usernamePassword(
                        credentialsId: 'docker-registry',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}"
                        sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                    }
                }
            }
            
            stage('Deploy') {
                when {
                    branch 'main'
                }
                steps {
                    sh "kubectl set image deployment/my-app my-app=${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
        
        post {
            always {
                cleanWs()
            }
            success {
                slackSend(color: 'good', message: "Build ${BUILD_NUMBER} successful")
            }
            failure {
                slackSend(color: 'danger', message: "Build ${BUILD_NUMBER} failed")
            }
        }
    }

  # Terraform模块模板
  terraform_module: |
    # ============================================
    # VPC模块
    # ============================================
    
    resource "aws_vpc" "main" {
      cidr_block           = var.vpc_cidr
      enable_dns_hostnames = true
      enable_dns_support   = true
      
      tags = {
        Name        = "${var.project_name}-vpc"
        Environment = var.environment
        ManagedBy   = "terraform"
      }
    }
    
    resource "aws_subnet" "public" {
      count             = length(var.public_subnet_cidrs)
      vpc_id            = aws_vpc.main.id
      cidr_block        = var.public_subnet_cidrs[count.index]
      availability_zone = var.availability_zones[count.index]
      
      tags = {
        Name        = "${var.project_name}-public-${count.index + 1}"
        Environment = var.environment
        Type        = "public"
      }
    }
    
    # ============================================
    # 变量定义
    # ============================================
    variable "vpc_cidr" {
      description = "VPC CIDR block"
      type        = string
      default     = "10.0.0.0/16"
    }
    
    variable "environment" {
      description = "Environment name"
      type        = string
    }

# ============================================
# Skill示例
# ============================================
skill_examples:
  dockerfile_generator:
    id: "dockerfile-generator"
    name: "Dockerfile生成"
    description: "根据应用类型生成优化的多阶段Dockerfile"

  k8s_manifest_generator:
    id: "k8s-manifest-generator"
    name: "K8s配置生成"
    description: "生成Kubernetes Deployment/Service/Ingress配置"

  helm_chart_generator:
    id: "helm-chart-generator"
    name: "Helm Chart生成"
    description: "生成Helm Chart模板和values配置"

  jenkins_pipeline_generator:
    id: "jenkins-pipeline-generator"
    name: "Jenkins Pipeline生成"
    description: "生成Jenkins Pipeline配置"

  terraform_module_generator:
    id: "terraform-module-generator"
    name: "Terraform模块生成"
    description: "生成Terraform基础设施模块"

# ============================================
# 注意事项
# ============================================
notes:
  - "Docker镜像使用多阶段构建减小体积"
  - "Kubernetes资源设置合理的requests和limits"
  - "CI/CD流水线包含测试和安全扫描阶段"
  - "Terraform模块保持可复用性"
  - "监控告警规则需要分级（严重/警告/提示）"
  - "生产环境配置使用Secret管理敏感信息"
  - "部署策略使用RollingUpdate避免中断"
  - "容器运行使用非root用户"