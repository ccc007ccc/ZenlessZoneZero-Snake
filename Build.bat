@echo off
REM 设置字符编码为 UTF-8
chcp 65001
cls

REM compile_WebServer.bat

REM 设置变量
set "SCRIPT_NAME=start.py"
set "EXE_NAME=zzz-snake.exe"
set "TEMP_DIR=temp_build"
set "OUTPUT_DIR=output"

REM 创建临时目录和输出目录
if not exist "%TEMP_DIR%" mkdir "%TEMP_DIR%"
if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

REM 安装必要的 Python 包
echo 正在安装必要的 Python 包...
pip install pyinstaller
pip install -r requirements.txt

REM 复制 Python 脚本到临时目录
copy "%SCRIPT_NAME%" "%TEMP_DIR%"

REM 切换到临时目录
cd "%TEMP_DIR%"

REM 使用 PyInstaller 编译脚本
echo 正在编译脚本...
pyinstaller -D --uac-admin --onefile --name "%EXE_NAME%" "%SCRIPT_NAME%" 

REM 将生成的 EXE 文件移动到输出目录
move "dist\%EXE_NAME%" "..\%OUTPUT_DIR%"

REM 切换回原始目录
cd ..

REM 清理临时文件
rmdir /s /q "%TEMP_DIR%"

echo 编译完成！executable 文件位于: %OUTPUT_DIR%\%EXE_NAME%

REM 暂停以查看输出
pause