#!/usr/bin/python3
'''module'''

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

try:
    data = load_from_json_file("add_item.json")
    if not isinstance(data, list):
        raise TypeError("Data loaded from JSON is not a list")
except FileNotFoundError:
    data = []

data.extend(sys.argv[1:])
save_to_json_file(data, "add_item.json")

