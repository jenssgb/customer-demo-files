# DEMO: C13 — The Event Planner
**APP:** Microsoft 365 Copilot (Multi-App: Word + Outlook + Calendar + OneNote)
**TYPE:** Cowork — Multi-Step Cross-App
**DURATION:** ~90 seconds
**FEATURE:** Edit with Copilot + Work IQ + Scheduled Prompts

---

## HOOK (5 sec)
> "Team offsite is in three weeks. Fifteen people, dietary restrictions, parking questions, a strategy morning, a workshop afternoon — and nobody has created the agenda, invites, logistics email, or shared notes space yet. That's four apps, one afternoon, zero time."

---

## SETUP (10 sec)

**What the viewer sees:**
- File open: `c13_team_list.xlsx` in SharePoint (Microsoft/Copilot-Demos)
  - 15 team members: name, email, role, dietary restrictions, parking needs, T-shirt sizes
  - Summary sheet: event date (July 26, 2026), location, schedule
- Copilot sidebar open in Word

**Context:**
Sarah Mitchell (VP Engineering) just confirmed the offsite venue: The Workshop SF, 420 Bryant St. 15 people. She has the team list — and nothing else. No agenda doc, no invites sent, no logistics email, no shared OneNote. Three weeks to go. This is the kind of thing that eats a full afternoon manually.

---

## PROMPT (10 sec)

```
Plan our team offsite for July 26. 15 attendees from c13_team_list.xlsx.

1. Create agenda (Word): morning strategy session 9am–12pm, afternoon workshop 1–5pm, team dinner 6:30pm at The Workshop SF. Include dietary notes from the team list.

2. Send calendar invites to all 15 attendees. Add location, parking note for the 7 who need it, and agenda summary in the invite body.

3. Draft logistics email with venue address (420 Bryant St, San Francisco), parking options, dress code (smart casual), and dietary accommodation confirmation for each attendee.

4. Create a shared OneNote notebook "Q3 Offsite 2026" with sections: Agenda, Strategy Session Notes, Workshop Output, Action Items, Decisions Made.
```

---

## MAGIC (40 sec)

**What Copilot does — step by step:**

1. **Reads the team list** — pulls all 15 names, emails, roles, dietary restrictions, and parking flags from `c13_team_list.xlsx` via Work IQ
2. **Creates the agenda in Word** — structures the day with timed blocks, adds a dietary requirements summary table at the end (4 restrictions: gluten-free, vegan ×2, halal ×2, nut allergy, lactose-free), includes facilitator notes per session
3. **Drafts calendar invites** — one per attendee, personalized: parking note only for the 7 who flagged it, dietary confirmation included, agenda embedded in body
4. **Writes the logistics email** — addresses all 15, mentions venue + Google Maps link, parking garage options nearby ($18/day), dress code, dietary confirmation, RSVP deadline
5. **Scaffolds the OneNote** — creates the notebook with 5 pre-structured sections ready for the day, pins it to the Teams channel

**Checkpoint at the end:**
> "Done. Agenda doc created (8 pages), 15 calendar invites drafted, logistics email ready to review, OneNote notebook live. 3 items flagged for your review: Fatima and Omar have Halal-only requirement — confirm caterer. Aisha has a nut allergy — flagged in all docs. 7 parking invites include garage note."

---

## RESULT (15 sec)

**Show:**
- Word agenda: clean 8-page doc, timed agenda blocks, dietary table
- Calendar: 15 draft invites, each personalized with parking/dietary notes
- Logistics email: addresses all, covers every detail, ready to send
- OneNote: 5 sections structured and ready

**Highlight:**
- **Before:** 4 apps, ~3 hours minimum. Manually build agenda, copy-paste 15 emails, write 15 calendar invites by hand, remember dietary restrictions, set up OneNote from scratch.
- **After:** 90 seconds. Every deliverable, every detail, every attendee covered — and Copilot flagged the 3 dietary items that need a human confirmation before anything goes out.

---

## CTA (10 sec)
> "Your next offsite package: 4 apps, 15 people, 90 seconds. Try it with your own team list → aka.ms/tryCopilot"

---

## Pain Point Research

**Source:** r/ExecutiveAssistants (2024–2026)
- "I hate event planning" — top-voted EA thread: the *logistics coordination* (dietary restrictions, parking, calendar wrangling) is the most-cited time sink, not the strategy
- "Corporate offsite prep" — 3–4 hour minimum for 15 people: agenda (Word), calendar invites (Outlook × 15), logistics email, shared notes space (OneNote/Teams)
- r/projectmanagement: "The actual planning is fine — it's the 15 separate calendar invites and chasing dietary restrictions that destroys the afternoon"
- Microsoft Work Trend Index 2026: Cross-app coordination (doc → calendar → email → notes) is cited as top-3 knowledge-work friction for EAs and team leads

**The real manual path:**
1. Open Word → blank agenda → type from scratch → 45 min
2. Open Outlook → create calendar event → duplicate 14 times → personalize each → 45 min
3. Compose logistics email → manually reference dietary notes → 20 min
4. Open OneNote → create notebook → add sections → 15 min
5. **Total: ~2–2.5 hours minimum. For a competent EA. On a good day.**

---

## Files
- **Data:** `c13_team_list.xlsx` (SharePoint: Microsoft/Copilot-Demos/c13_team_list.xlsx)
  - Sheet 1: 15 attendees — name, email, role, department, dietary restrictions, parking needed, T-shirt size, emergency contact
  - Sheet 2: Summary — event details, date, location, dietary count, schedule

## Metadata
- **Demo ID:** C13
- **Type:** Cowork (Multi-Step Cross-App)
- **Apps:** Word + Outlook + Calendar + OneNote
- **Difficulty:** Medium
- **Created:** 2026-07-15
