# React前端开发 Agent编写规则
# 适用场景：React、Redux、Next.js、Tailwind CSS

# ============================================
# 技术栈定义
# ============================================
tech_stack:
  framework: "React 18.x"
  language: "TypeScript 5.x"
  state_management:
    - "Redux Toolkit"
    - "Zustand"
    - "Jotai"
    - "React Context"
  router:
    - "React Router 6.x"
    - "Next.js App Router"
  styling:
    - "Tailwind CSS"
    - "CSS Modules"
    - "Styled Components"
    - "Emotion"
  ui_frameworks:
    - "shadcn/ui"
    - "Ant Design"
    - "Material UI"
    - "Chakra UI"
  meta_framework: "Next.js 14.x"

# ============================================
# Agent角色能力模板
# ============================================
capabilities_template:
  core_skills:
    - skill: "React开发"
      level: "expert"
      components:
        - "Hooks（useState/useEffect/useContext）"
        - "自定义Hooks"
        - "组件生命周期"
        - "并发特性（Suspense/Transitions）"

    - skill: "TypeScript集成"
      level: "advanced"
      components:
        - "组件类型定义"
        - "Props类型约束"
        - "泛型组件"
        - "类型推导"

    - skill: "状态管理"
      level: "advanced"
      components:
        - "Redux Toolkit"
        - "Zustand轻量状态"
        - "React Context"

    - skill: "Next.js开发"
      level: "intermediate"
      components:
        - "App Router"
        - "Server Components"
        - "Server Actions"
        - "数据获取策略"

    - skill: "样式方案"
      level: "advanced"
      components:
        - "Tailwind CSS"
        - "CSS Modules"
        - "响应式设计"

# ============================================
# 项目结构规范
# ============================================
project_structure:
  react_standard: |
    {project_name}/
    ├── src/
    │   ├── main.tsx           # 入口文件
    │   ├── App.tsx            # 根组件
    │   ├── components/        # 公共组件
    │   │   ├── ui/            # UI组件
    │   │   │   ├── Button/
    │   │   │   │   ├── Button.tsx
    │   │   │   │   ├── Button.styles.ts
    │   │   │   │   ├── index.ts
    │   │   │   ├── Modal/
    │   │   │   ├── Table/
    │   │   ├── layout/        # 布局组件
    │   │   │   ├── Header.tsx
    │   │   │   ├── Sidebar.tsx
    │   │   │   ├── Footer.tsx
    │   │   ├── common/        # 通用组件
    │   │   │   ├── Loading.tsx
    │   │   │   ├── ErrorBoundary.tsx
    │   │   ├── forms/         # 表单组件
    │   │   │   ├── FormField.tsx
    │   │   │   ├── FormSelect.tsx
    │   ├── pages/             # 页面组件
    │   │   ├── Home/
    │   │   │   ├── index.tsx
    │   │   │   ├── components/
    │   │   │   ├── hooks.ts
    │   │   │   ├── types.ts
    │   │   ├── User/
    │   │   │   ├── List/
    │   │   │   ├── Detail/
    │   │   │   ├── Edit/
    │   │   ├── Dashboard/
    │   ├── hooks/             # 自定义Hooks
    │   │   ├── useAuth.ts
    │   │   ├── useApi.ts
    │   │   ├── useLocalStorage.ts
    │   │   ├── useDebounce.ts
    │   ├── services/          # 服务层
    │   │   ├── api/
    │   │   │   ├── client.ts
    │   │   │   ├── user.ts
    │   │   │   ├── auth.ts
    │   │   ├── auth/
    │   │   │   ├── authService.ts
    │   ├── store/             # 状态管理
    │   │   ├── index.ts
    │   │   ├── slices/
    │   │   │   ├── userSlice.ts
    │   │   │   ├── authSlice.ts
    │   │   ├── hooks.ts       # Redux Hooks
    │   ├── types/             # 类型定义
    │   │   ├── index.ts
    │   │   ├── api.ts
    │   │   ├── models/
    │   │   │   ├── user.ts
    │   │   │   ├── auth.ts
    │   ├── utils/             # 工具函数
    │   │   ├── format.ts
    │   │   ├── validation.ts
    │   │   ├── storage.ts
    │   ├── constants/         # 常量
    │   │   ├── routes.ts
    │   │   ├── api.ts
    │   ├── context/           # Context
    │   │   ├── AuthContext.tsx
    │   │   ├── ThemeContext.tsx
    │   ├── styles/            # 全局样式
    │   │   ├── globals.css
    │   │   ├── tailwind.css
    │   └── router/            # 路由配置
    │   │   ├── index.tsx
    │   │   ├── routes.ts
    │   │   ├── guards.tsx
    ├── public/
    ├── .env
    ├── .env.development
    ├── .env.production
    ├── index.html
    ├── package.json
    ├── tsconfig.json
    ├── tailwind.config.js
    ├── vite.config.ts
    └── README.md

  nextjs_app_router: |
    {project_name}/
    ├── app/
    │   ├── layout.tsx         # 根布局
    │   ├── page.tsx           # 首页
    │   ├── globals.css        # 全局样式
    │   ├── (auth)/            # 路由组
    │   │   ├── login/
    │   │   │   ├── page.tsx
    │   │   ├── register/
    │   │   │   ├── page.tsx
    │   ├── dashboard/
    │   │   ├── layout.tsx
    │   │   ├── page.tsx
    │   │   ├── users/
    │   │   │   ├── page.tsx
    │   │   │   ├── [id]/      # 动态路由
    │   │   │   │   ├── page.tsx
    │   ├── api/               # API路由
    │   │   ├── users/
    │   │   │   ├── route.ts
    │   │   │   ├── [id]/route.ts
    │   ├── components/        # 组件
    │   │   ├── ui/
    │   │   ├── layout/
    │   ├── lib/               # 工具库
    │   │   ├── api.ts
    │   │   ├── auth.ts
    │   │   ├── utils.ts
    │   ├── hooks/             # Hooks
    │   ├── types/             # 类型
    │   └── store/             # 状态（可选）
    ├── public/
    ├── .env.local
    ├── .env.production
    ├── next.config.js
    ├── tailwind.config.js
    ├── tsconfig.json
    ├── package.json
    └── README.md

