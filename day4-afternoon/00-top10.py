#!/usr/bin/env python3

"""
Usage: ./00-top10.py <ctab_file>
"""

import sys
import pandas as pd

df = pd.read_table(sys.argv[1])
df2 = df.sort_values("FPKM", ascending = False)

df2.iloc[0:10, :].to_csv(sys.stdout, sep = "\t", index = False)
# iloc = integer location