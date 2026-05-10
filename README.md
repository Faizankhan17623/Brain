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
├── 00-inbox/        Raw sources land here first (auto-synced from claude.ai)
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
├── sync_claude.py   Auto-sync script — fetches new claude.ai chats every 5 hours
├── build_vault_v2.py  Rebuilds Conversations/ from conversations.json export
├── index.md         Master catalog of all wiki pages
├── log.md           Append-only activity log
└── 🏠 Home.md       Vault dashboard
```

---

## Auto-Sync System

New claude.ai conversations automatically sync to `00-inbox/` every 5 hours via `sync_claude.py` running on Windows Task Scheduler.

```
claude.ai chat → Task Scheduler (every 5h) → sync_claude.py → 00-inbox/ → /inbox ingest → vault
```

**Setup:**
```bash
pip install requests python-dotenv
# Add CLAUDE_SESSION_KEY to .env
python sync_claude.py   # test run
```

---

## How It Was Built

### The Pattern (Karpathy LLM-wiki)

- Human drops a source (URL, text, file, conversation)
- Claude reads it, discusses key takeaways, and writes a wiki page
- Claude updates all related pages and the index
- Knowledge compounds over time — one ingest touches 5–15 pages

### Slash Commands

| Command | What it does |
|---------|-------------|
| `/inbox` | Ingests a new source → writes wiki page → updates index.md + log.md |
| `/daily` | Creates today's daily note in 01-daily/ with Yesterday/Tomorrow chain |

### Shortcut Commands

```
"Log application to [Company] for [Role] — status Applied"
"Mark DSA done for today"
"Add [Course] on [Platform] to my course list"
"Add [Name] — [Role] at [Company] — connected today on LinkedIn"
"What do I need to do today?"
"Show my habit streak this week"
```

---

## Tools Used

| Tool | Purpose |
|------|---------|
| [Obsidian](https://obsidian.md) | UI layer — note viewing, graph view, backlinks |
| [Claude Code](https://claude.ai/code) | AI that writes and maintains all content |
| `sync_claude.py` | Pulls new claude.ai chats into 00-inbox/ automatically |
| `build_vault_v2.py` | One-time script to rebuild Conversations/ from JSON export |
| Dataview plugin | Live query tables inside Obsidian |
| Calendar plugin | Calendar sidebar for daily notes |
| Minimal theme | Clean UI theme for Obsidian |

---

## Key Features

- **Auto-sync** — claude.ai chats land in `00-inbox/` every 5 hours automatically
- **Job Hunt Tracker** — every application with follow-up dates, interview rounds, outcome
- **Habit Tracker** — daily checklist with weekly streak table
- **Course List** — all learning resources with status and progress
- **Networking Log** — LinkedIn contacts and recruiters tracker
- **Interview Prep Hub** — company-by-company prep guide
- **Code Snippet Library** — React, Node/Express, Claude API snippets
- **Spaced Repetition Queue** — concepts with review-by dates
- **Daily Notes** — chained Yesterday/Tomorrow navigation

---

## What's Not in This Repo

For privacy, the following are excluded from git:

- `.env` — session keys
- `conversations.json` — raw conversation export (30MB)
- `Conversations/` — private conversation archive
- `00-inbox/` — private synced chats
- `sync_state.json` — sync metadata
- `memories.json`, `users.json`, `projects.json` — private data

---

## About

Built by **Faizan Khan** — MCA student, MERN developer, AI Engineering aspirant.

- Portfolio: [portfolio-pied-eight-2csy0b9zua.vercel.app](https://portfolio-pied-eight-2csy0b9zua.vercel.app/)
- LinkedIn: [linkedin.com/in/FaizanKhan-FullStack](https://www.linkedin.com/in/FaizanKhan-FullStack)
- GitHub: [github.com/Faizankhan17623](https://github.com/Faizankhan17623)
