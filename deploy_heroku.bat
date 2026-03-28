@echo off
echo 🚀 Deploying Farm Management System to Heroku...
echo.

REM Check if Heroku CLI is installed
heroku --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Heroku CLI is not installed.
    echo Please install Heroku CLI from: https://devcenter.heroku.com/articles/heroku-cli
    pause
    exit /b 1
)

REM Check if git is initialized
if not exist .git (
    echo Initializing git repository...
    git init
    git add .
    git commit -m "Initial commit"
)

REM Ask for app name
set /p APP_NAME="Enter your Heroku app name (or press Enter for auto-generated): "

if "%APP_NAME%"=="" (
    echo Creating Heroku app with auto-generated name...
    heroku create
) else (
    echo Creating Heroku app: %APP_NAME%
    heroku create %APP_NAME%
)

echo.
echo 📝 Setting up environment variables...

REM Generate a random secret key
for /f "delims=" %%i in ('powershell -command "$bytes = [System.Text.Encoding]::UTF8.GetBytes((New-Guid).ToString()); [System.Convert]::ToBase64String($bytes)"') do set SECRET_KEY=%%i

heroku config:set SECRET_KEY=%SECRET_KEY%

echo ✅ Set SECRET_KEY
echo.

echo 🗄️ Setting up database...
heroku addons:create heroku-postgresql:hobby-dev
echo ✅ Added PostgreSQL database
echo.

echo 📤 Deploying to Heroku...
git add .
git commit -m "Ready for production deployment"
git push heroku main

echo.
echo 🎉 Deployment completed!
echo.
heroku open

echo.
echo 📋 Useful Heroku commands:
echo - View logs: heroku logs --tail
echo - Open app: heroku open
echo - View config: heroku config
echo - Scale dynos: heroku ps:scale web=1
echo.
pause