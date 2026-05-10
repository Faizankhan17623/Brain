"""
Obsidian Vault Builder for Faizan's Claude Conversation Archive
Creates markdown files with frontmatter from conversations.json, projects.json, memories.json
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

VAULT = Path("C:/Users/fk241/OneDrive/Desktop/Brain")

# ─── Auto-tagging keyword map ────────────────────────────────────────────────
TAG_RULES = [
    (["ai engineer", "ai engineering", "agentic ai", "llm", "ollama", "anthropic", "claude api", "openai"],
     ["ai-engineering", "technical-learning"]),
    (["ml engineer", "machine learning", "data scientist", "neural network"],
     ["ml-engineering", "technical-learning"]),
    (["resume", "ats", "jobscan", "cv", "latex", "overleaf"],
     ["resume", "job-hunting"]),
    (["linkedin", "linkedin profile", "linkedin optimization"],
     ["linkedin", "job-hunting"]),
    (["job", "fresher", "interview", "hiring", "placement", "apply", "application"],
     ["job-hunting"]),
    (["mern", "react", "node.js", "nodejs", "mongodb", "express", "full stack", "fullstack"],
     ["mern-stack", "web-development"]),
    (["python", "python crash course", "pip", "venv", "jupyter"],
     ["python", "programming"]),
    (["dsa", "data structures", "algorithms", "leetcode", "two pointer", "brute force", "array"],
     ["dsa", "programming"]),
    (["math", "mathematics", "fraction", "integer", "geometry", "algebra", "decimal"],
     ["mathematics", "learning"]),
    (["ear", "tinnitus", "hearing", "audiogram", "ent", "infection", "wisdom teeth", "doctor"],
     ["health", "medical"]),
    (["fitness", "weight", "gym", "exercise", "jawline", "diet"],
     ["health", "fitness"]),
    (["cine circuit", "movie booking", "ticket", "theatre", "razorpay"],
     ["project-cine-circuit", "projects"]),
    (["studynotion", "edtech", "lms", "cloudinary"],
     ["project-studynotion", "projects"]),
    (["linkvault", "bookmark"],
     ["project-linkvault", "projects"]),
    (["islam", "islamic", "prayer", "quran", "hadith", "religion", "ahlul", "faith", "muslim"],
     ["islam", "religion", "personal"]),
    (["marriage", "rishta", "proposal", "relationship"],
     ["personal", "life"]),
    (["css", "html", "javascript", "frontend", "ui", "design"],
     ["frontend", "web-development"]),
    (["git", "github", "collaboration", "repository"],
     ["git", "programming"]),
    (["mysql", "database", "sql"],
     ["database", "programming"]),
    (["roadmap", "learning plan", "study plan", "schedule"],
     ["learning", "planning"]),
    (["cybersecurity", "ethical hacker", "hacking", "security"],
     ["cybersecurity", "security"]),
    (["payment", "upi", "phonepe", "gpay", "money"],
     ["finance", "personal"]),
    (["college", "mca", "bca", "semester", "exam", "student"],
     ["education", "college"]),
    (["websocket", "api", "rest", "endpoint", "backend"],
     ["backend", "web-development"]),
    (["freelance", "startup", "company", "work"],
     ["career"]),
    (["cognizant", "zensar", "tech mahindra", "sarvam", "primis", "weave", "cloudsek"],
     ["job-hunting", "companies"]),
    (["astrology", "horoscope"],
     ["personal", "astrology"]),
    (["java", "practical"],
     ["java", "programming", "education"]),
    (["instagram", "social media", "bio"],
     ["social-media", "personal"]),
]

CATEGORY_MAP = {
    "career": ["job", "resume", "ats", "linkedin", "interview", "hiring", "fresher", "placement"],
    "technical-learning": ["python", "dsa", "algorithm", "data structure", "leetcode", "programming"],
    "mathematics": ["math", "fraction", "integer", "geometry", "decimal", "algebra", "hcf", "lcm"],
    "ai-ml": ["ai engineer", "ml engineer", "machine learning", "llm", "ollama", "agentic"],
    "web-development": ["mern", "react", "node", "mongodb", "express", "css", "html", "javascript", "frontend", "backend"],
    "projects": ["cine circuit", "studynotion", "linkvault", "ticket", "theatre", "razorpay", "booking"],
    "health": ["ear", "tinnitus", "hearing", "fitness", "weight", "gym", "jawline", "audiogram", "doctor"],
    "personal": ["islam", "marriage", "rishta", "prayer", "religion", "instagram", "astrology", "personal"],
    "education": ["college", "mca", "bca", "semester", "exam", "java practical"],
    "cybersecurity": ["ethical hacker", "hacking", "cybersecurity", "security", "unauthorized"],
}

def infer_tags(text_lower):
    tags = set()
    for keywords, tag_list in TAG_RULES:
        if any(kw in text_lower for kw in keywords):
            tags.update(tag_list)
    return sorted(tags)

def infer_category(text_lower):
    scores = {}
    for category, keywords in CATEGORY_MAP.items():
        score = sum(1 for kw in keywords if kw in text_lower)
        if score > 0:
            scores[category] = score
    if not scores:
        return "general"
    return max(scores, key=scores.get)

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name[:100] if name else "Untitled"

def format_message(msg):
    sender = "**Faizan**" if msg.get("sender") == "human" else "**Claude**"
    text = msg.get("text", "").strip()
    if not text:
        content = msg.get("content", [])
        if content:
            text = " ".join(c.get("text", "") for c in content if isinstance(c, dict)).strip()
    if not text:
        return ""
    ts = msg.get("created_at", "")[:16].replace("T", " ")
    return f"{sender} `{ts}`\n\n{text}\n\n---\n"

def build_conversation_md(conv, index):
    uuid = conv.get("uuid", "")
    name = conv.get("name", "").strip() or "Untitled Conversation"
    summary = conv.get("summary", "").strip()
    created = conv.get("created_at", "")
    updated = conv.get("updated_at", "")
    messages = conv.get("chat_messages", [])

    created_date = created[:10] if created else "unknown"
    created_full = created[:19].replace("T", " ") if created else ""
    updated_full = updated[:19].replace("T", " ") if updated else ""

    combined_text = (name + " " + summary + " " +
                     " ".join(m.get("text", "") for m in messages[:10])).lower()

    tags = infer_tags(combined_text)
    category = infer_category(combined_text)

    # Detect people mentioned
    people = ["[[Faizan Khan]]"]
    people_raw = ["Faizan Khan"]
    if any(x in combined_text for x in ["dr. gaikwad", "gaikwad", "ent"]):
        people.append("[[Dr. Gaikwad]]")
        people_raw.append("Dr. Gaikwad")

    # Detect project links
    projects_linked = []
    if any(x in combined_text for x in ["cine circuit", "movie booking", "theatre", "razorpay"]):
        projects_linked.append("[[Cine Circuit]]")
    if any(x in combined_text for x in ["studynotion", "edtech", "lms"]):
        projects_linked.append("[[StudyNotion]]")
    if any(x in combined_text for x in ["linkvault", "bookmark manager"]):
        projects_linked.append("[[LinkVault]]")

    # Topic links
    topic_links = []
    if any(x in combined_text for x in ["ai engineer", "agentic ai", "llm"]):
        topic_links.append("[[AI Engineering]]")
    if any(x in combined_text for x in ["mern", "react", "node"]):
        topic_links.append("[[MERN Stack]]")
    if any(x in combined_text for x in ["resume", "ats"]):
        topic_links.append("[[Resume Building]]")
    if any(x in combined_text for x in ["dsa", "algorithm", "two pointer"]):
        topic_links.append("[[DSA Learning]]")
    if any(x in combined_text for x in ["math", "fraction", "geometry"]):
        topic_links.append("[[Mathematics]]")
    if any(x in combined_text for x in ["python"]):
        topic_links.append("[[Python Learning]]")
    if any(x in combined_text for x in ["linkedin"]):
        topic_links.append("[[LinkedIn Profile]]")
    if any(x in combined_text for x in ["job", "interview", "hiring", "fresher"]):
        topic_links.append("[[Job Hunting]]")
    if any(x in combined_text for x in ["ear", "tinnitus", "audiogram"]):
        topic_links.append("[[Ear Health]]")
    if any(x in combined_text for x in ["fitness", "weight", "gym", "jawline"]):
        topic_links.append("[[Fitness Journey]]")
    if any(x in combined_text for x in ["islam", "prayer", "quran", "hadith"]):
        topic_links.append("[[Islam & Faith]]")

    # Remove duplicates
    topic_links = list(dict.fromkeys(topic_links))

    tags_yaml = "\n".join(f"  - {t}" for t in tags) if tags else "  - general"
    people_yaml = "\n".join(f'  - "{p}"' for p in people_raw)
    projects_yaml = "\n".join(f'  - "{p.strip("[]")}"' for p in projects_linked) if projects_linked else ""
    topics_yaml = "\n".join(f'  - "{t.strip("[]")}"' for t in topic_links) if topic_links else ""

    frontmatter = f"""---
