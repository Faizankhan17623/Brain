---
title: "Changing models in Ollama with Claude"
date: 2026-04-14
created: 2026-04-14 16:09:34
updated: 2026-04-14 16:56:35
uuid: b58cf360-90a4-4e70-b0f4-51bbaf7adf85
category: ai-ml
message_count: 8
tags:
  - ai-engineering
  - programming
people:
  - "Faizan Khan"
related_topics:
  - "AI Engineering"
---
# Changing models in Ollama with Claude

## Connections
**People:** [[Faizan Khan]]

**Topics:** [[AI Engineering]]

**Companies:** [[Anthropic]]

## Conversation

**Faizan** `2026-04-14 16:09`

hye i have installed ollam and thre iw nat to use claude code but there alos i wnat to use some specific model so how do i chagne it tell me

---
**Claude** `2026-04-14 16:10`

The user wants to know how to use Claude Code with Ollama and change the model. Let me think about this.

Claude Code supports using custom models via the ANTHROPIC_BASE_URL environment variable or by configuring it to use Ollama's OpenAI-compatible API. Let me think about what I know here.

Claude Code can be configured to use different models. For Ollama specifically, since Ollama has an OpenAI-compatible API, you can point Claude Code to use it.

Let me check the skill for product self-knowledge since this involves Claude Code specifics.

Actually, I know the basics here. Claude Code uses the Anthropic API by default, but you can configure it to use other providers. For Ollama:


Ollama runs locally on port 11434 with an OpenAI-compatible endpoint, so I'd need to configure Claude Code to point there using environment variables or a model flag, though I should verify the exact configuration approach since Ollama's API differs from Anthropic's.
```
This block is not supported on your current device yet.
```

Let me check the Claude Code docs map to find info about using custom models / Ollama.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now I have a clear picture. Let me summarize the two main ways to use Claude Code with Ollama and change the model.Bhai got it, yeh thoda naya feature hai (January 2026 mein aaya) — Ollama ab Anthropic Messages API support karta hai, so Claude Code directly Ollama models ke saath kaam karta hai. Do easy ways hain:

---

## Method 1 — `ollama launch` command (Easiest)

Ollama ke through Claude Code directly launch kar sakte ho aur model specify kar sakte ho:

```bash
ollama launch claude --model qwen3-coder
# ya
ollama launch claude --model glm-4.7-flash
# ya koi bhi model jo tune pull kiya ho
ollama launch claude --model llama3
```

Agar model specify nahi kiya toh ek model selection menu aayega jahan arrow keys se choose kar sakte ho.

---

## Method 2 — Environment Variables set karo (Manual, More Control)

Yeh 3 env vars set karo:

```bash
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL="http://localhost:11434"
```

Phir model flag ke saath Claude Code run karo:

```bash
claude --model glm-4.7-flash
```

Permanent karna hai toh `.bashrc` ya `.zshrc` mein add kar do woh lines.

---

## Method 3 — `settings.json` mein default model set karo

Claude Code ke settings.json mein yeh config add karo default model permanently set karne ke liye:

```json
{
  "model": "qwen3-coder:30b",
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "ollama",
    "ANTHROPIC_API_KEY": "",
    "ANTHROPIC_BASE_URL": "http://localhost:11434"
  }
}
```

---

## Model Choice (Tera System ke liye)

Tera Acer Nitro V hai — GPU hai toh decent performance milega. Tool-calling aur 128K context ke liye `glm-4.7-flash` best recommend hai locally. Agar general coding chahiye toh `qwen3-coder` bhi solid option hai.

```bash
ollama pull glm-4.7-flash   # Tool calling support + 128K context
# ya
ollama pull qwen3-coder     # Good for general coding
```

> **Note:** At least 32K token context wala model use karna recommended hai Claude Code ke saath.

---
**Faizan** `2026-04-14 16:53`

`.bashrc` ya `.zshrc` m ya two files kaha find karu adn like i do not know by defautl where i have installed the claude code so how to find that also tel lme

---
**Claude** `2026-04-14 16:54`

