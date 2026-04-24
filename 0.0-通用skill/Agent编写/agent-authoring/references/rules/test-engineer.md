# 测试工程师 Agent编写规则
# 适用场景：自动化测试、单元测试、集成测试、性能测试

# ============================================
# 技术栈定义
# ============================================
tech_stack:
  test_frameworks:
    - name: "pytest"
      language: "Python"
      description: "Python测试框架"
    - name: "Jest"
      language: "JavaScript/TypeScript"
      description: "JavaScript测试框架"
    - name: "JUnit"
      language: "Java"
      description: "Java单元测试框架"
    - name: "Go testing"
      language: "Go"
      description: "Go内置测试框架"
    - name: "Vitest"
      language: "Vue/TypeScript"
      description: "Vite原生测试框架"
  e2e_tools:
    - "Selenium"
    - "Playwright"
    - "Cypress"
    - "Puppeteer"
  performance_tools:
    - "JMeter"
    - "Locust"
    - "k6"
    - "Gatling"
  api_test:
    - "Postman"
    - "REST Client"
    - "httpx"
  mock_tools:
    - "Mockito"
    - "unittest.mock"
    - "sinon"

# ============================================
# Agent角色能力模板
# ============================================
capabilities_template:
  core_skills:
    - skill: "单元测试"
      level: "expert"
      components:
        - "测试用例设计"
        - "Mock和Stub"
        - "断言和验证"
        - "覆盖率分析"
        - "边界测试"

    - skill: "集成测试"
      level: "expert"
      components:
        - "API集成测试"
        - "数据库测试"
        - "服务集成验证"
        - "测试环境管理"

    - skill: "自动化测试"
      level: "advanced"
      components:
        - "E2E测试脚本"
        - "测试框架选择"
        - "CI集成"
        - "测试报告生成"

    - skill: "性能测试"
      level: "intermediate"
      components:
        - "负载测试"
        - "压力测试"
        - "基准测试"
        - "性能分析"

    - skill: "测试管理"
      level: "advanced"
      components:
        - "测试计划制定"
        - "缺陷跟踪"
        - "测试报告"
        - "质量评估"

# ============================================
# 项目结构规范
# ============================================
project_structure:
  test_project_python: |
    {project_name}/
    ├── tests/
    │   ├── unit/                  # 单元测试
    │   │   ├── test_user_service.py
    │   │   ├── test_auth_service.py
    │   │   ├── conftest.py        # pytest fixtures
    │   ├── integration/           # 集成测试
    │   │   ├── test_api.py
    │   │   ├── test_database.py
    │   │   ├── conftest.py
    │   ├── e2e/                   # 端到端测试
    │   │   ├── test_login_flow.py
    │   │   ├── test_order_flow.py
    │   ├── performance/           # 性能测试
    │   │   ├── locustfile.py
    │   │   ├── benchmark_test.py
    │   ├── fixtures/              # 测试数据
    │   │   ├── users.json
    │   │   ├── orders.json
    │   ├── mocks/                 # Mock数据
    │   │   ├── mock_api.py
    │   ├── reports/               # 测试报告
    │   ├── pytest.ini             # pytest配置
    │   ├── conftest.py            # 全局fixtures
    ├── .coveragerc                # 覆盖率配置
    ├── requirements-test.txt
    └── README.md

  test_project_java: |
    {project_name}/
    ├── src/test/java/
    │   ├── unit/                  # 单元测试
    │   │   ├── UserServiceTest.java
    │   │   ├── AuthServiceTest.java
    │   ├── integration/           # 集成测试
    │   │   ├── ApiIntegrationTest.java
    │   │   ├── DatabaseTest.java
    │   ├── e2e/                   # 端到端测试
    │   │   ├── LoginFlowTest.java
    │   ├── performance/           # 性能测试
    │   │   ├── LoadTest.java
    │   ├── mocks/                 # Mock类
    │   ├── resources/             # 测试资源
    │   │   ├── test-data.json
    │   │   ├── application-test.yml
    ├── src/test/resources/
    ├── reports/
    └ README.md

  test_project_frontend: |
    {project_name}/
    ├── tests/
    │   ├── unit/                  # 单元测试
    │   │   ├── components/
    │   │   │   ├── Button.test.ts
    │   │   │   ├── Modal.test.ts
    │   │   ├── hooks/
    │   │   │   ├── useAuth.test.ts
    │   │   ├── utils/
    │   │   │   ├── format.test.ts
    │   ├── integration/           # 集成测试
    │   │   ├── api/
    │   │   │   ├── userApi.test.ts
    │   ├── e2e/                   # E2E测试
    │   │   ├── login.spec.ts
    │   │   ├── order.spec.ts
    │   │   ├── playwright.config.ts
    │   ├── fixtures/              # 测试数据
    │   │   ├── mockData.ts
    │   ├── mocks/                 # Mock handlers
    │   │   ├── handlers.ts
    │   ├── setup.ts               # 测试setup
    │   ├── vitest.config.ts       # Vitest配置
    ├── playwright-report/
    ├── coverage/
    └ README.md

