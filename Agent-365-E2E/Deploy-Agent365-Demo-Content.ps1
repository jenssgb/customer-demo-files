param(
    [string]$OneDriveUrl = "https://m365cpi98544940-my.sharepoint.com/personal/LeilaG_M365CPI98544940_onmicrosoft_com",
    [string]$Folder = "Documents/Agent-365-E2E-Demo"
)

$ErrorActionPreference = "Stop"

Connect-PnPOnline -Url $OneDriveUrl -ClientId "82e36ff4-c78b-4327-b6f0-dcc11b212a78" -Thumbprint "3065D8C303D949AEFA2F5495F9603E84A5015CAC" -Tenant "m365cpi98544940.onmicrosoft.com"

$files = @(
    "Agent-365-E2E-Briefing.html",
    "README.md",
    "Prompts/Agent-365-E2E-Demo.md",
    "data/AgentBuilder_OrderDesk_Brief.docx",
    "data/CopilotStudio_Fulfillment_Agent_Spec.docx",
    "data/Agent365_Governance_Checklist.docx",
    "data/Zava_Rush_Order_Context.docx",
    "data/Zava_Order_Intake.csv",
    "data/Agent365_Agent_Review_Register.csv"
)

foreach ($file in $files) {
    Add-PnPFile -Path (Join-Path $PSScriptRoot $file) -Folder $Folder | Out-Null
    Write-Host "Uploaded $file"
}

Write-Host "Agent 365 E2E demo content uploaded to $Folder"
