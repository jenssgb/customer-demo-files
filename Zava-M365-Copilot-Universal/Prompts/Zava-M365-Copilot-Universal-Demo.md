# Zava Top Microsoft 365 Copilot Demo

## 1 - Copilot Chat Situation Brief

### Create the boardroom brief

```prompt
You are my Chief of Staff at Zava. Use Zava_Rush_Order_Context.docx, Zava_Email_Thread.docx, Zava_Meeting_Transcript.docx, and Zava_Executive_Decision_Memo.docx. Create a boardroom briefing in seven points: decision, deadline, customer objective, critical dependencies, risks, open owner actions, and recommended executive stance.
```

### Presenter Action

```demo
Sign in as Preston Morales for the main ZAVA flow. Open Microsoft 365 Copilot Chat and upload the files or reference them from Preston's OneDrive. Emphasize that Copilot turns scattered context into a decision-ready situation brief.
```

### Structure the Copilot Page

```prompt
Format the briefing as a Copilot Page with three sections: 1) Decision statement, 2) Evidence to verify, 3) Customer response principles. Write it so that Zoe, Maya, Omar, Lena, and Rafael can continue working from it immediately.
```

## 2 - Microsoft 365 Copilot Analyst Agent

### Analyze feasibility and price floor

```prompt
Analyze Zava_Order_Analysis.xlsx, Zava_Risk_Register.csv, and Zava_Pricing_Assumptions.csv. Answer four questions: 1) Can Zava commit to 20,000 units within 14 days? 2) Which SKU or dependency is the bottleneck? 3) Which price floor protects a 32 percent gross margin? 4) Which conditions must appear in the customer response?
```

### Build the decision table for Zoe

```prompt
Create a decision table with these columns: decision point, fact, risk, owner, condition for commitment, and communication guidance. Close with a three-sentence recommendation for Zoe.
```

### Presenter Action

```demo
Use the Microsoft 365 Copilot Analyst agent if it is available. If Analyst is not visible in Copilot Chat Tools, use Copilot Chat with the uploaded files or Copilot in Excel as the backup path. Show that Copilot is weighing dependencies against the decision criteria, not only summarizing text.
```

## 3 - Copilot in Excel

### Explain the dashboard

```prompt
Analyze this workbook. Start on the Executive Summary sheet. Explain the most important numbers, identify bottlenecks by SKU, color, and size, and suggest two visuals that Zoe can understand in 60 seconds.
```

### Create the management summary

```prompt
Add a management summary with four parts: 1) total supply versus requested quantity, 2) risk indicator by color, 3) recommended price floor, 4) next action by owner. Then create a chart for Total14DaySupply by color.
```

### Presenter Action

```demo
Open Zava_Order_Analysis.xlsx in Excel. Show the Executive Summary, the inventory formulas, and the chart. Then ask Copilot to create the management summary.
```

## 4 - Copilot in Outlook

### Draft the reply

```prompt
Draft a response to events-procurement@microsoft.example. Tone: calm, confident, and executive-ready. Say that Zava can make a conditional commitment if capacity, NFC activation, and Singapore freight are confirmed today. Name EUR 25.80 as the price floor, mention the White XL/XXL constraint transparently, and propose a 15-minute alignment call today.
```

### Improve with Copilot coaching

```prompt
Improve the reply for clarity, tone, and risk transparency. Remove internal cost details. Make the commitment conditions explicit but customer-friendly.
```

### Presenter Action

```demo
Switch to Outlook or use the email thread in Copilot Chat. Show that the response is grounded in analysis, risk, and price floor rather than generic wording.
```

## 5 - Copilot in Word

### Improve the operations plan

```prompt
Open Zava_Operations_Plan.docx and improve it for Zoe. Add an executive summary, a risk indicator section, and a table called "Next 4 hours" with owner, deadline, dependency, and definition of done.
```

### Word Agent alternative

```prompt
Create a new Word document titled "Zava Rush Order War Room Plan". Use all Zava files as context. Structure it as: Decision, Evidence, Risks, Workstreams, Customer Message, Executive Approval Checklist.
```

