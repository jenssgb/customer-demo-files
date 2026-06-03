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
14. Microsoft Agent 365 shows how IT observes, governs, and secures Agent Builder and Copilot Studio agents.
15. Finance month-end close uses SAP actuals and TM1 forecast data to produce variance analysis, close controls, and CFO commentary.
16. Legal Agent in Word uses Word, Legal Agent if available, and Copilot Chat fallback to review a vendor agreement against a playbook.

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
- Agent Builder knowledge sources: https://learn.microsoft.com/microsoft-365/copilot/extensibility/agent-builder-add-knowledge
- Microsoft 365 Copilot connectors overview: https://learn.microsoft.com/microsoft-365/copilot/extensibility/overview-copilot-connector
- Build your first custom Copilot connector: https://learn.microsoft.com/microsoft-365/copilot/extensibility/build-your-first-connector
- Copilot Studio MCP onboarding: https://learn.microsoft.com/microsoft-copilot-studio/mcp-add-existing-server-to-agent
- Add MCP tools to Copilot Studio agents: https://learn.microsoft.com/microsoft-copilot-studio/mcp-add-components-to-agent
- Manage Agent 365 tools and BYO MCP servers: https://learn.microsoft.com/microsoft-365/admin/manage/manage-tools-for-agent?view=o365-worldwide
- Microsoft Agent 365 overview: https://learn.microsoft.com/microsoft-agent-365/overview
- Copilot Studio and Agent 365: https://learn.microsoft.com/microsoft-agent-365/builder/overview
- Agent activity view: https://learn.microsoft.com/microsoft-agent-365/observe-agents-microsoft-365-copilot
- Manage Agent 365 agents: https://learn.microsoft.com/microsoft-agent-365/admin/manage-agents#view-available-agents
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
| `data/agent-365/AgentBuilder_OrderDesk_Brief.docx` | Agent Builder source brief for the Agent 365 E2E module |
| `data/agent-365/CopilotStudio_Fulfillment_Agent_Spec.docx` | Copilot Studio production-agent specification for the Agent 365 E2E module |
| `data/agent-365/Agent365_Governance_Checklist.docx` | Observe, govern, secure checklist for Agent 365 presenter and admin review |
| `data/agent-365/Agent365_Agent_Review_Register.csv` | Mock agent inventory and review register for Agent 365 backup evidence |
| `data/agent-365/Agent365_vs_PowerPlatform_Governance.csv` | Concrete objection-handling dataset: Power Platform Governance vs Agent 365 |
| `data/agent-365/AgentBuilder_Connector_MCP_Extension_Plan.csv` | Learn-verified matrix for Agent Builder knowledge, Copilot connectors, Copilot Studio MCP, and Agent 365 tool governance |
| `data/agent-365/Zava_Public_OrderSignals_MCP_Registration.json` | BYO MCP registration template for the Copilot Studio / Agent 365 tool-governance UI demo |
| `data/agent-365/Zava_Order_Intake.csv` | Agent Builder and Copilot Studio test orders for the Agent 365 E2E module |
| `data/agent-365/Zava_Rush_Order_Context.docx` | Business context for the Agent Builder agent in the Agent 365 E2E module |
| `data/finance-close/` | SAP actuals, TM1 budget/forecast, variance flat table, and mapping rules for the month-end close extension |
| `data/legal-review/` | Contract, legal playbook, and counterparty memo for the Word Legal Agent extension |
| `Deploy-Zava-Demo-Content.ps1` | Upload script for the CDX OneDrive or SharePoint demo folder |

Note: The PromptPrompter script and this README remain Markdown because they are tooling and documentation files. The demo grounding data in `data/` is now Word, Excel, CSV, or PowerPoint friendly; no Markdown files are used as Copilot grounding data.

## Microsoft Learn Feature Matrix

Status: June 3, 2026. Verified with Microsoft Learn documentation. Scenario labels use visible product, feature, or agent names; Work IQ is grounding context, not a live scenario title.

## Copilot License and Frontier Map

Use the HTML runbook tab **Copilot license map** for the presenter-ready view. Source of truth: Microsoft 365 Copilot Service Description for generally available / worldwide features, Copilot Chat FAQ for baseline Chat capabilities, and Microsoft Frontier / Agent 365 Learn pages for preview-gated items.

Key rule: call a feature **generally available** only when it is listed as available in the Microsoft 365 Copilot Service Description or release notes. Call a feature **Frontier / preview** when it requires Frontier enrollment, appears with `(Frontier)` in the Agent Store, depends on admin opt-in, Anthropic or other model approval, or is absent from the core Service Description.

