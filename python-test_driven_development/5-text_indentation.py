#!/usr/bin/python3
"""Formats text with double newlines after punctuation."""


def text_indentation(text):
    """Print text with 2 newlines after each '.', '?', and ':'.

    No spaces at the beginning or end of each printed line.

    Args:
        text: a string.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for ch in text:
        line += ch
        if ch in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
