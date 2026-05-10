"""
Obsidian Vault Builder v2 — Improved tagging using message-only analysis.
Key fix: only analyze actual message text, NOT the AI-generated summary.
Also creates Companies/ and Places/ hub files.
"""

import json
import re
from datetime import datetime
from pathlib import Path

VAULT = Path("C:/Users/fk241/OneDrive/Desktop/Brain")

# ─── Tag rules — keywords must appear in ACTUAL message text only ────────────
TAG_RULES = [
    (["ai engineer", "agentic ai", "llm", "rag ", " rag,", "anthropic api", "claude api",
      "claude code", "openai", "langchain", "hugging face", "vector db", "embedding",
      "coding agent", "ai agent", "ai roadmap", "generative ai"],
     ["ai-engineering"]),
    (["ml engineer", "machine learning", "neural network", "deep learning", "scikit",
      "tensorflow", "pytorch", "data scientist"],
     ["ml-engineering"]),
    (["mern", " react", "node.js", "nodejs", "mongodb", "express.js", "expressjs",
      "mongoose", "redux", "tailwind", "next.js", "nextjs"],
     ["mern-stack"]),
    (["html", "css", "javascript", "typescript", " jsx", " tsx", "ui component",
      "tailwind", "bootstrap", "frontend", "front-end"],
     ["frontend"]),
    (["node", "express", "server", "middleware", "jwt", "backend", "back-end",
      "api endpoint", "rest api", "restful", "route handler", "controller", "mongoose"],
     ["backend"]),
    (["python", "pip install", "venv", "jupyter", "pandas", "numpy", ".py"],
     ["python"]),
    (["dsa", "data structure", "algorithm", "two pointer", "brute force", "leetcode",
      "binary search", "linked list", "stack", "queue", "tree", "graph traversal",
      "dynamic programming", "sliding window"],
     ["dsa"]),
    (["fraction", "integer", "geometry", "algebra", "decimal", "equation",
      "hcf", "lcm", "math", "percentage", "compound interest", "divisibility",
      "bar graph", "symmetry", "arithmetic", "grade 6", "grade 7", "grade 8",
      "grade 9", "grade 10", "standard 5", "standard 6"],
     ["mathematics"]),
    (["resume", " cv ", "ats score", "jobscan", "latex", "overleaf", "ats optimization",
      "resume template", "fresher resume"],
     ["resume"]),
    (["linkedin", "linkedin profile", "linkedin optimization", "linkedin url",
      "linkedin bio", "linkedin connections"],
     ["linkedin"]),
    (["job ", "fresher ", "interview ", "apply ", "hiring", "placement", "job description",
      "jd ", "off-campus", "campus drive", "job hunt", "job search", "job portal",
      "naukri", "indeed", "internship"],
     ["job-hunting"]),
    (["career path", "career choice", "career track", "career advice", "career goal",
      "roadmap", "learning plan", "18-month", "6-month", "phase 1", "phase 2"],
     ["career", "planning"]),
    (["mysql", "sql query", "database", "nosql", "collection", "schema", "aggregate",
      "indexing", "transaction"],
     ["database"]),
    (["git ", "github", "repository", "git commit", "git push", "git pull",
      "branch", "merge conflict", "pull request"],
     ["git"]),
    (["cybersecurity", "ethical hack", "hacking", "penetration test", "oscp",
      "metasploit", "nmap", "burp suite", "ctf", "vulnerability", "exploit",
      "unauthorized access", "hacker"],
     ["cybersecurity"]),
    (["java ", "jvm", "spring boot", "collection framework", "oops in java",
      "java practical", "mca exam", " oose ", "uml diagram", "java thread",
      "oose exam", "object oriented software"],
     ["education", "java"]),
    (["college", "mca ", "bca ", "semester", "exam", "allana", "poona college",
      "university", "practicals"],
     ["education", "college"]),
    (["fitness", "gym", "workout", "exercise", "weight loss", "fat", "jawline",
      "face structure", "round face", "stamina", "cardio", "treadmill", "rowing"],
     ["fitness", "health"]),
    (["ear ", "tinnitus", "audiogram", "hearing", "ent ", "ear infection", "ear cold",
      "ear wax", "wisdom teeth", "dr. gaikwad", "gaikwad"],
     ["health"]),
    (["head shape", "asymmetry", "cranial", "skull", "plagiocephaly"],
     ["health", "personal"]),
    (["islam", "prayer", "quran", "hadith", "muslim", "religion", "halal", "haram",
      "namaz", "salah", "ahlul", "prophet", "palestine", "free palestine", "al-aqsa"],
     ["islam", "personal"]),
    (["marriage", "rishta", "proposal", "relationship", "nikah", "wife", "husband"],
     ["personal"]),
    (["instagram", "social media", "bio", "post", "story", "reel", "twitter", "x.com"],
     ["personal", "social-media"]),
    (["payment", "upi", "phonepe", "gpay", "paytm", "bhim", "neft", "money transfer",
      "bank account", "contact details hidden", "pay unknown"],
     ["personal"]),
    (["astrology", "horoscope", "zodiac", "kundli", "birth chart", "planetary"],
     ["personal", "astrology"]),
    (["masturbat", "ejaculat", "sexual", "intimacy", "libido"],
     ["personal", "health"]),
    (["remote control", "laptop control", "mobile access", "teamviewer", "anydesk",
      "unauthorized access", "keylogger", "hacked"],
     ["cybersecurity", "personal"]),
    (["wifi", "airtel", "internet", "router", "password change", "device disconnect"],
     ["personal"]),
    (["cine circuit", "movie booking", "theatre owner", "ticket allot", "ticket lifecycle",
      "cinema booking", "razorpay", "show schedule", "seat allot"],
     ["projects", "project-cine-circuit"]),
    (["studynotion", "edtech", "lms ", "learning management"],
     ["projects", "project-studynotion"]),
    (["linkvault", "bookmark manager", "bookmark app"],
     ["projects", "project-linkvault"]),
    (["programming", "code", "debug", "function", "class", "variable", "bug ",
      "error ", "npm ", "package", "import ", "module"],
     ["programming"]),
    (["learn", "study", "course", "tutorial", "chapter", "textbook"],
     ["learning"]),
]

