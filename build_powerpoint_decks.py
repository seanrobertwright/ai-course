import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Ensure output directory exists
OUTPUT_DIR = r"E:\Projects\AI Course\presentations"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Visual Design Theme (Modern Dark Tech Slate)
BG_COLOR = RGBColor(15, 23, 42)        # Slate 900 #0F172A
CARD_BG = RGBColor(30, 41, 59)         # Slate 800 #1E293B
CARD_BORDER = RGBColor(51, 65, 85)     # Slate 700 #334155
CYAN_ACCENT = RGBColor(56, 189, 248)   # Sky 400 #38BDF8
EMERALD_ACCENT = RGBColor(52, 211, 153)# Emerald 400 #34D399
AMBER_ACCENT = RGBColor(251, 191, 36)  # Amber 400 #FBBF24
TEXT_WHITE = RGBColor(255, 255, 255)
TEXT_MUTED = RGBColor(148, 163, 184)   # Slate 400 #94A3B8
TEXT_BODY = RGBColor(226, 232, 240)    # Slate 200 #E2E8F0

def set_slide_background(slide):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = BG_COLOR

def add_header(slide, module_badge, title_text):
    # Module category badge
    badge_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(0.4))
    tf_badge = badge_box.text_frame
    tf_badge.word_wrap = True
    p_badge = tf_badge.paragraphs[0]
    p_badge.text = module_badge.upper()
    p_badge.font.size = Pt(11)
    p_badge.font.bold = True
    p_badge.font.color.rgb = CYAN_ACCENT
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.8))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.size = Pt(26)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_WHITE

def add_speaker_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = notes_text

def create_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.5)
    return shape

def add_title_slide(prs, module_number, module_title, subtitle, notes):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    set_slide_background(slide)
    
    # Decorative accent card
    create_card(slide, Inches(1.2), Inches(1.5), Inches(10.9), Inches(4.5))
    
    tb = slide.shapes.add_textbox(Inches(1.6), Inches(1.9), Inches(10.1), Inches(3.7))
    tf = tb.text_frame
    tf.word_wrap = True
    
    # Badge
    p0 = tf.paragraphs[0]
    p0.text = f"MODULE {module_number} • LIVE WORKSHOP SESSION".upper()
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = CYAN_ACCENT
    p0.space_after = Pt(14)
    
    # Title
    p1 = tf.add_paragraph()
    p1.text = module_title
    p1.font.size = Pt(38)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(14)
    
    # Subtitle
    p2 = tf.add_paragraph()
    p2.text = subtitle
    p2.font.size = Pt(18)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_after = Pt(20)
    
    p3 = tf.add_paragraph()
    p3.text = "Zero Coding Experience Required  |  Powered by Replit & AI Agents"
    p3.font.size = Pt(13)
    p3.font.color.rgb = EMERALD_ACCENT
    
    add_speaker_notes(slide, notes)
    return slide

def add_two_column_slide(prs, badge, title, left_title, left_bullets, right_title, right_bullets, notes, left_color=CYAN_ACCENT, right_color=EMERALD_ACCENT):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    set_slide_background(slide)
    add_header(slide, badge, title)
    
    col_width = Inches(5.6)
    col_height = Inches(4.8)
    top_pos = Inches(1.8)
    
    # Left Card
    create_card(slide, Inches(0.8), top_pos, col_width, col_height)
    tb_l = slide.shapes.add_textbox(Inches(1.1), top_pos + Inches(0.3), col_width - Inches(0.6), col_height - Inches(0.6))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    
    p_lh = tf_l.paragraphs[0]
    p_lh.text = left_title
    p_lh.font.size = Pt(20)
    p_lh.font.bold = True
    p_lh.font.color.rgb = left_color
    p_lh.space_after = Pt(14)
    
    for bullet in left_bullets:
        pb = tf_l.add_paragraph()
        pb.text = "• " + bullet
        pb.font.size = Pt(14)
        pb.font.color.rgb = TEXT_BODY
        pb.space_after = Pt(10)
        
    # Right Card
    create_card(slide, Inches(6.9), top_pos, col_width, col_height)
    tb_r = slide.shapes.add_textbox(Inches(7.2), top_pos + Inches(0.3), col_width - Inches(0.6), col_height - Inches(0.6))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    
    p_rh = tf_r.paragraphs[0]
    p_rh.text = right_title
    p_rh.font.size = Pt(20)
    p_rh.font.bold = True
    p_rh.font.color.rgb = right_color
    p_rh.space_after = Pt(14)
    
    for bullet in right_bullets:
        pb = tf_r.add_paragraph()
        pb.text = "• " + bullet
        pb.font.size = Pt(14)
        pb.font.color.rgb = TEXT_BODY
        pb.space_after = Pt(10)
        
    add_speaker_notes(slide, notes)
    return slide

