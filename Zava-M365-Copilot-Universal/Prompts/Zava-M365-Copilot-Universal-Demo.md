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
Build it live: Microsoft 365 Copilot > Agents > New agent > Skip to configure. Name = Zava Order Desk Agent; Description = triages Zava rush orders against stock, margin, and compliance; Instructions = paste the block above; Knowledge = upload AgentBuilder_OrderDesk_Brief.docx, Zava_Rush_Order_Context.docx, and Zava_Order_Intake.csv; Starter prompts = "Triage order ZO-3101" and "Which orders need escalation today?". Test in the Try it pane, then Create and share. Make the boundary explicit: Agent Builder consumes knowledge and answers - it cannot run actions or call APIs. That is why the end-to-end story in section 11 (Copilot Studio for actions, then Agent 365 for governance) follows.
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
1. Agent Builder (declarative) - inside Microsoft 365 Copilot, fields + knowledge, no actions. You built this live in section 7 (and section 11, Door 1).
2. Copilot Studio (low-code) - production path with real tools, actions, approvals, MCP, channels, admin review. You build this live in section 11, Door 2.
3. Azure AI Foundry (pro-code) - for AI engineers who need custom orchestration, evaluation, monitoring, and rollback. Not built live; position it as the engineering path.
Then the dome: whatever tool built the agent, it gets a Microsoft Entra Agent ID and shows up in Microsoft Agent 365, where IT observes, governs, and secures it (section 11, Door 4). That is why we build first and govern second.
```

### Optional: Foundry pro-code framing for AI-engineering audiences

```demo
Only if the audience is technical. Describe a pro-code "Zava Fulfillment Sentinel" in Azure AI Foundry: ingest order events, retrieve policy and inventory context, evaluate risk, propose a recommendation, write an auditable decision record - with evaluation criteria, monitoring signals, and human-review/rollback rules. Stay verbal; do not try to build it live. The point is that Agent 365 governs even this pro-code agent.
```

### Presenter Action

```demo
Use this as the executive platform close, not a feature dump. One sentence per stage: Agent Builder = fastest reusable agent (section 7); Copilot Studio = low-code production with tools and admin review (section 11, Door 2); Foundry = pro-code engineering path; Agent 365 = the control plane over all three (section 11, Door 4). Do NOT mix in Visual Creator or other prebuilt agents here - they are a separate creative track and break the platform narrative.
```

## 11 - Microsoft Agent 365 end-to-end: build it, extend it, govern it

> The integrated story. Sections 7-10 show each tool on its own. This section runs the whole arc as one demo: build a simple agent, build a real one with actions, enable tools safely, then govern both as digital workers in Agent 365. Four doors, one launch week.

### Door 0 - Set the compelling event

```demo
Frame the stakes before you build anything. It is launch week for Zava's NFC Smart Launch Shirt. Three rush orders are stuck in manual triage: Contoso Events (20,000 units, EMEA, critical), Fabrikam Sports (12,000, APAC), and Northwind Retail (8,500, North America) - 40,500 units, one shared deadline. One wrong commit blows the launch. The order desk needs an agent today; IT needs to govern it tomorrow. Then name the four doors out loud: 1) build it fast (Agent Builder), 2) make it production with actions (Copilot Studio), 3) enable knowledge and tools safely (connectors and MCP), 4) govern the whole estate (Agent 365).
```

### Door 1 - Build it fast: paste this into the Agent Builder Instructions field

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

### Door 1 - Build it live (Agent Builder)

```demo
Microsoft 365 Copilot > Agents > New agent > Skip to configure. Name = Zava Order Desk Agent; Description = triages Zava rush orders against stock, margin, and compliance; Instructions = paste the block above; Knowledge = upload AgentBuilder_OrderDesk_Brief.docx, Zava_Rush_Order_Context.docx, and Zava_Order_Intake.csv; Starter prompts = "Triage order ZO-3101" and "Which orders need escalation today?". Test in the Try it pane, then Create and share. Say the boundary out loud: Agent Builder consumes knowledge and answers - it cannot run actions or call APIs. That is exactly why Door 2 exists.
```

### Door 1 - Test the agent you just built

```prompt
Triage order ZO-3101.
```

### Door 2 - Make it production: paste this into the Copilot Studio Instructions field

```prompt
You are the Zava Fulfillment Escalation Agent. You handle rush orders that the Order Desk Agent flagged for escalation during the Smart Launch Shirt launch.

For a given order:
1. Use the order-status lookup tool to get current fulfilment and inventory status.
2. If the order is at risk (late, below margin floor, or compliance flag), use the approval tool to request a human decision from the fulfilment lead.
3. Once you have a decision, use the Teams escalation tool to notify the fulfilment channel with the order ID, the risk, and the approved next action.