# ============================================
# 命名规范
# ============================================
naming_conventions:
  # 测试文件命名
  test_files:
    - rule: "Python：test_前缀或_test后缀"
      examples: ["test_user_service.py", "user_service_test.py"]
    - rule: "Java：Test后缀"
      examples: ["UserServiceTest.java", "ApiIntegrationTest.java"]
    - rule: "JavaScript/TypeScript：.test.ts或.spec.ts"
      examples: ["Button.test.ts", "login.spec.ts"]

  # 测试类命名
  test_classes:
    - rule: "对应类名 + Test"
      examples: ["UserServiceTest", "AuthServiceTest"]

  # 测试方法命名
  test_methods:
    - rule: "test_ + 方法名 + 场景"
      examples: ["test_create_user_success", "test_login_invalid_password"]
    - rule: "描述性命名"
      examples: ["should_return_user_when_id_exists", "given_valid_input_then_create_order"]

  # 测试数据命名
  test_data:
    - rule: "fixtures/或mocks/目录"
      examples: ["fixtures/users.json", "mocks/mock_api.py"]
    - rule: "Mock文件mock_前缀"
      examples: ["mock_user_service.py", "mock_api_handler.ts"]

# ============================================
# 代码风格规范
# ============================================
code_style:
  # pytest测试模板
  pytest_test: |
    import pytest
    from unittest.mock import Mock, patch
    from app.services.user_service import UserService
    from app.models.user import User

    # Fixture定义
    @pytest.fixture
    def mock_db():
        """Mock数据库会话"""
        return Mock()

    @pytest.fixture
    def user_service(mock_db):
        """创建UserService实例"""
        return UserService(mock_db)

    @pytest.fixture
    def sample_user():
        """测试用户数据"""
        return User(
            id=1,
            username="testuser",
            email="test@example.com"
        )

    # 测试类
    class TestUserService:
        """UserService单元测试"""

        def test_create_user_success(self, user_service, sample_user):
            """测试成功创建用户"""
            # Given
            user_service.db.add = Mock(return_value=sample_user)
            
            # When
            result = user_service.create({
                "username": "testuser",
                "email": "test@example.com"
            })
            
            # Then
            assert result.username == "testuser"
            assert result.email == "test@example.com"

        def test_create_user_duplicate_email(self, user_service):
            """测试重复邮箱创建失败"""
            # Given
            user_service.get_by_email = Mock(return_value=User(email="test@example.com"))
            
            # When/Then
            with pytest.raises(ValueError, match="Email already exists"):
                user_service.create({
                    "username": "newuser",
                    "email": "test@example.com"
                })

        @patch('app.services.user_service.send_email')
        def test_create_user_sends_notification(self, mock_send, user_service):
            """测试创建用户发送通知"""
            # When
            user_service.create({"username": "test", "email": "test@example.com"})
            
            # Then
            mock_send.assert_called_once()

  # Jest/Vitest测试模板
  jest_test: |
    import { describe, it, expect, vi, beforeEach } from 'vitest'
    import { UserService } from '@/services/userService'
    import { mockApi } from '@/tests/mocks/api'

    // Mock设置
    vi.mock('@/api/userApi', () => ({
      userApi: mockApi
    }))

    describe('UserService', () => {
      let userService: UserService

      beforeEach(() => {
        userService = new UserService()
        vi.clearAllMocks()
      })

      describe('createUser', () => {
        it('should create user with valid data', async () => {
          // Given
          const userData = { username: 'test', email: 'test@example.com' }
          mockApi.create.mockResolvedValue({ id: 1, ...userData })

          // When
          const result = await userService.createUser(userData)

          // Then
          expect(result).toEqual({ id: 1, username: 'test', email: 'test@example.com' })
          expect(mockApi.create).toHaveBeenCalledWith(userData)
        })

        it('should throw error for invalid email', async () => {
          // Given
          const userData = { username: 'test', email: 'invalid-email' }

          // When/Then
          await expect(userService.createUser(userData))
            .rejects.toThrow('Invalid email format')
        })
      })
    })

  # Playwright E2E测试模板
  playwright_test: |
    import { test, expect } from '@playwright/test'

    test.describe('User Login Flow', () => {
      test.beforeEach(async ({ page }) => {
        await page.goto('/login')
      })

      test('should login successfully with valid credentials', async ({ page }) => {
        // Given - 输入有效凭证
        await page.fill('[name="username"]', 'testuser')
        await page.fill('[name="password"]', 'password123')
        
        // When - 点击登录
        await page.click('button[type="submit"]')
        
        // Then - 验证跳转到首页
        await expect(page).toHaveURL('/dashboard')
        await expect(page.locator('.welcome-message')).toContainText('Welcome, testuser')
      })

      test('should show error for invalid credentials', async ({ page }) => {
        // Given
        await page.fill('[name="username"]', 'invalid')
        await page.fill('[name="password"]', 'wrong')
        
        // When
        await page.click('button[type="submit"]')
        
        // Then
        await expect(page.locator('.error-message')).toBeVisible()
        await expect(page.locator('.error-message')).toContainText('Invalid credentials')
      })

      test('should disable submit button when form is invalid', async ({ page }) => {
        // Given - 空表单
        await page.fill('[name="username"]', '')
        await page.fill('[name="password"]', '')
        
        // Then
        await expect(page.locator('button[type="submit"]')).toBeDisabled()
      })
    })

  # JMeter性能测试配置
  jmeter_test: |
    <?xml version="1.0" encoding="UTF-8"?>
    <jmeterTestPlan version="1.2">
      <hashTree>
        <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="API Load Test">
          <elementProp name="TestPlan.user_defined_variables" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="BASE_URL" elementType="Argument">
                <stringProp name="Argument.name">BASE_URL</stringProp>
                <stringProp name="Argument.value">http://localhost:8080</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
        </TestPlan>
        <hashTree>
          <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="User Load">
            <stringProp name="ThreadGroup.num_threads">100</stringProp>
            <stringProp name="ThreadGroup.ramp_time">10</stringProp>
            <boolProp name="ThreadGroup.scheduler">true</boolProp>
            <stringProp name="ThreadGroup.duration">60</stringProp>
          </ThreadGroup>
          <hashTree>
            <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="Login">
              <stringProp name="HTTPSampler.domain">${BASE_URL}</stringProp>
              <stringProp name="HTTPSampler.path">/api/login</stringProp>
              <stringProp name="HTTPSampler.method">POST</stringProp>
              <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
                <collectionProp name="Arguments.arguments">
                  <elementProp name="username" elementType="HTTPArgument">
                    <stringProp name="Argument.value">testuser</stringProp>
                  </elementProp>
                  <elementProp name="password" elementType="HTTPArgument">
                    <stringProp name="Argument.value">password123</stringProp>
                  </elementProp>
                </collectionProp>
              </elementProp>
            </HTTPSamplerProxy>
          </hashTree>
        </hashTree>
      </hashTree>
    </jmeterTestPlan>

# ============================================
# Skill示例
# ============================================
skill_examples:
  test_case_generator:
    id: "test-case-generator"
    name: "测试用例生成"
    description: "根据功能需求生成测试用例文档"

  unit_test_generator:
    id: "unit-test-generator"
    name: "单元测试生成"
    description: "根据源代码生成单元测试代码"

  e2e_test_generator:
    id: "e2e-test-generator"
    name: "E2E测试生成"
    description: "生成Playwright/Cypress端到端测试"

  api_test_generator:
    id: "api-test-generator"
    name: "API测试生成"
    description: "根据API文档生成API测试脚本"

  performance_test_generator:
    id: "performance-test-generator"
    name: "性能测试生成"
    description: "生成JMeter/Locust性能测试脚本"

# ============================================
# 注意事项
# ============================================
notes:
  - "测试文件命名遵循框架规范"
  - "测试方法使用描述性命名"
  - "单元测试覆盖边界条件和异常场景"
  - "Mock外部依赖确保测试隔离"
  - "E2E测试覆盖核心业务流程"
  - "性能测试设置合理的并发和持续时间"
  - "测试报告包含覆盖率分析"
  - "CI集成自动运行测试"