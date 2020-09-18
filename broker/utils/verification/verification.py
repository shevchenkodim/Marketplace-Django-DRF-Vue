from typing import re


def clean_phone(phone):
    return re.sub('[^0-9]', '', phone)


def check_phone(phone):
    return re.match("380[0-9]{9}", phone)


def check_email(email):
    email_regex = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
    return email_regex.match(email)
