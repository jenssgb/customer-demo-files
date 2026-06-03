# Zava Top Microsoft 365 Copilot Demo

A complete, customer-ready Microsoft 365 Copilot demo based on Microsoft's fictional company **Zava**. The goal is a universal end-to-end scenario in the style of the premium KN and Vaillant runbooks: business story, live prompts, realistic demo files, Office artifacts, public download, and a one-line setup command.

## Goal

This demo shows, in 30 to 45 minutes, how Microsoft 365 Copilot turns a scattered business signal into an executive-ready decision. It also includes an optional 60-minute **Ultimate Track** that folds in the strongest patterns from the KN, Vaillant, BPW, Copilot Chat Sidebar, Excel Agent Mode, M365 Agents, Analyst agent + Copilot in Excel, and Legal Agent demo packages.

1. Copilot Chat identifies the rush-order context from email, meeting notes, memo, and briefing files.
2. Microsoft 365 Copilot Analyst agent evaluates feasibility, bottlenecks, and price floor.
3. Excel analyzes inventory, capacity, margin, and risk in a prepared workbook.
4. Outlook drafts a customer response with explicit conditions.
5. Word creates an operational execution plan.
6. PowerPoint turns the decision into an executive story.
7. Agent Builder turns the manual flow into a reusable Order Desk agent.

Optional Ultimate Track modules:

8. Researcher creates a market, supplier, and event-readiness brief for the rush order.
9. Analyst or code interpreter performs a deeper scenario analysis from the workbook and CSV files.
10. Teams Facilitator captures the war-room meeting, tracks decisions, and turns discussion into actions.
11. Teams Interpreter demonstrates multilingual executive collaboration for global launch stakeholders.
12. Prompt Coach, Writing Coach, Idea Coach, and Visual Creator sharpen prompts, messages, and launch concepts.
13. Copilot Studio or Foundry becomes the pro-developer / low-code extension path when declarative Agent Builder is not enough.
14. Finance month-end close uses SAP actuals and TM1 forecast data to produce variance analysis, close controls, and CFO commentary.
15. Legal Agent in Word uses Word, Legal Agent if available, and Copilot Chat fallback to review a vendor agreement against a playbook.

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
| `data/Zava_Rush_Order_Context.docx` | Business context for Chat, Word, and PowerPoint |
| `data/Zava_Inventory_Snapshot.csv` | Inventory data for analysis and charts |
| `data/Zava_Order_Intake.csv` | Multiple rush-order requests for agent test cases |
| `data/Zava_Risk_Register.csv` | Risk register with owners and mitigations |
| `data/Zava_Pricing_Assumptions.csv` | Price-floor and margin assumptions |
| `data/Zava_Email_Thread.docx` | Email-thread context for Outlook and Copilot Chat |
| `data/Zava_Launch_Brief.docx` | Product and campaign context |
| `data/Zava_Meeting_Transcript.docx` | Meeting context and action items |
| `data/Zava_Executive_Decision_Memo.docx` | COO decision memo |
| `data/Zava_Agent_Builder_Brief.docx` | Agent Builder instructions and guardrails |
| `data/Zava_Copilot_Notebook_Setup.docx` | Microsoft 365 Copilot Notebooks setup guide and reference list |
| `data/finance-close/` | SAP actuals, TM1 budget/forecast, variance flat table, and mapping rules for the month-end close extension |
| `data/legal-review/` | Contract, legal playbook, and counterparty memo for the Word Legal Agent extension |
| `Deploy-Zava-Demo-Content.ps1` | Upload script for the CDX OneDrive or SharePoint demo folder |

Note: The PromptPrompter script and this README remain Markdown because they are tooling and documentation files. The demo grounding data in `data/` is now Word, Excel, CSV, or PowerPoint friendly; no Markdown files are used as Copilot grounding data.

## Microsoft Learn MCP Feature Matrix

Status: June 3, 2026. Verified with Microsoft Learn MCP Search and Fetch. Scenario labels use visible product, feature, or agent names; Work IQ is grounding context, not a live scenario title.

