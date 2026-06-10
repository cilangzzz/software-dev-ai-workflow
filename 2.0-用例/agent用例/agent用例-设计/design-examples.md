# 设计系统分析用例

## 用例1：颜色Token一致性检查

### 场景描述
设计师需要检查设计系统中颜色Token的使用一致性，发现偏离设计规范的元素并获取优化建议。

### 使用Skill
- **Skill**: design-system-analyzer
- **触发方式**: `/design-system-analyzer` 或自然语言 "设计Token检查"

### 完整提示词
```
/design-system-analyzer

设计Token文件: design/tokens.json
检查类型: color
```

### 输入参数
| 参数名 | 类型 | 必填 | 值 |
|--------|------|------|-----|
| design_source | string | 是 | "design/tokens.json" |
| check_types | string | 否 | "color" |

### 执行过程

#### 步骤1：Token提取
从设计源提取Token定义：

**已定义的颜色Token**：
| Token名称 | 色值 | 用途 |
|-----------|------|------|
| primary-500 | #2563EB | 主品牌色 |
| primary-600 | #1D4ED8 | 主品牌色hover |
| gray-100 | #F3F4F6 | 背景色 |
| gray-500 | #6B7280 | 次要文字 |
| success-500 | #10B981 | 成功状态 |
| danger-500 | #EF4444 | 危险状态 |

**总计**: 32个颜色Token

#### 步骤2：使用分析
分析Token使用情况：

**规范颜色Token使用**：
| Token名称 | 使用次数 | 占比 | 状态 |
|-----------|----------|------|------|
| primary-500 | 156 | 28% | ✅ |
| primary-600 | 89 | 16% | ✅ |
| gray-100 | 78 | 14% | ✅ |
| gray-500 | 45 | 8% | ✅ |
| success-500 | 34 | 6% | ✅ |
| danger-500 | 28 | 5% | ✅ |

**非规范颜色使用**：
| 颜色值 | 使用次数 | 占比 | 出现位置 |
|--------|----------|------|----------|
| #3B82F6 | 23 | 4% | 按钮组件、导航栏 |
| #FF5733 | 12 | 2% | 促销标签 |
| #10B981 | 8 | 1% | 状态指示器 |
| #F59E0B | 6 | 1% | 警告图标 |

#### 步骤3：一致性检查
检查设计一致性：

**一致性评分**: 75/100 ⚠️

**问题统计**：
- 规范Token使用率: 77%
- 非规范颜色占比: 8%
- 缺失Token定义: 3个

#### 步骤4：偏差检测
检测偏离设计规范的元素：

**🔴 高优先级偏差**：
| 问题 | 位置 | 影响 | 建议 |
|------|------|------|------|
| 品牌色不一致 | 导航栏使用#3B82F6 | 品牌形象混乱 | 改用 primary-500 (#2563EB) |
| 主按钮颜色偏差 | 按钮组件使用#3B82F6 | 视觉不统一 | 使用 primary-600 (#1D4ED8) |

**🟡 中优先级偏差**：
| 问题 | 位置 | 建议 |
|------|------|------|
| 促销色未定义 | 促销标签 | 新增 promo-500 Token |
| 状态色未标准化 | 状态指示器 | 使用 success-500 |
| 文字色阶不完整 | 次要文字 | 使用 gray-400 |

#### 步骤5：报告生成
生成分析报告和优化建议：

**推荐的新Token定义**：
```json
{
  "promo": {
    "500": "#FF5733"
  },
  "warning": {
    "500": "#F59E0B"
  }
}
```

