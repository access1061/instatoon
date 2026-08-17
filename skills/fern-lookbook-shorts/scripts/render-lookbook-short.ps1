param(
    [Parameter(Mandatory=$true)][string]$Image,
    [Parameter(Mandatory=$true)][string]$Audio,
    [string]$Subtitle = "",
    [Parameter(Mandatory=$true)][string]$Output
)

$ErrorActionPreference = "Stop"
$duration = [double](& ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $Audio)
if ($LASTEXITCODE -ne 0 -or $duration -le 0) { throw "Could not measure audio duration." }
$frames = [math]::Ceiling($duration * 30)
$fadeOut = [math]::Max(0, $duration - 0.35)
$subtitleFilter = ""
if ($Subtitle) {
    $escaped = (Resolve-Path $Subtitle).Path.Replace('\','/').Replace(':','\:').Replace("'","\'")
    $subtitleFilter = ",subtitles='$escaped':fontsdir='C\:/Windows/Fonts'"
}

$filter = "scale=1120:1992:force_original_aspect_ratio=increase," +
    "crop=1080:1920," +
    "zoompan=z='1+0.035*on/${frames}':x='iw/2-(iw/zoom/2)':y='ih*0.34-(ih/zoom*0.34)':d=${frames}:s=1080x1920:fps=30," +
    "noise=alls=1.5:allf=t+u" + $subtitleFilter +
    ",fade=t=in:st=0:d=0.20,fade=t=out:st=${fadeOut}:d=0.35,setsar=1,format=yuv420p"

& ffmpeg -y -loop 1 -framerate 30 -i $Image -i $Audio -vf $filter `
    -map 0:v -map 1:a -t $duration -r 30 -c:v libx264 -preset medium -crf 18 `
    -c:a aac -b:a 192k -movflags +faststart $Output
if ($LASTEXITCODE -ne 0) { throw "FFmpeg render failed." }
