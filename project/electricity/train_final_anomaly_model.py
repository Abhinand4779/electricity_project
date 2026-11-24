
import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("datasets/smart_meter_data.csv")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df = df.sort_values("Timestamp").reset_index(drop=True)

# Create time features
df["Hour"] = df["Timestamp"].dt.hour
df["Day"] = df["Timestamp"].dt.day
df["DayOfWeek"] = df["Timestamp"].dt.day_of_week
df["Month"] = df["Timestamp"].dt.month
df["IsWeekend"] = (df["DayOfWeek"] >= 5).astype(int)

# Features used by the improved model
features = [
    "Electricity_Consumed",
    "Temperature",
    "Humidity",
    "Wind_Speed",
    "Avg_Past_Consumption",
    "Hour",
    "Day",
    "DayOfWeek",
    "Month",
    "IsWeekend"
]

X = df[features]
y = (df["Anomaly_Label"] == "Abnormal").astype(int)

# Train final model on the complete dataset
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=15,
    class_weight="balanced",
    random_state=42,
    n_jobs=1
)

model.fit(X, y)

# Create model directory
os.makedirs("consumption/ml_models", exist_ok=True)

# Save model and feature information
joblib.dump(
    model,
    "consumption/ml_models/anomaly_detector_improved.pkl"
)

joblib.dump(
    features,
    "consumption/ml_models/anomaly_features.pkl"
)

print("========== FINAL MODEL TRAINED ==========")
print("Model: Improved Random Forest")
print("Training records:", len(X))
print("Features:", features)
print("Model saved successfully!")
