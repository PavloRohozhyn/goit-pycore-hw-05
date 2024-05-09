"""
module handler
"""

from validation import input_error, validation_for_add_function, \
    validation_for_change_function, validation_for_show_function
from utils import print_with_color

@input_error
def parse_input(user_input):
    """ parse input data """

    # get command and arguments
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@validation_for_add_function
def add_contact(args, contacts) -> str | Exception:
    """ add contact """

    name, phone = args
    # add contact
    contacts[name] = phone
    return "Contact added"

@validation_for_change_function
def change_contact(args, contacts) -> str | Exception:
    """ change contact """

    name, phone = args
    contacts[name] = phone
    return "Contact updated."


@validation_for_show_function
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
