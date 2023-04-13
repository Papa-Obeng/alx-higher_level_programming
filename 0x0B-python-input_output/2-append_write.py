#!/usr/bin/python3
"""A file-appending function"""


def append_write(filename="", text=""):
    """This function appends a string at the end of a UTF8 text file
        and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
