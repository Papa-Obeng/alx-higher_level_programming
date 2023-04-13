#!/usr/bin/python3
"""Defines a function that returns a dictionary description of an object"""


def class_to_json(obj):
    """This function returns the dictionary description of an object"""
    return obj.__dict__
