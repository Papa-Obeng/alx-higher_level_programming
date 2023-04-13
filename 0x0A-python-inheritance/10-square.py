#!/usr/bin/python3
"""A Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Sqaure using Rectangle"""

    def __init__(self, size):
        """Initializes a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
