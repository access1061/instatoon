$ErrorActionPreference = "Stop"

$workspace = Split-Path -Parent $PSScriptRoot
$skillsRoot = Join-Path $workspace "skills"
$targetRoot = Join-Path $env:USERPROFILE ".codex\skills"

$skills = @(
    "handdrawn-illustrations",
    "handdrawn-illustrations2",
    "handdrawn-illustrations3",
    "pixel-modern-insta-toon",
    "git-account-switch"
)

New-Item -ItemType Directory -Force $targetRoot | Out-Null

foreach ($skill in $skills) {
    $source = Join-Path $skillsRoot $skill
    $target = Join-Path $targetRoot $skill

    if (-not (Test-Path -LiteralPath $source)) {
        throw "Missing skill source: $source"
    }

    Copy-Item -LiteralPath $source -Destination $target -Recurse -Force
    Write-Host "Installed $skill -> $target"
}

Write-Host "Done."