title: "{name.replace('"', "'")}"
date: {created_date}
created: {created_full}
updated: {updated_full}
uuid: {uuid}
category: {category}
message_count: {len(messages)}
tags:
{tags_yaml}
people:
{people_yaml}
"""
    if projects_yaml:
        frontmatter += f"projects:\n{projects_yaml}\n"
    if topics_yaml:
        frontmatter += f"related_topics:\n{topics_yaml}\n"
    frontmatter += "---\n"

    # Body
    num = str(index).zfill(3)
    body = f"# {name}\n\n"

    # Backlinks section
    if topic_links or projects_linked or people:
        body += "## Connections\n"
        if people:
            body += "**People:** " + " · ".join(people) + "\n\n"
        if projects_linked:
            body += "**Projects:** " + " · ".join(projects_linked) + "\n\n"
        if topic_links:
            body += "**Topics:** " + " · ".join(topic_links) + "\n\n"

    if summary:
        body += f"## Summary\n\n{summary}\n\n"

    if messages:
        body += f"## Conversation\n\n"
        for msg in messages:
            formatted = format_message(msg)
            if formatted:
                body += formatted

    return frontmatter + body

def create_vault_structure():
    dirs = [
        VAULT / "Conversations",
        VAULT / "Projects",
        VAULT / "People",
        VAULT / "Topics",
        VAULT / "Maps of Content",
        VAULT / "_attachments",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    print("Created directory structure.")

def write_conversations(conversations):
    conv_dir = VAULT / "Conversations"
    written = 0
    for i, conv in enumerate(conversations, 1):
        name = conv.get("name", "").strip() or "Untitled"
        safe_name = sanitize_filename(name)
        num = str(i).zfill(3)
        filename = f"{num} - {safe_name}.md"
        filepath = conv_dir / filename
        content = build_conversation_md(conv, i)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        written += 1
        if written % 10 == 0:
            print(f"  Written {written}/{len(conversations)} conversations...")
    print(f"Done: {written} conversation files created.")

def write_project_files():
    projects_data = [
        {
            "name": "Cine Circuit",
            "description": "Full-stack movie booking platform with multi-role dashboards (Admin, Theatre Owner, User, Organizer). Features 79 REST endpoints, 26 MongoDB collections, HMAC-SHA256 payment verification, cron-based ticket lifecycle management, and Razorpay integration.",
            "tech": ["MERN Stack", "MongoDB", "Express.js", "React", "Node.js", "Razorpay", "JWT", "Cloudinary"],
            "status": "Production",
            "tags": ["project", "full-stack", "mern-stack", "production"],
            "links": ["[[MERN Stack]]", "[[Job Hunting]]", "[[Resume Building]]"],
        },
        {
            "name": "StudyNotion",
            "description": "EdTech LMS (Learning Management System) with Redux Toolkit across 6 slices, MongoDB full-text search, Cloudinary media management. Used as portfolio project in job applications.",
            "tech": ["MERN Stack", "Redux Toolkit", "MongoDB", "Cloudinary"],
            "status": "Production",
            "tags": ["project", "full-stack", "mern-stack", "edtech", "production"],
            "links": ["[[MERN Stack]]", "[[Job Hunting]]", "[[Resume Building]]"],
        },
        {
            "name": "LinkVault",
            "description": "Planned full-stack bookmark manager app. MERN + PWA, Redux Toolkit, Tailwind CSS, JWT auth, deployed on Atlas/Render/Vercel.",
            "tech": ["MERN Stack", "Redux Toolkit", "Tailwind CSS", "JWT", "PWA"],
            "status": "Planned",
            "tags": ["project", "full-stack", "mern-stack", "planned"],
            "links": ["[[MERN Stack]]"],
        },
    ]

    for proj in projects_data:
        tags_yaml = "\n".join(f"  - {t}" for t in proj["tags"])
        tech_yaml = "\n".join(f'  - "{t}"' for t in proj["tech"])
        content = f"""---
