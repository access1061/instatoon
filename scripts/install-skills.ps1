$ErrorActionPreference = "Stop"

$workspace = Split-Path -Parent $PSScriptRoot
$skillsRoot = Join-Path $workspace "skills"
$targetRoot = Join-Path $env:USERPROFILE ".codex\skills"

$skills = @(
    "colored-insta-toon",
    "flat-illustration",
    "handdrawn-illustrations",
    "handdrawn-illustrations2",
    "handdrawn-illustrations3",
    "fantasy-party-insta-toon",
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

    New-Item -ItemType Directory -Force $target | Out-Null
    Get-ChildItem -LiteralPath $source -Force | Copy-Item -Destination $target -Recurse -Force
    Write-Host "Installed $skill -> $target"
}

Write-Host "Done."
