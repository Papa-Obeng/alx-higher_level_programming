#!/usr/bin/python3
"""This module checks whether an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Returns True if an object is an instance of the class
        otherwise, returns False
    """
    return (type(obj) == a_class)
