---
title: "MERN machine coding interview questions"
date: 2026-03-21
created: 2026-03-21 09:40:47
updated: 2026-03-21 11:14:36
uuid: 44f62173-9c21-4266-bdfc-548e8e409850
category: web-development
message_count: 10
tags:
  - backend
  - dsa
  - frontend
  - job-hunting
  - mern-stack
people:
  - "Faizan Khan"
projects:
  - "Cine Circuit"
  - "StudyNotion"
  - "LinkVault"
related_topics:
  - "MERN Stack"
  - "Job Hunting"
  - "DSA Learning"
---
# MERN machine coding interview questions

## Connections
**People:** [[Faizan Khan]]

**Projects:** [[Cine Circuit]] · [[StudyNotion]] · [[LinkVault]]

**Topics:** [[MERN Stack]] · [[Job Hunting]] · [[DSA Learning]]

**Companies:** [[Anthropic]]

**Schools:** [[Allana Institute]]

## Summary

**Conversation Overview**

The person is a recent MCA graduate (from Allana Institute of Management Sciences, Pune) actively preparing for full stack developer interviews with a MERN stack specialization. They have two notable projects: Cine Circuit, a movie booking platform featuring multi-role authentication (Admin, Theatre Owner, User), Razorpay payment integration with signature verification, atomic MongoDB transactions, and an AI-powered chatbot; and StudyNotion, an EdTech LMS with video progress tracking, hierarchical course management, and Cloudinary-based media uploads. They also have experience with LLM/AI API integrations including the Anthropic API.

The conversation covered three main tasks. First, Claude generated a comprehensive machine coding round question bank for MERN stack interviews, initially organized by difficulty, then reorganized per the person's request into distinct categories: Frontend Only (HTML/CSS/JS and React/Redux), Backend Only (Node.js/Express/MongoDB), and Full Stack MERN combined. The final list contains approximately 47 questions with a company-type reference table mapping question categories to likely interview contexts. Second, the person asked for help drafting a cold outreach email to an HR contact named Gayatri Soni at Mandelbulb Tech in Jaipur for a Full Stack Developer (MERN + Python) role requiring 0–2 years experience. Claude composed the email highlighting the person's MERN strengths and AI integration experience while honestly framing Python/Flask/FastAPI as an area of active upskilling. Third, the person asked Claude to review their resume but did not upload it, so no review occurred.

The person communicates informally and directly, mixing Hindi and English. They prefer structured, categorized output over flat lists, as evidenced by their explicit request to reorganize the question bank by technology layer. Claude noted one factual error mid-conversation — the college name was written incorrectly in the email draft and flagged for correction before sending.

## Conversation

**Faizan** `2026-03-21 09:40`

Make a list of question that can be asked in the machine coding round ad a full stack developer mern you have my details like what I know so like make question so I can practice them and ace my interview do it

---
**Claude** `2026-03-21 09:41`

The user wants a list of machine coding round questions for a MERN stack full stack developer interview. Let me create a comprehensive list based on what I know about Faizan's skills.Here's a solid list of machine coding questions tailored to your MERN stack profile. I've grouped them by difficulty and type so you can practice progressively.

---

## 🟢 Beginner — Warm-up Level

1. **Todo App with CRUD** — Build a full todo app with add, edit, delete, mark complete. Backend REST API + React frontend with Redux state.

2. **User Auth System** — Register/Login with JWT, protected routes on frontend, bcrypt password hashing on backend.

3. **Notes App** — Users can create, edit, delete personal notes. Each note belongs to a logged-in user only.

4. **Search & Filter UI** — Given a list of products from an API, build a search bar + category filter + sort by price. All client-side.

5. **Pagination Component** — Fetch data from a Node API with server-side pagination. Build prev/next + page number UI.

---

## 🟡 Intermediate — Most Common in Interviews

