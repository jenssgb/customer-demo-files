# Zava Top Microsoft 365 Copilot Demo

A complete, customer-ready Microsoft 365 Copilot demo based on Microsoft's fictional company **Zava**. The goal is a universal end-to-end scenario in the style of the premium KN and Vaillant runbooks: business story, live prompts, realistic demo files, Office artifacts, public download, and a one-line setup command.

## Goal

This demo shows, in 30 to 40 minutes, how Microsoft 365 Copilot turns a scattered business signal into an executive-ready decision:

1. Copilot Chat identifies the rush-order context from email, meeting notes, memo, and briefing files.
2. Analyst-style reasoning evaluates feasibility, bottlenecks, and price floor.
3. Excel analyzes inventory, capacity, margin, and risk in a prepared workbook.
4. Outlook drafts a customer response with explicit conditions.
5. Word creates an operational execution plan.
6. PowerPoint turns the decision into an executive story.
7. Agent Builder turns the manual flow into a reusable Order Desk agent.

## Zava Research Summary

Zava is a fictional Microsoft demo company in the retail and athletic-wear space. Microsoft Ignite describes Zava as a fictional athletic-wear company used in a demo about collaborative AI and product launch preparation.

This demo uses the strongest generic storyline: **Zava receives an urgent enterprise order for 20,000 smart launch shirts and must quickly validate inventory, production options, margin, operational risks, and the customer response.**

## Sources

- Microsoft Ignite Session `BRK284`: https://ignite.microsoft.com/en-US/sessions/BRK284
- Microsoft 365 Copilot Chat overview: https://learn.microsoft.com/copilot/overview
- Copilot Chat FAQ: https://learn.microsoft.com/copilot/faq
- Microsoft 365 Copilot overview: https://learn.microsoft.com/microsoft-365/copilot/microsoft-365-copilot-overview
- Word, Excel, and PowerPoint Agents: https://learn.microsoft.com/microsoft-365/copilot/wordexcelppt-agents
- Enterprise data protection: https://learn.microsoft.com/microsoft-365/copilot/enterprise-data-protection
- Agent Builder: https://learn.microsoft.com/microsoft-365/copilot/extensibility/agent-builder
- Microsoft 365 Copilot release notes: https://learn.microsoft.com/microsoft-365/copilot/release-notes

## Files

| File | Purpose |
| --- | --- |
| `Zava-M365-Copilot-Universal-Briefing.html` | Live runbook in the Clawpilot style with copy buttons |
| `Prompts/Zava-M365-Copilot-Universal-Demo.md` | PromptPrompter-ready demo script |
| `Zava_Order_Analysis.xlsx` | Excel dashboard with inventory, orders, pricing, risk register, and formulas |
| `Zava_Operations_Plan.docx` | Word seed document for the operations plan |
| `Zava_Executive_Story.pptx` | PowerPoint seed deck for the executive story |
| `data/Zava_Rush_Order_Context.md` | Business context for Chat, Word, and PowerPoint |
| `data/Zava_Inventory_Snapshot.csv` | Inventory data for analysis and charts |
| `data/Zava_Order_Intake.csv` | Multiple rush-order requests for agent test cases |
| `data/Zava_Risk_Register.csv` | Risk register with owners and mitigations |
| `data/Zava_Pricing_Assumptions.csv` | Price-floor and margin assumptions |
| `data/Zava_Email_Thread.html` | Email-thread context for Outlook and Copilot Chat |
| `data/Zava_Launch_Brief.md` | Product and campaign context |
| `data/Zava_Meeting_Transcript.md` | Meeting context and action items |
| `data/Zava_Executive_Decision_Memo.md` | COO decision memo |
| `data/Zava_Agent_Builder_Brief.md` | Agent Builder instructions and guardrails |
| `Deploy-Zava-Demo-Content.ps1` | Upload script for the CDX OneDrive or SharePoint demo folder |

## Microsoft Learn MCP Feature Matrix

