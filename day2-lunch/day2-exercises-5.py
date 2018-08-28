#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

i = 0
tot = 0
ct = 0

for i, line in enumerate(f):
    if line.startswith("SRR"):
        fields = line.rstrip("\r\n").split("\t")
        a = int(fields[4])
        tot += a
        ct += 1
        avg = tot/ct
        
print(avg)