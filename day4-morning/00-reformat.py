#!/usr/bin/env python3

"""
Usage: ./oo-reformat.py <ctab_file>

Convert ctab to bed format
-ctab : t_id chr strand end t_name ...
-bed : chr strand stop name strand score
"""

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1], sep = "\t")
    # Suggest use .(1)loc[] over[]
width = df.loc[:, "end"] - df.loc[:, "start"] + 1
df2 = df.assign(score = width)

coi = ["chr", "start", "end", "t_name", "strand", "score"]
    # coi = "columns of interest"
df2.loc[:, coi].to_csv(sys.stdout, sep = "\t", index = False)
    # row:column, no value gives all rows above
    # to_csv "comma separated value"
    # index = False suppresses index names(?)

#ctab_file = open(sys.argv[1])
#
#for i, line in enumerate(ctab_file):
#    if i == 0:
#        continue
#    fields = line.rstrip("\r\n").split("\t")
#    bed_order = [fields[1], fields[3], fields[4], fields[5], fields[2]]
#    print("\t".join(bed_order))
    