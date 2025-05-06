import re


def clean_text(text):
    return re.sub(r'[^a-z]', '', text.lower())


def extract_digits(text):
    return int(re.sub(r"[^\d]", "", text))
