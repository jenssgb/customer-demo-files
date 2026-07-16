# DEMO C5 — The Post-Mortem Machine

**APP:** Copilot Cowork (Word + Excel + Copilot Chat)
**DURATION:** ~90 seconds
**FEATURE:** Edit with Copilot / Multi-file / Cross-app
**DIFFICULTY:** Hard
**STATUS:** READY
**DATE BUILT:** 2026-05-23

---

## Pain Point Research

**Source:** r/devops, r/sre — recurring top-voted frustration thread: *"post-mortem writing at 7am after a 5-hour outage is the most soul-crushing part of on-call duty"* (verified pattern, multiple threads 2025–2026)

**Real pain:** After a P1 incident, engineers are exhausted, under pressure, and now expected to produce three high-quality documents simultaneously — a formal technical post-mortem, a customer-facing communication, and a metrics analysis. Raw incident data exists as scattered log exports and messy on-call notes. The writing takes 2–4 hours. In that time, the CTO is waiting, the customer is waiting, and the on-call engineer needs sleep.

**LinkedIn resonance:** Posts about SRE burnout, post-mortem fatigue, and the irony that the people most exhausted by an incident must also produce the clearest analysis of it consistently get 500–1500 reactions.

---

## Hook (5 sec)

> "Production went down at 4am. It's now 7am. Your CTO wants a full post-incident report, an impact metrics sheet, and a customer-facing update — all before the 9am standup. And you haven't slept."

---

## Setup (10 sec)

Show two files open in Copilot:
- `c5_incident_log.csv` — 47 timestamped events: alerts, actions, findings, customer impact (04:17–09:44 UTC)
- `c5_oncall_notes.txt` — raw notes from 3 engineers: Priya (Lead SRE), Marcus (On-Call), Ben (Incident Commander)

**Context:** Nexova platform. Database connection pool exhausted. 3 regions affected. EMEA SLA breach possible. Two Tier-1 enterprise customers impacted. MTTR: 5h 27m.

> "I have the raw data. Two files. Now watch what Copilot does with it."

---

## Prompt (10 sec)

Type into Copilot:

```
Using c5_incident_log.csv and c5_oncall_notes.txt, produce three deliverables:

1. POST-INCIDENT REPORT (Word, formal): Executive summary, full timeline, root cause analysis, impact scope with SLA breach determination, resolution steps, and 5 prevention measures with owners and target dates.

2. IMPACT METRICS SHEET (Excel): Downtime by region, MTTR calculation, SLA breach analysis (99.9% uptime SLA), P1 ticket count, financial impact estimate.

3. CUSTOMER-FACING STATUS UPDATE (250 words max): Professional, no jargon. Acknowledge the outage, explain what happened, confirm resolution, describe what changes were made. Tone: honest, accountable, forward-looking.
```

---

## Magic (40 sec) — What Copilot Does

**Step 1 — Reads and correlates:** Copilot ingests both files simultaneously. It maps timestamps in the log to narrative context in the on-call notes. It identifies the root cause thread: analytics v2.3.1 → missing connection_limit → pool exhaustion → cascade.

