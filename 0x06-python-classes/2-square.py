#!/usr/bin/python3


class Square:
    """This class represents a sqaure"""

    def __init__(self, size=0):
        """Args: size represents the size of the square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
