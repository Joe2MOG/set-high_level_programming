#!/usr/bin/python3
"""Prints the sum of all command-line arguments"""
from sys import argv

if __name__ == "__main__":
    total = 0
    for arg in argv[1:]:
        total += int(arg)
    print(total)