Quick map as of June 3, 2026:

| Bucket | Examples | Presenter stance |
| --- | --- | --- |
| Microsoft 365 subscription baseline | Copilot Chat, web grounding, Pages, file upload, image generation, previous chats, agents | Included baseline; organizational grounding needs upload/open context/pay-as-you-go agent. |
| Microsoft 365 Copilot license | Work/web chat, Microsoft Graph grounding, Copilot app, Search, Notebooks, Office app Copilots, built-in/custom agents | Main customer-facing licensing story. |
| Generally available app experiences | Teams, Outlook, Word, Excel, PowerPoint, OneNote, Loop, Clipchamp, Whiteboard, OneDrive, SharePoint | Check government-cloud caveats before promising. |
| Generally available extensibility | SharePoint agents, declarative agents, Copilot connectors, Power Platform connectors, Purview, Viva Insights | Safe to position; production automation may need Copilot Studio or governance. |
| First-party Microsoft agents | Researcher and Analyst | GA / Microsoft-installed for licensed users; not available in GCC, GCCH, or DoD. Researcher GA release note: July 22, 2025. |
| Frontier / preview | Agent 365 agents with own identity, Shadow AI, Frontier agents, AI-enabled Cloud PCs, Legal Agent in Word when visible only through Frontier | Tenant/admin/user gated; always prepare Copilot Chat or Office Copilot fallback. |

