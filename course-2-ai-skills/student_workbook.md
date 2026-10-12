# 📘 Course 2 Student Handbook & Lab Workbook
# Supercharging AI Agents with Skills

> **From Prompts to Reusable Superpowers**  
> This workbook is your hands-on guide for all 5 sessions of Course 2. Use it during live lab sprints to inspect code, author custom `SKILL.md` files, and document your agent superpowers.

---

## 📑 Table of Contents
- [Session 1: The Prompt vs. Skill Benchmark](#session-1-the-prompt-vs-skill-benchmark)
- [Session 2: Dissecting the Skill Anatomy](#session-2-dissecting-the-skill-anatomy)
- [Session 3: Installing & Triggering Community Skills](#session-3-installing--triggering-community-skills)
- [Session 4: Authoring Your Custom Domain Skill](#session-4-authoring-your-custom-domain-skill)
- [Session 5: Debugging, Tuning & Capstone Showcase](#session-5-debugging-tuning--capstone-showcase)
- [Appendix: Standard Skill Boilerplate Template](#appendix-standard-skill-boilerplate-template)

---

## Session 1: The Prompt vs. Skill Benchmark

### 🎯 Objective
Experience firsthand how a skill-equipped agent outperforms a standard, vanilla conversational prompt in structure, rigor, and depth.

### 🧪 Benchmark Experiment Worksheet

1. **Test A (Vanilla Agent):**
   - Open your AI Agent. Do not activate any skills.
   - Enter this prompt:
     ```text
     Review this landing page headline: "We make software that helps your business grow faster." 
     Give me feedback on how to improve it.
     ```
   - *Observation Notes:* How generic was the response? Did it give structured evaluation criteria or just casual opinions?

2. **Test B (Skill-Equipped Agent):**
   - Activate the `conversion-copy-audit` skill.
   - Re-enter the exact same prompt:
     ```text
     Review this landing page headline: "We make software that helps your business grow faster." 
     Give me feedback on how to improve it.
     ```
   - *Observation Notes:* Notice how the skill automatically applied a 7-point conversion rubric, scored clarity out of 10, and gave 3 distinct formula rewrites.

---

## Session 2: Dissecting the Skill Anatomy

### 🎯 Objective
Understand the file architecture of a skill folder and master YAML frontmatter.

### 📐 Anatomy Diagram & Inspection
```text
my-custom-skill/
├── SKILL.md           <-- The Master Blueprint (Required)
├── scripts/           <-- Helper scripts (Python, JS, Bash)
├── templates/         <-- Document boilerplates & forms
└── references/        <-- Style guides, rubrics, glossaries
```

### 🔍 SKILL.md Deconstruction Checklist
Open `starter-skills/conversion-copy-audit/SKILL.md` and verify each section:
- [ ] **YAML Frontmatter:** Fenced by `---` with `name` and `description`.
- [ ] **The Intent Radar:** Does the `description` clearly explain both *what* it does and *when* to wake up?
- [ ] **Procedural Workflow:** Numbered, sequential steps for the agent to follow.
- [ ] **Strict Guardrails:** Explicit rules using uppercase constraints (`MUST`, `MUST NOT`).
- [ ] **Output Shape:** Markdown template or rubric table.

---

## Session 3: Installing & Triggering Community Skills

### 🎯 Objective
Install a pre-built skill folder into your workspace and practice both **Natural Intent Triggering** and **Explicit Invocation**.

### 🛠️ 3-Step Installation Guide
1. Copy the skill folder (e.g. `customer-persona-generator`) into your project's `skills/` directory.
2. Verify that `SKILL.md` exists at `skills/customer-persona-generator/SKILL.md`.
3. Start a new agent session.

### 🎮 Dual-Triggering Lab
- **Method 1: Natural Intent Trigger:**
  ```text
  Can you generate a detailed buyer persona for a high-end specialty coffee brand?
  ```
  *(Check agent thought log: Did it automatically load `SKILL.md` based on description keywords?)*
- **Method 2: Explicit Invocation:**
  ```text
  Please run the customer-persona-generator skill to map out our ideal enterprise customer profile.
  ```

---

## Session 4: Authoring Your Custom Domain Skill

### 🎯 Objective
Extract your own domain expertise and author a production-ready `SKILL.md` from scratch.

### 📝 The 4-Step Authoring Canvas

Fill out this worksheet before writing your file:

| Section | Your Skill Planning Notes |
| :--- | :--- |
| **Skill Name** | *Lowercase hyphenated, e.g. `executive-brief-generator`* |
| **Radar Description** | *Sentence 1 (What): Formats updates into Minto Pyramid style.<br>Sentence 2 (When): Use whenever user asks to summarize updates for executives.* |
| **Step 1 (Analyze)** | *What should the agent inspect first?* |
| **Step 2 (Apply)** | *What framework, formula, or checklist must it apply?* |
| **Step 3 (Format)** | *What structure must the final output take?* |
| **Strict Constraints** | *What is the agent NEVER allowed to do? (e.g., "Max 3 bullets per section")* |

---

## Session 5: Debugging, Tuning & Capstone Showcase

### 🎯 Objective
Test your custom skill against positive and negative edge cases, eliminate trigger bugs, and deliver your graduation demo.

### 🧪 Stress-Test Matrix
Test your skill with these 3 prompts:
1. **Target Prompt (Should Trigger):** A clear request matching your skill's domain.
2. **Subtle Prompt (Should Trigger):** A casual or brief phrase to verify the radar catches intent.
3. **Negative Prompt (Must NOT Trigger):** An unrelated request (e.g., asking for a spaghetti recipe). Confirm the agent does *not* load this skill!

### 🎤 2-Minute Capstone Showcase Script
1. **Introduction (20s):** *"Hi, I'm [Name]. I built the [Skill Name] skill to solve [specific business problem]."*
2. **The Blueprint (40s):** *"Here is my SKILL.md. Notice how the description triggers on [keywords], and enforces these 2 non-negotiable rules..."*
3. **The Live Demo (40s):** *"Watch what happens when I give it this messy input: [Show structured output]."*
4. **Key Takeaway (20s):** *"Turning this into a reusable skill saves me [X hours/week] and ensures consistent quality every time."*

---

## Appendix: Standard Skill Boilerplate Template

Copy and paste this starter skeleton when creating any new skill:

```markdown
---
name: your-skill-name
description: A clear 1-2 sentence description explaining what this skill does and exactly WHEN the agent should trigger it. Use whenever the user asks to [action 1], [action 2], or [action 3].
---

# Your Skill Name

Briefly describe the purpose, role, and philosophy of this skill.

## Step-by-Step Workflow

1. **Step 1: Input Analysis**
   - Inspect the user's provided input for [key criteria].
   - If critical information is missing, ask 1 focused clarifying question.

2. **Step 2: Processing & Transformation**
   - Apply [specific methodology, rubric, or formula].
   - Evaluate against [quality criteria].

3. **Step 3: Output Formatting**
   - Structure the deliverable using the Output Template below.

## Rules & Constraints

- **STRICT CONSTRAINT:** You MUST NOT [disallowed behavior].
- **RULE:** Keep all explanations concise and actionable.
- **STYLE:** Maintain a [professional / encouraging / rigorous] tone.

## Output Template

Always format the final output using this structure:

### 📋 Executive Summary
[1-2 sentence high-level summary]

### 🎯 Key Actions / Recommendations
- **Item 1:** [Actionable recommendation]
- **Item 2:** [Actionable recommendation]
- **Item 3:** [Actionable recommendation]
```
