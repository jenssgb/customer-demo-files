# DEMO C7 — The Budget Reforecast

**APP:** Copilot (Cowork — Cross-App: Excel + Word + PowerPoint)
**DURATION:** ~90 seconds
**FEATURE:** Edit with Copilot / Work IQ / Multi-step Agent Mode
**DIFFICULTY:** Hard
**STATUS:** Ready
**CREATED:** 2026-06-02

---

## The Story

**Pain Point** (Reddit r/FP&A, r/CFO, LinkedIn Finance community — perennial top pain):

> "Q2 revenue just came in 12% below plan. It's Sunday evening. CFO called an emergency session. 
> You have the original budget in Excel, H1 actuals in another CSV, and a half-finished board 
> narrative in a Word doc. Leadership needs a revised full-year model with three scenarios, an 
> updated board narrative that doesn't spin the miss, and a 3-slide exec summary — all consistent 
> with each other — before Monday morning's leadership call."

**Why this resonates:**
- Mid-year reforecasts under board pressure are the single most stressful FP&A scenario
- Finance teams typically spend 4–6 hours cross-referencing Excel, Word, and PowerPoint manually
- Numbers in the deck don't match the model. Narrative doesn't reflect the scenarios. It's 11pm.
- Copilot bridges all three files in one conversation — keeping everything consistent

---

## Demo Script

### HOOK (5 sec)
*"It's Sunday night. Q2 missed by 12%. CFO wants a board-ready reforecast model, updated narrative, and exec slides — consistent across all three files — by tomorrow morning."*

### SETUP (10 sec)
Open Copilot Chat. Reference three files:
- `c7_original_budget.csv` — FY2026 budget (20 line items, monthly)
- `c7_actuals_h1.csv` — H1 actuals with variance analysis and root causes
- `c7_board_update_draft.txt` — Draft board update (Revenue Performance section flagged for rewrite)

*"I have my original budget, the H1 actuals with variance detail, and a board draft that still has placeholder text where the honest numbers should be."*

### PROMPT (10 sec)
Type into Copilot:

```
Using c7_original_budget.csv, c7_actuals_h1.csv, and c7_board_update_draft.txt:

1. REFORECAST MODEL (Excel): Pull H1 actuals, calculate H1 variance vs budget ($ and %). 
   Project H2 using 3 scenarios (Base: flat Q2 run-rate, Upside: +8% QoQ, 
   Downside: -5% QoQ). Calculate revised Full Year totals for each scenario. 
   Add a waterfall chart showing budget → actuals → reforecast by quarter.

2. UPDATED BOARD NARRATIVE (Word): Rewrite the Revenue Performance section of the 
   board update to reflect H1 miss. Acknowledge the gap honestly, explain the 2 root 
   causes from the actuals, and present the 3 reforecast scenarios with management 
   commentary. Tone: direct, leadership-ready, no spin.

3. EXEC SUMMARY SLIDE CONTENT: Draft content for 3 slides: (1) H1 Performance Snapshot 
   with key metrics, (2) Reforecast Scenarios with recommendation, (3) Top 3 Actions for 
   H2 recovery. Bullet format, 5 bullets max per slide.
```

### MAGIC (40 sec)
Watch Copilot:
1. **Reads all three files simultaneously** — surfaces H1 actuals ($7.73M vs $8.42M budget, -8.1%)
2. **Identifies the two root causes** from actuals: Americas SDR restructure pipeline gap + 3 EMEA enterprise deals pushed to Q3
3. **Builds the Excel model** — H1 actuals layer, three scenario projections, waterfall chart
4. **Rewrites the Word narrative** — replaces the diplomatic placeholder with direct, specific language about the miss and the plan
5. **Drafts the 3 slide outlines** — consistent numbers across all outputs, same root-cause language throughout

*"Notice: it pulled the root cause detail from the actuals file and used it in both the Word narrative AND the slide notes — everything stays consistent."*

### RESULT (15 sec)
Show the three outputs side by side:
- **Excel**: Waterfall chart, three scenario rows with FY totals — Base ($16.8M), Upside ($17.4M), Downside ($15.9M)
- **Word**: Revenue Performance section — acknowledges -$686K H1 gap, names the two root causes specifically, presents scenarios with management tone
- **Slides**: 3 crisp slides, numbers matching the Excel model exactly