| Feature | Current capability | Limits and requirements | Demo implication | Source |
| --- | --- | --- | --- | --- |
| Copilot Chat and file upload | Secure AI chat with web grounding, file upload, Copilot Pages, image generation, and agents. | Without a Microsoft 365 Copilot add-on license, Copilot Chat is not automatically grounded in Microsoft Graph data. Organizational context must be uploaded, opened in supported apps, or provided through an agent. | Upload or reference the Zava files explicitly. | https://learn.microsoft.com/copilot/overview |
| Enterprise Data Protection | Prompts and responses for Entra-signed-in users are covered by DPA and Product Terms; access controls and policies apply depending on the plan. | Web queries and Anthropic-based capabilities have additional data-handling notes. Do not overstate compliance coverage. | Position security clearly and avoid blanket compliance claims. | https://learn.microsoft.com/microsoft-365/copilot/enterprise-data-protection |
| Excel Edit with Copilot | Users can edit workbooks through chat, including tables, charts, PivotTables, and formulas. | Formerly Agent Mode; availability depends on license, client, rollout, and tenant configuration. | Keep the prepared workbook ready; use Copilot Chat with XLSX upload as backup. | https://learn.microsoft.com/microsoft-365/copilot/release-notes |
| Word, Excel, and PowerPoint Agents | Create Office files directly from Copilot Chat; licensed users can work with organizational data through Work IQ. | Anthropic models must be enabled; region, tenant, government cloud, and sovereign cloud restrictions apply. | Treat as an optional wow moment; seed files are the backup path. | https://learn.microsoft.com/microsoft-365/copilot/wordexcelppt-agents |
| Agent Builder | Build declarative agents with natural language, add knowledge sources, test, and share. | Not available on mobile; complex actions should move to Copilot Studio; admin controls and known limitations apply. | Build the Zava Order Desk as a declarative agent and do not promise external actions. | https://learn.microsoft.com/microsoft-365/copilot/extensibility/agent-builder |
| Agent Builder knowledge and Copilot connectors | Agent Builder can add public websites, SharePoint/OneDrive content, uploaded files, Teams chat URLs, and Microsoft 365 Copilot connectors enabled by the organization's admin. Copilot connectors can bring external enterprise content into Microsoft 365 Copilot and agent knowledge. | Public website URLs are limited to four URLs, two levels deep, without query parameters. Copilot connectors require admin setup, indexing/permissions, and tenant availability. Agent Builder consumes connector content as knowledge; complex tools/actions should move to Copilot Studio. | Show a Zava Supplier Signal Scout with public website knowledge as the live path and an admin-enabled GitHub/Copilot connector as the enterprise path. | https://learn.microsoft.com/microsoft-365/copilot/extensibility/agent-builder-add-knowledge |
| Copilot Studio MCP and Agent 365 tool governance | Copilot Studio can add MCP servers as tools. BYO MCP servers can be registered with Agent 365 for centralized approval, block/unblock, registry visibility, and observability. | BYO MCP server is preview. Microsoft Learn states supported client surfaces include Copilot Studio, VS Code, Claude Code, and GitHub Copilot CLI; Microsoft 365 Declarative Agents / Agent Builder are not yet supported for BYO MCP. | Use MCP as the production extension path after Agent Builder. Do not promise direct BYO MCP usage inside Agent Builder. | https://learn.microsoft.com/microsoft-365/admin/manage/manage-tools-for-agent?view=o365-worldwide |
| Researcher and Analyst | First-party Microsoft experiences available from Copilot Chat Tools for research and analysis tasks. Researcher and Analyst are Microsoft-installed experiences and are governed differently from normal custom agents. | Built-in agents such as Researcher and Analyst are not available in GCC, GCCH, or DoD. Availability and tenant rollout can vary. | Use as optional premium moments. Keep the normal Copilot Chat and workbook prompts as backup. | https://learn.microsoft.com/training/modules/explore-prebuilt-microsoft-365-copilot-agents/ |
| Teams Facilitator | Provides collaborative real-time notes, AI-powered Q&A, visual timeline markers, Teams Rooms support, mobile capture, and meeting interaction by mentioning Facilitator. | Requires Microsoft 365 Copilot and Teams licensing. Some capabilities, including Planner task tracking and Word or Loop drafting, are public preview. Not supported in 1:1 chats, group chats, or external meetings. | Use for a Zava war-room meeting only when the tenant and meeting policy are ready. Otherwise show the transcript file and explain the live pattern. | https://learn.microsoft.com/microsoftteams/facilitator-teams |
| Teams Interpreter | Real-time speech-to-speech translation in Teams meetings, with supported spoken and listening languages including English, German, French, Spanish, Italian, Portuguese, Japanese, Korean, and Mandarin. | Requires eligible Microsoft 365 base license, Teams license, and Microsoft 365 Copilot license. 20 hours per user per month are included, subject to capacity. Not supported for town halls, webinars, Teams free, unscheduled 1:1 calls, or Teams Rooms scheduled meetings. | Use as an optional global-leadership moment for the Zava COO, Singapore logistics, and German production stakeholders. | https://learn.microsoft.com/microsoftteams/interpreter-agent-teams |
| Prompt Coach, Writing Coach, Idea Coach, Visual Creator | Prebuilt Microsoft 365 Copilot agents help improve prompts, writing, ideation, and visual concepts. | Availability can depend on tenant rollout, licensing, and admin controls. Do not position these as custom business-process automation. | Use as short polish moments: improve the customer prompt, sharpen the response, brainstorm mitigation options, or create a campaign visual concept. | https://learn.microsoft.com/training/modules/explore-prebuilt-microsoft-365-copilot-agents/ |
| Copilot Studio and advanced actions | Use Copilot Studio when the scenario requires actions, external systems, richer orchestration, or more complex agent capabilities than Agent Builder. | Requires the right Power Platform, Copilot Studio, billing, governance, environment, and admin configuration. | Position as the escalation path from a declarative Zava Order Desk agent to a production-grade fulfillment agent. | https://learn.microsoft.com/microsoft-365/copilot/extensibility/agent-builder |
| Microsoft Agent 365 | Control plane to observe, govern, and secure agents. Provides centralized registry, visibility into adoption/activity/health, lifecycle governance, access/compliance guardrails, and security integrations with Entra, Purview, and Defender. Copilot Studio agents automatically appear in the registry and emit telemetry to Agent 365. | Agent 365 is commercially GA as of May 1, 2026, but some views, such as all-agents activity in Microsoft 365 Copilot, are preview, read-only, user-scoped, and retain activity for 30 days. At least one qualifying Agent 365 license is required to enable Agent 365. | Show Agent 365 after Agent Builder and Copilot Studio: registry, ownership, platform, connectors/tools, environment, activity, risk, and governance actions. If unavailable, use the Learn-verified matrix as the talk-track backup. | https://learn.microsoft.com/microsoft-agent-365/overview |
| Microsoft 365 Copilot Notebooks | Secure AI-powered workspace to gather, synthesize, and act on organizational content for structured problem solving; supports references from communications and files, insights, audio summaries, drafts, and collaboration through Copilot Pages. | Availability depends on tenant rollout, licensing, and client experience. | Use as the persistent executive decision room after the Chat and Office moments; use Copilot Pages as backup. | https://learn.microsoft.com/office365/servicedescriptions/office-365-platform-service-description/microsoft-365-copilot#feature-availability |

## Microsoft Agent 365 Demo Pattern

Agent 365 is not positioned as another assistant in the Zava story. It is the enterprise control plane that appears after the presenter has built or described both **Agent Builder in Microsoft 365 Copilot** and **Microsoft Copilot Studio** agents.

