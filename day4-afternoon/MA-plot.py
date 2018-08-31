#!/usr/bin/env python3

"""
Usage: ./MA-plot.py <ctab file> <ctab file>
Creat an MA plot of FPKMs of two samples specified at the command line.
ex: ./MA-plot.py ~/data/results/stringtie/SRR072893/t_data.ctab ~/data/results/stringtie/SRR072915/t_data.ctab 
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name")
df2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = "t_name")
fpkm1 = df1.loc[:, "FPKM"]
fpkm2 = df2.loc[:, "FPKM"]

fpkm1_log = np.log(fpkm1 + 1)
fpkm2_log = np.log(fpkm2 + 1)

ratio = np.log2(fpkm1 + 1) - np.log2(fpkm2 + 1)
average = 0.5 * (np.log2(fpkm1 + 1) + np.log2(fpkm2 + 1))

fig, ax = plt.subplots()
ax.scatter(average, ratio, alpha = 0.3)

ax.set_xlabel("Average")
ax.set_ylabel("Ratio")

fig.savefig("ma-plot_893_915.png")
plt.close(fig)