### 最终输出
```markdown
# 设计系统分析报告 - 颜色一致性

## 概述
- 分析范围: 全部页面
- 设计Token数: 32
- 一致性评分: 75/100 ⚠️

## Token使用分析

### 规范颜色Token（已定义）
| Token名称 | 使用次数 | 占比 | 状态 |
|-----------|----------|------|------|
| primary-500 | 156 | 28% | ✅ |
| primary-600 | 89 | 16% | ✅ |
| gray-100 | 78 | 14% | ✅ |
| gray-500 | 45 | 8% | ✅ |
| success-500 | 34 | 6% | ✅ |
| danger-500 | 28 | 5% | ✅ |

### 非规范颜色（⚠️ 问题）
| 颜色值 | 使用次数 | 占比 | 出现位置 |
|--------|----------|------|----------|
| #3B82F6 | 23 | 4% | 按钮组件、导航栏 |
| #FF5733 | 12 | 2% | 促销标签 |
| #10B981 | 8 | 1% | 状态指示器 |
| #F59E0B | 6 | 1% | 警告图标 |
| #6B7280 | 5 | 1% | 次要文字 |

## 一致性问题

### 🔴 高优先级
| 问题 | 位置 | 影响 | 建议 |
|------|------|------|------|
| 品牌色不一致 | 导航栏使用#3B82F6 | 品牌形象混乱 | 改用 primary-500 (#2563EB) |
| 主按钮颜色偏差 | 按钮组件使用#3B82F6 | 视觉不统一 | 使用 primary-600 (#1D4ED8) |

### 🟡 中优先级
| 问题 | 位置 | 建议 |
|------|------|------|
| 促销色未定义 | 促销标签 | 新增 promo-500 Token |
| 状态色未标准化 | 状态指示器 | 使用 success-500 |
| 文字色阶不完整 | 次要文字 | 使用 gray-400 |

## 推荐的颜色Token定义

```json
{
  "color": {
    "primary": {
      "50": "#EFF6FF",
      "100": "#DBEAFE",
      "200": "#BFDBFE",
      "300": "#93C5FD",
      "400": "#60A5FA",
      "500": "#3B82F6",
      "600": "#2563EB",
      "700": "#1D4ED8",
      "800": "#1E40AF",
      "900": "#1E3A8A"
    },
    "gray": {
      "50": "#F9FAFB",
      "100": "#F3F4F6",
      "200": "#E5E7EB",
      "300": "#D1D5DB",
      "400": "#9CA3AF",
      "500": "#6B7280",
      "600": "#4B5563",
      "700": "#374151",
      "800": "#1F2937",
      "900": "#111827"
    },
    "success": {
      "500": "#10B981"
    },
    "warning": {
      "500": "#F59E0B"
    },
    "danger": {
      "500": "#EF4444"
    },
    "promo": {
      "500": "#FF5733"
    }
  }
}
```

## 修复建议

### 立即执行
1. 替换所有 #3B82F6 为 primary-500
2. 定义促销色Token (promo-500)

### 计划执行
1. 完善文字色阶Token
2. 统一状态指示器颜色
3. 建立颜色使用规范文档
```

---

## 用例2：设计稿转代码

### 场景描述
前端开发人员需要将设计稿中的ProductCard组件转换为React代码，使用Tailwind CSS作为样式方案。

### 使用Skill
- **Skill**: design-to-code
- **触发方式**: `/design-to-code` 或自然语言 "设计稿转代码"

### 完整提示词
```
/design-to-code

设计文件: ProductCard (Figma导出)
框架: React
样式方案: Tailwind CSS
```

### 输入参数
| 参数名 | 类型 | 必填 | 值 |
|--------|------|------|-----|
| design_file | string | 是 | "design/cards/ProductCard.json" |
| framework | string | 是 | "react" |
| component_name | string | 否 | "ProductCard" |
| style_solution | string | 否 | "tailwind" |

### 执行过程

#### 步骤1：设计解析
解析设计稿结构：

**设计稿信息**：
- 组件名称: ProductCard
- 设计尺寸: 256px × 320px
- 包含元素: 图片、标题、价格、标签、按钮

**解析结果**：
- 容器: 卡片容器 (w-64, rounded-lg, shadow-md)
- 图片区: 商品图片 (h-48, object-cover)
- 信息区: 标题、价格、标签
- 操作区: 加入购物车按钮

#### 步骤2：结构识别
识别布局和组件结构：

**布局结构**：
```
┌─────────────────────────────────┐
│         [商品图片]               │  h-48
│                                 │
├─────────────────────────────────┤
│  商品标题                        │  p-4
│  ¥价格  ~~原价~~                 │
│  [加入购物车]                    │
└─────────────────────────────────┘
```

