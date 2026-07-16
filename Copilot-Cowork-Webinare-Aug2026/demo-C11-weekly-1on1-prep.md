# DEMO C11: The Weekly 1:1 Prep

**APP:** Microsoft 365 Copilot (Work IQ — Cross-App)
**TYPE:** Cowork (Multi-App: Outlook + Tasks + Teams + OneDrive)
**DURATION:** ~90 seconds
**FEATURE:** Work IQ · Cross-App Context · Scheduled Prompts

---

## HOOK (5 sec)

> "Your 1:1 with your manager is in 30 minutes. You know you had a good week. But the evidence is scattered across 12 sent emails, 6 completed tasks, three Teams threads, and two meeting notes you typed on your phone. You have no agenda and no idea what to say first."

---

## THE PAIN POINT

r/managers, r/ProductManagement, LinkedIn manager communities 2025–2026:

> *"I show up to 1:1s underprepared and forget half my wins and blockers."*
> *"My manager asks what I worked on this week and I stall for 10 seconds — and I actually DID a lot."*
> *"I keep a running doc for 1:1 prep but never have time to update it."*

This is one of the highest-frequency recurring pains in knowledge work. Every week, every manager, same ritual: 15 minutes before the meeting, scrambling to remember what you did.

**The manual path:**
- Scroll through Sent Items (5 min)
- Check Tasks/Planner for completed items (3 min)
- Skim Teams notifications for project threads (5 min)
- Re-read calendar for meetings with context (3 min)
- Write the agenda from memory, hoping you didn't forget anything (5 min)

**Total: 21 minutes of archaeology, every single week.** Times 50 weeks — that's 17+ hours/year, mostly before you've had your second coffee.

---

## SETUP (10 sec)

*You're playing Marcus Webb, Senior Engineering Manager at Meridian Analytics. Your 1:1 with VP of Engineering is in 30 minutes. You open Copilot Chat.*

---

## THE PROMPT

```
Prepare my weekly 1:1 with my VP for today's meeting in 30 minutes.

Pull context from:
- My sent emails from this week
- My completed tasks and open action items in Tasks
- My Teams channels and @mentions from the past 7 days
- My calendar meetings this week and their notes

Create a 1-page briefing with:
1. TOP 3 WINS THIS WEEK — my most impactful completed work, quantified where possible
2. BLOCKERS & ESCALATIONS — anything I need my VP's help to unblock
3. DECISIONS NEEDED — topics I need a call on before next week
4. WHAT I'M WORKING ON NEXT — top 3 priorities for the coming week
5. ONE QUESTION I WANT THEIR INPUT ON — the most important thing I want their perspective on

Tone: confident, concise, honest. One page. No filler. Save to OneDrive as '1on1-prep-2026-07-01.docx'.
```

---

## WHAT HAPPENS (40 sec)

**Copilot's multi-step execution:**

1. **Searches Sent Items** — pulls 5 emails sent this week, extracts outcomes: "Replied to Nexis Corp renewal → confirmed 12-month extension", "Sent F-14 architecture decision to team"
2. **Checks Tasks** — reads 6 completed tasks, 4 open: "Closed P0 incident review", "Delivered Q2 engineering capacity report"
3. **Scans Teams threads** — pulls @mentions and project channel updates: "F-14 scope discussion", "New hire onboarding for Priya"
4. **Reviews calendar** — reads meeting notes from standups, design reviews, the customer call
5. **Synthesizes into a 1-page briefing** — clean, structured, with specific quantified outcomes
6. **Creates Word doc** → saves to OneDrive automatically

---

## THE RESULT (15 sec)

A clean 1-page 1:1 prep brief in Word, automatically saved to OneDrive:

| Section | What it shows |
|---------|--------------|
| Top 3 Wins | F-14 architecture decision shipped, Nexis renewal confirmed ($240k ARR), P0 incident MTTR down 40% |
| Blockers | Vertex AI integration blocked on Legal review — need VP to escalate |
| Decisions Needed | Q3 headcount: approve 2 IC hires before Friday close |
| Next Week Focus | Priya onboarding, F-14 v2 kickoff, Q3 capacity planning |
| One Question | Should we delay the public API launch given the security review timeline? |

*From 21 minutes of manual archaeology to 60 seconds and a polished Word doc.*

---

## CTA (10 sec)

> "Every manager who does weekly 1:1s could save 15–20 minutes a week. That's a full day back per quarter — just from prep. Try it with your next 1:1."

---

## DEMO NOTES

- **No data file needed** — Copilot pulls live context from Work IQ (Outlook, Tasks, Teams, Calendar)
- **For demo purposes**: use the talking points above as the "expected output" narrative
- **Cowork type**: shows cross-app context aggregation in a single prompt
- **Scheduled prompt variant**: mention that this can be set up as a daily recurring task (C14 demo)
- **Difficulty**: Easy — audience immediately gets it, everyone has 1:1s

---

## LINKEDIN CAPTION IDEA

> **"Your 1:1 is in 30 minutes. You've had a great week. You have no agenda."**
>
> Sound familiar?
>
> One prompt to Copilot pulls your wins from sent mail, your blockers from Tasks, your project updates from Teams, and your meeting context from Calendar — and writes a 1-page prep brief in 60 seconds.
>
> 21 minutes of archaeology → 60 seconds.
> Every week. Without the scramble.
>
> #MicrosoftCopilot #M365 #Productivity #FutureOfWork
