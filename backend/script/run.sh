if [ "$OS" == "Windows_NT" ]; then
  sh venv/Scripts/activate
  python src/main.py
else
  source venv/bin/activate
  python3 src/main.py
fi
