# Session 5: Testing, Refining & Team Workflows — Scaling Skills

> **Target Duration:** 75–90 Minutes  
> **Audience:** Students who completed Sessions 1–4.  
> **Core Focus:** Debugging skills, handling edge cases, sharing skills across teams via Git, and presenting capstone skills.

---

## 🎯 Learning Objectives
1. Diagnose and fix the two classic skill bugs: **Under-triggering** and **Over-triggering**.
2. Master the **Negative Constraint Technique** to prevent agents from ignoring critical rules.
3. Package and distribute skills across teams using version control and shared repositories.
4. Present a working, validated custom skill in the live capstone showcase.

---

## 🖼️ Slide-by-Slide Presentation Guide

### Slide 5.1: The Polish Phase — From Prototype to Production
- **Visual:** A quality control inspector testing a skill cartridge with a magnifying glass and digital diagnostic screen.
- **Key Bullets:**
  - Writing the first draft of a skill is easy.
  - Making it bulletproof across edge cases and diverse team members is what makes it a real tool.
  - Today, we stress-test our skills and prepare them for production sharing.
- **Speaker Script:**
  > *"Welcome to our capstone session! Anyone can write a quick instruction file. But a truly world-class skill works reliably every single time, regardless of whether a senior manager, an intern, or a customer prompts it. Today, we learn how to debug skills, eliminate edge-case failures, and share them across our entire organization."*

---

### Slide 5.2: The Two Classic Skill Bugs
- **Visual:** A scale showing:
  - **Left (Under-Triggering / The Sleeper):** The skill never activates when you want it to. Cause: Description lacks specific verbs or is too narrow.
  - **Right (Over-Triggering / The Eager Beaver):** The skill activates even when you just say "Hello" or ask an unrelated question. Cause: Description is too generic (e.g. "Helps with all text").
- **Key Bullets:**
  - Tuning the radar description is an iterative science.
  - Test with at least 3 positive test prompts and 2 negative test prompts.
- **Speaker Script:**
  > *"There are two primary bugs in skill engineering. Bug #1 is Under-Triggering: you ask for a report, but the agent ignores the skill and gives a generic answer. Bug #2 is Over-Triggering: the agent jumps in like an eager beaver on every single conversation. We fix this by fine-tuning the description keywords."*

---

### Slide 5.3: The "Negative Constraint" Technique (Fixing Rule Evasion)
- **Visual:** A brick wall stopping the agent from wandering off.
  - *Weak:* "Try to keep the summary short."
  - *Bulletproof:* "CRITICAL CONSTRAINT: You MUST NOT exceed 3 bullet points per section. If an explanation is longer than 50 words, reject it and condense."
- **Key Bullets:**
  - LLMs are eager to please and tend to be verbose.
  - Use explicit uppercase constraints: `MUST`, `MUST NOT`, `NEVER`.
  - Provide an error-handling rule for invalid inputs.
- **Speaker Script:**
  > *"If an agent is ignoring one of your rules, gentle phrasing won't work. Don't say 'Please try to be brief.' Say: 'STRICT CONSTRAINT: You MUST NOT write more than three bullets.' High-contrast negative constraints give LLMs unambiguous guardrails."*

---

### Slide 5.4: Sharing Skills Across Teams (The Company Skill Library)
- **Visual:** A team repository in Git with multiple developers pulling the latest skill updates into their daily workflows.
- **Key Bullets:**
  - Skills are plain text and markdown—meaning they live perfectly inside Git!
  - When you update `SKILL.md` in the central repo, your entire team's agents instantly inherit the new rules.
  - No more distributing 10-page PDF guidelines that no one reads.
- **Speaker Script:**
  > *"Here is why enterprise companies are falling in love with agent skills: Instead of emailing around a 20-page style guide that sits unread in Google Drive, you commit a single `SKILL.md` to your team repository. Instantly, every developer, marketer, and product manager on your team has an AI agent that automatically enforces those exact standards."*

---

### Slide 5.5: Live Demo — Debugging & Tuning a Skill Live
- **Instructor Action:**
  1. Take a deliberately buggy skill with an over-broad description.
  2. Ask an unrelated question and show it mistakenly activating.
  3. Edit the description in real time to narrow its scope.
  4. Test again: show it ignoring the unrelated prompt, but triggering instantly on the target prompt.
  5. Demonstrate adding a negative constraint and verifying strict adherence.

---

### Slide 5.6: Capstone Showcase & Graduation (30 Minutes)
- **Student Showcase:**
  - Each student presents their custom skill in a 2-minute lightning demo:
    1. *What domain problem does your skill solve?*
    2. *Show the `SKILL.md` frontmatter and key rules.*
    3. *Run a live test with your agent and showcase the structured output!*

---

### Slide 5.7: The Future of Agentic Work
- **Key Bullets:**
  - You now know how to build apps (Course 1) AND equip agents with specialized intelligence (Course 2).
  - You have transformed from a prompt user into an **AI Systems Architect**.
  - Keep building, sharing, and expanding your personal skill library!