| Step | Product / capability | What to show | Backup path |
| --- | --- | --- | --- |
| 1 | Agent Builder in Microsoft 365 Copilot | Build the Zava Order Desk Agent from `data/agent-365/AgentBuilder_OrderDesk_Brief.docx` and `data/agent-365/Zava_Rush_Order_Context.docx`. | Use the prompt output as the build plan if authoring is unavailable. |
| 2 | Agent Builder test | Test order ZO-3102 from `data/agent-365/Zava_Order_Intake.csv` to prove the repeatable agent workflow. | Run in Copilot Chat with uploaded files if the built agent is not ready. |
| 3 | Admin extension lane for Agent Builder | As admin, show Microsoft 365 admin center > Settings > Search & intelligence > Data sources for Copilot connector readiness; as Preston, show Agent Builder > Knowledge where public URLs and admin-enabled Copilot connectors appear as knowledge sources. | Use `data/agent-365/AgentBuilder_Connector_MCP_Extension_Plan.csv` as the presenter checklist. Agent Builder consumes connector content as knowledge; it does not directly run MCP/API tools. |
| 4 | Copilot Studio MCP and Agent 365 tool governance | In Copilot Studio > Tools > Add a tool > Model Context Protocol, show the setup path for a production MCP/API tool. Then show Microsoft 365 admin center > Agents > Tools for approve/reject/block/unblock governance. | Use `data/agent-365/Zava_Public_OrderSignals_MCP_Registration.json`, `data/agent-365/AgentBuilder_Connector_MCP_Extension_Plan.csv`, and `data/agent-365/Agent365_Agent_Review_Register.csv` as non-secret backup evidence. |
| 5 | Microsoft Copilot Studio | Build or describe the Zava Fulfillment Escalation Agent with topics, actions, approvals, environment governance, analytics, and publish channels. | Use `data/agent-365/CopilotStudio_Fulfillment_Agent_Spec.docx` as the implementation blueprint. |
| 6 | Requested Copilot Studio agent | Microsoft 365 admin center > Agents > All agents > Requests. Review Data & tools, owner, actions, and publish scope. | Use `data/agent-365/Agent365_Agent_Review_Register.csv` if no pending request exists. |
| 7 | Power Platform Governance vs Agent 365 | Show that Power Platform Governance covers environments, connectors, DLP and maker controls, while Agent 365 adds agent-level registry, ownership, usage, activity, risk and lifecycle governance across supported agent platforms. | Use `data/agent-365/Agent365_vs_PowerPlatform_Governance.csv` as the objection-handling proof. |
| 8 | Microsoft Agent 365 registry | Microsoft 365 admin center > Agents > All agents / registry. Show inventory, owner, publisher, platform, environment, connectors/tools, and status. | If the UI is unavailable, state the tenant limitation and use the CSV register as backup evidence. |
| 9 | Microsoft Agent 365 activity / observability | Show activity, usage, tool invocation, or high-level admin signals where available. | State that all-agents activity view is preview, user-scoped, read-only, and 30-day retained. |
| 10 | Microsoft Agent 365 governance | Explain approve/publish, assign, block, reassign, delete, ownerless agent review, and audit readiness. | Do not click destructive actions live; explain the available controls. |
| 11 | Microsoft Agent 365 security and compliance | Tie the agent story to Entra identity/access, Purview audit/DLP, and Defender threat detection where available. | Keep this as a positioning close unless the tenant has configured views. |

### Power Platform Governance vs Agent 365 presenter stance

Power Platform Governance remains essential. It governs Power Platform environments, managed environments, makers, DLP/data policies, connector use, sharing, pipelines, insights and other Power Platform controls. Agent 365 is complementary: it governs agents as enterprise assets across supported Microsoft and connected agent platforms, including Agent Builder, Copilot Studio, SharePoint, Foundry, Agents Toolkit, Microsoft-built and some non-Microsoft agent sources. The strongest demo line is: Power Platform Governance answers "is this Copilot Studio environment and connector use allowed?" Agent 365 answers "what agents exist across the tenant, who owns them, who can use them, what are they doing, which ones are risky, and what lifecycle action should IT take?"

## Demo Files One-Liner

The public demo repository contains the `Zava-M365-Copilot-Universal/` folder. This one-liner copies the complete package to the demo VM desktop:

```powershell
$d=[Environment]::GetFolderPath('Desktop');$z="$env:TEMP\zava.zip";$t="$env:TEMP\zava";iwr 'https://github.com/jenssgb/customer-demo-files/archive/refs/heads/main.zip' -OutFile $z;ri "$d\ZAVA-Demo",$t -r -fo -ea 0;Expand-Archive $z $t -Force;mv "$t\customer-demo-files-main\Zava-M365-Copilot-Universal" "$d\ZAVA-Demo";ri $z,$t -r -fo;Start-Process msedge "$d\ZAVA-Demo\Zava-M365-Copilot-Universal-Briefing.html";ii "$d\ZAVA-Demo"
```

