# Legal Agent in Word Demo

## 1 · Setup

### Open the contract

```demo
Open Northwind_Property_Services_Agreement.docx in Word desktop. Open Copilot in Word. If the tenant has Frontier access, use the + button in the Copilot prompt box and select Legal Agent (Frontier). If not available, use normal Copilot in Word as the backup path.
```

### Attach context

```demo
Keep Contoso_Legal_Playbook_Service_Agreements.docx and Counterparty_Position_Memo.docx ready. If using normal Copilot Chat, upload all three files. If using Legal Agent in Word, use the contract as the active document and reference the playbook content where possible.
```

## 2 · Contract Understanding

### Executive summary

```prompt
Summarize this property services agreement for a General Counsel. Focus on commercial structure, high-risk clauses, negotiation pressure points, and what must be escalated before signature. Keep it to 10 bullets and cite the clause numbers you rely on.
```

### Clause risk scan

```prompt
Review the agreement for legal and commercial risk. Prioritize subcontracting, service credits, indexation, data protection, confidentiality, audit rights, liability, termination, governing law, and AI use. For each issue, explain the risk, cite the source clause, and suggest a negotiation position.
```

```demo
Show the citations. In Legal Agent, click citations to highlight the source language in the Word document. That is the trust moment.
```

## 3 · Playbook Review

### Compare against Contoso playbook

```prompt
Compare the agreement against Contoso_Legal_Playbook_Service_Agreements.docx. Identify every clause that does not match the preferred position or fallback. Create a table with: topic, current contract position, playbook position, risk level, suggested redline, and whether legal escalation is required.
```

### Business context overlay

```prompt
Use Counterparty_Position_Memo.docx as negotiation context. Which contract issues are legal must-fix items, which are business trade-offs, and which can be accepted with a comment or fallback language? Give me a recommended negotiation sequence.
```

## 4 · Redlining Moment

### Draft targeted redlines

```prompt
Draft negotiation-ready redlines for the highest-risk clauses. Preserve the original commercial intent where possible, but align with Contoso's playbook. Focus on: subcontractor approval, data processing purpose limitation, confidentiality survival, audit rights, liability cap carve-outs, termination fee, and AI tool controls.
```

### Comment for counsel

```prompt
Insert or propose short legal review comments for the clauses that need human counsel approval. Each comment should state the issue, why it matters, and the decision needed from Legal or the business owner.
```

```demo
If Legal Agent is available, show tracked changes/redlines. If only normal Copilot is available, ask it to draft clause text and paste one sample edit manually into Word with Track Changes enabled.
```

## 5 · Negotiation Pack

### Create signature recommendation

```prompt
Create a one-page signature recommendation for the General Counsel and CFO. Include: recommended position, top 5 risks, proposed fallbacks, items needing business approval, and a go/no-go recommendation.
```

### Meeting prep

```prompt
Create a 20-minute negotiation prep agenda for Legal, Procurement, IT Security, Finance, and Asset Management. Include the decision each stakeholder must make and the exact clause topic they own.
```

## 6 · Backup Path Without Legal Agent

### Normal Copilot in Word fallback

```prompt
Using the open contract, summarize the highest-risk clauses and draft replacement language for the data protection, liability, audit, termination, and AI use clauses. Make clear that this is a draft for legal review, not final legal advice.
```

### Copilot Chat fallback with all files

```prompt
Use the contract, playbook, and position memo I uploaded. Act as a legal operations assistant preparing counsel for review. Do not provide final legal advice. Produce a contract review matrix with citations, risks, proposed language, and owner decisions.
```