*"Four hours of Sunday-night copy-paste work: Excel model, Word narrative, slide content — consistent, board-ready, in 90 seconds."*

### CTA (10 sec)
*"The dataset is live on SharePoint — link in the post. Try the prompt on your own reforecast data. What's the most painful finance doc you build every quarter?"*

---

## Data Files

| File | Location | Description |
|------|----------|-------------|
| `c7_original_budget.csv` | [SharePoint](https://bluepolicy.sharepoint.com/sites/openclaw-data-agent/_layouts/15/Doc.aspx?sourcedoc=%7B4809987B-B303-4267-A115-6B9522B23731%7D&file=c7_original_budget.csv&action=default&mobileredirect=true) | FY2026 budget: 20 P&L line items, monthly cadence, $19.1M revenue plan |
| `c7_actuals_h1.csv` | [SharePoint](https://bluepolicy.sharepoint.com/sites/openclaw-data-agent/_layouts/15/Doc.aspx?sourcedoc=%7BD522BA04-15A0-4BDD-8EAA-F785EF3CC8BE%7D&file=c7_actuals_h1.csv&action=default&mobileredirect=true) | H1 2026 actuals: budget vs actual variance by month/quarter, 2 root causes embedded |
| `c7_board_update_draft.txt` | [SharePoint](https://bluepolicy.sharepoint.com/sites/openclaw-data-agent/Shared%20Documents/Microsoft/Copilot-Demos/c7_board_update_draft.txt) | Board update draft with placeholder Revenue Performance section flagged for rewrite |

---

## Key Numbers (Baked In)

- **FY2026 Budget Total Revenue:** $19.10M
- **H1 Budget:** $8.42M | **H1 Actuals:** $7.73M | **H1 Variance:** -$686K (-8.1%)
- **Q2 Miss:** -$593K (-13.5%)
- **Root Cause 1:** Americas SDR restructure (Feb 2026) → pipeline conversion rate 24%→17% → $249K New ARR miss
- **Root Cause 2:** 3 EMEA enterprise deals pushed Q3 (Vanterra $210K, Solaris $195K, Meridian $188K) → $141K miss
- **Bright spots:** NRR 118% (plan 115%), Gross Churn 2.1% (plan 2.5%), Enterprise ACV $167K (plan $145K)
- **Scenario range:**
  - Base ($16.8M FY): H2 at Q2 run-rate + EMEA deals close Q3
  - Upside ($17.4M FY): Americas conversion recovers + all 3 EMEA Q3
  - Downside ($15.9M FY): Recovery delayed, 1 EMEA deal slips to Q4

---

## LinkedIn Post Draft

> **You know this feeling:**
> 
> It's Sunday evening. Q2 just closed 12% below plan. CFO wants a full-year reforecast, updated board narrative, and exec slides — all consistent with each other — before tomorrow's 8am call.
> 
> Normally that's 4–5 hours of: Excel model → copy numbers to Word → manually update slides → realize the slides don't match the model → start over.
> 
> Here's what it looks like with Microsoft 365 Copilot:
> 
> *[Screen recording: 90s — Copilot reads 3 files, builds waterfall chart, rewrites board narrative, drafts 3 slides — consistent numbers throughout]*
> 
> One prompt. Three files. Three outputs. Consistent root-cause language across all of them.
> 
> The dataset is on SharePoint (link below) — try it on your own numbers.
> 
> What's the finance doc that costs you the most time every quarter?
> 
> #MicrosoftCopilot #FPandA #Finance #ProductivityTips #M365Copilot

---

## Wow Moments to Highlight

1. **Cross-file consistency** — Copilot uses the same two root-cause explanations in the Excel model notes, the Word narrative, AND the slide content. No manual sync.
2. **Honest language** — When rewriting the Word narrative, Copilot replaces the diplomatic placeholder with direct, specific acknowledgment of the gap and the plan. No spin.
3. **Scenario math** — Three scenario rows calculated correctly from the H1 actuals baseline, not from the original budget.
4. **Waterfall chart** — Visually shows budget → H1 actuals → projected H2 → FY reforecast by scenario. Finance directors love this.
