#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

c = 0

for i, line in enumerate(f):
    if line.startswith("SRR") and "NH:i:1" in line:
        fields = line.rstrip("\r\n").split("\t")
        c += 1
                
print("There are " + str(c) + " number of reads that map to exactly one location.")