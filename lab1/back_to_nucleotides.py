#!/usr/bin/env python3

"""
Usage: ./back_to_nucleotides.py blastn.output mafft.output
"""

import sys
import fasta

dna_reader = fasta.FASTAReader(open(sys.argv[1]))
aa_reader = fasta.FASTAReader(open(sys.argv[2]))

for(dna_id, dna), (aa_id, aa) in zip(dna_reader, aa_reader):
    nuc_seq = []
    j = 0
    for i in range(0, len(aa)):
        a = aa[i]
        nuc = dna[j:(j+3)]
        if a != "-":
            nuc_seq.append(nuc)
            j += 3
        else:
            nuc_seq.append("---")
    print(dna_id, ''.join(nuc_seq))
    #print(''.join(nuc_seq))
    