CATEGORY_MAP = {
    "career":         ["job ", "resume", "ats", "linkedin", "interview", "hiring", "fresher", "placement", "career path"],
    "technical-learning": ["python", "dsa", "algorithm", "data structure", "leetcode", "programming", "debug"],
    "mathematics":    ["fraction", "integer", "geometry", "decimal", "algebra", "hcf", "lcm", "math", "bar graph"],
    "ai-ml":          ["ai engineer", "ml engineer", "machine learning", "llm", "ollama", "agentic"],
    "web-development":["mern", " react", " node", "mongodb", "express", "css", "html", "javascript", "frontend", "backend"],
    "projects":       ["cine circuit", "studynotion", "linkvault", "ticket", "razorpay", "booking"],
    "health":         ["ear ", "tinnitus", "hearing", "fitness", "weight", "gym", "jawline", "audiogram", "doctor", "head shape"],
    "personal":       ["islam", "marriage", "rishta", "prayer", "religion", "instagram", "astrology", "payment", "upi", "wifi"],
    "education":      ["college", "mca ", "bca ", "semester", "exam", "java practical"],
    "cybersecurity":  ["ethical hack", "hacking", "cybersecurity", "security", "unauthorized"],
    "general":        [],
}

# ─── Entity detection — applied to messages only ─────────────────────────────

def detect_people(msg_text):
    people_raw, people_links = ["Faizan Khan"], ["[[Faizan Khan]]"]
    if any(x in msg_text for x in ["gaikwad", "dr. gaikwad", "audiogram", "tinnitus", "ent specialist"]):
        people_raw.append("Dr. Gaikwad")
        people_links.append("[[Dr. Gaikwad]]")
    return people_raw, people_links

