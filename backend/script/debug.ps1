if ($IsWindows)
{
  .\venv\Scripts\activate.ps1
  python -m src.test.main
}
elseif ($IsLinux -or $IsMacOS)
{
  ./venv/bin/activate.ps1
  python3 -m src.test.main
}
