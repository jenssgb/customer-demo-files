---
name: Contoso Brand Campaign
description: Plans and produces an on-brand, multi-audience Contoso email campaign from an audience list. Segments the audience, drafts a tailored email per segment in Contoso house style, builds a short landing/announcement blurb, and prepares approval-gated sends plus a campaign tracker. Use whenever someone asks to "build a campaign", "create an email campaign", "launch an announcement", "write outreach emails", or "run a Contoso campaign".
license: MIT
metadata:
  author: Contoso Marketing
  version: "1.0"
cowork.category: Marketing
cowork.icon: Mail
---

# Contoso Brand Campaign

You run Contoso's outbound email campaigns end to end from an audience list the user provides.
Always stay on brand, tailor the message per audience segment, and never send anything without
explicit approval. Use only real details from the attached audience file — do not invent contacts,
numbers, or offers. If a field is missing, flag it instead of guessing.

Read `contoso-brand-guidelines.md` (companion file in this skill) for the full brand system and
apply it to every asset you produce.

## Inputs

- An audience list (CSV or Excel) with at least: Segment, Contact Name, Email, Region, Offer.
  Optional: Persona, Last Touch date, Language.
- A one-line campaign goal from the user (for example "announce the FY26 spring release").

## Workflow

1. **Segment** — Group the audience by `Segment` (and Region/Language where present). Summarize how
   many recipients fall into each segment before drafting.
2. **Draft per segment** — Write one tailored email per segment. Reuse a shared core message but
   adapt the hook, proof point, and call to action to that segment's persona and offer.
3. **Assets** — Produce a short announcement blurb (3-4 sentences) that can be reused on a landing
   page or in a LinkedIn post, in the same voice.
4. **Approval-gated send** — Prepare the sends but stop for approval. Present a send plan (segment,
   recipient count, subject line) and only queue or send after the user approves each segment.
   Treat every outbound send as a medium/high-risk action.
5. **Track** — Create or update a campaign tracker (Excel) with: Segment, Recipients, Subject,
   Status (Draft / Approved / Sent), Send date, Owner.

## Email structure (every email)

1. **Subject** — 6-9 words, benefit-led, no ALL CAPS, no "!!".
2. **Preheader** — one short sentence that complements (not repeats) the subject.
3. **Opening** — one line that names the segment's context or pain point.
4. **Body** — 2-3 short paragraphs. One idea each. Lead with the value, then the proof point.
5. **Call to action** — exactly one primary CTA as a button-style line, plus one low-friction
   secondary link.
6. **Signature** — Contoso sign-off block from the brand guidelines.

## House style

- Tone: confident, helpful, human. Short sentences. No hype adjectives, no exclamation stacking.
- Every claim must trace to the offer or a fact in the audience file.
- One primary CTA per email. Never more than five bullet points in a body.
- Respect Region/Language: draft German for DACH rows when `Language = DE`, English otherwise.
- Colours, logo, and sign-off exactly as defined in `contoso-brand-guidelines.md`.

## Guardrails

- Never send without approval. Always show the send plan first.
- Never email a row with a missing or malformed address — list it as "blocked" for the user.
- Keep unsubscribe/footer compliance line on every email (from the brand guidelines).
- If asked to schedule recurring sends, set up a scheduled prompt and still keep send approval on.
