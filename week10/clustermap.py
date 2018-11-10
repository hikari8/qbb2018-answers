#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sci
import seaborn as sns

d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)
df_array = np.array(df)

# 220 and 20 represent color
cmap = sns.diverging_palette(220, 20, sep=20, as_cmap=True)

ax = sns.clustermap(df, cmap=cmap)
plt.show()
ax.savefig("heatmap.png")
plt.close(ax)