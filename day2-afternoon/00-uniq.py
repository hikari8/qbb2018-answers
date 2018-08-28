#!/usr/bin/env python3

# Print the unique gene names from a t_data.ctab file


import sys

#gene_names_seen = []
# create a list for gene names seen
#gene_names_seen = {}
# dictionary to help this script run faster
gene_names_seen = set()


for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    gene_name = fields[9]
    if gene_name in gene_names_seen:
        continue
    else:
        #gene_names_seen.append(gene_name)
        #gene_names_seen[gene_name] = True
        gene_names_seen.add(gene_name)

for name in gene_names_seen:
    print(name)

# The code that looked at lists took some time (4.3s)
# Dictionary took an order of magnitude faster.
