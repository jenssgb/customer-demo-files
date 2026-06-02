# Zava Top M365 Copilot Demo

## 1 · Copilot Chat Lagebild

### Boardroom Brief erstellen

```prompt
Du bist mein Chief of Staff bei Zava. Nutze Zava_Rush_Order_Context.md, Zava_Email_Thread.html, Zava_Meeting_Transcript.md und Zava_Executive_Decision_Memo.md. Erstelle ein Boardroom Briefing in 7 Punkten: Entscheidung, Deadline, Kundenziel, kritische Abhaengigkeiten, Risiken, offene Owner-Actions und empfohlene Haltung.
```

### Presenter Action

```demo
Oeffne Microsoft 365 Copilot Chat, lade die Dateien hoch oder referenziere sie aus OneDrive. Betone: Copilot macht aus verstreutem Kontext eine entscheidungsfaehige Lage.
```

### Copilot Page strukturieren

```prompt
Formatiere das Briefing als Copilot Page mit drei Bereichen: 1) Decision statement, 2) Evidence to verify, 3) Customer response principles. Schreibe so, dass Zoe, Maya, Omar, Lena und Rafael direkt weiterarbeiten koennen.
```

## 2 · Analyst Style Reasoning

### Feasibility und Preisfloor analysieren

```prompt
Analysiere Zava_Order_Analysis.xlsx sowie Zava_Risk_Register.csv und Zava_Pricing_Assumptions.csv. Beantworte: 1) Kann Zava 20.000 Einheiten in 14 Tagen zusagen? 2) Welche SKU oder Abhaengigkeit ist der Engpass? 3) Welcher Preisfloor schuetzt 32 Prozent Marge? 4) Welche Bedingungen muessen in die Kundenantwort?
```

### Entscheidungstabelle fuer Zoe

```prompt
Erstelle eine Entscheidungstabelle mit den Spalten: Entscheidungspunkt, Fakt, Risiko, Owner, Bedingung fuer Zusage, Kommunikationshinweis. Schließe mit einer 3-Satz-Empfehlung fuer Zoe.
```

### Presenter Action

```demo
Nutze wenn verfuegbar Think deeper oder Analyst-artiges Reasoning. Zeige, dass Copilot nicht nur zusammenfasst, sondern Abhaengigkeiten gegeneinander abwaegt.
```

## 3 · Excel Workbook

### Dashboard erklaeren

```prompt
Analysiere dieses Workbook. Starte auf dem Executive Summary Sheet. Erklaere die wichtigsten Zahlen, identifiziere die Engpaesse nach SKU/Farbe/Groesse und schlage zwei Visualisierungen vor, die Zoe in 60 Sekunden versteht.
```

### Management Summary erzeugen

```prompt
Fuege eine Management Summary hinzu: 1) Gesamtversorgung vs. Anfrage, 2) Risikoampel je Farbe, 3) empfohlener Preisfloor, 4) naechste Aktion je Owner. Erzeuge danach ein Chart fuer Total14DaySupply nach Farbe.
```

### Presenter Action

```demo
Oeffne Zava_Order_Analysis.xlsx in Excel. Zeige Executive Summary, Inventory-Formeln und den Chart. Danach Copilot um ein Management Summary bitten.
```

## 4 · Outlook Kundenantwort

### Antwort formulieren

```prompt
Entwirf eine Antwort an events-procurement@microsoft.example. Ton: ruhig, verbindlich, executive-ready. Sage: Zava kann grundsaetzlich zusagen, wenn heute Kapazitaet, NFC-Aktivierung und Singapore-Freight bestaetigt werden. Nenne EUR 25.80 als Preisfloor, erwaehne White XL/XXL transparent und schlage einen 15-Minuten-Call heute vor.
```

### Coach by Copilot

```prompt
Verbessere die Antwort auf Klarheit, Ton und Risiko-Transparenz. Entferne interne Kostendetails. Mache die Bedingungen fuer die Zusage explizit, aber kundenfreundlich.
```

### Presenter Action

```demo
Wechsle in Outlook oder nutze den Email Thread in Copilot Chat. Zeige: Die Antwort ist nicht generisch, sondern basiert auf Analyse, Risiko und Preisfloor.
```

## 5 · Word Operations Plan

### Plan verbessern

```prompt
Oeffne Zava_Operations_Plan.docx und ueberarbeite ihn fuer Zoe. Ergaenze eine Executive Summary, eine Risikoampel und eine Tabelle "Next 4 hours" mit Owner, Deadline, Dependency und Done Definition.
```

### Word Agent Alternative

```prompt
Erstelle ein neues Word-Dokument mit dem Titel "Zava Rush Order War Room Plan". Nutze alle Zava-Dateien als Kontext. Struktur: Decision, Evidence, Risks, Workstreams, Customer Message, Executive Approval Checklist.
```

### Presenter Action

```demo
Zeige den Unterschied zwischen Kundenantwort und internem Operations-Plan. Optional: Word Agent aus Copilot Chat verwenden, wenn verfuegbar.
```

## 6 · PowerPoint Executive Story

### Deck verbessern

```prompt
Oeffne Zava_Executive_Story.pptx. Verbessere das Deck fuer Zoe: fuege Sprecherhinweise hinzu, mache die Entscheidung auf Slide 5 noch klarer und ergaenze auf Slide 3 eine klare Risikoampel fuer White XL/XXL, NFC activation und Singapore freight.
```

### PowerPoint Agent Alternative

```prompt
Erstelle eine neue 6-Slide Praesentation fuer die COO-Entscheidung. Nutze Zava_Order_Analysis.xlsx, Zava_Executive_Decision_Memo.md, Zava_Risk_Register.csv und Zava_Meeting_Transcript.md. Slides: 1 Situation, 2 Customer ask, 3 Feasibility, 4 Margin guardrails, 5 Risks and mitigations, 6 Decision.
```

### Presenter Action

```demo
Oeffne den PowerPoint-Seed oder nutze den PowerPoint Agent. Ziel: Executive Story statt Folienmalerei.
```

## 7 · Agent Builder Skalierung

### Order Desk Agent entwerfen

```prompt
Entwirf einen Zava Order Desk Agent fuer Microsoft 365 Copilot. Nutze Zava_Agent_Builder_Brief.md als Grundlage. Gib aus: Agent Purpose, Instructions, Knowledge Sources, Starter Prompts, Guardrails, Escalation Rules und Beispielantwort fuer eine neue Rush Order.
```

### Agent Test Case

```prompt
Teste den Agenten mit Request ZO-1044 aus Zava_Order_Intake.csv. Fasse die Order zusammen, nenne die drei wichtigsten Pruefpunkte und formuliere eine knappe Empfehlung fuer Sales Operations.
```

### Presenter Action

```demo
Oeffne Agent Builder in Microsoft 365 Copilot. Nutze den Output als Bauplan. Erklaere: Aus einem manuellen Copilot-Flow wird ein wiederholbarer Order-Desk-Prozess.
```
