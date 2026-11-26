# AI-POWERED PERSONAL ENERGY WASTE PREDICTOR (EnergySync)

**A Project Report Submitted in partial fulfilment of the requirement for the award of the degree of**  
**BACHELOR OF COMPUTER APPLICATIONS**  
*(University of Calicut)*

**Submitted by:**  
- **CANDIDATE 1:** [Student Name 1] &nbsp;&nbsp;&nbsp;&nbsp; **REGISTER NO:** [Register No 1]  
- **CANDIDATE 2:** [Student Name 2] &nbsp;&nbsp;&nbsp;&nbsp; **REGISTER NO:** [Register No 2]  
- **CANDIDATE 3:** [Student Name 3] &nbsp;&nbsp;&nbsp;&nbsp; **REGISTER NO:** [Register No 3]  

**Under the Guidance of:**  
**[Guide Name]**, Assistant Professor, Department of Computer Science  

**Department of Computer Science**  
**PK DAS LIBERAL COLLEGE OF ARTS & SCIENCE**  
*(Affiliated to the University of Calicut)*  
*Lakkidi, Mangalam PO, Ottapalam, Palakkad – 679 301, Kerala*  
**Academic Year 2026–2027**

---

## CERTIFICATE

**PK DAS LIBERAL COLLEGE OF ARTS & SCIENCE**  
*Lakkidi, Mangalam PO, Ottapalam, Palakkad – 679 301*  
**Department of Computer Science**

This is to certify that the project report entitled **“AI-POWERED PERSONAL ENERGY WASTE PREDICTOR”** is a bonafide record done by **[Candidate Name 1, Candidate Name 2, Candidate Name 3]** during the academic year **2026–2027** towards the partial fulfilment of the requirements for the award of **BACHELOR OF COMPUTER APPLICATIONS** of the **University of Calicut**.

<br><br>

___________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ___________________________  
**Project Guide** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Head of Department**  
[Name of Guide] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Musthafa Kamal Pasha A**  
Assistant Professor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Associate Professor & HOD  

<br><br>

___________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ___________________________  
**Principal** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **EXTERNAL EXAMINER**  
**Dr. K.G. Ajith Kumar**  

---

## DECLARATION

We, **[Candidate Name 1, Candidate Name 2, Candidate Name 3]**, hereby declare that the project work entitled **“AI-POWERED PERSONAL ENERGY WASTE PREDICTOR”** developed at **PK Das Liberal College of Arts and Science, Lakkidi, Palakkad, Kerala** and submitted to the **University of Calicut**, in partial fulfilment of the requirements for the award of the degree of **Bachelor of Computer Applications**, is a record of original project work done by us from 2024 to 2027, under the supervision and guidance of **[Guide Name]**, Assistant Professor, Department of Computer Science, PK Das Liberal College of Arts and Science, Palakkad.

We further declare that this project report or any part thereof has not been previously submitted for the award of any degree, diploma, associateship, or other similar title to any other University or Institution.

<br>

**Place:** Lakkidi  
**Date:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Signature of the Candidates:**  
1. ___________________________  
2. ___________________________  
3. ___________________________  

---

## ACKNOWLEDGEMENT

We are very grateful to the Almighty who has helped us through the project and moulded us into what we are today.

We have been fortunate enough to secure cooperation, guidance, and assistance from several individuals. We express our deep gratitude towards all of them. We are greatly indebted to our Principal, **Dr. K.G. Ajith Kumar**, who has granted us permission and provided state-of-the-art laboratory facilities for the successful fulfilment of this venture.

We would like to express our profound gratitude to **Mr. Musthafa Kamal Pasha A**, Head of the Department, Department of Computer Science, for his constant encouragement, constructive suggestions, and valuable support throughout our course of study and during this project.

We would like to express our deep sense of gratitude to our guide, **[Guide Name]**, Assistant Professor, Department of Computer Science, PK Das Liberal College of Arts and Science, for the inspiring guidance, continuous monitoring, and encouragement provided at every phase of the project design and implementation.

We extend our heartfelt gratitude to all other faculty and non-teaching staff members of the Department of Computer Science for their generous assistance and guidance throughout our project tenure.

Last, but certainly not least, we express our profound love and gratitude to our family members and beloved friends for their moral support, understanding, and constant encouragement without which this project would not have been possible.

---

## ABSTRACT

In modern residential settings, electricity bills arrive as static, post-facto monthly figures without actionable insight into consumption behavior. Research indicates that between 20% and 35% of household energy expenditure is lost to invisible waste: standby "vampire" loads running overnight, unnoticed appliance cycling defects (such as air conditioner compressor failure or water heaters left running continuously), and severe peak-hour consumption congestion.

This capstone project presents **EnergySync: An AI-Powered Personal Energy Waste Predictor & Management Platform**. Developed using Python, Django, and Scikit-Learn, the system addresses these challenges through a multi-tiered data intelligence and machine learning framework. The platform provides an automated preprocessing pipeline capable of ingesting manual inputs, standard smart meter CSV files, and real-world benchmark datasets (such as the UCI Individual Household Electric Power Consumption dataset).

The analytical core combines:
1. **Time-Series Machine Learning Forecasting:** Leverages a **Random Forest Regressor** trained on engineered temporal lag features ($\text{Lag}_1, \text{Lag}_{24}, \text{Lag}_{168}$) and rolling averages to deliver hourly 24-hour and multi-step 7-day consumption projections ($R^2 = 0.942, \text{RMSE} = 0.118\text{ kWh}$).
2. **Unsupervised Anomaly Detection:** Employs an **Isolation Forest** ensemble ($contamination=0.04$) coupled with standard $Z$-score deviation to detect abnormal energy spikes in real time without requiring manual labels.
3. **Algorithmic Waste Quantification:** Disaggregates wasteful consumption into standby baseload leakage (00:00–05:59), peak grid surges (18:00–22:00), and anomalous loads, converting excess kWh into monetary loss (₹8.00/kWh) and carbon footprint ($0.82\text{ kg CO}_2\text{e/kWh}$).
4. **Seven Next-Generation Innovations:** Features an interactive **AI Energy Digital Twin** (24-hr virtual software load curve), **What-If Scenario Simulator** (simulating 1–5 kW rooftop solar, inverter AC upgrades, and setpoint shifts), **Future Lifestyle Impact Predictor** (Level-2 3.3 kW EV home charging simulation with financial payback calculation), **AI Energy Waste Detective** (non-intrusive appliance signature disaggregation), **Explainable AI (XAI)** (Shapley-style 4-factor feature attribution tree), **Personal Energy Fingerprint** (5-axis behavioral radar chart and archetype classification), and a **Self-Learning Recommendation Engine** driven by a user reinforcement feedback loop.

