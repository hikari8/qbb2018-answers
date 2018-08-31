#!/usr/bin/env python3

"""
Usage: ./compile-1.py <gene_name> <samples.csv> <ctab_dir>
Create a single file all.csv containing all FPKMs
ex: ./compile-1.py ~/qbb2018/samples.csv ~/data/results/stringtie/
"""

import sys
import os
import pandas as pd

all_files = {}
df = pd.read_csv(sys.argv[1])
# df = df.loc[soi, :]

for index, sample, sex, stage in df.itertuples():
    filename = os.path.join(sys.argv[2], sample, "t_data.ctab")
    ctab_df = pd.read_table(filename, index_col = "t_name")
    
    all_files[sex + "_" + stage] = ctab_df.loc[:, "FPKM"]
    df_all_files = pd.DataFrame(all_files)

print(df_all_files)