def add_three_card_slide(prs, badge, title, cards, notes):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    set_slide_background(slide)
    add_header(slide, badge, title)
    
    card_width = Inches(3.64)
    card_height = Inches(4.8)
    top_pos = Inches(1.8)
    
    left_positions = [Inches(0.8), Inches(4.84), Inches(8.88)]
    colors = [CYAN_ACCENT, EMERALD_ACCENT, AMBER_ACCENT]
    
    for idx, card in enumerate(cards):
        left_pos = left_positions[idx]
        color = colors[idx % len(colors)]
        
        create_card(slide, left_pos, top_pos, card_width, card_height)
        tb = slide.shapes.add_textbox(left_pos + Inches(0.25), top_pos + Inches(0.3), card_width - Inches(0.5), card_height - Inches(0.6))
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
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    set_slide_background(slide)
    add_header(slide, badge, title)
    
    top_pos = Inches(1.8)
    
    # Left Box: Missions & Options
    create_card(slide, Inches(0.8), top_pos, Inches(7.5), Inches(4.8))
    tb_l = slide.shapes.add_textbox(Inches(1.1), top_pos + Inches(0.3), Inches(6.9), Inches(4.2))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    
    p_m = tf_l.paragraphs[0]
    p_m.text = "🎯 YOUR MISSION"
    p_m.font.size = Pt(14)
    p_m.font.bold = True
    p_m.font.color.rgb = AMBER_ACCENT
    p_m.space_after = Pt(6)
    
    p_mt = tf_l.add_paragraph()
    p_mt.text = mission_text
    p_mt.font.size = Pt(15)
    p_mt.font.color.rgb = TEXT_WHITE
    p_mt.space_after = Pt(14)
    
    p_opt_hdr = tf_l.add_paragraph()
    p_opt_hdr.text = "PICK ONE STARTER PROJECT:"
    p_opt_hdr.font.size = Pt(13)
    p_opt_hdr.font.bold = True
    p_opt_hdr.font.color.rgb = CYAN_ACCENT
    p_opt_hdr.space_after = Pt(6)
    
    for opt in options:
        po = tf_l.add_paragraph()
        po.text = "• " + opt
        po.font.size = Pt(13)
        po.font.color.rgb = TEXT_BODY
        po.space_after = Pt(6)
        
    # Right Box: Live Workshop Rules & Checklist
    create_card(slide, Inches(8.7), top_pos, Inches(3.8), Inches(4.8))
    tb_r = slide.shapes.add_textbox(Inches(9.0), top_pos + Inches(0.3), Inches(3.2), Inches(4.2))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    
    p_chk_hdr = tf_r.paragraphs[0]
    p_chk_hdr.text = "⏱️ 25-MIN SPRINT CHECKLIST"
    p_chk_hdr.font.size = Pt(14)
    p_chk_hdr.font.bold = True
    p_chk_hdr.font.color.rgb = EMERALD_ACCENT
    p_chk_hdr.space_after = Pt(12)
    
    for item in checklist:
        pi = tf_r.add_paragraph()
        pi.text = "✅  " + item
        pi.font.size = Pt(13)
        pi.font.color.rgb = TEXT_WHITE
        pi.space_after = Pt(10)
        
    add_speaker_notes(slide, notes)
    return slide

