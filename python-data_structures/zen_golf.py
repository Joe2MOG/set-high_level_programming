#!/usr/bin/python3
"""Zen Golf: verbose vs Pythonic refactoring exercise."""


# Function 1: Sum of even numbers
def sum_even_verbose(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total = total + num
    return total


def sum_even_pythonic(numbers):
    """Calculates the sum of all even numbers in a sequence."""
    return sum(num for num in numbers if num % 2 == 0)


# Function 2: Find the longest word
def longest_word_verbose(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def longest_word_pythonic(words):
    return max(words, key=len, default="")


# Function 3: Filter positive numbers
def filter_positive_verbose(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result


def filter_positive_pythonic(numbers):
    """Returns positive numbers only, filtered from the input list."""
    return [num for num in numbers if num > 0]


if __name__ == "__main__":
    print(sum_even_verbose([1, 2, 3, 4, 5, 6]))
    print(sum_even_pythonic([1, 2, 3, 4, 5, 6]))
    print(longest_word_verbose(["cat", "elephant", "dog", "whale"]))
    print(longest_word_pythonic(["cat", "elephant", "dog", "whale"]))
    print(filter_positive_verbose([-3, -1, 0, 2, 5, -7]))
    print(filter_positive_pythonic([-3, -1, 0, 2, 5, -7]))
