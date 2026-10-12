import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

OUTPUT_DIR = r"E:\Projects\AI Course\course-2-ai-skills\presentations"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Course 2 Visual Theme: Premium Deep Indigo & Electric Violet
BG_COLOR = RGBColor(15, 23, 42)          # Deep Slate #0F172A
CARD_BG = RGBColor(30, 41, 59)           # Slate 800 #1E293B
CARD_BORDER = RGBColor(71, 85, 105)      # Slate 600 #475569
VIOLET_ACCENT = RGBColor(167, 139, 250)  # Violet 400 #A78BFA
CYAN_ACCENT = RGBColor(56, 189, 248)     # Sky 400 #38BDF8
EMERALD_ACCENT = RGBColor(52, 211, 153)  # Emerald 400 #34D399
AMBER_ACCENT = RGBColor(251, 191, 36)    # Amber 400 #FBBF24
TEXT_WHITE = RGBColor(255, 255, 255)
TEXT_MUTED = RGBColor(148, 163, 184)     # Slate 400 #94A3B8
TEXT_BODY = RGBColor(226, 232, 240)      # Slate 200 #E2E8F0

def set_slide_background(slide):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = BG_COLOR

def add_header(slide, badge_text, title_text):
    badge_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(0.4))
    tf_b = badge_box.text_frame
    tf_b.word_wrap = True
    p_b = tf_b.paragraphs[0]
    p_b.text = badge_text.upper()
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = VIOLET_ACCENT

    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.8))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.size = Pt(26)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_WHITE

def add_speaker_notes(slide, notes_text):
    slide.notes_slide.notes_text_frame.text = notes_text

def create_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.5)
    return shape

def add_title_slide(prs, session_num, title, subtitle, notes):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(slide)
    create_card(slide, Inches(1.2), Inches(1.5), Inches(10.9), Inches(4.5))

    tb = slide.shapes.add_textbox(Inches(1.6), Inches(1.9), Inches(10.1), Inches(3.7))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = f"COURSE 2 • SESSION {session_num} • LIVE WORKSHOP".upper()
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = VIOLET_ACCENT
    p0.space_after = Pt(14)

    p1 = tf.add_paragraph()
    p1.text = title
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(14)

    p2 = tf.add_paragraph()
    p2.text = subtitle
    p2.font.size = Pt(18)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_after = Pt(20)

    p3 = tf.add_paragraph()
    p3.text = "Supercharging AI Agents with Reusable Skills & Automation"
    p3.font.size = Pt(13)
    p3.font.color.rgb = CYAN_ACCENT

    add_speaker_notes(slide, notes)
    return slide

def add_two_column_slide(prs, badge, title, left_h, left_bullets, right_h, right_bullets, notes, left_color=VIOLET_ACCENT, right_color=CYAN_ACCENT):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(slide)
    add_header(slide, badge, title)

    col_w, col_h, top_pos = Inches(5.6), Inches(4.8), Inches(1.8)

    # Left
    create_card(slide, Inches(0.8), top_pos, col_w, col_h)
    tb_l = slide.shapes.add_textbox(Inches(1.1), top_pos + Inches(0.3), col_w - Inches(0.6), col_h - Inches(0.6))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    plh = tf_l.paragraphs[0]
    plh.text = left_h
    plh.font.size = Pt(20)
    plh.font.bold = True
    plh.font.color.rgb = left_color
    plh.space_after = Pt(14)
    for b in left_bullets:
        pb = tf_l.add_paragraph()
        pb.text = "• " + b
        pb.font.size = Pt(14)
        pb.font.color.rgb = TEXT_BODY
        pb.space_after = Pt(10)

    # Right
    create_card(slide, Inches(6.9), top_pos, col_w, col_h)
    tb_r = slide.shapes.add_textbox(Inches(7.2), top_pos + Inches(0.3), col_w - Inches(0.6), col_h - Inches(0.6))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    prh = tf_r.paragraphs[0]
    prh.text = right_h
    prh.font.size = Pt(20)
    prh.font.bold = True
    prh.font.color.rgb = right_color
    prh.space_after = Pt(14)
    for b in right_bullets:
        pb = tf_r.add_paragraph()
        pb.text = "• " + b
        pb.font.size = Pt(14)
        pb.font.color.rgb = TEXT_BODY
        pb.space_after = Pt(10)

    add_speaker_notes(slide, notes)
    return slide

