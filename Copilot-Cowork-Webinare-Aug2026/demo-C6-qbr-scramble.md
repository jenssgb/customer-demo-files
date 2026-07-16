# DEMO C6 — The QBR Scramble

**APP:** Copilot Chat (Cowork / Multi-App)
**DURATION:** ~90 seconds
**FEATURE:** Edit with Copilot · Multi-file reasoning · Word + Excel + Outlook output
**DIFFICULTY:** Hard
**STATUS:** READY

---

## The Hook (5 sec)

> "It's Sunday night. QBRs start Monday morning. You have 12 accounts, 3 RED, scattered exec feedback across 5 docs, and your VP wants a portfolio pre-brief by 8am. You've been doing this for 3 hours every quarter. Tonight, it takes 60 seconds."

---

## The Setup (10 sec)

Viewer sees:
- Copilot Chat open in M365 (or Teams)
- 3 files visible: `c6_account_health.csv`, `c6_project_status.csv`, `c6_exec_feedback.txt`
- CSM Jordan Ellis, Sunday 9:47pm, tired face energy 😅

**Context:** Jordan manages 12 enterprise accounts. Every quarter he manually compiles health scores, re-reads scattered exec feedback from emails and call notes, writes 3 individual meeting prep emails, and builds a risk table in Excel. It takes 2–3 hours every Sunday night before QBR week.

---

## The Prompt (10 sec)

```
Using c6_account_health.csv, c6_project_status.csv, and c6_exec_feedback.txt:

1. PRE-BRIEF MEMO (Word): Executive summary of my portfolio health. Highlight the 3 RED accounts with risk rationale. Identify the 2 upsell opportunities. Surface every exec's top concern from the feedback notes and match it to an action item. Format as a 2-page VP-ready memo.

2. ACCOUNT RISK DASHBOARD (Excel): Build a ranked risk table — all 12 accounts sorted by health score. Color-code RED/AMBER/GREEN. Add columns for renewal urgency (days to renewal), overdue action items, and a "CSM Recommendation" column (Escalate / Monitor / Expand). Add conditional data bars on health scores.

3. MEETING PREP EMAILS (Outlook drafts): Write 3 pre-meeting emails — one each for the RED accounts (Meridian, Nexflow, Steelbridge). Each email: brief agenda, what I know about their concerns from the feedback, 1–2 questions to open the conversation. Tone: confident, warm, prepared.
```

---

## The Magic (40 sec)

Copilot reads all three files simultaneously. Show the step-by-step execution plan it generates:

1. **Analyzes** `c6_account_health.csv` → identifies 3 RED accounts (health scores 28, 34, 31), 3 upsell accounts (Crestwood, Vantage, Pinnacle), sorts by health score
2. **Cross-references** `c6_project_status.csv` → matches RED accounts to stalled projects (compliance module, ERP integration, champion departure)
3. **Reads** `c6_exec_feedback.txt` → extracts per-exec concerns, maps overdue actions, identifies tone signals (David Kwan: frustrated/analytical, Helen Marsh: credibility on the line, Sara Okafor: new/skeptical)
4. **Creates** Word memo — portfolio health overview + RED account risk rationale + exec concern mapping + upsell pipeline
5. **Creates** Excel risk dashboard — 12 rows, sorted by health score, RAG color-coding, data bars, CSM Recommendation column
6. **Drafts** 3 Outlook emails — each personalized to the exec's specific concern, not generic templates

---

## The Result (15 sec)

**What Jordan sees 60 seconds later:**

- 📄 **Pre-Brief Memo** (Word, 2 pages): Portfolio summary, RED account triage, Meridian/Nexflow/Steelbridge risk rationale with exec names + concerns mapped to action items. Crestwood + Vantage flagged as upsell opportunities with context. VP-ready language.

- 📊 **Risk Dashboard** (Excel): 12 accounts ranked — Meridian (28) at the top in red, Luminary Education (94%) at the bottom in green. Data bars on health scores. "CSM Recommendation" column: 3 ESCALATE, 5 MONITOR, 4 EXPAND. Days-to-renewal urgency column highlights Ironclad (37 days) and Meridian (81 days) as critical.

