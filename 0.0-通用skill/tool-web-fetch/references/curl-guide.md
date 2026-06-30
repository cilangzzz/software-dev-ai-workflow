# curl 网页抓取快速参考

## 基础命令

### 抓取网页
```bash
# 基础抓取
curl -sL "https://example.com"

# 保存到文件
curl -sL "https://example.com" -o page.html

# 显示响应头
curl -sI "https://example.com"

# 跟随重定向
curl -sL -k "https://example.com"  # -k 忽略 SSL 证书
```

### 常用参数

| 参数 | 说明 |
|------|------|
| `-s` | 静默模式，不显示进度 |
| `-L` | 跟随重定向 |
| `-k` | 忽略 SSL 证书验证 |
| `-o` | 输出到文件 |
| `-O` | 使用远程文件名保存 |
| `-I` | 只获取响应头 |
| `-H` | 添加请求头 |
| `-A` | 设置 User-Agent |
| `-b` | 发送 Cookie |
| `-x` | 使用代理 |
| `--max-time` | 最大请求时间 |

## 反爬处理

### User-Agent 设置
```bash
# Chrome
curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" "https://example.com"

# Firefox
curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0" "https://example.com"

# Googlebot
curl -sL -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" "https://example.com"
```

### 完整请求头
```bash
curl -sL \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9" \
  -H "Accept-Language: zh-CN,zh;q=0.9,en;q=0.8" \
  -H "Cache-Control: no-cache" \
  "https://example.com"
```

### Cookie 使用
```bash
# 发送 Cookie
curl -sL -b "session=abc123; token=xyz789" "https://example.com"

# 从文件读取 Cookie
curl -sL -b cookies.txt "https://example.com"

# 保存响应 Cookie
curl -sL -c cookies.txt "https://example.com/login"
```

## GitHub 专用

### 获取文件内容
```bash
# README
curl -sL "https://raw.githubusercontent.com/owner/repo/main/README.md"

# 任意文件
curl -sL "https://raw.githubusercontent.com/owner/repo/branch/path/to/file"
```

### GitHub API
```bash
# 仓库信息
curl -sL "https://api.github.com/repos/owner/repo"

# Issues
curl -sL "https://api.github.com/repos/owner/repo/issues"

# Releases
curl -sL "https://api.github.com/repos/owner/repo/releases"

# 带认证（提高速率限制）
curl -sL -H "Authorization: token YOUR_TOKEN" "https://api.github.com/user"
```

## JSON 处理 (配合 jq)

### 安装 jq
```bash
# Ubuntu/Debian
sudo apt install jq

# macOS
brew install jq

# Windows (Scoop)
scoop install jq
```

### 常用 jq 命令
```bash
# 格式化 JSON
curl -sL "https://api.github.com/repos/owner/repo" | jq .

# 提取字段
curl -sL "https://api.github.com/repos/owner/repo" | jq '{name, stars: .stargazers_count}'

# 提取数组元素
curl -sL "https://api.github.com/repos/owner/repo/issues" | jq '.[].title'

# 过滤
curl -sL "https://api.github.com/repos/owner/repo/issues" | jq '.[] | select(.state == "open") | .title'
```

## 批量抓取

### 简单循环
```bash
for url in "url1" "url2" "url3"; do
  curl -sL "$url" -o "$(basename $url).html"
  sleep 1  # 延迟避免被封
done
```

### 并行抓取
```bash
# 使用 xargs
cat urls.txt | xargs -P 4 -I {} curl -sL {} -o {}.html
```

## 代理设置

```bash
# HTTP 代理
curl -sL -x "http://proxy:8080" "https://example.com"

# SOCKS5 代理
curl -sL -x "socks5://127.0.0.1:1080" "https://example.com"

# 带认证
curl -sL -x "http://user:pass@proxy:8080" "https://example.com"
```

## 故障排除

| 问题 | 解决方案 |
|------|----------|
| SSL 证书错误 | 添加 `-k` 参数 |
| 连接超时 | 添加 `--max-time 30` |
| 重定向循环 | 使用 `-L` 并检查 URL |
| 中文乱码 | 使用 `iconv` 或 Python 处理编码 |
| 403 禁止访问 | 添加 User-Agent 和其他请求头 |
