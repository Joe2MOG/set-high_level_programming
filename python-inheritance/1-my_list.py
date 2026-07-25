#!/usr/bin/python3
"""Module defining MyList that inherits from list."""


class MyList(list):
    """Custom list with a print_sorted method."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
