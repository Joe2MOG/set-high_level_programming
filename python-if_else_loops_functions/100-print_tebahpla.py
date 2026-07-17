#!/usr/bin/python3
for i in range(25, -1, -1):
    if i % 2 != 0:
        print("{:c}".format(97 + i), end="")
    else:
        print("{:c}".format(65 + i), end="")