### Presenter Action

```demo
Show the difference between the customer response and the internal operations plan. Optionally use the Word Agent from Copilot Chat if it is available in the tenant.
```

## 6 - Copilot in PowerPoint

### Improve the executive deck

```prompt
Open Zava_Executive_Story.pptx. Improve the deck for Zoe: add speaker notes, make the decision on slide 5 clearer, and add a risk indicator on slide 3 for White XL/XXL, NFC activation, and Singapore freight.
```

### PowerPoint Agent alternative

```prompt
Create a new six-slide presentation for the COO decision. Use Zava_Order_Analysis.xlsx, Zava_Executive_Decision_Memo.docx, Zava_Risk_Register.csv, and Zava_Meeting_Transcript.docx. Slides: 1 Situation, 2 Customer ask, 3 Feasibility, 4 Margin guardrails, 5 Risks and mitigations, 6 Decision.
```

### Presenter Action

```demo
Open the PowerPoint seed deck or use the PowerPoint Agent. The goal is to show executive storytelling, not manual slide production.
```

## 7 - Agent Builder in Microsoft 365 Copilot

### Paste this into the Agent Builder Instructions field

```prompt
You are the Zava Order Desk Agent. You triage incoming rush orders for the Smart Launch Shirt launch.

When the user gives an order ID, look it up in the uploaded order intake file and the Zava context files. Then run exactly three checks:
1. Stock cover - can we fulfil the quantity by the requested date?
2. Margin floor - is the unit price at or above the 25.80 floor?
3. Compliance - region, contract terms, and launch-window rules.

Always answer in this structure:
- Order summary (customer, quantity, region, requested date)
- The three checks, each marked PASS or FLAG with one line of reasoning
- Recommendation: proceed, hold, or escalate - and name the escalation owner

Be concise and decision-ready. If a check fails, lead with the escalation. Never invent data that is not in the knowledge files.
```

### Test the agent you just built

```prompt
Triage order ZO-3101.
```

### Presenter Action

```demo
Build it live: Microsoft 365 Copilot > Agents > New agent > Skip to configure. Name = Zava Order Desk Agent; Description = triages Zava rush orders against stock, margin, and compliance; Instructions = paste the block above; Knowledge = upload AgentBuilder_OrderDesk_Brief.docx, Zava_Rush_Order_Context.docx, and Zava_Order_Intake.csv; Starter prompts = "Triage order ZO-3101" and "Which orders need escalation today?". Test in the Try it pane, then Create and share. Make the boundary explicit: Agent Builder consumes knowledge and answers - it cannot run actions or call APIs. That is why demo 10 (Copilot Studio) and demo 11 (Agent 365) follow.
```

## 8 - Microsoft 365 Copilot Researcher, Analyst, and Coach Agents

### Researcher market and supplier brief

```prompt
Use Researcher for this task if it is available. Build a market and supplier readiness brief for Zava's 20,000-unit smart launch shirt order. Cover event demand signals, supplier capacity questions, logistics risk, sustainability concerns, and a one-page executive recommendation. Use the Zava files as internal context and clearly separate internal facts from external research assumptions.
```

### Analyst deep scenario model

```prompt
Use Analyst or code interpreter if available. Analyze Zava_Order_Analysis.xlsx, Zava_Inventory_Snapshot.csv, Zava_Order_Intake.csv, and Zava_Risk_Register.csv. Run three scenarios: commit today, split delivery, and decline unless constraints clear. For each scenario, estimate operational risk, customer impact, margin exposure, and recommended executive decision.
```

### Prompt Coach improvement

```prompt
Use Prompt Coach if available. Improve this prompt for a senior operations user: "Can we accept the Zava rush order?" Make it specific, grounded, role-aware, and safe. Include required files, decision criteria, output format, and assumptions to verify.
```

### Presenter Action

```demo
Use this section as the premium extension after the core Zava flow. Researcher and Analyst are optional first-party experiences; if they are not available, run the same prompts in Copilot Chat with uploaded files and explain the backup path.
```

## 9 - Teams Facilitator and Interpreter Agents

