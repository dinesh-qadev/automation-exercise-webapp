import random
import string


def generate_random_email(prefix="user", domain="test.com"):
    number = random.randint(1000, 9999)
    print(f"{prefix}{number}@{domain}")
    return f"{prefix}{number}@{domain}"
