#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)

kmeans = KMeans(n_clusters=5, random_state=0).fit_predict(df)

plt.figure()
plt.scatter(df["CFU"], df['poly'], c=kmeans, s=5, cmap='viridis')
plt.scatter(0.145778143645, 5.79585004994, color = "red", s=5)
plt.title("k-means_clustering")
plt.ylabel("poly expression")
plt.xlabel("CFU expression")
plt.savefig("kmeans.png")
plt.close()