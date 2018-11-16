#!/usr/bin/env python3

"""
./kmeans hema_data.txt

Generate kmeans clustering map and extract genes following a similar expression pattern to gene of interest.
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans

d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)

kmeans = KMeans(n_clusters=6, random_state=0).fit_predict(df)

# If you print(kmeans) here, you see that each gene has been designated numbers representing the cluster they belong to.
# The most upregulated gene as determined by a separate analysis was in cluster 2, which is why I have kmean[2].
cluster = kmeans[2]
genes = df.index[kmeans == cluster]
similar_genes = genes.values.tolist()

# I pipe the output of print() into text files in this assignment.
print(similar_genes)

plt.figure()
plt.scatter(df["CFU"], df['poly'], c=kmeans, s=5, cmap='viridis')

# I plotted where the most upregulated gene is in the plot because can.
plt.scatter(0.145778143645, 5.79585004994, color = "red", s=5)
plt.title("k-means clustering")
plt.ylabel("poly expression")
plt.xlabel("CFU expression")
plt.savefig("kmeans.png")
plt.close()