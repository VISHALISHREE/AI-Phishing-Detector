from feature_extraction import *

url = "paypal-login-security123.xyz"

print("Length:", url_length(url))
print("Dots:", count_dots(url))
print("Hyphen:", has_hyphen(url))
print("Digits:", digit_count(url))