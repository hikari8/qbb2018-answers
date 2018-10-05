#!/usr/bin/env python3

"""
Usage: ./pca.py plink_eigenvector_output plink_eigenvalue_output
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

eigenvals = []

for line in open(sys.argv[2]):
    eigenvals.append(float(line.rstrip("\n")))

fig, ax = plt.subplots()

for line in open(sys.argv[1]):
    fields = line.split()
    x = np.multiply(eigenvals[0], float(fields[2]))
    y = np.multiply(eigenvals[1], float(fields[3]))
    plt.scatter(x, y, c = "red", alpha = 0.5)

plt.xlabel("Principle Component 1")
plt.ylabel("Principle Component 2")
plt.title("PCA")
plt.tight_layout()
fig.savefig("pca.plot.png")
plt.close(fig)

