# DEMO C2 — The Board Pack
**App:** Copilot Cowork (Excel + Word + PowerPoint — Cross-App Flow)
**Duration:** ~120 seconds
**Feature:** Edit with Copilot · Cross-App / Cowork Mode · Work IQ

---

## THE PAIN POINT THAT INSPIRED THIS

*From r/excel (341 upvotes, May 2025):*
> "Finally ditched the copy-paste chaos. My reports update themselves now. We used to spend hours each week copying data from different systems into slides."

This is board pack week in every finance team, every quarter. Someone — usually a senior analyst or an EA — spends 1.5 to 2 days doing the following manually:

1. Open the Q1 financial model in Excel — manually note all the numbers
2. Open the CEO update draft in Word — skim for the narrative
3. Open last quarter's board deck — update 30 slides one by one
4. Copy the revenue number. Paste. Format it. Copy the next number. Paste. Format it.
5. Regenerate the charts. Fix the colors. Update the speaker notes.
6. Realize the numbers on slide 7 don't match slide 4. Fix. Break something else.

Industry data: finance teams report spending **16–24 hours** per quarter on board pack preparation — copying numbers between Excel, Word, and PowerPoint. Most of that time is not thinking. It's formatting.

Microsoft Copilot (Edit with Copilot in cross-app / Cowork mode) does all of it in one prompt.

---

## HOOK (5 sec)

> "Board meeting. Three days. Financials in Excel. CEO narrative in Word. Last quarter's deck has 30 slides. This normally takes two days. Watch what Copilot does in 90 seconds."

---

## SETUP (15 sec)

Show three open files side by side:
- **q1_board_financials.csv** — 24 KPIs across 5 categories (Revenue, Profitability, Customers, Sales, Operations). Q1 2026 actuals vs targets vs prior year. Status and Slide_Ref columns.
- **ceo_update.docx** — CEO's Q1 narrative: top 3 wins, 2 risks, 3 strategic Q2 priorities
- **company_template.pptx** — LoopSync brand template (custom colors, fonts, layouts)

Mention: "Normally I'd be spending the next two days manually pulling numbers from Excel and pasting them into slides. Not today."

---

## PROMPT (15 sec)

Open Copilot in PowerPoint (or M365 Copilot Chat with file access). Paste or type:

```
Create a board meeting pack from these three files:

1. Open q1_board_financials.csv and extract the key financial highlights for Q1 2026: Total Revenue, ARR, Gross Margin, EBITDA, Net Income, NRR, New Logos, Win Rate, and Cash Position — with actuals vs target and prior year.

2. Open ceo_update.docx and extract: top 3 wins this quarter, top 2 risks with RAG status, and the 3 strategic Q2 priorities.

3. Build a 15-slide PowerPoint using company_template.pptx:
   - Slide 1: Title (Board Meeting Q1 2026, April 15, 2026)
   - Slide 2: Executive Summary (financial health, strategic progress, key risks — 3 bullets)
   - Slides 3–7: Financial Highlights — one KPI per slide with a chart, actual vs target and prior year. Color KPIs green (beat target) or red (missed). Pull numbers directly from q1_board_financials.csv.
   - Slides 8–10: Strategic Q2 Priorities with progress status (RAG: Red/Amber/Green)
   - Slide 11: Key Risks and Mitigations (table format, 2 risks from CEO update)
   - Slide 12: Wins & Milestones Q1 (3 wins from CEO update, visual layout)
   - Slides 13–14: Q2 Outlook — revenue targets and hiring plan
   - Slide 15: Appendix cover

4. Apply company_template.pptx styling throughout — do not use default PowerPoint themes.

5. Add speaker notes to slides 3–12 with 2–3 talking points each, pulled from the CEO update doc.
```

---

## MAGIC (45 sec) — What Copilot Does

Narrate as it executes:

1. **Reads q1_board_financials.csv** — pulls 24 KPIs, identifies actuals vs targets vs YoY, reads the Status column (Green/Amber/Red)
2. **Reads ceo_update.docx** — extracts narrative structure: wins, risks with priorities, strategic initiatives
3. **Opens company_template.pptx** — uses LoopSync brand colors, master slides, and custom layouts
4. **Plans the deck structure** — you'll see Copilot's step-by-step plan appear before execution: "I'll create 15 slides, pulling data from file 1 for slides 3–7, narrative from file 2 for slides 8–12..."
5. **Builds slide by slide** — each financial slide has the actual number large, the vs-target delta in green or red, a clean bar or line chart
6. **Writes speaker notes** — not generic bullet points, but actual talking points grounded in the CEO update language
7. **Self-reviews** — Copilot checks consistency: same numbers appear across all slides

