#!/usr/bin/env python3

"""
Usage: ./01-merge.py <ctab_file1> <ctab_file2>
"""

import sys
import pandas as pd

ctab1 = pd.read_table(sys.argv[1], index_col = "t_name").loc[:, "FPKM"]
ctab2 = pd.read_table(sys.argv[2], index_col = "t_name").loc[:, "FPKM"]

d = { 'first' : ctab1, 'second' : ctab2}

df = pd.DataFrame(d)

df.to_csv(sys.stdout)