### Facilitator war-room prompt

```prompt
@Facilitator summarize the Zava rush-order war room so far. Capture decisions, unresolved risks, owners, deadlines, and the exact customer response principles we agreed to. Create a concise action list for Zoe, Maya, Omar, Lena, and Rafael.
```

### Facilitator action tracking

```prompt
@Facilitator turn the discussion into a 4-hour execution plan. Track tasks for capacity confirmation, NFC activation, Singapore freight, finance approval, and customer response. Mark dependencies and escalation points.
```

### Interpreter global meeting moment

```prompt
Use the Teams Interpreter agent if available. Demonstrate how a German production lead, an English-speaking COO, and a Singapore logistics owner can follow the same Zava decision meeting in their preferred language. Keep the explanation short and focus on global collaboration.
```

### Presenter Action

```demo
Use Leila only to start the Teams meeting with Facilitator/Interpreter when needed; the meeting voice and transcript can come from the simulator. Otherwise use Zava_Meeting_Transcript.docx as the backup and explain that Facilitator/Interpreter are meeting-layer capabilities, not file-processing features.
```

## 10 - Agent platform ladder: Builder, Copilot Studio, Foundry (positioning)

### Place each build tool on the ladder

```demo
This is positioning, not a live build. Make the relationship explicit so the audience stops seeing "random agents". There is one ladder with three build tools and one governance dome:
1. Agent Builder (declarative) - inside Microsoft 365 Copilot, fields + knowledge, no actions. You built this live in demo 7.
2. Copilot Studio (low-code) - production path with real tools, actions, approvals, MCP, channels, admin review. You built this live in demo 10/Copilot Studio.
3. Azure AI Foundry (pro-code) - for AI engineers who need custom orchestration, evaluation, monitoring, and rollback. Not built live; position it as the engineering path.
Then the dome: whatever tool built the agent, it gets a Microsoft Entra Agent ID and shows up in Microsoft Agent 365, where IT observes, governs, and secures it. That is why we build first and govern second.
```

### Optional: Foundry pro-code framing for AI-engineering audiences

```demo
Only if the audience is technical. Describe a pro-code "Zava Fulfillment Sentinel" in Azure AI Foundry: ingest order events, retrieve policy and inventory context, evaluate risk, propose a recommendation, write an auditable decision record - with evaluation criteria, monitoring signals, and human-review/rollback rules. Stay verbal; do not try to build it live. The point is that Agent 365 governs even this pro-code agent.
```

### Presenter Action

```demo
Use this as the executive platform close, not a feature dump. One sentence per stage: Agent Builder = fastest reusable agent (demo 7); Copilot Studio = low-code production with tools and admin review (demo 10); Foundry = pro-code engineering path; Agent 365 = the control plane over all three (demo 8/11). Do NOT mix in Visual Creator or other prebuilt agents here - they are a separate creative track and break the platform narrative.
```

## 11 - Microsoft Agent 365 E2E: Agent Builder, Copilot Studio, Control Plane

### Set the compelling event

```demo
Frame the stakes before you build anything. It is launch week for Zava's NFC Smart Launch Shirt. Three rush orders are stuck in manual triage: Contoso Events (20,000 units, EMEA, critical), Fabrikam Sports (12,000, APAC), and Northwind Retail (8,500, North America) - 40,500 units, one shared deadline. One wrong commit blows the launch. The order desk needs an agent today, and IT needs to govern it tomorrow. Then walk the three doors: build it fast (Agent Builder), make it production (Copilot Studio), govern the estate (Agent 365).
```

### Paste this into the Agent Builder Instructions field

```prompt
You are the Zava Order Desk Agent. You triage incoming rush orders for the Smart Launch Shirt launch.

When the user gives an order ID, look it up in the uploaded order intake file and the Zava context files. Then run exactly three checks:
1. Stock cover - can we fulfil the quantity by the requested date?
2. Margin floor - is the unit price at or above the 25.80 floor?
3. Compliance - region, contract terms, and launch-window rules.

Always answer in this structure:
- Order summary (customer, quantity, region, requested date)
- The three checks, each marked PASS or FLAG with one line of reasoning
- Recommendation: proceed, hold, or escalate - and name the escalation owner

Be concise and decision-ready. If a check fails, lead with the escalation. Never invent data that is not in the knowledge files.
```

