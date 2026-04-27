---
title: "Date input showing current date instead of release date"
date: 2026-02-17
created: 2026-02-17 09:50:49
updated: 2026-02-17 12:54:55
uuid: f7ebc0f1-03d3-46f6-86e4-7b1ff2938280
category: web-development
message_count: 14
tags:
  - backend
  - frontend
  - health
  - job-hunting
  - mern-stack
  - programming
  - resume
people:
  - "Faizan Khan"
related_topics:
  - "MERN Stack"
  - "Resume Building"
  - "Job Hunting"
  - "Ear Health"
---
# Date input showing current date instead of release date

## Connections
**People:** [[Faizan Khan]]

**Topics:** [[MERN Stack]] · [[Resume Building]] · [[Job Hunting]] · [[Ear Health]]

**Places:** [[India]]

## Summary

**Conversation Overview**

The user initially sought help with a date parsing issue in their theater booking platform, where release dates in "Fri, 20 Feb 2026" format weren't being handled correctly by their existing parseDMYDate function. Claude identified that the function needed to handle comma-separated formats and provided a solution. The user then questioned why their date picker only allowed selection within the next 10 days, which Claude explained was due to their own business rule implemented in the code with maxDate set to today plus 10 days. The user requested this limit be extended to 90 days, and Claude provided the specific code changes needed in three locations: the maxDate calculation, error message, and UI display text.

The conversation then shifted when the user asked for help creating a resume. Claude requested comprehensive details including contact information, work experience, projects, education, skills, certifications, target roles, and specific companies they're interested in. The user indicated they're targeting full stack developer, backend developer, frontend developer, Node.js developer, JavaScript developer, or React developer positions. Finally, the user provided what appears to be a large dataset of job listings and asked Claude to extract companies hiring for those specific developer roles. Claude analyzed the extensive data and organized the results into categorized tables by technology stack, identifying over 80 companies actively hiring across Node.js, React, full stack, JavaScript, and general backend/frontend positions, with particular emphasis on companies that would be good matches for someone with a MERN stack background.

## Conversation

**Faizan** `2026-02-17 09:50`

you need to do the chagens in thei code in this code there is a log where is that is it when we click on s ahow the nwe select the release date the probels that is coming is that the date in the input is like comign the current dat the date that is today iw at that eh date should come from the date wheh the moveis is release for eg release date is 20 but the date is comgin 17 that is the todays date so tell me what am i doing wroing ion thei code and how to resovel it

---
**Claude** `2026-02-17 09:51`

The user is saying that when they select a show and go to step 2 (release date), the date input is showing today's date (17th) instead of the movie's release date (20th) as the default/minimum value.

Looking at the code:

The `getMinDate()` function returns the minimum date for the input. The input has `min={getMinDate()}` and `value={releaseDate}` where `releaseDate` starts as `''`.

The issue is that when `releaseDate` is empty (`''`), the browser renders the date input showing today's date visually, even though the value is empty. But wait, the user says the date is "coming" as today's date - they might mean the min date is today's date.

Actually looking more carefully at `getMinDate()`:

```js
const getMinDate = () => {
    const tomorrow = new Date()
    tomorrow.setDate(tomorrow.getDate() + 1)
    tomorrow.setHours(0, 0, 0, 0)

    if (selectedShowData?.releasedate) {
      const releaseDateParsed = parseDMYDate(selectedShowData.releasedate)
      if (releaseDateParsed) {
        const releaseDateOnly = new Date(releaseDateParsed.getFullYear(), releaseDateParsed.getMonth(), releaseDateParsed.getDate())

        // If release date is in the future (after tomorrow), use release date
        if (releaseDateOnly.getTime() > tomorrow.getTime()) {
          return formatDateForInput(releaseDateOnly)
        }
      }
    }
    return formatDateForInput(tomorrow)
  }
```

So if the movie release date is Feb 20 and today is Feb 17, tomorrow is Feb 18. Since Feb 20 > Feb 18, `getMinDate()` should return Feb 20. That seems correct.


The problem might be that the input's empty value causes browsers to display today's date as a visual placeholder, or the user could be referring to the minimum selectable date being today. I need to check if `parseDMYDate` is correctly parsing the backend format `DD/MM/YYYY` - if `releasedate` is `"20/02/2025"`, the parsing needs to handle this correctly to extract the actual release date.

Looking at the date calculations, `today` and `maxDate` are recomputed on every render since they're declared at the component level outside any effect hook. The issue might be that the input field is showing today's date when it should be showing the parsed release date instead.

Re-reading the user's message, they seem to want the date input pre-populated with the movie's release date (the 20th) rather than defaulting to today (the 17th). When a show is selected, `releaseDate` should automatically be set to that movie's release date value.

