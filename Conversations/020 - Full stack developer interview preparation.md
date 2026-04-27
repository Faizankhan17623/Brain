---
title: "Full stack developer interview preparation"
date: 2026-02-17
created: 2026-02-17 10:40:09
updated: 2026-02-17 10:40:54
uuid: c72caedd-3767-4a0b-95e8-a3479091b4af
category: career
message_count: 2
tags:
  - dsa
  - job-hunting
  - mern-stack
people:
  - "Faizan Khan"
projects:
  - "Cine Circuit"
related_topics:
  - "MERN Stack"
  - "Job Hunting"
  - "DSA Learning"
---
# Full stack developer interview preparation

## Connections
**People:** [[Faizan Khan]]

**Projects:** [[Cine Circuit]]

**Topics:** [[MERN Stack]] · [[Job Hunting]] · [[DSA Learning]]

## Summary

**Conversation Overview**

The user requested comprehensive preparation for upcoming full stack developer or MERN stack developer interviews. Claude provided an extensive interview preparation guide covering all major components of the MERN stack (MongoDB, Express, React, Node.js) along with foundational web technologies. The preparation material was structured by technology category, covering key concepts, common interview questions, and practical code examples.

The guide included detailed coverage of JavaScript fundamentals like closures, hoisting, the event loop, promises, and array methods, which are frequently tested in technical interviews. For React, Claude covered essential hooks, the Virtual DOM, performance optimization techniques, and component patterns. The Node.js and Express section focused on middleware, error handling, REST API best practices, and JWT authentication flows. MongoDB coverage included schema design principles, common queries, aggregation pipelines, and indexing strategies.

Claude also included sections on security essentials, basic system design concepts for senior roles, behavioral interview questions, and provided a quick revision checklist for the user to track their preparation progress. The material was presented in a practical, interview-focused format with code examples and specific technical details that interviewers commonly ask about. The user was offered additional support for deeper dives into specific topics, mock interview questions, or coding challenge walkthroughs to further enhance their preparation.

## Conversation

**Faizan** `2026-02-17 10:40`

Prepare me for my upcoming full stack developer or mern stack developer interview prepare me

---
**Claude** `2026-02-17 10:40`

Faizan wants comprehensive MERN stack interview preparation. Let me provide a well-structured guide covering the key topics.# MERN Stack Interview Preparation 🚀

Let me break this down by category — covering concepts, common questions, and what interviewers actually look for.

---

## 🌐 HTML & CSS

**Key Concepts to Know:**
- Semantic HTML (article, section, nav, header, footer, main)
- Box model (margin, border, padding, content)
- Flexbox vs Grid — when to use which
- CSS specificity (inline > id > class > tag)
- Responsive design with media queries
- Position: static, relative, absolute, fixed, sticky

**Common Questions:**
- What's the difference between `display: none` and `visibility: hidden`?
- What is z-index and stacking context?
- How does CSS specificity work?
- What are pseudo-classes vs pseudo-elements?

---

## ⚡ JavaScript (Most Important)

**Core Concepts:**

**1. var / let / const**
- `var` → function scoped, hoisted, re-declarable
- `let` → block scoped, not re-declarable
- `const` → block scoped, can't be reassigned (but object properties can change)

**2. Hoisting**
```js
console.log(x); // undefined (var is hoisted)
var x = 5;

console.log(y); // ReferenceError (let is not initialized)
let y = 5;
```

**3. Closures**
```js
function counter() {
  let count = 0;
  return function() {
    return ++count;
  };
}
const increment = counter();
increment(); // 1
increment(); // 2
```

**4. Event Loop & Async**
- Call Stack → Web APIs → Callback Queue → Microtask Queue
- Microtasks (Promises) run before macrotasks (setTimeout)
```js
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
console.log('4');
// Output: 1, 4, 3, 2
```

**5. Promise vs async/await**
```js
// Promise
fetch(url).then(res => res.json()).then(data => console.log(data));

// async/await
const data = await fetch(url).then(res => res.json());
```

**6. Prototypes & `this`**
- `this` depends on how a function is called
- Arrow functions don't have their own `this`
- `call`, `apply`, `bind` to manually set `this`

**7. Array Methods (very commonly tested)**
```js
// map, filter, reduce, find, some, every, flat, flatMap
const nums = [1, 2, 3, 4, 5];
nums.filter(n => n % 2 === 0);        // [2, 4]
nums.reduce((acc, n) => acc + n, 0);  // 15
nums.find(n => n > 3);                // 4
```

**8. Destructuring & Spread**
```js
const { name, age } = user;
const newArr = [...arr1, ...arr2];
const newObj = { ...obj1, ...obj2 };
```

**9. Deep Copy vs Shallow Copy**
```js
// Shallow
const copy = { ...original };

// Deep
const deep = JSON.parse(JSON.stringify(original)); // loses functions/dates
const deep2 = structuredClone(original); // modern approach
```

---

## ⚛️ React

**Key Concepts:**

**1. Hooks**
- `useState` — local state
- `useEffect` — side effects (runs after render)
- `useRef` — DOM reference or mutable value without re-render
- `useMemo` — memoize computed value
- `useCallback` — memoize function reference
- `useContext` — consume context

**2. useEffect Behavior**
```js
useEffect(() => {}, []);        // runs once on mount
useEffect(() => {}, [value]);   // runs on mount + when value changes
useEffect(() => {});            // runs after every render

// Cleanup
useEffect(() => {
  const timer = setInterval(...);
  return () => clearInterval(timer); // cleanup
}, []);
```

**3. Virtual DOM**
React keeps a virtual copy of the DOM. On state change, it diffs the old and new virtual DOM (reconciliation) and only updates what changed in the real DOM.