Always confirm back to the user: what you checked, who you escalated to, and the current status. Never commit stock or send an external message without an approval.
```

### Door 2 - Build it live with real actions (Copilot Studio)

```demo
Copilot Studio > Agents > Create > New agent (or Copy to Copilot Studio from the Agent Builder agent). Instructions = paste the block above; Knowledge = fulfillment spec plus order intake; Tools > Add a tool = add three actions: (1) Microsoft Teams - post message to the fulfilment channel, (2) Approvals - human-in-the-loop decision, (3) Model Context Protocol - read-only order-status lookup. Test in the built-in test panel until the escalation flow passes. Channels > Microsoft 365 Copilot and Microsoft Teams > turn on Make agent available in Microsoft 365 Copilot > Edit details > Save; then Save again to submit for admin review. The point: this agent can ACT - message a person, request approval, look up live status - which Agent Builder cannot. Presenter safety: in a shared tenant, show the tools configured and the "Save for review" hand-off; do not fire real Teams messages unless prepared.
```

### Door 2 - Test the full tool chain

```prompt
Order ZO-3101 was flagged for escalation. Check its status, request approval from the fulfilment lead, and notify the fulfilment team with the recommended action.
```

### Door 3 - Enable knowledge safely: connector for Agent Builder (admin click-path)

```demo
No prompt box here - this is an admin click-path. As MOD Administrator: Microsoft 365 admin center > Settings > Search & intelligence > Data sources. Show the Copilot connector pattern: connector deployed, schema registered, items indexed, admin consent granted. Then switch to Preston: Microsoft 365 Copilot > Agent Builder > New agent > Configure > Knowledge - show where an admin-enabled connector appears as a selectable knowledge source, and test with a Zava supplier/order-signal question. No live connector? Narrate the same pattern from the connector rows in AgentBuilder_Connector_MCP_Extension_Plan.csv - evidence, not a required input.
```

### Door 3 - Enable tools safely: MCP in Copilot Studio (admin click-path)

```demo
No prompt box - admin click-path. Copilot Studio > Zava Fulfillment Escalation Agent > Tools > Add a tool > Model Context Protocol. Walk the non-secret registration: server name, streamable MCP endpoint, auth pattern, and read-only tools such as get_order_risk_signal and search_supplier_signals (reference: Zava_Public_OrderSignals_MCP_Registration.json). State the boundary: the same MCP server cannot be attached directly to Agent Builder - API/tool work belongs in Copilot Studio.
```

### Door 3 - Govern the tools (admin click-path)

```demo
No prompt box - admin click-path. Microsoft 365 admin center > Agents > Tools. If Requests is visible, show the requested MCP/tool entry and the approve, reject, block, unblock controls. Walk the review questions out loud: who owns the tool, what data it can access, which agent can call it, what authentication it uses, whether tenant-wide consent is required, and what the rollback path is.
```

### Door 4 - Govern the estate: open the agent estate (admin click-path)

```demo
No prompt box - Agent 365 is the control plane, an admin and governance surface. Microsoft 365 admin center > Agents > All agents. Find BOTH agents you just built: the Zava Order Desk Agent (Agent Builder) and the Zava Fulfillment Escalation Agent (Copilot Studio) - already listed, no manual registration. Open one to show its Microsoft Entra Agent ID, owner, publisher, and status. Say it: "I built these today and they already have their own identity that IT can govern."
```

### Door 4 - Identity: each agent is a real Entra principal (admin click-path)

```demo
Microsoft Entra admin center > Agent IDs. Show object identity, owner, and the access package that defines what the agent can reach. Explain: Copilot Studio agents receive an Entra Agent ID automatically - that identity is what makes governance, audit, and Conditional Access possible, just like for an employee. Backup evidence: Agent365_Agent_Review_Register.csv (owner/platform columns show the same concept).
```

### Door 4 - Observe: one registry, one Agent Map (admin click-path)

```demo
Microsoft 365 admin center > Agents > Overview - show the 30-day snapshot, total agents, usage trends, and actionable insights (pending requests, agents without owners). Open All agents for inventory, ownership, platform, and risk signals on both Zava agents. If available, open Agent Map to visualize which data and tools each agent touches.
```

### Door 4 - Govern: act on the agent lifecycle (admin click-path)

```demo
Microsoft 365 admin center > Agents > Requests. Open the pending request for the Zava Fulfillment Escalation Agent (submitted from Copilot Studio in Door 2) and walk the Data and tools review: owner, data sources, tools/actions, target users, risk, mitigations - then publish or reject with a scope. Then show two more lifecycle actions: reassign an ownerless agent to a real owner, and tighten the Entra access package. Backup: Agent365_Governance_Checklist.docx. Do not click destructive actions live.
```

### Door 4 - Secure: Purview data control + Defender runtime block (admin click-path)

```demo
In Microsoft Purview, point to DLP and audit coverage on the data the agent can access - for example, preventing it from sharing launch-contract data externally. In Microsoft Defender, show runtime protection that detects and blocks unsafe agent actions (unauthorized access, data exfiltration, prompt injection, tool misuse) and treats the agent as a first-class security principal. Portals not demo-ready? Narrate the control and use Agent365_Governance_Checklist.docx as policy evidence.
```

### Door 4 - Objection handling: Power Platform Governance vs Agent 365

```prompt
Use data/agent-365/Agent365_vs_PowerPlatform_Governance.csv. The customer says: "We already have Power Platform Governance, so why do we need Agent 365?" Create a concrete answer using the Zava Fulfillment Escalation Agent and Zava Order Desk Agent. Show: what Power Platform Governance already covers, what it does not cover, what Agent 365 adds, and the exact demo click path that proves the difference.
```

### Door 4 - Executive close (say it, do not prompt it)

```demo
Close verbally from the controls on screen - do not ask Copilot to write it. Tie each control to the Smart Launch Shirt go-live: the Entra Agent ID gives accountability, the registry removes shadow agents, the lifecycle review stops a bad agent before it ships, Purview prevents a contract-data leak, and Defender blocks a compromised agent at runtime. Headline: "Launch week is no longer a risk. Every agent acting for Zava is identified, governed, and secured from one place - so Zava can scale agents with confidence." Known limits to respect: agent activity view is preview, read-only, user-scoped, 30-day retention; Defender/Purview agent surfaces depend on E5 and tenant configuration.
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

