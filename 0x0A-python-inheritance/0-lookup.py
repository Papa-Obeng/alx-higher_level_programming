#!/usr/bin/python3
"""
    This module returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """The lookup function looks out for all attributes and methods of an
        object
    """
    return dir(obj)
