#!/usr/bin/env python3

import sys
import fasta

target = fasta.FASTAReader(open(sys.argv[1]))
query = fasta.FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])

kmers = {}

for ident, sequence in query:
    for i in range(0, len(sequence)-k):
        kmer = sequence[i:i+k]
        if kmer not in kmers:
            kmers[kmer] = [i]
        else:
            kmers[kmer].append(i)

for ident, sequence in target:
    for i in range(0, len(sequence)-k):
        kmer = sequence[i:i+k]
        if kmer in kmers:
            for var in kmers[kmer]:
                print(ident, "\t", i, "\t", var, "\t", kmer)