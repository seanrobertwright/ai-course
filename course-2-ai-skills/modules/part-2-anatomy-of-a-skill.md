# Session 2: The Anatomy of a Skill — Under the Hood

> **Target Duration:** 75–90 Minutes  
> **Audience:** Students who completed Session 1.  
> **Core Focus:** Dissecting the structure of a skill folder, `SKILL.md`, YAML frontmatter, and progressive disclosure.

---

## 🎯 Learning Objectives
1. Explain the standard directory layout of a modern AI skill folder.
2. Master the anatomy of `SKILL.md`: YAML Frontmatter vs. Markdown Body.
3. Understand how AI agents use the `description` field as an **Intent Radar** for dynamic activation.
4. Grasp the engineering principle of **Progressive Disclosure** (keeping agent context windows lean).

---

## 🖼️ Slide-by-Slide Presentation Guide

### Slide 2.1: Opening the Skill Cartridge
- **Visual:** A retro game cartridge splitting open to reveal a circuit board: labeled "Metadata (Radar)", "Core Instructions (The Brain)", and "Auxiliary Tools (Scripts & References)".
- **Key Bullets:**
  - In Session 1, we learned that skills give agents superpowers.
  - Today, we inspect the engineering behind the cartridge.
  - A skill is simply an organized folder with standard files—nothing mysterious!
- **Speaker Script:**
  > *"When you play a video game, you plug in a cartridge. Inside that cartridge is game code, graphics, and music. In the AI agent world, a skill is just a neatly organized folder containing a special instruction file called SKILL.md and optional helper folders. Today, we're opening up the cartridge so you understand every single moving part."*

---

### Slide 2.2: The Standard Skill Folder Architecture
- **Visual:** An illustrated folder tree diagram:
  ```text
  my-custom-skill/
  ├── SKILL.md           # The Master Blueprint (Required)
  ├── scripts/           # Executable helper scripts (Python/JS/Shell)
  ├── templates/         # Boilerplates, starter documents, markdown forms
  ├── references/        # Deep reference docs, style guides, glossaries
  └── examples/          # Sample inputs and expected golden outputs
  ```
- **Key Bullets:**
  - `SKILL.md` is the only mandatory file; everything else is optional.
  - Keep related assets organized in dedicated subdirectories.
  - Agents can read from `references/` or run files in `scripts/` when needed.
- **Speaker Script:**
  > *"Here is the standard skill layout recognized by agent systems worldwide. At the root is SKILL.md—this is the master blueprint. If your skill needs a Python script to calculate statistics, it lives in `scripts/`. If it needs a company brand template, it lives in `templates/`. It's clean, predictable, and modular."*

---

### Slide 2.3: Deconstructing SKILL.md (Part 1: The YAML Frontmatter)
- **Visual:** Code snippet with clear callouts highlighting the top lines between `---` markers:
  ```yaml
  ---
  name: brand-voice-editor
  description: Audits written articles and landing pages against official company brand guidelines. Use whenever the user asks to polish copy, check brand tone, or review marketing material.
  ---
  ```
- **Key Bullets:**
  - **YAML Frontmatter:** The metadata header at the very top of the file, fenced by three dashes `---`.
  - **`name`:** A unique, lowercase hyphenated identifier (e.g. `brand-voice-editor`).
  - **`description`:** The most critical sentence in the entire skill!
- **Speaker Script:**
  > *"At the very top of SKILL.md, between two lines of triple dashes, is the YAML Frontmatter. You only need two fields: name and description. But let me emphasize this: the `description` is the most important sentence you will ever write. It acts as the agent's radar. It tells the agent: 'Here is what I do, and here is exactly WHEN you should wake me up.'"*

---

### Slide 2.4: Progressive Disclosure (Why Skills Don't Slow Down Your AI)
- **Visual:** A two-stage funnel:
  - **Stage 1 (Idle):** Agent context loads *only* the 2-sentence description (~30 tokens). Lean, cheap, blazing fast.
  - **Stage 2 (Triggered):** User says "Check this blog post for tone." The agent matches the intent, opens `SKILL.md`, and reads the full 300-word SOP.
- **Key Bullets:**
  - If you paste 20 mega-prompts into an AI, it forgets and slows down.
  - With **Progressive Disclosure**, you can install 50 different skills without degrading performance!
  - The full skill is loaded *just-in-time*, only when needed.
- **Speaker Script:**
  > *"How can an agent have 50 different skills installed without slowing down to a crawl? The secret is Progressive Disclosure. When the agent boots up, it doesn't read all 50 manuals. It only glances at the 2-sentence descriptions on the front cover. Only when you ask for something related to that topic does the agent pull the full manual off the shelf."*

---

### Slide 2.5: Deconstructing SKILL.md (Part 2: The Instruction Body)
- **Visual:** Highlighting the markdown sections under the frontmatter:
  - **# Overview:** What this skill accomplishes.
  - **## Step-by-Step Workflow:** 1. Analyze input, 2. Check rules, 3. Format output.
  - **## Rules & Standards:** Strict do's and don'ts.
  - **## Output Template:** The exact markdown table or structure to produce.
- **Speaker Script:**
  > *"Below the frontmatter is standard GitHub-flavored Markdown. You write clear, numbered procedural steps. Give the agent a rigid output format—like a markdown table or callout box—so the final result looks pristine and consistent every single time."*

---

### Slide 2.6: Live Demo — Inspecting a Live Skill
- **Instructor Action:**
  1. Open an existing production skill in the workspace (e.g., a style-checker or PRD-generator).
  2. Walk through the YAML frontmatter.
  3. Show how the instructions guide the agent step-by-step.
  4. Open the `references/` subfolder and show how the agent can cite supporting files.
  5. Trigger the skill live by typing a prompt matching the description.

---

### Slide 2.7: Student Hands-On Lab (25 Minutes)
- **Student Mission:**
  1. Open the sample skill template provided in your workbook.
  2. Identify the YAML frontmatter (`name` and `description`).
  3. Tweak the `description` to make it more specific.
  4. Add one new strict rule to the **## Rules & Standards** section.
  5. Test it with your agent to observe the rule being enforced live!

---

### Slide 2.8: Session Wrap-Up & What's Next
- **Key Bullets:**
  - A skill is a folder with `SKILL.md` + optional scripts/references.
  - YAML frontmatter tells the agent *when* to trigger.
  - Progressive disclosure keeps context lean and fast.
  - **Coming in Session 3:** How to find, install, and run existing community skills in your agent workspace!
