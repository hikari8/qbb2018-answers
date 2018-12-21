#!/usr/bin/env python

import sys
import os
import hifive
import numpy

# open(sys.argv[1])
# hic = hifive.HiC('week13.hcp')
#
# data = hic.cis_heatmap(chrom='chr17', start=15000000, stop=17500000, binsize=10000, datatype='fend', arraytype='full')
# print(data)

list_of_midpoints = []
for line in open(sys.argv[1]):
    if line.startswith("chr17"):
        fields = line.rstrip("\r\n").split("\t")
        start = int(fields[1])
        end = int(fields[2])
        if start >= 15000000 and end <=17500000:
            midpoint = ((end - start)/2) + start
            list_of_midpoints.append(midpoint)
# print(list_of_midpoints, len(list_of_midpoints))

ctcf_point_list =[]
for value in list_of_midpoints:
    ctcf_point = ((value - 15000000)/10000)
    ctcf_point_list.append(ctcf_point)

unique_ctcf_bin = numpy.unique(ctcf_point_list)

hic = hifive.HiC('week13.hcp')
data = hic.cis_heatmap(chrom='chr17', start=15000000, stop=17500000, binsize=10000, datatype='fend', arraytype='full')
data[:, :, 1] *= numpy.sum(data[:, :, 0]) / numpy.sum(data[:, :, 1])
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = data[:, :, 0]

enriched_bin = []
for i in range(len(unique_ctcf_bin)):
    for j in range(i, len(unique_ctcf_bin)):
        if data[unique_ctcf_bin[i], unique_ctcf_bin[j]] > 1:
            enriched_bin.append((unique_ctcf_bin[i], unique_ctcf_bin[j], data[unique_ctcf_bin[i], unique_ctcf_bin[j]]))

genomic_enriched_bin = []
for row, column, value in enriched_bin:
    genomic_row = (row*10000) + 15000000
    genomic_column = (column*10000) + 15000000
    genomic_enriched_bin.append((genomic_row, genomic_column, value))

sorted_genomic_enriched_bin = sorted(genomic_enriched_bin, key = lambda t:t[2], reverse=True)
# print(sorted_genomic_enriched_bin)

for row, column, value in sorted_genomic_enriched_bin:
    print(str(row) + "\t" + str(column) + "\t" + str(value))