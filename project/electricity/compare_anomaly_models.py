
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    average_precision_score
)

# 1. Load dataset
df = pd.read_csv("datasets/smart_meter_data.csv")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df = df.sort_values("Timestamp").reset_index(drop=True)

# 2. Create time features
df["Hour"] = df["Timestamp"].dt.hour
df["Day"] = df["Timestamp"].dt.day
df["DayOfWeek"] = df["Timestamp"].dt.day_of_week
df["Month"] = df["Timestamp"].dt.month
df["IsWeekend"] = (df["DayOfWeek"] >= 5).astype(int)

# 3. Prepare features
old_features = [
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

new_features = [
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

X_old = df[old_features]
X_new = df[new_features]

y = (df["Anomaly_Label"] == "Abnormal").astype(int)

# 4. Chronological 80/20 split
split = int(len(df) * 0.8)

X_old_train, X_old_test = X_old.iloc[:split], X_old.iloc[split:]
X_train, X_test = X_new.iloc[:split], X_new.iloc[split:]

y_train, y_test = y.iloc[:split], y.iloc[split:]

# 5. Evaluation function
def evaluate_model(name, y_true, predictions, scores=None):

    print("\n" + "=" * 55)
    print(name)
    print("=" * 55)

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, predictions, labels=[0, 1]))

    print("\nClassification Report:")
    print(classification_report(
        y_true,
        predictions,
        labels=[0, 1],
        target_names=["Normal", "Abnormal"],
        zero_division=0
    ))

    if scores is not None:
        print(
            "Average Precision:",
            round(average_precision_score(y_true, scores), 4)
        )


# 6. Model 1: Original Random Forest
old_rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

old_rf.fit(X_old_train, y_train)

old_predictions = old_rf.predict(X_old_test)
old_scores = old_rf.predict_proba(X_old_test)[:, 1]

evaluate_model(
    "MODEL 1 - ORIGINAL RANDOM FOREST",
    y_test,
    old_predictions,
    old_scores
)

# 7. Model 2: Improved Random Forest
new_rf = RandomForestClassifier(
    n_estimators=300,
    max_depth=15,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

new_rf.fit(X_train, y_train)

new_predictions = new_rf.predict(X_test)
new_scores = new_rf.predict_proba(X_test)[:, 1]

evaluate_model(
    "MODEL 2 - IMPROVED RANDOM FOREST",
    y_test,
    new_predictions,
    new_scores
)

# 8. Model 3: Isolation Forest
isolation = IsolationForest(
    n_estimators=200,
    contamination=0.05,
    random_state=42,
    n_jobs=-1
)

isolation.fit(X_train)

isolation_predictions = isolation.predict(X_test)

# Isolation Forest: -1 = anomaly, 1 = normal
isolation_predictions = (isolation_predictions == -1).astype(int)

isolation_scores = -isolation.decision_function(X_test)

evaluate_model(
    "MODEL 3 - ISOLATION FOREST",
    y_test,
    isolation_predictions,
    isolation_scores
)

# 9. Model 4: Rule-based detection
consumption = df["Electricity_Consumed"].iloc[split:]

rule_predictions = (
    (consumption < 0.10) |
    (consumption > 0.75)
).astype(int)

evaluate_model(
    "MODEL 4 - RULE-BASED DETECTION",
    y_test,
    rule_predictions
)

print("\n========== COMPARISON COMPLETED ==========")
