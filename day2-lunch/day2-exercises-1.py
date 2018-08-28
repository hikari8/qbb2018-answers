#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

i = 0
a = 0

for i, line in enumerate(f):
    if line.startswith("SRR072893"):
        i += 1
    else:
        a += 1
        
print(i, a)

    #else:
    #    a = a + 1
    #    print(i, count)
    #fields = line.rstrip("\r\n").split("\t")
    #tx_len = int(fields[4]) - int(fields[3])
    #if tx_len > 10000:
    #    print(fields[5], tx_len)
    
    #print(line.rstrip())
    #if i > 10:
    #    break