def add_three_card_slide(prs, badge, title, cards, notes):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(slide)
    add_header(slide, badge, title)

    card_w, card_h, top_pos = Inches(3.64), Inches(4.8), Inches(1.8)
    left_positions = [Inches(0.8), Inches(4.84), Inches(8.88)]
    colors = [VIOLET_ACCENT, CYAN_ACCENT, EMERALD_ACCENT]

    for idx, card in enumerate(cards):
        left_pos = left_positions[idx]
        color = colors[idx % len(colors)]
        create_card(slide, left_pos, top_pos, card_w, card_h)
        tb = slide.shapes.add_textbox(left_pos + Inches(0.25), top_pos + Inches(0.3), card_w - Inches(0.5), card_h - Inches(0.6))
        tf = tb.text_frame
        tf.word_wrap = True

        p_num = tf.paragraphs[0]
        p_num.text = f"0{idx+1}"
        p_num.font.size = Pt(12)
        p_num.font.bold = True
        p_num.font.color.rgb = color
        p_num.space_after = Pt(6)

        p_title = tf.add_paragraph()
        p_title.text = card["title"]
        p_title.font.size = Pt(18)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE
        p_title.space_after = Pt(12)

        for bullet in card["bullets"]:
            pb = tf.add_paragraph()
            pb.text = "• " + bullet
            pb.font.size = Pt(13)
            pb.font.color.rgb = TEXT_BODY
            pb.space_after = Pt(8)

    add_speaker_notes(slide, notes)
    return slide

def add_lab_slide(prs, badge, title, mission_text, options, checklist, notes):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(slide)
    add_header(slide, badge, title)
    top_pos = Inches(1.8)

    # Left: Mission
    create_card(slide, Inches(0.8), top_pos, Inches(7.5), Inches(4.8))
    tb_l = slide.shapes.add_textbox(Inches(1.1), top_pos + Inches(0.3), Inches(6.9), Inches(4.2))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True

    pm = tf_l.paragraphs[0]
    pm.text = "🎯 LAB MISSION"
    pm.font.size = Pt(14)
    pm.font.bold = True
    pm.font.color.rgb = AMBER_ACCENT
    pm.space_after = Pt(6)

    pmt = tf_l.add_paragraph()
    pmt.text = mission_text
    pmt.font.size = Pt(15)
    pmt.font.color.rgb = TEXT_WHITE
    pmt.space_after = Pt(14)

    p_opt = tf_l.add_paragraph()
    p_opt.text = "FOCUS OPTIONS:"
    p_opt.font.size = Pt(13)
    p_opt.font.bold = True
    p_opt.font.color.rgb = VIOLET_ACCENT
    p_opt.space_after = Pt(6)

    for opt in options:
        po = tf_l.add_paragraph()
        po.text = "• " + opt
        po.font.size = Pt(13)
        po.font.color.rgb = TEXT_BODY
        po.space_after = Pt(6)

    # Right: Checklist
    create_card(slide, Inches(8.7), top_pos, Inches(3.8), Inches(4.8))
    tb_r = slide.shapes.add_textbox(Inches(9.0), top_pos + Inches(0.3), Inches(3.2), Inches(4.2))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    p_chk = tf_r.paragraphs[0]
    p_chk.text = "⏱️ SPRINT CHECKLIST"
    p_chk.font.size = Pt(14)
    p_chk.font.bold = True
    p_chk.font.color.rgb = EMERALD_ACCENT
    p_chk.space_after = Pt(12)

    for item in checklist:
        pi = tf_r.add_paragraph()
        pi.text = "✅  " + item
        pi.font.size = Pt(13)
        pi.font.color.rgb = TEXT_WHITE
        pi.space_after = Pt(10)

    add_speaker_notes(slide, notes)
    return slide

