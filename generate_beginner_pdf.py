import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
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
            self.drawString(54, 755, "Beginner-Friendly Project Viva Guide | AI-Powered Energy Waste Predictor")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(54, 747, 558, 747)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 45, 558, 45)
        
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 32, page_str)
        self.drawString(54, 32, "EnergySync - Basic Questions & Simple Answers for Students")
        self.restoreState()

def create_beginner_viva_pdf(output_filename):
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        leftMargin=50,
        rightMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()
    
    # Palette
    primary_color = colors.HexColor("#0f3d2e")     # Deep Forest Green
    secondary_color = colors.HexColor("#1b7a4b")   # Bright Green
    accent_blue = colors.HexColor("#1d4ed8")       # Classic Blue
    dark_text = colors.HexColor("#1e293b")         # Slate Dark
    light_box = colors.HexColor("#f8fafc")
    border_color = colors.HexColor("#e2e8f0")

    # Typography
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=primary_color,
        alignment=1,
        spaceAfter=8
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#475569"),
        alignment=1,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=primary_color,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    q_title_style = ParagraphStyle(
        'QTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#0f172a"),
        spaceBefore=7,
        spaceAfter=2,
        keepWithNext=True
    )

    ans_style = ParagraphStyle(
        'Answer',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=12,
        textColor=colors.HexColor("#334155"),
        spaceAfter=5
    )

    analogy_style = ParagraphStyle(
        'Analogy',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#15803d"),
        leftIndent=12,
        spaceAfter=5
    )

    one_liner_style = ParagraphStyle(
        'OneLiner',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=12,
        textColor=colors.HexColor("#1e40af"),
        leftIndent=12,
        spaceAfter=5
    )

    story = []

    # Title Banner
    story.append(Paragraph("AI & MACHINE LEARNING FOR BEGINNERS", title_style))
    story.append(Paragraph("<b>Zero-To-Hero Viva Voce Practice Guide & Basic Concepts Handbook</b><br/>Project: AI-Powered Personal Energy Waste Predictor (EnergySync)", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=secondary_color, spaceAfter=12))

    # Intro note box
    intro_table = Table([[
        Paragraph("<b>💡 Student Advice for Viva:</b> External examiners often start by checking your <i>basic concepts</i>. If you can clearly explain what Machine Learning is, what a Random Forest is, and why data needs cleaning with simple real-life analogies, you will gain immediate confidence and secure top marks! Use the 1-line memorization tips below.", ans_style)
    ]], colWidths=[512])
    intro_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f0fdf4")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(intro_table)
    story.append(Spacer(1, 10))

    # =========================================================================
    # SECTION 1: WHAT IS AI & ML?
    # =========================================================================
    story.append(Paragraph("1. Absolute Basics: What is AI and Machine Learning?", h1_style))

    q1 = [
        ("Q1: What is Artificial Intelligence (AI)?",
         "<b>Simple Definition:</b> AI is the science of making computers and software smart enough to perform tasks that normally require human intelligence (like recognizing objects, understanding speech, making decisions, and detecting patterns).",
         "🌱 <b>Analogy:</b> Think of AI as the broad umbrella. Just like 'Vehicles' includes cars, bicycles, and airplanes, 'AI' includes robotics, computer vision, and machine learning."),

        ("Q2: What is Machine Learning (ML)?",
         "<b>Simple Definition:</b> Machine Learning is a specific branch of AI where computers <b>learn from past data and experience</b> to make future predictions, instead of a human programmer writing down every single rule manually.",
         "🌱 <b>Analogy:</b> Teaching a child what a dog looks like. You don't write 1,000 mathematical rules describing ears, fur, and tails. Instead, you show the child 100 pictures of dogs. The child's brain automatically learns the pattern. That is exactly how ML works!"),

        ("Q3: How is Machine Learning different from Traditional Programming?",
         "<b>Traditional Programming:</b> Human writes <code>Rules (Code) + Data &rarr; Computer gives Output</code>.<br/>"
         "<b>Machine Learning:</b> Human feeds <code>Data + Answers (Past Output) &rarr; Computer discovers the Rules (Model)</code>.",
         "🌱 <b>In our project:</b> In traditional programming, you would have to write rules like 'IF hour is 3 AM AND usage > 5 THEN alert'. In ML, the algorithm looks at 34,000 hours of real usage and figures out by itself what is normal and what is weird!"),

        ("Q4: What is Supervised Learning vs Unsupervised Learning?",
         "<b>Supervised Learning:</b> The computer learns with a teacher (labeled answers). You feed data and tell it: 'Here are temperature and hour, and the correct consumption was 2.5 kWh.'<br/>"
         "<b>Unsupervised Learning:</b> The computer learns on its own without any teacher or labels. It looks at raw numbers and groups similar things together or spots weird oddballs.",
         "🌱 <b>In our project:</b> Our <b>Random Forest Regressor</b> is Supervised (it learns from past known kWh). Our <b>Isolation Forest</b> is Unsupervised (it finds strange spikes without needing any human to label them first)."),

        ("Q5: What is the difference between Regression and Classification?",
         "<b>Regression:</b> Predicts a continuous number (e.g. predicting electricity usage: 1.45 kWh, house price: ₹50 Lakhs, temperature: 29.5°C).<br/>"
         "<b>Classification:</b> Predicts a category or label (e.g. Normal vs Abnormal, Pass vs Fail, Spam vs Not Spam).",
         "🌱 <b>In our project:</b> Predicting tomorrow's energy consumption (kWh) is <b>Regression</b>. Flagging usage as 'Normal' or 'Abnormal' is <b>Classification</b>.")
    ]

    for q, ans, analogy in q1:
        story.append(Paragraph(q, q_title_style))
        story.append(Paragraph(ans, ans_style))
        story.append(Paragraph(analogy, analogy_style))
        story.append(Spacer(1, 2))

    story.append(PageBreak())

    # =========================================================================
    # SECTION 2: MACHINE LEARNING ALGORITHMS EXPLAINED SIMPLY
    # =========================================================================
    story.append(Paragraph("2. Machine Learning Algorithms Explained Simply", h1_style))

    q2 = [
        ("Q6: What is a Decision Tree?",
         "<b>Simple Definition:</b> A Decision Tree is a flowchart of yes/no questions that leads to a prediction. For example: Is it night? (Yes) &rarr; Is temperature high? (No) &rarr; Predicted consumption = 0.4 kWh.",
         "🌱 <b>Analogy:</b> Playing the game '20 Questions' where you narrow down the answer by asking simple yes/no questions."),

        ("Q7: What is a Random Forest? Why is it called a 'Forest'?",
         "<b>Simple Definition:</b> A Random Forest is an ensemble (collection) of many Decision Trees (in our project, <b>200 trees</b>) working together as a team. Each tree makes a prediction, and the forest takes the average of all predictions.",
         "🌱 <b>Analogy:</b> If you want to buy a new phone, you don't ask just one friend (one tree) because they might be biased. You ask 20 friends (a forest) and take the majority opinion. A crowd of trees is much smarter and makes far fewer mistakes than a single tree!"),

        ("Q8: What is Linear Regression?",
         "<b>Simple Definition:</b> Linear Regression is the simplest prediction method. It tries to draw a single straight line through data points to predict the future (Equation: <i>y = mx + c</i>).",
         "🌱 <b>Why it fails for electricity:</b> Electricity usage doesn't follow a straight line! At 20°C you use no AC, but at 35°C usage explodes exponentially. A straight line cannot curve to match real life, which is why Random Forest beats Linear Regression."),

        ("Q9: What is an Anomaly (or Outlier)?",
         "<b>Simple Definition:</b> An anomaly is a data point that is completely different, unexpected, or abnormal compared to the rest of the data.",
         "🌱 <b>Real-Life Example:</b> If all students in a class are between 18 and 22 years old, and suddenly a 75-year-old student joins, that person is an anomaly. In our project: if a home usually consumes 0.3 kWh at 3:00 AM while everyone is asleep, but today consumes 7.0 kWh, that is an energy anomaly!"),

        ("Q10: What is an Isolation Forest? How does it find strange spikes?",
         "<b>Simple Definition:</b> Isolation Forest is a clever algorithm designed specifically to catch anomalies. Instead of modeling what is normal, it focuses on <b>how easy it is to isolate (separate) a point</b>.",
         "🌱 <b>The Sheep Analogy:</b> Imagine 100 white sheep clustered together in the center of a field, and 1 black sheep standing far away near the fence. If you draw random lines across the field, you can isolate the lonely black sheep with just 1 or 2 cuts! But to isolate one specific white sheep in the middle of the crowd, you need 20 cuts. <b>Anomalies isolate quickly in few cuts!</b>"),

        ("Q11: What is Time-Series Data?",
         "<b>Simple Definition:</b> Time-series data is simply a sequence of numbers recorded at regular intervals of time (e.g. every hour, every day, every month).",
         "🌱 <b>In our project:</b> Hourly electricity consumption is time-series data because the value at 2:00 PM is related to what happened at 1:00 PM and what happens every day at 2:00 PM.")
    ]

    for q, ans, analogy in q2:
        story.append(Paragraph(q, q_title_style))
        story.append(Paragraph(ans, ans_style))
        story.append(Paragraph(analogy, analogy_style))
        story.append(Spacer(1, 2))

    story.append(PageBreak())

    # =========================================================================
    # SECTION 3: METRICS, DATA CLEANING & DOMAIN CONCEPTS
    # =========================================================================
    story.append(Paragraph("3. Model Performance Metrics in Plain English", h1_style))

    q3 = [
        ("Q12: What is R² (R-squared) Score?",
         "<b>Simple Definition:</b> R² score tells you how well your model explains the reality of the data. It ranges from 0 to 1 (or 0% to 100%).<br/>"
         "• R² = 1.0 means 100% perfect predictions.<br/>"
         "• In our project: <b>Random Forest achieved R² = 0.842 (84.2%)</b>, which means our AI model accurately captures 84.2% of the variations in electricity consumption!"),

        ("Q13: What is MAE (Mean Absolute Error)?",
         "<b>Simple Definition:</b> MAE is the average mistake (in actual units) the model makes.<br/>"
         "• In our project: Random Forest MAE is <b>0.071 kWh</b>. This means when the AI predicts electricity usage, its guess is off by only 0.071 units on average! That is extremely accurate."),

        ("Q14: What is Overfitting and Underfitting?",
         "<b>Overfitting:</b> The model memorizes the training data like a student who memorizes exam answers word-for-word without understanding. It scores 100% on practice questions, but fails the real exam on new questions.<br/>"
         "<b>Underfitting:</b> The model is too simple and didn't learn enough. (Like drawing a straight line when data curves).<br/>"
         "• <b>How we solved it:</b> We split data 80% for training and 20% for testing to verify the model works on unseen data.")
    ]

    for q, ans in q3:
        story.append(Paragraph(q, q_title_style))
        story.append(Paragraph(ans, ans_style))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 4))
    story.append(Paragraph("4. Data Preprocessing & Cleaning (Why Clean Data?)", h1_style))

    q4 = [
        ("Q15: What is Data Preprocessing? Why is it necessary?",
         "<b>Simple Definition:</b> Data preprocessing means cleaning raw data before feeding it to machine learning models. Real data collected from sensors or files has errors, missing blanks, and duplicates.<br/>"
         "🌱 <b>Golden Rule of AI:</b> <i>'Garbage In, Garbage Out'</i>. If you train an AI model on dirty, corrupted data, its predictions will be useless."),

        ("Q16: What 4 things does our Preprocessing Pipeline do?",
         "Inside <code>preprocessing.py</code>, our code automatically executes 4 steps:<br/>"
         "<b>1. Deduplication:</b> Removes repeated timestamps so the same hour isn't counted twice.<br/>"
         "<b>2. Missing Value Imputation:</b> Fills empty temperature values with the median of past days.<br/>"
         "<b>3. Sanity Filtering:</b> Deletes impossible numbers (like negative electricity usage or corrupted text).<br/>"
         "<b>4. Feature Extraction:</b> Automatically extracts the hour of day, day of week, and usage period (Night, Morning, Afternoon, Evening).")
    ]

    for q, ans in q4:
        story.append(Paragraph(q, q_title_style))
        story.append(Paragraph(ans, ans_style))
        story.append(Spacer(1, 2))

    story.append(PageBreak())

    # =========================================================================
    # SECTION 5: ELECTRICAL & ENERGY DOMAIN BASICS
    # =========================================================================
    story.append(Paragraph("5. Electrical & Energy Terms (Every Student Must Know)", h1_style))

    q5 = [
        ("Q17: What is the difference between kW (Kilowatt) and kWh (Kilowatt-hour)?",
         "• <b>kW (Power):</b> The <i>speed</i> or rate at which an appliance draws electricity right now. (Like speed of a car: 60 km/h).<br/>"
         "• <b>kWh (Energy):</b> The <i>total amount</i> of electricity consumed over time. (Like total distance traveled: 60 km).<br/>"
         "🌱 <b>Example:</b> A 1,000 Watt (1 kW) air conditioner running for 3 hours consumes: <code>1 kW * 3 hours = 3 kWh</code>. Your electricity bill charges you per kWh!"),

        ("Q18: What is Vampire Power / Standby Power?",
         "<b>Simple Definition:</b> Vampire power (also called phantom load) is the electricity wasted by electronics while they are plugged in and turned 'off' or in standby mode (TVs, microwave clocks, chargers, gaming consoles, set-top boxes).<br/>"
         "• In an average home, vampire power wastes <b>5% to 10%</b> of the entire electricity bill! Our project detects this between 12:00 AM and 6:00 AM."),

        ("Q19: What is Baseload?",
         "<b>Simple Definition:</b> Baseload is the minimum continuous amount of electricity a house always uses 24/7, even when everyone is sleeping and lights are off (e.g. refrigerator compressor, Wi-Fi router, security cameras)."),

        ("Q20: What are Peak Hours and Off-Peak Hours?",
         "• <b>Peak Hours (6 PM to 10 PM):</b> The time of day when everyone comes home, turns on lights, ACs, and cooking appliances. Grid electricity demand is highest, and utility companies charge higher rates.<br/>"
         "• <b>Off-Peak Hours (11 AM to 4 PM & Night):</b> Demand is low or solar energy is abundant. Electricity is cheaper and greener."),

        ("Q21: What is Carbon Footprint & why 0.82 kg CO2e / kWh?",
         "<b>Simple Definition:</b> Carbon footprint measures the pollution (greenhouse gases) caused by our electricity consumption. In India, most grid electricity comes from coal power plants. Generating 1 kWh of electricity releases approximately <b>0.82 kg of CO2</b> into the atmosphere. Every unit of electricity saved directly stops pollution!")
    ]

    for q, ans in q5:
        story.append(Paragraph(q, q_title_style))
        story.append(Paragraph(ans, ans_style))
        story.append(Spacer(1, 2))

    story.append(PageBreak())

    # =========================================================================
    # SECTION 6: THE 1-LINE MEMORIZATION CHEAT SHEET (VIVA SAVER)
    # =========================================================================
    story.append(Paragraph("6. Student 1-Line Memorization Cheat Sheet", h1_style))
    story.append(Paragraph("If the examiner asks a quick question, speak these exact 1-line answers confidently:", ans_style))

    cheat_sheet = [
        ("Examiner: 'What is your project about?'",
         "\"Our project is an AI system that monitors electricity consumption, predicts future usage using Random Forest, and detects hidden energy waste using Isolation Forest.\""),

        ("Examiner: 'What is Machine Learning?'",
         "\"Machine Learning is a subset of AI where computers learn patterns from past data to make predictions without being explicitly programmed with manual rules.\""),

        ("Examiner: 'Why did you use Random Forest?'",
         "\"Because Random Forest uses an ensemble of 200 decision trees to capture non-linear electricity consumption patterns, achieving an R² of 0.84 compared to 0.08 for Linear Regression.\""),

        ("Examiner: 'Why did you use Isolation Forest?'",
         "\"Because Isolation Forest is an unsupervised algorithm that isolates rare spikes and abnormal midnight usage in very few splits, without needing manual anomaly labels.\""),

        ("Examiner: 'What is your dataset?'",
         "\"We used the UCI Household Electric Power Consumption dataset of 34,085 real records and Kaggle smart meter datasets.\""),

        ("Examiner: 'What is the Energy Efficiency Score?'",
         "\"It is a personalized 0-to-100 score calculated by our algorithm based on anomaly frequency, midnight vampire load ratio, peak usage spikes, and consistency.\""),

        ("Examiner: 'What is the main benefit to the consumer?'",
         "\"It reduces unnecessary electricity waste, cuts monthly electricity bills by up to 20%, and lowers household carbon emissions.\"")
    ]

    for q, ans in cheat_sheet:
        story.append(Paragraph(f"<b>{q}</b>", q_title_style))
        story.append(Paragraph(ans, one_liner_style))
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 15))
    story.append(HRFlowable(width="100%", thickness=1, color=secondary_color, spaceAfter=8))
    story.append(Paragraph("<b>End of Beginner-Friendly Practice Guide</b> | Prepared for Final Year Students", subtitle_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    return output_filename

if __name__ == "__main__":
    out_path = r"c:\Users\HP\Downloads\project\Beginner_Friendly_AI_Energy_Project_Viva_Guide.pdf"
    res = create_beginner_viva_pdf(out_path)
    print("Beginner PDF generated successfully at:", res)
