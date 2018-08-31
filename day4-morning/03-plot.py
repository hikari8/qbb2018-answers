#!/usr/bin/env python3

"""
Usage: ./03-plot.py <ctab_file>
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name")

gene_lengths = df.loc[:, "length"]
print( "Mean gene length: {0}".format(np.mean(gene_lengths)))
    #{0} means "0th argument"
gene_exons = df.loc[:, "num_exons"]
length_vs_exons = np.corrcoef(gene_lengths, gene_exons)[0, 1]
    # why did adding [0,1] make it not a 2 * 2 matrix??
print(type(length_vs_exons))
print("Pearson's r: {0:0.4f}".format(length_vs_exons))

#fig, ax = plt.subplots()
#ax.scatter(gene_lengths, gene_exons)
#fig.savefig("scatter.png")
#plt.close(fig)

fig, (ax1, ax2) = plt.subplots(2)
ax1.hist(gene_lengths)
ax2.hist(gene_exons)
fig.savefig("scatter_2.png")
plt.close(fig)