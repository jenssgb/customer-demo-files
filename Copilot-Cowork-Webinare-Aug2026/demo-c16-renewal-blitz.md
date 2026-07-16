# DEMO C16: The Renewal Blitz

**App:** Microsoft 365 Copilot Cowork (Multi-App: Excel + Word + Outlook + Calendar)
**Duration:** ~90 seconds
**Feature:** Copilot Cowork — Cross-App Orchestration, Task Continuity, Work IQ
**Type:** Cowork (multi-step, multi-app)

---

## HOOK (5 sec)

> "It's Q3 renewal season. Ten accounts. $808,000 ARR. Three are on fire. One renewal closes in 23 days and the COO has never even been onboarded. Your CSM team has the data — it's scattered across four apps."

---

## SETUP (10 sec)

Open `c16_renewal_blitz.xlsx` — show the Account Renewal Tracker with 10 accounts, RED/AMBER/GREEN color coding, open support ticket counts, usage percentages, days to renewal.

**The situation:**
- BlueSky Logistics: 23 days to renewal, COO never onboarded, 9 open tickets, 29% platform usage
- TerraAxis Corp: 29 days, champion left the company June 2nd, CTO skeptical
- Nexis Corporation: 44 days, $285k ARR, 7 open tickets, champion displaced in reorg

Before Copilot: CSM would open the tracker (App 1), open Outlook to draft 3+ personalized executive emails (App 2), open Word to write the exec briefing decks (App 3), open Calendar to find scheduling slots (App 4) — then manually cross-reference all the context between apps. 2–3 hours minimum.

---

## PROMPT (10 sec)

```
Using c16_renewal_blitz.xlsx, run the Q3 Renewal Blitz playbook:

1. TRIAGE (Excel): Add a 'Renewal Blitz Priority' column to Account Renewal Tracker — CRITICAL (renewal <30 days, RED risk), P1 (renewal 30–60 days, RED/AMBER), P2 (AMBER, >60 days), P3 (GREEN). Sort by priority. Add a summary row showing total ARR at risk by tier.

2. EXEC SAVE BRIEFS (Word): For the 3 RED accounts, create a 1-page Account Save Brief each — account health snapshot, what went wrong, what we've committed to fix (from Actions & Checkpoints), and a recommended ask for the executive contact. Use the Outreach Context sheet for talking points and CSM/AE names.

3. OUTREACH EMAILS (Outlook drafts): Draft 3 personalized outreach emails — one per RED account — from the assigned CSM to the executive contact. Each email references their specific situation, acknowledges the issue, and proposes a concrete next step. Tone: direct, accountable, human.

4. CALENDAR REQUESTS: Draft calendar invites for the 3 CRITICAL/P1 actions due this week from the Actions & Checkpoints sheet. Include a 2-sentence context note in each invite body.

5. CHECKPOINT: After completing steps 1–4, give me a status brief: which actions are done, which are in-flight, and what I need to personally review before sending anything.
```

---

## MAGIC (40 sec)

Copilot Cowork creates a plan:
- **Step 1:** Reads Account Renewal Tracker + Actions & Checkpoints sheets → adds Priority column → sorts → adds ARR summary
- **Step 2:** Cross-references Outreach Context sheet for talking points → generates 3 Account Save Briefs in Word, each with health snapshot, root cause, commitment, and ask
- **Step 3:** Pulls champion names, economic buyer emails, and account history from the tracker → drafts 3 personalized Outlook emails, each different in tone and specific issue addressed
- **Step 4:** Reads Actions & Checkpoints for due dates → drafts calendar invites with correct attendees and context
- **Step 5:** Returns a Checkpoint summary — "4 actions completed, 3 emails held for your review, 1 invite pending COO availability confirmation"

**Highlight:** Copilot automatically surfaces the BlueSky Logistics situation as the most critical — the COO has never been contacted — and flags it for VP CS personal outreach rather than CSM.

---

## RESULT (15 sec)

Show what was produced in ~60 seconds:
- Excel: 10 accounts sorted by Renewal Blitz Priority with ARR-at-risk summary
- Word: 3 × Account Save Briefs, each customized to the account's specific risk and executive audience
- Outlook: 3 draft emails in the CSM's outbox — ready to send, waiting for review
- Calendar: 3 draft invites with context notes
- A checkpoint summary that tells you exactly what needs your eye before anything goes out

**The before:** 2–3 hours of tab-switching, copy-pasting from tracker to email, re-reading notes, formatting Word docs, then finding calendar slots. Context lost between each app switch.

**The after:** 90 seconds. Full portfolio. Every deliverable ready for human review.

---

## CTA (10 sec)

> "Your renewal motion is only as fast as your cross-app coordination. Copilot Cowork connects the tracker, the brief, the email, and the calendar — so you spend your time on the conversation, not the assembly."
>
> Try it: `aka.ms/CopilotCowork`

---

## Pain Point Research

**Sources:**
- r/CustomerSuccess (Reddit, 2025–2026): "Every Q3 I spend Monday through Wednesday just triaging which accounts need an exec save — by the time I'm ready to send emails it's Thursday" — top comment with 340+ upvotes in a thread about CS team tools
- LinkedIn CS Leadership community (June 2026): "The problem with renewal season isn't the conversations — it's the 2–3 hours of prep work before each conversation that lives across Salesforce, email, Excel, and your notes app"
- Gainsight Customer Success Index 2025: 67% of CSMs say cross-app context switching is the #1 source of dropped renewal signals; average CSM switches between 5+ apps to prepare for a single renewal meeting
- Salesforce State of Sales 2025: Account health data, support ticket history, and email communication history are stored in different systems for 78% of enterprise CS teams — requiring manual aggregation for every QBR
- Microsoft Work Trend Index 2026: Knowledge workers switch apps an average of 10x per hour; each switch costs 20+ minutes of productive focus time daily

---

## Data File: c16_renewal_blitz.xlsx

**SharePoint:** `Microsoft/Copilot-Demos/c16_renewal_blitz.xlsx`

**Sheets:**
1. **Account Renewal Tracker** — 10 accounts, 23 columns: ARR, renewal date, days to renewal, health score, NPS, usage %, champion info, economic buyer info, open tickets, risk status (RED/AMBER/GREEN), last contact date, next action
2. **Open Support Tickets** — 28 open tickets across 7 accounts: ticket ID, priority (P1/P2/P3), days open, customer verbatim notes. 2 P1 tickets at BlueSky are contractual breach risk.
3. **Outreach Context** — CSM/AE contact info, company details, account-specific talking points, ROI stats, competitive differentiators, migration risk data
4. **Actions & Checkpoints** — 15 planned renewal actions: owner, due date, priority (CRITICAL/P1/P2/P3), outcome goal, execution notes
5. **Renewal Summary** — Pre-built portfolio dashboard: RED/AMBER/GREEN counts and ARR, renewals by time bucket, critical account table

**Baked storylines:**
- BlueSky Logistics: COO was never onboarded (signed by Ops Director), discovered tool in budget review, 23-day deadline = highest urgency in the demo
- TerraAxis Corp: Champion left June 2nd — common churn signal, tests Copilot's ability to surface relationship gaps
- Nexis Corporation: $285k ARR, 3-year customer, displaced champion from reorg — most nuanced save scenario
- Meridian + CoreLogic: Easy wins that show portfolio balance (not all accounts are on fire)
- Vantara: Expansion opportunity hiding in a Green account

---

## Difficulty: Medium
## Status: READY
