---
title: "Coding interview question types"
date: 2026-02-28
created: 2026-02-28 14:36:57
updated: 2026-02-28 14:37:29
uuid: 3a6863ab-b91f-46bc-bc84-6394861ee1a8
category: general
message_count: 2
tags:
  - general
people:
  - "Faizan Khan"
---
# Coding interview question types

## Connections
**People:** [[Faizan Khan]]

## Summary

**Conversation Overview**

The user is preparing for coding interviews targeting Full Stack, Frontend, Backend, React Developer, and JavaScript Developer roles at startups. They requested a comprehensive breakdown of both theoretical and practical question types they should expect during the interview process. Claude provided an extensive overview organized into theory questions covering JavaScript core concepts, React-specific knowledge, Node.js/backend fundamentals, MongoDB database concepts, and general computer science topics including basic system design. For practical coding questions, Claude outlined data structures and algorithms patterns prioritized by frequency, JavaScript output-based questions testing language fundamentals, machine coding rounds requiring live implementation of components like todo apps and search bars, frontend system design scenarios, and API design challenges. Claude specifically tailored the advice for startup environments, providing a prioritized study approach emphasizing JavaScript fundamentals and machine coding rounds as most critical, followed by React knowledge, basic DSA problems, and backend concepts. The conversation concluded with Claude offering to create a structured preparation plan or provide deeper dives into specific categories with practice problems, demonstrating readiness to provide ongoing interview preparation support.

## Conversation

**Faizan** `2026-02-28 14:37`

what are the type of question both theaory and practical so that i am prepeare for my coding interivew tel lme

---
**Claude** `2026-02-28 14:37`

Faizan is preparing for coding interviews. He's a MERN stack developer targeting Full Stack, Frontend, Backend, React Developer, and JavaScript Developer roles at startups. Let me give him a comprehensive breakdown of both theory and practical question types he should prepare for.Here's a complete breakdown of what to expect in coding interviews, Faizan — both theory and practical sides:

## Theory Questions

**JavaScript Core Concepts**
These come up in almost every round: closures, hoisting, event loop, call stack, callback queue, microtask vs macrotask queue, prototypal inheritance, `this` keyword behavior, arrow vs regular functions, `var`/`let`/`const` differences, type coercion, shallow vs deep copy, and event delegation/bubbling/capturing.

**React Specific**
Virtual DOM and reconciliation, component lifecycle (class + hooks equivalent), useState vs useReducer, useEffect cleanup and dependency array, React.memo / useMemo / useCallback and when to use each, controlled vs uncontrolled components, Context API vs Redux (tradeoffs), keys in lists and why they matter, React fiber architecture (high-level), and SSR vs CSR vs SSG.

**Node.js / Backend**
Event-driven architecture, how Node handles concurrency (single-threaded + event loop), middleware concept in Express, streams and buffers, authentication strategies (JWT vs session), REST API design principles, status codes and when to use them, error handling patterns, and CORS.

**Database (MongoDB)**
Indexing and why it matters, aggregation pipeline stages, embedding vs referencing (document design), transactions and when you need them, sharding and replication (high-level), and difference between SQL and NoSQL tradeoffs.

**General CS / System Design (Lite)**
HTTP methods, HTTP vs HTTPS, cookies vs localStorage vs sessionStorage, caching strategies, how DNS works, what happens when you type a URL in the browser, basic security concepts (XSS, CSRF, SQL injection), and OAuth flow basics.

---

## Practical / Coding Questions

**DSA (Data Structures & Algorithms)**
This is the most tested category. Focus on these patterns in order of priority:

Arrays & Strings — two pointer, sliding window, frequency maps, kadane's algorithm. Linked Lists — reverse, detect cycle, merge two sorted. Stacks & Queues — valid parentheses, next greater element, implement queue using stacks. Hash Maps — two sum pattern, group anagrams, subarray sum equals K. Trees — BFS, DFS, inorder/preorder/postorder, lowest common ancestor, max depth. Sorting & Searching — binary search variations, merge sort, quick sort. Recursion & Backtracking — subsets, permutations, N-queens (less common for frontend roles). Dynamic Programming — fibonacci, climbing stairs, coin change, longest common subsequence (mostly for backend/full stack roles).

**JavaScript Output-Based Questions**
They'll show you code and ask "what's the output?" — these test closures, async/await, promise chaining, setTimeout behavior, `this` binding, and scope.

**Machine Coding / Live Coding Rounds**
Build something in 45-60 minutes. Common tasks: todo app, autocomplete/search bar, infinite scroll, debounce/throttle implementation, custom hooks (useDebounce, useFetch), pagination component, star rating component, accordion/tabs, shopping cart with state management, stopwatch/timer, and modal with portal.

**System Design (Frontend)**
Design a chat application, design a newsfeed (like Twitter/Instagram), design an image carousel with lazy loading, design a notification system, or design a dashboard with real-time data.

**API Design Round**
Design REST endpoints for a given feature, handle authentication and authorization, write Express routes with proper error handling, and explain your database schema choices.

---

## How to Prioritize (for startup roles)

Since you're targeting startups, here's the order of importance:

1. **JavaScript fundamentals + output questions** — almost guaranteed
2. **Machine coding round** — very common in startups
3. **React theory + practical** — core for frontend/full stack
4. **DSA (easy-medium level)** — arrays, strings, hash maps, stacks
5. **Node/MongoDB theory** — for backend/full stack rounds
6. **System design lite** — sometimes asked for mid-level roles

Want me to create a structured day-by-day preparation plan, or should I deep-dive into any specific category with practice problems?

---
