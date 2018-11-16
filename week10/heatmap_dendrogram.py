#!/usr/bin/env python3

"""
Usage: ./heatmap_dendrogram hema_data.txt
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)
df_array = np.array(df)

# I don't think I can reorder the columns in a manner that preserves the dendrogram with seaborn.
# I removed the Y-label because listing the genes for this plot didn't seem useful.

cmap = sns.diverging_palette(250, 15, sep=20, center='dark', as_cmap=True)
g = sns.clustermap(df, cmap=cmap, yticklabels=False)
g.savefig("heatmap_dendrogram.png")
plt.close()