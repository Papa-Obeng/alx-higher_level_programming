#!/usr/bin/python3
"""A file-writing function"""


def write_file(filename="", text=""):
    """This function writes a string to a UTF8 text file and returns
        the number of characters in the string
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
