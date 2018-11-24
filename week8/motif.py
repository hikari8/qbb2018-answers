#!/usr/bin/env python3

"""
Usage: ./motif.py bedtools_intersect_output.bed
"""

import sys
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

motif_position = []
for line in open(sys.argv[1]):
    fields = line.rstrip("\r\n").split("\t")
    motif_start = int(fields[3])
    motif_end = int(fields[4])
    peak_start = int(fields[10])
    peak_end = int(fields[11])
    peak_length = (peak_end - peak_start) + 1
    start = motif_start - peak_start
    end = peak_end - motif_end
    relative_position = start/peak_length
    motif_position.append(relative_position)

fig, ax = plt.subplots()
plt.hist(motif_position, color = "skyblue", bins=50)
plt.xlabel('Position of Motif Frequency Relative to Peak')
plt.ylabel('Frequency')
plt.title( 'Density Plot of Motif Matches' )
plt.savefig('density_plot.png')
plt.close()