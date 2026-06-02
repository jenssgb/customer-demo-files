# Zava Top M365 Copilot Demo

Top-Demo fuer Microsoft 365 Copilot auf Basis der fiktiven Microsoft-Firma **Zava**. Ziel ist ein universelles, kundentaugliches E2E-Szenario im Stil der KN/Vaillant-Runbooks: Business-Story, Live-Prompts, echte Demo-Dateien, Office-Artefakte, Public-Download und One-Liner.

## Ziel

Eine universelle, kundenunabhaengige Demo, die in 30 bis 40 Minuten zeigt, wie Microsoft 365 Copilot vom ersten Business-Signal bis zur entscheidungsreifen Antwort arbeitet:

1. Copilot Chat erkennt aus Mail, Meeting, Memo und Briefing den Rush-Order-Kontext.
2. Analyst/Reasoning-Style Prompting bewertet Feasibility, Engpass und Preisfloor.
3. Excel analysiert Bestand, Kapazitaet, Marge und Risiko im Workbook.
4. Outlook formuliert eine belastbare Kundenantwort.
5. Word erstellt einen Operations-Plan.
6. PowerPoint erzeugt eine Executive Story.
7. Agent Builder skizziert einen wiederverwendbaren Order-Desk-Agenten.

## Zava Research Summary

Zava ist eine fiktive Microsoft-Demo-Firma aus dem Retail-/Athletic-Wear-Kontext. Microsoft Ignite beschreibt Zava als fictional athletic-wear company in einer Demo zu kollaborativer AI und Produktlaunch-Vorbereitung.

Diese Demo nutzt daraus die stabilste Storyline: **Zava erhaelt eine dringende Grossbestellung fuer 20.000 smarte Launch-Shirts und muss Bestand, Produktionsoptionen, Marge, Risiken und Kundenantwort schnell klaeren.**

## Quellen

- Microsoft Ignite Session `BRK284`: https://ignite.microsoft.com/en-US/sessions/BRK284
- Microsoft 365 Copilot Chat overview: https://learn.microsoft.com/copilot/overview
- Copilot Chat FAQ: https://learn.microsoft.com/copilot/faq
- Microsoft 365 Copilot overview: https://learn.microsoft.com/microsoft-365/copilot/microsoft-365-copilot-overview
- Word, Excel, and PowerPoint Agents: https://learn.microsoft.com/microsoft-365/copilot/wordexcelppt-agents
- Enterprise data protection: https://learn.microsoft.com/microsoft-365/copilot/enterprise-data-protection

## Dateien

| Datei | Zweck |
| --- | --- |
| `Zava-M365-Copilot-Universal-Briefing.html` | Live-Runbook im Clawpilot-Stil mit Copy-Buttons |
| `Prompts/Zava-M365-Copilot-Universal-Demo.md` | PromptPrompter-Datei |
| `Zava_Order_Analysis.xlsx` | Excel-Dashboard mit Inventory, Orders, Pricing, Risk Register und Formeln |
| `Zava_Operations_Plan.docx` | Word-Seed fuer den Operations-Plan |
| `Zava_Executive_Story.pptx` | PowerPoint-Seed fuer die Executive Story |
| `data/Zava_Rush_Order_Context.md` | Business-Kontext fuer Chat, Word und PowerPoint |
| `data/Zava_Inventory_Snapshot.csv` | Inventory-Daten fuer Analyse und Charts |
| `data/Zava_Order_Intake.csv` | Mehrere Rush-Order-Requests fuer Agent-Testcases |
| `data/Zava_Risk_Register.csv` | Risiko-Register mit Ownern und Mitigations |
| `data/Zava_Pricing_Assumptions.csv` | Preisfloor- und Margin-Annahmen |
| `data/Zava_Email_Thread.html` | Outlook-/Edge-Kontext fuer Zusammenfassung und Antwort |
| `data/Zava_Launch_Brief.md` | Produkt- und Kampagnenkontext |
| `data/Zava_Meeting_Transcript.md` | Meeting-Kontext fuer Action Items |
| `data/Zava_Executive_Decision_Memo.md` | COO-Entscheidungsvorlage |
| `data/Zava_Agent_Builder_Brief.md` | Agent Builder Instructions und Guardrails |
| `Deploy-Zava-Demo-Content.ps1` | Upload in den CDX OneDrive/SharePoint Demo-Folder |

## Demo Files One-Liner

Das Public Demo-Repo enthaelt den Ordner `Zava-M365-Copilot-Universal/`. Dieser One-Liner kopiert das Paket auf den Desktop der Demo-VM:

```powershell
$d=[Environment]::GetFolderPath('Desktop');$z="$env:TEMP\zava.zip";iwr 'https://github.com/jenssgb/customer-demo-files/archive/refs/heads/main.zip' -OutFile $z;ri "$d\ZAVA-Demo" -r -fo -ea 0;Expand-Archive $z "$env:TEMP\zava" -Force;mv "$env:TEMP\zava\customer-demo-files-main\Zava-M365-Copilot-Universal" "$d\ZAVA-Demo";ri $z,"$env:TEMP\zava" -r -fo;ii "$d\ZAVA-Demo"
```

## Presenter Setup

1. Demo-Dateien per One-Liner auf den Desktop kopieren.
2. Den Ordner `ZAVA-Demo` in OneDrive/SharePoint bereitstellen oder einzelne Dateien in Copilot Chat hochladen.
3. Microsoft 365 Copilot Chat oeffnen: https://m365copilot.com
4. Excel im Browser oder Desktop mit `Zava_Order_Analysis.xlsx` oeffnen.
5. Outlook mit dem Email-Thread oder dem generierten Reply-Prompt zeigen.
6. Word und PowerPoint Seeds fuer Office-Agent-/Copilot-Verbesserungen oeffnen.

## Demo Arc

| Segment | Dauer | Kernaussage |
| --- | ---: | --- |
| Signal | 6 min | Copilot findet aus Mail, Meeting, Memo und Briefing die eigentliche Entscheidung. |
| Reasoning | 6 min | Copilot bewertet Feasibility, Engpass, Preisfloor und Bedingungen. |
| Analyse | 8 min | Excel/Copilot macht aus Rohdaten ein belastbares Fulfillment-Bild. |
| Antwort | 7 min | Outlook und Word wandeln Entscheidung in Kundenkommunikation und Operations-Plan. |
| Story | 5 min | PowerPoint erzeugt die Executive Narrative. |
| Scale | 5 min | Agent Builder macht aus dem Ablauf einen wiederholbaren Prozess. |
