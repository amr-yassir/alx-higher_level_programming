#!/usr/bin/python3
'''module'''


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


arg_list = list(sys.argv[1:])

try:
    data = load_from_json_file('add_item.json')
except Exception:
    data = []

data.extend(arg_list)
save_to_json_file(data, 'add_item.json')