def detect_projects(msg_text):
    projects = []
    if any(x in msg_text for x in ["cine circuit", "movie booking", "theatre owner",
                                     "ticket allot", "cinema booking", "razorpay", "show schedule"]):
        projects.append("[[Cine Circuit]]")
    if any(x in msg_text for x in ["studynotion", "edtech", "lms ", "learning management"]):
        projects.append("[[StudyNotion]]")
    if any(x in msg_text for x in ["linkvault", "bookmark manager", "bookmark app"]):
        projects.append("[[LinkVault]]")
    return projects

def detect_companies(msg_text):
    companies = []
    if "zensar" in msg_text:
        companies.append("[[Zensar Technologies]]")
    if "cognizant" in msg_text:
        companies.append("[[Cognizant GenC]]")
    if "cloudsek" in msg_text:
        companies.append("[[CloudSEK]]")
    if "sarvam" in msg_text:
        companies.append("[[Sarvam AI]]")
    if "tech mahindra" in msg_text or "techm" in msg_text:
        companies.append("[[Tech Mahindra]]")
    if "primis" in msg_text:
        companies.append("[[Primis Digital]]")
    if "weave" in msg_text and ("job" in msg_text or "company" in msg_text or "apply" in msg_text):
        companies.append("[[Weave]]")
    if "anthropic" in msg_text:
        companies.append("[[Anthropic]]")
    return list(dict.fromkeys(companies))

def detect_places(msg_text):
    places = []
    if "pune" in msg_text:
        places.append("[[Pune]]")
    if " india" in msg_text or "india." in msg_text or "india," in msg_text or "indian " in msg_text:
        places.append("[[India]]")
    if "palestine" in msg_text or "al-aqsa" in msg_text or "gaza" in msg_text:
        places.append("[[Palestine]]")
    return list(dict.fromkeys(places))

def detect_schools(msg_text):
    schools = []
    if "allana" in msg_text or "allama" in msg_text:
        schools.append("[[Allana Institute]]")
    if "poona college" in msg_text:
        schools.append("[[Poona College]]")
    return schools

def detect_topics(tags, msg_text):
    topics = []
    if "ai-engineering" in tags:
        topics.append("[[AI Engineering]]")
    if "ml-engineering" in tags:
        topics.append("[[ML Engineering]]")
    if "mern-stack" in tags:
        topics.append("[[MERN Stack]]")
    if "resume" in tags:
        topics.append("[[Resume Building]]")
    if "linkedin" in tags:
        topics.append("[[LinkedIn Profile]]")
    if "job-hunting" in tags:
        topics.append("[[Job Hunting]]")
    if "dsa" in tags:
        topics.append("[[DSA Learning]]")
    if "python" in tags:
        topics.append("[[Python Learning]]")
    if "mathematics" in tags:
        topics.append("[[Mathematics]]")
    if "health" in tags and any(x in msg_text for x in ["ear ", "tinnitus", "audiogram", "gaikwad", "ear cold", "ear wax"]):
        topics.append("[[Ear Health]]")
    if "fitness" in tags:
        topics.append("[[Fitness Journey]]")
    if "islam" in tags:
        topics.append("[[Islam & Faith]]")
    return list(dict.fromkeys(topics))

# ─── Core helpers ─────────────────────────────────────────────────────────────

def infer_tags(msg_text):
    tags = set()
    for keywords, tag_list in TAG_RULES:
        if any(kw in msg_text for kw in keywords):
            tags.update(tag_list)
    return sorted(tags)

def infer_category(msg_text):
    scores = {}
    for cat, keywords in CATEGORY_MAP.items():
        if not keywords:
            continue
        score = sum(1 for kw in keywords if kw in msg_text)
        if score > 0:
            scores[cat] = score
    return max(scores, key=scores.get) if scores else "general"

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name[:100] if name else "Untitled"

