param(
  [switch] $StrictMetadata = $true
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$examplesDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$skillRoot = Split-Path -Parent $examplesDir
$manager = Join-Path $skillRoot 'scripts\\ssh_config_manager.py'

if (-not (Test-Path -LiteralPath $manager)) {
  throw "未找到 ssh_config_manager.py：$manager"
}

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
  $python = Get-Command py -ErrorAction SilentlyContinue
}
if (-not $python) {
  throw "未找到 Python（python/py）。请先安装 Python，并确保可在 PATH 中调用。"
}

$jsonFiles = Get-ChildItem -LiteralPath $examplesDir -File -Filter *.json | Sort-Object Name
if (-not $jsonFiles) {
  Write-Host "未找到示例 JSON（跳过）：$examplesDir"
  exit 0
}

$failed = New-Object System.Collections.Generic.List[string]

foreach ($file in $jsonFiles) {
  Write-Host "校验：$($file.Name)"

  $args = @($manager, 'validate', $file.FullName)
  if ($StrictMetadata) {
    $args += '--strict-metadata'
  }

  & $python @args | Write-Host
  if ($LASTEXITCODE -ne 0) {
    $failed.Add($file.Name) | Out-Null
  }
}

if ($failed.Count -gt 0) {
  Write-Host "示例冒烟测试失败：$($failed.Count) 个文件"
  $failed | ForEach-Object { Write-Host "  - $_" }
  exit 1
}

Write-Host "示例冒烟测试通过：$($jsonFiles.Count) 个文件"
exit 0

