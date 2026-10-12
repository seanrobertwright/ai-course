# ⚡ Course 2: Skill Authoring Quick-Reference Cheatsheet

> **Keep this tab open while writing custom skills!**  
> Use these pre-tested copy-paste snippets for YAML frontmatter, workflow steps, strict guardrails, and debugging prompts.

---

## 🎴 1. The 2-Sentence Radar Description Formula

The `description` field in your YAML frontmatter determines whether your agent awakens. Follow this formula:

```yaml
---
name: my-specialist-skill
description: [Sentence 1: What it does and what methodology it uses]. Use whenever the user asks to [Trigger Verb 1], [Trigger Verb 2], or [Trigger Phrase 3].
---
```

### High-Converting Examples:
* **Brand Tone:**
  ```yaml
  description: Audits written copy, blog posts, and landing pages against the official brand voice guidelines. Use whenever the user asks to review brand tone, polish marketing copy, or check voice alignment.
  ```
* **Executive Summary:**
  ```yaml
  description: Condenses raw project notes and email threads into a 3-bullet Minto Pyramid executive update. Use whenever the user asks to summarize project updates for leadership or prepare an executive brief.
  ```
* **Code QA:**
  ```yaml
  description: Audits web applications for mobile responsiveness, accessibility (WCAG), and clean UI layout. Use whenever the user asks to audit frontend code, check mobile styling, or review accessibility.
  ```

---

## 🛡️ 2. The Negative Constraint Pattern (Preventing AI Drift)

Language models follow negative constraints with higher fidelity when formatted in high-contrast blocks:

```markdown
## Non-Negotiable Guardrails

- **STRICT NEGATIVE CONSTRAINT:** You MUST NOT use buzzwords such as "delve", "tapestry", "game-changer", or "revolutionize".
- **LENGTH CONSTRAINT:** You MUST NEVER exceed 3 bullet points per category.
- **FORMAT CONSTRAINT:** You MUST ALWAYS provide the output in a markdown table; do not write conversational preamble.
```

---

## 🤖 3. Directing Your Agent to Help You Author a Skill

You can direct your AI agent to draft a skill *for you* using this meta-prompt:

```text
I want to create a new custom AI Skill called "[Skill Name]". 

Here is what the skill needs to do:
- [Describe the task in plain English]
- [Mention any rules, checklists, or steps you always follow]
- [Describe who it is for and what the output should look like]

Please generate a complete, production-ready SKILL.md file for me. 
Include:
1. Valid YAML frontmatter with a high-accuracy trigger description.
2. A clear, numbered procedural workflow.
3. Strict non-negotiable guardrails.
4. A structured output template with markdown formatting.
```

---

## 🚑 4. Skill Debugging Triage Prompts

### If your skill won't trigger (Under-Triggering):
```text
I created a skill with this frontmatter:
[PASTE YAML FRONTMATTER]

When I typed "[YOUR TEST PROMPT]", the agent did not activate the skill. 
How should I rewrite the description to make sure the agent detects this intent reliably?
```

### If the agent is ignoring a rule inside the skill:
```text
My skill specifies this rule:
[PASTE RULE]

However, the agent generated this response that violates the rule:
[PASTE VIOLATION]

Please rewrite this section of SKILL.md with stronger negative constraints and structural guardrails to guarantee compliance.
```
