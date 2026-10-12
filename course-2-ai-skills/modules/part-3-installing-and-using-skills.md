# Session 3: Installing & Using Skills — The Ecosystem

> **Target Duration:** 75–90 Minutes  
> **Audience:** Students who completed Sessions 1 & 2.  
> **Core Focus:** Skill discovery, local vs. global installation, natural intent triggering vs. explicit invocation, and verifying activation.

---

## 🎯 Learning Objectives
1. Understand the difference between **Project (Local) Skills** and **User (Global) Skills**.
2. Discover where to find pre-built community skills and industry skill packs.
3. Install a skill package into your agent workspace in under 60 seconds.
4. Trigger skills through both **Natural Intent Detection** and **Explicit Invocation**.
5. Verify that the agent actually consulted the skill before responding.

---

## 🖼️ Slide-by-Slide Presentation Guide

### Slide 3.1: The Skills App Store
- **Visual:** A modern app store or plugin marketplace mockup showing skill cards: "UI Design Auditor", "SEO Content Optimizer", "SQL Query Builder", "Legal Contract Summarizer".
- **Key Bullets:**
  - You don't have to build every skill from scratch.
  - A thriving global ecosystem of open-source and community skills already exists.
  - Installing a skill is as simple as copying a folder into your workspace!
- **Speaker Script:**
  > *"When you buy a smartphone, you don't write your own maps app or camera app from scratch. You install them from the app store. The AI world has reached that exact inflection point. Rather than inventing every prompt and rule yourself, you can install tested, production-grade skills created by world-class specialists."*

---

### Slide 3.2: Where Do Skills Live? (Local vs. Global)
- **Visual:** Diagram contrasting:
  - **Local (Project-Level):** Inside the project workspace (e.g. `my-project/.skills/` or `skills/`). Available only when working on this specific project.
  - **Global (User-Level):** Inside your user profile or root directory. Available across *all* projects you ever work on.
- **Key Bullets:**
  - **Use Local for:** Project-specific conventions, client brand guides, unique database schemas.
  - **Use Global for:** General superpowers you want everywhere (e.g., Code Reviewer, Tone Polisher, Markdown Formatter).
- **Speaker Script:**
  > *"Skills can live in two places. If a skill contains private client guidelines or rules specific to one web app, you put it in that project's folder. But if a skill is a general superpower—like your favorite writing coach or code auditor—you install it globally so it's ready in every project you ever open."*

---

### Slide 3.3: Two Ways to Wake Up a Skill
- **Visual:** Split screen:
  - **Left (Natural Intent Matching):** You type: *"Can you review this copy for brand voice?"* ➔ Agent's internal radar detects the keyword intent from the skill's description and automatically opens `SKILL.md`.
  - **Right (Explicit Invocation):** You type: *"Please activate the brand-voice skill and evaluate this text."*
- **Key Bullets:**
  - Modern agents auto-trigger skills based on the `description` metadata.
  - You can also explicitly name the skill if you want 100% guaranteed invocation.
- **Speaker Script:**
  > *"How does the agent know when to open the skill binder? There are two ways. Most of the time, it happens naturally: the agent compares your prompt to the skill descriptions and says, 'Aha! This user is asking for brand review, let me open the brand-voice skill.' But if you want to be completely sure, you can simply type: 'Use the brand-voice skill on this draft.'"*

---

### Slide 3.4: How to Know the Agent Actually Used Your Skill (The Verification Check)
- **Visual:** A magnifying glass inspecting the agent's thought process / execution log:
  `Step 1: Reading skill file file:///skills/brand-voice/SKILL.md -> Step 2: Applying 5 Brand Voice Rules -> Step 3: Producing Audit Table.`
- **Key Bullets:**
  - Never guess whether the agent used the skill.
  - Look for the file access step in the agent's thought log.
  - Skills should specify a signature output format (e.g. a unique header or scoring table) so you immediately see the skill's imprint.
- **Speaker Script:**
  > *"How can you prove the agent actually read your skill and didn't just hallucinate a generic response? Two ways: First, look at the agent's activity log—you will see it specifically inspect `SKILL.md`. Second, your skill should instruct the agent to produce a distinct signature header or rating rubric. If that rubric appears, you know the skill fired perfectly."*

---

### Slide 3.5: Live Demo — Installing a Community Skill in 60 Seconds
- **Instructor Action:**
  1. Show a folder containing a pre-made `landing-page-critique` skill.
  2. Drag and drop (or copy) the folder into the workspace's skills directory.
  3. Ask the agent: *"Critique this landing page hero section."*
  4. Show the agent automatically discovering the skill, reading `SKILL.md`, and returning the structured scorecard.
  5. Demonstrate explicit invocation: *"Now run the same text through the copywriting-polish skill."*

---

### Slide 3.6: Student Hands-On Lab (25 Minutes)
- **Student Mission:**
  1. Download or copy the pre-built `customer-persona-generator` skill from the workshop files.
  2. Place it into your workspace skills directory.
  3. Issue a natural prompt (e.g. *"Generate a buyer persona for a high-end coffee subscription"*).
  4. Verify that the agent triggered the skill and produced the exact structured persona card.
  5. Try triggering it with 2 different prompts to test the radar sensitivity.

---

### Slide 3.7: Session Wrap-Up & What's Next
- **Key Bullets:**
  - Installing skills takes seconds: it's just copying a folder.
  - Skills trigger automatically via intent matching or explicit requests.
  - **Coming in Session 4:** The real magic! We will learn how to turn your own unique expertise and business workflows into a brand-new custom skill from scratch.
