#!/usr/bin/env python3

"""
Usage: ./generalized.py <gene_name> <samples.csv> <ctab_dir>
Create a plot for genes of interest.
ex: ./generalized.py Sxl ~/qbb2018/samples.csv ~/data/results/stringtie/
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def timecourse(sample, sex, gene):
    df = pd.read_csv(sample)
    soi = df.loc[:, "sex"] == sex
    df = df.loc[soi, :]
    fpkms_avg = []
    stages = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col = "t_name")
        roi = ctab_df.loc[:, "gene_name"] == gene
        fpkms = ctab_df.loc[roi, "FPKM"]
        fpkms_avg.append(np.mean(fpkms))
        stages.append(stage)
    return fpkms_avg, stages

fpkms_f, stages = timecourse(sys.argv[2], "female", sys.argv[1])
fpkms_m, stages = timecourse(sys.argv[2], "male", sys.argv[1])

fig, ax = plt.subplots()
ax.plot(fpkms_f, "r", label = "female")
ax.plot(fpkms_m, "b", label = "male")
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance (RPKM)")
ax.set_title(sys.argv[1])
ax.set_xticklabels(stages, rotation = 90)
plt.legend(bbox_to_anchor = (1.0, 0.5), loc = 2, borderaxespad = 0)
plt.tight_layout()
fig.savefig("timecourse_gen.png", bbox_inches = "tight")
plt.close(fig)