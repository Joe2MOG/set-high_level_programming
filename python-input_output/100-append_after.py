#!/usr/bin/python3
"""Module that inserts a line after lines containing a search string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line that contains search_string."""
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