### Presenter Action

```demo
Build it live in Microsoft 365 Copilot > Agents > Create agent (Agent Builder). Fill the panes in order: Name = Zava Order Desk Agent; Description = triages rush orders against supply, margin, and compliance guardrails; Instructions = paste the prompt output; Knowledge = add the two Zava Word files and the intake CSV; Starter prompts = "Triage order ZO-3101" and "Which orders need escalation today?". Test in the right-hand pane, then Create and share. The moment: a working triage agent in under three minutes, grounded only on Zava's files - and IT will still govern it.
```

### Test the Agent Builder agent

```prompt
Use data/agent-365/Zava_Order_Intake.csv. Test the Zava Order Desk Agent with order ZO-3102. Summarize the request, identify the top three checks, apply the guardrails, and return a recommendation with escalation owner and next action.
```

### Show org-wide connector knowledge for Agent Builder

```demo
As MOD Administrator, open Microsoft 365 admin center > Settings > Search & intelligence > Data sources. Show the Copilot connector pattern: connector deployed, schema registered, items indexed, admin consent granted, and connector results enabled where appropriate. If the live connector is not available, open data/agent-365/AgentBuilder_Connector_MCP_Extension_Plan.csv and show the Copilot connector rows. Then switch to Preston: Microsoft 365 Copilot > Agent Builder > New agent > Configure > Knowledge. Show where an admin-enabled Microsoft 365 Copilot connector appears as a selectable knowledge source. The point: Agent Builder can reuse admin-provided external knowledge for the organization.
```

### Show MCP/API tools in Copilot Studio

```demo
As MOD Administrator, open Copilot Studio > Zava Fulfillment Escalation Agent > Tools > Add a tool > Model Context Protocol. Use data/agent-365/Zava_Public_OrderSignals_MCP_Registration.json only as the non-secret server registration reference: server name, streamable endpoint, auth pattern, and read-only tools such as get_order_risk_signal and search_supplier_signals. Explain the boundary clearly: API-like work, actions, and MCP belong in Copilot Studio, not directly in Agent Builder.
```

### Show Agent 365 tool governance

```demo
As MOD Administrator, open Microsoft 365 admin center > Agents > Tools. If Requests is visible, show the requested MCP/tool entry and the approve, reject, block, and unblock controls. If there is no pending request, use data/agent-365/AgentBuilder_Connector_MCP_Extension_Plan.csv and Agent365_Agent_Review_Register.csv as backup evidence. Explain the review questions: owner, data access, agent scope, authentication, tenant-wide consent, monitoring, and rollback path.
```

### Paste this into the Copilot Studio Instructions field

```prompt
You are the Zava Fulfillment Escalation Agent. You handle rush orders that the Order Desk Agent flagged for escalation during the Smart Launch Shirt launch.

For a given order:
1. Use the order-status lookup tool to get current fulfilment and inventory status.
2. If the order is at risk (late, below margin floor, or compliance flag), use the approval tool to request a human decision from the fulfilment lead.
3. Once you have a decision, use the Teams escalation tool to notify the fulfilment channel with the order ID, the risk, and the approved next action.

Always confirm back to the user: what you checked, who you escalated to, and the current status. Never commit stock or send an external message without an approval.
```

### Presenter Action

```demo
Build it live in Copilot Studio > Agents > Create > New agent (or Copy to Copilot Studio from the Agent Builder agent). Then: Instructions = paste the design prompt output; Knowledge = fulfillment spec plus order intake; Tools/actions = Teams escalation message, a human approval step, and an order-status lookup; Test in the built-in test panel until the escalation flow passes; Channels > Microsoft 365 Copilot and Microsoft Teams > turn on Make agent available in Microsoft 365 Copilot > Edit details > Save; then Save to submit for admin review. The agent now appears as a request in the admin center. If the tenant is not ready, use the prompt output as the build blueprint.
```

