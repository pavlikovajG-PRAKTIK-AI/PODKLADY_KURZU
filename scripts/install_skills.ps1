# Instalace skillu PRAKTIK-AI do Claude Code (karta Code v aplikaci Claude Desktop)
# Spusteni: dvojklik na Nainstalovat_skilly.cmd ve stejne slozce (funguje v libovolnem spravci souboru),
#           nebo v Pruzkumniku klik pravym na tento soubor -> Spustit v PowerShellu,
#           nebo primo v PowerShellu:  powershell -ExecutionPolicy Bypass -File .\install_skills.ps1
# Skript zkopiruje slozky ze ..\skills\ do %USERPROFILE%\.claude\skills\ (existujici verze prepise).
# Kdyz slozka skills chybi, rozbali zipy ze ..\zips\.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$src  = Join-Path $root "skills"
$zips = Join-Path $root "zips"
$dst  = Join-Path $env:USERPROFILE ".claude\skills"

New-Item -ItemType Directory -Force -Path $dst | Out-Null

if (Test-Path $src) {
    Get-ChildItem -Path $src -Directory | ForEach-Object {
        $target = Join-Path $dst $_.Name
        if (Test-Path $target) { Remove-Item -Recurse -Force $target }
        Copy-Item -Recurse -Path $_.FullName -Destination $target
        Write-Host ("Nainstalovan skill: " + $_.Name)
    }
}
elseif (Test-Path $zips) {
    Get-ChildItem -Path $zips -Filter *.zip | ForEach-Object {
        $name = $_.BaseName
        $target = Join-Path $dst $name
        if (Test-Path $target) { Remove-Item -Recurse -Force $target }
        Expand-Archive -Path $_.FullName -DestinationPath $dst -Force
        Write-Host ("Nainstalovan skill ze zipu: " + $name)
    }
}
else {
    Write-Host "Nenalezena slozka skills ani zips vedle slozky scripts: $root"
    exit 1
}

Write-Host ""
Write-Host "Hotovo. V karte Code v Claude Desktop napiste /praktik (nebo /praktik-kurz, /praktik-rozhovor, /praktik-qa, /praktik-export)."
Write-Host "Claude Code slozku se skilly sleduje, novou verzi zachyti i v uz bezici relaci. Kdyz se skill nenabidne, otevrete novou relaci."
