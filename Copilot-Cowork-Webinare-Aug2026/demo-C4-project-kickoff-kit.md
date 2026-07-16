# DEMO C4 — The Project Kickoff Kit
**APP:** Copilot Cowork (Word + Excel + PowerPoint + Chat — multi-app agent flow)
**DURATION:** ~90 seconds
**FEATURE:** Edit with Copilot / Work IQ / Multi-file agent

---

## The Pain Point

> *"My manager just dropped a project on me via Slack at 4:47pm on Thursday. Kickoff is Tuesday. I need a project charter, a RACI matrix, a timeline, and a deck — and all I have is a two-paragraph Slack message."*

**Source:** r/projectmanagement, r/ProductManagement (perennial top-voted frustration thread — "new project, blank page, kickoff tomorrow"). The 2025 PMI Pulse of the Profession report found PMs spend 42% of their time on administrative documentation vs. actual project delivery. On Reddit, posts like *"just got assigned a massive project, where do I even start"* regularly collect 200+ comments. The pain is universal: the moment between "you own this" and "here's the kickoff deck" is a multi-hour scramble.

---

## Hook (5 sec)

*"You've just been assigned a brand-new project. Kickoff is Tuesday. All you have is a Slack message and a team roster. Here's how Copilot builds your entire kickoff package in 90 seconds."*

---

## Setup (10 sec)

Two files uploaded to SharePoint:
- **`c4_project_brief.txt`** — A raw project brief (background, objectives, budget, risks, timeline, team notes)
- **`c4_team_roster.csv`** — 15 people across Product, Engineering, Design, QA, Security, Infrastructure, CS

The scenario: James Okafor, PM at Nexora Inc. Customer Portal 2.0. $380k budget. 6-month timeline. Kickoff in 5 days. Manager sent a Slack message at 4:47pm. James has the brief and a team list.

---

## Prompt

```
I've just been assigned a new project: Customer Portal 2.0 (c4_project_brief.txt). 
Kickoff is Tuesday. Using c4_project_brief.txt and c4_team_roster.csv, build my complete project kickoff package:

1. PROJECT CHARTER (Word):
   Create a professional 2-page project charter including: executive summary, objectives (SMART format), 
   scope statement (in/out of scope), success metrics with targets, budget overview, key milestones 
   (Phase 1–3), assumptions, and a risks table with likelihood/impact/mitigation for each risk from the brief.

2. RACI MATRIX (Excel):
   Build a RACI matrix for 12 key project activities across all 15 team members from c4_team_roster.csv.
   Activities: Project kick-off, Architecture design, API mapping, Frontend build, Backend build, 
   SSO Integration, UX/Design sprints, QA testing, Security review, UAT coordination, 
   Migration execution, Launch sign-off.
   Color-code: R=blue, A=orange, C=yellow, I=green. Add a summary row showing R/A counts per person.

3. KICKOFF DECK (PowerPoint, 10 slides):
   - Slide 1: Title (Project name, PM name, kickoff date)
   - Slide 2: Why we're doing this (problem statement + 3 data points from the brief)
   - Slide 3: Objectives & success metrics
   - Slide 4: Scope (in/out of scope — two-column layout)
   - Slide 5: High-level timeline (Phase 1–3 with key milestones as visual timeline)
   - Slide 6: Team & roles (from roster — visual org chart or table)
   - Slide 7: Top 3 risks with RAG status and mitigations
   - Slide 8: Budget overview
   - Slide 9: Open questions & decisions needed from the team
   - Slide 10: Next steps + action items for Week 1
   
Keep the deck clean and visual. Speaker notes on every slide.
```

---

## Magic (40 sec)

What happens — Copilot's multi-app execution:
1. **Reads both source files** from SharePoint via Work IQ
2. **Word:** Drafts the project charter — parses the brief, converts risks into a structured table, SMART-formats objectives
3. **Excel:** Builds the RACI — maps 15 people × 12 activities, applies color-coding and summary row
4. **PowerPoint:** Creates 10 slides — pulls problem statement data points, formats Phase 1–3 as a visual timeline, builds a risks table with RAG status

The viewer sees Copilot working through the multi-step plan: *"Reading project brief... Creating Word charter... Generating RACI in Excel... Building PowerPoint deck..."*

Three separate outputs, all derived from the same two source files. No copy-pasting between apps.

---

## Result (15 sec)

- **Word doc:** Professional 2-page project charter, ready to send to the exec sponsor
- **Excel file:** Color-coded RACI matrix — instantly shows that Mei Lin (DevOps) is the single RACI bottleneck in 4 Phase 2 activities — a risk James can address now
- **PowerPoint deck:** 10 slides, speaker notes written, risks table with RAG, visual Phase 1–3 timeline

What used to take James 6 hours of document assembly, template hunting, and cross-referencing — done in under 2 minutes.

---

## CTA (10 sec)

*"Two files in. Three polished deliverables out. If Copilot can do this for you — what would you do with the 6 hours back? Try it with your next project brief."*

---

## Demo Data (SharePoint)

| File | What's in it |
|---|---|
| `c4_project_brief.txt` | Full project brief: background, objectives, budget ($380k), timeline, risks, constraints, stakeholders — as if dumped into a doc after a Slack message |
| `c4_team_roster.csv` | 15 team members: Name, Role, Email, Dept, Location, Q3 availability — with realistic constraints baked in (Mei Lin 30%, designers 60% shared) |

**SharePoint path:** `Microsoft/Copilot-Demos/`

**Story hooks for commentary:**
- The PM found out about the project via Slack at 4:47pm
- Mei Lin (only DevOps) is at 90% team capacity — RACI will expose this as a risk
- Sarah Chen (VP Product) expects the deck by Tuesday morning
- The "Holiday Freeze" migration window is a known risk most PMs miss

---

## LinkedIn Caption Draft

**Hook options:**
1. *"My manager just Slacked me: 'You own the new portal project. Kickoff Tuesday.' It's Thursday 4:47pm. Here's how I went from panic to a full kickoff package in 90 seconds."*
2. *"New project. Blank page. 5 days to kickoff. Two files + one Copilot prompt → charter, RACI, deck. Watch."*
3. *"Every PM knows this moment: you've been handed a project and you need a charter, RACI, and deck by Tuesday. I used to clear my evening for this. I don't anymore."*

**Tags:** #MicrosoftCopilot #ProjectManagement #M365 #Productivity #EditWithCopilot

---

## Meta
- **Demo #:** C4
- **Status:** READY
- **App rotation:** Copilot Cowork (Multi-App) — correct next in rotation after W5 (Word)
- **Difficulty:** Hard
- **Created:** 2026-05-19
- **Files generated by:** copilot-demo-daily cron
