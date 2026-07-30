#!/usr/bin/python3
"""Module defining Student with reload_from_json."""


class Student:
    """A student that can update its attributes from a dictionary."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Replace all attributes with values from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