The solution is to update `handleShowSelect` so it parses the movie's release date and formats it properly for the input field. When `show.data?.releasedate` exists, parse it using `parseDMYDate`, then format it with `formatDateForInput` before setting it as the state. If parsing fails or no release date exists, clear the field instead.## The Problem

In `handleShowSelect`, you're setting `setReleaseDate('')` — so the date input has an empty value. When a date input is empty, **browsers visually display today's date as a placeholder**. That's why you see 17th instead of 20th.

You need to **pre-populate** `releaseDate` with the movie's release date when a show is selected.

## The Fix

Change your `handleShowSelect` function:

```js
const handleShowSelect = (show, index) => {
  setSelectedShow(show.data?._id)
  setSelectedShowData(show.data)
  setSelectedShowIndex(show.index)
  setDateError('')

  // ✅ Pre-set the date input to the movie's release date
  if (show.data?.releasedate) {
    const parsed = parseDMYDate(show.data.releasedate)
    if (parsed) {
      setReleaseDate(formatDateForInput(parsed))
    } else {
      setReleaseDate('')
    }
  } else {
    setReleaseDate('')
  }

  setStep(2)
}
```

Now when the user clicks a show with release date 20/02/2025, the date input will show **20th February** instead of today (17th).

> **Why this works:** `parseDMYDate` converts your backend `DD/MM/YYYY` string into a JS Date, then `formatDateForInput` converts it to `YYYY-MM-DD` which is what the HTML date input expects as its `value`.

---
**Faizan** `2026-02-17 09:53`

nope not workign now is tead of 17 i am able to see 18 but i wnat to see 20 because that is the release date so you are doign wsomething wroing in thei code so wait one minute take the ful lcode one again too bro 

resovle this isse it has wasted al ot of my time so resovle it please

---
**Claude** `2026-02-17 09:53`

The issue is that when the release date is set to 20 (20/02/2025 for example), the pre-populated date is showing 18 instead of 20. This is a timezone issue.

When `parseDMYDate` creates `new Date(year, month, day)`, it creates a local date. But when `formatDateForInput` converts it, there might be an off-by-one.

Wait, actually the problem is likely in `handleShowSelect` - when the release date is pre-set, it goes through `setReleaseDate` directly without going through `handleDateChange` validation. But the date shown is wrong.

Actually wait - if release date is `20/02/2025`, `parseDMYDate` returns `new Date(2025, 1, 20)` which is Feb 20. Then `formatDateForInput` returns `2025-02-20`. That should be correct.

But the user says they see 18 instead of 20. Hmm. Let me think...

Oh wait! The `getMinDate()` function - when the input has `min` set to a certain date, the browser might display that min date if the value is invalid or before the min. 

Actually no - we're setting the value directly.

Wait - could it be a timezone issue? `new Date(year, month, day)` creates local time midnight. `formatDateForInput` reads `getFullYear()`, `getMonth()`, `getDate()` - all local time. So that should be fine.

Hmm, but the user says they see 18 now (previously 17 with my fix). 18 would be tomorrow (today is 17 Feb 2026). So the `getMinDate()` is returning tomorrow (18th) and the browser is clamping the value to the min?

Oh! That's the issue. The `releaseDate` state is being set to `2026-02-20`, but then there's a `dateError` being set because of some validation... No wait, we're not calling `handleDateChange`.


Looking at this more carefully - if the release date stored is 20/02/2026 and today is 17/02/2026, then `getMinDate()` should return 20/02/2026 since that's the release date. The input value is also set to 20, so the min and value match. But the user is seeing 18 displayed instead. This suggests either the stored release date in the database is actually different than expected, or `parseDMYDate` is parsing the date incorrectly.

Could the backend be returning the release date in a different format entirely - like ISO format `2025-02-20` instead of `DD/MM/YYYY`? Or maybe the issue is that `formatDateDisplay(releaseDate)` is calling `parseDMYDate` on a string that's already in `YYYY-MM-DD` format, which would parse it wrong.

Actually, the user said they're seeing 18 in the input field but want 20. If the input is showing 18, then `parseDMYDate(show.data.releasedate)` is likely parsing the backend value as February 18th instead of February 20th. Either `parseDMYDate` is misinterpreting the format, or `formatDateForInput` is shifting the date by a couple days - possibly due to timezone handling when converting to UTC.

The real issue might be that the backend is sending `releasedate` in a different format than expected. If it's coming as an ISO string like `2026-02-20T00:00:00.000Z` instead of `DD/MM/YYYY`, then `parseDMYDate` would fail to parse it since it splits by `/`, return null, and leave the input empty or with a default value.

