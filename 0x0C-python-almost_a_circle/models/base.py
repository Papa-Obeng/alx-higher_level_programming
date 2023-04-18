#!/usr/bin/python3


class Base:
    """A sample Base class defined"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class"""

        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