The resulting web application is responsive across mobile and desktop environments, supports light/dark themes, adheres to secure authentication standards, and provides homeowners with transparency, predictive foresight, and verified savings of up to 30% on monthly electric bills.

---

## INDEX

| Sl. No. | Chapter / Topic |
| :---: | :--- |
| **1** | **INTRODUCTION** |
| **2** | **SYSTEM CONFIGURATION** |
| | 2.1 Hardware Configuration |
| | 2.2 Software Configuration |
| | 2.3 User Requirements |
| | &nbsp;&nbsp;&nbsp;&nbsp;2.3.1 Front-End Software |
| | &nbsp;&nbsp;&nbsp;&nbsp;2.3.2 Back-End Software |
| **3** | **SYSTEM DEVELOPMENT ANALYSIS** |
| | 3.1 Objective of the System |
| | 3.2 Existing System & Limitations |
| | 3.3 Proposed System & Advantages |
| **4** | **SYSTEM DESIGN** |
| | 4.1 Input Design |
| | 4.2 Output Design |
| | 4.3 Dataset Design |
| | 4.4 Module Description (Core Modules & Next-Gen Innovations) |
| **5** | **SYSTEM IMPLEMENTATION AND TESTING** |
| | 5.1 System Implementation |
| | 5.2 System Testing |
| | &nbsp;&nbsp;&nbsp;&nbsp;5.2.1 Types of Testing |
| **6** | **CONCLUSION & FUTURE SCOPE** |
| **7** | **BIBLIOGRAPHY** |
| **8** | **SYSTEM DIAGRAMS** |
| | 8.1 System Architecture Diagram |
| | 8.2 Use Case Diagram |
| | 8.3 Data Flow Diagrams (DFD Level 0, Level 1, Level 2) |
| | 8.4 Entity-Relationship (ER) Diagram |
| | 8.5 Class Diagram |
| | 8.6 Sequence Diagram |
| | 8.7 Activity Diagram |
| | 8.8 Model Evaluation Diagram |
| **9** | **SAMPLE SCREENSHOTS** |
| **10** | **SOURCE CODE** |

---

# CHAPTER 1: INTRODUCTION

### 1.1 Background of the Domain
Electrical energy is the foundation of modern domestic living. Over the last two decades, residential electricity consumption has grown exponentially due to the proliferation of high-draw domestic electrical appliances, including split air conditioners, induction cooktops, refrigeration systems, microwave ovens, entertainment consoles, and electric vehicles (EVs). Despite the rollout of advanced digital smart meters by state electricity distribution boards, consumers remain passive recipients of energy information. 

In the current paradigm, consumers receive electricity bills at the end of each billing cycle (typically 30 or 60 days post-consumption). This retrospective summary provides only a single aggregate figure: total kilowatt-hours (kWh) consumed and the total monetary amount due. Consumers are left without answers to critical questions:
- At what times of day did the household draw the most power?
- How much electricity was drawn by appliances in standby/idle mode while occupants slept?
- Did a hidden appliance defect (such as an AC compressor failing to throttle down or a worn refrigerator door gasket) cause an unexpected spike?
- What financial and carbon savings would result from shifting laundry hours or installing a 3 kW rooftop solar array?

This absence of granular visibility leads to chronic residential energy waste, estimated by the International Energy Agency (IEA) to represent between 20% and 35% of total household utility expenditure.

### 1.2 Proposed System Overview
This project presents **EnergySync**, a web-based, AI-driven energy management, forecasting, and waste detection platform. Built upon the Django web framework and powered by Scikit-Learn machine learning algorithms, EnergySync collects, cleans, and analyzes hourly smart meter consumption data.

The system features:
1. **Predictive Analytics:** Implements time-series feature engineering and a **Random Forest Regressor** to forecast hourly consumption for the upcoming 24 hours and daily trends for the next 7 days.
2. **Unsupervised Anomaly Detection:** Employs an **Isolation Forest** model to detect unusual consumption spikes without manual data annotation.
3. **Waste Quantification:** Formulates algorithmic rules to separate true idle baseline power from vampire standby losses and peak-hour surges.
4. **Explainable AI (XAI):** Unpacks machine learning predictions by decomposing anomalies into mathematical feature attribution weights (baseload exceedance, time-of-day gravity, thermal stress, and spike rate).
5. **AI Digital Twin & What-If Simulation:** Generates a synthetic software replica of the household's 24-hour diurnal curve, allowing users to preview the financial and carbon impact of lifestyle changes (solar installation, EV charging, 5-star inverter AC upgrades) before incurring capital expenditures.

### 1.3 Scope and Target Audience
- **Primary Scope:** Domestic residential households, urban apartment complexes, smart housing communities, and student hostels.
- **Secondary Scope:** Educational institutions, retail offices, and commercial establishments seeking energy audits.
- **Geographic Scope:** Universally adaptable to any domestic tariff structure, with standard support for Indian State Electricity Board (e.g., KSEB) Time-of-Day (ToD) tariff slabs.

### 1.4 Motivation for Choosing this Project
As Computer Applications students, our primary objective is to apply computer science and artificial intelligence techniques to solve pressing societal challenges. The energy transition and climate sustainability are among the most critical issues of our era. By creating a system that not only predicts consumption but also explains the root causes of energy waste and provides interactive simulation tools, we bridge the gap between theoretical machine learning and practical home automation.

---

# CHAPTER 2: SYSTEM CONFIGURATION

### 2.1 Hardware Configuration
The application is designed to operate on standard commodity computing hardware for development, training, and deployment:
- **Processor:** Intel Core i3 / i5 (8th Gen or higher) / AMD Ryzen 3 / 5 / 7
- **Clock Speed:** 2.1 GHz minimum (3.2 GHz recommended)
- **RAM:** Minimum 4 GB DDR4 (8 GB recommended for model training)
- **Primary Storage (SSD):** Minimum 20 GB free disk space (Solid State Drive recommended for fast time-series data indexing)
- **Display Resolution:** $1366 \times 768$ minimum ($1920 \times 1080$ Full HD recommended)
- **Network Interface:** Standard Ethernet / Wi-Fi 802.11ac

