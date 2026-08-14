# Instala videos-tienda en ~/.claude/skills y revisa dependencias.
#   .\install.ps1
$ErrorActionPreference = "Stop"

$origen  = $PSScriptRoot
$destino = Join-Path $HOME ".claude\skills\videos-tienda"

if ($origen -ne $destino) {
    New-Item -ItemType Directory -Force $destino | Out-Null
    foreach ($item in @("SKILL.md", "README.md", "LICENSE", "requirements.txt")) {
        $ruta = Join-Path $origen $item
        if (Test-Path $ruta) { Copy-Item $ruta $destino -Force }
    }
    foreach ($carpeta in @("scripts", "references", "assets")) {
        $ruta = Join-Path $origen $carpeta
        if (Test-Path $ruta) {
            Copy-Item $ruta $destino -Recurse -Force
        }
    }
    Write-Host "instalada en $destino"
} else {
    Write-Host "ya estas en la carpeta de skills: $destino"
}

Write-Host "`n== Dependencias =="

function Revisa($nombre, $comando, $obligatorio, $comoInstalar) {
    if (Get-Command $comando -ErrorAction SilentlyContinue) {
        Write-Host ("  {0,-16} ok" -f $nombre)
    } elseif ($obligatorio) {
        Write-Host ("  {0,-16} FALTA (obligatorio) -> {1}" -f $nombre, $comoInstalar) -ForegroundColor Red
    } else {
        Write-Host ("  {0,-16} no instalado -> {1}" -f $nombre, $comoInstalar) -ForegroundColor Yellow
    }
}

Revisa "FFmpeg"  "ffmpeg"  $true  "winget install Gyan.FFmpeg"
Revisa "Python"  "python"  $true  "https://python.org"

$py = (Get-Command python -ErrorAction SilentlyContinue)
if ($py) {
    $whisper = & python -c "import importlib.util as u; print(bool(u.find_spec('faster_whisper')))" 2>$null
    if ($whisper -eq "True") {
        Write-Host "  faster-whisper   ok"
    } else {
        Write-Host "  faster-whisper   no instalado -> pip install faster-whisper (solo para subtitulos automaticos)" -ForegroundColor Yellow
    }
    $cv = & python -c "import importlib.util as u; print(bool(u.find_spec('cv2')))" 2>$null
    if ($cv -eq "True") {
        Write-Host "  opencv           ok"
    } else {
        Write-Host "  opencv           no instalado -> pip install opencv-python (mejora el reencuadre)" -ForegroundColor Yellow
    }
}

if (Get-Command ffmpeg -ErrorAction SilentlyContinue) {
    $encoders = & ffmpeg -hide_banner -encoders 2>&1 | Select-String "h264_nvenc"
    if ($encoders) { Write-Host "  GPU NVENC        disponible (render rapido)" }
    else { Write-Host "  GPU NVENC        no disponible (se usa CPU)" -ForegroundColor Yellow }
}

Write-Host "`nListo. Abre Claude Code y pide por ejemplo: 'hazme un reel con estas fotos'."
