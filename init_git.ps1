# Git 初始化并推送到 GitHub
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Git 初始化并推送到 GitHub" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查 Git 是否安装
try {
    $gitVersion = git --version
    Write-Host "[成功] 检测到 Git: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "[错误] 未检测到 Git，请先安装 Git" -ForegroundColor Red
    Write-Host "下载地址: https://git-scm.com/download/win" -ForegroundColor Yellow
    Read-Host "按 Enter 键退出"
    exit 1
}

Write-Host ""
Write-Host "[1/5] 初始化 Git 仓库..." -ForegroundColor Yellow
git init

Write-Host ""
Write-Host "[2/5] 添加远程仓库..." -ForegroundColor Yellow
git remote add origin https://github.com/1027552032/UI_Code.git
git remote -v

Write-Host ""
Write-Host "[3/5] 添加文件到暂存区..." -ForegroundColor Yellow
git add .

Write-Host ""
Write-Host "[4/5] 提交代码..." -ForegroundColor Yellow
git commit -m "feat: Add CI/CD with GitHub Actions"

Write-Host ""
Write-Host "[5/5] 推送到 GitHub..." -ForegroundColor Yellow
git branch -M main
git push -u origin main

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  完成！请检查 GitHub 仓库" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "后续步骤:" -ForegroundColor Yellow
Write-Host "1. 进入仓库 Settings -> Pages" -ForegroundColor White
Write-Host "2. Source 选择 'Deploy from a branch'" -ForegroundColor White
Write-Host "3. Branch 选择 'gh-pages' / '/(root)'" -ForegroundColor White
Write-Host "4. 点击 Save" -ForegroundColor White
Write-Host ""
Read-Host "按 Enter 键退出"
