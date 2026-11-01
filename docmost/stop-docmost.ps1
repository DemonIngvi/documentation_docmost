# Останавливает контейнеры Docmost (данные сохраняются) и снимает удержание WSL.
wsl.exe -d Ubuntu --cd /mnt/d/documentation/docmost -- docker compose stop
Get-CimInstance Win32_Process -Filter "Name='wsl.exe'" |
    Where-Object { $_.CommandLine -match 'DOCMOST_KEEPALIVE' } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
