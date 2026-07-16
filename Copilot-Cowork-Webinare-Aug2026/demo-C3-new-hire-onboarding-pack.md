# DEMO C3 — New Hire Onboarding Pack
**APP:** Copilot Chat (BizChat) + Microsoft 365 Copilot  
**DURATION:** ~90 seconds  
**FEATURE:** Copilot Chat with Work IQ + File References  
**STATUS:** READY  
**DATE BUILT:** 2026-05-06  

---

## 🎯 The Pain Point (Researched)

From Reddit r/managers (March 2026, 2k upvotes):
> *"New hires are taking 4–6 weeks to get productive and it's killing our momentum. What are you guys doing for onboarding?"*

Stats that land:
- **2 in 5 new starters** leave within the first 90 days because they don't feel engaged or properly onboarded
- Most managers spend **3–5 hours** manually assembling a welcome email + 30-60-90 day plan + scheduling 6 intro meetings
- The painful part: half of it is copy-paste from the last hire's onboarding. Nobody has time to do it well. So it doesn't get done.

---

## 🎬 SCRIPT

### HOOK (5 sec)
> *"New team member starts Monday. It's Thursday. You still have no welcome email, no onboarding plan, and 6 intro meetings to schedule. Sound familiar?"*

### SETUP (10 sec)
Open Copilot Chat. Two files are referenced:
- `c3_role_description.txt` — role description for the new Senior PM
- `c3_team_contacts.csv` — 6 team members with context, availability, talking points

Context: The manager has 45 minutes before their next call. They need the whole onboarding package — now.

### PROMPT (10 sec)
Type (or paste) this prompt:

```
Prepare a new hire onboarding package for Alex Chen, starting as Senior Product Manager — Platform Integrations on Monday, May 11.

1. Draft a welcome email from me to Alex: introduce the team, share the first-week vibe, and make them feel genuinely excited to start. Warm but professional. Max 200 words.

2. Using role_description.txt, create a 30-60-90 day plan:
   - Days 1–30: Learning & Listening (who to meet, what to read, tools to learn)
   - Days 31–60: Contributing (first PRD, first backlog session, first customer call)
   - Days 61–90: Leading (own a delivery, propose roadmap changes, set Q3 OKRs)
   Format as a Word document table with one section per phase.

3. Using team_contacts.csv, schedule intro meetings next week (May 12–16):
   - 30 minutes each, 6 people
   - Respect their preferred meeting times
   - Avoid back-to-back blocks — leave at least 30 min between
   - Group similar roles on the same day where possible
   
4. For each intro meeting, draft a calendar invite with a 2-sentence agenda note that gives Alex context on who they're meeting.
```

### MAGIC (40 sec)
Watch Copilot:
1. **Parse the role description** — extracts milestones, tools, key reads, manager notes
2. **Draft the welcome email** — personalized, warm, actionable (first week schedule embedded)
3. **Build the 30-60-90 table** — structured, specific, role-aware (not a generic template)
4. **Read the contacts CSV** — cross-references availability, roles, and talking points
5. **Propose a weekly schedule** — groups Engineering + Product on Tuesday, Customer Success + Partnerships on Thursday, no back-to-back
6. **Draft 6 calendar invites** — each with a bespoke 2-sentence agenda based on the contact's context

### RESULT (15 sec)
> *"In under 2 minutes: a professional welcome email, a role-specific 90-day plan with real milestones, a conflict-free intro meeting schedule for 6 people, and 6 ready-to-send calendar invites — all from two files and one prompt."*

**Wow moments to highlight:**
- The 30-60-90 plan references actual tools (Productboard, Confluence, Mixpanel) from the role doc
- The schedule respects "Sarah prefers Tues–Thurs AM" from the CSV
- Calendar invites include contextual notes like "Tom has UX prototypes waiting for a PM to champion — come ready to listen"

### CTA (10 sec)
> *"Next time someone joins your team — don't start from scratch. File + prompt + 90 seconds. Try it. Link to the files in the comments."*

---

## 📁 Data Files

| File | Location | Description |
|------|----------|-------------|
| `c3_role_description.txt` | SharePoint: Microsoft/Copilot-Demos/ | Full role description: Senior PM — Platform Integrations. Includes 90-day success metrics, tools, key reads, manager notes. |
| `c3_team_contacts.csv` | SharePoint: Microsoft/Copilot-Demos/ | 6 team members with name, role, dept, email, availability, context, talking points. |

**SharePoint URLs:**
- Role: https://bluepolicy.sharepoint.com/sites/openclaw-data-agent/Shared%20Documents/Microsoft/Copilot-Demos/c3_role_description.txt
- Contacts: https://bluepolicy.sharepoint.com/sites/openclaw-data-agent/_layouts/15/Doc.aspx?sourcedoc=%7B2C791DFE-96B5-4A70-AD98-6863C9B156FF%7D&file=c3_team_contacts.csv&action=default&mobileredirect=true

---

## 💡 Demo Tips

**If Copilot asks for calendar access:** Toggle on "Work" sources so it can check real calendar availability. Without this, it will use the preferred times from the CSV instead — still a good demo.

**Strongest moment:** The 30-60-90 plan. It's not a generic "meet people, learn stuff" template — it references real tools from the role doc and includes the manager's quote ("Listen before you fix"). That's the clip.

**Variation for Excel audience:** After Copilot generates the schedule, paste the meeting list into Excel and ask Copilot to "create a tracker for these onboarding activities with completion checkboxes and a progress donut chart." Cross-app chain demo.

---

## 📌 LinkedIn Post Angle

**Hook options:**
1. *"40% of new hires leave in 90 days. Not because of the job — because of the onboarding."*
2. *"It's Thursday. New hire starts Monday. 3 hours of copy-paste work or 90 seconds with Copilot."*
3. *"The best onboarding I've seen came from 2 files and 1 prompt."*

**Format:** Screen recording (90s) + hook text + 3 bullet "what Copilot built" summary + CTA

---

## 🔗 Related Demos
- C1: Monday Morning Briefing (Work IQ for email/calendar triage)
- C2: Board Pack (cross-file multi-step Word + Excel + PPT)
- Next: B1 — Competitive Intel (BizChat + web sources for sales talking points)
