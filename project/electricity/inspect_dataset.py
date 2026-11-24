
import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/smart_meter_data.csv")

print("\n========== DATASET OVERVIEW ==========")

print("\nTotal Records:", len(df))
print("Total Columns:", len(df.columns))

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== FIRST 5 RECORDS ==========")
print(df.head())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE RECORDS ==========")
print(df.duplicated().sum())

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

print("\n========== ANOMALY DISTRIBUTION ==========")
print(df["Anomaly_Label"].value_counts())

print("\n========== DATASET INFORMATION ==========")
print(df.info())
