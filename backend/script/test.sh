if [ "$OS" == "Windows_NT" ]; then
  sh venv/Scripts/activate
  python -m src.test.main
else
  source venv/bin/activate
  python3 -m src.test.main
fi
