Write-Host "Setting up your environment..."
cd frontend && npm install && cd ..\backend && python -m venv venv && .\venv\Scripts\activate.ps1 && python -m pip install -r requirements.txt && deactivate && cd ..
Write-Host "Done!"