def add_framework_slide(prs, badge, title, framework_name, items, notes):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    set_slide_background(slide)
    add_header(slide, badge, title)
    
    top_pos = Inches(1.8)
    card_width = Inches(5.6)
    card_height = Inches(2.25)
    
    coords = [
        (Inches(0.8), top_pos),
        (Inches(6.9), top_pos),
        (Inches(0.8), top_pos + Inches(2.55)),
        (Inches(6.9), top_pos + Inches(2.55))
    ]
    colors = [CYAN_ACCENT, EMERALD_ACCENT, AMBER_ACCENT, RGBColor(167, 139, 250)]
    
    for idx, item in enumerate(items):
        pos = coords[idx]
        color = colors[idx]
        
        create_card(slide, pos[0], pos[1], card_width, card_height)
        tb = slide.shapes.add_textbox(pos[0] + Inches(0.3), pos[1] + Inches(0.2), card_width - Inches(0.6), card_height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p_letter = tf.paragraphs[0]
        p_letter.text = item["letter"] + " — " + item["name"]
        p_letter.font.size = Pt(16)
        p_letter.font.bold = True
        p_letter.font.color.rgb = color
        p_letter.space_after = Pt(4)
        
        p_desc = tf.add_paragraph()
        p_desc.text = item["desc"]
        p_desc.font.size = Pt(13)
        p_desc.font.color.rgb = TEXT_BODY
        p_desc.space_after = Pt(4)
        
        p_ex = tf.add_paragraph()
        p_ex.text = "Example: \"" + item["example"] + "\""
        p_ex.font.size = Pt(11)
        p_ex.font.color.rgb = TEXT_MUTED
        
    add_speaker_notes(slide, notes)
    return slide

def build_module_slides(prs, module_id):
    if module_id == 1:
        add_title_slide(
            prs, 1,
            "The New Era of Creation",
            "Demystifying AI Agents & Building Your First App in 20 Minutes",
            "Welcome everyone! Reassure attendees that zero technical background is needed. Today they step into the role of software architect. Start with live chat icebreaker: 'What is #1 tool you wish existed?'"
        )
        add_two_column_slide(
            prs, "Module 1 • Foundation",
            "The Great Shift: Chatbot vs. Autonomous AI Agent",
            "The Chatbot (The Advisor)",
            [
                "Examples: Standard ChatGPT, Claude chat",
                "Answers questions, generates text, gives advice",
                "Cannot touch your computer files or install tools",
                "Metaphor: An architect giving you a book on carpentry"
            ],
            "The AI Agent (The Builder)",
            [
                "Examples: Replit Agent",
                "Has independent tools and execution power",
                "Creates files, installs libraries, runs live code",
                "Reads its own error messages and auto-fixes bugs",
                "Metaphor: The carpenter who actually builds the chair"
            ],
            "Use the carpenter metaphor. Emphasize that Replit Agent is not just generating text snippets; it is an active developer running a cloud computer for you."
        )
        add_three_card_slide(
            prs, "Module 1 • Environment",
            "Why Replit? Zero Local Setup, Maximum Power",
            [
                {
                    "title": "100% In Browser",
                    "bullets": [
                        "No downloading VS Code, Git, or Python",
                        "Works on PC, Mac, Chromebook, or iPad",
                        "Eliminates 80% of beginner setup errors"
                    ]
                },
                {
                    "title": "Instant Live Preview",
                    "bullets": [
                        "See your app run side-by-side as it is built",
                        "Real-time visual feedback loop",
                        "Test buttons and forms immediately"
                    ]
                },
                {
                    "title": "Global Cloud Hosting",
                    "bullets": [
                        "One-click public web URL generated",
                        "Open the link on your phone in minutes",
                        "Share live prototypes with colleagues"
                    ]
                }
            ],
            "Explain that 80% of people give up learning code because of local terminal installation errors on Day 1. Replit eliminates that hurdle completely."
        )
        add_two_column_slide(
            prs, "Module 1 • Communication",
            "The Golden Rule: Specificity Equals Success",
            "❌ Weak Prompt (Vague)",
            [
                "\"Make me a cool website for lunch.\"",
                "The agent has to guess user intent",
                "Results in generic, unpredictable layout",
                "Leaves out colors, actions, and features"
            ],
            "✅ Architect Prompt (Clear Spec)",
            [
                "\"Build a modern web app called 'Lunch Roulette'.\"",
                "\"Let users add restaurant names into a list.\"",
                "\"Click a big 'Spin' button to randomly pick one.\"",
                "\"Play an animation and celebrate with confetti.\"",
                "\"Clean, mobile-friendly design with dark mode.\""
            ],
            "Point out that AI cannot read minds. The more causal and visual detail you provide, the closer the first draft will match your vision."
        )
        add_lab_slide(
            prs, "Module 1 • Hands-on Lab",
            "Live Lab: Build & Launch Your First Web App",
            "Open replit.com, click 'Create with Agent', and describe your starter app using clear plain English.",
            [
                "Option A: Tip & Bill Splitter (Enter total, select tip %, split by # of diners)",
                "Option B: Lunch Roulette / Decision Spinner (Add items, spin wheel, celebratory confetti)",
                "Option C: Daily Motivation Affirmation Generator (Pick mood, get tailored quote)"
            ],
            [
                "Write your starter prompt",
                "Watch the agent build the files",
                "Test the interactive buttons",
                "Scan/open the URL on your phone!",
                "Drop your live link in group chat"
            ],
            "Set a 25-minute timer. Put low ambient music on. Remind students: if the agent makes a mistake, tell it: 'When I clicked X, Y happened; please fix.' Facilitators watch the chat for stuck students."
        )

    elif module_id == 2:
        add_title_slide(
            prs, 2,
            "The Art of the Spec",
            "Directing AI Agents Like a Senior Product Manager",
            "Welcome back! Today we transition from quick wins to structured software design. You are the Product Manager."
        )
        add_two_column_slide(
            prs, "Module 2 • Product Thinking",
            "You Are the General Contractor, Not the Bricklayer",
            "The Bricklayer Mindset (Old Way)",
            [
                "Obsessed with syntax, semicolons, brackets",
                "Memorizing obscure programming rules",
                "Easily stuck by typos and library conflicts",
                "High technical barrier, slow creation"
            ],
            "The Product Manager Mindset (AI Way)",
            [
                "Focuses on user journeys and problem solving",
                "Defines clear requirements and acceptance criteria",
                "Leverages domain expertise (business, design, healthcare)",
                "Iterates rapidly with autonomous engineering agents"
            ],
            "Remind attendees that domain expertise (knowing what users actually need) is now more valuable than memorizing code syntax."
        )
        add_framework_slide(
            prs, "Module 2 • Prompt Framework",
            "The C.A.R.E. Framework for Agent Specifications",
            "C.A.R.E.",
            [
                {"letter": "C", "name": "Context", "desc": "Who is this for? What is the scenario?", "example": "A daily habit tracker for busy remote workers."},
                {"letter": "A", "name": "Action", "desc": "What is the primary user flow & main action?", "example": "Users type a new habit and tap to mark it done."},
                {"letter": "R", "name": "Rules", "desc": "What constraints must (or must NOT) happen?", "example": "Show a streak flame counter; reset count if missed."},
                {"letter": "E", "name": "Experience", "desc": "Visual tone, color scheme, feel?", "example": "Sleek dark mode with emerald green accents."}
            ],
            "Encourage students to take a screenshot of C.A.R.E. This is their blueprint for all future agent prompts."
        )
        add_three_card_slide(
            prs, "Module 2 • Iteration Strategy",
            "Iterative Layering: Building in Sprints",
            [
                {
                    "title": "Sprint 1: Core Engine",
                    "bullets": [
                        "Focus strictly on the MVP (Minimum Viable Product)",
                        "Does the basic input and button click work?",
                        "Verify in preview before adding fluff"
                    ]
                },
                {
                    "title": "Sprint 2: Visual Polish",
                    "bullets": [
                        "Upgrade styling, typography, and layout",
                        "Add animations, empty states, and feedback toasts",
                        "Ensure responsive mobile display"
                    ]
                },
                {
                    "title": "Sprint 3: Power Features",
                    "bullets": [
                        "Add data export, audio chimes, or stats charts",
                        "Layer complexity only on top of stable foundations"
                    ]
                }
            ],
            "Warn against the 'Idea Avalanche'—trying to build 20 features in prompt #1 is the top reason beginners get buggy code."
        )
        add_lab_slide(
            prs, "Module 2 • Hands-on Lab",
            "Live Lab: Build a Smart Daily Habit Tracker",
            "Draft a structured C.A.R.E. prompt to build a Habit Tracker or Link Hub, then run two iterative follow-up sprints.",
            [
                "Project 1: Smart Daily Habit Tracker (Streak fire emoji, weekly progress bar)",
                "Project 2: Personal Micro-Portfolio / Link Hub (Bio, social links, contact modal)",
                "Project 3: Interactive Recipe Meal Planner (Add meals, generate grocery list)"
            ],
            [
                "Prompt MVP with C.A.R.E.",
                "Sprint 1: Test basic check-off logic",
                "Sprint 2: Ask agent for theme/polish upgrade",
                "Sprint 3: Add sound chime or stats summary",
                "Test checkpoint rollback feature once"
            ],
            "Have students practice giving precise feedback: 'When I clicked X, Y happened; please make Z happen instead.'"
        )

    elif module_id == 3:
        add_title_slide(
            prs, 3,
            "Peeking Under the Hood",
            "Software Architecture & Code Reading Without Jargon",
            "Today we look at project files. Reassure students: opening code files will not break anything."
        )
        add_two_column_slide(
            prs, "Module 3 • Architecture",
            "The Two Halves of Every Web Application",
            "The Frontend (The Dining Room)",
            [
                "Everything the user sees and touches in their browser",
                "HTML: The structural skeleton (headings, buttons)",
                "CSS / Tailwind: The paint, colors, fonts, margins",
                "React / JS: The interactive animations and clicks"
            ],
            "The Backend (The Kitchen)",
            [
                "The engine running behind closed doors on the server",
                "Handles heavy processing, business logic, computations",
                "Communicates securely with databases and external services",
                "Keeps secret keys hidden from public eyes"
            ],
            "Use the restaurant dining room and kitchen metaphor. The customer orders in the dining room, but cooking happens in the kitchen."
        )
        add_three_card_slide(
            prs, "Module 3 • File Explorer",
            "De-Coding the Replit File Tree",
            [
                {
                    "title": "App.tsx / index.html",
                    "bullets": [
                        "The main visual layout",
                        "Where titles, buttons, and form inputs live",
                        "Easy to spot English words inside quotes"
                    ]
                },
                {
                    "title": "style.css / Tailwind",
                    "bullets": [
                        "Controls colors, spacing, and styling",
                        "Look for color names like 'bg-blue-600'",
                        "Easy to change theme colors by hand"
                    ]
                },
                {
                    "title": "server.py / index.ts",
                    "bullets": [
                        "The backend server engine",
                        "Listens for user requests",
                        "Dispatches responses and saves data"
                    ]
                }
            ],
            "Show that code files are just organized text documents. Don't fear the file extensions."
        )
        add_two_column_slide(
            prs, "Module 3 • Workflow",
            "The Hybrid Workflow: When to Direct vs. When to Edit",
            "Direct the AI Agent For:",
            [
                "Building complex interactive logic",
                "Writing database schemas and server routes",
                "Connecting third-party integrations",
                "Diagnosing and refactoring buggy code"
            ],
            "Make Direct Micro-Edits For:",
            [
                "Fixing typos in headlines and descriptions",
                "Swapping an image URL or company logo",
                "Tweaking hex colors or button labels",
                "Saves 30 seconds of waiting for an agent re-run"
            ],
            "Demonstrate how fast it is to edit a single headline directly in the code editor versus asking the agent to do it."
        )
        add_lab_slide(
            prs, "Module 3 • Hands-on Lab",
            "Live Lab: Safely Customizing Your App's Code",
            "Open your Part 2 project in the Replit Code Editor view, locate copy and styling, and make safe direct manual edits.",
            [
                "Task 1: Change main headline & subtitle directly in code",
                "Task 2: Swap a color class (e.g. from blue to emerald or violet)",
                "Task 3: Replace an icon or image link with your own URL",
                "Task 4: Use the Agent to add a new interactive modal or banner"
            ],
            [
                "Switch to Code View in Replit",
                "Find human-readable text strings",
                "Edit headline and save file",
                "Watch preview update instantly",
                "Ask agent for one new feature"
            ],
            "Encourage students to break their fear of touching code files. Ctrl+Z (Undo) is always there if they make a mistake."
        )

    elif module_id == 4:
        add_title_slide(
            prs, 4,
            "AI Inside Your Apps",
            "Powering Apps with Built-In AI & Understanding APIs",
            "Today we give our apps their own brain! And the best part: zero API keys or external billing required—we use Replit's built-in AI."
        )
        add_two_column_slide(
            prs, "Module 4 • Concepts",
            "What is an API? (The Restaurant Waiter Metaphor)",
            "The Customer (Your Web App)",
            [
                "The user types text and requests an analysis",
                "App cannot afford supercomputers on user's phone",
                "Needs to send the request to a giant AI data center",
                "Metaphor: Sitting at a table looking at the menu"
            ],
            "The API Waiter (The Messenger)",
            [
                "API = Application Programming Interface",
                "Takes the user prompt from your app over the internet",
                "Delivers prompt to the AI model data center",
                "Carries freshly generated insights back to the screen"
            ],
            "Emphasize that an API is simply a digital messenger. You don't need to understand the supercomputer, just how to send the message."
        )
        add_two_column_slide(
            prs, "Module 4 • Architecture",
            "Two Different AIs in This Course",
            "The Construction AI (Replit Agent)",
            [
                "The builder and software contractor",
                "Writes your code, sets up your files, fixes bugs",
                "Used during the creation and development phase",
                "Talks to YOU, the creator"
            ],
            "The Internal AI (Replit Built-In AI)",
            [
                "The brain installed inside your completed product",
                "Processes user inputs and generates live content",
                "Operates whenever end-users use the live application",
                "Talks to YOUR USERS"
            ],
            "Make sure students clearly understand the difference between the AI that builds the app vs. the AI that runs inside the app."
        )
        add_three_card_slide(
            prs, "Module 4 • Replit Intelligence",
            "Zero Friction: Replit's Native AI Integration",
            [
                {
                    "title": "No External Billing",
                    "bullets": [
                        "No separate OpenAI or Anthropic accounts needed",
                        "No credit cards required for workshop participants",
                        "Eliminates 100% of payment/setup friction"
                    ]
                },
                {
                    "title": "Built-In AI Models",
                    "bullets": [
                        "Replit provides integrated access to powerful LLMs",
                        "Agent wires up the backend connection automatically",
                        "Environment handles security behind the scenes"
                    ]
                },
                {
                    "title": "Prompts Inside Prompts",
                    "bullets": [
                        "You tell the agent: 'Hook up AI to critique pitches'",
                        "You define the internal system persona",
                        "Instant intelligent responses in your UI"
                    ]
                }
            ],
            "Highlight the convenience of Replit's native AI: students can jump straight into building without billing hurdles."
        )
        add_lab_slide(
            prs, "Module 4 • Hands-on Lab",
            "Live Lab: Build 'The Pitch Doctor' AI Assistant",
            "Direct Replit Agent to build an interactive AI tool using Replit's built-in intelligence to critique and improve user inputs.",
            [
                "Option A: The Pitch Doctor (Pastes startup pitch, selects tone: Brutal VC or Gentle Coach, gets 1-10 rating & advice)",
                "Option B: Cold Email Polish Assistant (Pastes draft, selects goal, gets 3 high-converting rewrites)",
                "Option C: Jargon Buster (Pastes complex legal/medical jargon, explains it with 5th-grade analogies)"
            ],
            [
                "Prompt Replit Agent for AI app",
                "Define persona in prompt spec",
                "Test live generation with sample text",
                "Verify formatted response card",
                "Share your favorite AI output in chat!"
            ],
            "Help students experiment with different system personas (e.g. 'Act like a Shakespearean poet' or 'Act like an aggressive venture capitalist')."
        )

    elif module_id == 5:
        add_title_slide(
            prs, 5,
            "Databases & Memory",
            "Building Applications That Remember Everything",
            "Today we give our apps permanent memory. No more amnesia when refreshing the browser!"
        )
        add_two_column_slide(
            prs, "Module 5 • Core Problem",
            "The Refresh Test: The Problem with 'Amnesia Apps'",
            "Stateless Apps (Temporary Memory)",
            [
                "Data lives only in browser temporary memory (RAM)",
                "Refresh the tab or close the browser ➔ data is lost!",
                "Open on your phone ➔ completely blank screen",
                "Great for quick calculators, bad for real businesses"
            ],
            "Stateful Apps (Persistent Memory)",
            [
                "Data is safely stored in a cloud database",
                "Refresh 100 times ➔ all records remain intact",
                "Multiple users can view and contribute simultaneously",
                "The foundation of real software (Instagram, Airbnb)"
            ],
            "Show the pain point: refresh a form and watch everything vanish. Then show the superpower of a database."
        )
        add_three_card_slide(
            prs, "Module 5 • Concepts",
            "What is a Database? (A Supercharged Spreadsheet)",
            [
                {
                    "title": "Tables = Tabs",
                    "bullets": [
                        "Each category gets a sheet",
                        "Examples: 'Users', 'Pitches', 'Comments'",
                        "Neat, isolated data buckets"
                    ]
                },
                {
                    "title": "Columns = Categories",
                    "bullets": [
                        "The headers at the top of the sheet",
                        "Name, Score, Feedback, Created_At",
                        "Defines what data is tracked"
                    ]
                },
                {
                    "title": "Rows & IDs = Records",
                    "bullets": [
                        "Each user submission adds one row",
                        "Every row gets a unique ID number",
                        "Allows instant sorting, searching & upvoting"
                    ]
                }
            ],
            "Relate databases to Google Sheets or Excel. It removes 100% of the mathematical intimidation of database theory."
        )
        add_two_column_slide(
            prs, "Module 5 • Architecture",
            "User Accounts: The Hotel Keycard System",
            "Registration & Passwords",
            [
                "User creates an account with email and password",
                "Database securely scrambles (hashes) password",
                "Creates unique record: User #402"
            ],
            "Sessions & Permissions (The Keycard)",
            [
                "App issues a secure digital session token",
                "Like a hotel room keycard tapping into Room 402",
                "App automatically filters: 'Show only User #402's notes'"
            ],
            "Explain user auth using the hotel keycard metaphor. Replit Agent sets up the security cryptography automatically."
        )
        add_lab_slide(
            prs, "Module 5 • Hands-on Lab",
            "Live Lab: Adding History & Upvotes to Your AI App",
            "Instruct Replit Agent to attach a persistent database to save every generated item and render a public community feed.",
            [
                "Feature 1: Persist every AI review into database tables",
                "Feature 2: Add a 'Community Feed' or 'History Gallery' below the form",
                "Feature 3: Add an interactive Upvote / Heart counter to each saved card",
                "Feature 4: Allow sorting by 'Most Upvoted' vs. 'Most Recent'"
            ],
            [
                "Prompt agent to add database tables",
                "Submit test data into your form",
                "Confirm data appears in history feed",
                "Perform the 'Refresh Test' to verify!",
                "Upvote another classmate's entry"
            ],
            "Have students do the definitive test: close the browser tab completely, reopen it, and celebrate when their data is still there."
        )

    elif module_id == 6:
        add_title_slide(
            prs, 6,
            "Launching & The AI Architect Mindset",
            "Debugging, One-Click Deployment & Your Future as a Builder",
            "Welcome to the finale! Today we conquer error debugging, launch to the global web with custom domains, and celebrate graduations."
        )
        add_three_card_slide(
            prs, "Module 6 • Problem Solving",
            "The 3-Step Agent Debugging Triage",
            [
                {
                    "title": "1. Copy the Error",
                    "bullets": [
                        "Red console text is NOT a failure; it is a clue",
                        "Copy the exact error message from the preview/terminal",
                        "Errors tell agents exact files and line numbers"
                    ]
                },
                {
                    "title": "2. Feed to Agent",
                    "bullets": [
                        "Paste error calmly into Replit Agent chat",
                        "State what you were trying to do",
                        "Watch the agent diagnose and auto-repair"
                    ]
                },
                {
                    "title": "3. Visual Debugging",
                    "bullets": [
                        "For layout or visual glitches, take a screenshot",
                        "Upload screenshot directly into Agent chat",
                        "Say: 'Fix the card alignment shown here'"
                    ]
                }
            ],
            "Normalize bugs: Senior staff engineers Google error messages every hour. In Replit, errors give the agent exact instructions."
        )
        add_two_column_slide(
            prs, "Module 6 • Production",
            "Development Workspace vs. Global Production Deployment",
            "Development Workspace",
            [
                "Your private workshop and digital workbench",
                "Changes appear live in real time",
                "Goes to sleep when you close your laptop",
                "Designed for testing, experimenting, and tweaking"
            ],
            "Production Cloud Deployment",
            [
                "Packaged on high-speed global cloud servers",
                "Runs 24/7/365 with 99.9% uptime",
                "Handles thousands of simultaneous visitors",
                "Connect your own custom domain (e.g. mycoolapp.com)"
            ],
            "Explain the difference between working in the kitchen vs. opening the doors to the public restaurant."
        )
        add_two_column_slide(
            prs, "Module 6 • The Mindset",
            "The Transformation: You Are an AI Software Architect",
            "The Old World (Observer)",
            [
                "Limited by whatever off-the-shelf software existed",
                "Dependent on engineering backlogs and quotes",
                "Intimidated by programming jargon and syntax",
                "Ideas remained trapped in notebooks"
            ],
            "The New World (Architect)",
            [
                "You translate business problems into software specs",
                "Direct autonomous AI agents to build MVPs in hours",
                "Test real products with real users on the real web",
                "Your super-power: Taste, empathy, and clear thinking"
            ],
            "Deliver an inspiring closing speech. Reiterate that the barrier to building software has dropped to zero."
        )
        add_lab_slide(
            prs, "Module 6 • Graduation",
            "Live Capstone Showcase: 2-Minute Lightning Demos",
            "Deploy your finished app to production, share your public URL in the chat, and present your 2-minute lightning demo!",
            [
                "1. Click 'Deploy' in Replit and generate your public live URL",
                "2. Share the URL in the workshop chat for everyone to test",
                "3. Deliver your 2-Minute Demo: What problem does it solve? What AI feature are you proud of?"
            ],
            [
                "Click Deploy in Replit",
                "Verify live production URL works",
                "Post URL in group chat",
                "Present 2-minute lightning demo",
                "Receive course graduation badge!"
            ],
            "Run student show-and-tell. Celebrate every single app built. Encourage students to keep building on Replit."
        )

def main():
    prs_master = Presentation()
    prs_master.slide_width = Inches(13.333)
    prs_master.slide_height = Inches(7.5)
    
    module_names = [
        "Demystifying_AI_and_Replit",
        "The_Art_of_the_Spec",
        "Peeking_Under_the_Hood",
        "AI_Inside_Your_Apps",
        "Databases_and_Memory",
        "Launching_Debugging_and_Mindset"
    ]
    
    # Build Master Deck (All 6 modules)
    print("Building Master Course Deck...")
    for mod_id in range(1, 7):
        build_module_slides(prs_master, mod_id)
        
    master_path = os.path.join(OUTPUT_DIR, "Master_Course_Deck.pptx")
    prs_master.save(master_path)
    print(f"Saved: {master_path}")
    
    # Build Individual Module Decks for focused session delivery
    for mod_id in range(1, 7):
        print(f"Building Module {mod_id} Deck...")
        prs_single = Presentation()
        prs_single.slide_width = Inches(13.333)
        prs_single.slide_height = Inches(7.5)
        build_module_slides(prs_single, mod_id)
        
        filename = f"Module_{mod_id}_{module_names[mod_id-1]}.pptx"
        single_path = os.path.join(OUTPUT_DIR, filename)
        prs_single.save(single_path)
        print(f"Saved: {single_path}")

if __name__ == "__main__":
    main()