def build_skills_session_slides(prs, session_id):
    if session_id == 1:
        add_title_slide(
            prs, 1,
            "Demystifying Skills",
            "Why Prompts Fail at Scale & The 3 Superpowers of Skills",
            "Welcome to Course 2! In Course 1, we learned how to talk to agents. In Course 2, we turn generalist agents into specialized domain experts using Skills. Warm-up prompt in chat: 'How often do you find yourself re-typing company rules into ChatGPT?'"
        )
        add_two_column_slide(
            prs, "Session 1 • Foundations",
            "The Problem with 'Mega-Prompts' vs. The Skill Solution",
            "The Prompting Fatigue Problem",
            [
                "Copy-pasting 2,000-word prompt docs every morning",
                "Context bloat: fills up memory and slows down AI",
                "Inconsistent results: AI skips rules #12 and #19",
                "Every new chat suffers from total amnesia"
            ],
            "The Skill Solution",
            [
                "Packaged, reusable unit of domain capability",
                "Combines explicit SOPs + automation scripts",
                "Triggered on-demand; zero context bloat",
                "Enforces identical quality standards every single time"
            ],
            "Use the new hire intern metaphor. You don't re-explain company guidelines every morning; you hand them a permanent SOP binder and toolbelt."
        )
        add_three_card_slide(
            prs, "Session 1 • Superpowers",
            "The 3 Superpowers of AI Agent Skills",
            [
                {
                    "title": "Deterministic Consistency",
                    "bullets": [
                        "Eliminates guesswork and hallucinated formats",
                        "Enforces strict checklists and rubrics",
                        "Same high quality regardless of user"
                    ]
                },
                {
                    "title": "Progressive Disclosure",
                    "bullets": [
                        "Agent context stays fast and lean (~30 tokens)",
                        "Only loads full skill when user asks for it",
                        "Install 50+ skills without performance drops"
                    ]
                },
                {
                    "title": "Executable Automation",
                    "bullets": [
                        "Skills bundle actual code scripts & templates",
                        "Agent can run tools, calculate, and format",
                        "Transforms advice into active execution"
                    ]
                }
            ],
            "Walk through the 3 superpowers. Highlight Progressive Disclosure as the engineering breakthrough that allows scaling."
        )
        add_lab_slide(
            prs, "Session 1 • Benchmark Lab",
            "Live Benchmark: Vanilla Prompt vs. Skill-Equipped Agent",
            "Run an identical request through an untrained agent vs. a skill-equipped agent and compare the outputs.",
            [
                "Test A: Ask vanilla agent to 'Review landing page copy'",
                "Test B: Equip agent with conversion-copy-audit skill and repeat",
                "Evaluate: Depth, structure, actionable rigor, and formatting"
            ],
            [
                "Run Test A (Vanilla prompt)",
                "Activate Skill Cartridge",
                "Run Test B (Same prompt with skill)",
                "Document side-by-side differences",
                "Post before/after in workshop chat"
            ],
            "Have students observe how the skill automatically enforces a 7-point audit table that vanilla AI would never generate unprompted."
        )

    elif session_id == 2:
        add_title_slide(
            prs, 2,
            "The Anatomy of a Skill",
            "Deconstructing SKILL.md, Frontmatter & Folder Architecture",
            "Today we look inside the skill cartridge. By the end of this session, students will understand every file inside a skill directory."
        )
        add_three_card_slide(
            prs, "Session 2 • Architecture",
            "The Standard Skill Directory Layout",
            [
                {
                    "title": "SKILL.md (Required)",
                    "bullets": [
                        "The master blueprint and instruction manual",
                        "Contains YAML frontmatter at the top",
                        "Specifies step-by-step procedures and rules"
                    ]
                },
                {
                    "title": "templates/ & references/",
                    "bullets": [
                        "Markdown starter boilerplates and forms",
                        "Deep reference guides, style manuals, glossaries",
                        "Consulted by the agent when relevant"
                    ]
                },
                {
                    "title": "scripts/ & examples/",
                    "bullets": [
                        "Executable Python, Node, or Shell scripts",
                        "Input/output golden examples for few-shot guidance",
                        "Enables active computing inside skills"
                    ]
                }
            ],
            "Emphasize that SKILL.md is the only required file. Everything else is modular and added as needed."
        )
        add_two_column_slide(
            prs, "Session 2 • SKILL.md Breakdown",
            "Frontmatter vs. Markdown Body: Two Critical Zones",
            "Zone 1: YAML Frontmatter (The Radar)",
            [
                "Fenced by triple dashes `---` at the very top",
                "`name`: Unique hyphenated ID (e.g. `brand-editor`)",
                "`description`: The most important sentence in the skill!",
                "Acts as the agent's trigger radar to know when to wake up"
            ],
            "Zone 2: Markdown Body (The Brain)",
            [
                "Step-by-step numbered procedural workflow",
                "Strict constraints and non-negotiable rules",
                "Output formatting templates (tables, cards)",
                "Links to helper scripts and references"
            ],
            "Stress the importance of the description field. It is what allows the agent to auto-discover the skill without human intervention."
        )
        add_lab_slide(
            prs, "Session 2 • Hands-on Lab",
            "Live Lab: Dissecting & Tuning a Production Skill",
            "Open the sample skill in your workspace, inspect its frontmatter and body, and customize its rule set.",
            [
                "Inspect: Read the description radar and observe triggers",
                "Modify: Add one strict constraint to ## Rules & Standards",
                "Test: Prompt the agent to verify that the new rule is enforced"
            ],
            [
                "Open SKILL.md in code editor",
                "Identify YAML frontmatter fields",
                "Add custom rule (e.g. 'Max 3 bullets')",
                "Test with live agent prompt",
                "Verify rule adherence in response"
            ],
            "Guide students through adding strict negative constraints (e.g., 'MUST NOT use jargon') and testing the result."
        )

    elif session_id == 3:
        add_title_slide(
            prs, 3,
            "Installing & Using Skills",
            "Skill Ecosystems, Local vs. Global & Activation Verification",
            "Today we learn how to discover, download, install, and trigger community skills in under 60 seconds."
        )
        add_two_column_slide(
            prs, "Session 3 • Installation",
            "Where Skills Live: Local (Project) vs. Global (User)",
            "Local Project Skills",
            [
                "Stored inside the project folder (`skills/`)",
                "Dedicated to that specific codebase or client",
                "Examples: Project database schema rules, client brand guide",
                "Shared with collaborators when committing to Git"
            ],
            "Global User Skills",
            [
                "Stored in your user home directory",
                "Available across every project you ever open",
                "Examples: Writing coach, meeting notes formatter, code auditor",
                "Your personal persistent superpower library"
            ],
            "Clarify when to use local vs. global skills. Local is for specific projects/teams; global is for your personal workflow."
        )
        add_two_column_slide(
            prs, "Session 3 • Invocation",
            "Two Ways to Trigger: Natural Radar vs. Direct Invocation",
            "Natural Intent Triggering",
            [
                "You type: 'Can you polish this marketing text?'",
                "Agent matches keywords in skill description",
                "Automatically loads `SKILL.md` in background",
                "Seamless, conversational, zero memorization needed"
            ],
            "Explicit Direct Invocation",
            [
                "You type: 'Use the brand-voice skill on this text.'",
                "Forces 100% guaranteed skill activation",
                "Great when multiple skills overlap",
                "Eliminates any chance of the agent missing intent"
            ],
            "Show both invocation patterns live on screen. Highlight that natural triggering is great for daily work, while explicit invocation guarantees execution."
        )
        add_lab_slide(
            prs, "Session 3 • Hands-on Lab",
            "Live Lab: Installing & Activating a Community Skill",
            "Install the pre-built 'Customer Persona Generator' skill and trigger it using both natural and explicit methods.",
            [
                "Method 1: Natural prompt ('Build a persona for a boutique fitness studio')",
                "Method 2: Explicit prompt ('Activate customer-persona-generator on...')"
            ],
            [
                "Copy skill folder into workspace",
                "Test natural intent trigger",
                "Verify signature output card",
                "Test explicit name invocation",
                "Confirm skill file read in agent log"
            ],
            "Have students verify the agent's thought logs to see the exact moment the agent calls view_file on the SKILL.md document."
        )

    elif session_id == 4:
        add_title_slide(
            prs, 4,
            "Authoring Custom Skills",
            "From Skill Consumer to Toolmaker: Creating Your Superpowers",
            "Today is the big leap: students become AI toolmakers. We turn their own domain expertise into a reusable skill."
        )
        add_three_card_slide(
            prs, "Session 4 • Strategy",
            "Finding High-Value 'Skill Opportunities'",
            [
                {
                    "title": "1. Repetitive Friction",
                    "bullets": [
                        "Any task you explain to AI >2x a week",
                        "Weekly status reports, meeting summaries",
                        "Code boilerplate generation"
                    ]
                },
                {
                    "title": "2. Tribal Knowledge",
                    "bullets": [
                        "Unwritten company guidelines & style rules",
                        "Domain compliance & legal review checklists",
                        "Industry-specific vocabulary & rubrics"
                    ]
                },
                {
                    "title": "3. High-Stakes Accuracy",
                    "bullets": [
                        "PRD specs & engineering requirements",
                        "Client proposals & executive email polish",
                        "Tasks where consistency is mandatory"
                    ]
                }
            ],
            "Help students brainstorm their skill idea. Remind them: your unique domain background is your competitive advantage."
        )
        add_two_column_slide(
            prs, "Session 4 • Authoring Framework",
            "The 4-Step Skill Authoring Blueprint",
            "1. The Radar Description",
            [
                "Sentence 1: What the skill does clearly",
                "Sentence 2: Exactly WHEN to trigger ('Use whenever...')",
                "Include concrete trigger verbs and domain keywords"
            ],
            "2. Steps, Rules & Output Shape",
            [
                "Step-by-step numbered workflow",
                "Negative constraints (`MUST NOT`, `NEVER`)",
                "Provide an exact markdown template or table shape"
            ],
            "Walk through the 4-step blueprint. Explain that giving an output template gives the agent a clear target mold to fill."
        )
        add_lab_slide(
            prs, "Session 4 • Hands-on Lab",
            "Live Lab: Build Your First Custom Domain Skill",
            "Create a new skill folder and author a complete SKILL.md from scratch using the student workbook template.",
            [
                "Idea 1: Executive Brief Synthesizer (Condenses updates into 3 actionable bullets)",
                "Idea 2: PRD Feature Spec Generator (Turns ideas into technical specs)",
                "Idea 3: Brand Tone Polish Assistant (Enforces custom brand voice)"
            ],
            [
                "Create folder & blank SKILL.md",
                "Write YAML frontmatter radar",
                "Write 3 procedural steps",
                "Add 2 strict negative constraints",
                "Test live with your agent!"
            ],
            "Facilitators assist students in crafting their description field so the agent triggers cleanly on test prompts."
        )

    elif session_id == 5:
        add_title_slide(
            prs, 5,
            "Testing, Refining & Team Workflows",
            "Debugging, Scaling Across Teams with Git & Capstone Showcase",
            "Finale session! We learn how to debug skills, eliminate edge cases, share skills across organizations, and present capstone creations."
        )
        add_two_column_slide(
            prs, "Session 5 • Debugging",
            "The Two Classic Skill Bugs & How to Fix Them",
            "Bug 1: Under-Triggering (The Sleeper)",
            [
                "Symptom: Skill fails to wake up on relevant prompts",
                "Root Cause: Description is too narrow or missing verbs",
                "Fix: Add explicit trigger synonyms: 'Use when user asks to X, Y, or Z'"
            ],
            "Bug 2: Over-Triggering (The Eager Beaver)",
            [
                "Symptom: Skill activates on casual or unrelated chats",
                "Root Cause: Description is overly broad (e.g. 'helps write text')",
                "Fix: Add strict scope boundaries and context filters"
            ],
            "Explain the balance between sensitivity and specificity in skill trigger descriptions."
        )
        add_two_column_slide(
            prs, "Session 5 • Scaling",
            "The Company Skill Library: Distributing via Git",
            "Centralized SOPs in Git",
            [
                "Skills live as plain markdown in Git repositories",
                "Commit updates to central repo in seconds",
                "Whole team pulls latest version automatically"
            ],
            "Zero Training Lag",
            [
                "When company policy updates, update `SKILL.md`",
                "Every team member's AI adopts new rules instantly",
                "Replaces 30-page employee manuals with live agent tools"
            ],
            "Describe the enterprise value: rather than training 500 employees on a new rule, you update one SKILL.md file and every agent enforces it."
        )
        add_lab_slide(
            prs, "Session 5 • Graduation",
            "Capstone Skill Showcase: 2-Minute Lightning Demos",
            "Demonstrate your custom skill live to the cohort: explain the problem, show your SKILL.md, and test it live!",
            [
                "1. Introduce your skill: What problem does it solve?",
                "2. Show your YAML frontmatter radar and key guardrails",
                "3. Run a live prompt test and celebrate the structured output!"
            ],
            [
                "Finalize custom SKILL.md",
                "Run positive & negative test prompt",
                "Deliver 2-minute demo",
                "Share skill package in group chat",
                "Receive Course 2 Graduation Badge!"
            ],
            "Celebrate every graduate. Highlight how they've leveled up from prompt users to autonomous agent toolmakers."
        )

def main():
    prs_master = Presentation()
    prs_master.slide_width = Inches(13.333)
    prs_master.slide_height = Inches(7.5)

    session_names = [
        "Demystifying_Skills",
        "Anatomy_of_a_Skill",
        "Installing_and_Using_Skills",
        "Authoring_Custom_Skills",
        "Testing_and_Team_Workflows"
    ]

    print("Building Master Skills Deck...")
    for s_id in range(1, 6):
        build_skills_session_slides(prs_master, s_id)

    master_path = os.path.join(OUTPUT_DIR, "Master_Skills_Course_Deck.pptx")
    prs_master.save(master_path)
    print(f"Saved: {master_path}")

    for s_id in range(1, 6):
        print(f"Building Session {s_id} Deck...")
        prs_single = Presentation()
        prs_single.slide_width = Inches(13.333)
        prs_single.slide_height = Inches(7.5)
        build_skills_session_slides(prs_single, s_id)

        filename = f"Session_{s_id}_{session_names[s_id-1]}.pptx"
        single_path = os.path.join(OUTPUT_DIR, filename)
        prs_single.save(single_path)
        print(f"Saved: {single_path}")

if __name__ == "__main__":
    main()
