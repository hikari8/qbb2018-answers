#!/usr/bin/env python3

"""
Usage: ./day5-q5.py <histone_file1> <histone_file2> ... <histone_file4> <samples.ctab>
"""

import sys
import os
import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt

means = {}

h3k4me1 = sys.argv[1].split(os.sep)[-1]
m1 = pd.read_table(sys.argv[1], sep = "\t").iloc[:, 4]
h3k4me3 = sys.argv[2].split(os.sep)[-1]
m2 = pd.read_table(sys.argv[2], sep = "\t").iloc[:, 4]
h3k9ac = sys.argv[3].split(os.sep)[-1]
m3 = pd.read_table(sys.argv[3], sep = "\t").iloc[:, 4]
h3k27ac = sys.argv[4].split(os.sep)[-1]
m4 = pd.read_table(sys.argv[4], sep = "\t").iloc[:, 4]
h3k27me3 = sys.argv[5].split(os.sep)[-1]
m5 = pd.read_table(sys.argv[5], sep = "\t").iloc[:, 4]

fpkm_name = sys.argv[6].split(os.sep)[-1]
fpkm = pd.read_csv(sys.argv[6], sep = "\t").loc[:, "FPKM"]

means = {h3k4me1 : m1, h3k4me3 : m2, h3k9ac : m3, h3k27ac: m4, h3k27me3: m5, "fpkm": fpkm}
means_df = pd.DataFrame(means)
means_df.columns = ["h3k4me1", "h3k4me3", "h3k9ac", "h3k27ac", "h3k27me3", "fpkm"]

result = sm.ols(formula = 'fpkm ~ h3k4me1 + h3k4me3 + h3k9ac + h3k27ac + h3k27me3', data = means_df).fit()

fig, ax = plt.subplots()
ax.hist(result.resid, bins=5000)
ax.set_title("Residuals of Model")
ax.set_xlabel("Residuals")
ax.set_ylabel("Frequency")
ax.set_xlim(left=-100, right=100)
fig.savefig("893_resid.png")
plt.close(fig)