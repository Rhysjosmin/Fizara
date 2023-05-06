start "FrontEnd" cmd /c "venv\Scripts\python.exe -m http.server"
start "Server" cmd /c "venv\Scripts\activate.bat && py Server\app.py"

start chrome http://127.0.0.1:5000
start chrome http://127.0.0.1:8000