I need to handle multiple date formats in the parsing logic. The most straightforward approach is to write a more flexible date parser that can recognize both `DD/MM/YYYY` and ISO formats, then use that in `handleShowSelect` instead of relying solely on `parseDMYDate`.

For the `DD/MM/YYYY` case, I'd split on `/` and construct a Date object with the parsed day, month, and year values. For ISO or `YYYY-MM-DD` formats, I'd pass the string directly to the Date constructor and validate it worked. The user should also log `show.data.releasedate` to confirm what format the backend is actually sending.The real issue is likely that `parseDMYDate` is **failing silently** — the `releasedate` from your backend might not actually be in `DD/MM/YYYY` format (could be ISO string like `2026-02-20T00:00:00.000Z`). When parsing fails, it returns `null`, so `releaseDate` gets set to `''`, and the browser shows the `min` date (tomorrow = 18th).

**Add this console.log first to confirm:**
```js
const handleShowSelect = (show, index) => {
  console.log('releasedate from backend:', show.data?.releasedate) // CHECK THIS
  ...
}
```

**Then replace `parseDMYDate` with this robust version that handles multiple formats:**

```js
const parseDMYDate = (dateStr) => {
  if (!dateStr) return null

  // Format: DD/MM/YYYY
  if (dateStr.includes('/')) {
    const parts = dateStr.split('/')
    if (parts.length === 3) {
      const day = parseInt(parts[0], 10)
      const month = parseInt(parts[1], 10) - 1
      const year = parseInt(parts[2], 10)
      return new Date(year, month, day)
    }
  }

  // Format: ISO string or YYYY-MM-DD (e.g. "2026-02-20T00:00:00.000Z" or "2026-02-20")
  if (dateStr.includes('-')) {
    const d = new Date(dateStr)
    if (!isNaN(d.getTime())) {
      // Force local date to avoid timezone shift
      return new Date(d.getFullYear(), d.getMonth(), d.getDate())
    }
  }

  return null
}
```

This single change fixes everything because `parseDMYDate` is used in `handleShowSelect`, `handleDateChange`, `formatDateDisplay`, and `getMinDate` — so all of them will now correctly parse whatever format your backend sends.

The key line is `new Date(d.getFullYear(), d.getMonth(), d.getDate())` — this strips the timezone from ISO strings which would otherwise cause the -1 or -2 day shift you were seeing.

---
**Faizan** `2026-02-17 09:56`

nah still the same isue see this image you can understand what is goin wrong though and this is what comign ffomr the backend releasedate from backend: Fri, 20 Feb 2026 and this is the full code

---
**Claude** `2026-02-17 09:56`

The backend is returning `"Fri, 20 Feb 2026"` format, not `DD/MM/YYYY` or ISO. My parseDMYDate doesn't handle this format. I need to add parsing for this format.Found it! The backend returns **`"Fri, 20 Feb 2026"`** — neither `DD/MM/YYYY` nor ISO format. Your `parseDMYDate` doesn't handle this, so it returns `null`, and the date stays empty. Fix just the `parseDMYDate` function:

```js
const parseDMYDate = (dateStr) => {
  if (!dateStr) return null

  // Format: DD/MM/YYYY
  if (dateStr.includes('/')) {
    const parts = dateStr.split('/')
    if (parts.length === 3) {
      const day = parseInt(parts[0], 10)
      const month = parseInt(parts[1], 10) - 1
      const year = parseInt(parts[2], 10)
      return new Date(year, month, day)
    }
  }

  // ✅ Format: "Fri, 20 Feb 2026" (backend format)
  if (dateStr.includes(',')) {
    const d = new Date(dateStr)
    if (!isNaN(d.getTime())) {
      return new Date(d.getFullYear(), d.getMonth(), d.getDate())
    }
  }

  // Format: ISO string or YYYY-MM-DD
  if (dateStr.includes('-')) {
    const d = new Date(dateStr)
    if (!isNaN(d.getTime())) {
      return new Date(d.getFullYear(), d.getMonth(), d.getDate())
    }
  }

  return null
}
```

The key fix is the `dateStr.includes(',')` block. `new Date("Fri, 20 Feb 2026")` works perfectly in JS, and wrapping it with `new Date(year, month, date)` strips any timezone offset so you always get exactly the 20th.

---
**Faizan** `2026-02-17 09:57`

and can you also tell me why am i seeign the next 10 days date on ly this is the full code sir jee

---
**Claude** `2026-02-17 09:58`

The user is asking two things:
1. The date fix (which should now work with the "Fri, 20 Feb 2026" format)
2. Why they're seeing only the next 10 days in the date picker

For question 2: The `max` is set to `formatDateForInput(maxDate)` which is today + 10 days. The release date (Feb 20) is within 10 days from Feb 17, so it shows. But the issue is the `max` prop restricts the calendar to only show/allow dates up to 10 days from today. So dates beyond that are greyed out.

