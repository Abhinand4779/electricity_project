
import pandas as pd

# Load dataset
df = pd.read_csv("datasets/smart_meter_data.csv")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

df = df.sort_values("Timestamp").reset_index(drop=True)

target = "Electricity_Consumed"

# Create historical features
df["Previous_Consumption"] = df[target].shift(1)

df["Consumption_1_Hour_Ago"] = df[target].shift(2)

df["Consumption_24_Hours_Ago"] = df[target].shift(48)

df["Rolling_Average_4"] = (
    df[target].shift(1).rolling(4).mean()
)

df["Rolling_Average_48"] = (
    df[target].shift(1).rolling(48).mean()
)

print("\n========== HISTORICAL FEATURE CORRELATION ==========")

features = [
    "Previous_Consumption",
    "Consumption_1_Hour_Ago",
    "Consumption_24_Hours_Ago",
    "Rolling_Average_4",
    "Rolling_Average_48"
]

print(
    df[features + [target]].corr()[target].sort_values(
        ascending=False
    )
)

print("\n========== ANOMALY DISTRIBUTION BY HOUR ==========")

df["Hour"] = df["Timestamp"].dt.hour

print(
    pd.crosstab(
        df["Hour"],
        df["Anomaly_Label"],
        normalize="index"
    ).round(3)
)

print("\n========== HISTORICAL FEATURES ==========")

print(df[features].describe())

print("\n========== ANALYSIS COMPLETED ==========")
