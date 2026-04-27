# Faizan's Brain

A personal knowledge wiki built and maintained using the **Karpathy LLM-wiki pattern** — where an AI (Claude) writes and maintains all wiki content, and the human curates sources, asks questions, and directs analysis.

---

## What This Is

This vault is a persistent, compounding second brain. Knowledge is compiled once and kept current — not re-derived on every query. It covers career, learning, projects, health, and personal life.

Built with **Obsidian** as the UI layer and **Claude Code** as the AI that writes and maintains everything.

---

## Vault Structure

```
Brain/
├── 00-inbox/        Raw sources land here first
├── 01-daily/        YYYY-MM-DD daily notes
├── 02-projects/     Active project notes and trackers
├── 03-meetings/     Meeting notes
├── 04-resources/    Reference pages, learnings, concept wiki pages
├── 05-goals/        Annual + quarterly goals
├── 06-people/       CRM-style notes on contacts
├── 07-archive/      Completed/archived notes
│
├── Conversations/   Archive of 97 Claude conversation exports (read-only)
├── Projects/        Hub pages: Cine Circuit, StudyNotion, LinkVault
├── Topics/          Topic wiki pages: AI Engineering, MERN Stack, DSA, etc.
├── Companies/       Target employer hub pages
├── People/          Personal CRM pages
│
├── index.md         Master catalog of all wiki pages
├── log.md           Append-only activity log
└── 🏠 Home.md       Vault dashboard
```

---

## How It Was Built

### The Pattern (Karpathy LLM-wiki)

The idea is simple:
- Human drops a source (URL, text, file, conversation)
- Claude reads it, discusses key takeaways, and writes a wiki page
- Claude updates all related pages and the index
- Knowledge compounds over time — one ingest touches 5–15 pages

### Prompts Used

**Vault initialization prompt:**
```
You are maintaining a personal Obsidian wiki using the Karpathy LLM-wiki pattern.
Claude writes and maintains all wiki content. I curate sources and direct analysis.
The wiki is a persistent, compounding artifact — knowledge is compiled once and kept current.
```

**Ingest prompt (for new sources):**
```
/inbox [paste URL or text here]
```
Claude then: reads the source → discusses takeaways → writes a summary page in 04-resources/ → updates index.md → updates related pages → appends to log.md.

**Query prompt:**
```
[Ask any question about your own knowledge base]
```
Claude then: reads index.md → drills into relevant pages → synthesizes answer with wikilink citations → files reusable answers back as new pages.

**Daily note prompt:**
```
/daily
```
Claude creates today's daily note in 01-daily/YYYY-MM-DD.md with correct frontmatter and Yesterday/Tomorrow chain links.

**Shortcut commands:**
```
"Log application to [Company] for [Role] — status Applied"
"Mark DSA done for today"
"Add [Course] on [Platform] to my course list"
"Add [Name] — [Role] at [Company] — connected today on LinkedIn"
"What do I need to do today?"
```

---

## Tools Used

| Tool | Purpose |
|------|---------|
| [Obsidian](https://obsidian.md) | UI layer — note viewing, graph view, backlinks |
| [Claude Code](https://claude.ai/code) | AI that writes and maintains all content |
| Dataview plugin | Live query tables inside Obsidian |
| Calendar plugin | Calendar sidebar for daily notes |
| Minimal theme | Clean UI theme for Obsidian |

---

## Key Features

- **Job Hunt Tracker** — every application with follow-up dates, interview rounds, outcome
- **Habit Tracker** — daily checklist with weekly streak table
- **Course List** — all learning resources with status and progress
- **Networking Log** — LinkedIn contacts and recruiters tracker
- **Interview Prep Hub** — company-by-company prep guide
- **Code Snippet Library** — React, Node/Express, Claude API snippets
- **Spaced Repetition Queue** — concepts with review-by dates
- **Daily Notes** — chained Yesterday/Tomorrow navigation

---

## About

Built by **Faizan Khan** — MCA student, MERN developer, AI Engineering aspirant.

- Portfolio: [portfolio-pied-eight-2csy0b9zua.vercel.app](https://portfolio-pied-eight-2csy0b9zua.vercel.app/)
- LinkedIn: [linkedin.com/in/FaizanKhan-FullStack](https://www.linkedin.com/in/FaizanKhan-FullStack)
- GitHub: [github.com/Faizankhan17623](https://github.com/Faizankhan17623)
