# 📘 Zero to Builder: Student Handbook & Lab Workbook

> **Welcome to the Builder Era!**  
> *Zero coding required. Zero prior AI experience needed.*  
> This workbook is your personal guide for all 6 live sessions. Use it to follow along, copy starter prompt templates, track your progress checklists, and document your creations.

---

## 🚀 Pre-Course Onboarding: Your 3-Minute Setup

Before Session 1 begins, complete these two simple steps:

1. **Create your free account:**
   - Go to [replit.com](https://replit.com) in Google Chrome, Safari, Edge, or Brave.
   - Click **Sign Up** (you can sign up with Google, GitHub, or an email address).
2. **Bookmark your workspace:**
   - You don't need to install VS Code, Python, Git, or terminal software. Everything we do happens inside your web browser.

---

## 📑 Table of Contents

- [Session 1: Your First App in 20 Minutes](#session-1-your-first-app-in-20-minutes)
- [Session 2: The C.A.R.E. Prompting Blueprint](#session-2-the-care-prompting-blueprint)
- [Session 3: Peeking Under the Hood (Safe Code Customization)](#session-3-peeking-under-the-hood-safe-code-customization)
- [Session 4: Giving Your App a Brain (Replit Built-In AI)](#session-4-giving-your-app-a-brain-replit-built-in-ai)
- [Session 5: Databases & Memory (Apps That Remember)](#session-5-databases--memory-apps-that-remember)
- [Session 6: Launching, Debugging & Capstone Showcase](#session-6-launching-debugging--capstone-showcase)
- [Appendix A: The "Zero-Panic" Troubleshooting Protocol](#appendix-a-the-zero-panic-troubleshooting-protocol)
- [Appendix B: Plain-English Tech Glossary](#appendix-b-plain-english-tech-glossary)

---

## Session 1: Your First App in 20 Minutes

### 🎯 Session Goal
Experience the thrill of autonomous creation. Describe an interactive tool in plain English and see it running live in minutes.

### 📝 Lab Starter Prompts (Choose One)

#### Option A: Lunch Roulette / Decision Spinner
```text
Build a modern, friendly web app called "Lunch Roulette". 
Allow users to type restaurant names into an input box to add them to a list. 
Include a big, colorful "Spin" button that randomly selects one restaurant with a spinning animation, highlights the winner in a card, and triggers a celebratory confetti burst. 
Give it a clean mobile-friendly design with light and dark mode.
```

#### Option B: Tip & Bill Splitter
```text
Build a sleek, easy-to-use "Smart Tip & Bill Splitter" web app. 
Let users enter the total bill amount, choose a tip percentage (15%, 18%, 20%, or custom), and choose the number of people splitting the bill. 
Instantly calculate and display: total tip, total bill with tip, and amount owed per person. 
Give it large readable numbers and a modern card layout.
```

#### Option C: Daily Affirmation & Mood Boost
```text
Build a soothing web app called "Daily Mood Boost". 
Let users select how they are feeling today from 5 mood buttons (e.g., Stressed, Tired, Motivated, Anxious, Grateful). 
When clicked, show an uplifting quote, a 60-second animated breathing circle, and a gentle soothing pastel background.
```

### ✅ 25-Minute Lab Checklist
- [ ] Paste your chosen prompt into Replit Agent chat.
- [ ] Watch the agent plan, install files, and display the live preview.
- [ ] Test the interactive buttons on your screen.
- [ ] Scan or open the live preview link on your mobile phone.
- [ ] Paste your app link in the live workshop chat!

---

## Session 2: The C.A.R.E. Prompting Blueprint

### 🎯 Session Goal
Think like a Product Manager. Direct the agent using the C.A.R.E. framework and build in layered sprints rather than asking for 20 features all at once.

### 📐 The C.A.R.E. Spec Worksheet

When creating your next app, fill out this 4-step blueprint:

| Component | Question to Answer | Your Notes / Spec |
| :--- | :--- | :--- |
| **C — Context** | Who is this app for? What problem does it solve? | *e.g., "A daily habit tracker for busy professionals who want to build consistency."* |
| **A — Action** | What is the primary action the user takes? | *e.g., "User types a habit name, clicks 'Add', and checks a box when completed today."* |
| **R — Rules** | What must happen? What must NOT happen? | *e.g., "Show a streak fire counter. If unchecked, streak remains. Progress bar reaches 100% when all habits are done."* |
| **E — Experience** | What should the visual design and tone look like? | *e.g., "Minimalist slate dark mode with emerald green accents and smooth button animations."* |

### 🏃 Sprint-by-Sprint Iteration Plan
1. **Sprint 1 (Core Engine):** Build the basic inputs, buttons, and display. Test that the logic works.
2. **Sprint 2 (Polish & Layout):** Ask: *"Change the color theme to dark mode with emerald green buttons, add sound effects when completing a task, and ensure it looks great on mobile."*
3. **Sprint 3 (Power Feature):** Ask: *"Add a weekly progress summary bar at the top and an export button."*

---

## Session 3: Peeking Under the Hood (Safe Code Customization)

### 🎯 Session Goal
Learn to navigate the Replit file tree without fear. Make safe direct text and color edits, and discover the "Hybrid Workflow" (direct edits + agent direction).

### 🔍 File Navigation Cheat Sheet

| File Name | Plain-English Role | What You Can Safely Edit |
| :--- | :--- | :--- |
| `App.tsx` / `index.html` | The Floor Plan | Headlines, subtitles, button labels, and placeholder text inside quotes `"..."`. |
| `style.css` / Tailwind classes | The Paint & Interior Design | Color names (e.g. `bg-blue-600` ➔ `bg-purple-600`), font sizes (`text-lg`), padding. |
| `server.py` / `index.ts` | The Kitchen Engine | Leave for the agent unless instructed! Handles server logic and routing. |

### 🛠️ Safe Hands-On Exercise
1. **Switch to Code Editor View:** Click the file explorer icon on the left panel in Replit.
2. **Find Your Headline:** Open `App.tsx` or `index.html`. Press `Ctrl+F` (or `Cmd+F` on Mac) and search for the main title on your screen.
3. **Make the Edit:** Change the text inside the quotes to your own customized phrase.
4. **Hit Save (`Ctrl+S` / `Cmd+S`):** Look at the preview—it updates instantly!
5. **The Safety Net:** If you make a mistake, simply press `Ctrl+Z` (Undo) or click the **History (Clock)** icon at the top of Replit to roll back to any previous checkpoint.

---

## Session 4: Giving Your App a Brain (Replit Built-In AI)

### 🎯 Session Goal
Transform static apps into intelligent thinking tools using Replit's built-in AI. Zero external credit cards or API keys needed!

### 🧠 The "Prompt Inside a Prompt" Recipe

When prompting Replit Agent to connect the built-in AI, specify both the **App Action** and the **Internal Persona**:

```text
Build a web application called "The Pitch Doctor". 
The user pastes a 2-sentence business pitch into a text area and chooses a review persona:
- "Brutal Venture Capitalist" (Tough, numbers-driven, skeptical)
- "Empathetic Founder Coach" (Warm, encouraging, actionable)
- "Curious 10-Year-Old" (Simple, fun, jargon-free)

When the user clicks "Review Pitch", send the pitch to Replit's built-in AI model. 
Instruct the AI to return:
1. A Score out of 10
2. Three specific strengths
3. Three brutal areas for improvement

Display the response in a styled card with high contrast.
```

### ✅ Verification Checklist
- [ ] Prompt Replit Agent with the persona guidelines.
- [ ] Submit a test input (e.g. *"Uber for dog walking with GPS collars"*).
- [ ] Verify that the AI analyzes the input and displays structured feedback.
- [ ] Try switching personas to confirm the tone changes!

---

## Session 5: Databases & Memory (Apps That Remember)

### 🎯 Session Goal
Give your application permanent memory. Save user submissions into a cloud database so that refreshing the page never erases data.

### 📊 The Database Mental Model

Think of a database as a cloud-hosted Google Sheet:
- **Table:** A tab in the spreadsheet (e.g., `Reviews` or `Habits`).
- **Columns:** The headers (`id`, `title`, `score`, `feedback`, `created_at`).
- **Rows:** Every time a user submits your form, a new row is added.

### 📝 Prompt Template to Add Persistence
```text
Please add a persistent database to save every generated review. 
Create a table that stores:
- Original submission text
- Selected persona
- AI score and feedback
- Submission timestamp

Below the main form, add a "Recent Reviews Gallery" that lists all previous submissions from the database. 
Add an interactive "Upvote / Heart" button to each card, and allow users to sort the feed by "Most Upvoted" or "Newest".
```

### 🧪 The Ultimate "Refresh Test"
1. Type a new submission into your app and submit it.
2. Confirm it appears in the gallery below.
3. Close the browser tab completely.
4. Re-open the URL (or open it on your phone or in an incognito window).
5. **Success Milestone:** Your data is still there!

---

## Session 6: Launching, Debugging & Capstone Showcase

### 🎯 Session Goal
Conquer errors calmly, deploy your application to permanent production cloud hosting, and present your capstone creation.

### 🚀 Production Deployment Checklist
- [ ] Click the **Deploy** button in the top-right corner of Replit.
- [ ] Select **Autoscale Deployment** (or Static Deployment for simple web apps).
- [ ] Click **Deploy Now**.
- [ ] Copy your live production URL (e.g., `https://your-app-name.replit.app`).
- [ ] Test the link on your phone.
- [ ] Optional: Follow the prompts in Replit to connect a custom domain (e.g., `www.mycoolapp.com`).

### 🎤 2-Minute Capstone Presentation Script
When it is your turn to share in the live workshop, use this simple format:
1. **The Hook (15 secs):** *"Hi everyone, my name is [Name], and I built [App Name]."*
2. **The Problem (30 secs):** *"I created this because [problem it solves for users]."*
3. **The Live Demo (45 secs):** *"Let me show you how it works: I input X, click Y, and the AI generates Z. And notice here that it saves permanently to the database."*
4. **The Big Takeaway (30 secs):** *"Before this workshop, I had zero coding experience. The most surprising part of using Replit Agent was [your favorite insight]."*

---

## Appendix A: The "Zero-Panic" Troubleshooting Protocol

If an error message appears, follow this 3-step checklist:

1. **Step 1: Don't Panic.** Red text in a console is simply a clue, not a failure.
2. **Step 2: Copy the Error.** Copy the red text from the Replit console or preview banner.
3. **Step 3: Feed It to the Agent:**
   > *"I received this error when clicking 'Submit': [paste error]. Please explain what went wrong and fix the code."*
4. **Step 4: The Checkpoint Rewind (Safety Net):** If the agent gets confused, click the **History (Clock)** icon at the top of Replit and roll back to the version from 10 minutes ago.

---

## Appendix B: Plain-English Tech Glossary

- **AI Agent:** An autonomous AI system that doesn't just chat, but can create files, run code, and fix errors.
- **Frontend:** The "dining room" of your app—everything the user sees, clicks, and touches on their screen.
- **Backend:** The "kitchen" of your app—the server that runs computations, manages security, and talks to databases.
- **API (Application Programming Interface):** A digital waiter that carries requests between your app and external AI supercomputers.
- **Database:** A permanent cloud spreadsheet that stores user data so it never disappears on page refresh.
- **Deployment:** Moving your app from your private workbench onto high-speed 24/7 cloud servers for the public web.
- **MVP (Minimum Viable Product):** The simplest possible version of your idea that works. Always build this first!
