"""
validation module
"""
import re


def validation_name(name: str):
    """
    name validation
    """
    return re.match(r'^[a-zA-Z]+$', name)


def validation_phone(phone: str):
    """
    phone validation
    """
    return re.match(r'^[0-9]+$', phone)
