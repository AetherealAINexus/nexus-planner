@echo off
setlocal

echo 🚀 Bootstrapping Nexus Ship...

:: Set Python executable (change if needed)
set PYTHON_EXE=python

:: Create venv if it doesn't exist
if not exist "venv" (
    echo 🔵 Creating virtual environment...
    %PYTHON_EXE% -m venv venv
)

:: Activate venv
echo 🟢 Activating virtual environment...
call venv\Scripts\activate.bat

:: Install requirements
echo 📦 Installing dependencies...
pip install --no-cache-dir -r requirements.txt

:: Launch the ship app
echo 🚀 Launching ship core...
uvicorn run:app --host 0.0.0.0 --port 8080

endlocal
pause
