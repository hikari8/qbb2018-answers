#!/usr/bin/env python3

"""
Usage: ./day5-q2.py <samples.ctab>
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

for line in open(sys.argv[1]):
    if line.startswith("t"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    if fields[2] == "+":
        pmr_start = int(fields[3]) - 500
        if pmr_start < 0:
            pmr_start = 0
        end = fields[3]
        print(fields[1] + "\t" + str(pmr_start) + "\t" + str(end) + "\t" + fields[5])
    else:
        start = int(fields[4]) + 500
        end = fields[4]
        
        print(fields[1] + "\t" + str(end) + "\t" + str(start) + "\t" + fields[5])

# I flipped the start and the end