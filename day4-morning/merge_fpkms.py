#!/usr/bin/env python3

"""
Usage: /merge_fpkms.py <threshold> <ctab_file1> <ctab_file2> ... <ctab_filen>
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fpkms = {}

#name of input file
for i in range(2, len(sys.argv)):
    name = sys.argv[i].split(os.sep)[-2]
    #fpkm()
    fpkm = pd.read_csv(sys.argv[i], sep = "\t", index_col = "t_name").loc[:, "FPKM"]
    fpkms[name] = fpkm

fpkms_df = pd.DataFrame(fpkms)
fpkms_sum = pd.DataFrame.sum(fpkms_df, 1)
roi = fpkms_sum > float(sys.argv[1])

fpkms_df.loc[roi, :].to_csv(sys.stdout, sep = "\t", index = True)
