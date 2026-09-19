# Instalace skillů PRAKTIK-AI do Claude Code (karta Code v aplikaci Claude Desktop)
# Spuštění: klikněte pravým na soubor -> Spustit v PowerShellu,
#           nebo v PowerShellu:  powershell -ExecutionPolicy Bypass -File .\install_skills.ps1
# Skript zkopíruje složky ze .\skills\ do %USERPROFILE%\.claude\skills\ (existující verze přepíše).

$ErrorActionPreference = "Stop"
$src = Join-Path $PSScriptRoot "..\skills"
$dst = Join-Path $env:USERPROFILE ".claude\skills"

if (-not (Test-Path $src)) { Write-Host "Nenalezena slozka skills vedle tohoto skriptu: $src"; exit 1 }
New-Item -ItemType Directory -Force -Path $dst | Out-Null

Get-ChildItem -Path $src -Directory | ForEach-Object {
    $target = Join-Path $dst $_.Name
    if (Test-Path $target) { Remove-Item -Recurse -Force $target }
    Copy-Item -Recurse -Path $_.FullName -Destination $target
    Write-Host ("Nainstalovan skill: " + $_.Name)
}

Write-Host ""
Write-Host "Hotovo. V karte Code v Claude Desktop napiste /praktik (nebo /praktik-kurz, /praktik-rozhovor, /praktik-qa, /praktik-export)."
Write-Host "Pokud mate Claude Code otevreny, restartujte relaci, aby se skilly nacetly."
