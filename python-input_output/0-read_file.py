#!/usr/bin/python3
"""Module that defines read_file."""


def read_file(filename=""):
    """Read a text file and print its contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