| Feature | Current capability | Limits and requirements | Demo implication | Source |
| --- | --- | --- | --- | --- |
| Copilot Chat and file upload | Secure AI chat with web grounding, file upload, Copilot Pages, image generation, and agents. | Without a Microsoft 365 Copilot add-on license, Copilot Chat is not automatically grounded in Microsoft Graph data. Organizational context must be uploaded, opened in supported apps, or provided through an agent. | Upload or reference the Zava files explicitly. | https://learn.microsoft.com/copilot/overview |
| Enterprise Data Protection | Prompts and responses for Entra-signed-in users are covered by DPA and Product Terms; access controls and policies apply depending on the plan. | Web queries and Anthropic-based capabilities have additional data-handling notes. Do not overstate compliance coverage. | Position security clearly and avoid blanket compliance claims. | https://learn.microsoft.com/microsoft-365/copilot/enterprise-data-protection |
| Excel Edit with Copilot | Users can edit workbooks through chat, including tables, charts, PivotTables, and formulas. | Formerly Agent Mode; availability depends on license, client, rollout, and tenant configuration. | Keep the prepared workbook ready; use Copilot Chat with XLSX upload as backup. | https://learn.microsoft.com/microsoft-365/copilot/release-notes |
| Word, Excel, and PowerPoint Agents | Create Office files directly from Copilot Chat; licensed users can work with organizational data through Work IQ. | Anthropic models must be enabled; region, tenant, government cloud, and sovereign cloud restrictions apply. | Treat as an optional wow moment; seed files are the backup path. | https://learn.microsoft.com/microsoft-365/copilot/wordexcelppt-agents |
| Agent Builder | Build declarative agents with natural language, add knowledge sources, test, and share. | Not available on mobile; complex actions should move to Copilot Studio; admin controls and known limitations apply. | Build the Zava Order Desk as a declarative agent and do not promise external actions. | https://learn.microsoft.com/microsoft-365/copilot/extensibility/agent-builder |
| Researcher and Analyst | First-party Microsoft experiences available from Copilot Chat Tools for research and analysis tasks. Researcher and Analyst are Microsoft-installed experiences and are governed differently from normal custom agents. | Built-in agents such as Researcher and Analyst are not available in GCC, GCCH, or DoD. Availability and tenant rollout can vary. | Use as optional premium moments. Keep the normal Copilot Chat and workbook prompts as backup. | https://learn.microsoft.com/training/modules/explore-prebuilt-microsoft-365-copilot-agents/ |
| Teams Facilitator | Provides collaborative real-time notes, AI-powered Q&A, visual timeline markers, Teams Rooms support, mobile capture, and meeting interaction by mentioning Facilitator. | Requires Microsoft 365 Copilot and Teams licensing. Some capabilities, including Planner task tracking and Word or Loop drafting, are public preview. Not supported in 1:1 chats, group chats, or external meetings. | Use for a Zava war-room meeting only when the tenant and meeting policy are ready. Otherwise show the transcript file and explain the live pattern. | https://learn.microsoft.com/microsoftteams/facilitator-teams |
| Teams Interpreter | Real-time speech-to-speech translation in Teams meetings, with supported spoken and listening languages including English, German, French, Spanish, Italian, Portuguese, Japanese, Korean, and Mandarin. | Requires eligible Microsoft 365 base license, Teams license, and Microsoft 365 Copilot license. 20 hours per user per month are included, subject to capacity. Not supported for town halls, webinars, Teams free, unscheduled 1:1 calls, or Teams Rooms scheduled meetings. | Use as an optional global-leadership moment for the Zava COO, Singapore logistics, and German production stakeholders. | https://learn.microsoft.com/microsoftteams/interpreter-agent-teams |
| Prompt Coach, Writing Coach, Idea Coach, Visual Creator | Prebuilt Microsoft 365 Copilot agents help improve prompts, writing, ideation, and visual concepts. | Availability can depend on tenant rollout, licensing, and admin controls. Do not position these as custom business-process automation. | Use as short polish moments: improve the customer prompt, sharpen the response, brainstorm mitigation options, or create a campaign visual concept. | https://learn.microsoft.com/training/modules/explore-prebuilt-microsoft-365-copilot-agents/ |
| Copilot Studio and advanced actions | Use Copilot Studio when the scenario requires actions, external systems, richer orchestration, or more complex agent capabilities than Agent Builder. | Requires the right Power Platform, Copilot Studio, billing, governance, environment, and admin configuration. | Position as the escalation path from a declarative Zava Order Desk agent to a production-grade fulfillment agent. | https://learn.microsoft.com/microsoft-365/copilot/extensibility/agent-builder |
| Microsoft 365 Copilot Notebooks | Secure AI-powered workspace to gather, synthesize, and act on organizational content for structured problem solving; supports references from communications and files, insights, audio summaries, drafts, and collaboration through Copilot Pages. | Availability depends on tenant rollout, licensing, and client experience. | Use as the persistent executive decision room after the Chat and Office moments; use Copilot Pages as backup. | https://learn.microsoft.com/office365/servicedescriptions/office-365-platform-service-description/microsoft-365-copilot#feature-availability |

