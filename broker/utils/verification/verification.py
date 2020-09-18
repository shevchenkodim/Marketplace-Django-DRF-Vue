import re


def clean_phone(phone):
    """ Clear in phone any symbol """
    return re.sub('[^0-9]', '', phone)


def check_phone(phone):
    """ Check valid phone """
    return re.match("380[0-9]{9}", phone)


def check_email(email):
    """ Check valid email """
    email_regex = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
    return email_regex.match(email)
