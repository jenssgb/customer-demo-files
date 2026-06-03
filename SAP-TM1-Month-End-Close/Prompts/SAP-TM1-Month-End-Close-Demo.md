# SAP TM1 Month-End Close Demo

## 1 · Setup and Story

### Presenter setup

```demo
Open the folder Demos/SAP-TM1-Month-End-Close/data. For the fastest run, use SAP_TM1_Variance_Flat_Table.csv in Copilot Chat or Analyst. For the full heavy run, upload SAP_Actuals_May2026.csv, TM1_Budget_Forecast_May2026.csv, and Account_Mapping_and_Rules.csv together.
```

### Frame the business problem

```demo
Tell the room: SAP is the system of record for actuals. TM1 is the planning and forecast system. The close problem is not calculating one variance; it is reconciling different system grains, mappings, account types, and business meaning quickly enough for Day 3 close review.
```

## 2 · Excel Fast Path: Variance Flat Table

### CFO variance overview

```prompt
Analyze SAP_TM1_Variance_Flat_Table.csv for the May 2026 month-end close. Create a CFO-ready variance overview with:
1. total SAP actuals, TM1 forecast, and absolute variance,
2. top 10 unfavorable variances by company code, property, and GL account,
3. a split by revenue, OpEx, capex, depreciation, finance, and tax,
4. clear explanation of why account type matters for favorability,
5. the three issues I should ask controllers to explain first.
```

### Management summary table

```prompt
Create a management summary table from SAP_TM1_Variance_Flat_Table.csv with these columns: rank, company code, property, account group, SAP GL account, SAP account name, SAP actual, TM1 forecast, absolute variance, favorable variance, variance status, likely root cause, owner question. Use finance language, not generic analytics language.
```

### Variance logic check

```prompt
Check whether the variance interpretation is account-type aware. Revenue should be favorable when actual is higher than forecast. Expense and capex should be unfavorable when actual is higher than forecast. Identify any rows where a naive Actual minus Forecast interpretation would mislead the CFO.
```

```demo
This is the first aha moment: the model should explain that the sign of a variance is not enough. Revenue, expense, capex, and mixed FX accounts need different business interpretation.
```

## 3 · Analyst Heavy Path: Join SAP and TM1

### Multi-file reconciliation

```prompt
Use Analyst. Upload SAP_Actuals_May2026.csv, TM1_Budget_Forecast_May2026.csv, and Account_Mapping_and_Rules.csv. Join SAP actuals to TM1 forecast by company code/entity, posting month/month, property ID, and mapped SAP GL account. Aggregate SAP line items to the same grain as TM1. Then calculate budget variance, forecast variance, favorable variance, and variance percent. Return the top 15 unfavorable variances and explain the root cause pattern.
```

### Mapping gap detection

```prompt
Investigate mapping quality between SAP and TM1. Find:
1. TM1 accounts with no SAP GL mapping,
2. SAP actuals that do not land on a TM1 forecast line,
3. cost center naming or mapping mismatches,
4. properties or entities that appear in only one source,
5. the estimated financial exposure of mapping gaps.
Create a remediation table with issue, examples, exposure, owner, and next action.
```

### Anomaly and audit scan

```prompt
Run a close-control scan on SAP_Actuals_May2026.csv. Detect late postings, high-value manual journals, unusual vendor/account combinations, duplicate-looking adjustments, weekend postings, and large accrual reversals. Summarize the top audit risks and quantify exposure by company code, journal source, and GL account.
```

### Show the code

```prompt
Show me the Python code you used for the SAP vs TM1 reconciliation and anomaly detection. Add comments so a junior FP&A analyst can understand it. Then list which assumptions should be validated before this goes into a real close process.
```

```demo
This is the Analyst differentiation: reproducible Python, joins across files, anomaly logic, and transparent assumptions. It is not just a prettier Excel summary.
```

## 4 · Finance Agent / Excel Variance Analysis Path

### Finance variance criteria

```prompt
Use the variance analysis feature on the workbook or flat table. Focus on May 2026, unfavorable variances above 50,000, and the attributes company code, property, account group, SAP GL account, and account type. Prioritize root causes that could affect the CFO close meeting: revenue shortfall, utility overspend, maintenance spike, capex acceleration, manual journal, late posting, or missing TM1 mapping.
```

### Period-over-period angle

```prompt
Compare May 2026 with the prior months in the dataset. Identify month-over-month trends that make the May variance suspicious or important. Separate recurring run-rate issues from one-time close timing issues.
```

```demo
If the Finance add-in is not available in the tenant, run the same analysis in Analyst using the CSV files. State clearly that the dedicated Finance variance feature is the process-specific Excel experience, while Analyst is the flexible data-science backup path.
```

## 5 · CFO Commentary and Close Meeting

### Draft CFO commentary

```prompt
Draft the May 2026 month-end close commentary for the CFO. Use the SAP vs TM1 variance analysis. Structure it as:
1. Executive summary in 5 bullets,
2. top unfavorable variances and root causes,
3. revenue risks,
4. OpEx and utility overspend,
5. capex and depreciation items,
6. mapping or data-quality issues,
7. decisions needed from the CFO.
Keep it concise, concrete, and suitable for a close review meeting.
```

### Controller questions

```prompt
Create a controller follow-up list for the top 15 unfavorable variances. For each item provide: responsible owner, exact question, evidence needed, due date, and whether this is likely timing, run-rate, forecast miss, mapping issue, or posting error.
```

### Executive slide outline

```prompt
Turn the month-end close findings into a six-slide executive deck outline: 1 close status, 2 P&L variance bridge, 3 top property drivers, 4 control and mapping issues, 5 forecast implications, 6 CFO decisions. For each slide include title, message, visual, and speaker note.
```

## 6 · Agent Builder Close Assistant

### Create the close assistant concept

```prompt
Design a Month-End Close Variance Assistant for Microsoft 365 Copilot. It should help controllers compare SAP actuals with TM1 budget and forecast. Provide: agent purpose, instructions, knowledge sources, starter prompts, guardrails, escalation rules, and a sample answer for a controller asking why utilities are over forecast in May 2026.
```

### Production guardrails

```prompt
Define the production guardrails for a SAP TM1 close assistant. Include data freshness checks, mapping ownership, account-type variance logic, approval rules for manual journals, audit logging, human review thresholds, and what the agent must refuse to answer without source data.
```

```demo
Close the story: the demo starts as ad-hoc analysis, becomes repeatable variance review, and then becomes a governed assistant that finance can call every close cycle.
```
