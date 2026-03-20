# Skill: design-to-code

## 基本信息
- **名称**: design-to-code
- **版本**: 1.0.0
- **所属部门**: 设计部
- **优先级**: P0

## 功能描述
将设计稿转换为可执行的前端代码。支持主流设计工具格式，生成React/Vue等框架的组件代码。

## 触发条件
- 命令触发: `/design-to-code`
- 自然语言触发:
  - "设计稿转代码"
  - "生成组件代码"
  - "设计转前端"

## 输入参数
| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| design_file | string | 是 | 设计文件路径或导出数据 |
| framework | string | 是 | 目标框架：react / vue / html |
| component_name | string | 否 | 组件名称 |
| style_solution | string | 否 | 样式方案：css / scss / styled / tailwind |

## 执行流程
1. **设计解析** - 解析设计稿结构
2. **结构识别** - 识别布局和组件结构
3. **样式提取** - 提取样式属性
4. **代码生成** - 生成目标框架代码
5. **优化处理** - 优化代码结构和命名

## 输出格式

### 代码生成报告
```markdown
# 设计转代码报告

## 基本信息
- 组件名称: {name}
- 目标框架: {framework}
- 样式方案: {style}

## 生成的文件
### {filename}.tsx
```tsx
{component_code}
```

### {filename}.css
```css
{style_code}
```

## 组件结构
```
{name}/
├── index.tsx      # 组件入口
├── styles.css     # 样式文件
└── types.ts       # 类型定义
```

## 使用说明
```tsx
import { {name} } from './components/{name}';

<{name}
  title="示例标题"
  onClick={() => {}}
/>
```

## 注意事项
- {note1}
- {note2}
```

## 使用示例

### 示例：卡片组件转换
**输入**:
```
design_file: design/cards/ProductCard.json
framework: react
component_name: ProductCard
style_solution: tailwind
```

**输出**:
```markdown
# 设计转代码报告

## 基本信息
- 组件名称: ProductCard
- 目标框架: React
- 样式方案: Tailwind CSS

## 生成的文件
### ProductCard.tsx
```tsx
import React from 'react';

interface ProductCardProps {
  image: string;
  title: string;
  price: number;
  originalPrice?: number;
  onAddToCart?: () => void;
}

export const ProductCard: React.FC<ProductCardProps> = ({
  image,
  title,
  price,
  originalPrice,
  onAddToCart,
}) => {
  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden w-64">
      <img
        src={image}
        alt={title}
        className="w-full h-48 object-cover"
      />
      <div className="p-4">
        <h3 className="text-lg font-medium text-gray-900 truncate">
          {title}
        </h3>
        <div className="mt-2 flex items-center gap-2">
          <span className="text-xl font-bold text-red-600">
            ¥{price}
          </span>
          {originalPrice && (
            <span className="text-sm text-gray-400 line-through">
              ¥{originalPrice}
            </span>
          )}
        </div>
        <button
          onClick={onAddToCart}
          className="mt-4 w-full bg-blue-500 text-white py-2 rounded-md
                     hover:bg-blue-600 transition-colors"
        >
          加入购物车
        </button>
      </div>
    </div>
  );
};
```

## 组件结构
```
ProductCard/
├── index.tsx      # 组件入口
├── ProductCard.tsx
└── types.ts
```

## 使用说明
```tsx
import { ProductCard } from './components/ProductCard';

<ProductCard
  image="/product.jpg"
  title="商品名称"
  price={99}
  originalPrice={199}
  onAddToCart={() => console.log('added')}
/>
```

## 注意事项
- 图片路径需要根据实际项目配置
- 按钮交互需要连接实际业务逻辑
- 响应式断点需要根据设计调整
```

## 质量标准
- 代码可运行率 100%
- 样式还原度 ≥ 90%
- 组件复用性良好

## 依赖工具
- Read - 读取设计文件
- Write - 输出代码文件
- Bash - 执行格式化命令

## 注意事项
- 生成的代码需要人工Review
- 复杂交互需要手动补充
- 建议结合设计系统Token
- 响应式设计需要额外处理