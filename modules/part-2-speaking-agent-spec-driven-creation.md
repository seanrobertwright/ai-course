# Part 2: The Art of the Spec — Directing AI Agents Like a Product Manager

> **Target Duration:** 60–90 Minutes  
> **Audience Background:** Zero coding experience, completed Part 1.  
> **Primary Goal:** Master the art of structured communication with AI agents; learn how to build complex apps iteratively without overwhelming the agent.

---

## 🎯 Learning Objectives
1. Understand the **Product Manager (PM)** role vs. the **Engineer** role in an AI-native world.
2. Master the **C.A.R.E. Prompting Framework** for crafting unambiguous software specifications.
3. Learn the principle of **Iterative Layering** (MVP first, then enhancements).
4. Discover how to provide precise corrective feedback when the agent gets something wrong.

---

## 🖼️ Slide-by-Slide Presentation Guide

### Slide 1: You Are Now the Product Manager
- **Visual:** Illustration of a Product Manager holding a blueprint, coordinating with an AI engineering team.
- **Key Bullets:**
  - Engineers write syntax; Product Managers define **what to build and why**.
  - In traditional tech, PMs spend weeks writing specs for human developers.
  - With Replit Agent, your spec turns into working code in minutes.
- **Speaker Script:**
  > *"In Part 1, we learned that agents act as our construction crew. But every construction crew needs a general contractor or architect. That is your new title: Product Manager. A great PM doesn't need to know how to pour concrete, but they must be crystal clear about how many rooms the house has, where the doors go, and who will live there."*

---

### Slide 2: The Number 1 Mistake Beginners Make
- **Visual:** A graphic showing an "Idea Avalanche": throwing 20 complex features into prompt #1, resulting in a confusing, buggy mess.
- **Key Bullets:**
  - ❌ *The Avalanche:* "Build me Amazon + Netflix + TikTok with payments and crypto."
  - ✅ *The Foundation:* Build the Minimum Viable Product (MVP) first, test it, then layer on features one at a time.
  - Agents work best when given focused, coherent goals.
- **Speaker Script:**
  > *"When people discover how powerful Replit Agent is, their first instinct is to ask for everything at once. They want user logins, credit card payments, live video, 3D animations, and social sharing in prompt number one! That's like asking a contractor to build the roof before the foundation is poured. Start with the core loop first."*

---

### Slide 3: The C.A.R.E. Framework for Agent Prompts
- **Visual:** 4-quadrant diagram detailing C.A.R.E.:
  - **C - Context:** Who is this for? What is the scenario?
  - **A - Action:** What is the primary user flow?
  - **R - Rules & Constraints:** What must (or must NOT) happen?
  - **E - Experience:** What should the design, visual tone, and feel look like?
- **Key Bullets:**
  - **Context:** "A productivity dashboard for freelance writers..."
  - **Action:** "Allow them to create daily word count goals and log progress..."
  - **Rules:** "Progress bars should turn green at 100%, red if under target. Keep data saved locally..."
  - **Experience:** "Minimalist, soothing color palette (slate grey, soft emerald), clean typography."
- **Speaker Script:**
  > *"To get breathtaking results from Replit Agent on the very first try, remember C.A.R.E. Context, Action, Rules, Experience. When you give the agent these four ingredients, it has full clarity on both the functional requirements and the visual expectations."*

---

### Slide 4: Iterative Layering — Building in Sprints
- **Visual:** A 3-step stair-step diagram:
  1. *Step 1 (Core Engine):* Does the main button and input work?
  2. *Step 2 (Experience Polish):* Add animations, responsive layout, dark mode.
  3. *Step 3 (Advanced Features):* Add sound effects, export to PDF, statistics charts.
- **Key Bullets:**
  - Never change 5 things at once if you can change 1 or 2.
  - Test each version in the preview before prompting the next feature.
  - Replit has built-in version history / checkpoints: you can always rollback!
- **Speaker Script:**
  > *"Software development happens in layers. We call this 'sprinting'. In Sprint 1, we make sure the core engine runs. Once we verify it works in the live preview, we prompt Sprint 2: adding polish, charts, and colors. This ensures you never get stuck with an untraceable bug."*

---

### Slide 5: How to Correct an Agent (Steering, Not Shouting)
- **Visual:** Side-by-side prompt comparison:
  - ❌ *Vague:* "This looks broken. Fix it."
  - ❌ *Frustrated:* "Why didn't you listen to me? I said make it good!"
  - ✅ *Constructive & Specific:* "When I click the 'Add Habit' button, the item appears in the list, but the text box doesn't clear. Please make sure the input clears automatically after submitting."
- **Key Bullets:**
  - Describe:
    1. What action you took.
    2. What happened (the unexpected result).
    3. What you expected to happen instead.
- **Speaker Script:**
  > *"When an agent does something unexpected, don't get frustrated. Treat it like a junior developer who is eager to please but needs specific directions. Describe the exact behavior: 'When I clicked X, Y happened, but I expected Z.' The agent will pinpoint the exact code line and fix it instantly."*

---

### Slide 6: Live Demo — Building a "Smart Daily Habit Tracker"
- **Instructor Action:**
  1. Start with a structured C.A.R.E. prompt for a 7-Day Habit Tracker.
  2. Review the agent's generated MVP live.
  3. Intentionally prompt a design update: *"Change the color scheme to dark mode with neon accents and add a streak fire emoji counter."*
  4. Prompt an interactive feature: *"Add a weekly progress summary bar at the top."*
  5. Demonstrate the Replit checkpoint/history feature (showing how to roll back if needed).

---

### Slide 7: Student Hands-On Lab (25 Minutes)
- **Student Challenge:**
  - Create a **"Personal Micro-Portfolio / Link Hub"** (like Linktree, but supercharged).
  - *Must-Have Features:*
    - Profile picture, bio, and social links with icons.
    - An interactive contact form or "Book a 15-min chat" modal.
    - A toggle for light/dark theme.
    - A simple visitor counter or click tracker for each link.
  - Practice using the C.A.R.E. framework for the first prompt, then do at least **two iterative follow-up prompts** to refine the design.

---

### Slide 8: Takeaways & What's Next
- **Key Bullets:**
  - Clear thinking leads to clear software.
  - Iteration beats trying to be perfect in prompt one.
  - **Coming in Part 3:** What's actually happening behind the curtain? We will peek under the hood at HTML, CSS, and basic project files—without the scary math.
