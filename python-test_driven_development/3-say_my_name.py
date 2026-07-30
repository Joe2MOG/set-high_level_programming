#!/usr/bin/python3
"""Prints a name in the format 'My name is <first> <last>'."""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first_name> <last_name>'.

    Args:
        first_name: a string.
        last_name: a string, defaults to "".

    Raises:
        TypeError: if first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
