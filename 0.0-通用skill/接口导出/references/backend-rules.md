# 各技术栈代码扫描和解析规则

## 通用流程

```
识别技术栈 → 扫描Controller文件 → 解析路由映射 → 解析参数 → 解析返回类型 → 提取注释/注解
```

## Java SpringBoot

### 文件扫描

```bash
# 扫描所有Controller文件
Glob pattern: "**/controller/**/*.java"
Glob pattern: "**/*Controller.java"
```

### 注解识别

| 注解 | 用途 | 提取信息 |
|------|------|----------|
| `@RestController` | 标记REST控制器 | 类为API源 |
| `@Controller` | 标记控制器 | 类为API源（需配合@ResponseBody） |
| `@RequestMapping("/path")` | 类级别路径前缀 | api_prefix + path |
| `@GetMapping("/path")` | GET请求映射 | method=GET, path |
| `@PostMapping("/path")` | POST请求映射 | method=POST, path |
| `@PutMapping("/path")` | PUT请求映射 | method=PUT, path |
| `@DeleteMapping("/path")` | DELETE请求映射 | method=DELETE, path |
| `@PatchMapping("/path")` | PATCH请求映射 | method=PATCH, path |
| `@RequestBody` | JSON请求体 | requestBody, content: application/json |
| `@RequestParam("name")` | 查询参数 | parameter, in: query |
| `@PathVariable("name")` | 路径变量 | parameter, in: path |
| `@RequestHeader("name")` | 请求头 | parameter, in: header |
| `@CookieValue("name")` | Cookie | parameter, in: cookie |
| `@Valid` | 启用校验 | 递归解析DTO的校验注解 |
| `@CrossOrigin` | 跨域 | 标记为支持跨域 |

### Swagger/SpringDoc 注解

| 注解 | 用途 | 映射字段 |
|------|------|----------|
| `@Operation(summary="接口名")` | 接口描述 | summary, description |
| `@ApiResponse(responseCode="200")` | 响应描述 | responses.200 |
| `@Parameter(description="参数描述")` | 参数描述 | parameter.description |
| `@Schema(description="字段描述")` | 字段描述 | property.description |
| `@Tag(name="模块名")` | 分组 | tags |
| `@Api(tags={"模块"})` | 分组 (Swagger2) | tags |

### 校验注解 → Schema 映射

| 校验注解 | Schema属性 |
|----------|-----------|
| `@NotNull` | required: true |
| `@NotBlank` | required: true, minLength: 1 |
| `@NotEmpty` | required: true, minItems/minLength: 1 |
| `@Size(min=1, max=100)` | minLength, maxLength |
| `@Min(0)` | minimum: 0 |
| `@Max(100)` | maximum: 100 |
| `@Email` | format: email |
| `@Pattern(regexp="...")` | pattern: "..." |
| `@Positive` | exclusiveMinimum: 0 |
| `@Negative` | exclusiveMaximum: 0 |
| `@Past` | format: date-time |
| `@Future` | format: date-time |

### DTO/VO/Entity 解析

```
1. 读取类文件
2. 提取所有字段（包括父类字段）
3. 对每个字段：
   - 提取字段类型 → JSON Schema type
   - 提取 @Schema(description) → description
   - 提取校验注解 → required, minLength, maxLength等
   - 提取 @JsonProperty(name) → 属性名
   - 如果是枚举类型 → enum: [值列表]
   - 如果是嵌套对象 → 递归解析或使用 $ref
   - 如果是集合类型 → type: array, items: {类型}
```

### 循环引用处理

```
检测方式：维护已解析类的集合，再次遇到时使用 $ref
输出格式：
  "$ref": "#/components/schemas/ClassName"
同时将类定义添加到 components/schemas 中
```

## Python FastAPI

### 文件扫描

```bash
Glob pattern: "**/router*.py"
Glob pattern: "**/api/**/*.py"
Glob pattern: "**/views/**/*.py"
```

### 装饰器识别

| 装饰器 | 用途 |
|--------|------|
| `@app.get("/path")` | GET请求 |
| `@app.post("/path")` | POST请求 |
| `@app.put("/path")` | PUT请求 |
| `@app.delete("/path")` | DELETE请求 |
| `@router.get("/path")` | GET请求（Router） |
| `@router.post("/path")` | POST请求（Router） |

### 参数识别

