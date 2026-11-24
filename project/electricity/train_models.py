
import os
import pandas as pd
import joblib

from sklearn.ensemble import (
    RandomForestRegressor,
    RandomForestClassifier
)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    classification_report,
    confusion_matrix,
    accuracy_score,
    f1_score
)


# ==========================================
# 1. LOAD DATASET
# ==========================================

DATASET_PATH = "datasets/smart_meter_data.csv"

df = pd.read_csv(DATASET_PATH)

print("\n========== LOADING DATASET ==========")

print("Total records:", len(df))


# ==========================================
# 2. DATA PREPROCESSING
# ==========================================

df["Timestamp"] = pd.to_datetime(
    df["Timestamp"],
    errors="coerce"
)

df = df.dropna(subset=["Timestamp"])

df = df.sort_values("Timestamp").reset_index(drop=True)

# Create time-related features
df["Hour"] = df["Timestamp"].dt.hour
df["Day"] = df["Timestamp"].dt.day
df["DayOfWeek"] = df["Timestamp"].dt.day_of_week
df["Month"] = df["Timestamp"].dt.month
df["IsWeekend"] = (
df["Timestamp"].dt.day_of_week >= 5).astype(int)

# Model input features
FEATURES = [
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

# Sort chronologically and use first 80% for training
split_index = int(len(df) * 0.80)

train_data = df.iloc[:split_index].copy()
test_data = df.iloc[split_index:].copy()

X_train = train_data[FEATURES]
X_test = test_data[FEATURES]

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# ==========================================
# 3. MODEL 1 - CONSUMPTION PREDICTION
# ==========================================

print("\n========== RANDOM FOREST REGRESSOR ==========")

y_train = train_data["Electricity_Consumed"]
y_test = test_data["Electricity_Consumed"]

regressor = RandomForestRegressor(
    n_estimators=200,
    max_depth=15,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)

regressor.fit(X_train, y_train)

predictions = regressor.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5

r2 = r2_score(y_test, predictions)

print("\nConsumption Prediction Results")

print("MAE:", round(mae, 4))
print("RMSE:", round(rmse, 4))
print("R2 Score:", round(r2, 4))


# ==========================================
# 4. MODEL 2 - ANOMALY DETECTION
# ==========================================

print("\n========== RANDOM FOREST CLASSIFIER ==========")

y_anomaly_train = train_data["Anomaly_Label"].str.strip()
y_anomaly_test = test_data["Anomaly_Label"].str.strip()

classifier = RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

classifier.fit(X_train, y_anomaly_train)

anomaly_predictions = classifier.predict(X_test)

print("\nAnomaly Detection Results")

print(
    "Accuracy:",
    round(
        accuracy_score(
            y_anomaly_test,
            anomaly_predictions
        ),
        4
    )
)

print(
    "F1 Score:",
    round(
        f1_score(
            y_anomaly_test,
            anomaly_predictions,
            pos_label="Abnormal"
        ),
        4
    )
)

print("\nClassification Report:")

print(
    classification_report(
        y_anomaly_test,
        anomaly_predictions,
        zero_division=0
    )
)

print("Confusion Matrix:")

print(
    confusion_matrix(
        y_anomaly_test,
        anomaly_predictions,
        labels=["Normal", "Abnormal"]
    )
)


# ==========================================
# 5. SAVE TRAINED MODELS
# ==========================================

MODEL_DIR = "consumption/ml_models"

os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(
    regressor,
    os.path.join(
        MODEL_DIR,
        "consumption_predictor.pkl"
    )
)

joblib.dump(
    classifier,
    os.path.join(
        MODEL_DIR,
        "anomaly_detector.pkl"
    )
)

joblib.dump(
    FEATURES,
    os.path.join(
        MODEL_DIR,
        "model_features.pkl"
    )
)


# ==========================================
# 6. FEATURE IMPORTANCE
# ==========================================

print("\n========== FEATURE IMPORTANCE ==========")

importance = pd.DataFrame({
    "Feature": FEATURES,
    "Importance": regressor.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance.to_string(index=False))


print("\n======================================")
print("BOTH ML MODELS TRAINED SUCCESSFULLY!")
print("======================================")

print("\nSaved models in:", MODEL_DIR)
