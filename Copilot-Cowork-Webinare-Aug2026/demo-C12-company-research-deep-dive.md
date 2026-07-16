# DEMO C12: The Company Research Deep Dive

**APP:** Microsoft 365 Copilot Chat (BizChat) + Deep Research  
**TYPE:** Cowork — Multi-App (BizChat Deep Research → Word → Outlook)  
**DURATION:** ~90 seconds  
**DIFFICULTY:** Medium  
**FEATURE:** Deep Research, Work IQ, web grounding, Word output

---

## HOOK (5 sec)

> "Prospect meeting tomorrow morning. The invite says 'strategic partnership discussion' — and you know almost nothing about them beyond the domain name. You've got 20 minutes and a lot of tabs to open. Or one prompt."

---

## THE PAIN POINT

Sales prep is universally painful:
- Manually search the company website, Crunchbase, LinkedIn, recent news
- Open 8–12 browser tabs, copy-paste snippets into a notes doc
- Cross-reference pain points, stakeholders, recent announcements
- Write a briefing that's already 2 hours of work before the first slide

**Research sources:** r/sales, LinkedIn enterprise sales community, Microsoft Work Trend Index 2026 — *"pre-call research consumes up to 90 minutes per strategic meeting, and reps still walk in missing key signals"*

**Manual effort:** 1–2 hours of tab archaeology. Typical quality: shallow. Stakeholder context: guesswork. Pain points: uncorroborated.

---

## SETUP (10 sec)

> "You're a Microsoft Partner sales executive. You have a meeting tomorrow with Andreas Müller, VP Enterprise EMEA at Nexaris Technologies. The invite came in as 'strategic partnership discussion.' You open Copilot Chat."

Supporting context file uploaded: `c12_prospect_brief.xlsx`  
*(4 sheets: Prospect Overview, Recent News & Events, Stakeholder Map, Pain Points & Pitch Angles — use as grounding for the demo or let Copilot research independently)*

---

## PROMPT (10 sec)

```
Research Nexaris Technologies (nexaris.io) for my strategic partnership meeting tomorrow with Andreas Müller, their VP Enterprise EMEA.

Using web research and any context in c12_prospect_brief.xlsx, create a 2-page Meeting Briefing Doc:

1. COMPANY SNAPSHOT — size, revenue, funding, key products, top customers, tech stack
2. RECENT SIGNALS — last 90 days: product launches, hiring moves, funding, exec statements, analyst coverage
3. KEY STAKEHOLDERS — Andreas Müller + 3 others I should know before walking in. For each: role, influence level, LinkedIn signal, conversation hook.
4. PAIN POINTS — top 3 business challenges Nexaris faces right now, with evidence
5. OUR ANGLE — how Microsoft 365 Copilot and the M365 platform addresses each pain point (1 sentence each)
6. OPENING QUESTIONS — 3 sharp questions to ask Andreas in the first 10 minutes that show we've done our homework

Format: clean Word doc, 2 pages max, save to OneDrive as 'nexaris-meeting-brief-2026-07-16.docx'. Tone: confident, specific, no filler.
```

---

## WHAT COPILOT DOES (40 sec)

**Step 1 — Deep Research triggers:**
- Searches web for Nexaris Technologies: company profile, Crunchbase/PitchBook signals, recent press releases, G2 reviews
- Finds: Series D $40M (Mar 2025), NexaAI 3.0 launch (Jun 2026), Gartner MQ Challenger, Snowflake partnership, EMEA expansion

**Step 2 — Work IQ scan (if internal context exists):**
- Checks for prior email threads, meeting notes, or CRM records mentioning Nexaris
- Surfaces: any previous touchpoints, existing contacts, prior proposals

**Step 3 — Stakeholder research:**
- Finds LinkedIn profiles: Lena Richter (CEO), James Tao (CTO), Andreas Müller, Sofia Hernandez (Partnerships)
- Cross-references recent posts and public signals

**Step 4 — Synthesizes into Word doc:**
- Structured 2-page briefing with all 6 sections
- Pain points backed by G2 reviews, Gartner placement, and exec LinkedIn statements
- M365 angles mapped to each pain: Copilot Studio no-code, Purview governance, Fabric integration

**Step 5 — Saves to OneDrive:** `nexaris-meeting-brief-2026-07-16.docx`

---

## RESULT (15 sec)

> "A 2-page, evidence-backed meeting briefing. Company snapshot, stakeholder map, pain points with sources, and sharp opening questions — ready in 60 seconds."

**Wow moments to highlight:**
- Copilot found the Gartner MQ Challenger placement *and* the G2 review pain point about no-code gaps
- Stakeholder section includes LinkedIn signals and conversation hooks
- Pain-to-pitch mapping is done automatically — no manual research-to-pitch translation
- Saved to OneDrive, ready to share with the AE before the meeting

---

## WITHOUT COPILOT — MANUAL PATH

1. Google "Nexaris Technologies" → Crunchbase → LinkedIn → PitchBook (4+ tabs, 15 min)
2. Search recent news, press releases, TechCrunch (20 min)
3. Find and read all stakeholder LinkedIn profiles (15 min)
4. Look up G2 reviews, analyst coverage (10 min)
5. Write the briefing doc from scratch (30–45 min)
6. Format, edit, share with team (10 min)

**Total: 90–120 minutes per strategic meeting.** Most reps skip half of it. The result: shallow prep, missed signals, and questions that could have been Googled.

---

## CTA (10 sec)

> "Open Copilot Chat before your next prospect meeting. One prompt. Two pages. Walk in knowing more than your prospect expects you to."

**Try it:** microsoft365.com/copilot

---

## LINKEDIN CAPTION (DRAFT)

> "Sales prep used to be 2 hours of tab archaeology.
> 
> Website → Crunchbase → LinkedIn → G2 → TechCrunch → copy-paste into a notes doc → try to remember what you read.
> 
> I asked M365 Copilot to research a prospect and create my meeting brief. One prompt.
> 
> It found their Gartner MQ placement, the exact pain point buried in their G2 reviews, the CEO's LinkedIn post from last week, and their recent product launch — then mapped all of it to our pitch angles.
> 
> 60 seconds. 2-page Word doc. Saved to OneDrive.
> 
> The best prep I've ever walked into a partnership meeting with.
> 
> #MicrosoftCopilot #M365 #SalesEnablement #AIatWork"

---

*Generated: 2026-07-13 | Demo Library C12 | Type: Cowork (BizChat Deep Research)*