But wait - the user is asking "why am I seeing only the next 10 days" - this is by design in the code! The `max={formatDateForInput(maxDate)}` limits the date picker to today + 10 days. The user seems confused why only those dates are selectable.

Actually re-reading: the user seems to be asking why the calendar only shows the next 10 days as selectable. This is intentional in the code - it's a business rule. But maybe the user wants to understand it or wants to change it.

Actually I think the user is asking why the date input only allows selection within next 10 days - and the answer is simply because of the `max` attribute set to `maxDate` (today + 10). This is a deliberate rule in the code.

Let me just explain both points clearly.## Two separate things happening:

**1. The date fix** — should now work with the latest `parseDMYDate` since `"Fri, 20 Feb 2026"` contains a comma. Test it and confirm.

---

**2. Why only 10 days are selectable — this is intentional in YOUR OWN code:**

Look at this in your date input:
```jsx
max={formatDateForInput(maxDate)}  // maxDate = today + 10 days
```

And this at the top of the component:
```js
const maxDate = new Date(today)
maxDate.setDate(maxDate.getDate() + 10)  // ← YOU set this rule
```

So dates beyond 10 days from today are greyed out/blocked by design. This is your own business rule: *"Cannot create tickets more than 10 days in advance"*.

**If you want to increase it**, just change the `10` to whatever you want:
```js
maxDate.setDate(maxDate.getDate() + 30) // allows 30 days ahead
```

Or **remove the max limit entirely** by removing the `max` prop from the input:
```jsx
// Remove this ↓
max={formatDateForInput(maxDate)}
```

And remove the check in `handleDateChange`:
```js
// Remove this block ↓
if (selectedDate > maxDate) {
  setDateError('Cannot create tickets more than 10 days in advance')
  return
}
```

So it's not a bug — it's your own rule. Decide what limit makes sense for your business.

---
**Faizan** `2026-02-17 09:58`

in the max allow 90 days

---
**Claude** `2026-02-17 09:58`

Simple change.Just change one line:

```js
maxDate.setDate(maxDate.getDate() + 90)
```

And update the error message in `handleDateChange`:

```js
if (selectedDate > maxDate) {
  setDateError('Cannot create tickets more than 90 days in advance')
  return
}
```

And the rule display text in the UI:

```jsx
<li>• Cannot select more than 90 days in advance</li>
```

That's it — 3 places, all just changing `10` to `90`.

---
**Faizan** `2026-02-17 12:46`

cna you help me  create a resume for me

---
**Claude** `2026-02-17 12:46`

The user wants help creating a resume. I should ask for their details.Sure! I'll need some details from you to build it. Please share:

1. **Full Name & Contact Info** — email, phone, LinkedIn, GitHub, location (city)
2. **Work Experience** — company names, roles, dates, and what you did
3. **Projects** — project names, tech used, what it does (your theater booking platform, etc.)
4. **Education** — degree, university, year
5. **Skills** — tech stack (I know you have MERN, Docker, MySQL, CI/CD etc. but confirm and add anything else)
6. **Any certifications or achievements**

