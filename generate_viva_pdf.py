import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 755, "AI-Powered Personal Energy Waste Predictor | Final Year Project Viva & Defense Guide")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(54, 747, 558, 747)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 45, 558, 45)
        
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 32, page_str)
        self.drawString(54, 32, "Confidential - Academic Project Examination & Practice Material")
        self.restoreState()

def create_project_viva_pdf(output_filename):
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Custom Palette
    primary_color = colors.HexColor("#0f3d2e")     # Forest Green
    secondary_color = colors.HexColor("#1b7a4b")   # Bright Green
    accent_color = colors.HexColor("#2563eb")      # Blue
    dark_neutral = colors.HexColor("#1e293b")      # Slate 800
    light_bg = colors.HexColor("#f8fafc")          # Slate 50
    callout_bg = colors.HexColor("#f0fdf4")        # Light green bg
    warning_bg = colors.HexColor("#fef3c7")        # Light amber bg
    border_color = colors.HexColor("#e2e8f0")

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=primary_color,
        alignment=1, # Center
        spaceAfter=10
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#475569"),
        alignment=1,
        spaceAfter=20
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=primary_color,
        spaceBefore=16,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=secondary_color,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    q_title_style = ParagraphStyle(
        'QTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=8,
        spaceAfter=2,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=dark_neutral,
        spaceAfter=5
    )

    answer_style = ParagraphStyle(
        'Answer',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=12,
        textColor=colors.HexColor("#334155"),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=12,
        textColor=colors.HexColor("#334155"),
        leftIndent=15,
        spaceAfter=3
    )

    code_style = ParagraphStyle(
        'CodeText',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#0f172a")
    )

    table_header_style = ParagraphStyle(
        'TH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TD',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=dark_neutral
    )

    story = []

    # =========================================================================
    # COVER / HEADER TITLE BLOCK
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("AI-POWERED PERSONAL ENERGY WASTE PREDICTOR", title_style))
    story.append(Paragraph("<b>Comprehensive Final Year Project Defense & Viva Voce Examination Guide</b><br/>Academic Subject: Artificial Intelligence, Machine Learning & Smart Grid Management", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=secondary_color, spaceAfter=15))

    # Meta Info Table
    meta_data = [
        [Paragraph("<b>Project Domain:</b>", table_cell_style), Paragraph("Artificial Intelligence & Machine Learning", table_cell_style),
         Paragraph("<b>Target Audience:</b>", table_cell_style), Paragraph("B.Tech / B.E. / MCA Final Year Students", table_cell_style)],
        [Paragraph("<b>Primary Language:</b>", table_cell_style), Paragraph("Python 3.12, Django 4.2+", table_cell_style),
         Paragraph("<b>Core Models:</b>", table_cell_style), Paragraph("Isolation Forest, Random Forest, LinReg", table_cell_style)],
        [Paragraph("<b>Datasets:</b>", table_cell_style), Paragraph("UCI Household (34k) & Kaggle Smart Meter (5k)", table_cell_style),
         Paragraph("<b>Key Outcomes:</b>", table_cell_style), Paragraph("Waste Loss (kWh/₹), 0-100 Score, 7-Day Forecast", table_cell_style)]
    ]
    t_meta = Table(meta_data, colWidths=[100, 150, 100, 154])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), light_bg),
        ('BOX', (0,0), (-1,-1), 1, border_color),
        ('INNERGRID', (0,0), (-1,-1), 0.5, border_color),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 15))

    # =========================================================================
    # SECTION 1: EXECUTIVE PROJECT OVERVIEW & ELEVATOR PITCHES
    # =========================================================================
    story.append(Paragraph("1. Executive Project Overview & Evaluator Elevator Pitches", h1_style))
    story.append(Paragraph(
        "Students must be able to summarize the project clearly without technical stammering. Prepare these three elevator pitches according to the time allotted by the external examiner.", body_style
    ))
    
    pitches = [
        ("30-Second Rapid Pitch", 
         "\"Our project, EnergySync, is an AI-powered personal energy auditor that detects household electricity wastage, forecasts future demand, and generates personalized conservation schedules. Unlike traditional electric meters that only show total kWh at the end of the month, our system uses an unsupervised Isolation Forest trained on 34,000+ real records to identify midnight vampire loads and surge anomalies in real time, while a Random Forest regressor forecasts 7-day future demand with an R² of 0.84.\""),
        ("2-Minute Technical Summary",
         "\"EnergySync solves the 'blind billing' problem where households waste 15% to 35% of electricity without awareness. The application consists of an automated 4-stage data pipeline: First, data ingestion and preprocessing that deduplicates timestamps, imputes missing environmental data, and extracts temporal periods. Second, a dual-layer ML architecture: an Isolation Forest model for unsupervised anomaly detection and a Random Forest Regressor for non-linear consumption forecasting. Third, an Energy Waste Analysis engine that quantifies midnight idle baseload waste, peak evening surge loss, and converts lost kWh into financial costs and carbon emissions (0.82 kg CO2e/kWh). Finally, it computes a personalized 0-100 Energy Efficiency Score and provides load-shifting appliance timetables.\"")
    ]
    for p_title, p_desc in pitches:
        story.append(Paragraph(f"<b>{p_title}</b>", h2_style))
        story.append(Paragraph(p_desc, answer_style))
        story.append(Spacer(1, 4))

    # =========================================================================
    # SECTION 2: MACHINE LEARNING & AI VIVA QUESTIONS
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("2. Core Machine Learning & AI Technical Questions (Viva Deep-Dive)", h1_style))

    ml_qa = [
        ("Q1: Which Machine Learning algorithms are implemented in this project and what specific role does each play?",
         "The project implements three primary machine learning models and one baseline comparative model as per Section 12 of the academic specifications:<br/>"
         "<b>1. Isolation Forest (Unsupervised Anomaly Detection):</b> Deployed in <code>household_anomaly_model.pkl</code>. Trained on 34,085 hourly records from the UCI Individual Household Electric Power Consumption dataset. It isolates atypical usage patterns (midnight vampire power, sudden spikes) without requiring manual labels.<br/>"
         "<b>2. Random Forest Regressor (Nonlinear Forecasting):</b> Deployed in <code>consumption_predictor.pkl</code>. Comprises 200 estimators to capture multi-variable relationships between weather (temperature, humidity, wind) and temporal features (hour, day of week) to predict future kWh consumption.<br/>"
         "<b>3. Linear Regression (Baseline Comparison):</b> Deployed in <code>linear_regression_predictor.pkl</code>. Evaluates basic linear assumptions and proves why complex nonlinear tree models are required for human consumption habits.<br/>"
         "<b>4. Random Forest Classifier (Supervised Verification):</b> Evaluates multi-parameter smart meter datasets to classify normal vs abnormal intervals."),

        ("Q2: How does the Isolation Forest algorithm mathematically isolate energy anomalies?",
         "Isolation Forest is built on the premise that anomalies are 'few and different'. Unlike density or distance algorithms (like DBSCAN or K-Means) that calculate computationally expensive pairwise distances, Isolation Forest isolates observations by randomly selecting a feature and randomly selecting a split value between the minimum and maximum values of that feature.<br/>"
         "• Normal points reside in dense clusters and require many random splits (deep path length <i>h(x)</i>) to isolate.<br/>"
         "• Anomalies (e.g. 6.8 kWh consumption at 3:00 AM) fall in sparse regions and are isolated near the root of the tree with very short path lengths.<br/>"
         "The anomaly score <i>s(x, n)</i> is defined as: <b>s(x, n) = 2^(-E(h(x)) / c(n))</b>, where <i>E(h(x))</i> is the average path length across 200 trees, and <i>c(n)</i> is the average path length of unsuccessful searches in a Binary Search Tree of <i>n</i> samples. A score above the contamination threshold flags an active anomaly."),

        ("Q3: Why is Random Forest Regressor significantly superior to Linear Regression for electricity prediction?",
         "In our project benchmarks, the Random Forest Regressor achieved an <b>R² score of 0.842</b> and <b>MAE of 0.071 kWh</b>, whereas Linear Regression achieved an <b>R² of only 0.086</b> and <b>MAE of 0.125 kWh</b>.<br/>"
         "The reasons are:<br/>"
         "1. <b>Non-Linear Thermodynamics:</b> Cooling/heating power consumption is non-linear. Below 22°C, air conditioners remain off. As temperature increases past 28°C, AC compressor work spikes exponentially.<br/>"
         "2. <b>Temporal Discontinuity:</b> The transition between 05:00 AM and 07:00 AM represents a sharp step-function in human activity that linear planes cannot represent.<br/>"
         "3. <b>Interaction Effects:</b> High humidity combined with high temperature creates an exaggerated perceived heat index, triggering peak cooling demand. Random Forest splits naturally handle feature interactions without manual polynomial expansion."),

        ("Q4: What feature engineering was conducted on the time-series datasets?",
         "Raw timestamps alone cannot be ingested by tree-based regressors. The automated preprocessing pipeline extracts:<br/>"
         "• <code>Hour</code> (0–23): Diurnal cycle indicator.<br/>"
         "• <code>DayOfWeek</code> (0–6) and <code>IsWeekend</code> (binary): Differentiates commercial workday routines from weekend domestic occupancy.<br/>"
         "• <code>Month</code> (1–12): Captures seasonal HVAC variations.<br/>"
         "• <code>UsagePeriod</code>: Segmented into academic blocks: <i>Night (00:00–05:59)</i>, <i>Morning (06:00–11:59)</i>, <i>Afternoon (12:00–16:59)</i>, and <i>Evening (17:00–23:59)</i>.<br/>"
         "• <code>Avg_Past_Consumption</code>: Rolling historical baseline representing the consumer's typical consumption level."),

        ("Q5: What datasets were utilized to train and evaluate the models?",
         "1. <b>UCI Machine Learning Repository: Individual Household Electric Power Consumption Dataset:</b> Contains 34,085 cleaned hourly records collected from a residential household over 4 years. Used for training the unsupervised Isolation Forest model.<br/>"
         "2. <b>Kaggle Smart Meter Electricity Consumption Dataset:</b> 5,000 interval observations containing environmental attributes (Temperature, Humidity, Wind Speed) paired with actual anomaly labels. Used for regression benchmarking and supervised classifier evaluation.")
    ]

    for q, a in ml_qa:
        story.append(Paragraph(q, q_title_style))
        story.append(Paragraph(a, answer_style))
        story.append(Spacer(1, 3))

    story.append(PageBreak())

    # =========================================================================
    # SECTION 3: MATHEMATICAL FORMULATIONS & DOMAIN LOGIC
    # =========================================================================
    story.append(Paragraph("3. Mathematical Formulations & Domain Logic", h1_style))
    story.append(Paragraph(
        "Examiners frequently test students on the mathematical and statistical formulas implemented in the codebase.", body_style
    ))

    math_qa = [
        ("Q6: How is the Personalized Energy Efficiency Score (0 to 100) calculated?",
         "The Efficiency Score is an academic multi-attribute index calculated inside <code>consumption/efficiency_score.py</code>:<br/>"
         "<b>Total Score = P_anomaly + P_baseload + P_peak + P_stability (bounded between 0 and 100)</b><br/>"
         "• <b>1. Anomaly Penalty (P_anomaly, max 35 pts):</b> Evaluates the proportion of abnormal intervals: <code>P_anomaly = max(5, int(35 * (1 - min(anomaly_ratio * 4.0, 0.85))))</code>.<br/>"
         "• <b>2. Midnight Baseload Inefficiency (P_baseload, max 25 pts):</b> Computes the ratio of night consumption (00:00–05:59) to daytime average. Ratios &le; 0.35 earn 25 pts; ratios &gt; 0.85 drop to 6 pts.<br/>"
         "• <b>3. Peak-to-Average Ratio (P_peak, max 25 pts):</b> Computes <code>95th_percentile / mean_kwh</code>. Ratios &le; 1.8 earn 25 pts; excessive spikes (&gt; 3.5) drop to 5 pts.<br/>"
         "• <b>4. Usage Stability (P_stability, max 15 pts):</b> Measures the Coefficient of Variation (CoV = &sigma; / &mu;). CoV &le; 0.40 earns 15 pts; chaotic variance drops to 3 pts.<br/>"
         "<b>Grade Mapping:</b> 88–100: Grade A+ | 78–87: Grade A | 65–77: Grade B | 50–64: Grade C | Below 50: Grade D."),

        ("Q7: What is the mathematical formula used for Energy Waste Estimation?",
         "Energy waste is estimated inside <code>consumption/waste_analysis.py</code> as the sum of three independent inefficiency mechanisms:<br/>"
         "<b>Total Waste (kWh) = W_baseload + (0.7 * W_anomaly) + W_peak</b><br/>"
         "• <b>Baseload / Standby Waste (W_baseload):</b> During midnight hours (00:00–05:59), the minimum 20th percentile represents unavoidable refrigerator/router baseload. Any night draw exceeding 1.4x of this baseline is classified as vampire power waste.<br/>"
         "• <b>Anomaly Waste (W_anomaly):</b> The cumulative sum of kWh in flagged anomaly records exceeding the user's historical mean.<br/>"
         "• <b>Peak Evening Spikes (W_peak):</b> Demand occurring between 18:00–22:00 that exceeds the 85th percentile of normal consumption.<br/>"
         "• <b>Financial Impact:</b> <code>Waste (kWh) * ₹8.00/kWh (Tariff Rate)</code>.<br/>"
         "• <b>Carbon Emissions:</b> <code>Waste (kWh) * 0.82 kg CO2e/kWh (Grid Emission Factor)</code>.")
    ]

    for q, a in math_qa:
        story.append(Paragraph(q, q_title_style))
        story.append(Paragraph(a, answer_style))
        story.append(Spacer(1, 3))

    # Benchmark Comparison Table
    story.append(Spacer(1, 5))
    story.append(Paragraph("<b>Table 1: Algorithm Evaluation & Benchmark Metrics (Section 12 Compliance)</b>", h2_style))
    table_data = [
        [Paragraph("<b>Algorithm</b>", table_header_style), Paragraph("<b>Paradigm</b>", table_header_style),
         Paragraph("<b>Primary Metric</b>", table_header_style), Paragraph("<b>Secondary Metric</b>", table_header_style),
         Paragraph("<b>Selected Role</b>", table_header_style)],
        [Paragraph("Random Forest Regressor", table_cell_style), Paragraph("Supervised Ensemble", table_cell_style),
         Paragraph("R²: 0.8420", table_cell_style), Paragraph("MAE: 0.0712 kWh", table_cell_style), Paragraph("Primary Demand Predictor", table_cell_style)],
        [Paragraph("Linear Regression", table_cell_style), Paragraph("Supervised Linear", table_cell_style),
         Paragraph("R²: 0.0862", table_cell_style), Paragraph("MAE: 0.1246 kWh", table_cell_style), Paragraph("Baseline Benchmark", table_cell_style)],
        [Paragraph("Isolation Forest", table_cell_style), Paragraph("Unsupervised Ensembles", table_cell_style),
         Paragraph("Contamination: 2.0%", table_cell_style), Paragraph("Trained: 34,085 UCI rows", table_cell_style), Paragraph("Real-Time Anomaly Engine", table_cell_style)],
        [Paragraph("Random Forest Classifier", table_cell_style), Paragraph("Supervised Tree Ensemble", table_cell_style),
         Paragraph("Accuracy: 98.8%", table_cell_style), Paragraph("F1-Score: 0.892", table_cell_style), Paragraph("Multi-Feature Classifier", table_cell_style)]
    ]
    t_bench = Table(table_data, colWidths=[110, 100, 95, 95, 104])
    t_bench.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('BOX', (0,0), (-1,-1), 1, border_color),
        ('INNERGRID', (0,0), (-1,-1), 0.5, border_color),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_bench)
    story.append(Spacer(1, 10))

    # =========================================================================
    # SECTION 4: FULL-STACK ARCHITECTURE & SOFTWARE DESIGN
    # =========================================================================
    story.append(Paragraph("4. System Architecture, Django & Database Questions", h1_style))

    arch_qa = [
        ("Q8: Why was Django chosen as the backend web framework instead of Flask or FastAPI?",
         "While Flask and FastAPI are lightweight, Django provides an enterprise-ready 'batteries-included' architecture essential for full-stack data projects:<br/>"
         "1. <b>Object-Relational Mapping (ORM):</b> Built-in query optimization, schema migrations, and indexing.<br/>"
         "2. <b>Security Controls:</b> Out-of-the-box CSRF protection, SQL injection prevention, clickjacking protection, and secure password hashing (PBKDF2 SHA-256).<br/>"
         "3. <b>Multi-User Isolation:</b> Individual user authentication isolates historical records and custom anomalies."),

        ("Q9: What database schema was designed to support the system?",
         "The database contains 5 core interconnected models inside <code>consumption/models.py</code>:<br/>"
         "• <code>ElectricityConsumption</code>: Stores historical records (user foreign key, timestamp, energy_kwh, temperature, source: manual/dataset). Indexed by (user, recorded_at).<br/>"
         "• <code>ConsumptionPrediction</code>: Stores forecast targets, predicted kWh values, and algorithm names.<br/>"
         "• <code>EnergyAnomaly</code>: Foreign key to ElectricityConsumption, anomaly score, description, and resolution boolean.<br/>"
         "• <code>EnergyRecommendation</code>: Title, description, estimated savings (kWh), and completion status.<br/>"
         "• <code>EnergyEfficiencyScore</code>: Numeric score (0–100), period start/end dates, and computation timestamp."),

        ("Q10: How does the preprocessing engine clean dirty smart meter data?",
         "Implemented in <code>clean_and_preprocess_dataframe()</code>:<br/>"
         "1. <b>Header Normalization:</b> Maps heterogeneous column names (e.g. 'power', 'kwh', 'energy') to canonical fields.<br/>"
         "2. <b>Deduplication:</b> Removes duplicate timestamp intervals using <code>df.drop_duplicates(subset=['recorded_at'])</code>.<br/>"
         "3. <b>Imputation:</b> Replaces missing temperature values with the median of historical readings.<br/>"
         "4. <b>Validation:</b> Drops negative values and invalid timestamps.")
    ]

    for q, a in arch_qa:
        story.append(Paragraph(q, q_title_style))
        story.append(Paragraph(a, answer_style))
        story.append(Spacer(1, 3))

    story.append(PageBreak())

    # =========================================================================
    # SECTION 5: EXAMINER "GRILL" / DEFENSE TRAP QUESTIONS
    # =========================================================================
    story.append(Paragraph("5. Examiner Defense Trap Questions (\"Grill Questions\")", h1_style))
    story.append(Paragraph(
        "External examiners specifically ask these difficult questions to test whether students truly understand the limitations and design choices of the project.", body_style
    ))

    trap_qa = [
        ("Trap Q1: \"If a resident buys an Electric Vehicle (EV) and charges it overnight, won't your Isolation Forest falsely flag it as a midnight waste anomaly?\"",
         "<b>How to Answer Confidently:</b><br/>"
         "\"Yes, initially an unexpected 7 kW EV charging session will be flagged as an anomaly because it deviates from historical baseload. However, our system provides an explicit <b>Anomaly Resolution feature ('Mark Resolved')</b> and includes a dedicated <b>Appliance Operating Schedule</b> that designates 11:00 PM – 05:00 AM specifically for EV charging. Furthermore, in future enhancements, we can introduce clustered load profiling (clustering consecutive high draws into known EV profiles) to distinguish purposeful scheduled charging from unintended vampire power waste.\""),

        ("Trap Q2: \"Why didn't you use Deep Learning (LSTM / GRU / Transformers) for time-series forecasting?\"",
         "<b>How to Answer Confidently:</b><br/>"
         "\"We deliberately evaluated model complexity versus operational constraints:<br/>"
         "1. <b>Inference Latency & Portability:</b> Random Forest inference takes less than 15 milliseconds and runs smoothly on standard client CPUs without requiring GPU acceleration.<br/>"
         "2. <b>Data Efficiency:</b> Deep recurrent networks (LSTMs) require massive sequential datasets and are prone to overfitting on sparse or irregular consumer logging.<br/>"
         "3. <b>Explainability:</b> Tree ensembles provide clear feature importances, allowing us to explain to consumers exactly why a forecast rose (e.g., due to a 32°C heatwave).\""),

        ("Trap Q3: \"Can your system identify the exact appliance that wasted electricity without sub-metering?\"",
         "<b>How to Answer Confidently:</b><br/>"
         "\"As stated in Section 16 (Limitations) of our project documentation, without appliance-level smart plugs or high-frequency current sensors (NILM - Non-Intrusive Load Monitoring), the system analyzes whole-home aggregate consumption. However, our system accurately infers the appliance category using <b>temporal heuristics and power signatures</b>: for example, continuous 300W midnight baseload is attributed to standby electronics and refrigeration, while sharp 2.5 kW spikes during peak hours are matched with water heaters and HVAC systems.\""),

        ("Trap Q4: \"What is the significance of the 0.82 kg CO2e / kWh carbon factor?\"",
         "<b>How to Answer Confidently:</b><br/>"
         "\"0.82 kg CO2e per kWh is the standard national average grid emission factor established by the Central Electricity Authority (CEA). Because fossil fuels (coal and natural gas) comprise the baseline of electrical grid generation, every kilowatt-hour of electricity conserved directly prevents 0.82 kg of greenhouse gas emissions from entering the atmosphere.\"")
    ]

    for q, a in trap_qa:
        story.append(Paragraph(q, q_title_style))
        story.append(Paragraph(a, answer_style))
        story.append(Spacer(1, 3))

    # =========================================================================
    # SECTION 6: APPLIANCE SCHEDULING & LOAD SHIFTING
    # =========================================================================
    story.append(Spacer(1, 6))
    story.append(Paragraph("6. Optimal Energy-Saving Appliance Timetable (Module 7)", h1_style))
    
    sched_data = [
        [Paragraph("<b>Appliance</b>", table_header_style), Paragraph("<b>Optimal Window</b>", table_header_style),
         Paragraph("<b>Technical Justification</b>", table_header_style), Paragraph("<b>Expected Impact</b>", table_header_style)],
        [Paragraph("Washing Machine & Dryer", table_cell_style), Paragraph("10:00 AM – 02:00 PM", table_cell_style),
         Paragraph("Aligns with solar generation peak; avoids evening grid peak tariff.", table_cell_style), Paragraph("High (Saves 25% peak charge)", table_cell_style)],
        [Paragraph("Dishwasher", table_cell_style), Paragraph("01:00 PM – 04:00 PM", table_cell_style),
         Paragraph("Shifts thermal water heating away from 18:00–21:00 dinner grid surge.", table_cell_style), Paragraph("Medium", table_cell_style)],
        [Paragraph("Air Conditioning (AC)", table_cell_style), Paragraph("Pre-cool 03:00 PM; set 25°C", table_cell_style),
         Paragraph("Pre-cooling avoids compressor strain at heat peak. 1°C rise saves 6% power.", table_cell_style), Paragraph("Very High (15–20% bill cut)", table_cell_style)],
        [Paragraph("Water Heater (Geyser)", table_cell_style), Paragraph("06:00 AM – 08:00 AM (Timer)", table_cell_style),
         Paragraph("Eliminates 24/7 continuous standby reheating thermal losses.", table_cell_style), Paragraph("High (1.5–3 kWh/day saved)", table_cell_style)],
        [Paragraph("EV Charging", table_cell_style), Paragraph("11:00 PM – 05:00 AM", table_cell_style),
         Paragraph("Takes advantage of lowest off-peak night rate and flat grid demand.", table_cell_style), Paragraph("Very High", table_cell_style)]
    ]
    t_sched = Table(sched_data, colWidths=[110, 105, 185, 104])
    t_sched.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), secondary_color),
        ('BOX', (0,0), (-1,-1), 1, border_color),
        ('INNERGRID', (0,0), (-1,-1), 0.5, border_color),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_sched)

    story.append(PageBreak())

    # =========================================================================
    # SECTION 7: 25 RAPID-FIRE VIVA PRACTICE QUESTIONS
    # =========================================================================
    story.append(Paragraph("7. 25 Rapid-Fire Practice Questions (Quick Revision)", h1_style))
    story.append(Paragraph("Review these short definition questions right before entering the viva exam hall:", body_style))

    rapid_fire = [
        ("1. What is Vampire / Standby Power?", "Electricity consumed by electronics and appliances while turned off or in standby mode (typically 5–10% of residential power)."),
        ("2. What is Peak Shaving?", "The process of reducing electrical consumption during intervals of maximum network demand to lower peak utility tariffs."),
        ("3. What is Contamination in Isolation Forest?", "The expected proportion of outliers in the dataset (configured to 0.02 or 2.0% in our household model)."),
        ("4. What does R² (Coefficient of Determination) measure?", "The proportion of variance in the dependent variable (kWh) predictable from the independent features (0 to 1)."),
        ("5. What is MAE?", "Mean Absolute Error: the average magnitude of absolute errors between predicted and actual consumption."),
        ("6. What is the difference between supervised and unsupervised learning in this project?", "Supervised regression learns from historical labeled targets (kWh), while unsupervised Isolation Forest detects anomalies without ground-truth anomaly tags."),
        ("7. What is Non-Intrusive Load Monitoring (NILM)?", "A technique for disaggregating total household electrical load into individual appliance signatures using signal analysis."),
        ("8. How is the Carbon Emission factor defined?", "The quantity of greenhouse gases emitted per unit of electricity generated (0.82 kg CO2e per kWh from the grid)."),
        ("9. What does the Coefficient of Variation (CoV) represent?", "Standard deviation divided by the mean (&sigma;/&mu;); used as a measure of consumption volatility in the efficiency score."),
        ("10. What is an ensemble model?", "A machine learning technique that combines predictions from multiple base models (e.g., 200 decision trees) to improve generalization."),
        ("11. Why is SQLite used for this deployment?", "Zero-configuration, serverless, self-contained, and perfectly portable for standalone academic evaluation."),
        ("12. What does Django ORM provide?", "Abstraction to query and manipulate database records using Python classes instead of writing raw SQL queries."),
        ("13. What is the role of the Decision Function in Isolation Forest?", "Outputs the anomaly score; negative values indicate anomalies that required fewer tree splits to isolate."),
        ("14. What are Diurnal Patterns?", "Daily cyclical behavioral patterns that repeat every 24 hours (morning waking surges and evening dinner peaks)."),
        ("15. What features define our UsagePeriod?", "Night (00–06), Morning (06–12), Afternoon (12–17), and Evening (17–24)."),
        ("16. Why is temperature imputed with median rather than mean?", "Median is robust against extreme weather outliers and sensor anomalies."),
        ("17. What is the default tariff rate configured in the project?", "₹8.00 per kilowatt-hour (standard domestic tiered billing midpoint)."),
        ("18. What does Bagging mean in Random Forest?", "Bootstrap Aggregating: training trees on random subsets of data with replacement and averaging predictions."),
        ("19. How does the application handle duplicate uploads?", "The preprocessing pipeline checks existing timestamps for the user and drops duplicates before saving."),
        ("20. What is the purpose of the Scenario Simulator?", "Allows users to test hypothetical weather conditions and hours to simulate predicted kWh and compare RF vs Linear Regression."),
        ("21. What happens if a user inputs a negative kWh value?", "The form validator and preprocessing pipeline reject negative numbers as physically impossible."),
        ("22. What is Baseload?", "The permanent minimum electrical power draw required by continuous loads like refrigerators, alarms, and routers."),
        ("23. How are recommendations made actionable?", "Each tip specifies exact potential kWh savings and provides a 'Mark Done' toggle to track completed savings."),
        ("24. What is the difference between kWh and kW?", "kW (Kilowatt) is the rate of power demand; kWh (Kilowatt-hour) is the total energy consumed over time."),
        ("25. Why is this considered an end-to-end project?", "It spans the complete lifecycle: raw dataset ingestion, automated preprocessing, machine learning inference, financial/environmental impact calculation, and a full-stack interactive web interface.")
    ]

    for q_text, ans_text in rapid_fire:
        story.append(Paragraph(f"<b>{q_text}</b> — {ans_text}", bullet_style))

    story.append(Spacer(1, 15))
    story.append(HRFlowable(width="100%", thickness=1, color=secondary_color, spaceAfter=10))
    story.append(Paragraph("<b>End of Final Year Project Viva & Defense Guide</b> | Generated for EnergySync Project", subtitle_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    return output_filename

if __name__ == "__main__":
    out_path = r"c:\Users\HP\Downloads\project\AI_Energy_Waste_Predictor_Final_Year_Project_Viva_Guide.pdf"
    res = create_project_viva_pdf(out_path)
    print("PDF Generated successfully at:", res)

