$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$paseoCli = Join-Path $projectRoot '.tools/paseo/node_modules/.bin/paseo.cmd'
if (-not (Test-Path -LiteralPath $paseoCli)) {
    throw 'Run: npm.cmd install --prefix .tools/paseo @getpaseo/cli --no-audit --no-fund'
}
$env:PATH = (Split-Path -Parent $paseoCli) + ';' + $env:PATH
if (-not $env:PASEO_HOME -and -not $env:PASEO_HOST -and $args -notcontains '--home' -and $args -notcontains '--host') {
    $env:PASEO_HOME = Join-Path $projectRoot '.paseo-local'
}
$paseoEntry = Join-Path $projectRoot '.tools/paseo/node_modules/@getpaseo/cli/bin/paseo'
& node $paseoEntry @args
exit $LASTEXITCODE
