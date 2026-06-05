import pandas as pd

data = pd.read_csv("dataset/data.csv")

print(data[data["url"].str.contains("google", case=False, na=False)].head(20))