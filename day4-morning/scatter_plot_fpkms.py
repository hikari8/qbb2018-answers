#!/usr/bin/env python3

"""
Usage: /scatter_plot.py <ctab_file1> <ctab_file2>
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fpkm1 = pd.read_csv(sys.argv[1], sep = "\t").loc[:, "FPKM"]
fpkm2 = pd.read_csv(sys.argv[2], sep = "\t").loc[:, "FPKM"]
name1 = sys.argv[1].split(os.sep)[-2]
name2 = sys.argv[2].split(os.sep)[-2]

# log scale original data
fpkm1_log = np.log(fpkm1 + 1)
fpkm2_log = np.log(fpkm2 + 1)

# Trying to plot a fit
poly = np.polyfit(fpkm1, fpkm2, deg = 1)
x = np.linspace(min(fpkm1_log), max(fpkm1_log))
y = np.poly1d(np.polyfit(fpkm1, fpkm2, 1))

# Scaling the graph
fig, ax = plt.subplots()
ax.scatter(fpkm1_log, fpkm2_log, alpha = 0.3)
plt.plot(x, y(x), "r")

# Set axes limits
axes = plt.gca()
axes.set_xlim([0.01,10])
axes.set_ylim([0.01,10])

# Label names
ax.set_xlabel("log FPKM Value of %s" %name1)
ax.set_ylabel("log FPKM Value %s" %name2)
ax.set_title("Comparison of FPKM Values: %s vs %s" %(name1, name2))
ax.text(7, 1, "best fit line: " + str(y))
fig.savefig("fpkmplot.png")
plt.close(fig)