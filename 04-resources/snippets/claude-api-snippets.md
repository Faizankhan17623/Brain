---
title: "Claude API Snippets"
date: 2026-04-27
type: resource
status: active
tags:
  - claude
  - anthropic
  - ai-engineering
  - snippets
---

# Claude API Snippets

Patterns for building with the Anthropic Claude API. Faizan holds certifications in Claude Code, Claude API, and MCP.

---

## Basic Message

```python
import anthropic

client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY from env

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude!"}]
)
print(message.content[0].text)
```

---

## Streaming Response

```python
with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Write a poem about Pune."}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

---

## System Prompt

```python
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="You are a helpful MERN stack mentor. Give concise, practical answers.",
    messages=[{"role": "user", "content": "Explain useEffect cleanup."}]
)
```

---

## Multi-turn Conversation

```python
conversation = []

def chat(user_message):
    conversation.append({"role": "user", "content": user_message})
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=conversation
    )
    assistant_message = response.content[0].text
    conversation.append({"role": "assistant", "content": assistant_message})
    return assistant_message
```

---

## Tool Use (Function Calling)

```python
tools = [{
    "name": "get_weather",
    "description": "Get current weather for a city",
    "input_schema": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "City name"}
        },
        "required": ["city"]
    }
}]

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in Pune?"}]
)

if response.stop_reason == "tool_use":
    tool_call = next(b for b in response.content if b.type == "tool_use")
    print(f"Tool: {tool_call.name}, Input: {tool_call.input}")
```

---

## Prompt Caching (cost reduction)

```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=[{
        "type": "text",
        "text": "You are an expert MERN stack assistant. " + long_context_here,
        "cache_control": {"type": "ephemeral"}  # cache this prefix
    }],
    messages=[{"role": "user", "content": "How do I handle CORS?"}]
)
```

---

## Node.js / JavaScript Version

```javascript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic(); // ANTHROPIC_API_KEY from env

const message = await client.messages.create({
  model: 'claude-sonnet-4-6',
  max_tokens: 1024,
  messages: [{ role: 'user', content: 'Hello from Node.js!' }]
});

console.log(message.content[0].text);
```

---

## Model Reference

| Model | ID | Best For |
|-------|----|---------|
| Sonnet 4.6 | `claude-sonnet-4-6` | Balanced — daily use |
| Opus 4.7 | `claude-opus-4-7` | Complex reasoning |
| Haiku 4.5 | `claude-haiku-4-5-20251001` | Fast, cheap, simple tasks |

---

*Last updated: 2026-04-27 | Back to [[snippets/README]]*
