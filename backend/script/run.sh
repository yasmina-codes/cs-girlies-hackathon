if [ "$OS" == "Windows_NT" ]; then
  sh venv/Scripts/activate
  python -m src.prog.main
else
  source venv/bin/activate
  python3 -m src.prog.main
fi