# ============================================
# 命名规范
# ============================================
naming_conventions:
  # 文件命名
  files:
    - rule: "组件文件PascalCase.tsx"
      examples: ["Button.tsx", "UserList.tsx", "DataTable.tsx"]
    - rule: "Hook文件use前缀.ts"
      examples: ["useAuth.ts", "useDebounce.ts", "useApi.ts"]
    - rule: "服务文件小驼峰.ts"
      examples: ["userService.ts", "authService.ts"]
    - rule: "类型文件小驼峰.ts或.d.ts"
      examples: ["user.ts", "api.d.ts"]
    - rule: "样式文件.styles.ts或.css"
      examples: ["Button.styles.ts", "globals.css"]
    - rule: "index.ts作为导出入口"
      examples: ["components/ui/Button/index.ts"]

  # 组件命名
  components:
    - rule: "PascalCase"
      examples: ["UserList", "SearchForm", "DataTable"]
    - rule: "页面组件Page后缀（可选）"
      examples: ["UserListPage", "DashboardPage"]
    - rule: "布局组件Layout后缀"
      examples: ["MainLayout", "AuthLayout"]
    - rule: "UI组件文件夹组织"
      examples: ["Button/Button.tsx + Button.styles.ts + index.ts"]

  # Props类型命名
  props_types:
    - rule: "组件名Props"
      examples: ["ButtonProps", "UserListProps", "ModalProps"]
    - rule: "使用interface或type"
      examples: ["interface ButtonProps { ... }", "type UserListProps = { ... }"]

  # Hook命名
  hooks:
    - rule: "useXxx"
      examples: ["useAuth", "useDebounce", "useApi", "useLocalStorage"]

  # 变量命名
  variables:
    - rule: "小驼峰"
      examples: ["userName", "isLoading", "fetchData"]
    - rule: "布尔值is/has/should前缀"
      examples: ["isLoading", "hasError", "shouldRender"]
    - rule: "事件处理handle前缀"
      examples: ["handleClick", "handleSubmit", "handleChange"]

  # 常量命名
  constants:
    - rule: "UPPER_CASE或小驼峰"
      examples: ["API_BASE_URL", "MAX_RETRIES", "defaultPageSize"]