**组件层级**：
- Card (容器)
  - Image (商品图片)
  - Content (内容区)
    - Title (标题)
    - Price (价格区)
    - Tags (标签区)
    - Button (操作按钮)

#### 步骤3：样式提取
提取样式属性：

**设计Token映射**：
| 设计属性 | Token | Tailwind类 |
|----------|-------|------------|
| 主品牌色 | primary-500 | bg-blue-500 |
| 圆角 | radius-md | rounded-lg |
| 阴影 | shadow-card | shadow-md |
| 间距 | spacing-4 | p-4 |

**详细样式**：
- 卡片: bg-white, rounded-lg, shadow-md, w-64
- 图片: w-full, h-48, object-cover
- 标题: text-lg, font-medium, text-gray-900
- 价格: text-xl, font-bold, text-red-600
- 按钮: bg-blue-500, text-white, py-2, rounded-md

#### 步骤4：代码生成
生成目标框架代码：

**组件接口定义**：
```typescript
interface ProductCardProps {
  product: Product;
  onAddToCart?: (product: Product) => void;
}
```

**生成代码结构**：
- ProductCard.tsx (组件主文件)
- types.ts (类型定义)
- ProductCard.stories.tsx (Storybook)

#### 步骤5：优化处理
优化代码结构和命名：

**优化点**：
- 添加 loading="lazy" 实现图片懒加载
- 添加 hover、active、disabled 状态
- 支持 originalPrice 可选显示
- 添加 truncat 处理标题溢出

### 最终输出
```markdown
# 设计转代码报告 - ProductCard组件

## 基本信息
- 组件名称: ProductCard
- 目标框架: React + TypeScript
- 样式方案: Tailwind CSS

## 设计解析

### 布局结构
```
┌─────────────────────────────────┐
│         [商品图片]               │  h-48
│                                 │
├─────────────────────────────────┤
│  商品标题                        │  p-4
│  ¥价格  ~~原价~~                 │
│  [加入购物车]                    │
└─────────────────────────────────┘
```

### 设计Token映射
| 设计属性 | Token | Tailwind类 |
|----------|-------|------------|
| 主品牌色 | primary-500 | bg-blue-500 |
| 圆角 | radius-md | rounded-lg |
| 阴影 | shadow-card | shadow-md |
| 间距 | spacing-4 | p-4 |

## 生成的代码

### ProductCard.tsx
```tsx
import React from 'react';
import { Product } from '../types';

interface ProductCardProps {
  product: Product;
  onAddToCart?: (product: Product) => void;
}

export const ProductCard: React.FC<ProductCardProps> = ({
  product,
  onAddToCart,
}) => {
  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden w-64 hover:shadow-lg transition-shadow">
      {/* 商品图片 */}
      <img
        src={product.image}
        alt={product.name}
        className="w-full h-48 object-cover"
        loading="lazy"
      />

      {/* 商品信息 */}
      <div className="p-4">
        {/* 商品标题 */}
        <h3 className="text-lg font-medium text-gray-900 truncate" title={product.name}>
          {product.name}
        </h3>

        {/* 价格区域 */}
        <div className="mt-2 flex items-baseline gap-2">
          <span className="text-xl font-bold text-red-600">
            ¥{product.price.toFixed(2)}
          </span>
          {product.originalPrice && (
            <span className="text-sm text-gray-400 line-through">
              ¥{product.originalPrice.toFixed(2)}
            </span>
          )}
        </div>

        {/* 标签 */}
        {product.tags?.map((tag) => (
          <span
            key={tag}
            className="inline-block mt-2 px-2 py-1 text-xs bg-red-100 text-red-600 rounded"
          >
            {tag}
          </span>
        ))}

        {/* 加入购物车按钮 */}
        <button
          onClick={() => onAddToCart?.(product)}
          className="mt-4 w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 active:bg-blue-700 transition-colors disabled:bg-gray-300 disabled:cursor-not-allowed"
          disabled={!product.inStock}
        >
          {product.inStock ? '加入购物车' : '已售罄'}
        </button>
      </div>
    </div>
  );
};
```

### types.ts
```ts
export interface Product {
  id: string;
  name: string;
  image: string;
  price: number;
  originalPrice?: number;
  tags?: string[];
  inStock: boolean;
}
```

### ProductCard.stories.tsx (Storybook)
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { ProductCard } from './ProductCard';

const meta: Meta<typeof ProductCard> = {
  title: 'Components/ProductCard',
  component: ProductCard,
};

export default meta;
type Story = StoryObj<typeof ProductCard>;

export const Default: Story = {
  args: {
    product: {
      id: '1',
      name: 'Apple iPhone 15 Pro',
      image: 'https://placehold.co/256x192',
      price: 8999,
      originalPrice: 9999,
      tags: ['新品', '热销'],
      inStock: true,
    },
  },
};

export const OutOfStock: Story = {
  args: {
    product: {
      id: '2',
      name: 'Sold Out Product',
      image: 'https://placehold.co/256x192',
      price: 199,
      inStock: false,
    },
  },
};
```

