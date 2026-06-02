# Zava Top Microsoft 365 Copilot Demo

## 1 - Copilot Chat Situation Brief

### Create the boardroom brief

```prompt
You are my Chief of Staff at Zava. Use Zava_Rush_Order_Context.md, Zava_Email_Thread.html, Zava_Meeting_Transcript.md, and Zava_Executive_Decision_Memo.md. Create a boardroom briefing in seven points: decision, deadline, customer objective, critical dependencies, risks, open owner actions, and recommended executive stance.
```

### Presenter Action

```demo
Open Microsoft 365 Copilot Chat and upload the files or reference them from OneDrive. Emphasize that Copilot turns scattered context into a decision-ready situation brief.
```

### Structure the Copilot Page

```prompt
Format the briefing as a Copilot Page with three sections: 1) Decision statement, 2) Evidence to verify, 3) Customer response principles. Write it so that Zoe, Maya, Omar, Lena, and Rafael can continue working from it immediately.
```

## 2 - Analyst-Style Reasoning

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
Use Think Deeper or an analyst-style reasoning mode if available. Show that Copilot is not only summarizing; it is weighing dependencies against the decision criteria.
```

## 3 - Excel Workbook

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

## 4 - Outlook Customer Response

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

## 5 - Word Operations Plan

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

## 6 - PowerPoint Executive Story

### Improve the executive deck

```prompt
Open Zava_Executive_Story.pptx. Improve the deck for Zoe: add speaker notes, make the decision on slide 5 clearer, and add a risk indicator on slide 3 for White XL/XXL, NFC activation, and Singapore freight.
```

### PowerPoint Agent alternative

```prompt
Create a new six-slide presentation for the COO decision. Use Zava_Order_Analysis.xlsx, Zava_Executive_Decision_Memo.md, Zava_Risk_Register.csv, and Zava_Meeting_Transcript.md. Slides: 1 Situation, 2 Customer ask, 3 Feasibility, 4 Margin guardrails, 5 Risks and mitigations, 6 Decision.
```

### Presenter Action

```demo
Open the PowerPoint seed deck or use the PowerPoint Agent. The goal is to show executive storytelling, not manual slide production.
```

## 7 - Agent Builder Scale-Out

### Design the Order Desk agent

```prompt
Design a Zava Order Desk Agent for Microsoft 365 Copilot. Use Zava_Agent_Builder_Brief.md as the foundation. Provide: Agent Purpose, Instructions, Knowledge Sources, Starter Prompts, Guardrails, Escalation Rules, and an example response for a new rush order.
```

### Test the agent with a second order

```prompt
Test the agent with request ZO-1044 from Zava_Order_Intake.csv. Summarize the order, name the three most important checks, and provide a concise recommendation for Sales Operations.
```

### Presenter Action

```demo
Open Agent Builder in Microsoft 365 Copilot. Use the output as the build plan. Explain that the manual Copilot flow becomes a repeatable Order Desk process.
```
