#!/usr/bin/env python3

"""
Usage: ./allele_frequency.py
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

allele_frequency = []

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    else:
        fields = line.split()
        of_interest = float(fields[7].split("=")[1].split(",")[0])
        allele_frequency.append(of_interest)

allele_frequency.sort()

fig, ax = plt.subplots()
plt.hist(allele_frequency, bins = 1000)
plt.xlim(0, 1.1)
plt.xlabel("Allele Frequency")
plt.ylabel("Frequency")
plt.title("Allele Frequency Spectrum")
plt.tight_layout()
fig.savefig("allele_freq.png")
plt.close(fig)