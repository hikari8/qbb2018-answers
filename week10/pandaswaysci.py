#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sci
import seaborn as sns


cols = ['CFU', 'poly', 'unk', 'int', 'mys', 'mid']
data = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data)
df_array = np.array(df)

fig, axes = plt.subplots(nrows = 2)
axes[0] = sns.heatmap(df_array)
axes[1] = sns.clustermap(df_array, metric='euclidean', standard_scale=1, method='ward', cmap='Blues')
fig.tight_layout()
plt.show()
plt.close(fig)
