import re
import tkinter.messagebox as msg



def name_validator(name, message):
    if isinstance(name, str) and re.match("^[آ-ی\s]{2,30}$", name):
        return name
    else:
        raise ValueError(message)


def nationalId_validator(nationalId, message):
    if re.match("^(\d{10}|\d{3}\-\d{6}\-\d)$", nationalId):
        # isinstance(nationalId, str) and
        return nationalId
    else:
        raise ValueError(message)



def date_birth_validator(date, message):
    if isinstance(date, str) and re.match("^([1][0-9][0-9][0-9])\.[0-1][0-9]\.(([0-2][0-9])|(30))$", date):
        return date
    else:
        raise ValueError(message)

def date_create_validator(date, message):
    if isinstance(date, str) :
        return date
    else:
        raise ValueError(message)



def number_extent_validator(number, message):
    if isinstance(number, str) :
        return number
    else:
        raise ValueError(message)
def number_validator(number, message):
    if isinstance(number, str) and re.match("^[0-12]$", number):
        return number
    else:
        raise ValueError(message)

def number_price_validator(number, message):
    if isinstance(number, str) and re.match("^[0-9]{4,13}$", number):
        return number
    else:
        raise ValueError(message)