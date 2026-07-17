#!/usr/bin/python3
"""A command-line calculator supporting basic operations"""
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    operators = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = operators[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
