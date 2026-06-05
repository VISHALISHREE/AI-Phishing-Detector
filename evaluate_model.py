import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

from feature_extraction import *

# Load dataset
data = pd.read_csv("dataset/data.csv")

# Generate all features
data["url_length"] = data["url"].apply(url_length)
data["dot_count"] = data["url"].apply(count_dots)
data["has_hyphen"] = data["url"].apply(has_hyphen)
data["digit_count"] = data["url"].apply(digit_count)

data["has_https"] = data["url"].apply(has_https)
data["has_at_symbol"] = data["url"].apply(has_at_symbol)
data["slash_count"] = data["url"].apply(slash_count)
data["keyword_score"] = data["url"].apply(suspicious_keywords)

data["special_char_count"] = data["url"].apply(special_char_count)
data["subdomain_count"] = data["url"].apply(subdomain_count)
data["contains_ip"] = data["url"].apply(contains_ip)
data["suspicious_tld"] = data["url"].apply(suspicious_tld)

# Input features
X = data[
    [
        "url_length",
        "dot_count",
        "has_hyphen",
        "digit_count",
        "has_https",
        "has_at_symbol",
        "slash_count",
        "keyword_score",
        "special_char_count",
        "subdomain_count",
        "contains_ip",
        "suspicious_tld"
    ]
]

# Labels
y = data["type"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = model.score(X_test, y_test)

print("Accuracy:", accuracy)

# Detailed report
print("\nClassification Report:\n")
print(classification_report(y_test, predictions))