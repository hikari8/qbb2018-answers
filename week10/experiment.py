#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.mixture import GaussianMixture

d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)

clustering = GaussianMixture(n_components = 5).fit(df).predict(df)

plt.figure()
plt.scatter(df["CFU"], df['poly'], c=clustering, s=5, cmap='viridis')
plt.title("GaussianMixture_clustering")
plt.ylabel("poly expression")
plt.xlabel("CFU expression")
plt.savefig("GaussianMixture.png")
plt.close()