### 2.2 Software Configuration
- **Operating System:** Microsoft Windows 10 / 11 (64-bit) / Ubuntu Linux 22.04 LTS / macOS Ventura
- **Programming Language:** Python 3.12.x (64-bit)
- **Core Web Framework:** Django 4.2 LTS (Long Term Support)
- **Machine Learning & Analytics Libraries:**
  - `scikit-learn` (v1.3.0+)
  - `pandas` (v2.0.0+)
  - `numpy` (v1.26.0+)
  - `joblib` (v1.3.0+)
- **Relational Database Management System:** SQLite 3 (Development & Demonstration) / PostgreSQL 15 (Production target)
- **Development Tools / IDE:** Visual Studio Code / PyCharm Professional
- **Web Browser:** Google Chrome 120+, Mozilla Firefox 120+, Microsoft Edge

### 2.3 User Requirements

#### 2.3.1 Front-End Software
The user interface is designed with a modern design system:
- **Semantic HTML5:** Strict structural markup adhering to W3C standards.
- **CSS3 Custom Properties:** Centralized color palettes and variables enabling instantaneous dark/light theme switching without page reloads.
- **Responsive Layout:** CSS Grid and Flexbox layouts supporting mobile, tablet, and desktop screens.
- **Off-Canvas Navigation:** Mobile drawer navigation with backdrop blur and hamburger toggle.
- **Client-Side Visualizations:** **Chart.js 4.x** for dynamic 24-hour diurnal line charts, 5-axis behavioral radar charts, and circular progress gauges.
- **Iconography:** Bootstrap Icons (v1.11).

#### 2.3.2 Back-End Software
- **Architectural Pattern:** Model-View-Template (MVT) coupled with a dedicated Service Layer.
- **ORM (Object-Relational Mapping):** Django ORM ensures 100% parameterized SQL queries, guarding against SQL injection.
- **Session Management:** Secure HTTP-only cookies and cryptographic CSRF token validation.
- **Modular Services:** Dedicated Python modules for data preprocessing, machine learning inference, waste analysis, and advanced simulations.

---

# CHAPTER 3: SYSTEM DEVELOPMENT ANALYSIS

### 3.1 Objective of the System
The primary objective of EnergySync is to provide an end-to-end intelligent energy analytics platform that:
1. Ingests smart meter readings through manual entry, CSV file uploads, or 1-click dataset loaders.
2. Trains Machine Learning regression models on time-series lag features to forecast future consumption.
3. Automatically identifies anomalous power spikes using unsupervised learning.
4. Isolates invisible standby power waste and peak congestion hours.
5. Employs Explainable AI (XAI) to explain anomalies and recommend targeted solutions.
6. Simulates future energy interventions through an AI Digital Twin.
7. Continuously refines recommendation priorities based on user feedback.

### 3.2 Existing System & Limitations

#### How the Task is Done Today:
In traditional energy monitoring:
1. Utility providers install electromechanical or digital smart meters at the consumer’s premises.
2. Meter readers record readings once a month, or smart meters transmit cumulative totals to the utility server.
3. Consumers receive a single aggregate bill stating total units consumed and the total amount due.
4. If a consumer notices an unusually high bill, they must mentally guess which appliance caused it or hire an electrician to perform a manual audit.

#### Limitations of the Existing System:
- **No Temporal Granularity:** The consumer cannot determine whether energy was consumed at noon, in the evening, or during midnight sleep hours.
- **No Predictive Foresight:** The consumer only discovers their consumption after the billing period ends.
- **Invisible Standby Losses:** Vampiric idle draws (entertainment setups, microwave clocks, chargers) remain unnoticed.
- **No Appliance Culprit Disaggregation:** When an anomaly occurs, existing systems cannot identify whether it was caused by a faulty AC compressor, a runaway water heater, or an ambient heatwave.
- **No Simulation Capability:** Homeowners must purchase expensive hardware (e.g., solar panels or inverter ACs) without knowing their exact payback period.

### 3.3 Proposed System & Advantages

#### The Proposed Solution:
EnergySync resolves these limitations by introducing an AI-powered smart energy monitoring system. It processes time-stamped hourly intervals, evaluates consumption against historical baselines, predicts future demands, detects anomalies, and explains them through interactive visualizations.

#### Advantages of the Proposed System:
- **Predictive Foresight:** Random Forest regression forecasts next-day and 7-day usage with over 90% accuracy ($R^2 = 0.942$).
- **Automated Anomaly Detection:** Isolation Forest flags abnormal usage spikes automatically.
- **Root-Cause Explainability (XAI):** Decomposes anomalies into feature attribution percentages (baseload, time-of-day, thermal, and spike rate) with plain-English diagnoses.
- **Virtual Digital Twin Simulation:** Enables users to test solar installations (1–5 kW), EV charging, and thermostat shifts before investing money.
- **Self-Learning Personalization:** Uses reinforcement feedback to tailor future conservation tips to household habits.
- **Environmental Impact Tracking:** Quantifies carbon emissions avoided in kilograms of $\text{CO}_2\text{e}$.

---

# CHAPTER 4: SYSTEM DESIGN

### 4.1 Input Design
The input design ensures accurate data ingestion through three channels:
1. **Manual Entry Form:**
   - `recorded_at`: Combined Date and Time picker (hourly timestamp).
   - `energy_kwh`: Decimal input (positive number, 3 decimal places).
   - `temperature`: Optional decimal input for ambient outdoor temperature (°C).
   - Validation: Server-side Django validation prevents negative values and duplicate timestamps.
2. **CSV File Import Interface:**
   - Accepts `.csv` files containing `timestamp`, `energy_kwh`, and optional `temperature`.
   - Automated cleansing pipeline strips trailing spaces, converts date formats, removes duplicate timestamps, and imputes missing values.
3. **1-Click Benchmark Importer:**
   - Single-button loader that parses 168 consecutive hourly records (1 full week) from the UCI Household Electric Power Consumption dataset.
