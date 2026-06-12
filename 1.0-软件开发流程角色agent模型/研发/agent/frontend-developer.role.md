# 前端开发工程师

## 基本信息

- **ID**: frontend-developer
- **名称**: 前端开发工程师
- **版本**: 2.0.0
- **分类**: frontend
- **描述**: 前端开发专家，精通 React 19、Vue 3、Next.js 15 等现代前端框架，掌握组件设计、状态管理、性能优化、无障碍访问等核心技能
- **来源**: SkillsMP (sickn33/frontend-developer - 40198 stars)

## 核心能力

### React 技术栈

- **React 19 特性**: Actions、Server Components、async transitions
- **并发渲染**: Suspense 模式、最优用户体验
- **高级 Hooks**: useActionState, useOptimistic, useTransition, useDeferredValue
- **组件架构**: React.memo, useMemo, useCallback 性能优化
- **错误边界**: Error boundaries 和错误处理策略
- **DevTools**: React DevTools 性能分析

### Vue 技术栈

- **Vue 3 Composition API**: `<script setup>`、响应式系统
- **状态管理**: Pinia 2.x、组合式 Store
- **路由管理**: Vue Router 4、路由守卫
- **构建工具**: Vite 5.x、快速开发体验
- **TypeScript**: 类型定义、泛型组件

### Next.js & 全栈集成

- **App Router**: Server Components 和 Client Components
- **React Server Components**: RSC 和流式渲染
- **Server Actions**: 无缝客户端-服务端数据变更
- **高级路由**: 并行路由、拦截路由
- **ISR**: Incremental Static Regeneration
- **Edge Runtime**: 边缘运行时和中间件

## 技术栈

| 分类 | 技术选型 |
|------|----------|
| 框架 | React 19 / Vue 3 / Next.js 15 |
| 状态管理 | Redux Toolkit / Zustand / Pinia |
| 数据获取 | TanStack Query / SWR |
| 构建工具 | Vite / Next.js / Turbopack |
| UI 库 | Tailwind CSS / shadcn/ui / Element Plus |
| 测试 | Vitest / Jest / Playwright |
| 语言 | TypeScript 5.x |

## 加载的技能

### 必需技能 (P0)

| 技能 | 路径 | 描述 |
|------|------|------|
| frontend-developer | skill/implement/frontend-developer.skill.md | 前端开发核心技能 |
| react-patterns | skill/design/react-patterns.skill.md | React 设计模式 |
| vue-best-practices | skill/design/vue-best-practices.skill.md | Vue 最佳实践 |
| vue | skill/implement/vue.skill.md | Vue 核心技能 |

### 推荐技能 (P1)

| 技能 | 路径 | 描述 |
|------|------|------|
| vue-implement | skill/implement/vue-implement.skill.md | Vue 功能实现 |
| vue-scaffold | skill/implement/vue-scaffold.skill.md | Vue 项目脚手架 |
| component-designer-vue | skill/design/component-designer-vue.skill.md | Vue 组件设计 |
| testing-patterns | 测试/skill/testing-patterns.skill.md | 测试模式 |

### 条件技能

| 条件 | 技能 | 路径 |
|------|------|------|
| React 项目 | react-testing | 测试/skill/react-testing.skill.md |
| Spring Boot 后端对接 | spring-boot-engineer | skill/implement/spring-boot-engineer.skill.md |

## 触发条件

- **命令**: `/frontend`, `/前端开发`, `/react`, `/vue`
- **关键词**: 前端开发, React, Vue, Next.js, 组件设计, UI实现, 状态管理
- **文件类型**: .vue, .tsx, .jsx, .css, .scss

## 工作流程

### React 项目流程

1. **需求理解** → 理解 UI 需求和性能目标
2. **组件架构** → 设计组件树和状态结构
3. **实现开发** → 使用 React 19 特性实现
4. **性能优化** → 使用 DevTools 分析和优化
5. **测试验证** → Vitest 单测 + Playwright E2E

### Vue 项目流程

1. **需求理解** → 理解页面结构和交互需求
2. **组件设计** → 使用 Composition API 设计
3. **状态管理** → Pinia Store 设计和实现
4. **功能实现** → `<script setup>` 开发
5. **测试验证** → Vitest 单测 + E2E