| 参数方式 | 说明 |
|----------|------|
| `param: str = Query(...)` | 查询参数 |
| `param: str = Path(...)` | 路径参数 |
| `param: str = Header(...)` | 请求头 |
| `body: UserCreate` | 请求体（Pydantic model） |
| `response_model=UserResponse` | 响应模型 |

### Pydantic Model 解析

```python
class UserCreate(BaseModel):
    username: str = Field(..., min_length=1, max_length=50, description="用户名")
    password: str = Field(..., description="密码")
    rememberMe: bool = Field(default=False, description="记住我")
```

→ 对应 JSON Schema:
```json
{
  "type": "object",
  "properties": {
    "username": { "type": "string", "minLength": 1, "maxLength": 50, "description": "用户名" },
    "password": { "type": "string", "description": "密码" },
    "rememberMe": { "type": "boolean", "default": false, "description": "记住我" }
  },
  "required": ["username", "password"]
}
```

## Python Flask

### 文件扫描

```bash
Glob pattern: "**/views/**/*.py"
Glob pattern: "**/routes/**/*.py"
Glob pattern: "**/api/**/*.py"
```

### 装饰器识别

| 装饰器 | 用途 |
|--------|------|
| `@app.route("/path", methods=["GET"])` | 路由定义 |
| `@blueprint.route("/path")` | Blueprint路由 |

## Go Gin

### 文件扫描

```bash
Glob pattern: "**/handler/**/*.go"
Glob pattern: "**/controller/**/*.go"
Glob pattern: "**/api/**/*.go"
```

### 路由识别

| 调用 | 用途 |
|------|------|
| `r.GET("/path", handler)` | GET请求 |
| `r.POST("/path", handler)` | POST请求 |
| `group.GET("/path", handler)` | 路由组 |
| `c.ShouldBindJSON(&req)` | JSON参数绑定 |
| `c.Query("key")` | 查询参数 |
| `c.Param("key")` | 路径参数 |

### 结构体Tag解析

```go
type LoginRequest struct {
    Username string `json:"username" binding:"required" description:"用户名"`
    Password string `json:"password" binding:"required" description:"密码"`
}
```

## Node.js Express

### 文件扫描

```bash
Glob pattern: "**/routes/**/*.js"
Glob pattern: "**/routes/**/*.ts"
Glob pattern: "**/controllers/**/*.js"
```

### 路由识别

| 调用 | 用途 |
|------|------|
| `app.get("/path", handler)` | GET请求 |
| `app.post("/path", handler)` | POST请求 |
| `router.get("/path", handler)` | Router路由 |
| `req.body` | 请求体 |
| `req.query.key` | 查询参数 |
| `req.params.key` | 路径参数 |
| `req.headers.key` | 请求头 |

## Node.js NestJS

### 文件扫描

```bash
Glob pattern: "**/*.controller.ts"
Glob pattern: "**/*.module.ts"
```

### 装饰器识别

| 装饰器 | 用途 |
|--------|------|
| `@Controller("/path")` | 控制器前缀 |
| `@Get("/path")` | GET请求 |
| `@Post("/path")` | POST请求 |
| `@Put("/path")` | PUT请求 |
| `@Delete("/path")` | DELETE请求 |
| `@Body()` | 请求体 |
| `@Query("key")` | 查询参数 |
| `@Param("key")` | 路径参数 |
| `@Header("key")` | 请求头 |
| `@ApiTags("模块")` | Swagger分组 |
| `@ApiOperation({summary:"接口名"})` | 接口描述 |
| `@ApiResponse({status:200})` | 响应描述 |

## C# ASP.NET

### 文件扫描

```bash
Glob pattern: "**/Controllers/**/*.cs"
Glob pattern: "**/*Controller.cs"
```

### 属性识别

| 属性 | 用途 |
|------|------|
| `[ApiController]` | API控制器标记 |
| `[Route("api/[controller]")]` | 路由前缀 |
| `[HttpGet]` / `[HttpGet("{id}")]` | GET请求 |
| `[HttpPost]` | POST请求 |
| `[HttpPut]` | PUT请求 |
| `[HttpDelete]` | DELETE请求 |
| `[FromBody]` | 请求体 |
| `[FromQuery]` | 查询参数 |
| `[FromRoute]` | 路径参数 |
| `[FromHeader]` | 请求头 |