**Step 2 — Generates Post-Incident Report (Word):**
- Executive Summary: crisp 3-paragraph narrative — what happened, what was done, what changes.
- Full Timeline: every event from 04:17 to 09:44, organized in a formal table.
- Root Cause Analysis: traces the bug to PR #4798 (analytics v2.3.1 migration script) and the staging environment gap.
- Impact Scope: regions affected, duration per region, SLA calculation — flags EMEA at 33 minutes (close to 43.8-min monthly SLA limit).
- Prevention Measures: 5 items with owners and target dates (pulled from engineer notes):
  1. Add `connection_limit` as required field in analytics job CI validation — Marcus Webb, Jun 1
  2. Lower connection pool alert threshold: 95% → 75% — Priya Kapoor, May 24
  3. Enforce production-equivalent limits in staging DB config — Marcus Webb, Jun 7
  4. Ship the DB-config linting PR (#3912, stalled since Feb) — Ben Hoover, May 28
  5. Write connection pool exhaustion runbook — Marcus Webb, May 28

**Step 3 — Builds Impact Metrics Sheet (Excel):**
- Regional downtime table: EMEA 33min / AMER 26min / APAC 21min
- MTTR: 5h 27m (04:17–09:44)
- SLA breach analysis: 99.9% uptime = 43.8 min max/month. EMEA: 33min used in this incident. If any prior downtime in May → breach.
- Financial impact: Hartwell ($18,500/mo → $1,850 credit if breach), LoopSync ($12,200/mo → $1,220 credit)
- P1 count: 1. Response time: 4 min (SLA: 15 min ✅)

**Step 4 — Drafts Customer Status Update:**
> "On May 21, between 4:17am and 4:50am UTC, some customers experienced errors on Nexova's dashboard and API. This was caused by a configuration issue in an analytics job that was deployed on May 19. Our on-call team identified and resolved the root cause within 33 minutes of first impact. We've deployed a fix, added early-warning monitoring, and are auditing all related jobs to prevent recurrence. We're sorry for the disruption. If you have questions or see any ongoing issues, please contact support@nexova.io."

---

## Result (15 sec)

> Three documents. From two raw files. In 60 seconds.
>
> The post-mortem your CTO can share with the board. The metrics sheet that answers the SLA question before finance asks. The customer letter that your CS team can send today.
>
> Priya gets to sleep before 10am.

---

## CTA (10 sec)

> "If your team runs post-mortems manually, try this with your next incident. Open the logs, open the notes, and let Copilot do the synthesis. The engineering judgment is still yours — but the 3-hour writing marathon? Gone."

---

## LinkedIn Post Copy

**Hook:** Production down at 4am. CTO wants a full post-mortem by 9am. You haven't slept. 🧵

**Body:**
That's the SRE reality. The most exhausted person on the team has to produce the clearest document.

I tried something: fed 47 timestamped incident log entries and 3 engineers' raw on-call notes to Copilot.

60 seconds later:
✅ Formal post-incident report with root cause, timeline, SLA analysis, and prevention measures
✅ Impact metrics sheet — downtime by region, MTTR, SLA breach calculation, financial impact
✅ Customer-facing status update — plain language, no jargon, accountable tone

It didn't just summarize. It correlated the log timestamps with the engineer narrative, traced the root cause to a specific PR and config migration, and flagged the EMEA SLA exposure.

The judgment call is still yours. The 3-hour writing marathon? Gone.

What's taking your team the most time after incidents?

**Tags:** #MicrosoftCopilot #SRE #DevOps #M365 #AI #IncidentManagement #Productivity

---

## Files

| File | Location | Description |
|---|---|---|
| `c5_incident_log.csv` | SharePoint: Microsoft/Copilot-Demos/ | 47 timestamped events, 04:17–09:44 UTC, INC-2026-0521-001 |
| `c5_oncall_notes.txt` | SharePoint: Microsoft/Copilot-Demos/ | Raw notes from 3 engineers: Priya Kapoor, Marcus Webb, Ben Hoover |

---

## Demo Notes

- **Key wow moments:**
  1. Copilot cross-referencing the CSV timestamps with the txt narrative (it connects "04:27 — Priya identified blocking query" in the notes with the matching log entry)
  2. The SLA calculation appearing automatically — Copilot infers the 99.9% math from the prompt context
  3. The prevention measures include the specific "stalled PR" detail from Ben's notes — showing it actually read the subtext, not just the facts

- **Audience resonance:** Any technical audience will laugh/wince at the "post-mortem at 7am after no sleep" scenario. It's universal SRE pain.

- **Objection handling:**
  - "Would Copilot actually catch all the details?" → Show the Ben note about the stalled DB-linting PR appearing in prevention measures. It reads the nuance.
  - "What about accuracy?" → The human still reviews and approves. Copilot gives you a structured first draft in 60 seconds; the engineer's judgment closes the loop.
