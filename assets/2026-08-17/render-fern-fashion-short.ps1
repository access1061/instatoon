param(
    [string]$Background = "fern-fashion-magazine-9x16-source.png",
    [string]$Audio = "fern_fashion_0817_clean.wav",
    [string]$Subtitle = "fern-fashion-short.ass",
    [string]$Output = "fern-fashion-short-9x16.mp4"
)

$ErrorActionPreference = "Stop"
$assetDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location $assetDir

try {
    $filter = "[0:v]scale=1080:1920," +
        "zoompan=z='1+0.025*on/239':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+10*on/239':d=240:s=1080x1920:fps=30," +
        "drawbox=x='if(between(t,3.72,4.32),(t-3.72)*2300-300,-1000)':y=0:w=180:h=1920:color=0x8D62C9@0.10:t=fill," +
        "noise=alls=2:allf=t+u," +
        "subtitles=${Subtitle}:fontsdir='C\:/Windows/Fonts'," +
        "fade=t=in:st=0:d=0.25,fade=t=out:st=7.65:d=0.35,format=yuv420p[v]"

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
}
finally {
    Pop-Location
}

