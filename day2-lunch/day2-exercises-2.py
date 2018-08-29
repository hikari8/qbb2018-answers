#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

b = 0

for i, line in enumerate(f):
    if line.startswith("SRR") and "40M" in line:
        fields = line.rstrip("\r\n").split("\t")
        b += 1

print("There are " + str(b) + " that match perfectly with genome.") 