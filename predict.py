import joblib

from feature_extraction import *

model = joblib.load("model.pkl")

url = input("Enter URL: ")

features = [[
    url_length(url),
    count_dots(url),
    has_hyphen(url),
    digit_count(url),
    has_https(url),
    has_at_symbol(url),
    slash_count(url),
    suspicious_keywords(url)
]]

print("Features:", features)

prediction = model.predict(features)

print("Prediction:", prediction[0])