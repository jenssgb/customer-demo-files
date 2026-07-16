# DEMO C8: The Interview Debrief Machine

**APP:** Copilot Chat (Cowork — Word + Excel)  
**DURATION:** ~90 seconds  
**FEATURE:** Edit with Copilot / Agent Mode (Multi-App, Work IQ)  
**DIFFICULTY:** Medium  
**FILE:** [c8_interview_feedback.csv](https://bluepolicy.sharepoint.com/sites/openclaw-data-agent/_layouts/15/Doc.aspx?sourcedoc=%7BB16A8E0A-5DDF-471A-B545-E76E5E64C46B%7D&file=c8_interview_feedback.csv&action=default&mobileredirect=true)  
**DATE BUILT:** 2026-06-07  

---

## Pain Point (Validated)

**Sources:** r/managers, r/recruiting, LinkedIn HR community 2024–2026

> *"It's 7pm. You interviewed 6 candidates today. The hiring decision meeting is at 9am. You have 5 interviewers, 30 rows of raw scores and notes, a CSV export from your ATS — and zero debrief documents. You need a comparison matrix, a hiring recommendation memo, and 5 personalized rejection emails. And you haven't eaten dinner."*

**Why this resonates:**
- r/askmanagers (April 2026): "The gap between interview and hiring manager feedback is my biggest bottleneck — notes sit unread for 2–3 days"
- r/humanresources (Sep 2025): Personalized rejections for candidates who've been through multiple rounds is the professional expectation — but almost nobody does it because it takes too long
- r/interviews (Apr 2025): "With AI you can write rejections that sound personal even when you're writing 5 at once" — candidates notice the difference and remember it
- Universal pattern: hiring managers spend 45–90 min after a full interview day on debrief admin before they can even start synthesizing a decision

---

## Setup

**Data file:** `c8_interview_feedback.csv` on SharePoint  
**What's in it:**
- 6 candidates: Mia Hartley, Jin Sato, Amara Osei, Tomás Rivera, Priya Kapoor, Liam O'Brien
- 5 interviewers: VP of Product, Engineering Lead, Head of Design, PM Peer, Chief of Staff
- 5 competencies scored: Problem Solving, Communication, Leadership, Technical Depth, Culture Fit
- Raw interview notes — candid, realistic, not sanitized
- Baked-in drama:
  - **Mia** = clear hire (4.8 avg, Strong Hire consensus across all 5 interviewers)
  - **Jin** = split controversy (Engineering Lead: Strong Hire 4.4 / Head of Design: No Hire 2.6 / CoS: No Hire)
  - **Tomás Rivera** = safety flag from Engineering Lead, Design, and CoS (interrupting behavior + cultural risk comment)
  - **Liam** = strong no hire (Eng Lead ended session early)
  - **Priya Kapoor** = salary flag (at $110k — below market for role, raise negotiation likely)
  - **Mia** = salary negotiation flag ($135k above midpoint — board approval needed)

---

## The Prompt

```
Using c8_interview_feedback.csv (6 candidates, 5 interviewers, raw notes and scores), build my complete hiring decision package:

1. CANDIDATE COMPARISON MATRIX (Excel): 6 candidates × 5 competencies, color-coded scores, overall rank, Hire/No-Hire flag, interviewer consensus column. Highlight top 2 in green, red flag any with < 3.0 average. Add a panel split alert for candidates where interviewers disagree by > 2 points on any competency.

2. HIRING RECOMMENDATION MEMO (Word): 1-page hiring manager memo — top candidate summary, key differentiators, one risk/concern, recommended offer terms. Flag any safety or cultural concerns from the panel. Tone: direct, evidence-based.

3. DRAFT COMMUNICATIONS (Word): Offer email to top candidate (warm, specific, include role + start date). 5 personalized rejection emails — each references one genuine strength from the interview notes. No generic copy-paste rejections.
```

---

## What Copilot Does (the Magic)

1. **Opens the CSV** via Work IQ — reads all 30 rows across 5 interviewers
2. **Builds the comparison matrix in Excel:**
   - Calculates average scores per candidate per competency
   - Color-codes: green ≥ 4.0 / amber 3.0–3.9 / red < 3.0
   - Flags Hire/No-Hire by majority panel consensus
   - Adds a "Panel Split" column — highlights Jin's controversy automatically
   - Surfaces Tomás Rivera's safety flags in a separate alert section
3. **Writes the recommendation memo in Word:**
   - Identifies Mia as clear hire with evidence citations from 4 interviewers
   - Notes Jin's panel split and what each side was seeing
   - Flags the Tomás Rivera safety concern (interrupting pattern + cultural risk comment)
   - Recommends offer terms with salary negotiation note for Mia
4. **Drafts 5 rejection emails:**
   - Each one references the candidate's real strength from notes
   - Liam's: "Your energy and honesty about where you are in your career journey came through clearly..."
   - Jin's: "Your technical depth and analytical instincts were genuinely impressive..."
   - None of them are copy-paste — Copilot reads the notes and individualizes

---

## Result

In ~90 seconds, a hiring manager has:
- ✅ A decision-ready candidate matrix with panel consensus and split alerts
- ✅ A 1-page hiring memo they can bring directly to the 9am meeting
- ✅ 5 respectful, personalized rejection emails ready to send after the offer is out
- ✅ Safety flags surfaced and documented — not buried in raw notes

---

## LinkedIn Hook / CTA

> **"It's 7pm. Your hiring decision is at 9am. You have 6 candidates, 30 rows of raw interview scores, and 5 rejection emails to write.**
>
> **Copilot built the comparison matrix, wrote the hiring recommendation memo, and drafted personalized rejections for all 5 — referenced to each person's actual interview notes.**
>
> **90 seconds. The candidates will remember that rejection email. The hiring manager won't miss their dinner.**
>
> Try it: link in comments 👇"

---

## Demo Script (Talking Points)

**HOOK (5 sec):**  
"Full day of interviews. 6 candidates. 5 interviewers. It's 7pm and the hiring decision is at 9am. Nobody submitted their debrief notes. You have a CSV from your ATS and a very short night."

**SETUP (10 sec):**  
Open Copilot Chat. Show c8_interview_feedback.csv is attached from SharePoint. "30 rows. Six candidates, five interviewers, raw scores and notes for every conversation today."

**PROMPT (10 sec):**  
Type the prompt above. "One ask — three deliverables."

**MAGIC (40 sec):**  
- Watch Copilot read the CSV and start building the Excel matrix
- Point out when it auto-flags Jin's split (panel spread > 2)
- Point out Tomás Rivera's safety flag section
- Show the Word memo: "This is a direct hire recommendation a VP could walk into a meeting with"
- Show one rejection email: "This isn't a template — it references what Liam actually said in his interview"

**RESULT (15 sec):**  
- Decision matrix: ✅
- Hiring memo: ✅  
- 5 personalized rejections: ✅
- Dinner: also ✅

**CTA (10 sec):**  
"The candidates will remember that rejection email. The hiring manager gets to sleep. Link to the data file and prompt in the comments."

---

## Notes

- The **Jin split** is the demo's most interesting moment — Copilot should surface the disagreement automatically and flag it for the hiring manager. This is the "oh wow" moment: not just scores, but pattern recognition across interviewers.
- The **safety flag** from Tomás Rivera's notes (interrupting pattern + cultural risk comment) should be prominently flagged in the memo, not buried. Demonstrates that Copilot reads unstructured text and extracts structured risk signals.
- **Mia's salary flag** ($135k vs likely $125k band midpoint) should appear in the offer recommendation — "Note: candidate indicated $135k expectation; verify against current band before verbal offer."
