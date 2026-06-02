# Zava M365 Copilot Universal Demo

## 1 · Signal aus Copilot Chat

### Kontext zusammenfassen

```prompt
Du bist mein Chief of Staff bei Zava. Nutze die bereitgestellten Dateien Zava_Rush_Order_Context.md, Zava_Email_Thread.html und Zava_Launch_Brief.md. Fasse die Situation in 6 Bullet Points zusammen: Kundennachfrage, Deadline, Entscheidung, Risiken, offene Fragen und empfohlener naechster Schritt.
```

### Presenter Action

```demo
Oeffne Microsoft 365 Copilot Chat, lade die drei Kontextdateien hoch oder referenziere sie aus OneDrive, und fuehre den Prompt aus. Betone: Copilot macht aus verstreutem Kontext eine entscheidungsfaehige Lage.
```

### Entscheidungsfrage schaerfen

```prompt
Formuliere daraus eine klare Go/No-Go-Frage fuer Zoe, COO von Zava. Gib mir ausserdem die 5 Datenpunkte, die wir vor der Kundenantwort pruefen muessen.
```

## 2 · Excel Analyse

### Bestand und Kapazitaet bewerten

```prompt
Analysiere Zava_Inventory_Snapshot.csv. Berechne verfuegbare Einheiten plus zusaetzliche 14-Tage-Kapazitaet nach Farbe und Groesse. Reicht das fuer 20.000 Einheiten? Zeige Engpaesse und die kritischsten Risiken.
```

### Marge und Preisempfehlung

```prompt
Berechne eine Preisempfehlung, die mindestens 32 Prozent Bruttomarge schuetzt. Beruecksichtige UnitCostEUR und ExpediteCostEUR. Gib mir eine kurze Management-Empfehlung mit Preisfloor, Risikoannahmen und operativen Sofortmassnahmen.
```

### Presenter Action

```demo
Oeffne die CSV in Excel und nutze Copilot in Excel. Bitte Copilot danach um ein Chart nach Farbe/Risiko und eine kurze Summary-Zelle fuer das Management.
```

## 3 · Outlook Antwort

### Kundenantwort formulieren

```prompt
Entwirf eine Antwort an events-procurement@microsoft.example. Ton: verbindlich, professionell, ruhig. Sage, dass Zava die 20.000 Einheiten grundsaetzlich erfuellen kann, nenne den empfohlenen Preisfloor EUR 25.80, die zwei operativen Voraussetzungen und den transparenten Risikohinweis zu White XL/XXL. Schlage einen 15-Minuten-Call heute vor.
```

### Presenter Action

```demo
Wechsle zu Outlook oder Copilot Chat mit Email-Kontext. Zeige, wie die Antwort aus Analyse + Thread entsteht und nicht bei Null beginnt.
```

## 4 · Word Operations Plan

### Plan erstellen

```prompt
Erstelle einen einseitigen Operations Plan fuer die Zava Rush Order. Struktur: Ziel, Entscheidung, Workstreams, Owner, Deadline heute, Risiken, Mitigations, Kommunikationsplan. Nutze die Rollen aus dem Kontext.
```

### Presenter Action

```demo
Nutze Word Copilot oder den Word Agent. Zeige danach eine Iteration: kuerzer, executive-ready, mit Tabelle fuer Owner und Deadlines.
```

## 5 · PowerPoint Executive Story

### Deck generieren

```prompt
Erstelle eine 5-Slide Executive Story fuer Zoe: 1) Situation, 2) Fulfillment-Plan, 3) Finanzielle Leitplanken, 4) Risiken und Mitigation, 5) Entscheidung und naechste 4 Stunden. Nutze einen modernen Retail-Tech-Ton fuer Zava.
```

### Presenter Action

```demo
Nutze PowerPoint Copilot oder den PowerPoint Agent. Ziel ist nicht perfektes Design, sondern die Story vom Signal zur Entscheidung.
```

## 6 · Agent Builder Skalierung

### Agent entwerfen

```prompt
Entwirf einen Zava Order Desk Agent fuer Microsoft 365 Copilot. Der Agent soll Rush Orders aus Mails, Inventory-Dateien und Launch-Briefings zusammenfassen, Fulfillment-Risiken erkennen, Preisfloor und naechste Aktionen vorschlagen und eine Outlook-Antwort vorbereiten. Gib Instructions, Knowledge Sources, Starter Prompts und Guardrails aus.
```

### Presenter Action

```demo
Oeffne Agent Builder in Microsoft 365 Copilot. Nutze den Output als Bauplan. Erklaere: Aus einem manuellen Copilot-Flow wird ein wiederholbarer Agent.
```