title: "{proj['name']}"
type: project
status: {proj['status']}
tags:
{tags_yaml}
tech_stack:
{tech_yaml}
---

# {proj['name']}

## Overview

{proj['description']}

## Tech Stack

{chr(10).join('- ' + t for t in proj['tech'])}

## Related

{chr(10).join('- ' + l for l in proj['links'])}

## Conversations

> [!note] Auto-linked conversations mentioning this project appear below via Obsidian backlinks.
"""
        filepath = VAULT / "Projects" / f"{proj['name']}.md"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    print("Written project files.")

def write_people_files():
    people = [
        {
            "name": "Faizan Khan",
            "role": "Self",
            "bio": "22-year-old MCA student (2025–2027) at Allama Institute of Management Sciences, Pune. BCA graduate (CGPA 8.10) from Poona College. Self-taught MERN stack developer targeting AI Engineering as career. Phone: +91 90115 75978. Email: fk3701@gmail.com. LinkedIn: linkedin.com/in/faizan-fullstack. GitHub: github.com/Faizankhan17623.",
            "tags": ["person", "self", "mern-developer", "mca-student", "ai-engineer-aspirant"],
        },
        {
            "name": "Dr. Gaikwad",
            "role": "ENT Specialist",
            "bio": "ENT specialist who treated Faizan for ear infection, tinnitus, and post-wisdom teeth surgery issues. Administered audiogram showing left ear normalized, right ear improved to mild.",
            "tags": ["person", "doctor", "ent-specialist"],
        },
    ]

    for person in people:
        tags_yaml = "\n".join(f"  - {t}" for t in person["tags"])
        content = f"""---
