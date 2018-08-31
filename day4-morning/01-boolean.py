#!/usr/bin/env python3

"""
Usage: ./01-boolean.py <ctab_file> <FPKM> <chr>

Filter genes based on minimum FPKM and chr
"""

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1], sep = "\t")

roi_fpkm = df.loc[:, "FPKM"] > float(sys.argv[2])
roi_chr = df.loc[:, "chr"] == sys.argv[3]

roi = roi_fpkm & roi_chr
df.loc[roi, :].to_csv(sys.stdout, sep = "\t", index = False)