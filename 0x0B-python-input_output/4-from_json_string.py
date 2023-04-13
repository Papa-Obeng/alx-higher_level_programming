#!/usr/bin/python3
"""An object returning function"""
import json


def from_json_string(my_str):
    """This function returns an object represented by a json string"""
    return json.loads(my_str)
