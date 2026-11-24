
import pandas as pd

df = pd.read_csv("datasets/smart_meter_data.csv")

print("\n========== CORRELATION ANALYSIS ==========")

print(
    df[
        [
            "Electricity_Consumed",
            "Temperature",
            "Humidity",
            "Wind_Speed",
            "Avg_Past_Consumption"
        ]
    ].corr()["Electricity_Consumed"].sort_values(
        ascending=False
    )
)

print("\n========== ANOMALY STATISTICS ==========")

print(df.groupby("Anomaly_Label")[
    [
        "Electricity_Consumed",
        "Temperature",
        "Humidity",
        "Wind_Speed",
        "Avg_Past_Consumption"
    ]
].mean())

print("\n========== TIMESTAMP ANALYSIS ==========")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

print("First timestamp:", df["Timestamp"].min())
print("Last timestamp:", df["Timestamp"].max())

print("\nTime difference between first records:")

print(df["Timestamp"].diff().value_counts().head())

print("\n========== COMPLETE ==========")
