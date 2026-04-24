# Vue前端开发 Agent编写规则
# 适用场景：Vue3、Pinia、Vite、TypeScript

# ============================================
# 技术栈定义
# ============================================
tech_stack:
  framework: "Vue 3.x"
  build_tool: "Vite 5.x"
  state_management: "Pinia 2.x"
  router: "Vue Router 4.x"
  language: "TypeScript 5.x"
  css:
    - "Tailwind CSS"
    - "SCSS"
    - "UnoCSS"
  ui_frameworks:
    - "Element Plus"
    - "Ant Design Vue"
    - "Naive UI"

# ============================================
# Agent角色能力模板
# ============================================
capabilities_template:
  core_skills:
    - skill: "Vue3开发"
      level: "expert"
      components:
        - "Composition API"
        - "Setup语法糖"
        - "响应式系统（ref/reactive）"
        - "生命周期钩子"

    - skill: "组件设计"
      level: "expert"
      components:
        - "单文件组件SFC"
        - "Props/Emits定义"
        - "插槽Slots"
        - "组件通信（provide/inject）"

    - skill: "状态管理"
      level: "advanced"
      components:
        - "Pinia Store"
        - "组合式Store"
        - "持久化插件"
        - "状态订阅"

    - skill: "TypeScript"
      level: "advanced"
      components:
        - "类型定义"
        - "泛型组件"
        - "类型推导"
        - "Props类型约束"

    - skill: "路由管理"
      level: "advanced"
      components:
        - "Vue Router 4"
        - "路由守卫"
        - "动态路由"
        - "路由懒加载"

# ============================================
# 项目结构规范
# ============================================
project_structure:
  vue3_standard: |
    {project_name}/
    ├── src/
    │   ├── main.ts            # 入口文件
    │   ├── App.vue            # 根组件
    │   ├── api/               # API接口
    │   │   ├── index.ts       # Axios实例
    │   │   ├── types.ts       # API类型
    │   │   └── modules/       # 模块API
    │   │   │   ├── user.ts
    │   │   │   └── item.ts
    │   ├── assets/            # 静态资源
    │   │   ├── images/
    │   │   └── styles/
    │   ├── components/        # 公共组件
    │   │   ├── common/
    │   │   │   ├── Button.vue
    │   │   │   ├── Modal.vue
    │   │   ├── layout/
    │   │   │   ├── Header.vue
    │   │   │   ├── Sidebar.vue
    │   │   └── business/      # 业务组件
    │   ├── composables/       # 组合式函数
    │   │   ├── useUser.ts
    │   │   ├── useTable.ts
    │   │   └── usePermission.ts
    │   ├── directives/        # 自定义指令
    │   │   ├── permission.ts
    │   │   └── loading.ts
    │   ├── layouts/           # 布局组件
    │   │   ├── DefaultLayout.vue
    │   │   └── BlankLayout.vue
    │   ├── router/            # 路由配置
    │   │   ├── index.ts
    │   │   ├── routes/
    │   │   │   ├── user.ts
    │   │   │   └── dashboard.ts
    │   │   └── guards.ts      # 路由守卫
    │   ├── stores/            # Pinia状态
    │   │   ├── index.ts
    │   │   └── modules/
    │   │   │   ├── userStore.ts
    │   │   │   ├── appStore.ts
    │   ├── styles/            # 样式文件
    │   │   ├── index.scss
    │   │   ├── variables.scss
    │   │   └── mixins.scss
    │   ├── types/             # 类型定义
    │   │   ├── global.d.ts
    │   │   ├── api.d.ts
    │   │   └── models/
    │   │   │   ├── user.ts
    │   ├── utils/             # 工具函数
    │   │   ├── request.ts
    │   │   ├── storage.ts
    │   │   ├── format.ts
    │   │   └── validate.ts
    │   └── views/             # 页面组件
    │   │   ├── home/
    │   │   │   ├── index.vue
    │   │   │   ├── components/
    │   │   │   └── hooks.ts
    │   │   ├── user/
    │   │   │   ├── list/
    │   │   │   ├── detail/
    │   │   │   └── edit/
    ├── public/
    ├── .env
    ├── .env.development
    ├── .env.production
    ├── index.html
    ├── package.json
    ├── tsconfig.json
    ├── vite.config.ts
    ├── tailwind.config.js    # Tailwind配置
    └── README.md

# ============================================
# 命名规范
# ============================================
naming_conventions:
  # 文件命名
  files:
    - rule: "组件文件PascalCase.vue"
      examples: ["UserList.vue", "SearchForm.vue", "DataTable.vue"]
    - rule: "组合式函数use前缀.ts"
      examples: ["useUserStore.ts", "useSearch.ts", "useTable.ts"]
    - rule: "API文件小驼峰.ts"
      examples: ["userApi.ts", "orderApi.ts"]
    - rule: "Store文件Store后缀.ts"
      examples: ["userStore.ts", "appStore.ts"]
    - rule: "类型文件.d.ts或.ts"
      examples: ["user.d.ts", "models/user.ts"]

  # 组件命名
  components:
    - rule: "PascalCase"
      examples: ["UserList", "SearchForm", "DataTable"]
    - rule: "多词命名避免与HTML冲突"
      examples: ["TodoList（而非Todo）", "CancelButton"]
    - rule: "布局组件Layout后缀"
      examples: ["DefaultLayout", "BlankLayout"]
    - rule: "页面组件index.vue命名"
      examples: ["views/user/list/index.vue"]

  # Props/Emits命名
  props_emits:
    - rule: "Props小驼峰"
      examples: ["userName", "isVisible", "dataSource"]
    - rule: "Emits动词过去式或动词"
      examples: ["update:modelValue", "close", "submit", "change"]

  # Store命名
  stores:
    - rule: "useXxxStore函数名"
      examples: ["useUserStore", "useCartStore", "useAppStore"]

  # 变量命名
  variables:
    - rule: "ref/reactive变量小驼峰"
      examples: ["userName", "loading", "tableData"]
    - rule: "常量UPPER_CASE或k前缀"
      examples: ["MAX_SIZE", "kDefaultPageSize"]