def get_messages_text(messages, human_only=False):
    """Extract text from messages. human_only=True uses only Faizan's messages for tagging
    to avoid false positives from Claude's verbose responses mentioning tangential topics."""
    texts = []
    for msg in messages:
        if human_only and msg.get("sender") != "human":
            continue
        text = msg.get("text", "").strip()
        if not text:
            content = msg.get("content", [])
            if content:
                text = " ".join(
                    c.get("text", "") for c in content if isinstance(c, dict)
                ).strip()
        if text:
            texts.append(text)
    return " ".join(texts)

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

# ─── Build single conversation markdown ───────────────────────────────────────

def build_conversation_md(conv, index):
    uuid    = conv.get("uuid", "")
    name    = conv.get("name", "").strip() or "Untitled Conversation"
    summary = conv.get("summary", "").strip()
    created = conv.get("created_at", "")
    updated = conv.get("updated_at", "")
    messages = conv.get("chat_messages", [])

    created_date = created[:10] if created else "unknown"
    created_full = created[:19].replace("T", " ") if created else ""
    updated_full = updated[:19].replace("T", " ") if updated else ""

    # ── Analyze ONLY Faizan's own messages for tags (avoids false positives
    #    from Claude's verbose responses mentioning tangential topics)
    #    Use all messages for entity detection (companies/places/people).
    human_text = get_messages_text(messages, human_only=True).lower()
    msg_text   = get_messages_text(messages, human_only=False).lower()

    tags          = infer_tags(human_text)    # human messages only → precise tags
    category      = infer_category(human_text)
    people_raw, people_links = detect_people(msg_text)   # all messages for entities
    project_links = detect_projects(msg_text)
    company_links = detect_companies(msg_text)
    place_links   = detect_places(msg_text)
    school_links  = detect_schools(msg_text)
    topic_links   = detect_topics(tags, msg_text)

    # ── Frontmatter ──
    tags_yaml    = "\n".join(f"  - {t}" for t in tags) if tags else "  - general"
    people_yaml  = "\n".join(f'  - "{p}"' for p in people_raw)
    proj_yaml    = ("\nprojects:\n" + "\n".join(f'  - "{p.strip("[]")}"' for p in project_links)) if project_links else ""
    topics_yaml  = ("\nrelated_topics:\n" + "\n".join(f'  - "{t.strip("[]")}"' for t in topic_links)) if topic_links else ""

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
{people_yaml}{proj_yaml}{topics_yaml}
---
"""

    # ── Connections body ──
    body = f"# {name}\n\n"
    has_connections = (topic_links or project_links or len(people_links) > 1
                       or company_links or place_links or school_links)
    if has_connections:
        body += "## Connections\n"
        body += "**People:** " + " · ".join(people_links) + "\n\n"
        if project_links:
            body += "**Projects:** " + " · ".join(project_links) + "\n\n"
        if topic_links:
            body += "**Topics:** " + " · ".join(topic_links) + "\n\n"
        if company_links:
            body += "**Companies:** " + " · ".join(company_links) + "\n\n"
        if place_links:
            body += "**Places:** " + " · ".join(place_links) + "\n\n"
        if school_links:
            body += "**Schools:** " + " · ".join(school_links) + "\n\n"
    else:
        body += "## Connections\n**People:** [[Faizan Khan]]\n\n"

    if summary:
        body += f"## Summary\n\n{summary}\n\n"

    if messages:
        body += "## Conversation\n\n"
        for msg in messages:
            formatted = format_message(msg)
            if formatted:
                body += formatted

    return frontmatter + body

# ─── Hub file writers ──────────────────────────────────────────────────────────

def write_company_files():
    companies = [
        ("Zensar Technologies", "employer-target", "IT services company. Faizan applied for Job ID 142126 with a tailored LaTeX resume that achieved 100% ATS score on Jobscan.", ["[[Job Hunting]]", "[[Resume Building]]"]),
        ("Cognizant GenC", "employer-target", "Cognizant's fresher hiring program (GenC track). Faizan targeted this with a March 2026 deadline.", ["[[Job Hunting]]", "[[Resume Building]]"]),
        ("Sarvam AI", "employer-target", "Indian AI startup. Faizan identified Frontend Engineer Intern — Arya Team as a strong fit for his profile.", ["[[Job Hunting]]", "[[AI Engineering]]"]),
        ("CloudSEK", "employer-target", "Cybersecurity company. One of Faizan's targeted employers for fresher roles.", ["[[Job Hunting]]"]),
        ("Tech Mahindra", "employer-target", "IT services company. Faizan applied for Associate Software Engineer off-campus drive.", ["[[Job Hunting]]", "[[Resume Building]]"]),
        ("Primis Digital", "employer-target", "Digital company offering Jr. Python Full Stack Developer role — identified as a viable fresher target.", ["[[Job Hunting]]", "[[Python Learning]]"]),
        ("Weave", "employer-target", "Tech company targeted by Faizan in his fresher job hunt.", ["[[Job Hunting]]"]),
        ("Anthropic", "ai-company", "AI safety company that makes Claude. Faizan has Anthropic Academy certifications: Claude Code in Action, Building with Claude API, MCP Introduction.", ["[[AI Engineering]]"]),
    ]

    comp_dir = VAULT / "Companies"
    comp_dir.mkdir(exist_ok=True)

    for name, category, desc, links in companies:
        tags_yaml = f"  - company\n  - {category}"
        links_str = "\n".join(f"- {l}" for l in links)
        content = f"""---