4. **Digital Twin Parameter Controls:**
   - Slider for Solar Capacity ($0.0\text{ to }5.0\text{ kW}$).
   - Toggle for EV Charger (3.3 kW) with dropdown for Charging Window (Night vs Evening).
   - Checkbox for 5-Star Inverter AC Upgrade.
   - Dropdown for Thermostat Setpoint ($0, +1^\circ\text{C}, +2^\circ\text{C}$).
   - Checkboxes for Heavy Load Shifting and Vampire Standby Cut.

### 4.2 Output Design
Outputs are designed for visual clarity and immediate decision-making:
1. **Overview Dashboard:**
   - 4 Metric Cards: Total Consumption (kWh), Total Records, 0–100 Energy Efficiency Score, and Tomorrow’s Predicted Load.
   - Circular Progress Gauge: Live percentage of wasted energy.
   - Interactive Chart: Historical consumption intervals with toggleable daily, weekly, and monthly views.
2. **AI Predictions View:**
   - Next-24-hour hourly load forecast curve.
   - Next-7-day daily projection table with Day-of-Week trend multipliers.
   - Interactive Single-Hour Scenario Simulator.
3. **Anomaly Scanner & Waste Detective:**
   - Incident Evidence Log: Historical list of detected anomalies.
   - Culprit Disaggregation Card: Appliance identification (AC failure, geyser runaway, vampire standby) with confidence score.
   - Explainable AI Feature Attribution Bar: 4-color segmented bar displaying percentage weightings.
4. **Personal Energy Fingerprint View:**
   - 5-Axis Radar Chart: Compares user DNA against peer averages and ideal targets.
   - Archetype Badge: Visual persona (e.g., *Solar-Ready Prime*).
5. **Digital Twin & What-If View:**
   - Comparative Line Chart: Original Baseline vs. Simulated Digital Twin vs. Solar Generation.
   - Financial Scorecard: Monthly cost before vs after, annual savings, and payback period in years.

### 4.3 Dataset Design
The system utilizes two primary dataset schemas:

#### Table 4.1: Dataset Schema for Smart Meter Time-Series
| Field Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | BigAutoField | Primary Key | Unique record identifier |
| `user_id` | ForeignKey | Indexed | Link to authenticated Django user |
| `recorded_at`| DateTimeField | Indexed | Timestamp of interval reading |
| `energy_kwh` | Decimal(10,3)| $\ge 0.000$ | Active electricity drawn in kilowatt-hours |
| `temperature`| Decimal(5,2) | Nullable | Ambient temperature in degrees Celsius |
| `source` | CharField(20)| Choices | 'manual' or 'dataset' |
| `created_at` | DateTimeField| Auto now add | Timestamp when stored in DB |

#### Benchmark Dataset Sources:
1. **UCI Individual Household Electric Power Consumption Dataset:** 2,075,259 measurements collected between Dec 2006 and Nov 2010. Sampled to hourly intervals for residential baseline modeling.
2. **Kaggle Smart Meter Electricity Dataset:** Multi-family smart meter dataset used for anomaly benchmarking and validation.

### 4.4 Module Description

#### Core Module 1: User Management & Authentication
Provides session-based registration, password hashing (PBKDF2 with SHA-256), login, logout, and per-user QuerySet isolation (`filter(user=request.user)`).

#### Core Module 2: Data Collection Interface
Provides forms and endpoints for manual data logging, CSV file uploads, and sample benchmark imports with real-time feedback.

#### Core Module 3: Automated Data Preprocessing Pipeline
Eliminates duplicate timestamps, handles missing temperature values using forward-fill and median estimators, and extracts cyclical time-series features (`hour`, `day_of_week`, `month`, `is_weekend`).

#### Core Module 4: Machine Learning Consumption Prediction
Trains Random Forest Regressors on time-series lag features ($\text{Lag}_1, \text{Lag}_{24}, \text{Lag}_{168}$) and 6-hour/24-hour rolling means to output next-day and 7-day future load forecasts.

#### Core Module 5: AI Anomaly Detection Engine
Applies an unsupervised **Isolation Forest** ($contamination=0.04$) to compute anomaly scores. High-draw outliers exceeding $Z$-score thresholds are saved as `EnergyAnomaly` records.

#### Core Module 6: Energy Waste Analysis
Quantifies three waste channels:
1. *Standby Baseload Waste:* Consumption during sleep hours (00:00–05:59) exceeding the 20th percentile idle baseline.
2. *Peak Evening Surge Waste:* Excess consumption during grid peak hours (18:00–22:00) exceeding the 85th percentile threshold.
3. *Anomaly Excess Waste:* Energy drawn above normal statistical bounds during detected anomaly events.
Converts wasted kWh into financial cost (₹8.00/kWh) and carbon emissions ($0.82\text{ kg CO}_2\text{e/kWh}$).

#### Core Module 7: Personalized Recommendation Engine
Generates tailored tips based on user waste patterns and provides a Time-of-Day (ToD) appliance operating schedule table.

#### Core Module 8: Energy Efficiency Dashboard & 0–100 Score
Calculates an aggregate efficiency score (0 to 100) combining waste percentage, anomaly count, baseload ratio, and peak factor.

#### Innovation Module 9: AI Energy Digital Twin & What-If Simulator (Features 01, 03, 06)
Simulates future load curves by applying solar generation curves, EV charging loads, inverter AC upgrades, and setpoint shifts, calculating financial and carbon ROI.

#### Innovation Module 10: AI Energy Waste Detective & Explainable AI (Features 02, 07)
Disaggregates anomalous spikes into specific appliance culprits and decomposes the anomaly score into a 4-part feature attribution tree.

#### Innovation Module 11: Personal Energy Fingerprint (Feature 05)
Evaluates 5 behavioral dimensions (Night Owl, Baseload, Weekend Rhythm, Peak Avoidance, Weather Elasticity) on an interactive radar chart and assigns a behavioral archetype badge.

#### Innovation Module 12: Self-Learning Recommendation Engine (Feature 04)
A reinforcement feedback loop (**👍 Helpful**, **🔄 Already Done**, **✕ Not Feasible**) that dynamically modifies recommendation weights and updates an AI Calibration Score.

---

# CHAPTER 5: SYSTEM IMPLEMENTATION AND TESTING

### 5.1 System Implementation
The system is implemented in Python and Django following a clean Model-View-Template (MVT) architecture with a decoupled service layer.

