#!/usr/bin/env python3

"""
Parse a single FASTA record from stdin and print id and sequence
"""

import sys

line = sys.stdin.readline()
assert line.startswith(">"), "Not a FASTA file."
ident = line[1:].rstrip("\r\n")

sequences = []
while True:
    line = sys.stdin.readline()
    if not line.startswith(">"):
        sequences.append(line.strip())
    else:
        break

sequence = "".join(sequences)

print(ident, sequence)