title: "{person['name']}"
type: person
role: {person['role']}
tags:
{tags_yaml}
---

# {person['name']}

**Role:** {person['role']}

## About

{person['bio']}

## Mentioned In

> [!note] Conversations mentioning {person['name']} appear below via Obsidian backlinks.
"""
        safe = sanitize_filename(person["name"])
        filepath = VAULT / "People" / f"{safe}.md"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    print("Written people files.")

def write_topic_files():
    topics = [
        ("AI Engineering", "ai-engineering", "Career path chosen by Faizan — building AI-powered products and systems using LLMs, agents, RAG, and APIs. Maximum overlap with MERN background.", ["[[MERN Stack]]", "[[Python Learning]]", "[[DSA Learning]]", "[[Job Hunting]]"]),
        ("MERN Stack", "web-development", "MongoDB, Express.js, React, Node.js. Faizan's primary tech stack and job target. Core projects: [[Cine Circuit]] and [[StudyNotion]].", ["[[Cine Circuit]]", "[[StudyNotion]]", "[[AI Engineering]]", "[[Job Hunting]]"]),
        ("Resume Building", "job-hunting", "Faizan's iterative resume process — LaTeX/Overleaf, ATS optimization via Jobscan, JD-specific tailoring. Zensar (100% ATS score), Primis Digital, Sarvam AI, Cognizant GenC targeted.", ["[[LinkedIn Profile]]", "[[Job Hunting]]", "[[Faizan Khan]]"]),
        ("LinkedIn Profile", "job-hunting", "LinkedIn profile optimization work — About section, Experience, Projects, Featured, Certifications sections. Top pinned skills: React.js, Node.js, MongoDB.", ["[[Resume Building]]", "[[Job Hunting]]"]),
        ("Job Hunting", "career", "Active fresher job search targeting Full Stack Developer and AI Engineer roles in India. Companies: Zensar, Cognizant GenC, CloudSEK, Weave, Sarvam AI, Tech Mahindra, Primis Digital.", ["[[Resume Building]]", "[[LinkedIn Profile]]", "[[MERN Stack]]", "[[AI Engineering]]"]),
        ("DSA Learning", "programming", "Data Structures & Algorithms practice. JavaScript-first approach. Topics covered: loops, arrays, two pointers, brute force. LeetCode referenced.", ["[[Python Learning]]", "[[AI Engineering]]", "[[Technical Learning]]"]),
        ("Python Learning", "programming", "Python for AI engineering track. Completed Python Crash Course Chapters 2–9. Topics: variables, data types, operators, control flow, strings, lists, tuples.", ["[[DSA Learning]]", "[[AI Engineering]]", "[[Mathematics]]"]),
        ("Mathematics", "learning", "School-level math foundation for AI/ML. Working through Grades 6–10 systematically. Grade 6 Part 1 chapters: Geometry, Angles, Integers, Fractions, Decimals, Bar Graphs, Symmetry, Divisibility, HCF/LCM.", ["[[Python Learning]]", "[[AI Engineering]]", "[[ML Engineering]]"]),
        ("Ear Health", "health", "Ongoing ear health situation: infection, tinnitus, post-wisdom teeth surgery. ENT specialist [[Dr. Gaikwad]] treated. Audiogram showed improvement — left ear normalized, right mild.", ["[[Faizan Khan]]", "[[Dr. Gaikwad]]"]),
        ("Fitness Journey", "health", "Goal: reduce from ~88kg to 65–70kg. Gym access: treadmill, cycle, rowing machine, pull-up bar. Jawline improvement goals related to weight loss.", ["[[Faizan Khan]]"]),
        ("Islam & Faith", "personal", "Faizan's Islamic practice (Ahlul Hadith orientation). Faith integrated into personal decision-making.", ["[[Faizan Khan]]"]),
        ("ML Engineering", "ai-ml", "ML Engineer career path — working with models and algorithms, staying current with research. Compared against AI Engineer and Data Scientist paths.", ["[[AI Engineering]]", "[[Mathematics]]"]),
    ]

    for (title, category, desc, links) in topics:
        safe = sanitize_filename(title)
        links_str = "\n".join(f"- {l}" for l in links)
        content = f"""---
