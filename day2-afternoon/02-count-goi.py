#!/usr/bin/env python3

# Print the unique gene names from a t_data.ctab file


import sys

genes_of_interest = set()
for line in open(sys.argv[1]):
    genes_of_interest.add(line.strip())

gene_name_counts = {}

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    gene_name = fields[9]
    if gene_name in genes_of_interest:
        if gene_name in gene_name_counts:
            gene_name_counts[gene_name] += 1
        else:
            gene_name_counts[gene_name] = 1

for name, value in gene_name_counts.items():
    print(name, value)
