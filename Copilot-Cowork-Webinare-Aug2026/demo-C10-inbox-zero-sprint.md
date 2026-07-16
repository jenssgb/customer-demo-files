# DEMO: The Inbox Zero Sprint (C10)
**App:** Microsoft 365 Copilot Chat (BizChat) + Outlook Copilot  
**Type:** Cowork (Cross-App)  
**Duration:** ~90 seconds  
**Feature:** Work IQ · Enterprise Search · Draft Generation · Task Extraction  
**Difficulty:** Easy  

---

## HOOK (5 sec)

> "You came back from vacation to 127 unread emails.  
> Three threads are probably urgent. A dozen are FYI noise.  
> The real risk is missing the ONE customer or manager ask buried on page two.  
> This used to take 90 minutes of manual archaeology. Watch."

---

## SETUP (10 sec)

**What the viewer sees:**
- Copilot Chat open in Microsoft 365 (browser or Teams)
- Reference: `c10_inbox_sample.xlsx` — 127 unread emails with senders, subjects, categories, and urgency tags
- Context: You just returned from 8 days off. It's Monday morning.

**Demo context (on screen or spoken):**
> "I have 127 unread emails. 10 need action today. 15 need follow-up. The rest are noise.  
> I'm going to have Copilot triage the whole inbox, draft replies for the top 3 urgent threads,  
> and build me a follow-up task list — in one prompt."

---

## PROMPT (15 sec)

```
Using c10_inbox_sample.xlsx, help me triage my inbox after 8 days away.

1. PRIORITY TRIAGE: Organize all 127 emails into three buckets:
   - Action Required Today: anything that needs a reply or decision from me before EOD
   - Follow-up Needed: threads I need to respond to this week
   - FYI / Can Wait: newsletters, automations, low-urgency CC's

2. TOP 3 URGENT: For the 3 most critical "Action Required" emails, summarize
   what's at stake and what I need to do — in 2 sentences each.

3. DRAFT REPLIES: Write replies for Email #1 (Nexis Corp escalation),
   Email #3 (F-14 scope cut), and Email #5 (Board deck input needed by noon).
   Tone: professional, direct, no filler.

4. FOLLOW-UP TASK LIST: Create a bulleted list of all follow-up items with
   suggested deadlines (P1 = today, P2 = this week, P3 = this month).
```

---

## MAGIC — What Copilot Does (40 sec)

1. **Triage across 127 rows** — reads sender, subject, urgency tag, key ask, and thread size simultaneously
2. **Priority bucketing** — groups into Action Required (10), Follow-up (9), FYI (8), Can Wait (100)
3. **Risk surfacing** — flags that #1 (Nexis Corp) has a 3pm client deadline, #3 (F-14) blocks 3 sprints and is already 48h overdue, #5 (Board deck) closes at noon
4. **Draft generation** — writes three distinct replies in context-appropriate tone:
   - Nexis escalation: empathetic, action-oriented, routes to CSM
   - F-14 scope cut: asks for impact analysis before committing
   - Board deck: concise 2-sentence Q3 narrative
5. **Task extraction** — outputs a structured P1/P2/P3 follow-up list with suggested deadlines based on urgency signals in the data

---

## RESULT (15 sec)

**Show on screen:**
- Priority summary table (Action/Follow-up/FYI/Can Wait counts)
- 3 ready-to-send email drafts in message format
- Bulleted task list with P1–P3 tags and deadlines

**Highlight the wow moments:**
- 127 emails → actionable triage in seconds
- 3 drafts written in the correct tone without prompting the style separately
- Zero missed urgency signals (Nexis 3pm deadline, F-14 board call, offer expiry today)

> "What used to be 90 minutes of inbox archaeology is now a 30-second prompt.  
> Copilot reads the urgency signals, writes the replies, builds the task list.  
> You start Monday morning with a clear head — not a full inbox."

---

## CTA (10 sec)

> "Try it with your own inbox.  
> Start with: 'Organize my inbox from the past week by urgency.  
> Draft replies for the top 3 threads and give me a follow-up task list.'  
> Copilot Chat. Microsoft 365. Link in bio."

---

## Pain Point Sourcing

- **Microsoft Work Trend Index 2025–2026:** Knowledge workers interrupted every 2 minutes; 275+ interruptions/workday
- **Atlassian 2025:** Average knowledge worker receives ~300 business emails/week, checks inbox 30x/hour
- **cloudHQ / Superhuman blog:** Email consumes up to 28% of the knowledge workweek (5–15.5 hrs/week depending on role)
- **r/Outlook, r/productivity:** "Back from PTO inbox archaeology" is a perennial top-upvoted frustration
- **Microsoft Work Trend Index 2026:** 67% of knowledge workers dread the post-vacation inbox as much as the actual backlog

**Why this resonates:**
> "Everyone has lived this. You take 5 days off. You come back to chaos.  
> The anxiety isn't the 127 emails — it's the fear that something critical is buried in there  
> and you won't find it until it's too late. Copilot removes that anxiety entirely."

---

## Data File

**File:** `c10_inbox_sample.xlsx`  
**SharePoint:** `Microsoft/Copilot-Demos/c10_inbox_sample.xlsx`  
**URL:** https://bluepolicy.sharepoint.com/sites/openclaw-data-agent/_layouts/15/Doc.aspx?sourcedoc=%7B373FEDDA-0292-49FE-9891-D62DDC65248F%7D&file=c10_inbox_sample.xlsx&action=default&mobileredirect=true

**Sheets:**
1. `Inbox (127 Unread)` — 127 rows: EmailID, Received, From, Title, Subject, Category, Urgency, Action, Est_Minutes, Thread_Size, Attachments, CC_Count, Key_Ask, Notes
2. `Priority Summary` — Urgency breakdown with counts and estimated time
3. `Draft Replies Needed` — 10 emails with draft tone guidance

**Key hooks baked in:**
- **Email #1:** Nexis Corp SLA breach — client demands call by 3pm, CFO copied
- **Email #3:** F-14 scope cut 40% — blocks 3 sprints, already 48h overdue
- **Email #5:** CEO asking for board deck input by noon
- **Email #10:** Staff Engineer offer expiring at 5pm today (competing offer)
- **Email #11:** Vertex AI integration assigned to your team while you were out
- **10 Action Required** emails, **9 Follow-ups**, **8 FYI**, **100 Can Wait**

---

## LinkedIn Post Draft

**Hook:**
> You come back from vacation to 127 unread emails.  
> 3 are urgent. 12 are noise. 1 is a crisis you don't know about yet.  
> Finding it manually takes 90 minutes. Or one Copilot prompt.

**Visual:** Screen recording of triage → 3 drafts generated in <10 seconds

**Body:**
> "Triage my inbox. Draft replies for the top 3 urgent threads. Build me a follow-up task list."  
> That's the whole prompt.  
> Copilot reads sender, urgency, thread context — flags the Nexis escalation with a 3pm deadline,  
> drafts a reply to the CEO's board deck ask, and builds a P1/P2/P3 task list.  
> Monday mornings just got a lot less anxious.  
> M365 Copilot. Inbox Zero. 30 seconds.

**CTA:** "What does your Monday morning look like without inbox dread? Drop it below 👇"