title: "{title}"
type: topic
category: {category}
tags:
  - topic
  - {category}
---

# {title}

{desc}

## Related

{links_str}

## Conversations

> [!note] All conversations tagged with this topic appear below via backlinks.
"""
        filepath = VAULT / "Topics" / f"{safe}.md"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    print("Written topic files.")

def write_moc_files():
    mocs = {
        "MOC - Career & Jobs": {
            "desc": "Map of Content for all career-related conversations, job applications, and professional development.",
            "sections": {
                "Job Hunting": ["[[Job Hunting]]", "[[Resume Building]]", "[[LinkedIn Profile]]"],
                "Target Companies": ["Zensar Technologies", "Cognizant GenC", "Sarvam AI", "CloudSEK", "Weave", "Primis Digital", "Tech Mahindra"],
                "Key Projects": ["[[Cine Circuit]]", "[[StudyNotion]]", "[[LinkVault]]"],
            }
        },
        "MOC - Technical Learning": {
            "desc": "Map of Content for programming, AI/ML, DSA, and web development learning.",
            "sections": {
                "Tracks": ["[[AI Engineering]]", "[[ML Engineering]]", "[[MERN Stack]]"],
                "Skills": ["[[Python Learning]]", "[[DSA Learning]]", "[[Mathematics]]"],
            }
        },
        "MOC - Health & Personal": {
            "desc": "Map of Content for health, fitness, personal life, and faith topics.",
            "sections": {
                "Health": ["[[Ear Health]]", "[[Fitness Journey]]"],
                "Personal": ["[[Islam & Faith]]"],
            }
        },
        "MOC - Projects": {
            "desc": "Map of Content for all development projects.",
            "sections": {
                "Production": ["[[Cine Circuit]]", "[[StudyNotion]]"],
                "Planned": ["[[LinkVault]]"],
            }
        },
    }

    for moc_title, moc_data in mocs.items():
        safe = sanitize_filename(moc_title)
        body = f"""---
title: "{moc_title}"
type: moc
tags:
  - moc
  - map-of-content
---

# {moc_title}

{moc_data['desc']}

"""
        for section, items in moc_data["sections"].items():
            body += f"## {section}\n\n"
            for item in items:
                body += f"- {item}\n"
            body += "\n"

        filepath = VAULT / "Maps of Content" / f"{safe}.md"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(body)
    print("Written MOC files.")

def write_home_file(conversations):
    total = len(conversations)
    date_range_start = min(c.get("created_at", "")[:10] for c in conversations if c.get("created_at"))
    date_range_end = max(c.get("created_at", "")[:10] for c in conversations if c.get("created_at"))

    content = f"""---
title: "🏠 Home"
type: home
tags:
  - home
  - index
---

# Faizan's Brain — Obsidian Vault

> Personal knowledge base built from {total} Claude conversations ({date_range_start} → {date_range_end}).

## Quick Links

- [[MOC - Career & Jobs]] — job hunting, resumes, LinkedIn
- [[MOC - Technical Learning]] — AI/ML, MERN, Python, DSA, Math
- [[MOC - Health & Personal]] — ear health, fitness, faith
- [[MOC - Projects]] — Cine Circuit, StudyNotion, LinkVault

