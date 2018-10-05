#!/usr/bin/env python3

"""
Usage: ./plot.py freebayes_output summary.txt

"""

import sys
import matplotlib.pyplot as plt
import numpy as np

position = 0

read_depth = []
genotype_quality = []
allele_frequency = []
variant = []

# from generated vcf file

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    else:
        fields = line.split("\t")
        genotype_quality.append(float(fields[5]))
        for id_val in fields[7].split(";"):
            id, val = id_val.split("=")
            if id == "DP":
                read_depth.append(float(val.split(",")[0]))
            if id == "AF":
                allele_frequency.append(float(val.split(",")[0]))

# from summary.txt

# effects = []
# percentages = []
#
# for line in open(sys.argv[2]):
#     effects.append(line.split()[0])
#     percentages.append(float(line.split()[2]))

percentages = [42.313, 10.568, 3.972, 0.082, 0.0, 0.0, 0.011, 43.053]
effects = ["Downstream", "Exon", "Intergenic", "Intron", "Acceptor",
             "Donor", "Splice Site", "Upstream"]
    
# finally, to plotting

fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (20, 12))
axes = axes.flatten()

# for read depth
axes[0].hist(read_depth, color = "blue", bins = 100)
axes[0].set_yscale("log")
axes[0].set_xlabel("Read Depth")
axes[0].set_ylabel("Count")
axes[0].set_title("Read depth distribution")

# for genotype quality distribution
axes[1].hist(genotype_quality, color = "green", bins = 500)
axes[1].set_yscale("log")
axes[1].set_xlabel("Genotype Quality")
axes[1].set_ylabel("Count")
axes[1].set_title("Genotype quality distribution")

# for allele frequency spectrum
axes[2].hist(allele_frequency, color = "red", bins = 50)
axes[2].set_xlabel("Allele frequency")
axes[2].set_ylabel("Count")
axes[2].set_title("Allele frequency distribution")

# for variant effect
axes[3].bar(np.arange(8), percentages, color = "orange")
axes[3].set_xticklabels(effects)
axes[3].set_xlabel("Type of variant")
axes[3].set_ylabel("Frequency (%)")
axes[3].set_title("Predicted effects of each variant")

fig.savefig("alltheplots_filtered.png")
plt.close(fig)