### Prepare the admin request

```prompt
Create an admin review package for the Zava Fulfillment Escalation Agent. Include agent name, owner, publisher, data sources, tools/actions, connectors, target users, business justification, risks, mitigations, and publish scope recommendation.
```

### Review the requested Copilot Studio agent

```demo
Open Microsoft 365 admin center. Go to Agents > All agents > Requests. Select the requested Copilot Studio agent if available. Review Data & tools, owner, capabilities, sources, actions, and requested publish scope. Do not publish broadly in a live customer demo unless the tenant is prepared.
```

### See your agent in Agent 365 (no prompt - this is an admin surface)

```demo
Agent 365 is an admin and governance surface, not a chat box - there is no prompt to type. Open Microsoft 365 admin center > Copilot > Agents > All agents. Find the Zava Order Desk Agent you built in demo 7 - it is already listed with no manual registration. Open it and show: Microsoft Entra Agent ID, owner, publisher (built with Agent Builder), status, environment, and the activity view (inputs, outputs, actions, results - preview, read-only, 30-day retention). Say it out loud: "I built this 3 minutes ago and it already has its own identity and activity trail that IT can govern." Backup if the tenant has no Agent 365: open data/agent-365/Agent365_Agent_Review_Register.csv and walk the same fields.
```

### Power Platform Governance vs Agent 365 objection handling

```prompt
Use data/agent-365/Agent365_vs_PowerPlatform_Governance.csv. The customer says: "We already have Power Platform Governance, so why do we need Agent 365?" Create a concrete answer using the Zava Fulfillment Escalation Agent and Zava Order Desk Agent. Show: what Power Platform Governance already covers, what it does not cover, what Agent 365 adds, and the exact demo click path that proves the difference.
```

### Show telemetry and activity

```demo
Open Microsoft 365 Copilot > All agents > Agent activity if the preview is visible. Show status, timing, inputs/outputs, actions taken, and results. If the view is not available, state the tenant limitation and continue with the registry and governance controls.
```

### Executive governance close

```demo
Show Agent 365 governance controls where available: publish/reject, assign, block, reassign, delete, ownerless-agent review, Purview audit/DLP, Defender threat detection, and Entra identity/access positioning. Do not ask Copilot to write the close; close verbally from the controls on screen.
```

### Presenter Action

```demo
If Agent 365 is visible, show All agents, agent details, registry fields, activity or usage, and governance actions such as block, reassign, publish/reject, or delete where available. If the tenant does not expose Agent 365 yet, use the Learn-verified matrix and data/agent-365/Agent365_Agent_Review_Register.csv as backup evidence. Do not click destructive actions live.
```

## 12 - Microsoft 365 Copilot Notebooks Extension: Executive Decision Room

### Create the Zava notebook

```demo
Open Microsoft 365 Copilot and create a new Microsoft 365 Copilot Notebook named "Zava Executive Decision Room". Use Zava_Copilot_Notebook_Setup.docx as the presenter checklist. Add the core Zava Word documents, Zava_Order_Analysis.xlsx, the finance close variance CSV, and the legal review documents as notebook references if the tenant experience supports them.
```

### Build the decision map

```prompt
Create an executive decision map for the Zava rush order. Connect operational feasibility, customer deadline, margin guardrails, SAP/TM1 finance close signals, legal contract risk, owners, and unresolved dependencies. Separate confirmed facts from assumptions and show what Zoe must decide today.
```

### Synthesize across operations, finance, and legal

```prompt
Using the notebook references, synthesize the strongest executive recommendation. Include: recommended decision, evidence, finance impact, legal risk, customer response language, owner actions, and what should not be promised until confirmed.
```

### Create the final COO briefing

```prompt
Draft the final COO briefing from this notebook. Format it as: Situation, Recommendation, Evidence, Analyst agent + Copilot in Excel Watchpoints, Legal Agent in Word Watchpoints, Decision Needed, Next 4 Hours. Keep it concise enough for a five-minute executive review.
```

### Presenter Action

