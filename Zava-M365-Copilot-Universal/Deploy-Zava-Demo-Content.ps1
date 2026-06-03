param(
    [string]$OneDriveUrl = "https://m365cpi98544940-my.sharepoint.com/personal/leilag_m365cpi98544940_onmicrosoft_com",
    [string]$TargetFolder = "Documents/Zava-M365-Copilot-Universal",
    [switch]$OpenBriefing
)

$ErrorActionPreference = "Stop"

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$dataPath = Join-Path $scriptRoot "data"
$briefing = Join-Path $scriptRoot "Zava-M365-Copilot-Universal-Briefing.html"
$promptFile = Join-Path $scriptRoot "Prompts\Zava-M365-Copilot-Universal-Demo.md"
$officeFiles = @(
    "Zava_Order_Analysis.xlsx",
    "Zava_Operations_Plan.docx",
    "Zava_Executive_Story.pptx"
) | ForEach-Object { Join-Path $scriptRoot $_ }

Connect-PnPOnline -Url $OneDriveUrl -ClientId "82e36ff4-c78b-4327-b6f0-dcc11b212a78" -Thumbprint "3065D8C303D949AEFA2F5495F9603E84A5015CAC" -Tenant "m365cpi98544940.onmicrosoft.com"

Resolve-PnPFolder -SiteRelativePath $TargetFolder | Out-Null

Get-ChildItem -Path $dataPath -File -Recurse | ForEach-Object {
    $relativeFolder = [System.IO.Path]::GetRelativePath($dataPath, $_.DirectoryName)
    $uploadFolder = $TargetFolder

    if ($relativeFolder -and $relativeFolder -ne ".") {
        $uploadFolder = ($TargetFolder.TrimEnd("/") + "/" + ($relativeFolder -replace "\\", "/"))
        Resolve-PnPFolder -SiteRelativePath $uploadFolder | Out-Null
    }

    Add-PnPFile -Path $_.FullName -Folder $uploadFolder | Out-Null
    Write-Host "Uploaded $($_.Name) to $uploadFolder"
}

$officeFiles | Where-Object { Test-Path $_ } | ForEach-Object {
    Add-PnPFile -Path $_ -Folder $TargetFolder | Out-Null
    Write-Host "Uploaded $(Split-Path $_ -Leaf) to $TargetFolder"
}

if (Test-Path $promptFile) {
    Add-PnPFile -Path $promptFile -Folder $TargetFolder | Out-Null
    Write-Host "Uploaded $(Split-Path $promptFile -Leaf) to $TargetFolder"
}

Add-PnPFile -Path $briefing -Folder $TargetFolder | Out-Null
Write-Host "Uploaded briefing to $TargetFolder"

if ($OpenBriefing) {
    Start-Process "msedge" $briefing
}