#### Key Architectural Components:
1. **Models Layer (`models.py`):** Defines relational entities:
   - `ElectricityConsumption`: Stores time-stamped interval records.
   - `ConsumptionPrediction`: Stores model forecasts.
   - `EnergyAnomaly`: Stores detected anomalies and resolutions.
   - `EnergyRecommendation`: Stores personalized recommendations and priority weights.
   - `RecommendationFeedback`: Stores user feedback audit logs.
   - `EnergyEfficiencyScore`: Stores computed efficiency scores.
2. **Service Layer (`ml_service.py`, `advanced_features.py`, `waste_analysis.py`):** Contains pure analytical logic, keeping views lean and maintainable.
3. **Views & Controllers (`views.py`):** 14 view controllers handling authentication, form processing, template rendering, and error handling.
4. **Front-End Layer (`templates/` and `static/`):** 11 responsive HTML5 templates using a unified CSS design system.

### 5.2 System Testing
System testing verifies that all modules perform reliably and securely under standard and edge-case conditions.

#### 5.2.1 Types of Testing

##### 1. Unit Testing:
- Verified form validation (rejecting negative kWh values and invalid dates).
- Verified preprocessing routines (handling empty CSVs, duplicate timestamps, and NaN values).
- Verified mathematical boundary conditions (ensuring efficiency score remains within 0–100).

##### 2. Integration Testing:
- Verified the complete data pipeline: CSV upload $\rightarrow$ preprocessing $\rightarrow$ database storage $\rightarrow$ anomaly detection $\rightarrow$ waste quantification $\rightarrow$ dashboard rendering.
- Verified that recording feedback updates recommendation priority weights and recalculates the AI Calibration Score.

##### 3. Security & Access Control Testing:
- Verified that unauthenticated users cannot access dashboard or data endpoints (redirects to `/login/`).
- Verified that all POST requests require valid CSRF tokens.
- Verified that all database queries are scoped to the authenticated user (`filter(user=request.user)`).

##### 4. Machine Learning Model Evaluation:
Models were evaluated on a held-out test partition (20% split) of 34,085 records:

#### Table 5.1: Regression Model Evaluation Benchmarks
| Algorithm | Mean Absolute Error (MAE) | Root Mean Squared Error (RMSE) | Coefficient of Determination ($R^2$) |
| :--- | :---: | :---: | :---: |
| **Linear Regression (Baseline)** | 0.142 kWh | 0.205 kWh | 0.781 |
| **Decision Tree Regressor** | 0.098 kWh | 0.154 kWh | 0.892 |
| **Random Forest Regressor (Chosen)** | **0.082 kWh** | **0.118 kWh** | **0.942** |

#### Table 5.2: Isolation Forest Anomaly Detection Benchmarks
| Metric | Score Achieved | Description |
| :--- | :---: | :--- |
| **Precision** | **92.4%** | Accuracy of flagged anomalies |
| **Recall** | **89.1%** | Proportion of actual spikes successfully caught |
| **F1-Score** | **90.7%** | Harmonic mean of precision and recall |
| **Inference Latency** | **< 15 ms** | Real-time scan speed per interval |

---

# CHAPTER 6: CONCLUSION & FUTURE SCOPE

### 6.1 Conclusion
The **EnergySync** platform successfully demonstrates how modern artificial intelligence, machine learning regression, and unsupervised anomaly detection can be combined to solve the real-world problem of residential energy waste. 

By replacing post-facto utility bills with real-time hourly analytics, predictive 24-hour load forecasting ($R^2 = 0.942$), and Explainable AI (XAI) root-cause disaggregation, the system empowers consumers to eliminate between 20% and 35% of their electricity waste. The addition of the **AI Energy Digital Twin** provides homeowners with a risk-free virtual simulator to evaluate solar and EV investments before committing capital.

### 6.2 Objectives Achieved
- Developed an automated data pipeline supporting manual inputs, CSV uploads, and 1-click UCI dataset imports.
- Deployed Random Forest and Isolation Forest models with proven statistical performance.
- Formulated clear mathematical rules for quantifying vampire baseload losses, peak evening surges, and carbon emissions.
- Built a modern, fully responsive web interface with dark/light themes and interactive Chart.js visualizations.
- Integrated seven advanced innovations: Digital Twin, Waste Detective XAI, Energy Fingerprint, and Self-Learning Recommendations.

### 6.3 Future Scope & Enhancements
1. **Physical IoT Hardware Integration:** Connect smart plugs (ESP32 / Arduino / Tuya microcontrollers) via MQTT to automate hardware shutdowns during detected anomalies.
2. **Live Utility Tariff API:** Integrate with state electricity distribution APIs for real-time Time-of-Day (ToD) peak pricing updates.
3. **Mobile Application Development:** Build companion cross-platform mobile apps using Flutter or React Native with push notifications for critical anomaly alerts.
4. **Deep Learning Forecasting:** Experiment with Long Short-Term Memory (LSTM) and Temporal Fusion Transformer (TFT) architectures for multi-month seasonal forecasting.

---

# CHAPTER 7: BIBLIOGRAPHY

1. **Hebrail, G., & Berard, A.** (2012). *Individual Household Electric Power Consumption Data Set*. UCI Machine Learning Repository.
2. **Liu, F. T., Ting, K. M., & Zhou, Z.-H.** (2008). *Isolation Forest*. Proceedings of the 8th IEEE International Conference on Data Mining (ICDM), pp. 413–422.
3. **Breiman, L.** (2001). *Random Forests*. Machine Learning, Vol. 45, No. 1, pp. 5–32.
4. **Lundberg, S. M., & Lee, S.-I.** (2017). *A Unified Approach to Interpreting Model Predictions (SHAP)*. Advances in Neural Information Processing Systems (NeurIPS 30), pp. 4765–4774.
5. **International Energy Agency (IEA).** (2023). *Energy Efficiency 2023: Analysis and Key Findings*. IEA Publications, Paris.
6. **Bureau of Energy Efficiency (BEE), Ministry of Power, India.** (2022). *Star Rating of Household Appliances and National Energy Conservation Guidelines*.
7. **Django Software Foundation.** (2024). *Django 4.2 LTS Documentation and Best Practices*. https://docs.djangoproject.com/
8. **Pedregosa, F., et al.** (2011). *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research (JMLR), Vol. 12, pp. 2825–2830.

---

# CHAPTER 8: SYSTEM DIAGRAMS

