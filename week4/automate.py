#!/usr/bin/env python3

"""
./automate.py

For every .qassoc(quantitative trait association test report) in the same directory,
this python script will generate a Manhattan plot.

"""

import os

list_of_files = []

for file_name in os.listdir():
    if file_name.endswith(".qassoc"):
        list_of_files.append(file_name)

# Somehow just coding "list_of_files" is not good enough because
# python wants integers not strings or whatever so I added the range(len())
for i in range(len(list_of_files)):
    os.system("./manhattan_pandasway.py " + str(list_of_files[i]))