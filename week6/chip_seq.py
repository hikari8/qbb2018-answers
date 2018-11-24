#!/usr/bin/env python3

"""
./chip_seq.py Mus_muculus.GRCm38.94_features.bed bedtools_output_overlap.bed bedtools_output_not_overlap.bed
"""

import sys
import matplotlib.pyplot as plt
import numpy as np

# Compile a dictionary that designates feature names (promoter, intron, exon) to each base pair position.
# Organize gained and lost peaks into features as described by the dictionary.
features_dictionary = {}
for line in open(sys.argv[1]):
    fields = line.rstrip("\r\n").split("\t")
    start = int(fields[1])
    end = int(fields[2])
    feature = fields[3]
    for base_pair_position in range(start,end):
        features_dictionary[base_pair_position] = feature

exon_gained = 0
intron_gained = 0
promoter_gained = 0
gained_peak = 0
for line in open(sys.argv[2]):
    fields = line.rstrip("\r\n").split("\t")
    gained_start = int(fields[1])
    gained_end = int(fields[2])
    gained_peak += 1
    gained_site = []
    for base_pair_position in range(gained_start, gained_end):
        if base_pair_position in features_dictionary:
            gained_feature = features_dictionary[base_pair_position]
            # Recall: output of features_dictionary[base_pair_position] is feature, this sets gained feature as feature.
            if gained_feature not in gained_site:
                gained_site.append(gained_feature)
                # Here, I'm trying to extract the number of sites as opposed to number of base pairs per line in file.
                # I'm also considering that CTCF bound sites may be occupying several features.
                if gained_feature == "exon":
                    exon_gained += 1
                elif gained_feature == "intron":
                    intron_gained += 1
                elif gained_feature == "promoter":
                    promoter_gained += 1
# print(exon_gained, intron_gained, promoter_gained)
# gives 88 239 31

exon_lost = 0
intron_lost = 0
promoter_lost = 0
lost_peak = 0
for line in open(sys.argv[3]):
    fields = line.rstrip("\r\n").split("\t")
    lost_start = int(fields[1])
    lost_end = int(fields[2])
    lost_peak += 1
    lost_site = []
    for base_pair_position in range(lost_start, lost_end):
        if base_pair_position in features_dictionary:
            lost_feature = features_dictionary[base_pair_position]
            if lost_feature not in lost_site:
                lost_site.append(lost_feature)
                if lost_feature == "exon":
                    exon_lost += 1
                elif lost_feature == "intron":
                    intron_lost += 1
                elif lost_feature == "promoter":
                    promoter_lost += 1
# print(exon_lost, intron_lost, promoter_lost)
# gives 7 28 1

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20,5))

ax1.bar(np.arange(3), [exon_gained, intron_gained, promoter_gained], width=0.3, color="orange", label="CTCF sites gained in ER4 cells")
ax1.bar(np.arange(3), [exon_lost, intron_lost, promoter_lost], width=0.3, color="cyan", label="CTCF sites lost in ER4 cells")
ax1.set_xticks(np.arange(3))
ax1.set_xticklabels(['exons', 'introns', 'promoters'])
ax1.set_ylabel("Number of CTCF binding sites")
ax1.set_title("Number of CTCF binding sites by feature in ER4 cells")
ax1.legend()

ax2.bar(0, gained_peak, width=0.3, color="orange", align="center", label="CTCF sites gained in ER4 cells")
ax2.bar(1, lost_peak, width=0.3, color="cyan", align="center", label="CTCF sites lost in ER4 cells")
ax2.set_xticks(np.arange(2))
ax2.set_xticklabels(['gained', 'lost'])
ax2.set_ylabel("Number of CTCF binding sites")
ax2.set_title("CTCF binding sites differentiation in ER4 cells")
ax2.legend(loc='upper right')

fig.savefig("chip_seq_plot.png")
plt.close(fig)