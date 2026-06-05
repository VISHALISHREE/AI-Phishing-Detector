import re


def url_length(url):
    return len(url)


def count_dots(url):
    return url.count(".")


def has_hyphen(url):
    return 1 if "-" in url else 0


def digit_count(url):
    return sum(char.isdigit() for char in url)


def has_https(url):
    return 1 if "https" in url.lower() else 0


def has_at_symbol(url):
    return 1 if "@" in url else 0


def slash_count(url):
    return url.count("/")


def suspicious_keywords(url):
    keywords = [
        "login",
        "verify",
        "account",
        "secure",
        "update",
        "bank",
        "signin"
    ]

    url = url.lower()

    return sum(keyword in url for keyword in keywords)


def special_char_count(url):
    special_chars = "-_@?=&%"

    return sum(
        1 for char in url
        if char in special_chars
    )


def subdomain_count(url):
    return max(0, url.count(".") - 1)


def contains_ip(url):
    pattern = r"\d+\.\d+\.\d+\.\d+"

    return 1 if re.search(pattern, url) else 0


def suspicious_tld(url):
    suspicious = [
        ".xyz",
        ".top",
        ".club",
        ".online",
        ".site",
        ".tk",
        ".ml"
    ]

    url = url.lower()

    return 1 if any(
        tld in url
        for tld in suspicious
    ) else 0