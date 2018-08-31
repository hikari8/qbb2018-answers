#!/usr/bin/env python3

"""
Usage: ./third-q.py <gene_name> <samples.csv> <ctab_dir>
Create a plot for all the genes of interest (separated by commas in the command line)
ex: ./third-q.py Szl,... ~/qbb2018/samples.csv ~/data/results/stringtie/
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("Hello")

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

for gene in sys.argv[1].split(','):
    fpkms_f, stages = timecourse(sys.argv[2], "female", gene)
    fpkms_m, stages = timecourse(sys.argv[2], "male", gene)
    
    fig, ax = plt.subplots()
    ax.plot(fpkms_f, "r", label = "female")
    ax.plot(fpkms_m, "b", label = "male")
    ax.set_xlabel("developmental stage")
    ax.set_ylabel("mRNA abundance (RPKM)")
    ax.set_title(gene)
    ax.set_xticklabels(stages, rotation = 90)
    plt.legend(bbox_to_anchor = (1.0, 0.5), loc = 2, borderaxespad = 0)
    plt.tight_layout()
    fig.savefig("timecourse%s.png" % (str(gene)) , bbox_inches = "tight")
    plt.close(fig)