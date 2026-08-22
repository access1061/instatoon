$ErrorActionPreference = "Stop"

$tools = @("node", "npm", "ffmpeg", "ffprobe")
foreach ($tool in $tools) {
    $found = Get-Command $tool -ErrorAction SilentlyContinue
    if ($found) {
        Write-Output ("OK   {0}: {1}" -f $tool, $found.Source)
    } else {
        Write-Output ("MISS {0}" -f $tool)
    }
}

$sharpRoot = Split-Path -Parent $PSScriptRoot
Push-Location $sharpRoot
try {
    & node -e "try{console.log('OK   sharp:',require('sharp').versions.sharp)}catch(e){console.log('MISS sharp (run npm install in skill folder)')}"
} finally {
    Pop-Location
}