## Demo Identity Model

| Role | User | UPN | Use in this demo |
|------|------|-----|------------------|
| Admin / Maker | MOD Administrator | `admin@M365CPI98544940.onmicrosoft.com` | Administrative settings, Copilot Studio, Power Platform, Agent 365, connector and MCP governance |
| Primary ZAVA demo user | Preston Morales | `PrestonM@M365CPI98544940.onmicrosoft.com` | End-to-end ZAVA business flow with full Microsoft 365 Copilot license |
| Copilot Chat baseline | Selma Nyberg | `SelmaN@M365CPI98544940.onmicrosoft.com` | Copilot Chat scenario without full Microsoft 365 Copilot license |
| Teams meeting simulator | Leila Goncalves | `LeilaG@M365CPI98544940.onmicrosoft.com` | Starts the Teams meeting with Facilitator/Interpreter when needed; meeting voice and transcript can come from the simulator |

## Presenter Setup

1. Sign in to the main demo VM as Preston Morales (`PrestonM@M365CPI98544940.onmicrosoft.com`) for the full ZAVA end-to-end flow.
2. Keep MOD Administrator (`admin@M365CPI98544940.onmicrosoft.com`) separate for admin settings, Copilot Studio, Agent 365, connector, and MCP governance.
3. Use Selma Nyberg (`SelmaN@M365CPI98544940.onmicrosoft.com`) only for the Copilot Chat baseline without a full Copilot license.
4. Use Leila Goncalves (`LeilaG@M365CPI98544940.onmicrosoft.com`) only when a Teams meeting, Facilitator, Interpreter, transcript, or meeting simulator is required.
5. Copy the demo files to Preston's desktop with the one-liner.
6. Place the `ZAVA-Demo` folder in Preston's OneDrive or SharePoint, or upload individual files directly in Copilot Chat.
7. Open Microsoft 365 Copilot Chat: https://m365copilot.com
8. Open `Zava_Order_Analysis.xlsx` in Excel for web or desktop.
9. Use the email thread or reply prompt for the Outlook section.
10. Open the Word and PowerPoint seed files for Office Copilot or Word, Excel, and PowerPoint Agents.
11. For the Notebook module, create a Microsoft 365 Copilot Notebook named `Zava Executive Decision Room` and use `data/Zava_Copilot_Notebook_Setup.docx` as the source checklist.
12. For the Agent 365 E2E module, keep `data/agent-365/` ready for Agent Builder, Copilot Studio, requested-agent review, registry, and governance prompts.

## Demo Arc

| Segment | Duration | Core message |
| --- | ---: | --- |
| Microsoft 365 Copilot Chat | 6 min | Copilot identifies the real decision from email, meeting notes, memo, and briefing files. |
| Microsoft 365 Copilot Analyst agent | 6 min | Analyst evaluates feasibility, bottlenecks, price floor, and conditions. Backup: Copilot Chat or Copilot in Excel. |
| Copilot in Excel | 8 min | Excel and Copilot turn raw data into a reliable fulfillment view. |
| Copilot in Outlook and Copilot in Word | 7 min | Copilot in Outlook and Copilot in Word turn the decision into customer communication and an operations plan. |
| Copilot in PowerPoint | 5 min | PowerPoint creates the executive narrative. |
| Agent Builder in Microsoft 365 Copilot | 5 min | Agent Builder turns the flow into a repeatable process. |
| Microsoft Agent 365 | 5 min | Agent 365 shows how IT observes, governs, and secures Agent Builder and Copilot Studio agents. |
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
| Microsoft Agent 365 | Agent registry, activity/observability, lifecycle governance, Entra/Purview/Defender positioning for Agent Builder and Copilot Studio agents | New Zava module |
| Microsoft 365 Copilot Notebooks | Microsoft 365 Copilot Notebooks setup, reference collection, decision map, COO briefing | New Zava module |
| Analyst agent + Copilot in Excel | SAP actuals vs. TM1 forecast, variance analysis, close controls, CFO commentary | SAP/TM1 Month-End Close |
| Legal Agent in Word | Word contract summary, Legal Agent path, playbook comparison, redline fallback | Legal Agent Word |

Presenter rule: show only the modules available in the tenant. For anything preview-gated, admin-gated, region-limited, or model-provider-dependent, use the included seed files and transcripts as the backup path.
