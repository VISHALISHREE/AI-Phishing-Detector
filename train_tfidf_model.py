import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load dataset
data = pd.read_csv("dataset/data.csv")

data = data.sample(
    n=100000,
    random_state=42
)

# Input URLs
X = data["url"]

# Labels
y = data["type"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(
    max_features=5000
)

# Convert URLs into vectors
X_train_tfidf = vectorizer.fit_transform(X_train)

X_test_tfidf = vectorizer.transform(X_test)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train_tfidf, y_train)

# Predictions
predictions = model.predict(X_test_tfidf)

# Accuracy
accuracy = model.score(X_test_tfidf, y_test)

print("Accuracy:", accuracy)

print("\nClassification Report:\n")

print(classification_report(y_test, predictions))

joblib.dump(model, "tfidf_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("TF-IDF model saved successfully!")