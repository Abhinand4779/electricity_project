
import pandas as pd
import numpy as np

df = pd.read_csv("datasets/smart_meter_data.csv")

print("\n========== ANOMALY QUANTILES ==========")

print(
    df.groupby("Anomaly_Label")["Electricity_Consumed"]
    .quantile([0, 0.05, 0.25, 0.50, 0.75, 0.95, 1])
    .unstack()
)

print("\n========== EXTREME CONSUMPTION ==========")

for label, group in df.groupby("Anomaly_Label"):
    values = group["Electricity_Consumed"]

    print(f"\n{label}")
    print("Minimum:", values.min())
    print("Maximum:", values.max())
    print("Below 0.10:", (values < 0.10).sum())
    print("Above 0.75:", (values > 0.75).sum())

print("\n========== ANOMALY FEATURE RANGES ==========")

features = [
    "Electricity_Consumed",
    "Temperature",
    "Humidity",
    "Wind_Speed",
    "Avg_Past_Consumption"
]

for feature in features:
    print(f"\n{feature}")

    print(
        df.groupby("Anomaly_Label")[feature]
        .agg(["min", "max", "mean", "std"])
        .round(4)
    )

print("\n========== LABEL AND CONSUMPTION RELATIONSHIP ==========")

df["Extreme_Consumption"] = (
    (df["Electricity_Consumed"] < 0.10) |
    (df["Electricity_Consumed"] > 0.75)
)

print(
    pd.crosstab(
        df["Anomaly_Label"],
        df["Extreme_Consumption"],
        normalize="index"
    ).round(3)
)

print("\n========== COMPLETED ==========")
