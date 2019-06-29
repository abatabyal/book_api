from datetime import datetime

def non_empty_string(s):
    if not s:
        raise ValueError("Must not be empty string")
    return s

def non_empty_integer(s):
    if int(s) <= 0:
        raise ValueError("Must not be empty integer")
    return s

def non_empty_list(s):
    if not s:
        raise ValueError("Must not be empty List")
    return s

def check_date_format(s):
    if not s:
        raise ValueError("Release Date Cannot be empty")
    try:
        datetime.strptime(s, "%Y-%m-%d")
    except:
        raise ValueError("Does not meet date format")
    return s