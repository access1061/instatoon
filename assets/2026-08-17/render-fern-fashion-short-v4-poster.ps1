param(
    [string]$Background = "fern-fashion-magazine-9x16-source.png",
    [string]$Audio = "fern_fashion_0817_clean.wav",
    [string]$Subtitle = "fern-fashion-short-v4-poster.ass",
    [string]$Output = "fern-fashion-short-v4-poster-9x16.mp4"
)

$ErrorActionPreference = "Stop"
$assetDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location $assetDir

try {
    Write-Host "Rendering Fern Fashion Short V4 (Refer1 Poster Style)..."
    $filter = "[0:v]scale=1080:1920," +
        "zoompan=z='1+0.020*on/239':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+6*on/239':d=240:s=1080x1920:fps=30," +
        "drawbox=x='if(between(t,3.72,4.25),(t-3.72)*2600-300,-1000)':y=0:w=180:h=1920:color=0x9A6BD4@0.12:t=fill," +
        "noise=alls=2:allf=t+u," +
        "subtitles=${Subtitle}:fontsdir='C\:/Windows/Fonts'," +
        "fade=t=in:st=0:d=0.20,fade=t=out:st=7.65:d=0.35,format=yuv420p[v]"

    & ffmpeg -y `
        -loop 1 -framerate 30 -i $Background `
        -i $Audio `
        -filter_complex $filter `
        -map "[v]" -map 1:a `
        -t 8 -r 30 `
        -c:v libx264 -preset medium -crf 18 `
        -c:a aac -b:a 192k `
        -movflags +faststart `
        $Output

    if ($LASTEXITCODE -ne 0) {
        throw "ffmpeg render failed with exit code $LASTEXITCODE"
    }

    Write-Host "Generating QA snapshots for V4..."
    & ffmpeg -y -ss 00:00:02.500 -i $Output -vframes 1 qa-v4-01.png
    & ffmpeg -y -ss 00:00:04.000 -i $Output -vframes 1 qa-v4-02.png
    & ffmpeg -y -ss 00:00:06.500 -i $Output -vframes 1 qa-v4-03.png

    Write-Host "Done! Output: $Output"
}
finally {
    Pop-Location
}
