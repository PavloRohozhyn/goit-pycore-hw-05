"""
module errors
"""

def error_args(e):
    """ when command doesn't have enough arguments """

    return f"Error: maybe, you forgot to pass arguments into command ({e})"


def error_item_exist(name):
    """ when item exists into contact list """

    return f"Name ({name}) already exists, use (change) command to edit data"


def error_item_doesnt_exist(name):
    """ when item doesnt exists into contact list """

    return f'Name {name} doesnt exists in contact list, use (add) command to add contact into contact list'


def error_validation_name(name):
    """ validation contact name """

    return f'Invalid contact name ({name}) was passed'


def error_validation_phone(phone):
    """ validation contact phone """

    return f'Invalid phone numer ({phone}) was passed'
