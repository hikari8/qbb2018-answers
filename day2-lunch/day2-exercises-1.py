#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

i = 0
a = 0

for i, line in enumerate(f):
    if line.startswith("SRR"):
        i += 1
        
print(i)