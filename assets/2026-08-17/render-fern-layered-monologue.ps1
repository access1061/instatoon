param(
    [string]$Background = "..\..\skills\fern-lookbook-shorts\assets\layers\background-1080x1920.png",
    [string]$Character = "..\..\skills\fern-lookbook-shorts\assets\layers\character-1080x1920.png",
    [string]$SideCharacter = "..\..\skills\fern-lookbook-shorts\assets\layers\character-side-profile-forward-staff-1080x1920.png",
    [string]$Overlay = "..\..\skills\fern-lookbook-shorts\assets\layers\overlay.png",
    [string]$Audio = "fern_lookbook_monologue_0817_clean.wav",
    [string]$Subtitle = "fern-lookbook-monologue-ja-natural.ass",
    [string]$Output = "fern-lookbook-front5-side5-profile-ja-9x16.mp4"
)

$ErrorActionPreference = "Stop"
$assetDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location $assetDir
try {
    $duration = [double](& ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $Audio)
    if ($LASTEXITCODE -ne 0 -or $duration -le 0) { throw "Could not measure audio duration." }
    $d = $duration.ToString('0.######', [Globalization.CultureInfo]::InvariantCulture)
    $sub = (Resolve-Path $Subtitle).Path.Replace('\','/').Replace(':','\:').Replace("'","\'")

    $filter = "[0:v]scale=1092:1942,crop=1080:1920:x='6*t/$d':y='11-6*t/$d',setsar=1[bg];" +
        "[1:v]format=rgba,fade=t=out:st=4.80:d=0.36:alpha=1[front];" +
        "[2:v]format=rgba,fade=t=in:st=4.80:d=0.36:alpha=1[side];" +
        "[bg][front]overlay=x='4*t/$d':y='-3*t/$d':format=auto[bf];" +
        "[bf][side]overlay=x='-3+3*t/$d':y='2-2*t/$d':format=auto[bfs];" +
        "[3:v]format=rgba[art];" +
        "[bfs][art]overlay=0:0:format=auto," +
        "drawbox=x='if(between(t,3.26,3.46),(t-3.26)*5400-1080,-2000)':y=610:w=1080:h=7:color=0x55327D@0.80:t=fill," +
        "drawbox=x='if(between(t,7.85,8.05),(t-7.85)*5400-1080,-2000)':y=1170:w=1080:h=7:color=0x184A9C@0.75:t=fill," +
        "subtitles='$sub':fontsdir='C\:/Windows/Fonts'," +
        "noise=alls=1.2:allf=t+u,fade=t=in:st=0:d=0.18,fade=t=out:st=9.62:d=0.34,setsar=1,format=yuv420p[v]"

    & ffmpeg -y `
        -loop 1 -framerate 30 -i $Background `
        -loop 1 -framerate 30 -i $Character `
        -loop 1 -framerate 30 -i $SideCharacter `
        -loop 1 -framerate 30 -i $Overlay `
        -i $Audio `
        -filter_complex $filter -map "[v]" -map 4:a `
        -t $d -r 30 -c:v libx264 -preset medium -crf 18 `
        -c:a aac -b:a 192k -movflags +faststart $Output
    if ($LASTEXITCODE -ne 0) { throw "FFmpeg render failed." }

    foreach ($item in @(@('2.0','qa-fern-profile-natural-01.png'), @('4.9','qa-fern-profile-natural-02.png'), @('5.3','qa-fern-profile-natural-03.png'), @('8.4','qa-fern-profile-natural-04.png'))) {
        & ffmpeg -y -v error -ss $item[0] -i $Output -frames:v 1 $item[1]
    }
} finally {
    Pop-Location
}
