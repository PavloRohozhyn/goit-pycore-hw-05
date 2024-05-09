""" validation module """
import re


def input_error(func):
    """ decorator - validation arguments structure """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return ["Give me name and phone please."]

    return inner


def validation_for_add_function(func):
    """ 
    decorator - validation params for "add" function
     - contact_name
     - phone_number
     - contact_name exists
     - phone_number exists 
    """

    def wrapper(*args, **kwargs):
        """ handle params """

        try:
            # str, str <- list <- tuple
            name, phone = data = args[0]

            # check first value - name
            if not validation_contact_name(name):
                raise ValueError('Invalid contact_name was passed')
            # check second value - phone
            elif not validation_phone_number(phone):
                raise ValueError('Invalid phone_number was passed')
            else:
                pass

            return func(*args, **kwargs)
        except ValueError as e:
            return f'Give me contact_name and phone_number please ({e})'
        except TypeError:
            return 'Please enter "contact_name" and "phone_number"'

    return wrapper


def validation_for_change_function(func):
    """ 
    decorator - validation params for "change" function
     - contact_name
     - phone_number
     - contact_name exists
     - phone_number exists 
    """

    def wrapper(*args, **kwargs):
        """ handle params """

        try:
            # str, str <- list <- tuple
            name, phone = data = args[0]

            # check first value - name
            if not validation_contact_name(name):
                raise ValueError('Invalid contact_name was passed')
            # check second value - phone
            elif not validation_phone_number(phone):
                raise ValueError('Invalid phone_number was passed')
            else:
                pass

            return func(*args, **kwargs)
        except ValueError as e:
            return f'Give me contact_name and phone_number please ({e})'
        except TypeError:
            return 'Please enter "contact_name" and "phone_number"'

    return wrapper


def validation_for_show_function(func):
    """ 
    decorator - validation params for "show" function 
     - phone_number
     - contact_name doesnt exists
    """

    def wrapper(*args, **kwargs):
        """ handle params """
        try:
            # str, str <- list <- tuple
            name = data = args[0]

            # check contact name
            if not check_contact_name(name):
                raise ValueError('Invalid phone_number was passed')
            else:
                pass

            return func(*args, **kwargs)
        except ValueError as e:
            return f'Give me contact_name and phone_number please ({e})'
        except TypeError:
            return 'Please enter "contact_name" and "phone_number"'

    return wrapper


def check_contact_name(name: str) -> bool:
    """ validation contact_name """

    if re.match(r'^[a-zA-Z]+$', name):
        return True
    else:
        return False


def check_phone_number(phone: str) -> bool:
    """ validation phone_number """

    if re.match(r'^[0-9]+$', phone):
        return True
    else:
        return False


def check_contact_name_exists(name: str, contacts: list) -> bool:
    pass


def check_contact_name_doesnt_exists(name: str, contacts: list) -> bool:
    pass


def check_phone_number_exists(phone: str, contacts: list) -> bool:
    pass

def check_phone_number_doesnt_exists(phone: str, contacts: list) -> bool:
    pass