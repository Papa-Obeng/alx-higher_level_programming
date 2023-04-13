#!/usr/bin/python3
"""A Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Sqaure class defined"""

    def __init__(self, size):
        """Initialize a new sqaure"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
