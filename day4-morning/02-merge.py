#!/usr/bin/env python3

"""
Usage: ./02-merge.py <sample1/t_data.ctab> <sample2/t_data.ctab>

Create cav file with FPKMs from two samples
- assumes ctab_file in directory with same name
"""

import sys
import os
import pandas as pd

name1 = sys.argv[1].split(os.sep)[-2]
fpkm1 = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name").loc[:, "FPKM"]

name2 = sys.argv[2].split(os.sep)[-2]
fpkm2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = "t_name").loc[:, "FPKM"]

fpkms = {name1 : fpkm1, name2: fpkm2}
fpkms_df = pd.DataFrame(fpkms)

fpkms_df.to_csv(sys.stdout)