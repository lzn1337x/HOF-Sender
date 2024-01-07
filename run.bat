@echo off

REM Check if dependencies are installed
for /f "tokens=*" %%i in ('pip freeze ^| find /i "colorama"') do set colorama_installed=%%i

if not defined colorama_installed (
    REM Install dependencies
    echo Installing dependencies...
    pip install -r requirements.txt
    if %errorlevel% equ 0 (
        echo Dependencies installed successfully.
    ) else (
        echo Failed to install dependencies. Please check your internet connection and try again.
        exit /b 1
    )
) else (
    echo Dependencies are already installed.
)

REM Introduce a 1-second delay
timeout /nobreak /t 1 >nul

REM Run the script
echo Running the script...
timeout /nobreak /t 1 >nul
python send.py

REM Check the exit code of the Python script
if %errorlevel% equ 0 (
    REM Introduce a 1-second delay
    timeout /nobreak /t 1 >nul
    echo Script executed successfully.
) else (
    echo An error occurred while running the script. Please check the error.log file for details.
)

REM Pause to keep the command prompt window open (optional)
pause