## Demo Files One-Liner

The public demo repository contains the `Zava-M365-Copilot-Universal/` folder. This one-liner copies the complete package to the demo VM desktop:

```powershell
$d=[Environment]::GetFolderPath('Desktop');$z="$env:TEMP\zava.zip";$t="$env:TEMP\zava";iwr 'https://github.com/jenssgb/customer-demo-files/archive/refs/heads/main.zip' -OutFile $z;ri "$d\ZAVA-Demo",$t -r -fo -ea 0;Expand-Archive $z $t -Force;mv "$t\customer-demo-files-main\Zava-M365-Copilot-Universal" "$d\ZAVA-Demo";ri $z,$t -r -fo;Start-Process msedge "$d\ZAVA-Demo\Zava-M365-Copilot-Universal-Briefing.html";ii "$d\ZAVA-Demo"
```

## Presenter Setup

1. Copy the demo files to the desktop with the one-liner.
2. Place the `ZAVA-Demo` folder in OneDrive or SharePoint, or upload individual files directly in Copilot Chat.
3. Open Microsoft 365 Copilot Chat: https://m365copilot.com
4. Open `Zava_Order_Analysis.xlsx` in Excel for web or desktop.
5. Use the email thread or reply prompt for the Outlook section.
6. Open the Word and PowerPoint seed files for Office Copilot or Word, Excel, and PowerPoint Agents.
7. For the Notebook module, create a Microsoft 365 Copilot Notebook named `Zava Executive Decision Room` and use `data/Zava_Copilot_Notebook_Setup.docx` as the source checklist.

## Demo Arc

| Segment | Duration | Core message |
| --- | ---: | --- |
| Microsoft 365 Copilot Chat | 6 min | Copilot identifies the real decision from email, meeting notes, memo, and briefing files. |
| Microsoft 365 Copilot Analyst agent | 6 min | Analyst evaluates feasibility, bottlenecks, price floor, and conditions. Backup: Copilot Chat or Copilot in Excel. |
| Copilot in Excel | 8 min | Excel and Copilot turn raw data into a reliable fulfillment view. |
| Copilot in Outlook and Copilot in Word | 7 min | Copilot in Outlook and Copilot in Word turn the decision into customer communication and an operations plan. |
| Copilot in PowerPoint | 5 min | PowerPoint creates the executive narrative. |
| Agent Builder in Microsoft 365 Copilot | 5 min | Agent Builder turns the flow into a repeatable process. |
| Microsoft 365 Copilot Notebooks | 6 min | Notebooks becomes the persistent decision workspace for operations, finance, and legal context. |
| Analyst agent + Copilot in Excel | 7 min | SAP/TM1 variance data becomes close commentary, controls, and CFO actions. |
| Legal Agent in Word | 7 min | A vendor agreement becomes a risk matrix, playbook comparison, and redline proposal. |

## Ultimate Demo Coverage

This package now intentionally covers the complete top-demo surface area:

| Track | Demo moments | Best source package reused |
| --- | --- | --- |
| Microsoft 365 Copilot Chat and Work IQ grounding | Situation brief, file upload, Copilot Pages, Edge-style sidebar backup | Copilot Chat Sidebar, KN Work IQ |
| Analyst agent and Copilot in Excel | Microsoft 365 Copilot Analyst agent, Copilot in Excel, Python/code-interpreter style analysis backup | Excel Agent Mode, KN Analyst Agent |
| Copilot in Word, Excel, PowerPoint, and Outlook | Word, Excel, and PowerPoint seed files plus Office Agent alternatives | BPW Cowork and Word, Excel, and PowerPoint Agents |
| Meeting intelligence | War-room transcript, Teams Facilitator optional live path, Interpreter optional global meeting path | KN executive showcase, M365 Agents |
| Agent Builder in Microsoft 365 Copilot | Agent Builder baseline, Copilot Studio escalation path, Foundry/pro-code positioning | Agent Builder E2E, KN Foundry Sentinel |
| Microsoft 365 Copilot Notebooks | Microsoft 365 Copilot Notebooks setup, reference collection, decision map, COO briefing | New Zava module |
| Analyst agent + Copilot in Excel | SAP actuals vs. TM1 forecast, variance analysis, close controls, CFO commentary | SAP/TM1 Month-End Close |
| Legal Agent in Word | Word contract summary, Legal Agent path, playbook comparison, redline fallback | Legal Agent Word |

Presenter rule: show only the modules available in the tenant. For anything preview-gated, admin-gated, region-limited, or model-provider-dependent, use the included seed files and transcripts as the backup path.