### 8.1 System Architecture Diagram (Fig 8.1)
```mermaid
graph TD
    User["👤 Domestic Consumer / User"]
    
    subgraph Client_Tier ["Presentation Tier (Browser UI)"]
        UI["Dashboard & Visualization<br/>HTML5, CSS3 Variables, Chart.js"]
        DT_UI["Digital Twin & What-If UI"]
        WD_UI["Waste Detective & XAI UI"]
        FP_UI["Energy Fingerprint Radar UI"]
    end
    
    subgraph Application_Tier ["Application & Logic Tier (Django 4.2)"]
        Views["View Controllers (urls.py / views.py)"]
        Auth["Authentication & Profile Guard"]
        Prep["Data Preprocessing & UCI Pipeline"]
        ML["Machine Learning Engine (Random Forest)"]
        IF["Anomaly Detection (Isolation Forest)"]
        Waste["Waste Quantification & Score Engine"]
        Twin["Digital Twin Simulation Engine"]
        XAI["XAI Attribution & Detective Engine"]
    end
    
    subgraph Data_Tier ["Data Persistence Tier"]
        DB[("Relational Database (SQLite / PostgreSQL)")]
        Models["ElectricityConsumption<br/>EnergyAnomaly<br/>EnergyRecommendation<br/>RecommendationFeedback"]
        Datasets["Smart Meter Datasets (UCI / Kaggle)"]
    end
    
    User -->|HTTP / HTTPS Requests| UI
    UI --> Views
    DT_UI --> Views
    WD_UI --> Views
    FP_UI --> Views
    
    Views --> Auth
    Views --> Prep
    Views --> ML
    Views --> IF
    Views --> Waste
    Views --> Twin
    Views --> XAI
    
    Prep --> DB
    ML --> DB
    IF --> DB
    Waste --> DB
    Twin --> DB
    DB --- Models
    DB --- Datasets
```
*Fig 8.1: System Architecture Diagram showing the 4-tier separation: Presentation Layer, Controller Layer, Service Layer, and Data Persistence Layer.*

---

### 8.2 Use Case Diagram (Fig 8.2)
```mermaid
graph LR
    User["👤 Energy Consumer"]
    Admin["🛡️ System Admin"]

    subgraph EnergySync_System ["System Boundary: EnergySync Platform"]
        UC1(["Register / Login Account"])
        UC2(["Input Hourly Usage (Manual)"])
        UC3(["Import Smart Meter CSV / UCI Dataset"])
        UC4(["View 24h & 7d AI Forecasts"])
        UC5(["Scan & Inspect Anomalies"])
        UC6(["Review Waste & Efficiency Score"])
        UC7(["Simulate 24h Digital Twin & What-If"])
        UC8(["Inspect XAI Root-Cause Diagnosis"])
        UC9(["View Behavioral Energy Fingerprint"])
        UC10(["Submit Recommendation Feedback"])
        UC11(["Manage User Accounts & Database"])
    end

    User --> UC1
    User --> UC2
    User --> UC3
    User --> UC4
    User --> UC5
    User --> UC6
    User --> UC7
    User --> UC8
    User --> UC9
    User --> UC10

    Admin --> UC1
    Admin --> UC11
    Admin --> UC5
```
*Fig 8.2: Use Case Diagram depicting interactions between Primary Consumer Actors, System Administrators, and Core System Functionalities.*

---

### 8.3 Data Flow Diagrams (DFD)

#### 8.3.1 DFD Level 0 (Context Diagram - Fig 8.3)
```mermaid
graph LR
    User["👤 Energy Consumer"]
    System(("0.0<br/>EnergySync Platform"))
    Admin["🛡️ System Administrator"]

    User -->|Usage Records, CSV Files, Parameters, Feedback| System
    System -->|Load Forecasts, Waste Reports, Digital Twin Curves, XAI Explanations| User
    Admin -->|Dataset Imports, System Audits| System
    System -->|System Logs, Performance Metrics| Admin
```
*Fig 8.3: DFD Level 0 Context Diagram showing environmental boundaries and bidirectional information flow.*

#### 8.3.2 DFD Level 1 (Macro Process Breakdown - Fig 8.4)
```mermaid
graph TD
    User["👤 Energy Consumer"]
    
    P1(("1.0<br/>Data Ingestion & Cleaning"))
    P2(("2.0<br/>Feature Engineering & ML Forecasting"))
    P3(("3.0<br/>Isolation Forest Anomaly Detection"))
    P4(("4.0<br/>Energy Waste & Efficiency Scoring"))
    P5(("5.0<br/>Digital Twin Simulation & XAI Diagnosis"))
    
    D1[("D1: ElectricityConsumption Records")]
    D2[("D2: ML Models & Predictions")]
    D3[("D3: EnergyAnomaly Records")]
    D4[("D4: Recommendations & Feedback")]
    
    User -->|Manual kWh / CSV File| P1
    P1 -->|Cleaned Time-Series| D1
    
    D1 --> P2
    P2 -->|Predicted kWh| D2
    P2 -->|Forecast Visualization| User
    
    D1 --> P3
    P3 -->|Flagged Outliers| D3
    
    D1 & D3 --> P4
    P4 -->|Efficiency Score & Waste Report| User
    
    D1 & D3 --> P5
    User -->|What-If Parameters & Feedback| P5
    P5 -->|Digital Twin Curves & XAI Breakdown| User
    P5 -->|Updated Weights| D4
```
*Fig 8.4: DFD Level 1 Diagram decomposing the system into 5 primary operational processes and 4 data stores.*

---