The user is asking two things:
1. Where to find `.bashrc` or `.zshrc` files
2. How to find where Claude Code is installed

They're on WSL2 (Ubuntu 22.04.5) based on memories.Bhai tu WSL2 (Ubuntu) use karta hai, toh yeh sab Linux commands se hoga. Let me explain both:

---

## 1. `.bashrc` file kahan hai?

Yeh ek **hidden file** hai tere **home directory** mein. WSL terminal mein run kar:

```bash
# Home directory mein ja
cd ~

# Hidden files dekh
ls -la | grep rc
```

Direct open karna hai toh:
```bash
nano ~/.bashrc
```

**Path basically yeh hota hai:**
```
/home/your_username/.bashrc
```

> `.bashrc` = bash shell ke liye (Ubuntu default)
> `.zshrc` = zsh shell ke liye (agar tune zsh install kiya ho)

Check kar konsa shell use ho raha hai:
```bash
echo $SHELL
```
Agar `/bin/bash` aaye → `.bashrc` use kar
Agar `/bin/zsh` aaye → `.zshrc` use kar

---

## 2. Claude Code kahan install hai?

```bash
which claude
```

Yeh exact path print karega, something like:
```
/usr/local/bin/claude
```

Ya version check ke saath:
```bash
claude --version
```

---

## 3. Env vars permanently set karna — Step by Step

```bash
# .bashrc open kar
nano ~/.bashrc
```

File ke **bilkul end mein** yeh lines add kar:

```bash
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL="http://localhost:11434"
```

Save karne ke liye: **Ctrl+O** → Enter → **Ctrl+X**

Phir changes apply kar:
```bash
source ~/.bashrc
```

Verify kar ki set hua:
```bash
echo $ANTHROPIC_BASE_URL
# Output: http://localhost:11434
```

Ab `claude --model glm-4.7-flash` directly chalega bina kuch extra kiye! 🎯

---
**Faizan** `2026-04-14 16:55`

nah re bro claude code instal hain ,mujhe bass ya wala model use karna hain jaan man ollama main claude code use karta hoon tab ke leya to uske leya puch raha hoon bro

---
**Claude** `2026-04-14 16:55`

He's saying Claude Code is already installed, he just wants to use a specific Ollama model when using Claude Code with Ollama. So he wants to know how to set the default model or specify which model to use.

Simple answer - just use the `ollama launch claude --model <modelname>` command, or set env vars in .bashrc.Ohh bhai simple hai! Just yeh command use kar jab bhi Claude Code Ollama ke saath chalana ho:

```bash
ollama launch claude --model <model-name>
```

Example:
```bash
ollama launch claude --model glm-4.7-flash
ollama launch claude --model qwen3-coder
ollama launch claude --model llama3
```

Bas! Jo model name likha `ollama pull` ke time, wahi name yahan daal do.

---

**Agar har baar model likhna nahi chahta** toh `.bashrc` mein ek alias bana de:

```bash
nano ~/.bashrc
```

End mein add kar:
```bash
alias cc-ollama='ollama launch claude --model glm-4.7-flash'
```

Save kar (`Ctrl+O` → Enter → `Ctrl+X`), phir:
```bash
source ~/.bashrc
```

Ab sirf `cc-ollama` type karo terminal mein — Claude Code directly us model ke saath open ho jayega. 🔥

---
**Faizan** `2026-04-14 16:56`

.bashrc  ya file location path keya hoga and like how to find this file tell me

---
**Claude** `2026-04-14 16:56`

Simple answer - .bashrc is always in home directory.Bhai `.bashrc` **always** home directory mein hoti hai, fixed location hai yeh:

```
/home/your_username/.bashrc
```

---

## Find karne ke liye run kar:

```bash
# Exact path dekh
echo ~/.bashrc

# File exist karti hai ya nahi check kar
ls -la ~/.bashrc
```

---

## Direct open karne ke liye:

```bash
nano ~/.bashrc
```

Bas! Koi dhundhna nahi padta, `~` automatically teri home directory ko point karta hai WSL mein. 

`~` = `/home/faizan` (tera case mein)

---