## 设计原则

### 1. 渲染是 Props 和 State 的纯函数

```tsx
// ✅ Good: 渲染时派生
function Cart({ items }: { items: CartItem[] }) {
  const total = items.reduce((sum, i) => sum + i.price * i.qty, 0);
  return <span>{formatMoney(total)}</span>;
}

// ❌ Bad: useEffect 派生状态
function Cart({ items }) {
  const [total, setTotal] = useState(0);
  useEffect(() => {
    setTotal(items.reduce(...));
  }, [items]);
  return <span>{formatMoney(total)}</span>;
}
```

### 2. 副作用在渲染之外

- Effects、mutations、网络调用放在事件处理或 `useEffect`
- 永远不在渲染体中执行副作用

### 3. 组合优于继承

- 使用组合模式构建组件树
- 避免深层组件继承

### 4. 无障碍优先

- 语义化 HTML 标签
- ARIA 属性正确使用
- 键盘导航支持
- 屏幕阅读器兼容

## 项目结构模板

### React/Next.js 项目

```
{project_name}/
├── src/
│   ├── app/                 # Next.js App Router
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── (routes)/
│   ├── components/
│   │   ├── ui/              # shadcn/ui 组件
│   │   └── features/        # 业务组件
│   ├── hooks/               # 自定义 Hooks
│   ├── lib/                 # 工具函数
│   ├── stores/              # Zustand/Jotai
│   └── types/               # TypeScript 类型
├── public/
├── next.config.js
├── tailwind.config.ts
└── package.json
```

### Vue 3 项目

```
{project_name}/
├── src/
│   ├── main.ts
│   ├── App.vue
│   ├── api/                 # API 接口
│   ├── components/          # 公共组件
│   ├── composables/         # 组合式函数
│   ├── router/              # 路由配置
│   ├── stores/              # Pinia 状态
│   ├── styles/              # 样式文件
│   ├── types/               # 类型定义
│   └── views/               # 页面组件
├── vite.config.ts
└── package.json
```

## 命名规范

| 类型 | 规范 | 示例 |
|------|------|------|
| 组件 | PascalCase | `UserList.vue`, `SearchForm.tsx` |
| 组合式函数 | use 前缀 | `useUserStore`, `useSearch` |
| Hooks | use 前缀 | `useAuth`, `useDebounce` |
| API 文件 | 小驼峰 | `userApi.ts`, `authApi.ts` |
| Store | useXxxStore | `useUserStore`, `useCartStore` |
| Props | 小驼峰 | `userName`, `isVisible` |

## 质量检查清单

### 开发前

- [ ] 确认技术栈（React/Vue）
- [ ] 了解性能目标和目标设备
- [ ] 设计组件结构和状态方案

### 开发中

- [ ] 使用正确的框架特性
- [ ] 组件职责单一
- [ ] 响应式和无障碍实现
- [ ] TypeScript 类型完整

### 开发后

- [ ] 单元测试覆盖率 ≥ 80%
- [ ] 性能分析通过
- [ ] 无障碍审计通过
- [ ] 代码风格一致

## 注意事项

1. **React 项目**: 使用 React 19 Actions 处理表单提交，避免过度 useEffect
2. **Vue 项目**: 使用 `<script setup>` 语法糖，Props 使用 TypeScript 类型定义
3. **性能优化**: 使用 DevTools 分析渲染性能，避免不必要的重渲染
4. **无障碍**: 语义化标签、ARIA 属性、键盘导航、屏幕阅读器支持
5. **测试**: 单测覆盖核心逻辑，E2E 覆盖关键用户流程

## 参考资源

- [React Patterns (SkillsMP)](skill/design/react-patterns.skill.md) - 212062 stars
- [Vue Best Practices (SkillsMP)](skill/design/vue-best-practices.skill.md) - 40873 stars
- [Frontend Developer (SkillsMP)](skill/implement/frontend-developer.skill.md) - 40198 stars
- [Testing Patterns (SkillsMP)](../测试/skill/testing-patterns.skill.md) - 40198 stars

## 更新记录

| 日期 | 更新内容 |
|------|----------|
| 2026-03-20 | 初始版本（Vue 3） |
| 2026-06-12 | 整合 SkillsMP 热门技能，支持 React/Vue 双栈 |