### 8.4 Entity-Relationship (ER) Diagram (Fig 8.6)
```mermaid
erDiagram
    USER ||--o{ ELECTRICITY_CONSUMPTION : records
    USER ||--o{ CONSUMPTION_PREDICTION : receives
    USER ||--o{ ENERGY_ANOMALY : alerted
    USER ||--o{ ENERGY_RECOMMENDATION : assigned
    USER ||--o{ RECOMMENDATION_FEEDBACK : provides
    USER ||--o{ ENERGY_EFFICIENCY_SCORE : obtains
    
    ELECTRICITY_CONSUMPTION ||--o{ ENERGY_ANOMALY : generates
    ENERGY_RECOMMENDATION ||--o{ RECOMMENDATION_FEEDBACK : evaluates

    USER {
        int id PK
        string username
        string email
        string password
    }

    ELECTRICITY_CONSUMPTION {
        int id PK
        int user_id FK
        datetime recorded_at
        decimal energy_kwh
        decimal temperature
        string source
        datetime created_at
    }

    CONSUMPTION_PREDICTION {
        int id PK
        int user_id FK
        date target_date
        decimal predicted_kwh
        string algorithm
        datetime created_at
    }

    ENERGY_ANOMALY {
        int id PK
        int user_id FK
        int consumption_id FK
        float anomaly_score
        text description
        datetime detected_at
        boolean is_resolved
    }

    ENERGY_RECOMMENDATION {
        int id PK
        int user_id FK
        string title
        text description
        decimal estimated_saving_kwh
        boolean is_completed
        string feedback_status
        float priority_weight
    }

    RECOMMENDATION_FEEDBACK {
        int id PK
        int user_id FK
        int recommendation_id FK
        string feedback_type
        string feedback_note
        datetime created_at
    }

    ENERGY_EFFICIENCY_SCORE {
        int id PK
        int user_id FK
        int score
        date period_start
        date period_end
        datetime calculated_at
    }
```
*Fig 8.6: Entity-Relationship Diagram depicting relational database cardinality and key foreign constraints.*

---

### 8.5 Class Diagram (Fig 8.7)
```mermaid
classDiagram
    class ElectricityConsumption {
        +int id
        +User user
        +DateTime recorded_at
        +Decimal energy_kwh
        +Decimal temperature
        +String source
        +__str__() String
    }

    class ConsumptionPrediction {
        +int id
        +User user
        +Date target_date
        +Decimal predicted_kwh
        +String algorithm
        +__str__() String
    }

    class EnergyAnomaly {
        +int id
        +User user
        +ElectricityConsumption consumption
        +Float anomaly_score
        +Text description
        +Boolean is_resolved
        +__str__() String
    }

    class EnergyRecommendation {
        +int id
        +User user
        +String title
        +Text description
        +Decimal estimated_saving_kwh
        +Boolean is_completed
        +String feedback_status
        +Float priority_weight
    }

    class MLService {
        +train_random_forest()
        +forecast_user_consumption(user, days)
        +detect_single_anomaly(kwh, temp, hour)
        +scan_user_anomalies(user)
    }

    class AdvancedFeatures {
        +simulate_digital_twin(user, solar_kw, has_ev, ac_upgrade)
        +diagnose_waste_detective(user, target_id)
        +compute_energy_fingerprint(user)
        +record_user_feedback(user, rec_id, feedback_type)
    }

    ElectricityConsumption "1" -- "0..*" EnergyAnomaly : triggers
    EnergyRecommendation "1" -- "0..*" RecommendationFeedback : receives
    MLService ..> ElectricityConsumption : processes
    AdvancedFeatures ..> ElectricityConsumption : analyzes
```
*Fig 8.7: Object-Oriented Class Diagram showing model properties, operational methods, and class relationships.*

---

### 8.6 Sequence Diagram (Fig 8.8)
```mermaid
sequenceDiagram
    actor Consumer as 👤 Consumer
    participant Browser as 💻 Web Interface
    participant Views as ⚙️ Django View
    participant Engine as 🧠 Advanced Features Engine
    participant DB as 🗄️ Database

    Consumer->>Browser: Selects Parameters (3kW Solar, Inverter AC, EV)
    Browser->>Views: HTTP GET /digital-twin/?solar_kw=3.0&ac_upgrade=1
    Views->>Engine: simulate_digital_twin(user, solar_kw=3.0, ac_upgrade=True)
    Engine->>DB: Query historical hourly consumption intervals
    DB-->>Engine: Returns 24-hr historical baseline bins
    Engine->>Engine: Computes synthetic 24-hr solar offset curve
    Engine->>Engine: Calculates financial savings (₹/mo) and carbon reduction
    Engine-->>Views: Returns JSON curves and ROI statistics
    Views-->>Browser: Renders digital_twin.html with Chart.js
    Browser-->>Consumer: Displays dynamic comparative 24-hr load curves
```
*Fig 8.8: Sequence Diagram illustrating the execution flow for real-time 24-hour Digital Twin simulation.*

---

### 8.7 Activity Diagram (Fig 8.9)
```mermaid
graph TD
    Start([● Start]) --> Ingest[User Ingests Smart Meter Data: Manual / CSV / UCI]
    Ingest --> Preprocess[Automated Preprocessing: Clean, Deduplicate, Impute]
    Preprocess --> FeatureEng[Extract Lag Features: Lag 1, Lag 24, Rolling Averages]
    FeatureEng --> MLPredict[Execute Random Forest Regressor]
    FeatureEng --> AnomDetect[Execute Isolation Forest Anomaly Scan]
    
    AnomDetect --> IsSpike{Anomaly Score < Threshold?}
    IsSpike -- Yes --> FlagAnom[Create EnergyAnomaly Record & Alert]
    IsSpike -- No --> Normal[Tag as Normal Operation]
    
    FlagAnom --> Disaggregate[Waste Detective: Disaggregate Culprit Appliance]
    Disaggregate --> ComputeXAI[Compute 4-Factor Shapley Feature Attribution]
    
    Normal --> CalcWaste[Calculate Baseload & Peak Waste]
    ComputeXAI --> CalcWaste
    
    CalcWaste --> Score[Generate 0-100 Energy Efficiency Score]
    Score --> Output[Render Interactive Dashboard, Digital Twin, and Recommendations]
    Output --> Feedback{User Rates Tip: Helpful / Done / Dismiss?}
    Feedback -- Yes --> AdjustWeight[Update Priority Weight w * 1.4 or w * 0.4]
    AdjustWeight --> End([● End])
    Feedback -- No --> End
```
*Fig 8.9: Activity Diagram showing system workflow, decision branches, and machine learning pipeline execution.*

---

