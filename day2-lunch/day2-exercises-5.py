#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

i = 0
a = 0
tot=0
ct=0

for i, line in enumerate(f):
    if line.startswith("SRR072893"):
        fields = line.rstrip("\r\n").split("\t")
        a = int(fields[4])
        tot+=a
        ct+=1
        
print(tot/ct)