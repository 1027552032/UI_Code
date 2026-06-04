@echo off
echo ========================================
echo   Git Init and Push to GitHub
echo ========================================
echo.

git --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git not found. Please install Git first.
    echo Download: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo [1/5] Initializing Git repo...
git init

echo.
echo [2/5] Adding remote origin...
git remote add origin https://github.com/1027552032/UI_Code.git
git remote -v

echo.
echo [3/5] Adding files to staging...
git add .

echo.
echo [4/5] Committing code...
git commit -m "feat: Add CI/CD with GitHub Actions"

echo.
echo [5/5] Pushing to GitHub...
git branch -M main
git push -u origin main

echo.
echo ========================================
echo   Done! Please check GitHub repo
echo ========================================
echo.
echo Next Steps:
echo 1. Go to repo Settings -> Pages
echo 2. Source: Deploy from a branch
echo 3. Branch: gh-pages / (root)
echo 4. Click Save
echo.
pause
