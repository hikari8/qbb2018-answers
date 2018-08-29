#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

for i, line in enumerate(f):
    # One way to skip header
    if i == 0:
        continue
    #another string operation
    ##if line.startwith("t_id"):
    ##    continue
    fields = line.rstrip("\r\n").split("\t")
    tx_len = int(fields[4]) - int(fields[3])
    if tx_len > 10000:
        print(fields[5], tx_len)
    
    #print(line.rstrip())
    #if i > 10:
    #    break