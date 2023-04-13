#!/usr/bin/python3
"""A JSON representation function"""
import json


def to_json_string(my_obj):
    """This function returns the json representation of a object"""
    return json.dumps(my_obj)
