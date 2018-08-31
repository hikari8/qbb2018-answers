#!/usr/bin/env python3

"""
Usage: 
Create a plot for FBtr0331261 abundance, comparing male and female at each developmental stages.   
ex: ./for_males.py FBtr0331261 ~/qbb2018/samples.csv ~/data/results/stringtie/
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def timecourse(sex):
    df = pd.read_csv(sys.argv[2])
    soi = df.loc[:, "sex"] == sex
    df = df.loc[soi, :]
    fpkms = []
    stages = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col = "t_name")
        fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        stages.append(stage)
    return fpkms, stages
    
fpkms_f, stages = timecourse("female")
fpkms_m, stages = timecourse("male")

fig, ax = plt.subplots()
ax.plot(fpkms_f, "r", label = "female")
ax.plot(fpkms_m, "b", label = "male")
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance (RPKM)")
ax.set_title("Sxl")
ax.set_xticklabels(stages, rotation = 90)
plt.legend(bbox_to_anchor = (1.0, 0.5), loc = 2, borderaxespad = 0)
plt.tight_layout()
fig.savefig("timecourse.png", bbox_inches = "tight")
plt.close(fig)

# fpkms_f = timecourse("female")
# fpkms_m = timecourse("male")
# fig, ax = plt.subplots()
# ax.plot(fpkms_f, "r", label = "female")
# ax.plot(fpkms_m, "b", label = "male")
# ax.set_xlabel("developmental stage")
# ax.set_ylabel("mRNA abundance (RPKM)")
# ax.set_title("Sxl")
# plt.xticks(np.arange(8), ('10', '11', '12', '13', '14a', '14b', '14c', '14d'))
# plt.xticks(rotation = 90)
# plt.tight_layout()
# box = ax.get_position()
# ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
# ax.legend(loc = "center left", bbox_to_anchor=(1, 0.5), frameon = False)
# fig.savefig("timecourse.png")
# plt.close(fig)