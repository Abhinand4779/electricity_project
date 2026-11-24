# AI-Powered Personal Energy Waste Predictor
**Artificial Intelligence and Machine Learning Project**

An intelligent energy-management system designed to monitor electricity consumption patterns, predict future requirements using machine learning, detect abnormal usage, estimate energy wastage, and recommend actionable energy-saving practices.

---

## 📌 Project Overview & Architecture

Based on the official project specification, this system addresses excess electricity consumption caused by invisible wastage habits, standby vampire loads, and unusual usage spikes.

```
User / Electricity Dataset (UCI / Kaggle / Manual / CSV)
                     ↓
         Data Collection & Preprocessing
      (Cleaning, Deduplication, Feature Extraction)
                     ↓
               Machine Learning Models
     ┌───────────────┬──────────────────────┬────────────────────┐
     │               │                      │                    │
Linear Regression   Random Forest      Time-Series          Isolation Forest
(Baseline Metric)   (Primary Predictor) (24h & 7d Forecast) (Unsupervised Anomaly)
     └───────────────┴──────────────────────┴────────────────────┘
                     ↓
         Energy Waste & Loss Analysis
 (Standby Baseload Waste, Peak Spikes, Financial & Carbon Impact)
                     ↓
      Energy-Saving Recommendation Engine
   (Actionable Savings & Appliance Operating Schedule)
                     ↓
        Interactive Management Dashboard
(Efficiency Score 0-100, Multi-period Comparisons, Anomaly Alerts)
```

---

## 🚀 Key Modules Implemented

### Module 1: User Management
- Secure user registration, authentication, and session handling.
- Individual user profile data isolation so each user manages their own energy records, anomalies, and efficiency scores.

### Module 2: Electricity Data Collection
- **Manual Data Entry**: Input consumption in kilowatt-hours (kWh) along with ambient temperature and environmental metrics.
- **CSV Dataset Import**: Direct file upload with support for standard smart meter CSV files.
- **1-Click Sample Benchmark Importer**: Quickly load 168 hourly records (1 full week) from the UCI Individual Household Electric Power Consumption dataset for instant evaluation.

### Module 3: Automated Data Preprocessing Pipeline
- **Deduplication**: Removes duplicate timestamp records.
- **Missing Value Imputation**: Imputes missing environmental readings (e.g., temperature) using median estimators.
- **Sanity & Outlier Filtering**: Identifies and drops negative values or invalid timestamps.
- **Feature Extraction**: Generates `Hour`, `Day`, `DayOfWeek`, `Month`, `IsWeekend`, and `UsagePeriod` (Night, Morning, Afternoon, Evening).

### Module 4: Electricity Consumption Prediction & Forecasting
- **Linear Regression & Random Forest Regression**: Evaluates both models and benchmarks MAE, RMSE, and $R^2$ scores.
- **Time-Series Forecasting**:
  - **Next 24 Hours**: Granular hourly consumption forecast.
  - **Next 7 Days**: Daily consumption forecast combining machine learning regressors with seasonal day-of-week trends.
- **Interactive Scenario Simulator**: Test hypothetical weather conditions, hours of day, and past baselines with instant predicted kWh output.

### Module 5: AI Anomaly Detection
- **Isolation Forest (Unsupervised)**: Trained on 34,085 UCI household records to identify atypical usage without requiring manual labels.
- **Random Forest Classifier (Supervised)**: Secondary multi-feature anomaly detection.
- **Automated Scan**: Automatically flags spikes during data entry or via a 1-click historical scan.
- **Anomaly Alerts**: Dynamic warning banners displayed across the dashboard and dedicated anomaly review interface.

### Module 6: Energy Waste Analysis
- **Standby / Baseload Midnight Waste**: Identifies vampire power loss occurring between 12:00 AM – 05:59 AM.
- **Peak Evening Surge Waste**: Analyzes demand spikes during dinner peak hours (06:00 PM – 10:00 PM).
- **Anomaly Excess Waste**: Calculates cumulative kWh consumed beyond expected normal thresholds.
- **Financial & Environmental Metrics**: Converts wasted kWh into monetary cost (₹ / $) and carbon emissions (0.82 kg $\text{CO}_2\text{e}$/kWh).

### Module 7: Energy-Saving Recommendations
- **Personalized Recommendations**: Automatically generates tailored tips based on user's actual waste breakdown.
- **Savings Tracker**: Users can mark recommendations as completed and track cumulative energy savings achieved.
- **Appliance Operating Schedule**: Clear timetable specifying optimal hours for running washing machines, dishwashers, AC pre-cooling, water heaters, and EV chargers to minimize peak grid charges.

### Module 8: Energy-Efficiency Dashboard & Score
- **Personalized Efficiency Score (0 to 100)**: Evaluates anomaly frequency, baseload ratio, peak-to-average ratio, and usage consistency to output an efficiency grade (A+, A, B, C, D).
- **Multi-Period Visual Comparisons**: Toggle seamlessly between **Daily Usage**, **Weekly Usage**, and **Monthly Usage** views with Bar or Line chart styles.
- **Carbon Footprint Tracker**: Live tracking of environmental impact and sustainability ratings.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.x, Django 4.2+
- **Database**: SQLite
- **Machine Learning**: Scikit-Learn, Pandas, NumPy, Joblib
- **Frontend & Visualization**: HTML5, CSS3, JavaScript, Chart.js, Bootstrap Icons
- **Datasets**:
  - UCI Individual Household Electric Power Consumption Dataset (`household_hourly_consumption.csv`)
  - Kaggle Smart Meter Electricity Consumption Dataset (`smart_meter_data.csv`)

---

## 💻 How to Run the Project

### 1. Open Terminal and Navigate to the Django Directory
```bash
cd project/electricity
```

### 2. Verify Database Migrations (Pre-applied)
```bash
python manage.py migrate
```

### 3. Start the Development Server
```bash
python manage.py runserver 8080
```

### 4. Open in Your Web Browser
Navigate to:
```
http://127.0.0.1:8080/
```

### 5. Login Credentials
Pre-configured accounts ready for testing:
- **Admin / Superuser Account**:
  - **Username**: `hp`
  - **Password**: `admin123`
- **Standard Demo Account**:
  - **Username**: `demo_user`
  - **Password**: `demo1234`
- *(Alternatively, click **"Create an account"** on the login page to register a new user)*

---

## 📁 Project Directory Structure

```
project/
├── electricity/                     # Django Project Root
│   ├── manage.py                    # Django management script
│   ├── db.sqlite3                   # SQLite database
│   ├── electricity/                 # Django settings and root routing
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── consumption/                 # Core Energy Application
│   │   ├── models.py                # Database models (Consumption, Anomaly, Prediction, etc.)
│   │   ├── views.py                 # View controllers for all 8 modules
│   │   ├── urls.py                  # Application routing
│   │   ├── forms.py                 # Input, upload, and simulator forms
│   │   ├── ml_service.py            # ML forecasting, anomaly detection, and benchmarks
│   │   ├── preprocessing.py         # Data cleaning, deduplication, and import pipeline
│   │   ├── waste_analysis.py        # Baseload, peak, and monetary waste calculations
│   │   ├── recommendations.py       # Personalized tips and appliance scheduling
│   │   ├── efficiency_score.py      # 0-100 score and grade evaluation engine
│   │   ├── ml_models/               # Serialized ML model bundles (.pkl)
│   │   ├── static/                  # CSS styles and JavaScript charts
│   │   └── templates/               # Responsive HTML templates
│   └── datasets/                    # Benchmark training and evaluation datasets
└── README.md                        # Documentation
```

