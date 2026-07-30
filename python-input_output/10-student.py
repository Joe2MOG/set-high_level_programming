#!/usr/bin/python3
"""Module defining Student class with filtered to_json."""


class Student:
    """A student class that supports attribute filtering."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary, optionally filtering by attribute names."""
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}
