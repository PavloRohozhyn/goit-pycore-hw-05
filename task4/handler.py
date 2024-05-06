"""
module handler
"""
from validation import validation_name, validation_phone
from errors import error_args, error_item_exist, error_item_doesnt_exist, error_validation_name, error_validation_phone
from utils import print_with_color

def parse_input(user_input):
    """ parse input data """

    # get command and arguments
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts) -> str | Exception:
    """ add contact """

    try:
        name = args[0]
        phone = args[1]
    except IndexError as e:
        return error_args(e)
    # validation name
    if not validation_name(name):
        return error_validation_name(name)
    # check if name exists
    if name in contacts:
        return error_item_exist(name)
    # validation phone
    if not validation_phone(phone):
        return error_validation_phone(phone)
    # add contact
    contacts[name] = phone
    return "Contact added"


def change_contact(args, contacts) -> str | Exception:
    """ change contact """

    try:
        name = args[0]
        phone = args[1]
    except IndexError as e:
        return error_args(e)
    # validation name
    if not validation_name(name):
        return error_validation_name(name)
    # check if exists contact
    if not name in contacts:
        return error_item_doesnt_exist(name)
    # validation phone
    if not validation_phone(phone):
        return error_validation_phone(phone)
    # change contact    
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts) :
    """ show phone """

    try:
        name = args[0]
    except IndexError as e:
        return error_args(e)
    # validation name
    if not validation_name(name):
        return error_validation_name(name)
    # check if exists
    if not name in contacts:
        return error_item_doesnt_exist(name)
    return contacts[name]


def show_all(contacts):
    """ shoa all """

    contacts = {'foo': '1111', 'bar': '2222', 'tree': '3333'}

    for name, phone in contacts.items():
        print_with_color(f"{name}: {phone}", 'yellow')
    return True
