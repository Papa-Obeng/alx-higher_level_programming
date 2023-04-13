#!/usr/bin/python3
"""A function that creates an Object from Json file"""
import json


def load_from_json_file(filename):
    """This function creates an object from json file"""
    with open(filename) as f:
        return json.load(f)
