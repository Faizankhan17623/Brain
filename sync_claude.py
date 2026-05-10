"""
sync_claude.py — Fetches new claude.ai conversations and drops them into 00-inbox/

How it works:
1. Calls claude.ai's internal API using your session cookie
2. Compares against already-synced UUIDs (stored in sync_state.json)
3. Saves each NEW conversation as a markdown file in 00-inbox/
4. Run this script every hour via Windows Task Scheduler

Setup:
1. Get your sessionKey cookie from claude.ai (F12 → Application → Cookies)
2. Paste it in SESSION_KEY below (or set env var CLAUDE_SESSION_KEY)
3. Run: python sync_claude.py
"""

import json
import os
import re
import requests
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# ─── CONFIG ───────────────────────────────────────────────────────────────────

VAULT       = Path("C:/Users/fk241/OneDrive/Desktop/Brain")
INBOX_DIR   = VAULT / "00-inbox"
STATE_FILE  = VAULT / "sync_state.json"   # tracks which UUIDs are already synced

# Load .env from vault root
load_dotenv(VAULT / ".env")
SESSION_KEY = os.environ.get("CLAUDE_SESSION_KEY", "")

# claude.ai internal API endpoints
BASE_URL         = "https://claude.ai"
CONVERSATIONS_URL = f"{BASE_URL}/api/organizations/{{org_id}}/chat_conversations?limit=50"
MESSAGES_URL      = f"{BASE_URL}/api/organizations/{{org_id}}/chat_conversations/{{conv_id}}"

# ─── HELPERS ──────────────────────────────────────────────────────────────────

def get_headers():
    return {
        "Cookie": f"sessionKey={SESSION_KEY}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://claude.ai/chats",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

def get_org_id(session: requests.Session) -> str:
    """Fetch the user's organization ID — required for all API calls."""
    resp = session.get(f"{BASE_URL}/api/organizations", headers=get_headers())
    resp.raise_for_status()
    orgs = resp.json()
    if not orgs:
        raise ValueError("No organizations found. Check your session key.")
    return orgs[0]["uuid"]

def load_state() -> set:
    """Return set of already-synced conversation UUIDs."""
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return set(data.get("synced_uuids", []))
    return set()

def save_state(synced_uuids: set):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump({"synced_uuids": sorted(synced_uuids)}, f, indent=2)

def sanitize_filename(name: str) -> str:
    name = re.sub(r'[\\/*?:"<>|]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name[:80] if name else "Untitled"

# ─── CONVERSATION FETCHER ─────────────────────────────────────────────────────

def fetch_all_conversations(session: requests.Session, org_id: str) -> list:
    """Fetch conversation list (no messages yet — just metadata)."""
    url = CONVERSATIONS_URL.format(org_id=org_id)
    resp = session.get(url, headers=get_headers())
    resp.raise_for_status()
    return resp.json()

def fetch_conversation_messages(session: requests.Session, org_id: str, conv_id: str) -> dict:
    """Fetch full conversation with all messages."""
    url = MESSAGES_URL.format(org_id=org_id, conv_id=conv_id)
    resp = session.get(url, headers=get_headers())
    resp.raise_for_status()
    return resp.json()

# ─── MARKDOWN FORMATTER ───────────────────────────────────────────────────────

def format_message(msg: dict) -> str:
    role = msg.get("sender", msg.get("role", "unknown"))
    sender = "**Faizan**" if role == "human" else "**Claude**"

    # Handle different content structures
    text = msg.get("text", "").strip()
    if not text:
        content = msg.get("content", [])
        if isinstance(content, list):
            text = " ".join(
                c.get("text", "") for c in content
                if isinstance(c, dict) and c.get("type") == "text"
            ).strip()
        elif isinstance(content, str):
            text = content.strip()

    if not text:
        return ""

    ts = msg.get("created_at", "")[:16].replace("T", " ")
    return f"{sender} `{ts}`\n\n{text}\n\n---\n"

def build_inbox_md(conv: dict) -> str:
    uuid    = conv.get("uuid", "")
    name    = conv.get("name", "").strip() or "Untitled Conversation"
    created = conv.get("created_at", "")
    updated = conv.get("updated_at", "")
    messages = conv.get("chat_messages", [])

    created_date = created[:10] if created else datetime.now().strftime("%Y-%m-%d")
    created_full = created[:19].replace("T", " ") if created else ""
    updated_full = updated[:19].replace("T", " ") if updated else ""

    frontmatter = f"""---
title: "{name.replace('"', "'")}"
date: {created_date}
created: {created_full}
updated: {updated_full}
uuid: {uuid}
type: inbox
status: active
source: "claude.ai sync"
tags:
  - inbox
  - needs-ingest
---
"""

    body = f"# {name}\n\n"
    body += f"> Synced from claude.ai on {datetime.now().strftime('%Y-%m-%d %H:%M')}. Run `/inbox` to ingest this into the vault.\n\n"
    body += "## Conversation\n\n"

    for msg in messages:
        formatted = format_message(msg)
        if formatted:
            body += formatted

    return frontmatter + body

# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    if not SESSION_KEY or SESSION_KEY == "PASTE_YOUR_SESSION_KEY_HERE":
        print("ERROR: Set your SESSION_KEY in sync_claude.py or via CLAUDE_SESSION_KEY env var.")
        return

    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    synced = load_state()

    session = requests.Session()

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Fetching conversations from claude.ai...")

    try:
        org_id = get_org_id(session)
        print(f"  Org ID: {org_id}")
    except Exception as e:
        print(f"ERROR getting org ID: {e}")
        print("  Check your session key — it may have expired.")
        return

    try:
        conversations = fetch_all_conversations(session, org_id)
        print(f"  Found {len(conversations)} conversations total.")
    except Exception as e:
        print(f"ERROR fetching conversations: {e}")
        return

    new_count = 0
    for conv in conversations:
        uuid = conv.get("uuid", "")
        if not uuid or uuid in synced:
            continue

        name = conv.get("name", "").strip() or "Untitled"
        print(f"  New conversation: {name[:60]}")

        # Fetch full messages
        try:
            full_conv = fetch_conversation_messages(session, org_id, uuid)
        except Exception as e:
            print(f"    ERROR fetching messages for {uuid}: {e}")
            continue

        # Write to 00-inbox/
        safe_name = sanitize_filename(name)
        date_prefix = (conv.get("created_at", "")[:10] or datetime.now().strftime("%Y-%m-%d"))
        filename = f"{date_prefix} - {safe_name}.md"
        filepath = INBOX_DIR / filename

        # Avoid overwriting if filename collision
        counter = 1
        while filepath.exists():
            filename = f"{date_prefix} - {safe_name} ({counter}).md"
            filepath = INBOX_DIR / filename
            counter += 1

        content = build_inbox_md(full_conv)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        synced.add(uuid)
        new_count += 1
        print(f"    Saved to 00-inbox/{filename}")

    save_state(synced)

    if new_count == 0:
        print("  No new conversations. Vault is up to date.")
    else:
        print(f"\nDone! {new_count} new conversation(s) saved to 00-inbox/")
        print("Run /inbox in Claude Code to ingest them into the vault.")

if __name__ == "__main__":
    main()
