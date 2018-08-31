#!/usr/bin/env python3

"""
Usage: ./02-boxplot.py <t_name> <sample.tsv> <ctab_dir>

Create a timecourse of a given transcript (FBtr0331261) for females
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[2])
soi = df.loc[:, "sex"] == "female"
df = df.loc[soi, :]

fpkms = []

for index, sample, sex, stage in df.itertuples():
    # "sample, sex, stage" shown when at ~/qbb2018/samples.csv in command line
    filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
    ctab_df = pd.read_table(filename, index_col = "t_name")
    fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
    # roi = ctab_df.loc[:,"gene_name"] == sys.argv[1]
#     fpkms.append(ctab_df.loc[roi, "FPKM"])

fig, ax = plt.subplots()
ax.plot(fpkms)
fig.savefig("timecourse.png")
plt.close(fig)