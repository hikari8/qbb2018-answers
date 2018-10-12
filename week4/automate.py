#!/usr/bin/env python3

"""
./automate.py
"""

import os

list_of_files = []

for file_name in os.listdir():
    if file_name.endswith(".qassoc"):
        list_of_files.append(file_name)

for i in range(len(list_of_files)):
    os.system("./manhattan_pandasway.py " + str(list_of_files[i]))