Status: June 2, 2026. Verified with Microsoft Learn MCP Search and Fetch.

| Feature | Current capability | Limits and requirements | Demo implication | Source |
| --- | --- | --- | --- | --- |
| Copilot Chat and file upload | Secure AI chat with web grounding, file upload, Copilot Pages, image generation, and agents. | Without a Microsoft 365 Copilot add-on license, Copilot Chat is not automatically grounded in Microsoft Graph data. Organizational context must be uploaded, opened in supported apps, or provided through an agent. | Upload or reference the Zava files explicitly. | https://learn.microsoft.com/copilot/overview |
| Enterprise Data Protection | Prompts and responses for Entra-signed-in users are covered by DPA and Product Terms; access controls and policies apply depending on the plan. | Web queries and Anthropic-based capabilities have additional data-handling notes. Do not overstate compliance coverage. | Position security clearly and avoid blanket compliance claims. | https://learn.microsoft.com/microsoft-365/copilot/enterprise-data-protection |
| Excel Edit with Copilot | Users can edit workbooks through chat, including tables, charts, PivotTables, and formulas. | Formerly Agent Mode; availability depends on license, client, rollout, and tenant configuration. | Keep the prepared workbook ready; use Copilot Chat with XLSX upload as backup. | https://learn.microsoft.com/microsoft-365/copilot/release-notes |
| Word, Excel, and PowerPoint Agents | Create Office files directly from Copilot Chat; licensed users can work with organizational data through Work IQ. | Anthropic models must be enabled; region, tenant, government cloud, and sovereign cloud restrictions apply. | Treat as an optional wow moment; seed files are the backup path. | https://learn.microsoft.com/microsoft-365/copilot/wordexcelppt-agents |
| Agent Builder | Build declarative agents with natural language, add knowledge sources, test, and share. | Not available on mobile; complex actions should move to Copilot Studio; admin controls and known limitations apply. | Build the Zava Order Desk as a declarative agent and do not promise external actions. | https://learn.microsoft.com/microsoft-365/copilot/extensibility/agent-builder |

## Demo Files One-Liner

The public demo repository contains the `Zava-M365-Copilot-Universal/` folder. This one-liner copies the complete package to the demo VM desktop:

```powershell
$d=[Environment]::GetFolderPath('Desktop');$z="$env:TEMP\zava.zip";iwr 'https://github.com/jenssgb/customer-demo-files/archive/refs/heads/main.zip' -OutFile $z;ri "$d\ZAVA-Demo" -r -fo -ea 0;Expand-Archive $z "$env:TEMP\zava" -Force;mv "$env:TEMP\zava\customer-demo-files-main\Zava-M365-Copilot-Universal" "$d\ZAVA-Demo";ri $z,"$env:TEMP\zava" -r -fo;ii "$d\ZAVA-Demo"
```

## Presenter Setup

1. Copy the demo files to the desktop with the one-liner.
2. Place the `ZAVA-Demo` folder in OneDrive or SharePoint, or upload individual files directly in Copilot Chat.
3. Open Microsoft 365 Copilot Chat: https://m365copilot.com
4. Open `Zava_Order_Analysis.xlsx` in Excel for web or desktop.
5. Use the email thread or reply prompt for the Outlook section.
6. Open the Word and PowerPoint seed files for Office Copilot or Office Agents.

## Demo Arc

| Segment | Duration | Core message |
| --- | ---: | --- |
| Signal | 6 min | Copilot identifies the real decision from email, meeting notes, memo, and briefing files. |
| Reasoning | 6 min | Copilot evaluates feasibility, bottlenecks, price floor, and conditions. |
| Analysis | 8 min | Excel and Copilot turn raw data into a reliable fulfillment view. |
| Response | 7 min | Outlook and Word turn the decision into customer communication and an operations plan. |
| Story | 5 min | PowerPoint creates the executive narrative. |
| Scale | 5 min | Agent Builder turns the flow into a repeatable process. |
