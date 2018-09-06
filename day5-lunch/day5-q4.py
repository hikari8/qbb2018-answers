#!/usr/bin/env python3

"""
Usage: ./day5-q4.py <histone_file1> <histone_file2> ... <histone_file4> <samples.ctab>
"""

import sys
import pandas as pd
import os
import statsmodels.formula.api as sm

means = {}

# histone = pd.read_table(sys.argv[1], index_col = 0).iloc[:, 4]

h3k4me1 = sys.argv[1].split(os.sep)[-1]
m1 = pd.read_csv(sys.argv[1], sep = "\t").iloc[:, 4]

h3k4me3 = sys.argv[2].split(os.sep)[-1]
m2 = pd.read_csv(sys.argv[2], sep = "\t").iloc[:, 4]

h3k9ac = sys.argv[3].split(os.sep)[-1]
m3 = pd.read_csv(sys.argv[3], sep = "\t").iloc[:, 4]

h3k27ac = sys.argv[4].split(os.sep)[-1]
m4 = pd.read_csv(sys.argv[4], sep = "\t").iloc[:, 4]

h3k27me3 = sys.argv[5].split(os.sep)[-1]
m5 = pd.read_csv(sys.argv[5], sep = "\t").iloc[:, 4]

fpkm_name = sys.argv[6].split(os.sep)[-1]
fpkm = pd.read_csv(sys.argv[6], sep = "\t").loc[:, "FPKM"]
print(fpkm_name)

means = {h3k4me1 : m1, h3k4me3 : m2, h3k9ac : m3, h3k27ac: m4, h3k27me3: m5, "fpkm": fpkm}
means_df = pd.DataFrame(means)
means_df.columns = ["h3k4me1", "h3k4me3", "h3k9ac", "h3k27ac", "h3k27me3", "fpkm"]

print(means_df.columns)

result = sm.ols(formula = 'fpkm ~ h3k4me1 + h3k4me3 + h3k9ac + h3k27ac + h3k27me3', data = means_df).fit()
print(result.summary())