```demo
Use this as the persistence and deep-thinking moment. Copilot Chat is good for one task; a Microsoft 365 Copilot Notebooks is the reusable workspace where the same references, prompts, and decisions stay together. If Microsoft 365 Copilot Notebooks are not available in the tenant, use Copilot Pages as the backup working surface.
```

## 13 - Microsoft 365 Copilot Analyst Agent + Copilot in Excel: SAP Actuals vs TM1 Forecast

### Open the finance close files

```demo
Open the ZAVA-Demo folder on the VM desktop. Use data/finance-close/SAP_TM1_Variance_Flat_Table.csv for the fast path, or upload SAP_Actuals_May2026.xlsx and TM1_Budget_Forecast_May2026.xlsx together for the heavier analyst path. Position the story as Zava's Finance team preparing month-end commentary for the COO.
```

### Find the biggest close variances

```prompt
You are the Finance Business Partner for Zava's month-end close. Analyze SAP_TM1_Variance_Flat_Table.csv. Identify the top 10 absolute variances versus TM1 forecast, grouped by Revenue, Opex, Capex, and Working Capital. For each variance, show actual, forecast, variance amount, variance percent, whether it is favorable or unfavorable, likely driver, owner, and the follow-up action needed before close sign-off.
```

### Separate business variance from data quality issues

```prompt
Review the SAP/TM1 variance data for items that look like timing issues, mapping problems, late postings, or manual journal anomalies. Create a close-control table with: issue type, evidence from the data, affected property or cost center, account, amount, risk to the close, owner, and recommended next step.
```

### Create the CFO close commentary

```prompt
Create an executive-ready month-end close commentary for Zava's CFO. Structure it as: 1) headline result, 2) top favorable drivers, 3) top unfavorable drivers, 4) risks and open items, 5) decisions needed today, 6) wording for the COO update. Keep it concise, factual, and ready to paste into a close deck.
```

### Presenter Action

```demo
Show this as the finance extension after the core Zava Excel section. The message is: Copilot can move Finance from raw SAP/TM1 extracts to variance explanation, close controls, and executive commentary. If Analyst is available, use it for multi-file reasoning. If not, use Copilot Chat with CSV/XLSX upload or Excel Copilot with the flat table.
```

## 14 - Legal Agent in Word (Frontier): Contract Review

### Open the legal review files

```demo
Open data/legal-review/Northwind_Property_Services_Agreement.docx in Word. Keep Contoso_Legal_Playbook_Service_Agreements.docx and Counterparty_Position_Memo.docx ready for Copilot Chat upload or Legal Agent context. Position the story as Zava Legal Agent in Word reviewing a vendor agreement before signing a time-critical services contract.
```

### Summarize the contract for General Counsel

```prompt
Summarize this property services agreement for Zava's General Counsel. Focus on commercial structure, high-risk clauses, negotiation pressure points, and what must be escalated before signature. Keep it to 10 bullets and cite the clause numbers you rely on.
```

### Perform a clause-level risk scan

```prompt
Review the agreement for legal and commercial risk. Prioritize subcontracting, service credits, indexation, data protection, confidentiality, audit rights, liability, termination, governing law, and AI use. For each issue, explain the risk, cite the source clause, and suggest a negotiation position.
```

### Compare against the legal playbook

```prompt
Compare the agreement against Contoso_Legal_Playbook_Service_Agreements.docx. Identify every clause that does not match Zava's preferred position or fallback. Create a table with: topic, current contract position, playbook position, risk level, suggested redline, and whether legal escalation is required.
```

### Draft targeted redlines

```prompt
Draft negotiation-ready redlines for the highest-risk clauses. Preserve the original commercial intent where possible, but align with Zava's playbook. Focus on subcontractor approval, data processing purpose limitation, confidentiality survival, audit rights, liability cap carve-outs, termination fee, and AI tool controls.
```

### Presenter Action

```demo
Use Legal Agent in Word if it is available in the tenant. If Legal Agent is not visible, use normal Copilot in Word for the open contract and Copilot Chat with all three legal files uploaded for the playbook comparison. Be explicit: this is legal operations acceleration and counsel review support, not final legal advice.
```

