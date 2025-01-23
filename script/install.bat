@ECHO OFF

ECHO Setting up your environment...
cd frontend && npm install && cd ..\backend && python -m venv venv && venv\Scripts\activate.bat && python -m pip install -r requirements.txt && deactivate && cd ..
ECHO Done!
