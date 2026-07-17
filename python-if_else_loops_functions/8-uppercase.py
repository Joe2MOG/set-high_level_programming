#!/usr/bin/python3
def uppercase(str):
    for c in str:
        offset = 32 if 97 <= ord(c) <= 122 else 0
        print("{:c}".format(ord(c) - offset), end="")
    print("")
