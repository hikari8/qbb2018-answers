#!/usr/bin/env python3

import sys

uniq_gene_type = {}
#count = 0

for i, line in enumerate(open(sys.argv[1])):
    if "#!" in line:
        continue
    fields = line.rstrip("\r\n").split("\t")
    gene_type = fields[2]
    if gene_type != "gene":
        continue
    string = fields[8].strip()
    if "gene_biotype" in string:
        biotype_index = string.index("gene_biotype")
        next_index = biotype_index + 14
        biotype_plus = string[next_index:next_index+40]
        bio_fields = biotype_plus.split('"')
        biotype = bio_fields[0]
        if biotype not in uniq_gene_type:
            uniq_gene_type[biotype] = 1
        else:
            uniq_gene_type[biotype] += 1

print(uniq_gene_type)

# Output is {'pseudogene': 257, 'protein_coding': 13917, 'lincRNA': 2366, 'pre_miRNA': 238, 'snRNA': 31, 'tRNA': 314, 'snoRNA': 288, 'rRNA': 147}