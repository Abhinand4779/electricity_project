# EnergySync — AI-Powered Personal Energy Waste Predictor
**Final-Year BCA / B.Sc / B.Tech Capstone Project**  
*An Intelligent Energy Analytics, Digital Twin Simulation, Anomaly Detection & Explainable AI (XAI) Platform*

---

## 📌 Project Overview
**EnergySync** is an end-to-end intelligent IoT/Smart Meter Energy Analytics Platform designed to monitor residential electricity consumption, forecast demand using Machine Learning, detect abnormal spikes, quantify energy wastage (standby vampire draw and peak surges), and provide actionable, self-learning conservation strategies.

In addition to fulfilling the **8 core academic requirements**, the platform incorporates **7 next-generation AI innovations** (Digital Twin, Waste Detective, What-If Simulator, Self-Learning Engine, Personal Energy Fingerprint, Future Lifestyle Impact Predictor, and Explainable AI).

---

## 🚀 Key Features & Modules

### A. The 8 Core Academic Modules
1. **User Authentication & Profile Isolation (Module 1):** Secure session-based authentication, user registration, and per-user data segregation.
2. **Electricity Data Collection Interface (Module 2):** Interval logging with manual kWh inputs, ambient temperature tracking, and date-time validation.
3. **Automated Data Preprocessing Pipeline (Module 3):** Missing-value median imputation, deduplication, sanity filtering, and a **1-click UCI Smart Meter Dataset importer** (loads 168+ real hourly records).
4. **Machine Learning Consumption Prediction (Module 4):**
   - **Random Forest Regressor** & **Linear Regression** benchmarking ($R^2$, RMSE, MAE).
   - **Time-Series Forecasting:** Next-24-hour granular curve and 7-day multi-step daily forecast.
   - **Interactive Scenario Simulator:** Live what-if predictions for custom temperature, hour, and day.
5. **AI Anomaly Detection Engine (Module 5):** Unsupervised **Isolation Forest** combined with statistical $Z$-score thresholding.
6. **Energy Waste Analysis (Module 6):** Disaggregates midnight vampire baseload loss (00:00–06:00), peak grid surges (18:00–22:00), financial waste (₹8.00/kWh), and carbon footprint ($0.82\text{ kg CO}_2\text{e/kWh}$).
7. **Personalized Recommendations (Module 7):** Tailored energy-saving tips and an optimal Time-of-Day (ToD) appliance operating schedule.
8. **Interactive Dashboard & Efficiency Scoring (Module 8):** Dynamic **0–100 Energy Efficiency Score**, KPI cards, consumption trends, and dark/light mode toggle.

---

### B. The 7 Next-Gen Advanced AI Innovations
1. **🧬 01 AI Energy Digital Twin (`/digital-twin/`):** 24-hour virtual software replica of the household diurnal load curve.
2. **🕵️ 02 AI Energy Waste Detective (`/waste-detective/`):** Non-intrusive appliance signature disaggregation (AC compressor drift, water heater runaway, vampire standby cluster, concurrent peak overload).
3. **⚙️ 03 What-If Energy Simulator (`/digital-twin/`):** Interactive scenario playground comparing Rooftop Solar (1–5 kW), Inverter AC upgrades, thermostat setpoint shifts, and peak load shifting.
4. **🧠 04 Self-Learning Recommendation Engine (`/recommendations/`):** Reinforcement feedback loop (**👍 Helpful**, **🔄 Already Done**, **✕ Not Feasible**) with dynamic weight updates and an AI Adaptation Calibration Score (up to 98%).
5. **🪪 05 Personal Energy Fingerprint (`/energy-fingerprint/`):** 5-axis behavioral radar profile (Night Owl, Baseload, Weekend Surge, Peak Avoidance, Weather Elasticity) + Household Archetype classification badge.
6. **📈 06 Future Lifestyle Impact Predictor (`/digital-twin/`):** Quantifies electrical, financial (₹/mo), and carbon impact of lifestyle upgrades like Electric Vehicle (EV) daily charging with ROI / Payback estimates.
7. **🔬 07 Explainable AI (XAI) (`/waste-detective/`):** Decomposes "black box" ML anomaly detection into Shapley-style feature attribution percentages and plain-English diagnostic explanations.

---

## 🛠️ Technology Stack
- **Backend:** Python 3.12, Django 4.2 LTS
- **Data Science & ML:** `scikit-learn`, `pandas`, `numpy`, `joblib`
- **Database:** SQLite (default) / PostgreSQL compatible
- **Frontend & UI:** Semantic HTML5, CSS3 Custom Properties (Design System with Dark/Light mode), Vanilla JavaScript, Chart.js 4.x, Bootstrap Icons
- **Datasets:** UCI Individual Household Electric Power Consumption & Kaggle Smart Meter Data

---

## 💻 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Abhinand4779/electricity_project.git
cd electricity_project
```

### 2. Navigate to Django Project Folder & Install Dependencies
```bash
cd project/electricity
pip install -r requirements.txt
```

### 3. Run the Development Server
```bash
python manage.py runserver
```
*(If port 8000 is occupied, use `python manage.py runserver 127.0.0.1:8080`)*

### 4. Open in Web Browser
Navigate to **`http://127.0.0.1:8000/`** (or `http://127.0.0.1:8080/`).

---

## 🔑 Two-Tier Authentication & Pre-Configured Credentials

EnergySync implements an enterprise-grade **Two-Tier Multi-Tenant Architecture** with dedicated authentication portals and a 1-click viva switcher in the top navigation bar:

| Portal Role | Dedicated Login URL | Username | Password | Operational Scope |
| :--- | :--- | :--- | :--- | :--- |
| **🛡️ Grid Administrator** | `http://127.0.0.1:8080/admin-login/` | `hp` | `admin123` | Macro-level grid demand, ML model health monitor, multi-household audit table & Django admin |
| **⚡ Domestic Consumer** | `http://127.0.0.1:8080/login/` | `demo_user` | `demo1234` | Single-home smart meter telemetry (171 records), KSEB bill calculation, and all 7 AI innovation tools |

---

## 📚 Academic & Viva Voce Documentation
The repository includes complete final-year examination and seminar defense guides:
- `AI_Energy_Project_Master_Viva_Handbook.pdf`: **Master 6-Page Technical Handbook & Top 25 Viva Q&A Guide**
- `COMPLETE_PROJECT_REPORT_CALICUT_UNIVERSITY.md`: University of Calicut Standard Comprehensive Project Report
- `AI_Energy_Waste_Predictor_Final_Year_Project_Viva_Guide.pdf`: 9-Page Comprehensive Defense Guide
- `Beginner_Friendly_AI_Energy_Project_Viva_Guide.pdf`: 5-Page Fundamental ML Q&A Guide
- `ADVANCED_AI_FEATURES_VIVA_GUIDE.md`: Technical defense guide for the 7 new AI innovations
- `BCA_Project_Presentation_Model.pptx`: Final-year university slide deck model
- `Project_Documentation_Academic_PDF.pdf`: Original Software Requirements Specification (SRS)
- `HOW_TO_RUN_FOR_STUDENTS.txt`: Handover and setup instructions for students