title: "{name}"
type: company
category: {category}
tags:
{tags_yaml}
---

# {name}

{desc}

## Related

{links_str}
- [[Faizan Khan]]

## Conversations

> [!note] Conversations mentioning {name} appear below via backlinks.
"""
        filepath = comp_dir / f"{sanitize_filename(name)}.md"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    print(f"Written {len(companies)} company files.")

def write_place_files():
    places = [
        ("Pune", "city", "Maharashtra, India", "City in Maharashtra, India. Faizan's home base. Location of [[Allana Institute]] (MCA 2025–2027) and [[Poona College]] (BCA, CGPA 8.10).", ["[[India]]", "[[Allana Institute]]", "[[Poona College]]", "[[Faizan Khan]]"]),
        ("India", "country", "South Asia", "Country. Faizan's primary job market for fresher Full Stack Developer and AI Engineering roles.", ["[[Pune]]", "[[Job Hunting]]", "[[Faizan Khan]]"]),
        ("Palestine", "territory", "Middle East", "Referenced in Faizan's conversations in the context of Islamic solidarity and current events.", ["[[Islam & Faith]]", "[[Faizan Khan]]"]),
    ]

    places_dir = VAULT / "Places"
    places_dir.mkdir(exist_ok=True)

    for name, ptype, region, desc, links in places:
        links_str = "\n".join(f"- {l}" for l in links)
        content = f"""---
title: "{name}"
type: place
place_type: {ptype}
region: "{region}"
tags:
  - place
  - {ptype}
---

# {name}

{desc}

## Related

{links_str}

## Conversations

> [!note] Conversations mentioning {name} appear below via backlinks.
"""
        filepath = places_dir / f"{sanitize_filename(name)}.md"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    print(f"Written {len(places)} place files.")

def write_school_files():
    schools_dir = VAULT / "Schools"
    schools_dir.mkdir(exist_ok=True)

    schools = [
        ("Allana Institute", "Allana Institute of Management Sciences, Pune. Faizan is enrolled in the MCA program (2025–2027).", "mca", ["[[Pune]]", "[[Faizan Khan]]"]),
        ("Poona College", "Poona College of Arts, Science and Commerce, Pune. Faizan completed his BCA here with CGPA 8.10.", "bca", ["[[Pune]]", "[[Faizan Khan]]"]),
    ]

    for name, desc, degree, links in schools:
        links_str = "\n".join(f"- {l}" for l in links)
        content = f"""---