Total Copilot execution time: approximately 45–60 seconds.

---

## RESULT (20 sec) — The Wow Moments

Flip through the deck. Highlight:

1. **Slide 3 (Revenue):** "$22.4M — ✅ Beat target by $600K | +17.3% YoY" — number is big, color is green, chart updates automatically
2. **Slide 5 (Profitability):** Infrastructure cost shows AMBER — Copilot correctly flagged the over-budget line from the CSV Status column
3. **Slide 12 (Q1 Wins):** Three clean win cards with language directly pulled from Sarah's CEO update — not rewritten, not hallucinated
4. **Speaker notes on Slide 6:** "NRR at 114% — best in company history. Third consecutive quarter of declining churn. Customer Success transformation delivering ahead of schedule." — Real talking points, ready to present.

The reveal: "This deck would have taken my team 2 days. It took Copilot 90 seconds. And the numbers are accurate because Copilot is reading them from the source file — not from memory."

---

## CTA (10 sec)

> "The next board meeting is in 3 days for a lot of you. You know what to do. Drop a 💙 if this would save your team time — I'll walk through the exact prompt in the comments."

---

## LINKEDIN POST DRAFT

**Hook:**
Board meeting. 3 days away.
Financials in Excel. CEO narrative in Word. 30 slides to update.

This used to take 2 days.
Copilot did it in 90 seconds.

**Body:**
Here's exactly what happened:

I gave Copilot 3 files:
📊 q1_financials.xlsx — 24 KPIs, actuals vs targets, prior year
📝 ceo_update.docx — wins, risks, strategic priorities
📽️ company_template.pptx — our board deck template

One prompt.
15 slides. Built from scratch.
Speaker notes. Charts. Color-coded KPIs.
Green where we beat plan. Amber where we didn't.
Talking points pulled from the CEO narrative — not invented.

The infrastructure cost overrun on slide 5? Copilot flagged it amber — because the source data said "Amber." It didn't clean up the bad news. It surfaced it.

That's what good board prep looks like.

**Closing:**
The copy-paste tax on finance teams is real.
Every quarter, someone spends 2 days doing work that should take 90 seconds.

Copilot's Cowork / cross-app mode is the end of that.

Drop a 💙 if you've lived this pain — I'll share the full prompt in the comments.

#Microsoft365 #Copilot #Finance #Productivity #AI #Leadership

---

## FILES USED

| File | Location | Description |
|------|----------|-------------|
| `q1_board_financials.csv` | SharePoint: Microsoft/Copilot-Demos/ | 24 KPIs × 4 columns (actual, target, prior year, status) |
| `ceo_update.docx` | SharePoint: Microsoft/Copilot-Demos/ | CEO Q1 narrative: wins, risks, Q2 priorities |
| `company_template.pptx` | SharePoint: Microsoft/Copilot-Demos/ | LoopSync brand template (TBD — use standard placeholder) |

---

## KEY STORYTELLING ANGLES

1. **The hidden tax** — Finance teams pay a "copy-paste tax" every quarter: 16–24 hours of manual work that generates no insight. Copilot eliminates it.

2. **It reads multiple files** — This is not a single-document demo. Copilot reads Excel data, Word narrative, AND a PowerPoint template simultaneously. That's the new paradigm.

3. **It doesn't hide the bad news** — Copilot read the Amber/Red status from the CSV and used it in the deck. The infrastructure cost overrun is prominently flagged on slide 5. Authentic, not sanitized.

4. **The speaker notes are actually good** — Other tools generate generic notes. Copilot pulled language from the CEO update and made them specific. That's the Work IQ advantage.

5. **The math check** — Copilot can verify that the same numbers appear consistently across slides. No more "slide 4 says $22.4M but slide 8 says $22.1M" embarrassment in the board room.

---

## METADATA

- **Demo Number:** C2
- **Series:** Copilot Cowork
- **App:** PowerPoint (cross-app: Excel + Word source files)
- **Feature:** Edit with Copilot, Cross-App / Cowork Mode, Work IQ file references
- **Difficulty:** Hard
- **Duration:** ~120 seconds
- **Status:** READY
- **Created:** 2026-05-05 by Data 🤖
- **Pain Point Source:** r/excel (341 upvotes: "copy-paste chaos") + industry benchmark (16–24h board pack prep)
