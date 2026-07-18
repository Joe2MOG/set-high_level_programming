#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in roman_string[::-1]:
        curr = values[ch]
        if curr >= prev:
            total += curr
        else:
            total -= curr
        prev = curr
    return total
