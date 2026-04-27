---
title: "Transitioning to AI engineering through agent development"
date: 2026-01-31
created: 2026-01-31 09:57:31
updated: 2026-01-31 09:58:29
uuid: 23cd298f-71ef-4e28-87f0-651eada367d6
category: ai-ml
message_count: 4
tags:
  - ai-engineering
  - learning
  - ml-engineering
  - programming
people:
  - "Faizan Khan"
related_topics:
  - "AI Engineering"
  - "ML Engineering"
---
# Transitioning to AI engineering through agent development

## Connections
**People:** [[Faizan Khan]]

**Topics:** [[AI Engineering]] · [[ML Engineering]]

**Companies:** [[Anthropic]]

## Summary

**Conversation Overview**

The user shared their strategic insight about the evolving AI landscape, recognizing that while AI agents are becoming more sophisticated, they still require human intervention for debugging, accuracy improvements, and handling failure cases. Based on this observation, they've decided to transition their career toward becoming an AI, ML, or LLM engineer, specifically focusing on generative AI and agentic AI to position themselves for high-value opportunities. They have a MERN stack development background with experience in Docker, MySQL, and CI/CD, which provides a strong foundation for this transition.

Claude validated the user's assessment about agent oversight being a critical bottleneck in production AI systems and confirmed that their software engineering background positions them well for AI engineering roles, since most positions require practical system-building skills rather than academic research credentials. The conversation focused on developing a practical 12-month transition plan, emphasizing that AI engineers are primarily software engineers who build production systems around LLMs rather than PhD researchers.

The roadmap Claude provided was structured in phases: months 1-3 for building foundational skills with RAG applications, prompt engineering, and vector databases; months 4-6 for developing multi-agent systems and evaluation frameworks; months 7-9 for active job hunting while continuing to build projects; and months 10-12 for landing roles and learning on the job. Claude emphasized targeting "LLM Engineer" or "AI Engineer" positions rather than traditional ML Engineer roles, and advised starting job applications at the 6-7 month mark rather than waiting for complete readiness. The user confirmed their 12-month timeline for making this career transition.

## Conversation

**Faizan** `2026-01-31 09:57`

Hi, there's something really going on I would really like to share it with you. You know, as AI agents get better and better, there's something I've really realized. As agents get better, you need someone to create agents, like to do the changes in the agents, like to make them more accurate. Agents are like self-thinking, like, hey, this is wrong and this is how we are to do. But there are some cases that agents do really fail, and for that, the human intervention is really required. So something that I'm planning right now is to, like, become an AI or an ML engineer or an LLM engineer, and in that learning path, I'll also add that generative AI and agentic AI learning path code, so that in the upcoming future, in upskilling, I'll get a good and high valuable job. So what are the answers and what are the takes on it?

---
**Claude** `2026-01-31 09:57`

Faizan is sharing an important realization about AI agents and their limitations, and is considering pivoting his career path toward AI/ML/LLM engineering with a focus on agentic AI. This aligns with what's in his memory - he was previously identified as considering AI-related skills, particularly RAG and AI agents, with AI Engineer being the best path given his full stack background.

Let me think about his key points:
1. AI agents are getting better but still need human oversight and refinement
2. He wants to become an AI/ML/LLM engineer
3. He wants to add generative AI and agentic AI to his learning path
4. Goal is upskilling for high-value jobs

Given his background as a MERN stack developer with Docker, MySQL, and CI/CD experience, this transition makes sense. He already has the software engineering foundation which is crucial for AI engineering roles.

I should:
- Validate his observation about agents needing human oversight
- Confirm this is a strong career direction given his background
- Be direct and practical (matching his communication preference)
- Focus on the practical path forward rather than theory
- Keep it concise

I should NOT:
- Be overly enthusiastic or use excessive formatting
- Give unnecessary background on why AI is important (he already gets it)
- Be condescending about his abilitiesYou're spot on about the agent oversight problem - it's becoming one of the biggest bottlenecks in production AI systems. Companies are shipping agents but quickly realizing they need engineers who can debug hallucinations, optimize prompt chains, tune retrieval systems, and build evaluation frameworks. That's exactly where the jobs are.

Your MERN stack background actually puts you in a strong position. Most "AI engineers" aren't PhD researchers - they're software engineers who understand how to build production systems around LLMs. You already know APIs, databases, deployment, and user-facing systems. That's the hard part.

Here's the practical path:

**Short term (1-3 months):**
- Get hands-on with LangChain or LlamaIndex - build a simple RAG system
- Learn prompt engineering deeply (not just basics - chains, few-shot, CoT)
- Understand vector databases (Pinecone, Weaviate, or even pgvector in PostgreSQL)
- Build one agent project end-to-end - even something simple like a customer service bot

**Medium term (3-6 months):**
- Learn evaluation frameworks (how do you measure if an agent is "accurate"?)
- Dive into agent frameworks (AutoGPT, LangGraph, CrewAI)
- Understand fine-tuning basics (when to use it vs RAG)
- Build projects that show agent failure handling and human-in-the-loop workflows

The "LLM Engineer" or "AI Engineer" title is what you want to target - not ML Engineer (too research-heavy) or traditional Data Scientist. Companies hiring for these roles care more about shipping products than academic credentials.

What's your timeline for making this transition?

---
**Faizan** `2026-01-31 09:58`

12 months

---
**Claude** `2026-01-31 09:58`

The user has a 12-month timeline to transition into AI/LLM engineering. Given their MERN stack background and the fact they're currently job hunting, this is a solid timeline. Let me give them a practical, realistic 12-month roadmap that builds on their existing skills.

I should be direct and practical - no fluff. They want actionable advice. I'll structure this as a phased approach that lets them start applying to jobs before the 12 months are up.12 months is solid - you can be job-ready in 6-9 and spend the rest landing the role and leveling up on the job.

**Months 1-3: Foundation**
- Build 2-3 RAG applications (different use cases: Q&A bot, document search, code assistant)
- Learn prompt engineering patterns deeply - test on real problems
- Get comfortable with OpenAI/Anthropic APIs, LangChain/LlamaIndex
- Study vector databases - implement similarity search from scratch once to understand it
- **Ship something** - even a small tool people can use

**Months 4-6: Agent systems**
- Build multi-agent systems (agents that call other agents/tools)
- Learn evaluation and monitoring - how do you measure success? catch failures?
- Implement human-in-the-loop workflows (your key insight about human intervention)
- Study production patterns: caching, rate limiting, fallbacks, error handling
- Start contributing to open source AI tools or build your own

**Months 7-9: Job hunting phase**
- Portfolio of 4-5 solid projects showing progression
- Start applying - you don't need to wait until month 12
- Tailor resume: "Full Stack Engineer → AI Engineer" narrative
- Interview prep: system design for AI systems, debugging agent failures
- Network in AI communities (Twitter/X, Discord servers, local meetups)

**Months 10-12: Landing + learning**
- Keep building while interviewing
- First offer might be "Full Stack Engineer working with AI" - that's fine
- Once hired, learn on the job - that's where real growth happens

Key: Don't wait to be "ready" before applying. Start applying at month 6-7 when you have real projects to show. The market values builders over credentials.

What's your current GitHub looking like? That'll be your main asset.

---
