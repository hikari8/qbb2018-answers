#!/usr/bin/env python3

"""
Usage: ./02-boxplot.py <gene_name> <sample.tsv> <ctab_dir>

Create a boxplot for a given gene in each sample
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[2])
fpkms = []

for index, sample, sex, stage in df.itertuples():
    # "sample, sex, stage" shown when at ~/qbb2018/samples.csv in command line
    filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
    ctab_df = pd.read_table(filename, index_col = "t_name")
    
    roi = ctab_df.loc[:,"gene_name"] == sys.argv[1]
    fpkms.append(ctab_df.loc[roi, "FPKM"])

fig, ax = plt.subplots()
ax.boxplot(fpkms)
fig.savefig("boxplot.png")
plt.close(fig)