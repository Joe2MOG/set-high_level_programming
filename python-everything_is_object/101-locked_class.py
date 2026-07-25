#!/usr/bin/python3
"""Module that provides a LockedClass with restricted attributes."""


class LockedClass:
    """A class that only allows the 'first_name' attribute."""
    __slots__ = ("first_name",)
