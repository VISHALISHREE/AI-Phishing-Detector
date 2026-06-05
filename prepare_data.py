import pandas as pd

from feature_extraction import *

data = pd.read_csv("dataset/data.csv")

data["url_length"] = data["url"].apply(url_length)

data["dot_count"] = data["url"].apply(count_dots)

data["has_hyphen"] = data["url"].apply(has_hyphen)

data["digit_count"] = data["url"].apply(digit_count)

print(data.head())

data["has_https"] = data["url"].apply(has_https)

data["has_at_symbol"] = data["url"].apply(has_at_symbol)

data["slash_count"] = data["url"].apply(slash_count)

data["keyword_score"] = data["url"].apply(suspicious_keywords)