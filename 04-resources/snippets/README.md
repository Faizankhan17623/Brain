---
title: "Code Snippet Library"
date: 2026-04-27
type: resource
status: active
tags:
  - snippets
  - code
  - reference
---

# Code Snippet Library

Reusable code patterns. Organized by technology. Copy-paste ready.

Tell Claude: *"Save this snippet: [paste code]"* — I will file it under the right technology below.
Tell Claude: *"Show me snippets for [React/Node/MongoDB/Claude API]"*

---

## Index

- [[snippets/react-snippets]] — Hooks, components, patterns
- [[snippets/node-express-snippets]] — Middleware, routes, auth
- [[snippets/mongodb-snippets]] — Queries, aggregation, indexes
- [[snippets/claude-api-snippets]] — Claude API, tool use, streaming
- [[snippets/css-snippets]] — Flexbox, Grid, animations
- [[snippets/javascript-snippets]] — Utility functions, array methods

---

## Quick Reference

### Most Used

```javascript
// Debounce — delay function call until user stops typing
const debounce = (fn, delay) => {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
};
```

```javascript
// Fetch with error handling
const fetchData = async (url) => {
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error('Fetch failed:', err);
    throw err;
  }
};
```

```javascript
// JWT verify middleware (Express)
const authMiddleware = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ message: 'No token' });
  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch {
    res.status(401).json({ message: 'Invalid token' });
  }
};
```

```javascript
// useLocalStorage hook (React)
const useLocalStorage = (key, initial) => {
  const [value, setValue] = useState(() => {
    try { return JSON.parse(localStorage.getItem(key)) ?? initial; }
    catch { return initial; }
  });
  const set = (v) => { setValue(v); localStorage.setItem(key, JSON.stringify(v)); };
  return [value, set];
};
```

---

*Last updated: 2026-04-27*
