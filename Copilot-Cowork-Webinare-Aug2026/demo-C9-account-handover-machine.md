# DEMO C9: The Account Handover Machine

**APP:** Copilot Cowork (Cross-App: Excel + Word + Outlook)
**DURATION:** ~90 seconds
**FEATURE:** Edit with Copilot / Cowork Multi-Step / Work IQ
**CREATED:** 2026-06-12
**STATUS:** READY

---

## THE STORY

> "Your top account executive just resigned. Last day is Friday. They own 8 accounts — $1.19M in ARR. Three of those accounts renew in the next 30 days. Two are already at risk. You have one afternoon to extract everything from their head and turn it into a handover kit the new owner can actually use."

**Why this resonates:**
- Sales leadership's #1 nightmare: key rep departure during renewal season
- Average rep carries relationship context that *doesn't live in CRM* — only in emails, call notes, and memory
- Manual handover: 4–6 hours of interviews, note-taking, formatting, and email writing
- Sources: r/sales, r/salesforce, LinkedIn Sales Community 2025–2026 — "account handover with renewals in flight" consistently top-voted nightmare scenario; Salesforce State of Sales 2025: 62% of reps say their CRM doesn't capture enough relationship nuance for a real handover

---

## HOOK (5 sec)

> "Your best rep just quit. Friday is their last day. $1.19M in accounts, three renewals in 30 days. You have one afternoon."

---

## SETUP (10 sec)

Open `c9_account_handover.csv` on SharePoint — 8 accounts with health scores, renewal dates, open commitments, relationship notes, escalation flags, and stakeholder contacts.

The spreadsheet is a raw data export — relationship context buried in text columns, priorities unclear, no structure for the new owner.

---

## PROMPT (shown on screen)

```
Using c9_account_handover.csv, build me a complete account handover kit for the incoming account owner.

1. PRIORITY TRIAGE (Excel, new sheet): Rank all 8 accounts by urgency. Color-code by HandoverPriority (P1-CRITICAL = red, P2-HIGH = orange, P3-MEDIUM = yellow, P4-MONITOR = green). Add columns: DaysToRenewal, ARR, HealthScore, RenewalRisk (flag accounts with HealthScore < 65 AND DaysToRenewal < 45 as HIGH RISK), TopAction (pull from OpenCommitments). Sort P1 accounts to top.

2. RELATIONSHIP BRIEF (Word, 1 page per P1 account — 3 docs total):
   For each P1 account (Meridian, Aurelius, Castellan):
   - Account snapshot: ARR, renewal date, health score, NPS
   - Who's who: decision-maker vs operator, relationship dynamics
   - Current status: open tickets, escalations, last contact
   - Open commitments: what was promised, by when
   - Landmines: what NOT to say or do on first call
   - Recommended first action in Week 1

3. INTRO EMAILS (Outlook drafts, one per P1 stakeholder): Write a warm, professional introduction email from the new account owner to the primary stakeholder of each P1 account. Reference the relationship context naturally — show you've done your homework. Don't mention the rep departure directly unless relationship notes suggest it's better to be transparent.
```

---

## WHAT COPILOT DOES (The Magic — 40 sec)

**Step 1 — Excel Triage Sheet:**
Copilot reads all 32 columns, calculates renewal urgency, applies conditional formatting with color-coded priority bands, adds RenewalRisk formula logic (HealthScore < 65 AND DaysToRenewal < 45), and sorts P1 accounts to top.

*Wow moment: It spots that Aurelius (renewal in 18 days, health 45, 3 escalated tickets) is the single most critical account — something that would take a human 20 minutes to triangulate from the raw data.*

**Step 2 — Relationship Briefs:**
Three Word documents, one per P1 account. For Meridian: "Thomas is skeptical after onboarding delays — Sandra Kowalski is your real champion. Ping Sandra first, bring data to every Thomas conversation." For Aurelius: "Do NOT promise anything without checking with our legal team — there's an active DLP policy dispute." For Castellan: "The adoption playbook promised by June 20 is non-negotiable for renewal — Roberta is under board pressure to show AI ROI."

*Wow moment: The "landmine" section. Relationship context that would normally live only in the departing rep's head — surfaced, structured, actionable.*

**Step 3 — Intro Emails:**
Three Outlook drafts, each personalized. To Sandra at Meridian: references the compliance dashboard commitment, confirms it's on track for June 30. To David at Castellan: acknowledges the Copilot adoption work, promises playbook delivery this week. To Karl-Heinz at Aurelius: warm tone, doesn't mention the legal dispute but asks for a call to understand current priorities.

*Wow moment: Each email reads like it was written by someone who's been on the account for 6 months.*

---

## RESULT (15 sec)

- Excel: 8 accounts ranked, color-coded, risk-flagged — new owner knows in 10 seconds where to spend their first week
- Word: 3 relationship briefs — the institutional knowledge that would otherwise walk out the door Friday
- Outlook: 3 introduction emails ready to send Monday morning

**Time saved:** What used to take 4–6 hours of knowledge transfer interviews + manual write-up → 90 seconds.

---

## CTA (10 sec)

> "The relationship context that lives in your rep's head? It doesn't have to walk out with them. Try this prompt with your next account handover."

---

## DATA FILE DETAILS

**File:** `c9_account_handover.csv`
**SharePoint:** `Microsoft/Copilot-Demos/c9_account_handover.csv`
**Rows:** 8 accounts
**Columns:** 32 (AccountID, CompanyName, Industry, Region, Tier, ARR, RenewalDate, DaysToRenewal, HealthScore, NPS, contacts, open commitments, relationship notes, handover priority)

**Baked-in storytelling hooks:**
- 3 P1-CRITICAL accounts with renewals in 18–26 days
- Aurelius: legal dispute, 7 open tickets, rep explicitly warns "do NOT promise anything"
- Meridian: hidden champion dynamic (CTO skeptical, IT Director is real ally)
- Castellan: CEO-level AI ROI pressure, non-negotiable playbook deadline
- GreenFlux: NPS 10, 96% license usage — reference/case study candidate hidden in noise
- Total ARR: $1,186,000 across 8 accounts

---

## LINKEDIN HOOK IDEAS

- "Your best rep just quit. Three accounts renew in 30 days. I asked Copilot to build the handover kit. Here's what happened."
- "62% of sales relationship context never makes it into CRM. This is what Copilot does with the 38% that does."
- "The 'institutional knowledge walking out the door' problem — solved in 90 seconds."