# ============================================
# 代码风格规范
# ============================================
code_style:
  # React组件模板
  react_component: |
    import React from 'react'
    import { useState, useEffect, useCallback } from 'react'

    // Props类型定义
    interface ButtonProps {
      title: string
      disabled?: boolean
      loading?: boolean
      onClick?: () => void
      variant?: 'primary' | 'secondary' | 'danger'
      size?: 'sm' | 'md' | 'lg'
    }

    // 组件实现
    export function Button({
      title,
      disabled = false,
      loading = false,
      onClick,
      variant = 'primary',
      size = 'md'
    }: ButtonProps) {
      const [isClicked, setIsClicked] = useState(false)

      const handleClick = useCallback(() => {
        if (!disabled && !loading && onClick) {
          setIsClicked(true)
          onClick()
        }
      }, [disabled, loading, onClick])

      useEffect(() => {
        if (isClicked) {
          setTimeout(() => setIsClicked(false), 200)
        }
      }, [isClicked])

      return (
        <button
          className={`btn btn-${variant} btn-${size}`}
          disabled={disabled || loading}
          onClick={handleClick}
        >
          {loading ? <Spinner /> : title}
        </button>
      )
    }

  # 自定义Hook模板
  custom_hook: |
    import { useState, useEffect, useCallback } from 'react'
    import type { ApiResponse, User } from '@/types'

    interface UseUserOptions {
      initialUserId?: number
      autoFetch?: boolean
    }

    interface UseUserReturn {
      user: User | null
      loading: boolean
      error: Error | null
      fetchUser: (id: number) => Promise<void>
      updateUser: (data: Partial<User>) => Promise<void>
    }

    export function useUser(options: UseUserOptions = {}): UseUserReturn {
      const { initialUserId, autoFetch = false } = options

      const [user, setUser] = useState<User | null>(null)
      const [loading, setLoading] = useState(false)
      const [error, setError] = useState<Error | null>(null)

      const fetchUser = useCallback(async (id: number) => {
        setLoading(true)
        setError(null)
        try {
          const res = await userService.get(id)
          setUser(res.data)
        } catch (err) {
          setError(err as Error)
        } finally {
          setLoading(false)
        }
      }, [])

      const updateUser = useCallback(async (data: Partial<User>) => {
        if (!user) return
        setLoading(true)
        try {
          const res = await userService.update(user.id, data)
          setUser(res.data)
        } catch (err) {
          setError(err as Error)
        } finally {
          setLoading(false)
        }
      }, [user])

      useEffect(() => {
        if (autoFetch && initialUserId) {
          fetchUser(initialUserId)
        }
      }, [autoFetch, initialUserId, fetchUser])

      return { user, loading, error, fetchUser, updateUser }
    }

  # Redux Slice模板
  redux_slice: |
    import { createSlice, PayloadAction } from '@reduxjs/toolkit'
    import type { User, AuthState } from '@/types'

    const initialState: AuthState = {
      user: null,
      token: null,
      isAuthenticated: false,
      loading: false,
      error: null
    }

    const authSlice = createSlice({
      name: 'auth',
      initialState,
      reducers: {
        setCredentials: (state, action: PayloadAction<{ user: User; token: string }>) => {
          state.user = action.payload.user
          state.token = action.payload.token
          state.isAuthenticated = true
        },
        logout: (state) => {
          state.user = null
          state.token = null
          state.isAuthenticated = false
        },
        setLoading: (state, action: PayloadAction<boolean>) => {
          state.loading = action.payload
        },
        setError: (state, action: PayloadAction<string | null>) => {
          state.error = action.payload
        }
      }
    })

    export const { setCredentials, logout, setLoading, setError } = authSlice.actions
    export default authSlice.reducer

# ============================================
# Skill示例
# ============================================
skill_examples:
  react_scaffold:
    id: "react-scaffold"
    name: "React项目脚手架"
    description: "生成React标准项目结构，包含Router、Redux、TypeScript配置"

  nextjs_scaffold:
    id: "nextjs-scaffold"
    name: "Next.js项目脚手架"
    description: "生成Next.js App Router项目结构"

  react_component_designer:
    id: "react-component-designer"
    name: "React组件设计"
    description: "根据UI设计生成React组件代码"

  react_hook_generator:
    id: "react-hook-generator"
    name: "React Hook生成"
    description: "生成自定义Hook代码"

# ============================================
# 注意事项
# ============================================
notes:
  - "组件使用函数组件和Hooks"
  - "Props使用TypeScript类型定义"
  - "自定义Hook以use开头"
  - "事件处理函数以handle前缀"
  - "布尔状态使用is/has/should前缀"
  - "CSS使用Tailwind或CSS Modules"
  - "Next.js优先使用App Router"
  - "Server Components减少客户端bundle"