# ============================================
# 代码风格规范
# ============================================
code_style:
  # Vue3组件模板
  vue3_component: |
    <script setup lang="ts">
    import { ref, computed, onMounted, watch } from 'vue'
    import type { PropType } from 'vue'

    // Props定义
    interface Props {
      title: string
      count?: number
      disabled?: boolean
    }
    const props = withDefaults(defineProps<Props>(), {
      count: 0,
      disabled: false
    })

    // Emits定义
    const emit = defineEmits<{
      update: [value: number]
      close: []
      submit: [data: SubmitData]
    }>()

    // 响应式状态
    const localCount = ref(props.count)
    const loading = ref(false)

    // 计算属性
    const doubled = computed(() => localCount.value * 2)
    const isDisabled = computed(() => props.disabled || loading.value)

    // 方法
    const handleClick = () => {
      emit('update', localCount.value + 1)
    }

    const handleSubmit = async () => {
      loading.value = true
      try {
        // 业务逻辑
        emit('submit', { count: localCount.value })
      } finally {
        loading.value = false
      }
    }

    // 监听器
    watch(() => props.count, (newVal) => {
      localCount.value = newVal
    })

    // 生命周期
    onMounted(() => {
      console.log('mounted')
    })
    </script>

    <template>
      <div class="component">
        <h2>{{ title }}</h2>
        <p>Count: {{ localCount }}</p>
        <button 
          @click="handleClick" 
          :disabled="isDisabled"
        >
          Add
        </button>
      </div>
    </template>

    <style scoped>
    .component {
      padding: 16px;
    }
    </style>

  # Pinia Store模板
  pinia_store: |
    import { defineStore } from 'pinia'
    import { ref, computed } from 'vue'
    import type { User } from '@/types/models/user'

    export const useUserStore = defineStore('user', () => {
      // State
      const userInfo = ref<User | null>(null)
      const token = ref<string>('')
      const loading = ref(false)

      // Getters
      const isLoggedIn = computed(() => !!token.value)
      const userName = computed(() => userInfo.value?.name ?? '')

      // Actions
      async function login(credentials: LoginCredentials) {
        loading.value = true
        try {
          const res = await userApi.login(credentials)
          token.value = res.token
          userInfo.value = res.user
        } finally {
          loading.value = false
        }
      }

      function logout() {
        token.value = ''
        userInfo.value = null
      }

      function updateUserInfo(user: User) {
        userInfo.value = user
      }

      return {
        // State
        userInfo,
        token,
        loading,
        // Getters
        isLoggedIn,
        userName,
        // Actions
        login,
        logout,
        updateUserInfo
      }
    })

  # Composable模板
  composable: |
    import { ref, onUnmounted } from 'vue'
    import type { TableData, TableParams } from '@/types'

    export function useTable<T>(apiFn: (params: TableParams) => Promise<TableData<T>>) {
      const data = ref<T[]>([])
      const loading = ref(false)
      const total = ref(0)
      const pagination = ref({
        page: 1,
        pageSize: 10
      })

      async function fetchData(params?: Partial<TableParams>) {
        loading.value = true
        try {
          const res = await apiFn({
            ...pagination.value,
            ...params
          })
          data.value = res.list
          total.value = res.total
        } finally {
          loading.value = false
        }
      }

      function changePage(page: number) {
        pagination.value.page = page
        fetchData()
      }

      function changePageSize(size: number) {
        pagination.value.pageSize = size
        pagination.value.page = 1
        fetchData()
      }

      // 自动清理
      onUnmounted(() => {
        data.value = []
      })

      return {
        data,
        loading,
        total,
        pagination,
        fetchData,
        changePage,
        changePageSize
      }
    }

# ============================================
# Skill示例
# ============================================
skill_examples:
  vue3_scaffold:
    id: "vue3-scaffold"
    name: "Vue3项目脚手架"
    description: "生成Vue3标准项目结构，包含Pinia、Router、TypeScript配置"

  vue3_component_designer:
    id: "vue3-component-designer"
    name: "Vue3组件设计"
    description: "根据UI设计稿生成Vue3组件代码"

  pinia_store_generator:
    id: "pinia-store-generator"
    name: "Pinia Store生成"
    description: "根据数据结构生成Pinia状态管理代码"

  vue3_composable_generator:
    id: "vue3-composable-generator"
    name: "Composable函数生成"
    description: "生成Vue3组合式函数代码"

# ============================================
# 注意事项
# ============================================
notes:
  - "使用<script setup>语法糖"
  - "Props和Emits使用TypeScript类型定义"
  - "组合式函数以use开头"
  - "Store使用Pinia，以useXxxStore命名"
  - "API调用统一使用封装的axios实例"
  - "页面组件使用index.vue命名"
  - "CSS使用scoped避免样式污染"