#!/usr/bin/env python3

import sys

count = 0
    
for i, line in enumerate(open(sys.argv[1])):
    if "#!" in line:
        continue
    fields = line.rstrip("\r\n").split("\t")
    gene_type = fields[2]
    if gene_type == "gene":
        string = fields[8].strip()
        if "gene_biotype" in string and '"protein_coding";' in string:
            count += 1

print(count)

# Output is "13917"