# SearXNG 自建部署指南

## 快速部署

### Docker 单容器

```bash
# 创建目录
mkdir -p ./searxng/config ./searxng/data

# 启动容器
docker run --name searxng -d \
    -p 8888:8080 \
    -v "./config:/etc/searxng" \
    -v "./data:/var/cache/searxng" \
    searxng/searxng:latest

# 访问 http://localhost:8888
```

### Docker Compose（推荐）

```bash
# 创建目录
mkdir -p ./searxng/core-config && cd ./searxng

# 下载配置文件
curl -fsSL \
    -O https://raw.githubusercontent.com/searxng/searxng/master/container/docker-compose.yml \
    -O https://raw.githubusercontent.com/searxng/searxng/master/container/.env.example

# 配置
cp .env.example .env
nano .env  # 编辑 SECRET_KEY

# 启动
docker compose up -d

# 查看状态
docker compose ps
```

## 配置说明

### 基础配置 (settings.yml)

```yaml
use_default_settings: true

server:
  # 绑定地址
  bind_address: "0.0.0.0:8080"
  
  # 密钥（必须修改）
  secret_key: "your-secret-key-change-this"
  
  # 限流配置
  limiter: false
  
  # 图片代理
  image_proxy: true

# 搜索引擎配置
engines:
  - name: google
    engine: google
    disabled: false
    
  - name: bing
    engine: bing
    disabled: false
    
  - name: github
    engine: github
    disabled: false
    
  - name: stackoverflow
    engine: stackoverflow
    disabled: false

# UI 配置
preferences:
  lock: []
  
search:
  # 默认语言
  default_lang: "zh-CN"
  # 自动补全
  autocomplete: "google"
```

### 环境变量 (.env)

```env
# 实例名称
SEARXNG_INSTANCE_NAME="My SearXNG"

# 密钥（必须修改）
SEARXNG_SECRET="your-random-secret-key-here"

# 绑定地址
SEARXNG_BIND_ADDRESS="0.0.0.0:8080"

# Redis 配置（可选，用于缓存）
# REDIS_URL="redis://redis:6379/0"
```

## 高级配置

### 启用 Redis 缓存

修改 docker-compose.yml：

```yaml
services:
  searxng:
    # ... 其他配置
    depends_on:
      - redis
      
  redis:
    image: redis:alpine
    volumes:
      - redis-data:/data

volumes:
  redis-data:
```

### 反向代理配置

#### Nginx

```nginx
server {
    listen 80;
    server_name search.example.com;

    location / {
        proxy_pass http://127.0.0.1:8888;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

#### Caddy

```
search.example.com {
    reverse_proxy localhost:8888
}
```

## API 使用

### JSON API

```bash
# 搜索并返回 JSON
curl "http://localhost:8888/search?q=python&format=json"

# 指定搜索引擎
curl "http://localhost:8888/search?q=!github%20react&format=json"

# 分页
curl "http://localhost:8888/search?q=python&format=json&pageno=2"
```

### Python 调用

```python
import requests

def search(query, instance="http://localhost:8888"):
    response = requests.get(
        f"{instance}/search",
        params={"q": query, "format": "json"}
    )
    return response.json()

# 使用
results = search("python web framework")
for item in results.get("results", []):
    print(f"{item['title']}: {item['url']}")
```

## 维护命令

```bash
# 查看日志
docker compose logs -f

# 重启服务
docker compose restart

# 更新镜像
docker compose pull
docker compose up -d

# 停止服务
docker compose down

# 完全清理
docker compose down -v
```

## 公开实例列表

| 实例 | 地址 | 特点 |
|------|------|------|
| searx.be | https://searx.be | 稳定，无追踪 |
| search.bus-hit.me | https://search.bus-hit.me | 快速 |
| searx.fmac.xyz | https://searx.fmac.xyz | 稳定 |
| search.sapti.me | https://search.sapti.me | 隐私友好 |

> 完整列表: https://searxng.org/#public_instances

## 故障排除

| 问题 | 解决方案 |
|------|----------|
| 无法访问 | 检查防火墙和端口映射 |
| 搜索无结果 | 检查搜索引擎配置 |
| 速度慢 | 启用 Redis 缓存 |
| 被封 IP | 配置代理或更换实例 |
