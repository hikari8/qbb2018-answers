#!/usr/bin/env python3

import sys

dist_to_mutation = {}
my_dist = 0
find_pos = 21378950

for i, line in enumerate(open(sys.argv[1])):
    if "#!" in line:
        continue
    fields = line.rstrip("\r\n").split("\t")
    gene_type = fields[2]
    chromosome = fields[0]
    if gene_type != "gene":
        continue
    if chromosome != "3R":
        continue
    if '"protein_coding"' in line:
        continue
    gene_start = int(fields[3])
    gene_end = int(fields[4])        
    if find_pos < gene_start:
        my_dist = gene_start - find_pos
    elif find_pos > gene_end:
        my_dist = find_pos - gene_end
    string = fields[8].strip()
    if "gene_id" in string:
        biotype_index = string.index("gene_id")
        next_index = biotype_index + 9
        biotype_plus = string[next_index:next_index+40]
        bio_fields = biotype_plus.split('"')
        biotype = bio_fields[0]
    dist_to_mutation.update({biotype:my_dist})
    
var = (min(dist_to_mutation, key = dist_to_mutation.get))
print(var, dist_to_mutation[var])

# Output is "FBgn0267713 22704"