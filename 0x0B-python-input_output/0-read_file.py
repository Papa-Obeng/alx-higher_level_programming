#!/usr/bin/python3
"""A text-file reading function"""


def read_file(filename=""):
    """this function prints the content of UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
