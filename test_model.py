import joblib

model = joblib.load("model.pkl")

print("Model loaded successfully!")
print(type(model))