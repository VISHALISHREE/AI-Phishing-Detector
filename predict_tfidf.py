import joblib

model = joblib.load("tfidf_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

url = input("Enter URL: ")

url_vector = vectorizer.transform([url])

print("Vector shape:", url_vector.shape)

prediction = model.predict(url_vector)

print("Prediction:", prediction[0])