# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## What This Vault Is

Faizan's Brain is a personal Obsidian wiki maintained by Claude using the Karpathy LLM-wiki pattern. Claude writes and maintains all wiki content. Faizan curates sources, asks questions, and directs analysis. The wiki is a **persistent, compounding artifact** — knowledge is compiled once and kept current, not re-derived on every query.

The existing `Conversations/` folder (97 Claude conversation files) is the original archive built by `build_vault_v2.py`. That archive is **read-only** source material. All new wiki pages go into the numbered folders.

---

## About Faizan

22-year-old MCA student (2025–2027) at [[Allana Institute]], [[Pune]]. BCA graduate, CGPA 8.10, [[Poona College]]. Self-taught MERN stack developer transitioning to AI Engineering. Active fresher job hunt (Full Stack + AI Engineering roles in India).

**Contact:** fk3701@gmail.com | +91 90115 75978

---

## Vault Structure

```
Brain/
├── 00-inbox/        Raw sources land here first
├── 01-daily/        YYYY-MM-DD.md daily notes, chained Yesterday/Tomorrow
├── 02-projects/     One sub-folder per active project
├── 03-meetings/     Meeting notes with date, attendees, project tag
├── 04-resources/    Reference pages, learnings, concept wiki pages
├── 05-goals/        Annual + quarterly goals
├── 06-people/       CRM-style notes on contacts
├── 07-archive/      Never delete — move here when done
│
├── Conversations/   READ-ONLY archive of 97 Claude conversation exports
├── Projects/        Hub pages: Cine Circuit, StudyNotion, LinkVault
├── Topics/          Topic wiki pages: AI Engineering, MERN Stack, DSA, etc.
├── Companies/       Target employer hub pages
├── Places/          Pune, India, Palestine
├── Schools/         Allana Institute, Poona College
├── People/          Faizan Khan, Dr. Gaikwad
├── Maps of Content/ MOC-* index pages
│
├── index.md         Master catalog of all wiki pages (updated on every ingest)
├── log.md           Append-only chronological record (ingest / query / lint)
└── 🏠 Home.md       Vault dashboard
```

---

## YAML Frontmatter Convention

Every note must have frontmatter:

```yaml
---
title: "Note Title"
date: YYYY-MM-DD
type: daily | inbox | project | meeting | resource | goal | person | topic | moc
status: active | done | archived
tags:
  - kebab-case-only
source: "URL or filename"
---
```

Rules:
- Tags always kebab-case (#ai-engineering, not #AIEngineering)
- Every mention of a project, person, company, or concept uses [[wikilinks]]
- Never delete files — move to 07-archive/ instead
- Daily notes always chain: Yesterday: [[YYYY-MM-DD]] and Tomorrow: [[YYYY-MM-DD]]

---

## Three Core Operations

### Ingest (new source → wiki)
When Faizan drops a file into 00-inbox/ or pastes a URL/text:
1. Read the source
2. Discuss key takeaways with Faizan
3. Write a summary page in 04-resources/ (or appropriate folder)
4. Update index.md with the new page
5. Update any relevant existing pages (Topics, Projects, People, Companies)
6. Append to log.md: ## [YYYY-MM-DD] ingest | Source Title

A single ingest may touch 5-15 wiki pages. That is expected and correct.

### Query (question → answer → file)
1. Read index.md to find relevant pages
2. Drill into those pages
3. Synthesize answer with [[citations]]
4. If the answer is reusable knowledge, file it back as a new wiki page in 04-resources/
5. Append to log.md: ## [YYYY-MM-DD] query | Question summary

### Lint (health check)
Scan for orphan pages, contradictions, stale claims, missing cross-references.
Append to log.md: ## [YYYY-MM-DD] lint | Issues found / fixed

---

## Active Projects (as of 2026-04)

| Project | Status | Notes |
|---------|--------|-------|
| [[Cine Circuit]] | Production | MERN, 79 REST endpoints, Razorpay, MongoDB |
| [[StudyNotion]] | Production | EdTech LMS, Redux Toolkit, Cloudinary |
| [[LinkVault]] | Planned | Bookmark manager, MERN + PWA |

---

## Active Learning Tracks

- [[AI Engineering]] — primary career target; LLMs, agents, RAG, Claude API
- [[MERN Stack]] — current stack
- [[Python Learning]] — for AI track (Chapters 2-9 done)
- [[DSA Learning]] — JavaScript-first, LeetCode
- [[Mathematics]] — Grade 6-10 foundation for AI/ML

---

## Job Hunt Context

Fresher targeting Full Stack Developer + AI Engineering roles in India.

Target companies: [[Zensar Technologies]] (Job ID 142126, 100% ATS), [[Cognizant GenC]], [[Sarvam AI]] (Frontend Intern – Arya Team), [[CloudSEK]], [[Tech Mahindra]], [[Primis Digital]], [[Weave]]

Anthropic certifications: Claude Code in Action, Building with Claude API, MCP Introduction.

---

## Builder Scripts (Legacy Archive)

```bash
python build_vault_v2.py   # Rebuilds Conversations/ from conversations.json
python build_vault.py      # v1 (deprecated)
```

build_vault_v2.py tags using Faizan's messages only to avoid false-positive tags. No external dependencies.

---

## Special Files

| File | Purpose |
|------|---------|
| index.md | Master catalog of all wiki pages by category — read this first on every query |
| log.md | Append-only log: ## [YYYY-MM-DD] type | description |
| 🏠 Home.md | Vault dashboard — quick links and stats |

---

## Slash Commands

| Command | What it does |
|---------|-------------|
| /daily | Creates or opens today's 01-daily/YYYY-MM-DD.md with correct frontmatter and Yesterday/Tomorrow chain |
| /inbox | Ingests whatever Faizan provides (URL, text, file) — summarizes, files to 04-resources/, updates index.md and log.md |

---

## Shortcut Commands (tell Claude these)

### Job Hunt
- *"Log application to [Company] for [Role] — status Applied"* → adds row to job-hunt-tracker
- *"Update [Company] status to Interview / Rejected / Offer"* → updates job-hunt-tracker
- *"Show all jobs I applied to this month"* → reads job-hunt-tracker and summarizes

### Habits
- *"Mark [habit] done for today"* → ticks off habit in habit-tracker
- *"Log today's habits — [list]"* → updates habit-tracker checklist
- *"Show my habit streak this week"* → reads habit-tracker weekly table

### Courses & Learning
- *"Add [course] on [platform] to my course list"* → adds row to course-list
- *"Mark [course] as done"* → updates status in course-list
- *"I finished [chapter/topic] of [course]"* → updates progress in course-list

### Networking
- *"Add [Name] — [Role] at [Company] — connected today, talked about [topic]"* → adds to networking-log
- *"Follow up with [Name] on [date]"* → updates follow-up column
- *"Update [Name] — they replied and said [X]"* → updates networking-log

### General
- *"Open my brain home"* → reads 🏠 Home.md
- *"What do I need to do today?"* → reads habit-tracker + job tracker
- *"Lint my vault"* → scans for orphan pages, missing links, stale content