title: "{name}"
type: school
degree: {degree}
tags:
  - school
  - education
  - pune
---

# {name}

{desc}

## Related

{links_str}

## Conversations

> [!note] Conversations mentioning {name} appear below via backlinks.
"""
        filepath = schools_dir / f"{sanitize_filename(name)}.md"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    print(f"Written {len(schools)} school files.")

def update_home_file(conversations):
    total = len(conversations)
    date_range_start = min(c.get("created_at", "")[:10] for c in conversations if c.get("created_at"))
    date_range_end   = max(c.get("created_at", "")[:10] for c in conversations if c.get("created_at"))

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

[[Faizan Khan]] — MCA student at [[Allana Institute]], [[Pune]]. Self-taught MERN developer targeting AI Engineering roles. BCA from [[Poona College]] (CGPA 8.10).

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

## Companies Targeted

- [[Zensar Technologies]] — Job ID 142126, 100% ATS on Jobscan
- [[Cognizant GenC]] — March 2026 deadline
- [[Sarvam AI]] — Frontend Intern, Arya Team
- [[CloudSEK]] — Cybersecurity fresher role
- [[Tech Mahindra]] — Associate Software Engineer off-campus
- [[Primis Digital]] — Jr. Python Full Stack Developer
- [[Anthropic]] — Certifications: Claude Code, Claude API, MCP

## Health & Personal

- [[Ear Health]] — Tinnitus/infection recovery with [[Dr. Gaikwad]]
- [[Fitness Journey]] — 88kg → 65–70kg goal
- [[Islam & Faith]] — Ahlul Hadith orientation

## Places

- [[Pune]] — Home city, [[India]]

## Vault Stats

| Metric | Value |
|--------|-------|
| Total Conversations | {total} |
| Date Range | {date_range_start} to {date_range_end} |
| Projects | 3 (2 production, 1 planned) |
| People | 2 |
| Topics | 12 |
| Companies | 8 |
| Places | 3 |

---

*Rebuilt on {datetime.now().strftime('%Y-%m-%d')} with v2 smart tagging (message-only analysis).*
"""
    filepath = VAULT / "🏠 Home.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated Home file.")

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Building Obsidian Vault v2 — Smart Tagging")
    print("=" * 60)

    with open(VAULT / "conversations.json", "r", encoding="utf-8") as f:
        conversations = json.load(f)
    print(f"Loaded {len(conversations)} conversations.")

    # Ensure directories exist
    for d in ["Conversations", "Projects", "People", "Topics",
              "Maps of Content", "_attachments", "Companies", "Places", "Schools"]:
        (VAULT / d).mkdir(parents=True, exist_ok=True)

    # Rebuild all conversation files
    conv_dir = VAULT / "Conversations"
    written = 0
    for i, conv in enumerate(conversations, 1):
        name = conv.get("name", "").strip() or "Untitled"
        safe_name = sanitize_filename(name)
        filename = f"{str(i).zfill(3)} - {safe_name}.md"
        content = build_conversation_md(conv, i)
        with open(conv_dir / filename, "w", encoding="utf-8") as f:
            f.write(content)
        written += 1
        if written % 20 == 0:
            print(f"  Written {written}/{len(conversations)} conversations...")

    print(f"Done: {written} conversation files rebuilt.")

    write_company_files()
    write_place_files()
    write_school_files()
    update_home_file(conversations)

    print()
    print("=" * 60)
    print("Vault v2 build complete!")
    print(f"  {written} conversation files (smart-tagged, message-only analysis)")
    print("  8 company files")
    print("  3 place files")
    print("  2 school files")
    print("  Updated Home file")
    print("=" * 60)

if __name__ == "__main__":
    main()
