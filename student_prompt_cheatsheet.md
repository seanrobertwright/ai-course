# ⚡ Student Quick-Reference Prompt Cheatsheet

> **Keep this tab open during live workshop sessions!**  
> Copy, customize, and paste these proven prompt templates directly into Replit Agent.

---

## 🎴 1. The C.A.R.E. Prompt Formula (Copy & Fill In)

```text
Build a modern web application called "[App Name]".

CONTEXT:
This app is designed for [target audience] who want to [goal or problem to solve].

ACTION / CORE WORKFLOW:
The user should be able to:
1. [Step 1: Input text, select options, or click button]
2. [Step 2: Trigger the main action or AI generation]
3. [Step 3: View the output or result displayed in a card]

RULES & CONSTRAINTS:
- [Rule 1: What must happen, e.g. "Validate that inputs are not empty"]
- [Rule 2: What must NOT happen, e.g. "Do not erase previous inputs on error"]
- [Rule 3: State or persistence, e.g. "Save entries so they survive page refresh"]

EXPERIENCE & STYLING:
- Style: Clean, modern, [minimalist / vibrant / playful / executive]
- Palette: [Dark mode with emerald accents / Clean light mode with indigo accents]
- Layout: Mobile-responsive card layout with smooth button hover effects.
```

---

## 🛠️ 2. The 3-Part Feedback Formula (When Correcting the Agent)

When the agent builds something slightly different from what you wanted, never just say *"It's broken"*. Use this 3-part formula:

```text
When I [describe the exact action you took], 
[describe the unexpected result that happened], 
but I expected [describe what should have happened instead]. 

Please update the code to fix this behavior.
```

### Examples:
- *"When I click the 'Add Task' button, the item appears in the list, but the text box does not clear. Please ensure the input clears automatically after submitting."*
- *"When I test the app on mobile, the submit button is cut off below the screen fold. Please adjust the container padding so the button is always visible."*

---

## 🤖 3. Replit Built-In AI Prompt Templates (Session 4)

### Template A: Evaluator & Scorer
```text
Connect this app to Replit's built-in AI model. When the user enters [type of text] and clicks "Evaluate", instruct the AI to:
- Act as [Persona, e.g. Senior Tech Recruiter / Startup Investor / Executive Coach]
- Give a score from 1 to 10
- Provide 3 specific strengths
- Provide 3 actionable areas for improvement
Return the output in clean, formatted sections inside a high-contrast card.
```

### Template B: Tone Transformer / Polisher
```text
Connect this app to Replit's built-in AI model. Let the user paste rough draft text and choose a target tone:
- "Executive & Concise"
- "Warm & Empathetic"
- "Persuasive & High-Energy"
Generate 3 distinct rewritten options with a one-click "Copy to Clipboard" button for each option.
```

---

## 💾 4. Database & Persistence Prompt Templates (Session 5)

### Add Storage & Community History:
```text
Please attach a persistent database to save every generated item. 
Store the following fields:
- original_input
- ai_result
- category_tag
- created_at timestamp

Below the generator form, display a "Community Gallery" displaying all past submissions from the database. 
Include an upvote/heart button on each item that increments a counter in the database.
```

---

## 🚑 5. The Error Debugging Prompt (Session 6)

When you see red error text in the console or preview:

```text
I am seeing the following error message in the console when trying to [action you took]:

---
[PASTE RED ERROR TEXT HERE]
---

Please analyze the root cause of this error, review the corresponding files, and repair the code so the app runs smoothly.
```