**4. Keys in Lists**
Keys help React identify which items changed. Always use unique, stable IDs — never use array index as key (causes bugs on reorder/delete).

**5. Controlled vs Uncontrolled Components**
```js
// Controlled — React controls the value
<input value={state} onChange={e => setState(e.target.value)} />

// Uncontrolled — DOM controls it
<input ref={inputRef} />
```

**6. Lifting State Up**
When siblings need to share state, move it to their closest common parent.

**7. React Performance**
- `React.memo` — prevents re-render if props unchanged
- `useMemo` — avoid expensive recalculations
- `useCallback` — stable function reference for child components
- Lazy loading: `React.lazy` + `Suspense`

**8. Common Interview Questions**
- What is reconciliation?
- Difference between `useEffect` and `useLayoutEffect`?
- What causes unnecessary re-renders?
- How does Context API work vs Redux?

---

## 🔄 Redux (Toolkit)

**Flow:** UI dispatches action → Reducer updates state → Component re-renders

**Your typical pattern:**
```js
// slice
const authSlice = createSlice({
  name: 'auth',
  initialState: { user: null, loading: false, error: null },
  extraReducers: (builder) => {
    builder
      .addCase(loginUser.pending, state => { state.loading = true })
      .addCase(loginUser.fulfilled, (state, action) => {
        state.loading = false;
        state.user = action.payload;
      })
      .addCase(loginUser.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  }
});
```

**Questions:**
- Redux vs Context API — when to use which?
- What is a selector? Why use `createSelector`?
- What is middleware? How does `redux-thunk` work?
- What's the difference between `createAsyncThunk` and a regular action?

---

## 🖥️ Node.js & Express

**Key Concepts:**

**1. Node.js Event Loop**
Node is single-threaded but handles concurrency via non-blocking I/O using the event loop. Heavy CPU tasks block the loop — use worker threads for those.

**2. Middleware**
```js
// Middleware runs in order — order matters!
app.use(express.json());
app.use(cors());
app.use('/api', router);

// Custom middleware
const authMiddleware = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ message: 'Unauthorized' });
  req.user = verifyToken(token);
  next();
};
```

**3. Error Handling**
```js
// Error middleware has 4 params
app.use((err, req, res, next) => {
  res.status(err.status || 500).json({ message: err.message });
});
```

**4. REST API Best Practices**
- Use proper HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Use proper status codes (200, 201, 400, 401, 403, 404, 500)
- Validate inputs (express-validator or Joi)
- Paginate large datasets

**5. JWT Authentication Flow**
```
Login → server creates JWT (header.payload.signature) → 
client stores token → sends in Authorization header → 
server verifies on each protected route
```

**Common Questions:**
- What is the difference between `process.nextTick` and `setImmediate`?
- How do you handle file uploads? (multer, Cloudinary)
- What is CORS and how do you configure it?
- How do you prevent SQL/NoSQL injection?

---

## 🍃 MongoDB

**Key Concepts:**

**1. Schema Design**
- Embed for data accessed together (1-to-few)
- Reference for large or frequently updated data (1-to-many)

**2. Common Queries**
```js
// Find with filter
await User.find({ role: 'admin', isActive: true });

// Populate
await Booking.find().populate('user', 'name email');

// Aggregation
await Show.aggregate([
  { $match: { status: 'active' } },
  { $group: { _id: '$theater', totalShows: { $sum: 1 } } },
  { $sort: { totalShows: -1 } }
]);
```

**3. Indexing**
```js
// Single index
userSchema.index({ email: 1 });

// Compound index
showSchema.index({ theater: 1, date: 1 });
```

**4. Common Questions**
- What's the difference between `find` and `findOne`?
- What is aggregation pipeline?
- How do you handle transactions in MongoDB?
- What are indexes and why are they important?

---

## 🔒 Security Essentials

- **JWT** — stateless auth, set expiry, use refresh tokens
- **bcrypt** — hash passwords, never store plain text
- **CORS** — configure allowed origins explicitly
- **Rate limiting** — prevent brute force (`express-rate-limit`)
- **Helmet** — sets secure HTTP headers
- **Input validation** — always validate and sanitize on server
- **Environment variables** — never hardcode secrets

---

## 🏗️ System Design (for senior roles)

Be ready to discuss your **theater booking platform** — it's a perfect example:

- How do you handle **concurrent seat booking**? (Optimistic locking, atomic MongoDB operations)
- How do you structure **role-based access**? (Admin, theater owner, show creator, user)
- How would you **scale** this? (Load balancing, caching with Redis, CDN for images)
- How do you handle **file uploads**? (Multer → Cloudinary)
- How is your **database structured**? (Shows, Theaters, Tickets, Users)

---

## 📋 Behavioral Questions

- Tell me about a difficult bug you solved → use your MongoDB/CORS issues
- Describe a complex feature you built → ticket allotment system
- How do you stay up to date? → mention your AI/ML transition
- What's your biggest weakness and how are you working on it?

---

## ✅ Quick Revision Checklist

| Topic | Status |
|-------|--------|
| JS closures, hoisting, event loop | ⬜ |
| Promise, async/await, error handling | ⬜ |
| React hooks (all major ones) | ⬜ |
| Redux Toolkit + createAsyncThunk | ⬜ |
| Express middleware + error handling | ⬜ |
| JWT auth flow | ⬜ |
| MongoDB queries + aggregation | ⬜ |
| REST API design principles | ⬜ |
| Basic system design | ⬜ |

---

Want me to go deeper on any specific topic, generate mock interview questions, or do a coding challenge walkthrough? 💪

---
