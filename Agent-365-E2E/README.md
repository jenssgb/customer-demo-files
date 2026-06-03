# Microsoft Agent 365 E2E Demo

End-to-end demo for Microsoft Agent 365 using one business storyline: Zava turns an urgent rush-order workflow into two agents, then governs them through Agent 365.

## Demo Goal

Show what is currently demoable across:

1. Agent Builder in Microsoft 365 Copilot: build a declarative Zava Order Desk Agent with knowledge sources and guardrails.
2. Microsoft Copilot Studio: build a production-style Zava Fulfillment Escalation Agent with actions, approval flow, environment governance, and publishing path.
3. Microsoft Agent 365: observe, govern, and secure both agent patterns through registry, requests, activity, ownership, governance controls, and security/compliance positioning.

## Official Sources

- Microsoft Agent 365 overview: https://learn.microsoft.com/microsoft-agent-365/overview
- Copilot Studio and Agent 365: https://learn.microsoft.com/microsoft-agent-365/builder/overview
- Agent activity view: https://learn.microsoft.com/microsoft-agent-365/observe-agents-microsoft-365-copilot
- Agent Builder: https://learn.microsoft.com/microsoft-365/copilot/extensibility/agent-builder
- Manage requested Copilot Studio agents: https://learn.microsoft.com/microsoft-365/copilot/agent-essentials/agent-lifecycle/agent-copilot-studio-requested

## Feature Matrix

| Product / capability | What is currently demoable | Limits / caveats | Demo implication |
| --- | --- | --- | --- |
| Agent Builder in Microsoft 365 Copilot | Create declarative agents from Microsoft 365 Copilot, add knowledge sources, test the agent, and share it. | Not available on mobile; complex actions require Copilot Studio; SharePoint permission behavior and admin controls matter. | Build the Zava Order Desk Agent as the fast citizen-agent path. |
| Microsoft Copilot Studio | Build more advanced agents with actions, topics, connectors, environment governance, and publish to Teams or Microsoft 365 Copilot channels. | Requires the right Copilot Studio, Power Platform, environment, billing, DLP, and admin configuration. | Build the Zava Fulfillment Escalation Agent as the low-code production path. |
| Requested Copilot Studio agents | Admins review requested agents in Microsoft 365 admin center > Agents > All agents > Requests; publish or reject and scope availability. | UI and availability depend on tenant configuration and publishing channel. | Show the approval gate before an agent becomes broadly available. |
| Microsoft Agent 365 registry | Centralized visibility for agents, including inventory, metadata, publisher, platform, connectors, environment, activity and health signals. | Requires qualifying Agent 365 license to enable; tenant rollout and admin role matter. | Show Agent 365 as the control plane after agent creation. |
| Copilot Studio telemetry in Agent 365 | Copilot Studio agents automatically appear in registry and send telemetry without manual SDK instrumentation. | Detail can vary by agent and tenant; some observability views are preview. | Explain automatic telemetry for invocations and tool/connector usage. |
| All-agents activity view | In Microsoft 365 Copilot, users can view agent activity, status/timing, inputs/outputs, actions taken, and results. | Preview, read-only, user-scoped, 30-day retention; admins do not see detailed user timelines in this view. | Use live if visible; otherwise use the runbook as talk-track backup. |
| Governance actions | Block, reassign, delete, publish/reject requested agents, review owners and metadata. | Do not click destructive actions in a live customer demo. Copilot Studio deletion may require Power Platform environment admin. | Demonstrate review and explain controls without breaking the tenant. |

## Files

| File | Purpose |
| --- | --- |
| `Agent-365-E2E-Briefing.html` | Live runbook with copy buttons and prominent file requirement cards |
| `Prompts/Agent-365-E2E-Demo.md` | PromptPrompter-ready script |
| `data/AgentBuilder_OrderDesk_Brief.docx` | Source document for the declarative Agent Builder agent |
| `data/CopilotStudio_Fulfillment_Agent_Spec.docx` | Source document for the Copilot Studio production agent concept |
| `data/Agent365_Governance_Checklist.docx` | Admin and presenter checklist for Agent 365 observe/govern/secure |
| `data/Zava_Rush_Order_Context.docx` | Business context for the Zava order scenario |
| `data/Zava_Order_Intake.csv` | Test orders for the Agent Builder agent |
| `data/Agent365_Agent_Review_Register.csv` | Mock governance register for admin review and backup evidence |
| `Deploy-Agent365-Demo-Content.ps1` | CDX OneDrive/SharePoint upload script |

## VM One-Liner

```powershell
$d=[Environment]::GetFolderPath('Desktop');$z="$env:TEMP\agent365.zip";$t="$env:TEMP\agent365";iwr 'https://github.com/jenssgb/customer-demo-files/archive/refs/heads/main.zip' -OutFile $z;ri "$d\AGENT365-Demo",$t -r -fo -ea 0;Expand-Archive $z $t -Force;mv "$t\customer-demo-files-main\Agent-365-E2E" "$d\AGENT365-Demo";ri $z,$t -r -fo;Start-Process msedge "$d\AGENT365-Demo\Agent-365-E2E-Briefing.html";ii "$d\AGENT365-Demo"
```

## Presenter Rule

Agent 365 is not another chatbot. The live story is: create agents, publish or request them, then observe, govern, and secure them as managed enterprise assets.
