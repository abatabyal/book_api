from datetime import datetime

def non_empty_string(s):
    """
    :param s: string coming with rest APIs in form of args, form or json
    :return: string is returned if not empty else ValueError is raised
    """
    if not s:
        raise ValueError("Must not be empty string")
    return s

def non_empty_integer(s):
    """
    :param s: integer coming with rest APIs in form of args, form or json
    :return: integer is returned if a > 0 else ValueError is raised
    """
    if int(s) <= 0:
        raise ValueError("Must not be empty integer")
    return s

def non_empty_list(s):
    """
    :param s: list coming with rest APIs in form of args, form or json
    :return: list is returned if not empty else ValueError is raised
    """
    if not s:
        raise ValueError("Must not be empty List")
    return s

def check_date_format(s):
    """
    :param s: date object coming with rest APIs in form of args, form or json
    :return: if date is not meet "%Y-%m-%d" format ValueError is raised
    """
    if not s:
        raise ValueError("Release Date Cannot be empty")
    try:
        datetime.strptime(s, "%Y-%m-%d")
    except:
        raise ValueError("Does not meet date format")
    return s