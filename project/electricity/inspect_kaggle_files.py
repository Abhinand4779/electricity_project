import os
import pandas as pd

dataset_folder = "datasets"

print("\n========== DATASET FILES ==========")

for root, dirs, files in os.walk(dataset_folder):
    for file in files:
        print(os.path.join(root, file))

csv_path = "datasets/smart_meter_data.csv"

df = pd.read_csv(csv_path)

print("\n========== DATASET INFORMATION ==========")
print(df.info())

print("\n========== MINIMUM VALUES ==========")
print(df.select_dtypes(include="number").min())

print("\n========== MAXIMUM VALUES ==========")
print(df.select_dtypes(include="number").max())

print("\n========== FIRST FIVE RECORDS ==========")
print(df.head())

print("\n========== COMPLETED ==========")