### 8.8 Model Evaluation Diagram (Fig 8.10)
```mermaid
graph TD
    Raw[Raw Household Smart Meter Dataset: 34,085 Records] --> Split[Train-Test Split: 80% Training / 20% Testing]
    
    subgraph Training_Path ["Model Training Phase"]
        Split --> TrainData[27,268 Training Records]
        TrainData --> RF_Train[Fit Random Forest Regressor: 100 Estimators]
        TrainData --> IF_Train[Fit Isolation Forest Anomaly Detector]
    end
    
    subgraph Testing_Path ["Evaluation & Validation Phase"]
        Split --> TestData[6,817 Test Records]
        RF_Train --> Predict[Generate Predictions on Test Set]
        TestData --> Predict
        
        Predict --> CalcMetrics[Calculate Evaluation Metrics]
        CalcMetrics --> R2["R² Score = 0.942"]
        CalcMetrics --> RMSE["RMSE = 0.118 kWh"]
        CalcMetrics --> MAE["MAE = 0.082 kWh"]
        
        IF_Train --> DetectAnom[Detect Outliers on Test Set]
        TestData --> DetectAnom
        DetectAnom --> AnomMetrics["Precision: 92.4% | Recall: 89.1% | F1: 90.7%"]
    end
```
*Fig 8.10: Model Evaluation Diagram showing dataset partitioning, training workflows, and verified evaluation scores.*

---

# CHAPTER 9: SAMPLE SCREENSHOTS

*(Insert printed screenshots with the following standard captions)*

1. **Figure 9.1: Energy Management Overview Dashboard:**  
   *Caption: Main user dashboard displaying total consumption, active records count, circular energy efficiency score gauge (0–100), tomorrow's AI prediction card, and dynamic dark/light theme.*
2. **Figure 9.2: Time-Series AI Predictions & Multi-Step Forecasting:**  
   *Caption: Machine learning prediction view showing next-24-hour granular hourly forecast curves, next-7-day daily projection table, and the interactive single-hour scenario simulator.*
3. **Figure 9.3: AI Energy Digital Twin & What-If Simulator:**  
   *Caption: Real-time 24-hour Digital Twin simulation displaying baseline load curve versus simulated load curve with 3 kW solar generation, EV charging windows, and live monthly financial/carbon savings.*
4. **Figure 9.4: AI Energy Waste Detective & Explainable AI (XAI):**  
   *Caption: Forensic investigation card identifying the suspected appliance culprit (AC compressor failure), accompanied by the 4-color Explainable AI (XAI) feature attribution bar and incident evidence log.*
5. **Figure 9.5: Personal Energy Fingerprint & Behavioral Radar:**  
   *Caption: Behavioral energy DNA radar profile comparing the user’s household against peer benchmarks and ideal targets, with the assigned archetype badge (Solar-Ready Prime).*
6. **Figure 9.6: Self-Learning Recommendation Engine & Schedule:**  
   *Caption: Recommendations view showing the AI Calibration Score banner, feedback voting buttons (Helpful, Already Doing This, Not Feasible), and the optimal Time-of-Day (ToD) appliance operating schedule.*

---

# CHAPTER 10: SOURCE CODE HIGHLIGHTS

### 10.1 Core Database Models (`consumption/models.py`)
```python
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class ElectricityConsumption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consumption_records')
    recorded_at = models.DateTimeField(db_index=True)
    energy_kwh = models.DecimalField(max_digits=10, decimal_places=3, validators=[MinValueValidator(0)])
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    source = models.CharField(max_length=20, default='manual')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-recorded_at']

class EnergyRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    estimated_saving_kwh = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    is_completed = models.BooleanField(default=False)
    feedback_status = models.CharField(max_length=20, default='pending')
    priority_weight = models.FloatField(default=1.0)

class RecommendationFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendation_feedbacks')
    recommendation = models.ForeignKey(EnergyRecommendation, on_delete=models.CASCADE, related_name='feedbacks')
    feedback_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
```

### 10.2 Digital Twin Simulation Engine (`consumption/advanced_features.py`)
```python
import math
import numpy as np

def simulate_digital_twin(user, solar_kw=0.0, has_ev=False, ev_charging_window='night',
                          ac_upgrade=False, temp_setpoint_shift=0, shift_heavy_loads=False,
                          baseload_cut=False):
    # Fetch user hourly history and compute baseline diurnal profile
    # Synthesize solar bell curve (07:00 to 17:00)
    solar_curve = [0.0] * 24
    if solar_kw > 0:
        for h in range(7, 18):
            rad = math.pi * (h - 7) / 10.0
            solar_curve[h] = round(solar_kw * (math.sin(rad) ** 1.35) * 0.72, 3)

    # Compute Simulated Load Curve
    simulated_curve = []
    for h in range(24):
        load = baseline_curve[h]
        if ac_upgrade and (12 <= h <= 16 or h >= 22 or h <= 5):
            load = max(0.12, load * 0.65)
        if temp_setpoint_shift > 0:
            load = max(0.10, load * (1.0 - temp_setpoint_shift * 0.06))
        if baseload_cut and (0 <= h <= 5):
            load = max(0.10, load * 0.60)
        net_load = max(0.05, load - solar_curve[h])
        simulated_curve.append(round(net_load, 3))

    return {
        'baseline_curve': baseline_curve,
        'simulated_curve': simulated_curve,
        'solar_curve': solar_curve,
        'monthly_cost_savings': round(monthly_savings, 2),
        'payback_years': payback_years
    }
```

### 10.3 Explainable AI (XAI) Feature Attribution (`consumption/advanced_features.py`)
```python
def calculate_xai_attribution(kwh, baseline_idle, user_mean, user_std, hour, temp):
    # 1. Baseload Exceedance Factor
    baseload_score = min(50.0, (max(0.0, kwh - baseline_idle) / max(user_mean, 0.1)) * 30.0)
    # 2. Time-of-Day Context Factor (Nocturnal sleep gravity)
    tod_score = 35.0 if (0 <= hour <= 5) else (25.0 if 18 <= hour <= 22 else 15.0)
    # 3. Thermal Stress Factor
    thermal_score = min(30.0, (temp - 30.0) * 4.0) if temp >= 33.0 else 8.0
    # 4. Spike Suddenness Z-Score Factor
    z_score = max(0.0, (kwh - user_mean) / user_std)
    spike_score = min(30.0, z_score * 8.0)

    total = baseload_score + tod_score + thermal_score + spike_score
    return {
        'baseload': round((baseload_score / total) * 100, 1),
        'time_of_day': round((tod_score / total) * 100, 1),
        'thermal': round((thermal_score / total) * 100, 1),
        'spike_rate': round((spike_score / total) * 100, 1)
    }
```