- 📧 **3 Outlook Draft Emails** — each tailored:
  - *Meridian (David Kwan)*: "David — I want to come to tomorrow's QBR with a concrete recovery plan, not talking points. Here's the agenda..."
  - *Nexflow (Sara Okafor)*: "Sara — I know you haven't seen a full platform overview yet. I'd like to start there, then walk you through the ROI case..."
  - *Steelbridge (Helen Marsh)*: "Helen — I hear you on needing written commitment. I'm bringing our Professional Services lead and a signed recovery timeline..."

**Wow moment:** Each email references the specific concern from the exec feedback — not a generic template. Copilot connected the dots across 3 files to write emails that sound like Jordan has a photographic memory.

---

## The CTA (10 sec)

> "Sunday night QBR prep: from 3 hours to 60 seconds.
> All you need: your account health CSV, your project status, and your call notes.
> **Try it tonight — your Monday self will thank you.**"

---

## LinkedIn Post Draft

**Hook:**
> It's 9pm Sunday. QBRs start at 8am Monday.

You have:
- 12 accounts
- 3 are RED
- Scattered exec feedback from 5 different calls
- A VP who wants a portfolio brief by morning

This used to take me 3 hours every quarter.

With M365 Copilot:

I dropped 3 files into Copilot Chat.
60 seconds later I had:

📄 A 2-page VP-ready portfolio memo
📊 An account risk dashboard (sorted, color-coded, with recommendations)
📧 3 personalized prep emails — each tailored to the exec's specific concern

The Nexflow email literally referenced that their champion left in March and addressed the new CFO's ROI question. I didn't tell it to do that. It read the feedback notes and figured it out.

**That's not autocomplete. That's a colleague who read the brief.**

---

## Source Data Notes

| File | Rows | Key Details |
|------|------|------------|
| `c6_account_health.csv` | 12 accounts | Health 28–94, 3 RED / 3 AMBER / 6 GREEN, ARR $72k–$620k, renewal 37–234 days out, 4 upsell flags |
| `c6_project_status.csv` | 5 projects | 3 RED / 2 AMBER, stalled ERP integration, champion departure, new CFO onboarding, competitor POC |
| `c6_exec_feedback.txt` | 5 exec profiles | David Kwan (angry/data-driven), Sara Okafor (new/skeptical/ROI-focused), Helen Marsh (credibility loss), Rebecca Torres (fresh/open), Tom Bradley (competitive eval) |

**Hooks baked in:**
- David Kwan (Meridian) may be evaluating alternatives — "evaluating alternatives" mentioned to a mutual contact
- Sara Okafor (Nexflow) has never seen the product — first touch is the QBR
- Helen Marsh (Steelbridge) wants a "signed commitment" — signals professional services expansion
- Crestwood has a dormant 50-seat expansion ($85k ARR) that the new CFO doesn't know about
- Vantage: CEO running competitor POC but internal champion (Claire Su) is an advocate

---

## SharePoint Files

- `c6_account_health.csv` → [SharePoint](https://bluepolicy.sharepoint.com/sites/openclaw-data-agent/_layouts/15/Doc.aspx?sourcedoc=%7B5786418C-BF02-4FB8-B924-AE3F5A8642D5%7D&file=c6_account_health.csv&action=default&mobileredirect=true)
- `c6_project_status.csv` → [SharePoint](https://bluepolicy.sharepoint.com/sites/openclaw-data-agent/_layouts/15/Doc.aspx?sourcedoc=%7B7691FD0C-388B-4F68-BCCE-14C1D20A2AEB%7D&file=c6_project_status.csv&action=default&mobileredirect=true)
- `c6_exec_feedback.txt` → [SharePoint](https://bluepolicy.sharepoint.com/sites/openclaw-data-agent/Shared%20Documents/Microsoft/Copilot-Demos/c6_exec_feedback.txt)
