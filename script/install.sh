echo "Setting up your environment..."
cd frontend && npm install && cd ../backend && python -m venv venv && source venv/Scripts/activate && python -m pip install -r requirements.txt && deactivate && cd ..
echo "Done!"
