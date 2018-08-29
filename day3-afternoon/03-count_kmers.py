#!/usr/bin/env python3

import sys
import fasta

reader = fasta.FASTAReader( sys.stdin )

kmers = {}
k = 11

for ident, sequence in reader:
    for i in range( 0, len(sequence) - k ):
        kmer = sequence[i:i+k]
        if kmer not in kmers:
            kmers[kmer] = 1
        else:
            kmers[kmer] += 1

for key in kmers:       
    print( key, kmers[key] )