Also let me know:
- What **type of roles** are you targeting? (Full Stack Dev, or AI/ML focused since you're transitioning?)
- Any **specific companies or job descriptions** you want to tailor it to?

Share whatever you have and I'll build it out!

---
**Faizan** `2026-02-17 12:52`

can you scrape this date and give me the names of the companues that are hiring for ful lstak develoepr backend developer frontend developer node js developer js developer or react developer tell me

---
**Claude** `2026-02-17 12:54`

The user wants me to filter through this data and find companies hiring for full stack, backend, frontend, Node.js, JS, or React developers. This is document analysis, not web scraping. I can do this directly from the content provided.

Let me go through and find relevant companies. I'll look for mentions of:
- Full stack / fullstack developer
- Backend developer/engineer
- Frontend developer/engineer
- Node.js developer
- JavaScript/JS developer
- React developer

Let me scan through:

1. TravelPerk - All software and product roles ✓
2. Uber - Frontend SWE, Backend SWE ✓
3. Plain - Senior Frontend Engineer, Senior Backend Engineer ✓
4. Findhotel - Software engineers ✓
5. Flexport - Full-stack, frontend, backend ✓
6. Yelp - SWE ✓
7. Skyscanner - frontend web, backend node.js ✓ (Node.js!)
8. Garden - Frontend Engineers, Open Source Developers (nodeJS, Typescript) ✓ Node.js, React
9. Veepee - NodeJs, React, JS, Ts ✓
10. RapidAPI - Frontend Engineer, Backend Engineer (NodeJS), Backend Engineer (Python), Sr. Software Engineer (JavaScript), Staff Software Engineer (JavaScript) ✓
11. Klarna - JavaScript (Backend and Frontend) ✓
12. Lebara - Full Stack Dev (React & Node) ✓ 
13. Omnipresent - Full stack JS engineer ✓
14. Envoy - Fullstack, Backend, Frontend ✓
15. M&S - React/Next.js engineers ✓
16. Personio - Backend/Frontend Engineers ✓
17. Humaans.io - Software Engineering (Full Stack) ✓
18. Miro - Engineering Manager, Software Engineer (Backend, Front, Fullstack) ✓


19. Treatwell - Frontend, Backend, Fullstack positions ✓
20. Netguru - Senior React Developer ✓
21. sennder - Senior Full stack Engineer, Software Engineer II (Frontend) ✓
22. Promaton - Senior Frontend (React, TypeScript), Senior Full Stack (React, TypeScript, Node) ✓
23. Presspage - Senior backend/frontend/fullstack developer ✓
24. VEED - Senior FrontEnd Engineer, Senior Backend Engineer ✓
25. Modash - Senior Full-Stack Engineer ✓
26. Synthesia - Senior Backend and Fullstack Engineers ✓
27. Bird Buddy - Senior Full Stack Developer, Front-end Developer, React Native Developer ✓
28. Archive Resale - Backend Engineer, Frontend Engineer, Full Stack Engineer ✓
29. Motorway - Frontend and Backend Engineers (React/Node) ✓
30. Ebury - sr node js dev, full stack dev ✓
31. Tessian - Senior NodeJS Engineer, Senior Frontend Engineer ✓
32. Lepaya - Principal Engineer (node.js), Senior BackEnd Engineer (node.js) ✓
33. Loominate.app - Full Stack Engineer (node.js) ✓
34. MailOnline - JavaScript developer (node and react) ✓
35. Ping Identity - NodeJS Dev ✓
36.
37. Olo - Senior Backend Engineer (Node.js), Senior Full Stack Engineer (Node.js + Vue) ✓
38. Kodify Media Group - React Frontend, Node.js Backend and Fullstack engineers in MERN tech stack ✓
39. Around - Backend Engineer (must have 4+ yrs Node, TypeScript), FullStack Engineer (must 4+ yrs React, TypeScript, Node) ✓
40. Aiven - Backend engineers (python), but let me check... no specific match
41. Normative.io - Backend Engineer, Frontend Engineer ✓
42. Shop Apotheke - Senior Nodejs Developers, Senior Full-Stack ✓
43. Caribou Wealth - Intermediate & Senior Full Stack Engineers (React + Type Script) ✓
44. Anyfin - Fullstack Developer, Backend Developer, Senior Backend Developer ✓
45. Crisp - Full-stack developers ✓
46. Australian Payment Plus - Back-End Developers (JS/TS) ✓
47. Feather - Frontend Engineer, Backend Engineer, Full Stack Engineer ✓
48. Simpplr - Back End (Node), Front End (React), Full Stack ✓
49. Circl Technologies - Frontend React Developers ✓
50. Busbud - Senior Engineer (Node.js mentioned in URL) ✓
51. Reedsy - Senior Fullstack Engineer (NodeJS + VueJS) ✓
52. Cleo - React/React Native Engineers ✓

Continuing through the next batch: Napo has senior backend roles, Instapro Group offers lead frontend (React) and senior backend positions, GoCardless and Vinted both have engineering openings across backend and frontend. Prezi, Normative, and Around all match the criteria with Around specifically listing Node/TypeScript backend and React fullstack roles. Transfergo's PHP backend position doesn't fit, Stacksocial doesn't qualify, but Omnipresent has a full stack JS engineer role. Still evaluating Vodoo and vidiq's frontend React position.

Moving forward, Appfolio, Concord Labs (TypeScript/NextJS fullstack), and Huckleberry Labs all work. FloSports has product engineering roles with Node/NestJS/TypeScript, giffgaff offers senior positions across multiple specialties, Toggl has frontend openings, and Unbabel provides senior-level backend and frontend roles. ResearchGate's React/PHP fullstack engineer matches, and Concord Labs appears again with another fullstack opportunity.

Continuing down the list: Inter-university Consortium has React/Node senior roles, Milk Moovement seeks fullstack engineers with JavaScript, Kilo Health covers frontend React, React Native mobile, and backend positions. Creative Fabrica offers React frontend roles alongside PHP/Go backend positions, Flyr Labs has React developer and fullstack openings, and PandaDoc specifically seeks senior React frontend engineers. Flink provides flexibility across backend, frontend, and fullstack tracks, while TransferRoom has fullstack opportunities.

Moving forward, Thinslices is hiring Node backend and fullstack JavaScript developers, Schibsted has both frontend and fullstack positions available, Starburst and Retool are recruiting software engineers and frontend engineers respectively. Braze and Cloudflare are hiring software engineers and engineering managers. Olo stands out with Node.js backend roles, fullstack .NET/JavaScript positions, and senior engineers combining Node.js with Vue. Ready Player Me is looking for fullstack developers.

Monday.com, Axoni (specifically React developers), Andela, Formitable, Envoy, GoodData, Docplanner, Choco Communications, GetYourGuide, Katanox, Seenons, and College Board all have open positions across backend, frontend, and fullstack engineering roles. College Board particularly emphasizes JavaScript/TypeScript and Node with React experience.

Continuing through the list: Pento seeks a Principal Backend Engineer, while Hightouch and Appsmith focus on senior-level backend and frontend positions respectively. Kinsta is actively hiring JavaScript developers at senior levels. Immigo needs a Founding Senior Front-end Engineer, and Caribou Wealth is looking for fullstack engineers with React and TypeScript skills. Dishpatch, Wandelbots, Neo Financial, Dayshape, and Qogita round out the opportunities with various senior engineering and software developer roles.

Moving forward, Reactive has openings across the full spectrum from frontend to backend to fullstack positions. Gooddata, Stack Overflow, and Kaizen Gaming are hiring across multiple engineering levels. Planner 5D specifically wants fullstack web engineers with PHP, JavaScript, and TypeScript experience. CKSource, ResearchGate, ClickHouse, Metabase, Personio, and Procore all have senior fullstack or specialized backend/frontend engineering positions available, with several emphasizing React and Node.js stacks.

Now I'm seeing the list is becoming unwieldy. Let me distill this down to the companies that are most clearly aligned with the search criteria—those explicitly calling for fullstack engineers, frontend developers, backend developers, or mentioning JavaScript, React, and Node.js specifically. I'll organize these by category to make the list more actionable and easier to reference. - Schibsted (Full-stack)
- Retool (Software Engineer)
- Ready Player Me (Full-Stack)
- Formitable (Full-stack)
- GetYourGuide (full-stack)
- Seenons (Full Stack)
- Dishpatch (Full Stack)
- Stack Overflow (Full Stack Developers)
- Planner 5D (Full-stack Web Engineers: JavaScript, TypeScript)
- Andela (Full Stack)
- Choco Communications (Fullstack)
- Katanox (Frontend and Backend)
- Caribou Wealth (Full Stack React + TypeScript)
- Reactor (Full-Stack Developer)

**Node.js specifically:**
- Skyscanner (backend node.js)
- Garden (nodeJS)
- Ebury (sr node js dev)
- Veepee (Node

.js)
- Lepaya (node.js)
- Shop Apotheke (Senior Nodejs Developers)
- Olo (Node.js)
- Tessian (NodeJS)
- Loominate.app (Full Stack Engineer node.js)
- Around/Miro Labs (Node, TypeScript)
- Thinslices (BE Node)
- FloSports (NestJS, Node)
- Reedsy (NodeJS)
- Simpplr (Back End Node)
- Motorway (React/Node)
- Kodify (Node.js Backend)
- Ping Identity (NodeJS)
- College Board (Node)
- Procore (React and Nodejs)
- RapidAPI (Backend Engineer NodeJS)
- MailOnline (node and react)

**React specifically:**
- Netguru (Senior React Developer)
- Promaton (React, TypeScript)
- M&S (React/Next.js)
- Instapro Group (Lead Frontend React)
- Caribou Wealth (React + TypeScript)
- Circl Technologies (Frontend React)
- vidiq (react, TS)
- ResearchGate (FullStack React/PHP)
- Flyr labs (React Developer)
- PandaDoc (React)
- TransferRoom (React)
- Kilo Health (React)
- Creative Fabrica (Frontend React)
- Axoni (React.js)
- College Board (React)
- Motorway (React/Node)
- Around/Miro Labs (React, TypeScript, Node)
- Simpplr (Front End React)
- Kodify (React Frontend, MERN)
- MailOnline (Node and React)
- Procore (React and Node.js)
- Feather (Frontend)
- Cleo (React/React Native)

**JavaScript-focused roles:**
- Klarna, Omnipresent, Australian Payment Plus, Milk Moovement, Kinsta, RapidAPI, Veepee, College Board, and Planner 5D all have JavaScript or JavaScript/TypeScript positions available. Now I should organize these companies by the specific tech stacks and role types to create a cleaner, more useful reference.Here are all the companies from this data hiring for **Full Stack, Backend, Frontend, Node.js, JS, or React** roles:

---

## 🟢 Node.js Specific
| Company | Role | Location |
|---|---|---|
| **Skyscanner** | Backend Node.js | London, Barcelona, Edinburgh |
| **Garden** | Open Source Developer (NodeJS, Typescript) | Berlin / Remote GMT ±2 |
| **Ebury** | Sr Node JS Dev, Full Stack Dev | Remote |
| **RapidAPI** | Backend Engineer (NodeJS), JS Engineer | Berlin, SF, Tel Aviv |
| **Lepaya** | Principal Engineer (Node.js), Senior Backend (Node.js) | Amsterdam / Remote |
| **Shop Apotheke** | Senior Nodejs Developers, Senior Full-Stack | Germany / Remote |
| **Olo** | Senior Backend Engineer (Node.js), Full Stack (Node.js + Vue) | Remote US / NYC |
| **Tessian** | Senior NodeJS Engineer, Senior Frontend Engineer | UK Remote |
| **Loominate.app** | Full Stack Engineer (node.js) | Remote |
| **Around (Miro Labs)** | Backend Engineer (Node, TypeScript), FullStack (React, TypeScript, Node) | Remote PST-EEST |
| **Thinslices** | Javascript BE Node, Full Stack | Romania, Portugal |
| **FloSports** | Full Stack, NestJS/Node | Austin TX / Remote |
| **Simpplr** | Back End (Node), Front End (React), Full Stack | Toronto, Brighton, Bengaluru |
| **Motorway** | Frontend & Backend (React/Node) | London & Krakow |
| **Kodify Media Group** | React Frontend, Node.js Backend, Fullstack (MERN) | Remote Europe (CET ±2h) |
| **Ping Identity** | NodeJS Dev | US, India |
| **College Board** | Full Stack (JavaScript/TypeScript/Node/React) | 100% Remote US |
| **Procore** | Associate Manager (React and Nodejs) | Remote US |
| **Reedsy** | Senior Fullstack (NodeJS + VueJS) | Europe |
| **Veepee** | NodeJs, React, JS, Ts | Barcelona, Amsterdam, Paris |

---

## 🔵 React Specific
| Company | Role | Location |
|---|---|---|
| **Netguru** | Senior React Developer | Poland |
| **Promaton** | Senior Frontend (React, TS), Senior Full Stack (React, TypeScript, Node) | Remote Europe |
| **M&S** | React/Next.js Engineers | UK Remote |
| **Instapro Group** | Lead Frontend Developer (React) | UK, Netherlands, Germany |
| **Caribou Wealth** | Full Stack Engineers (React + TypeScript) | Canada, US |
| **Circl Technologies** | Frontend React Developers | Remote EU |
| **vidiq** | Frontend Engineer (React, TS) | Global Remote |
| **ResearchGate** | Senior FullStack Engineer React/PHP | Germany, UK, Poland |
| **Flyr Labs** | Full Stack Engineer, React Developer | Amsterdam, Krakow |
| **PandaDoc** | Senior Frontend Engineers (React) | Europe Timezones |
| **TransferRoom** | Frontend (React), Full Stack (.NET, React) | London, Ukraine, Poland |
| **Kilo Health** | Frontend (React), Mobile (React Native) | Europe |
| **Creative Fabrica** | Frontend Engineers (React) | Amsterdam |
| **Axoni** | Front End Developers (React.js) | Remote US |
| **Cleo** | React/React Native Engineers | London / UK Remote |
| **Around (Miro Labs)** | FullStack (React, TypeScript, Node) | Remote |
| **MailOnline** | JavaScript Developer (node and react) | London, Hybrid |
| **Feather** | Frontend, Backend, Full Stack | Europe Remote |
| **Andela** | Full Stack Engineer | LATAM |
| **Axoni** | Front End Developers (React.js) | Remote USA |

---

## 🟡 Full Stack
| Company | Role | Location |
|---|---|---|
| **Flexport** | Full-stack, Frontend, Backend | US, Netherlands |
| **Omnipresent** | Full Stack JS Engineer | Remote GMT ±3 |
| **Envoy** | Fullstack, Backend, Frontend | SF, NYC |
| **Modash** | Senior Full-Stack Engineer | GMT-2/+6 |
| **Humaans.io** | Software Engineering (Full Stack) | London |
| **Miro** | Software Engineer (Backend, Front, Fullstack) | Amsterdam, Berlin |
| **sennder** | Senior Full Stack Engineer | Berlin, Barcelona |
| **VEED** | Senior Frontend Engineer, Senior Backend Engineer | Remote EU |
| **Bird Buddy** | Senior Full Stack Developer, Front-end Developer | Europe, UK |
| **Archive Resale** | Backend, Frontend, Full Stack Engineer | LA, NYC, SF, Remote |
| **Synthesia** | Senior Backend and Fullstack Engineers | Remote UK/Europe/US East |
| **Normative.io** | Backend, Frontend Engineers | Sweden / EU Remote |
| **Prezi** | Full Stack Engineers | Remote EU |
| **Flink** | Backend / Frontend / Mobile / Fullstack | Berlin, Amsterdam |
| **giffgaff** | Senior Software Engineers (Backend, Frontend, Full Stack) | London / UK Remote |
| **Busbud** | Senior Full Stack Engineer | Montreal / NA / Western Europe |
| **GetYourGuide** | Full-stack, Backend Engineers | Berlin, Zurich |
| **Concord Labs** | Full-stack Engineer (TypeScript, NextJS) | Remote US |
| **Huckleberry Labs** | Full Stack Software Engineer | Remote USA |
| **Dishpatch** | Senior Full Stack Engineer, Frontend Engineer | GMT |
| **Formitable** | Full-stack engineer, Frontend engineer | Amsterdam |
| **Stack Overflow** | Full Stack Developers | Remote US, UK, Germany, Canada |
| **Ready Player Me** | Full-Stack Developers | Europe |
| **Katanox** | Frontend and Backend Engineers | Amsterdam / Remote EU |
| **Seenons** | Front End, Back End, Full Stack | Remote, Berlin, Amsterdam |
| **Reactor/Reaktor** | Full-Stack Developer | Amsterdam, Lisbon, Helsinki |
| **Milk Moovement** | Full Stack, Senior Full Stack (Javascript) | Remote US/Canada |
| **Choco Communications** | Backend, Fullstack | Berlin |
| **Schibsted** | Front-end (13 roles), Full-stack (10 roles) | Sweden, Denmark, Norway |
| **Retool** | Frontend Engineer, Software Engineer | SF Bay Area |
| **Apollo.io** | Frontend, Backend, Full-stack | Remote Worldwide |
| **Andela** | Backend Engineer, Full Stack Engineer | LATAM |

---

## 🟠 JS / JavaScript
| Company | Role | Location |
|---|---|---|
| **Klarna** | JavaScript (Backend and Frontend) | Stockholm, Berlin, Madrid |
| **Australian Payment Plus** | Back-End Developers (JS/TS) | Melbourne, Sydney |
| **Kinsta** | JavaScript Developer, Senior JavaScript Developer | Remote |
| **Planner 5D** | Full-stack Web (JavaScript, TypeScript) | Europe Remote |
| **Veepee** | NodeJs, React, Js, Ts | Barcelona, Amsterdam, Paris |
| **RapidAPI** | Sr. Software Engineer (JavaScript), Staff (JavaScript) | Berlin, SF, Tel Aviv |
| **College Board** | Full Stack (JavaScript/TypeScript) | Remote US |

---

## 🔴 Backend / Frontend (General)
| Company | Role | Location |
|---|---|---|
| **Uber** | Frontend SWE, Backend SWE | Amsterdam, Sofia, Aarhus |
| **Plain** | Senior Frontend, Senior Backend | Remote GMT ±2 |
| **Skyscanner** | Frontend web, Backend | London, Barcelona |
| **Treatwell** | Frontend, Backend, Fullstack | UK, Italy, Spain, Germany |
| **Presspage** | Senior backend/frontend/fullstack | Amsterdam |
| **Ebury** | Full Stack Dev, Sr Node JS Dev | Remote |
| **Cleo** | Backend (Ruby/Python), React/React Native | London / UK Remote |
| **Netguru** | Senior React Developer, Senior Java Developer | Poland |
| **Unbabel** | Senior Frontend Engineer, Senior Backend Engineer | Lisbon, Edinburgh |
| **Docplanner** | Frontend and Backend Engineers | Europe |
| **Feather** | Frontend, Backend, Full Stack | Europe Remote ±2h CET |
| **GoCardless** | Software Engineers | London |
| **Vinted** | BE, Frontend | Berlin, Vilnius |
| **Personio** | Backend/Frontend Engineers | Germany, UK, Spain |
| **TransferGo** | Backend software engineer (PHP) | Lithuania, Poland |
| **Ravio** | Frontend and Backend (React, Typescript, Nodejs) | UK Remote |
| **Motorway** | Frontend and Backend (React/Node) | London & Krakow |
| **AirHelp** | Software Engineers (Ruby, Go, Python, JS) | Krakow, Gdansk, Barcelona |

---

**Total: 80+ companies** actively hiring across these roles. The standout ones for your MERN stack background are:

- **Kodify** (MERN explicitly)
- **Around/Miro Labs** (React + Node + TypeScript)
- **Motorway** (React/Node)
- **College Board** (JS/Node/React)
- **RapidAPI** (NodeJS + JS)
- **Simpplr** (Node backend + React frontend)
- **Ravio** (React, TypeScript, Nodejs)

---
