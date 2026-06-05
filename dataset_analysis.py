import pandas as pd

data = pd.read_csv("dataset/data.csv")

print("Dataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns)

print("\nCategory Counts:")
print(data["type"].value_counts())