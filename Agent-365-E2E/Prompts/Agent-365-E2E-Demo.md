# Microsoft Agent 365 E2E Demo

## 1 - Agent Builder in Microsoft 365 Copilot: Zava Order Desk Agent

### Build the declarative agent

```prompt
Use AgentBuilder_OrderDesk_Brief.docx and Zava_Rush_Order_Context.docx to design a Zava Order Desk Agent for Microsoft 365 Copilot. Create the agent purpose, instructions, knowledge sources, starter prompts, guardrails, escalation rules, and an example answer for rush order ZO-3101.
```

### Presenter Action

```demo
Open Microsoft 365 Copilot Chat, choose Agent Builder or New agent, and use the prompt output as the build plan. Add the Word documents as knowledge where the tenant experience allows it. Keep the story clear: Agent Builder is the fastest path for a declarative, grounded business agent.
```

### Test the agent

```prompt
Use Zava_Order_Intake.csv. Test the Zava Order Desk Agent with order ZO-3102. Summarize the request, identify the top three checks, apply the guardrails, and return a recommendation with escalation owner and next action.
```

## 2 - Microsoft Copilot Studio: Zava Fulfillment Escalation Agent

### Design the production agent

```prompt
Use CopilotStudio_Fulfillment_Agent_Spec.docx and Agent365_Governance_Checklist.docx. Transform the Zava Order Desk Agent into a Copilot Studio production agent. Include topics, triggers, actions, connectors, human approval steps, DLP/environment controls, analytics signals, and the publishing path to Microsoft 365 Copilot and Teams.
```

### Presenter Action

```demo
Open Copilot Studio. Create or describe the Zava Fulfillment Escalation Agent. Show where actions, topics, knowledge, authentication, environment, analytics, and publish channels would be configured. If the tenant is not ready, use the prompt output as the build blueprint.
```

### Prepare the admin request

```prompt
Create an admin review package for the Zava Fulfillment Escalation Agent. Include agent name, owner, publisher, data sources, tools/actions, connectors, target users, business justification, risks, mitigations, and publish scope recommendation.
```

## 3 - Microsoft 365 Admin Center: Requested Copilot Studio Agent

### Review the requested agent

```demo
Open Microsoft 365 admin center. Go to Agents > All agents > Requests. Select the requested Copilot Studio agent if available. Review Data & tools, owner, capabilities, sources, actions, and requested publish scope. Do not publish broadly in a live customer demo unless the tenant is prepared.
```

### Show the approval fields

```demo
Open Microsoft 365 admin center > Agents > All agents > Requests. Review owner, data sources, connectors/actions, environment, target users, risk, mitigations, and publish/reject decision. If no pending request exists, open Agent365_Agent_Review_Register.csv as backup evidence and show the same fields.
```

## 4 - Microsoft Agent 365: Registry and Inventory

### Open the control plane

```demo
Open Microsoft 365 admin center and go to Agents > Overview or Agents > All agents / Agent registry. Show that Agent 365 is the control plane after agents are created. Look for agent inventory, owner, publisher, platform, environment, connectors/tools, status, and governance gaps.
```

### Show the registry fields

```prompt
Use Agent365_Agent_Review_Register.csv. Explain how Microsoft Agent 365 helps the AI admin observe the Zava Order Desk Agent and Zava Fulfillment Escalation Agent. Structure the answer as: inventory, ownership, platform, environment, connectors/actions, risk signals, governance actions, and what would be unsafe without this registry.
```

## 5 - Microsoft Agent 365: Activity, Telemetry, and Usage

### Show activity if available

```demo
In Microsoft 365 Copilot, open All agents and select Agent activity if the preview is visible. Show status/timing, inputs/outputs, actions taken, and results. Say clearly that this activity view is preview, read-only, user-scoped, and retained for 30 days.
```

### Show activity fields

```demo
Open Microsoft 365 Copilot > All agents > Agent activity if the preview is visible. Show status, timing, inputs/outputs, actions taken, and results. If the view is not available, state the tenant limitation and continue with the registry and governance controls.
```

## 6 - Microsoft Agent 365: Govern and Secure

### Governance close

```demo
Show Agent 365 governance controls where available: publish/reject, assign, block, reassign, delete, ownerless-agent review, Purview audit/DLP, Defender threat detection, and Entra identity/access positioning. Do not ask Copilot to write the close; close verbally from the controls on screen.
```

### Presenter Action

```demo
Show governance actions only as a review, not by clicking destructive actions. If Agent 365 is not enabled in the tenant, use the HTML feature matrix and Agent365_Agent_Review_Register.csv as backup evidence.
```
