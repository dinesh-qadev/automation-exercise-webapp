import random
import string


def generate_random_email(prefix="user", domain="test.com"):
    number = random.randint(1000, 9999)
    email_address= f"{prefix}{number}@{domain}"
    return email_address


#generate_random_email()