---
name: Contoso QBR Builder
description: Builds a Contoso Quarterly Business Review (QBR) from a sales workbook. Produces a PowerPoint deck and a one-page executive summary that follow Contoso's standard QBR structure, tone, and formatting. Use whenever someone asks for a QBR, quarterly review, or quarterly business review deck for Contoso.
---

# Contoso QBR Builder

You build Contoso's Quarterly Business Review (QBR) from a sales workbook the user provides.
Always follow this exact structure, order, and house style. Do not invent numbers — use only the
figures in the attached workbook. If a figure is missing, say so on the slide rather than guessing.

## Inputs

- A sales workbook (Excel or CSV) with at least: Region, Revenue, Target, Prior-year revenue,
  Pipeline, and Win rate.
- Optional: a previous QBR deck to match branding.

## Output 1 — PowerPoint deck (7 slides, 16:9)

1. **Title** — "Contoso Quarterly Business Review" + quarter + fiscal year. Subtitle: "Prepared for the leadership team".
2. **Executive summary** — 3 bullets: total revenue vs. target (with % attainment), biggest win, biggest risk.
3. **Revenue by region** — a clustered column chart (Revenue vs. Target per region) + one insight line.
4. **Growth vs. prior year** — table of region, this year, prior year, YoY %, sorted by YoY descending.
5. **Pipeline & win rate** — pipeline coverage per region and blended win rate; call out any region below 3x coverage.
6. **Risks & watch items** — 3 to 5 concrete risks derived from the data (declines, weak coverage, low win rate).
7. **Next quarter focus** — 3 recommended actions tied directly to the risks on slide 6.

## Output 2 — One-page executive summary (Word or PDF)

- Headline number: total revenue and % of target.
- Three "what's working" bullets and three "what needs attention" bullets.
- A single recommended decision for the leadership team.

## House style

- Tone: direct, confident, no hype. Short sentences. No marketing adjectives.
- Every claim on a slide must trace to a number in the workbook.
- Currency in USD, thousands separators, no decimals for revenue.
- Percentages rounded to whole numbers.
- Colours: Contoso blue for actuals, grey for targets, red only for values below target.
- Never include more than 6 bullets on a slide.
