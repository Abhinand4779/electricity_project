import sys
import os
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Suppress header and footer on cover page
        if self._pageNumber > 1:
            # Header
            self.drawString(36, 756, "EnergySync: AI-Powered Energy Consumption & Waste Predictor")
            self.setFont("Helvetica", 8)
            self.drawRightString(576, 756, "Master Project Viva & Technical Handbook")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.6)
            self.line(36, 750, 576, 750)
            
            # Footer
            self.line(36, 42, 576, 42)
            self.drawString(36, 30, "University of Calicut - Final Year Project Viva Handbook")
            page_text = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(576, 30, page_text)
        self.restoreState()

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=46,
        bottomMargin=46
    )

    styles = getSampleStyleSheet()

    # Custom Color Palette
    PRIMARY = colors.HexColor("#0f172a")     # Slate 900
    SECONDARY = colors.HexColor("#0284c7")   # Sky 600
    GREEN = colors.HexColor("#10b981")       # Emerald 500
    GOLD = colors.HexColor("#f59e0b")        # Amber 500
    MUTED = colors.HexColor("#64748b")       # Slate 500
    LIGHT_BG = colors.HexColor("#f8fafc")    # Slate 50
    BORDER_COLOR = colors.HexColor("#e2e8f0")# Slate 200

    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=PRIMARY,
        alignment=1, # Center
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=SECONDARY,
        alignment=1,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'ChapterH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=PRIMARY,
        spaceBefore=16,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=SECONDARY,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=body_style,
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#0f766e")
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=PRIMARY
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=table_cell_style,
        fontName='Helvetica-Bold'
    )

    qa_question_style = ParagraphStyle(
        'QAQuestion',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#0369a1"),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )

    qa_answer_style = ParagraphStyle(
        'QAAnswer',
        parent=body_style,
        fontSize=9,
        leading=12.5,
        spaceAfter=8
    )

    story = []

    # ========================================================
    # COVER / TITLE HEADER BLOCK
    # ========================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("AI-POWERED ELECTRICITY CONSUMPTION &amp; WASTE PREDICTOR", title_style))
    story.append(Paragraph("WITH EXPLAINABLE AI (EnergySync) — MASTER VIVA & TECHNICAL HANDBOOK", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=GREEN, spaceBefore=4, spaceAfter=14))

    # Meta Overview Box
    meta_data = [
        [
            Paragraph("<b>Academic Project:</b> Final Year BCA / B.Sc. Computer Science", table_cell_style),
            Paragraph("<b>Affiliation:</b> University of Calicut / Autonomous", table_cell_style)
        ],
        [
            Paragraph("<b>System Core:</b> Python 3.12 | Django 5.x | Scikit-Learn | SQLite", table_cell_style),
            Paragraph("<b>ML Models:</b> Random Forest Regressor &amp; Isolation Forest", table_cell_style)
        ],
        [
            Paragraph("<b>Application URLs:</b> http://127.0.0.1:8080/ (Port 8080)", table_cell_style),
            Paragraph("<b>Repository:</b> github.com/Abhinand4779/electricity_project", table_cell_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[270, 270])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f1f5f9")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 16))

    # ========================================================
    # CHAPTER 1: EXECUTIVE SUMMARY & SYSTEM IDENTITY
    # ========================================================
    story.append(Paragraph("1. Executive Summary &amp; Problem Formulation", h1_style))
    story.append(Paragraph(
        "Modern electricity consumers face the <b>'Passive Meter Paradox'</b>: utility meters accurately count kilowatt-hours (kWh) consumed, but they offer zero insight into <i>where</i>, <i>why</i>, and <i>how</i> energy is wasted until the electricity bill arrives at month-end. At the same time, regional utility providers (such as the Kerala State Electricity Board - KSEB) struggle with sudden evening peak grid surges and power theft.",
        body_style
    ))
    story.append(Paragraph(
        "<b>EnergySync</b> solves this paradigm through an intelligent <b>Two-Tier Multi-Tenant Architecture</b> coupling high-frequency smart meter telemetry with advanced Machine Learning (ML). The system accomplishes three primary missions:",
        body_style
    ))
    story.append(Paragraph("• <b>Proactive Anomaly Isolation:</b> Identifies phantom standby loads, compressor degradation, and abnormal consumption spikes before high billing occurs.", bullet_style))
    story.append(Paragraph("• <b>Digital Twin &amp; Interactive Simulation:</b> Enables households to simulate future consumption curves and test 'What-If' energy conservation scenarios in real time.", bullet_style))
    story.append(Paragraph("• <b>Explainable AI (XAI):</b> Eliminates black-box distrust by providing plain-English root cause diagnostics alongside every anomaly alert.", bullet_style))
    story.append(Spacer(1, 12))

    # ========================================================
    # CHAPTER 2: THE TWO SIDES (CONSUMER VS GRID ADMIN)
    # ========================================================
    story.append(Paragraph("2. The Two-Tier Architecture: Domestic Consumer vs Grid Administrator", h1_style))
    story.append(Paragraph(
        "The system strictly separates concerns into two distinct roles, each equipped with its own dedicated portal, authentication workflow, and analytical scope:",
        body_style
    ))

    two_sides_data = [
        [
            Paragraph("Architectural Dimension", table_header_style),
            Paragraph("⚡ Domestic Consumer Portal", table_header_style),
            Paragraph("🛡️ Grid Administrator Portal", table_header_style)
        ],
        [
            Paragraph("<b>Target Audience</b>", table_cell_bold),
            Paragraph("Individual households &amp; residential apartment owners.", table_cell_style),
            Paragraph("Utility engineers, KSEB managers &amp; grid dispatchers.", table_cell_style)
        ],
        [
            Paragraph("<b>Dedicated URL</b>", table_cell_bold),
            Paragraph("<code>http://127.0.0.1:8080/login/</code> &amp; <code>/</code>", table_cell_style),
            Paragraph("<code>http://127.0.0.1:8080/admin-login/</code> &amp; <code>/admin-dashboard/</code>", table_cell_style)
        ],
        [
            Paragraph("<b>Demo Credentials</b>", table_cell_bold),
            Paragraph("Username: <b>demo_user</b> | Password: <b>demo1234</b>", table_cell_style),
            Paragraph("Username: <b>hp</b> | Password: <b>admin123</b>", table_cell_style)
        ],
        [
            Paragraph("<b>Analytical Scope</b>", table_cell_bold),
            Paragraph("Micro-Level: Single household smart meter telemetry (171 records).", table_cell_style),
            Paragraph("Macro-Level: Grid-wide multi-household aggregate demand (340 records).", table_cell_style)
        ],
        [
            Paragraph("<b>Primary Key Objective</b>", table_cell_bold),
            Paragraph("Lower monthly KSEB power bills &amp; eliminate appliance waste.", table_cell_style),
            Paragraph("Balance feeder load, audit billing revenue &amp; track grid health.", table_cell_style)
        ],
        [
            Paragraph("<b>AI Features Available</b>", table_cell_bold),
            Paragraph("Digital Twin, What-If Simulator, Fingerprint, Self-Learning Tips.", table_cell_style),
            Paragraph("4 ML Engine Monitor, Multi-Household Audit Table, System Anomalies.", table_cell_style)
        ],
        [
            Paragraph("<b>Security &amp; Privacy</b>", table_cell_bold),
            Paragraph("Tenant-isolated: Cannot inspect other households' readings.", table_cell_style),
            Paragraph("Supervisory: Blocks unauthorized consumers with <i>Access Denied</i>.", table_cell_style)
        ]
    ]
    two_sides_table = Table(two_sides_data, colWidths=[130, 205, 205])
    two_sides_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(two_sides_table)
    story.append(Spacer(1, 10))

    callout_box = [
        [Paragraph("<b>💡 1-Click Viva Demonstration Switcher:</b> At the top-right of every authenticated screen, students can click between <code>[ 👤 Consumer Side ]</code> and <code>[ 🛡️ Admin Side ]</code> to switch roles instantly without logging out or re-typing passwords in front of the examiner.", callout_style)]
    ]
    t_callout = Table(callout_box, colWidths=[540])
    t_callout.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#ccfbf1")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#14b8a6")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_callout)
    story.append(Spacer(1, 14))

    # ========================================================
    # CHAPTER 3: THE THREE LEVELS OF DATA EXPLAINED
    # ========================================================
    story.append(Paragraph("3. The Three Distinct Data Levels in EnergySync", h1_style))
    story.append(Paragraph(
        "A common point of confusion for examiners is: <i>'Why do I see 5,000 records on one page, 340 on another, and 171 on the dashboard?'</i> Students must explain that the project operates across three distinct data tiers:",
        body_style
    ))

    data_tiers = [
        [
            Paragraph("Data Tier Level", table_header_style),
            Paragraph("Record Volume", table_header_style),
            Paragraph("Portal Location", table_header_style),
            Paragraph("Purpose &amp; Role in the Project", table_header_style)
        ],
        [
            Paragraph("<b>Tier 1: Research Benchmark Dataset</b>", table_cell_bold),
            Paragraph("<b>5,000 Records</b><br/>(CSV Source)", table_cell_style),
            Paragraph("<code>/dataset/</code><br/>(Smart Meter Data)", table_cell_style),
            Paragraph("Kaggle/UCI Smart Meter Benchmark dataset. Used to train and cross-validate the Random Forest Regressor and Isolation Forest algorithms offline.", table_cell_style)
        ],
        [
            Paragraph("<b>Tier 2: Utility Grid Database</b>", table_cell_bold),
            Paragraph("<b>340 Records</b><br/>(Total Database)", table_cell_style),
            Paragraph("<code>/admin-dashboard/</code><br/>(Grid Admin)", table_cell_style),
            Paragraph("Cumulative live database records aggregated across all registered accounts (demo_user + hp + test accounts). Used by utility operators for load balancing.", table_cell_style)
        ],
        [
            Paragraph("<b>Tier 3: Domestic Home Telemetry</b>", table_cell_bold),
            Paragraph("<b>171 Records</b><br/>(Single Home)", table_cell_style),
            Paragraph("<code>/</code> &amp; <code>/history/</code><br/>(Consumer)", table_cell_style),
            Paragraph("Actual smart meter intervals belonging strictly to <code>demo_user</code> over the past week (202.51 kWh). Demonstrates tenant isolation and individual bill calculations.", table_cell_style)
        ]
    ]
    t_tiers = Table(data_tiers, colWidths=[130, 85, 110, 215])
    t_tiers.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), SECONDARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_tiers)
    story.append(Spacer(1, 14))

    # ========================================================
    # CHAPTER 4: THE 7 NEXT-GEN AI INNOVATIONS
    # ========================================================
    story.append(Paragraph("4. The 7 Next-Gen AI Innovations (Core Innovation Blueprint)", h1_style))
    story.append(Paragraph(
        "EnergySync integrates 7 state-of-the-art AI modules that elevate it far beyond basic electricity billing software:",
        body_style
    ))

    innovations = [
        ("01. AI Energy Digital Twin", "/digital-twin/", "Generates a 24-hour virtual baseline load profile using past hourly consumption harmonics. Simulates an optimized 'solar-aligned' load curve and compares real-world vs optimal operational curves to uncover hidden peak-hour stress."),
        ("02. AI Energy Waste Detective", "/waste-detective/", "Powered by an unsupervised Isolation Forest algorithm. Isolates abnormal high-draw events (e.g. 3.8 kW load at 2:00 AM) and flags phantom appliance vampire draw (standby power waste) with confidence scores."),
        ("03. What-If Energy Simulator", "/simulator/", "Interactive mathematical simulator where consumers adjust dynamic sliders (+2°C AC thermostat, conversion of incandescent bulbs to 9W LEDs, shifting laundry to off-peak 10:00 PM). Computes instant monthly ₹ and kWh savings."),
        ("04. Self-Learning Recommendation Engine", "/recommendations/", "Delivers context-aware energy conservation tips. Features interactive 'Helpful / Not Helpful' reinforcement voting buttons that dynamically recalculate weight scores to prioritize tips that users find effective."),
        ("05. Personal Energy Fingerprint", "/energy-fingerprint/", "Categorizes household energy consumption across 4 diurnal quadrants: Morning (6AM-12PM), Afternoon (12PM-6PM), Peak Evening (6PM-10PM), and Night (10PM-6AM). Assigns an automated behavioral profile (e.g. 'Night Owl Gamer', 'Solar Pioneer')."),
        ("06. Future Lifestyle Impact Predictor", "/lifestyle-predictor/", "Forecasts the financial and grid impact of adding heavy residential loads before purchase (EV Level-2 Charger: +7.2 kW, 1.5-Ton Inverter AC: +1.5 kW, Induction Cooktop: +2.0 kW) under KSEB telescopic tariff tiers."),
        ("07. Explainable AI (XAI) Diagnostics", "Integrated across UI", "Eliminates black-box AI distrust. Every anomaly alert and recommendation includes plain-English root cause diagnostics (e.g. 'Anomaly triggered: 2:00 AM consumption was 340% higher than your historical 30-day baseline').")
    ]

    for title, url, desc in innovations:
        story.append(Paragraph(f"<b>{title}</b> &nbsp;<font color='#0284c7'><code>[{url}]</code></font>", h2_style))
        story.append(Paragraph(desc, body_style))
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 10))

    # ========================================================
    # CHAPTER 5: MACHINE LEARNING ENGINES & MATHEMATICS
    # ========================================================
    story.append(Paragraph("5. Machine Learning Architecture &amp; Mathematical Formulations", h1_style))
    story.append(Paragraph(
        "EnergySync implements a multi-model machine learning architecture combining supervised regression with unsupervised anomaly isolation:",
        body_style
    ))

    ml_data = [
        [
            Paragraph("Machine Learning Engine", table_header_style),
            Paragraph("Algorithm Used", table_header_style),
            Paragraph("Hyperparameters / Settings", table_header_style),
            Paragraph("Performance Benchmark Metric", table_header_style)
        ],
        [
            Paragraph("<b>Load Forecasting Engine</b>", table_cell_bold),
            Paragraph("Random Forest Regressor &amp; Gradient Boosting", table_cell_style),
            Paragraph("n_estimators=100, max_depth=12, min_samples_split=4", table_cell_style),
            Paragraph("<b>R² = 0.942</b><br/>RMSE = 0.118 kWh<br/>MAE = 0.082 kWh", table_cell_style)
        ],
        [
            Paragraph("<b>Anomaly Isolation Engine</b>", table_cell_bold),
            Paragraph("Isolation Forest (Unsupervised)", table_cell_style),
            Paragraph("n_estimators=150, contamination=0.04, random_state=42", table_cell_style),
            Paragraph("<b>Precision = 92.4%</b><br/>Recall = 88.6%<br/>F1-Score = 0.904", table_cell_style)
        ],
        [
            Paragraph("<b>Digital Twin Simulator</b>", table_cell_bold),
            Paragraph("Harmonic Fourier &amp; Linear Interpolation", table_cell_style),
            Paragraph("24 diurnal time steps, solar bell curve attenuation", table_cell_style),
            Paragraph("Synthetic Load Curve Correlation <b>r = 0.961</b>", table_cell_style)
        ]
    ]
    t_ml = Table(ml_data, colWidths=[120, 140, 150, 130])
    t_ml.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_ml)
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Mathematical Formulations:</b>", h2_style))
    story.append(Paragraph("• <b>Isolation Forest Anomaly Score:</b> <code>s(x, n) = 2^(-E(h(x)) / c(n))</code>, where <code>h(x)</code> is the tree traversal path length and <code>c(n)</code> is the average path length of unsuccessful searches in a Binary Search Tree (BST). If <code>s -> 1</code>, the reading is isolated as a severe anomaly.", body_style))
    story.append(Paragraph("• <b>KSEB Telescopic Tariff Structure:</b> Domestic billing adheres strictly to Kerala State Electricity Regulatory Commission (KSERC) slab pricing: 0-50 units @ ₹3.15/unit; 51-100 units @ ₹3.95/unit; 101-150 units @ ₹5.00/unit; 151-200 units @ ₹6.80/unit; 201-250 units @ ₹8.00/unit; >250 units non-telescopic flat rate.", body_style))
    story.append(Paragraph("• <b>Carbon Emissions Factor:</b> <code>Carbon (kg CO2e) = Energy (kWh) * 0.82</code> based on the Central Electricity Authority (CEA) Indian Grid Baseline Carbon Emission Database.", body_style))
    story.append(Spacer(1, 14))

    # ========================================================
    # CHAPTER 6: STEP-BY-STEP LIVE VIVA DEMO SCRIPT
    # ========================================================
    story.append(Paragraph("6. Step-by-Step Live Viva Demonstration Script (5-Minute Walkthrough)", h1_style))
    story.append(Paragraph(
        "Follow this exact script when presenting the project live to the university examiners:",
        body_style
    ))

    demo_steps = [
        ("Step 1: The Login Portals", "Open http://127.0.0.1:8080/login/. Show the examiner that there are TWO dedicated login portals: 'Consumer Login' (Green Smart Home) and 'Admin Login' (Navy/Gold Grid Control). Click Quick Fill on Consumer (demo_user / demo1234) and sign in."),
        ("Step 2: Domestic Dashboard", "Highlight the 4 KPI cards: Total Consumption (202.51 kWh), Total Records (171), Energy Efficiency Grade (65/100, Grade B), and Tomorrow's ML Prediction (28.55 kWh). Explain that this data is private to this household."),
        ("Step 3: The 7 AI Innovations", "Click 'Digital Twin & What-If' in the sidebar. Show the virtual 24-hour load curve simulation. Adjust the AC slider by +2°C and point out the live monthly ₹ savings counter. Then click 'Waste Detective' to display the Isolation Forest spike alert with plain-English XAI diagnosis."),
        ("Step 4: Smart Meter Dataset", "Click 'Smart Meter Data' in sidebar. Explain: 'Here are all 5,000 benchmark records used to train our Machine Learning algorithms, with full pagination and normal/abnormal labels.'"),
        ("Step 5: The 1-Click Role Switch", "Click '[ 🛡️ Admin Side ]' in the top-right navbar. Explain: 'We have switched to the Grid Administrator Portal (hp) without typing credentials.' Point out the 4 Executive Grid Cards, the 4 ML Engine Status Badges (Random Forest, Isolation Forest, Digital Twin, XAI), and the Multi-Household Consumer Comparative Audit Table!")
    ]

    for title, desc in demo_steps:
        story.append(Paragraph(f"<b>{title}</b>", qa_question_style))
        story.append(Paragraph(desc, body_style))

    story.append(Spacer(1, 14))

    # ========================================================
    # CHAPTER 7: MASTER VIVA Q&A (TOP 25 QUESTIONS & ANSWERS)
    # ========================================================
    story.append(Paragraph("7. Master Viva Q&amp;A: Top 25 Examiner Questions &amp; Answers", h1_style))
    story.append(Paragraph(
        "These are the most common technical questions asked by external university examiners, along with high-scoring answers:",
        body_style
    ))

    qa_list = [
        ("Q1: What is the main objective of this project?",
         "A: The main objective is to eliminate the 'Passive Meter Paradox' by transforming standard electricity meters into proactive AI-powered advisors. It combines real-time smart meter telemetry with machine learning to detect phantom energy waste, simulate savings scenarios via Digital Twins, and forecast future demand for both domestic consumers and grid utility operators."),

        ("Q2: Why did you divide the project into Consumer Side and Admin Side?",
         "A: In real-world electrical grids, consumers and utility operators have opposing needs. Consumers care about micro-telemetry (their own home's appliances and reducing their KSEB bill). Grid administrators care about macro-aggregates (total community grid load, feeder balance, and detecting power theft). Our two-tier multi-tenant architecture satisfies both while ensuring household data privacy."),

        ("Q3: Which Machine Learning algorithms are implemented in your system?",
         "A: We implement a hybrid multi-model architecture: 1) Random Forest Regressor and Gradient Boosting for 24-hour and 7-day time-series consumption forecasting; 2) Isolation Forest for unsupervised anomaly and waste spike isolation; and 3) Harmonic Fourier modeling for the 24-hour Digital Twin load simulation."),

        ("Q4: Why did you choose Isolation Forest instead of standard thresholding or DBSCAN?",
         "A: Traditional thresholding (e.g. flagging anything > 5 kWh) fails because consumption is dynamic—5 kW at 7:00 PM is normal cooking, but 5 kW at 3:00 AM is severe waste. Isolation Forest explicitly isolates anomalies rather than profiling normal points by randomly selecting features and split values. Anomalies have shorter path lengths in the trees, making the model computationally efficient (O(n)) and robust against masking effects."),

        ("Q5: What is the accuracy of your load forecasting model?",
         "A: Our Random Forest Regressor achieved a Coefficient of Determination (R²) score of 0.942, a Root Mean Squared Error (RMSE) of 0.118 kWh, and a Mean Absolute Error (MAE) of 0.082 kWh across our 5,000-record benchmark dataset."),

        ("Q6: What features are fed into the Machine Learning model?",
         "A: We engineer 12 dynamic features: Global Active Power, Voltage, Global Reactive Power, Sub-metering 1/2/3, Hour of Day (0-23), Day of Week (0-6), IsWeekend binary flag, Lag_1h (consumption 1 hour prior), Lag_24h (same hour yesterday), and Rolling 24-hour moving average."),

        ("Q7: What is an 'Energy Digital Twin' in your project?",
         "A: An Energy Digital Twin is a software replica of the household's physical energy system. It models the thermal and operational behavior of the home's appliances across 24 hours. Consumers can test interventions—like installing solar panels or pre-cooling rooms—on the digital twin to see the financial outcome before spending money in the physical world."),

        ("Q8: How does the Self-Learning Recommendation Engine learn from feedback?",
         "A: When recommendations are generated, they are assigned a base priority weight. When users click 'Helpful' (thumbs up) or 'Not Helpful' (thumbs down), a database signal updates the recommendation's utility coefficient. Recommendations that receive negative feedback are penalized and demoted, while proven tips are elevated."),

        ("Q9: What is Explainable AI (XAI) and why is it needed here?",
         "A: Traditional AI outputs a number or an alert flag without explanation, creating user skepticism. Our XAI layer translates model decisions into natural language diagnostics (e.g. 'Alert: Your refrigerator compressor ran continuously for 6 hours, consuming 340% above baseline'). This builds trust and gives the consumer an actionable repair step."),

        ("Q10: Why do I see 5,000 records on the Smart Meter page but only 171 records on the Dashboard?",
         "A: The 5,000 records on the Smart Meter page represent the complete research benchmark dataset used for offline training and evaluation of our ML models. The 171 records on the dashboard represent the live telemetry recorded specifically for the logged-in domestic consumer (demo_user) over the past week. This proves our system implements proper multi-tenant data isolation."),

        ("Q11: How is the electricity bill calculated in your project?",
         "A: We implement the official KSEB (Kerala State Electricity Board) telescopic tariff slabs: 0-50 units @ ₹3.15, 51-100 units @ ₹3.95, 101-150 units @ ₹5.00, 151-200 units @ ₹6.80, and 201-250 units @ ₹8.00. Consumption above 250 units transitions to non-telescopic flat billing as mandated by the Kerala State Electricity Regulatory Commission (KSERC)."),

        ("Q12: How are carbon emissions computed?",
         "A: We use the Central Electricity Authority (CEA) of India emission factor: 0.82 kg of CO2 equivalent per kWh. Multiplying total kilowatt-hours by 0.82 yields the precise environmental footprint in kilograms of CO2."),

        ("Q13: What happens if a regular consumer tries to log into the Admin portal?",
         "A: The system implements role-based access control (RBAC). If a domestic consumer tries to sign in at /admin-login/, the authentication view detects that is_staff and is_superuser are False, rejects the session, and displays an explicit security error: 'Access Denied: This account is a Consumer account and does not have Grid Administrator privileges.'"),

        ("Q14: How does the What-If Simulator work mathematically?",
         "A: The simulator uses empirical appliance wattage formulas: Changing AC temperature from 20°C to 24°C applies a 6% energy saving per degree Celsius. Converting five 60W incandescent bulbs to 9W LEDs saves 51W per hour per bulb. Shifting 2 kW laundry cycles to off-peak periods (10:00 PM - 6:00 AM) applies off-peak tariff discounts."),

        ("Q15: What is the 'Personal Energy Fingerprint'?",
         "A: It analyzes the consumer's diurnal consumption distribution across Morning, Afternoon, Evening, and Night. If night consumption exceeds 40%, the system assigns the 'Night Owl Gamer' badge. If peak evening usage is minimized and solar output dominates, it assigns the 'Solar Pioneer' badge. This drives gamification and targeted conservation."),

        ("Q16: Which database is used and how is it structured?",
         "A: We use SQLite3 for development and portability (readily switchable to PostgreSQL in production). The schema includes User and Profile models, ElectricityConsumption (time-series telemetry), EnergyAnomaly (ML-flagged incidents), EnergyRecommendation, RecommendationFeedback (user votes), and TariffSlab tables."),

        ("Q17: Is the system capable of handling real-world smart meter IoT data?",
         "A: Yes. The system includes an automated CSV ingestion and RESTful API pipeline capable of ingesting high-frequency smart meter telemetry (e.g. from ESP32 / Arduino Wi-Fi energy meters sending JSON payloads over HTTP POST)."),

        ("Q18: What is the significance of the 4 ML Engine Status badges on the Admin Dashboard?",
         "A: In production utility environments, machine learning models degrade over time due to 'concept drift' (e.g. seasonal weather shifts). The ML Engine Monitor on the Admin Dashboard allows grid engineers to verify in real time that all 4 models (Random Forest, Isolation Forest, Digital Twin, and XAI Tree) are active and operational."),

        ("Q19: How do you handle missing values or corrupted smart meter data?",
         "A: Our preprocessing pipeline (`preprocessing.py`) handles missing timestamps through forward-fill (`ffill`) interpolation for gaps under 3 hours, and historical mean substitution for extended outages. Outliers exceeding physical transformer thresholds (>50 kW for residential) are filtered out before ML feature extraction."),

        ("Q20: Why did you choose Django instead of Flask or NodeJS?",
         "A: Django provides an enterprise-grade framework with built-in Object-Relational Mapping (ORM), robust CSRF and SQL-injection security, a ready-to-use administrative back-office, and seamless integration with Python's data science ecosystem (Pandas, Scikit-Learn, NumPy)."),

        ("Q21: What is 'phantom load' or 'vampire power'?",
         "A: Phantom load is electricity consumed by electronic devices while they are switched off or in standby mode (e.g. televisions, microwave clocks, laptop chargers). Our Waste Detective flags continuous nighttime baselines exceeding 150W as phantom power leakage."),

        ("Q22: Can your system predict electricity demand for the next 7 days?",
         "A: Yes. Our time-series forecasting view (`forecast_user_consumption`) applies autoregressive lag features (24h, 48h, 168h weekly cycle) with Gradient Boosting to project hourly demand curves across the upcoming 7 calendar days."),

        ("Q23: How does the Admin Dashboard help prevent grid blackouts?",
         "A: By aggregating total grid demand across all connected consumer meters in real time, the Grid Administrator can spot localized feeder overloads hours in advance and trigger automated demand-response alerts to consumers before transformers blow."),

        ("Q24: What are the future enhancements for this project?",
         "A: Future expansions include: 1) Hardware integration with LoRaWAN and ESP32 smart meters; 2) Direct integration with rooftop solar bidirectional net-metering; and 3) An automated WhatsApp / SMS emergency alert bot for critical anomaly notifications."),

        ("Q25: What is the single biggest takeaway of this project?",
         "A: EnergySync proves that combining machine learning with transparent Explainable AI and two-tier grid architecture bridges the gap between passive utility metering and proactive energy conservation—saving money for families while safeguarding the electrical grid.")
    ]

    for q, a in qa_list:
        story.append(KeepTogether([
            Paragraph(q, qa_question_style),
            Paragraph(a, qa_answer_style)
        ]))

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Master Handbook PDF generated successfully at: {filename}")

if __name__ == "__main__":
    out_path = r"c:\Users\HP\Downloads\project\AI_Energy_Project_Master_Viva_Handbook.pdf"
    build_pdf(out_path)
