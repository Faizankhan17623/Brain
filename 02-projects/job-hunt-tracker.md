---
title: "Job Hunt Tracker"
date: 2026-04-27
type: project
status: active
tags:
  - job-hunt
  - tracker
  - career
---

# Job Hunt Tracker

Live tracker for every job application Faizan has sent. Update this after every application, interview, or status change.

---

## How to Update

Tell Claude: *"Log application to [Company] for [Role] on [Date] — status [Applied/Interview/Rejected/Offer]"*
Tell Claude: *"Update [Company] status to [new status]"*

---

## Application Table

| # | Company | Role | Applied | ATS Score | Status | Follow-up Date | Interview Round | Outcome | Notes |
|---|---------|------|---------|-----------|--------|---------------|-----------------|---------|-------|
| 1 | [[Zensar Technologies]] | Full Stack Developer | 2026-04-20 | 100% | Applied | 2026-04-27 | — | — | Job ID 142126 |
| 2 | [[Cognizant GenC]] | GenC Developer | 2026-04 | — | Applied | 2026-04-27 | — | — | Fresher program |
| 3 | [[Sarvam AI]] | Frontend Intern | 2026-04 | — | Applied | 2026-04-27 | — | — | Arya Team |
| 4 | [[CloudSEK]] | Fresher Engineer | 2026-04 | — | Applied | 2026-04-27 | — | — | Cybersecurity |
| 5 | [[Tech Mahindra]] | Associate Software Engineer | 2026-04 | — | Applied | 2026-04-27 | — | — | Off-campus |
| 6 | [[Primis Digital]] | Jr. Python Full Stack Developer | 2026-04 | — | Applied | 2026-04-27 | — | — | Python + MERN |
| 7 | [[Weave]] | — | 2026-04 | — | Applied | 2026-04-27 | — | — | — |

---

## Status Legend

| Status | Meaning |
|--------|---------|
| **Applied** | Application submitted, waiting |
| **OA** | Online Assessment received |
| **Interview** | Interview scheduled or done |
| **Offer** | Offer received |
| **Rejected** | Rejected or ghosted |
| **Withdrawn** | Withdrew application |

---

## Stats

| Metric | Count |
|--------|-------|
| Total Applied | 7 |
| Active (waiting) | 7 |
| Interviews | 0 |
| Offers | 0 |
| Rejected | 0 |

---

## Interview Prep Links

- [[MOC - Career & Jobs]]
- [[Resume Building]]
- [[LinkedIn Profile]]
- [[DSA Learning]]

---

## Dataview Query (requires Dataview plugin)

```dataview
TABLE company, role, status, next-step
FROM "02-projects"
WHERE type = "application"
SORT date DESC
```

---

*Last updated: 2026-04-27*
