#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

a = 0

for i, line in enumerate(f):
    if line.startswith("SRR"):
        fields = line.rstrip("\r\n").split("\t") 
        a += 1
        print(fields[2])
        if a > 11:
            break