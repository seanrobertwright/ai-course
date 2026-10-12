# Session 4: Authoring Custom Skills — Building Your Own Superpowers

> **Target Duration:** 75–90 Minutes  
> **Audience:** Students who completed Sessions 1–3.  
> **Core Focus:** Turning domain expertise and repetitive workflows into custom, production-ready AI skills.

---

## 🎯 Learning Objectives
1. Identify high-value **"Skill Opportunities"** in your daily work or company processes.
2. Master the **4-Step Skill Authoring Framework** (Trigger, Workflow, Rules, Output Shape).
3. Write high-precision `description` trigger copy that avoids false triggers.
4. Author, package, and test your first custom skill from a blank document.

---

## 🖼️ Slide-by-Slide Presentation Guide

### Slide 4.1: From Skill Consumer to Skill Creator
- **Visual:** A creator at a drafting table designing a glowing skill cartridge with their own logo on it.
- **Key Bullets:**
  - Up until now, we've used pre-built skills.
  - Today, you become an **AI Toolmaker**.
  - Your unique real-world experience—in business, marketing, design, education, or healthcare—is your greatest competitive advantage.
- **Speaker Script:**
  > *"Anyone can use an off-the-shelf AI prompt. But the people who create real, lasting value are the toolmakers. Today, you are going to take the specialized knowledge in your head—your taste, your company's rules, your quality standards—and freeze it into a reusable digital asset that any AI agent can execute forever."*

---

### Slide 4.2: Finding Your First "Skill Opportunity"
- **Visual:** A 3-box filter for identifying great skill candidates:
  - **Box 1 (Repetitive):** Any task you find yourself explaining to colleagues or AI more than twice a week.
  - **Box 2 (Tribal Knowledge):** Company checklists, unwritten style rules, or quality rubrics.
  - **Box 3 (High Stakes):** Tasks where consistency matters (e.g. bug reviews, client email polish, legal disclaimers).
- **Key Bullets:**
  - Great ideas for your first skill:
    - *The Brand Voice Enforcer*
    - *The Meeting Notes Action-Item Synthesizer*
    - *The Code Quality & Accessibility Auditor*
    - *The User Interview Insight Extractor*
- **Speaker Script:**
  > *"How do you know what to turn into a skill? Look for friction in your work week. If you have an SOP document, an onboarding checklist, or something you find yourself correcting people on all the time, that is a prime candidate for a custom skill."*

---

### Slide 4.3: The 4-Step Skill Authoring Framework
- **Visual:** A 4-stage assembly line:
  1. **The Radar (Frontmatter):** Name + Description (When should it wake up?).
  2. **The Procedural Arc:** Step 1, Step 2, Step 3 (What exact actions does it take?).
  3. **The Non-Negotiable Guardrails:** Strict constraints (What must it never do?).
  4. **The Output Mold:** Markdown template (What should the finished deliverable look like?).
- **Speaker Script:**
  > *"Building a skill is like writing instructions for a top-tier assistant. Step 1: Tell it when to wake up. Step 2: Give it the step-by-step recipe. Step 3: Tell it what lines it cannot cross. Step 4: Show it an example of what a perfect finished product looks like."*

---

### Slide 4.4: The Art of the "Radar Description"
- **Visual:** Before-and-after description comparison:
  - ❌ *Weak & Vague:* `description: Helps with writing and editing.` (Will trigger constantly or never!)
  - ✅ *Precision Engineered:* `description: Formats, polishes, and scores executive email updates according to the Minto Pyramid Principle. Use whenever the user asks to summarize updates for leadership or draft executive communications.`
- **Key Bullets:**
  - State **what** it does AND **when** to activate.
  - Include specific trigger keywords and verbs (e.g. "audit", "draft executive update", "review PRD").
- **Speaker Script:**
  > *"If your description is too broad, the agent will try to use the skill when you're just saying hello. If it's too narrow, the agent will miss it. The sweet spot is two sentences: Sentence 1 explains what the skill does. Sentence 2 explicitly lists the triggers: 'Use whenever the user asks to X, Y, or Z.'"*

---

### Slide 4.5: Live Demo — Building a Custom Skill in 10 Minutes
- **Instructor Action:**
  1. Create a new folder: `skills/executive-brief-generator/`.
  2. Create a blank `SKILL.md`.
  3. Type out the YAML frontmatter live.
  4. Add 3 distinct procedural steps:
     - Step 1: Identify Key Decision / Recommendation.
     - Step 2: Extract supporting financial/timeline data.
     - Step 3: Enforce strict bullet constraints (maximum 3 bullets per section).
  5. Save the file and test it live with a messy, rambling email update.
  6. Watch the agent instantly synthesize a crisp executive brief!

---

### Slide 4.6: Student Hands-On Lab (25 Minutes)
- **Student Mission:**
  1. Choose an idea for your custom skill (e.g. Brand Tone Editor, PRD Writer, or Meeting Notes Synthesizer).
  2. Create your folder and `SKILL.md` using the workbook template.
  3. Fill in the YAML frontmatter (`name` + `description`).
  4. Write 3 procedural steps and at least 2 non-negotiable rules.
  5. Test your new skill by submitting test text to your agent!

---

### Slide 4.7: Session Wrap-Up & What's Next
- **Key Bullets:**
  - You are officially an AI Skill Author!
  - You turned human domain expertise into a reusable agent tool.
  - **Coming in Session 5:** How to test, debug, and package your skills so your entire team or company can use them via Git!
