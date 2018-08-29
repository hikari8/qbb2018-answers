#!/usr/bin/env python3
# Run with:

import sys
import numpy as np

#if len(sys.argv) > 1:
#    f = open(sys.argv[1])
#else:
#    f = sys.stdin

fly_names = {}
a = 0
    
for line in open(sys.argv[1]):
    if "DROME" in line and "FBgn" in line:
        fields = line.rstrip("\r\n").split()
        #a += 1
        #print(fields[3] + "\t\t" + fields[2])
        fly_names.update({fields[3]:fields[2]})
#print(a)

for line in open(sys.argv[2]):
    if "FBgn" in line:
        fields = line.rstrip("\r\n").split("\t")
        fly = fields[8]
        if fly in fly_names.keys():
            uniq = fly_names[fly]
            print(line.rstrip('\r\n') + "\t" + uniq)
        else:
            if len(sys.argv) > 3:
                pass
            else:
                print(line.rstrip('\r\n') + "\t" + "Not found")
                


