if ($IsWindows)
{
  .\venv\Scripts\activate.ps1
  python src\main.py
}
elseif ($IsLinux -or $IsMacOS)
{
  ./venv/bin/activate.ps1
  python3 src/main.py
}
