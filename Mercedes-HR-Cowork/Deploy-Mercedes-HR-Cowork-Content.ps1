#requires -Version 5.1
param(
    [string]$OneDriveUrl = "https://m365cpi98544940-my.sharepoint.com/personal/leilag_m365cpi98544940_onmicrosoft_com",
    [string]$TargetFolder = "Documents/Mercedes-HR-Cowork"
)

$ErrorActionPreference = "Stop"
$tenant = "m365cpi98544940.onmicrosoft.com"
$clientId = "82e36ff4-c78b-4327-b6f0-dcc11b212a78"
$thumbprint = "3065D8C303D949AEFA2F5495F9603E84A5015CAC"
$skillFolder = "Documents/Cowork/skills/mercedes-hr-delegation"

$contentFiles = @(
    "MBZ-MOCK-People-Transformation-Pulse.xlsx",
    "MBZ-MOCK-Executive-Transformation-Priorities.docx",
    "MBZ-MOCK-Onboarding-Cohort.xlsx",
    "MBZ-MOCK-Onboarding-Standards.docx"
)

try {
    Import-Module PnP.PowerShell -ErrorAction Stop
    Connect-PnPOnline -Url $OneDriveUrl -ClientId $clientId -Thumbprint $thumbprint -Tenant $tenant

    Resolve-PnPFolder -SiteRelativePath $TargetFolder | Out-Null
    foreach ($name in $contentFiles) {
        $path = Join-Path $PSScriptRoot $name
        if (-not (Test-Path $path)) {
            throw "Required demo file is missing: $path"
        }
        Add-PnPFile -Path $path -Folder $TargetFolder -NewFileName $name | Out-Null
        Write-Host "Uploaded $name"
    }

    Resolve-PnPFolder -SiteRelativePath $skillFolder | Out-Null
    $skillPath = Join-Path $PSScriptRoot "skills\mercedes-hr-delegation\SKILL.md"
    Add-PnPFile -Path $skillPath -Folder $skillFolder -NewFileName "SKILL.md" | Out-Null
    Write-Host "Installed custom skill at $skillFolder/SKILL.md"
    Write-Host "Mercedes HR Cowork demo content deployment complete."
}
finally {
    Disconnect-PnPOnline -ErrorAction SilentlyContinue
}
