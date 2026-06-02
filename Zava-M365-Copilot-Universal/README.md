# Zava M365 Copilot Universal Demo

Generische Microsoft 365 Copilot Demo auf Basis der fiktiven Microsoft-Firma **Zava**.

## Ziel

Eine universelle, kundenunabhaengige Demo, die in 25 bis 35 Minuten zeigt, wie Microsoft 365 Copilot vom ersten Business-Signal bis zur entscheidungsreifen Antwort arbeitet:

1. Copilot Chat erkennt den Kontext einer Rush-Order.
2. Excel analysiert Bestand, Kapazitaet, Marge und Risiko.
3. Outlook formuliert eine belastbare Kundenantwort.
4. Word erstellt einen Operations-Plan.
5. PowerPoint erzeugt eine Executive Story.
6. Agent Builder skizziert einen wiederverwendbaren Order-Desk-Agenten.

## Zava Research Summary

Zava ist eine fiktive Microsoft-Demo-Firma aus dem Retail-/Athletic-Wear-Kontext. Microsoft Ignite beschreibt Zava als fictional athletic-wear company in einer Demo zu kollaborativer AI und Produktlaunch-Vorbereitung. Oeffentliche Ignite-/Community-Snippets greifen Zava zudem als fictitious retailer auf, der grosse Bestellungen, Inventory, Quote-Erstellung und Kundenkommunikation mit Microsoft 365 Copilot und Agents koordiniert.

Diese Demo nutzt daraus die stabilste Storyline: **Zava erhaelt eine dringende Grossbestellung fuer 20.000 smarte Launch-Shirts und muss Bestand, Produktionsoptionen, Marge, Risiken und Kundenantwort schnell klaeren.**

## Quellen

- Microsoft Ignite Session `BRK284`: https://ignite.microsoft.com/en-US/sessions/BRK284
- Microsoft 365 Copilot Chat overview: https://learn.microsoft.com/copilot/overview
- Copilot Chat FAQ: https://learn.microsoft.com/copilot/faq
- Microsoft 365 Copilot overview: https://learn.microsoft.com/microsoft-365/copilot/microsoft-365-copilot-overview

## Dateien

| Datei | Zweck |
| --- | --- |
| `Zava-M365-Copilot-Universal-Briefing.html` | Live-Runbook im Clawpilot-Stil mit Copy-Buttons |
| `Prompts/Zava-M365-Copilot-Universal-Demo.md` | PromptPrompter-Datei |
| `data/Zava_Rush_Order_Context.md` | Business-Kontext fuer Chat, Word und PowerPoint |
| `data/Zava_Inventory_Snapshot.csv` | Excel-Demo-Daten fuer Analyse und Charts |
| `data/Zava_Email_Thread.html` | Outlook-/Edge-Kontext fuer Zusammenfassung und Antwort |
| `data/Zava_Launch_Brief.md` | Produkt- und Kampagnenkontext |
| `Deploy-Zava-Demo-Content.ps1` | Upload in den CDX OneDrive/SharePoint Demo-Folder |

## Demo Files One-Liner

Wenn die Dateien im Public Demo-Repo unter `Zava-M365-Copilot-Universal/` liegen, kopiert dieser One-Liner das Paket auf den Desktop der Demo-VM:

```powershell
$d=[Environment]::GetFolderPath('Desktop');$z="$env:TEMP\zava.zip";iwr 'https://github.com/jenssgb/customer-demo-files/archive/refs/heads/main.zip' -OutFile $z;ri "$d\ZAVA-Demo" -r -fo -ea 0;Expand-Archive $z "$env:TEMP\zava" -Force;mv "$env:TEMP\zava\customer-demo-files-main\Zava-M365-Copilot-Universal" "$d\ZAVA-Demo";ri $z,"$env:TEMP\zava" -r -fo;ii "$d\ZAVA-Demo"
```

## Presenter Setup

1. Demo-Dateien auf Desktop kopieren.
2. `Zava_Rush_Order_Context.md`, `Zava_Inventory_Snapshot.csv`, `Zava_Email_Thread.html` und `Zava_Launch_Brief.md` in OneDrive/SharePoint bereitstellen oder lokal in Copilot Chat hochladen.
3. Microsoft 365 Copilot Chat oeffnen: https://m365copilot.com
4. Excel im Browser oder Desktop mit `Zava_Inventory_Snapshot.csv` oeffnen.
5. Optional: Outlook mit dem Email-Thread als Kontext zeigen.

## Demo Arc

| Segment | Dauer | Kernaussage |
| --- | ---: | --- |
| Signal | 5 min | Copilot findet aus Mail, Briefing und Daten die eigentliche Entscheidung. |
| Analyse | 8 min | Excel/Copilot macht aus Rohdaten ein belastbares Fulfillment-Bild. |
| Antwort | 7 min | Outlook und Word wandeln Entscheidung in Kundenkommunikation und Operations-Plan. |
| Story | 5 min | PowerPoint erzeugt die Executive Narrative. |
| Scale | 5 min | Agent Builder macht aus dem Ablauf einen wiederholbaren Prozess. |
