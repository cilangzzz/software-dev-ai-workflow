# Python后端开发 Agent编写规则
# 适用场景：FastAPI、Django、Flask

# ============================================
# 技术栈定义
# ============================================
tech_stack:
  language: "Python 3.10+"
  frameworks:
    - name: "FastAPI"
      version: "0.100+"
      description: "高性能异步API框架"
    - name: "Django"
      version: "4.x"
      description: "全功能Web框架"
    - name: "Flask"
      version: "2.x"
      description: "轻量级Web框架"
  orm:
    - "SQLAlchemy 2.x"
    - "Django ORM"
  database:
    - "PostgreSQL"
    - "MySQL"
    - "MongoDB"
  async:
    - "asyncio"
    - "aiohttp"
    - "uvicorn"

# ============================================
# Agent角色能力模板
# ============================================
capabilities_template:
  core_skills:
    - skill: "FastAPI开发"
      level: "expert"
      components:
        - "异步路由和依赖注入"
        - "Pydantic数据验证"
        - "OpenAPI自动文档"
        - "中间件和异常处理"

    - skill: "Django开发"
      level: "expert"
      components:
        - "MTV架构模式"
        - "Django ORM查询"
        - "Django REST Framework"
        - "信号和中间件"

    - skill: "SQLAlchemy"
      level: "advanced"
      components:
        - "ORM映射和关系定义"
        - "异步SQLAlchemy"
        - "查询构建和优化"

    - skill: "异步编程"
      level: "advanced"
      components:
        - "asyncio并发"
        - "异步上下文管理"
        - "协程和任务调度"

# ============================================
# 项目结构规范
# ============================================
project_structure:
  fastapi_standard: |
    {project_name}/
    ├── app/
    │   ├── main.py              # FastAPI入口
    │   ├── api/
    │   │   ├── v1/
    │   │   │   ├── endpoints/
    │   │   │   │   ├── users.py
    │   │   │   │   └── items.py
    │   │   │   └── router.py
    │   │   └── deps.py          # 依赖注入
    │   ├── models/
    │   │   ├── user.py          # SQLAlchemy模型
    │   │   └── item.py
    │   ├── schemas/
    │   │   ├── user.py          # Pydantic schemas
    │   │   └── item.py
    │   ├── services/
    │   │   ├── user_service.py
    │   │   └── item_service.py
    │   ├── core/
    │   │   ├── config.py        # 配置管理
    │   │   ├── security.py      # 安全认证
    │   │   └── exceptions.py    # 异常定义
    │   └── db/
    │   │   ├── session.py       # 数据库会话
    │   │   └── base.py          # Base类
    ├── tests/
    │   ├── test_api/
    │   └── test_services/
    ├── alembic/                  # 数据库迁移
    │   ├── versions/
    │   └── env.py
    ├── .env
    ├── .env.example
    ├── pyproject.toml
    ├── requirements.txt
    ├── alembic.ini
    └── README.md

  django_standard: |
    {project_name}/
    ├── config/
    │   ├── settings/
    │   │   ├── base.py
    │   │   ├── development.py
    │   │   └── production.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    ├── apps/
    │   ├── users/
    │   │   ├── models.py
    │   │   ├── views.py
    │   │   ├── serializers.py
    │   │   ├── urls.py
    │   │   └── admin.py
    │   └── products/
    ├── manage.py
    ├── requirements/
    │   ├── base.txt
    │   ├── development.txt
    │   └── production.txt
    └── README.md

# ============================================
# 命名规范
# ============================================
naming_conventions:
  # 文件命名
  files:
    - rule: "Python文件小写+下划线"
      examples: ["user_service.py", "item_router.py"]
    - rule: "测试文件test_前缀"
      examples: ["test_user_service.py", "test_api.py"]

  # 类命名
  classes:
    - rule: "PascalCase大驼峰"
      examples: ["UserService", "ItemModel", "UserSchema"]
    - rule: "Model类以Model结尾（可选）"
      examples: ["User", "Item"]
    - rule: "Schema类以Schema/Request/Response结尾"
      examples: ["UserSchema", "UserCreateRequest", "UserResponse"]

  # 函数命名
  functions:
    - rule: "snake_case小写+下划线"
      examples: ["get_user", "create_item", "list_users"]
    - rule: "异步函数async_前缀（可选）"
      examples: ["async_get_user", "async_create_item"]

  # 变量命名
  variables:
    - rule: "snake_case"
      examples: ["user_id", "item_list", "db_session"]

# ============================================
# 代码风格规范
# ============================================
code_style:
  # FastAPI路由模板
  fastapi_router: |
    from fastapi import APIRouter, Depends, HTTPException
    from sqlalchemy.ext.asyncio import AsyncSession
    from app.api.deps import get_db
    from app.schemas.user import UserCreate, UserResponse
    from app.services.user_service import UserService

    router = APIRouter(prefix="/users", tags=["users"])

    @router.post("/", response_model=UserResponse)
    async def create_user(
        user_in: UserCreate,
        db: AsyncSession = Depends(get_db)
    ) -> UserResponse:
        service = UserService(db)
        user = await service.create(user_in)
        return UserResponse.model_validate(user)

    @router.get("/{user_id}", response_model=UserResponse)
    async def get_user(
        user_id: int,
        db: AsyncSession = Depends(get_db)
    ) -> UserResponse:
        service = UserService(db)
        user = await service.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse.model_validate(user)

  # Pydantic Schema模板
  pydantic_schema: |
    from pydantic import BaseModel, Field, EmailStr
    from datetime import datetime
    from typing import Optional

    class UserBase(BaseModel):
        email: EmailStr
        username: str = Field(..., min_length=3, max_length=50)

    class UserCreate(UserBase):
        password: str = Field(..., min_length=8)

    class UserUpdate(BaseModel):
        email: Optional[EmailStr] = None
        username: Optional[str] = Field(None, min_length=3, max_length=50)

    class UserResponse(UserBase):
        id: int
        created_at: datetime
        updated_at: datetime

        class Config:
            from_attributes = True

  # SQLAlchemy Model模板
  sqlalchemy_model: |
    from sqlalchemy import Column, Integer, String, DateTime
    from sqlalchemy.orm import relationship
    from app.db.base import Base
    from datetime import datetime

    class User(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True)
        email = Column(String(255), unique=True, index=True, nullable=False)
        username = Column(String(50), unique=True, index=True, nullable=False)
        hashed_password = Column(String(255), nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

        # 关系定义
        items = relationship("Item", back_populates="owner")

# ============================================
# Skill示例
# ============================================
skill_examples:
  fastapi_scaffold:
    id: "fastapi-scaffold"
    name: "FastAPI项目脚手架"
    description: "生成FastAPI标准项目结构，包含异步支持、认证、数据库配置"

  pydantic_schema_designer:
    id: "pydantic-schema-designer"
    name: "Pydantic Schema设计"
    description: "根据数据结构生成Pydantic验证Schema"

  sqlalchemy_model_designer:
    id: "sqlalchemy-model-designer"
    name: "SQLAlchemy模型设计"
    description: "根据数据库表结构生成SQLAlchemy ORM模型"

  async_service_generator:
    id: "async-service-generator"
    name: "异步服务生成"
    description: "生成异步CRUD服务代码"

# ============================================
# 注意事项
# ============================================
notes:
  - "使用pydantic v2语法（model_validate而非from_orm）"
  - "异步函数必须使用async/await"
  - "数据库会话使用AsyncSession"
  - "依赖注入使用Depends"
  - "环境变量使用pydantic-settings管理"
  - "类型注解使用typing模块"