## About Faizan

[[Faizan Khan]] — MCA student at Allama Institute of Management Sciences, Pune. Self-taught MERN developer targeting AI Engineering roles. BCA graduate (CGPA 8.10).

**Contacts:** fk3701@gmail.com | +91 90115 75978 | [LinkedIn](https://linkedin.com/in/faizan-fullstack) | [GitHub](https://github.com/Faizankhan17623)

## Core Projects

- [[Cine Circuit]] — Movie booking platform (79 REST endpoints, Razorpay, MongoDB)
- [[StudyNotion]] — EdTech LMS (Redux Toolkit, Cloudinary)
- [[LinkVault]] — Bookmark manager (planned)

## Active Learning Tracks

- [[AI Engineering]] — Primary career target
- [[MERN Stack]] — Current stack
- [[Python Learning]] — For AI track (Chapters 2–9 done)
- [[DSA Learning]] — JavaScript-first approach
- [[Mathematics]] — Grade 6–10 foundation for AI/ML

## Health Notes

- [[Ear Health]] — Tinnitus/infection recovery with [[Dr. Gaikwad]]
- [[Fitness Journey]] — 88kg → 65–70kg goal

## Vault Stats

| Metric | Value |
|--------|-------|
| Total Conversations | {total} |
| Date Range | {date_range_start} to {date_range_end} |
| Projects | 3 (2 production, 1 planned) |
| People | 2 |
| Topics | 12 |

---

*Generated on {datetime.now().strftime('%Y-%m-%d')} from Claude conversation export.*
"""
    filepath = VAULT / "🏠 Home.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Written Home file.")

def write_obsidian_config():
    config_dir = VAULT / ".obsidian"
    config_dir.mkdir(exist_ok=True)

    app_config = {
        "promptDelete": False,
        "trashOption": "system",
        "userIgnoreFilters": ["_attachments"],
        "attachmentFolderPath": "_attachments",
        "newFileLocation": "folder",
        "newFileFolderPath": "Conversations",
        "defaultViewMode": "source",
        "showInlineTitle": True,
        "showLineNumber": False,
        "strictLineBreaks": False,
    }

    graph_config = {
        "collapse-filter": False,
        "search": "",
        "showTags": True,
        "showAttachments": False,
        "hideUnresolved": False,
        "showOrphans": True,
        "collapse-color-groups": False,
        "colorGroups": [
            {"query": "tag:#projects", "color": {"a": 1, "rgb": 14701138}},
            {"query": "tag:#health", "color": {"a": 1, "rgb": 8388608}},
            {"query": "tag:#job-hunting", "color": {"a": 1, "rgb": 255165}},
            {"query": "tag:#mathematics", "color": {"a": 1, "rgb": 9699539}},
            {"query": "tag:#ai-engineering", "color": {"a": 1, "rgb": 3407871}},
        ],
        "collapse-display": False,
        "showArrow": True,
        "textFadeMultiplier": 0,
        "nodeSizeMultiplier": 1.2,
        "lineSizeMultiplier": 1,
        "collapse-forces": False,
        "centerStrength": 0.518713248970312,
        "repelStrength": 10,
        "linkStrength": 1,
        "linkDistance": 30,
        "scale": 1,
        "close": False,
    }

    with open(config_dir / "app.json", "w") as f:
        json.dump(app_config, f, indent=2)

    with open(config_dir / "graph.json", "w") as f:
        json.dump(graph_config, f, indent=2)

    print("Written Obsidian config.")

def main():
    print("=" * 60)
    print("Building Obsidian Vault from Claude Conversations")
    print("=" * 60)

    with open(VAULT / "conversations.json", "r", encoding="utf-8") as f:
        conversations = json.load(f)

    print(f"Loaded {len(conversations)} conversations.")

    create_vault_structure()
    write_obsidian_config()
    write_conversations(conversations)
    write_project_files()
    write_people_files()
    write_topic_files()
    write_moc_files()
    write_home_file(conversations)

    print()
    print("=" * 60)
    print("Vault build complete!")
    print(f"  {len(conversations)} conversation files")
    print("  3 project files")
    print("  2 people files")
    print("  12 topic files")
    print("  4 MOC files")
    print("  1 Home file")
    print("=" * 60)

if __name__ == "__main__":
    main()
