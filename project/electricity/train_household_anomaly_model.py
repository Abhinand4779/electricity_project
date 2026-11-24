
import pandas as pd
import joblib
from pathlib import Path
from sklearn.ensemble import IsolationForest

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "datasets" / "household_hourly_consumption.csv"
MODEL_DIR = BASE_DIR / "consumption" / "ml_models"

MODEL_DIR.mkdir(parents=True, exist_ok=True)

# Load dataset
df = pd.read_csv(DATASET_PATH)

# Features used by the model
features = [
    "energy_kwh",
    "hour",
    "day_of_week",
    "month",
    "is_weekend"
]

# Check required columns
if not all(column in df.columns for column in features):
    raise ValueError("Required dataset columns are missing.")

# Prepare data
X = df[features].copy()

# Train unsupervised anomaly detection model
model = IsolationForest(
    n_estimators=200,
    contamination=0.02,
    random_state=42
)

model.fit(X)

# Save model and feature names
joblib.dump(
    {
        "model": model,
        "features": features
    },
    MODEL_DIR / "household_anomaly_model.pkl"
)

# Display training results
predictions = model.predict(X)
anomalies = (predictions == -1).sum()

print("========== HOUSEHOLD MODEL TRAINED ==========")
print("Model: Isolation Forest")
print("Training records:", len(df))
print("Features:", features)
print("Detected unusual records:", anomalies)
print("Model saved successfully!")