## 使用示例

```tsx
import { ProductCard } from './components/ProductCard';

function ProductList({ products }) {
  const handleAddToCart = (product) => {
    // 加入购物车逻辑
    console.log('Add to cart:', product);
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
      {products.map((product) => (
        <ProductCard
          key={product.id}
          product={product}
          onAddToCart={handleAddToCart}
        />
      ))}
    </div>
  );
}
```

## 注意事项

1. **图片处理**: 添加了 `loading="lazy"` 实现懒加载
2. **响应式**: 需要根据实际布局调整 `w-64` 固定宽度
3. **无障碍**: 建议添加 `aria-label` 属性
4. **交互状态**: 已添加 hover、active、disabled 状态
5. **性能**: 大列表建议配合虚拟滚动使用
```

---

## 用例3：组件规范检查

### 场景描述
需要检查Button组件是否符合设计规范，包括尺寸、颜色、圆角、交互状态等方面。

### 使用Skill
- **Skill**: design-system-analyzer
- **触发方式**: `/design-system-analyzer` 或自然语言 "检查设计一致性"

### 完整提示词
```
/design-system-analyzer

检查目标: src/components/Button/
检查类型: 设计规范一致性
```

### 输入参数
| 参数名 | 类型 | 必填 | 值 |
|--------|------|------|-----|
| design_source | string | 是 | "src/components/Button/" |
| check_types | string | 否 | "all" |

### 执行过程

#### 步骤1：Token提取
从设计规范提取标准定义：

**Button设计规范**：
| 属性 | Small | Medium | Large |
|------|-------|--------|-------|
| 高度 | 32px | 40px | 48px |
| 水平内边距 | 16px | 16px | 24px |
| 圆角 | 4px | 6px | 8px |

**颜色规范**：
| 状态 | 规范色 |
|------|--------|
| Primary | #2563EB |
| Primary Hover | #1D4ED8 |
| Secondary | #6B7280 |
| Danger | #DC2626 |
| Disabled | #9CA3AF |

#### 步骤2：使用分析
分析实际组件实现：

**实际尺寸实现**：
| 属性 | Small | Medium | Large |
|------|-------|--------|-------|
| 高度 | 32px ✅ | 40px ✅ | 52px ❌ |
| 水平内边距 | 12px ⚠️ | 12px ⚠️ | 16px ⚠️ |

**实际颜色实现**：
| 状态 | 规范色 | 实际色 | 状态 |
|------|--------|--------|------|
| Primary | #2563EB | #2563EB | ✅ |
| Primary Hover | #1D4ED8 | #1E40AF | ⚠️ 色差 |
| Secondary | #6B7280 | #6B7280 | ✅ |
| Danger | #DC2626 | #EF4444 | ❌ 不一致 |
| Disabled | #9CA3AF | #D1D5DB | ⚠️ 色差 |

#### 步骤3：一致性检查
检查设计一致性：

**规范符合度**: 82/100

**检查结果统计**：
- 尺寸规范符合: 75%
- 颜色规范符合: 60%
- 交互状态完整: 60%

#### 步骤4：偏差检测
检测偏离设计规范的元素：

**尺寸偏差**：
- Large按钮高度错误: 应为48px，实际52px
- 水平内边距不足: 建议16px，实际12px
- 圆角值偏大: Medium应为6px，Large应为8px

**颜色偏差**：
- Danger颜色不一致: 应为#DC2626，实际#EF4444
- Primary Hover色差: 轻微色差
- Disabled色差: 略浅

**交互状态缺失**：
- Active状态: 未实现
- Focus状态: 未实现（影响键盘导航）
- Loading状态: 未实现

#### 步骤5：报告生成
生成分析报告和修复代码建议：

**修复代码建议**：
```tsx
const buttonSizes = {
  sm: 'h-8 px-4 text-sm rounded',      // 32px height, 16px padding
  md: 'h-10 px-4 text-base rounded-md', // 40px height, 6px radius
  lg: 'h-12 px-6 text-lg rounded-lg',   // 48px height, 8px radius
};
```

### 最终输出
```markdown
# 组件设计规范检查报告