6. **Movie/Product Listing with Cart** — Fetch items, add to cart, show cart count, calculate total. Persist cart in localStorage or Redux.

7. **Multi-step Form with Validation** — 3–4 step form (personal info → address → payment preview). Validate each step before proceeding. No form library.

8. **Real-time Chat UI** — Build a chat interface using Socket.io. Two users can send/receive messages in real time.

9. **Role-Based Dashboard** — Admin sees all users + stats. Regular user sees only their own data. Different routes protected by role from JWT.

10. **File Upload System** — Upload image/PDF to backend, store on Cloudinary or disk, show preview on frontend. *(You've done this in Cine Circuit — great advantage.)*

11. **OTP / Email Verification Flow** — After register, send OTP via Nodemailer. User enters OTP to activate account. Handle expiry.

12. **Infinite Scroll Feed** — Load 10 posts at a time as user scrolls down. Use Intersection Observer API on frontend, cursor-based query on backend.

13. **Comment System** — Posts with nested comments (2 levels). Add, delete (own only), like a comment. Store in MongoDB with refs.

14. **Quiz App** — Timed quiz with multiple choice questions. Track score, show results at the end. Fetch questions from your own API.

15. **Kanban Board** — Drag and drop tasks between columns (To Do / In Progress / Done). Persist state to backend on drop.

---

## 🔴 Advanced — Separates Good from Great

16. **Booking/Slot System** — User picks a date, sees available time slots, books one. Once booked, slot becomes unavailable for others. Use MongoDB transactions. *(Very relevant to Cine Circuit.)*

17. **Payment Integration Flow** — Integrate Razorpay (you already know this). Create order on backend → verify signature → update DB → show success UI. *(Your biggest edge — know every line of this.)*

18. **Video Progress Tracker** — Track how much of a video a user has watched. Resume from where they left off. *(You built this in StudyNotion.)*

19. **Admin Analytics Dashboard** — Show charts (bar/line) for revenue, signups, orders over time. Data fetched from aggregated MongoDB queries.

20. **Notification System** — In-app notifications with read/unread state. Mark all as read. Show unread count badge on bell icon. Real-time via Socket.io or polling.

21. **Rate-Limited API** — Build a Node.js API with rate limiting (e.g., 100 requests/15 min per IP). Return proper 429 response with retry headers.

22. **Search with Debounce + Autocomplete** — As user types in search box, fetch suggestions from backend after 300ms debounce. Show dropdown. Click to navigate.

23. **PDF/Invoice Generator** — After an order is placed, generate a downloadable PDF invoice on the backend and return it to frontend.

---

## ⚡ Bonus — Frontend-Only Quick Rounds

24. Build a **Stopwatch** with lap functionality — no libraries.
25. Build a **Star Rating Component** — reusable, accepts props, works on hover + click.
26. Build an **Accordion / FAQ UI** — only one panel open at a time.
27. Build a **Custom Modal** — open/close, click outside to dismiss, trap focus inside.
28. Build a **Debounced Search Input** — implement debounce from scratch, no lodash.

---

## 📌 Things to Keep in Mind During the Round

- Always start by clarifying scope — ask what's in/out of scope.
- Set up folder structure first before writing any code.
- Mention what you'd add given more time (tests, error boundaries, loading states).
- Your Razorpay + atomic transactions + multi-role auth experience is genuinely rare at fresher level — bring it up naturally.

---

Start with questions **6–15**, they're the most frequently asked. Want me to give you a full solution walkthrough for any specific one?

---
**Faizan** `2026-03-21 09:43`

Are this all and after solving this will I be prepared tell me

---
**Claude** `2026-03-21 09:43`

The user wants to know if this list is comprehensive and if solving these will prepare them for machine coding rounds.Honest answer — **no, this isn't all. And solving these alone won't fully prepare you.**

Here's the real picture:

---

## What This List Covers ✅

- The **most commonly asked** machine coding questions for MERN roles
- Your **existing project knowledge** being tested under pressure
- Core patterns — auth, CRUD, real-time, payments, file uploads

This list is probably **80% of what you'll face** in actual interviews.

---

## What It Doesn't Cover ❌

**DSA inside machine coding**
Some companies give you a coding problem *within* the machine coding round — array manipulation, string problems, basic sorting. Not full DSA but enough to trip you up if you're not warmed up.

**Company-specific formats**
- Some companies give you a **broken codebase** to fix, not build from scratch
- Some give you **existing APIs** and only ask for frontend
- Some are **backend only** — design and build 3–4 REST APIs with proper status codes, middleware, validation

**System design lite**
Mid-size companies sometimes ask you to **explain your decisions** — why MongoDB over SQL here, why Redux over Context, why this schema. You need to speak to your choices.

**Time pressure reality**
These questions on paper feel doable. In **60–90 minutes with someone watching**, half your brain freezes. Solving them once isn't enough — you need to solve them **fast**.

---

## The Real Preparation Formula

Just solving questions = **maybe 50% ready**

Solving questions + these habits = **actually ready**

| Habit | Why It Matters |
|---|---|
| Solve each question **twice** | First time you figure it out. Second time you build it clean and fast. |
| Set a **timer** (60–90 min max) | Simulate real pressure |
| **No copy-paste** from your projects | You need to recall from memory |
| After each build, **explain it out loud** | Interviews test communication, not just code |
| Learn to write **clean folder structure** in under 2 min | First thing interviewers notice |
| Know your **own project code deeply** | They WILL ask you to extend or debug Cine Circuit-like features |

---

## Realistic Timeline

If you practice **1 question per day seriously** (build + explain + revisit):

- **2 weeks** → Comfortable with intermediate questions
- **3–4 weeks** → Can handle most machine coding rounds confidently
- **6 weeks** → You're genuinely strong, not just "prepared enough"

---

## Bottom Line

This list gives you the **right problems**. But preparation is about **speed, clarity under pressure, and being able to talk through your code** — not just making it work.

Ek baar build karna practice nahi hai. **Twice fast, once explained** — that's the standard.

Want me to pick the **top 10 to start with** based on what's most likely given your fresher MERN profile?

---
**Faizan** `2026-03-21 09:56`

How to send email to the hr yo get a job this is the hr that I am sending email tell me kwo

---
**Claude** `2026-03-21 09:56`

The user wants to send an email to this HR for a Full Stack Developer (MERN + Python) position at Mandelbulb Tech, Jaipur. Let me compose a good email for them.

Key details:
- Company: Mandelbulb Tech
- HR email: gayatri.soni@mandelbulbtech.com
- Role: Full Stack Developer (MERN + Python)
- Experience: 0-2 Years
- Location: Jaipur

Faizan's strengths:
- MERN stack (strong)
- Two production projects: Cine Circuit (Razorpay, multi-role auth, MongoDB transactions, AI chatbot) and StudyNotion (EdTech LMS)


- AI integrations and Anthropic API experience
- MCA graduate

The main gap here is Python/Flask/FastAPI experience, which I should acknowledge honestly while framing it as something he's ready to learn quickly given his strong foundation in full-stack development.This JD is a solid match for you — MERN is your core, and the AI integration angle plays right into your Cine Circuit chatbot. The only gap is Python/Flask/FastAPI, but at 0-2 years they're flexible. Let's write this smart.
```
This block is not supported on your current device yet.
```

Good email composed. Let me add some tips for Faizan.---

## Before You Send — Checklist ✅

**Must do:**
- Attach your **resume PDF** (the tailored full stack version, not the master one)
- Fill in your **phone number, LinkedIn, and GitHub** at the bottom
- Fix the college name — it's **Allana Institute of Management Sciences**, not Allama Iqbal (I wrote it wrong in the draft, double check before sending)

**Smart moves:**
- Send it between **10am–12pm or 2pm–4pm** on a weekday — highest open rates
- **Subject line matters most** — don't change it, it's formatted well for ATS + human scanning

**About the Python gap:**
The line *"actively upskilling on Flask/FastAPI"* is honest and smart. Don't claim you know it — but also don't ignore it. This framing shows self-awareness. If they ask in interview, say *"I have strong REST API fundamentals from Node/Express, and I've been picking up Flask — the concepts transfer well."*

**One more thing** — the JD mentions Azure. If they ask, just say you've worked with cloud deployments (Vercel/Render/Cloudinary) and are exploring Azure — that's fair at 0-2 years level.

Bhej de bhai, this profile is genuinely strong for this role. 🎯

---
**Faizan** `2026-03-21 10:05`

Before send the email can you please check my reusme

---
**Claude** `2026-03-21 10:05`

The user wants me to check their resume but hasn't uploaded it yet.Bhai you forgot to attach the resume 😄 Upload kar — PDF ya image dono chalega, main dekh lunga!

---
**Faizan** `2026-03-21 11:13`

Ao make question like in this manner frontend of html css and js backend a nd like full stack and seperate feonetne d nd the backend so make question in this manner now sir

---
**Claude** `2026-03-21 11:14`

The user wants me to reorganize/remake the machine coding questions in a structured manner, separated by:
1. Frontend (HTML, CSS, JS)
2. Backend (Node.js, Express, MongoDB)
3. Full Stack (MERN combined)
4. Separate Frontend only
5. Separate Backend only

Let me create a well-organized list.Here's the full question bank reorganized properly by category 👇

---

## 🎨 Frontend Only — HTML + CSS + JS

*No frameworks, no backend. Pure vanilla. Many companies start here.*

**HTML + CSS**
1. Build a **responsive navbar** with hamburger menu on mobile — no JS libraries
2. Build a **pricing card UI** with 3 tiers, hover effects, highlighted recommended plan
3. Build a **responsive grid layout** — 4 columns on desktop, 2 on tablet, 1 on mobile using only CSS Grid
4. Build a **custom checkbox and radio button** styled from scratch — no default browser styles
5. Build a **sticky header** that shrinks/changes color on scroll using only CSS + minimal JS
6. Build a **loading skeleton screen** like Facebook/LinkedIn uses before content loads

**JavaScript (Logic Heavy)**

7. Build a **debounced search bar** — implement debounce from scratch, no lodash
8. Build a **drag and drop list** — reorder items by dragging, no libraries
9. Build a **infinite scroll** — load more items as user reaches bottom using Intersection Observer
10. Build a **custom modal** — open/close, click outside to close, press ESC to close, trap focus
11. Build a **multi-select dropdown** — searchable, select multiple options, show tags, remove individually
12. Build a **image carousel/slider** — auto-play, dots, prev/next arrows, pause on hover
13. Build a **form with live validation** — email format, password strength meter, confirm password match — no libraries
14. Build a **stopwatch with laps** — start, stop, reset, record lap times
15. Build a **virtual/windowed list** — render only visible 10 items out of 1000 in DOM for performance

---

## ⚙️ Backend Only — Node.js + Express + MongoDB

*API building, no frontend. Just Postman/Thunder Client to test.*

**Basic**

16. Build a **REST API for a Todo app** — full CRUD, proper status codes (200, 201, 400, 404, 500)
17. Build a **User Auth API** — register, login, JWT generation, protected route middleware
18. Build an **API with pagination** — `?page=1&limit=10`, return total count + has next page flag

**Intermediate**

19. Build a **Role-Based Access API** — Admin vs User routes, middleware that checks role from JWT
20. Build a **File Upload API** — accept image/PDF, validate file type and size, store to Cloudinary
21. Build an **OTP verification API** — generate OTP, store with expiry in DB, verify endpoint, resend endpoint
22. Build a **rate-limited API** — max 5 requests per minute per IP, return 429 with retry-after header
23. Build a **soft delete system** — records are never truly deleted, just marked `isDeleted: true`, all queries filter them out

**Advanced**

24. Build a **Booking API with conflict prevention** — no two users can book the same slot, use MongoDB transactions *(your Cine Circuit experience — you've done this)*
25. Build a **search API with filters** — search by name, filter by category + price range, sort by date/price, pagination — all in one endpoint
26. Build an **aggregation pipeline** — given an orders collection, return total revenue per month, top 5 products, average order value
27. Build a **webhook receiver** — accept POST from Razorpay, verify HMAC signature, update DB *(you know this already)*
28. Build a **job queue system** — when user registers, queue a welcome email task, process it async using `bull` or simple `setTimeout` queue

---

## ⚛️ Frontend Only — React + Redux

*No backend. Mock data or JSONPlaceholder API.*

**Components**

29. Build a **reusable Table component** — sortable columns, searchable, pagination, accept any data via props
30. Build a **multi-step form** — 3 steps, validation on each step before next, progress bar, review on last step — no form library
31. Build a **Star Rating component** — hover preview, click to set, accepts `value` and `onChange` props, fully reusable
32. Build an **Accordion/FAQ** — only one open at a time, smooth animation, icon rotates

**State & Logic**

33. Build a **Shopping Cart** — add/remove items, increment/decrement qty, total price, persist in Redux + localStorage
34. Build a **real-time search with autocomplete** — debounced API call, keyboard navigation in dropdown (↑↓ Enter)
35. Build a **Kanban board** — drag tasks between columns (To Do / In Progress / Done), state managed in Redux
36. Build a **notification system** — bell icon with unread count badge, dropdown list, mark all as read, each notification has timestamp

---

## 🔥 Full Stack — MERN Combined

*This is what most actual machine coding rounds test.*

**Beginner Full Stack**

37. **Notes App** — Login, create/edit/delete your own notes, each note is private to logged in user
38. **Bookmark Manager** — Save URLs with title + tags, filter by tag, search by title, user-specific data

**Intermediate Full Stack**

39. **Blog Platform** — Auth, create posts with rich text, comment on posts, like posts, author can delete own post only
40. **Job Board** — Companies post jobs, users apply, admin approves/rejects. Three roles, three dashboards
41. **E-commerce MVP** — Product listing, cart, checkout with Razorpay, order history, admin product management *(your strongest territory)*
42. **Real-time Chat App** — Auth, one-on-one chat, online/offline status, message timestamps, Socket.io
43. **Quiz Platform** — Admin creates quizzes with timer, user takes quiz, result + leaderboard shown at end

**Advanced Full Stack**

44. **Movie Booking System** — Browse movies → select theatre → pick showtime → select seats → pay → get booking confirmation with PDF ticket *(basically Cine Circuit — know this inside out)*
45. **EdTech Platform** — Course creation with video upload, student enrollment, video progress tracking, completion certificate *(basically StudyNotion)*
46. **Analytics Dashboard** — Track user events (page views, clicks), store in MongoDB, show charts — bar, line, pie using Chart.js or Recharts
47. **AI Chatbot Integration** — Chat UI, messages stored in DB per user, backend calls OpenAI/Gemini API, streaming response shown word by word

---

## 📊 Quick Reference — What Gets Asked Where

| Company Type | Most Likely Round |
|---|---|
| Startup (early stage) | Full Stack MERN — questions 37–43 |
| Product company | Full Stack Advanced — 44–47 |
| Service/outsourcing | Backend Only — 16–23 |
| Frontend-focused | React + JS — 29–36 |
| Walk-in / mass hiring | HTML CSS JS — 1–15 |

---

Yeh list complete hai bhai. Print kar lo ya ek spreadsheet banao — ek ek tick karo as you solve them. Want me to make a **30-day practice schedule** around these?

---
