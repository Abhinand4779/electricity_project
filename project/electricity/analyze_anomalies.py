
import pandas as pd

df = pd.read_csv("datasets/smart_meter_data.csv")

features = [
    "Electricity_Consumed",
    "Temperature",
    "Humidity",
    "Wind_Speed",
    "Avg_Past_Consumption"
]

# 1. Compare feature averages
print("\n========== NORMAL VS ABNORMAL ==========")

print(
    df.groupby("Anomaly_Label")[features].mean().round(4)
)

# 2. Compare feature distributions
print("\n========== FEATURE STANDARD DEVIATION ==========")

print(
    df.groupby("Anomaly_Label")[features].std().round(4)
)

# 3. Correlation with electricity consumption
print("\n========== CORRELATION BY CLASS ==========")

for label in df["Anomaly_Label"].unique():

    subset = df[df["Anomaly_Label"] == label]

    print(f"\n{label}:")

    print(
        subset[features].corr()["Electricity_Consumed"]
        .round(4)
    )

# 4. Check target variation
print("\n========== CONSUMPTION DISTRIBUTION ==========")

print(
    df.groupby("Anomaly_Label")[
        "Electricity_Consumed"
    ].describe().round(4)
)

# 5. Check target autocorrelation
print("\n========== AUTOCORRELATION ==========")

for lag in [1, 2, 4, 48, 96]:

    print(
        f"Lag {lag}:",
        round(
            df["Electricity_Consumed"].autocorr(lag=lag),
            4
        )
    )

print("\n========== ANALYSIS COMPLETED ==========")