## 检查概要
- 检查组件: Button
- 检查时间: 2024-01-15
- 规范符合度: 82/100

## 检查结果

### 尺寸规范检查

| 属性 | 规范值 | 实际值 | 状态 |
|------|--------|--------|------|
| Small 高度 | 32px | 32px | ✅ |
| Medium 高度 | 40px | 40px | ✅ |
| Large 高度 | 48px | 52px | ❌ 偏大4px |
| 水平内边距 | 16px | 12px | ⚠️ 偏小 |

### 颜色规范检查

| 状态 | 规范色 | 实际色 | 状态 |
|------|--------|--------|------|
| Primary | #2563EB | #2563EB | ✅ |
| Primary Hover | #1D4ED8 | #1E40AF | ⚠️ 色差 |
| Secondary | #6B7280 | #6B7280 | ✅ |
| Danger | #DC2626 | #EF4444 | ❌ 颜色不一致 |
| Disabled | #9CA3AF | #D1D5DB | ⚠️ 色差 |

### 圆角规范检查

| 尺寸 | 规范值 | 实际值 | 状态 |
|------|--------|--------|------|
| Small | 4px | 4px | ✅ |
| Medium | 6px | 8px | ❌ 偏大 |
| Large | 8px | 12px | ❌ 偏大 |

### 交互状态检查

| 状态 | 规范要求 | 实现情况 | 状态 |
|------|----------|----------|------|
| Hover | 背景色加深10% | 已实现 | ✅ |
| Active | 背景色加深20% | 未实现 | ❌ |
| Focus | 2px outline | 未实现 | ❌ |
| Disabled | 透明度60% | 已实现 | ✅ |
| Loading | 显示spinner | 未实现 | ❌ |

## 问题详情

### 🔴 必须修复
1. **Large按钮高度错误**: 应为48px，实际52px
2. **Danger颜色不一致**: 应为#DC2626，实际#EF4444
3. **缺少Focus状态**: 影响键盘导航体验

### 🟡 建议修复
1. **水平内边距不足**: 建议16px，实际12px
2. **圆角值偏大**: Medium应为6px，Large应为8px
3. **Primary Hover色差**: 轻微色差

## 修复代码建议

```tsx
// Button.tsx - 修复后的样式定义

const buttonSizes = {
  sm: 'h-8 px-4 text-sm rounded',      // 32px height, 16px padding
  md: 'h-10 px-4 text-base rounded-md', // 40px height, 6px radius
  lg: 'h-12 px-6 text-lg rounded-lg',   // 48px height, 8px radius
};

const buttonVariants = {
  primary: `
    bg-blue-600
    hover:bg-blue-700
    active:bg-blue-800
    focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2
    text-white
  `,
  secondary: `
    bg-gray-500
    hover:bg-gray-600
    active:bg-gray-700
    focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2
    text-white
  `,
  danger: `
    bg-red-600
    hover:bg-red-700
    active:bg-red-800
    focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2
    text-white
  `,
  disabled: `
    bg-gray-300
    text-gray-500
    cursor-not-allowed
    opacity-60
  `,
};
```

## 设计规范文档更新建议

建议将实际使用的颜色值更新到设计Token中，确保设计稿与代码一致：

```json
{
  "color": {
    "danger": {
      "500": "#DC2626",
      "600": "#B91C1C",
      "700": "#991B1B"
    }
  }
}
```
```