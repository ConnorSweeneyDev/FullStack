if ($IsWindows) { python src\main.py }
elseif ($IsLinux -or $IsMacOS) { python3 src/main.py }
