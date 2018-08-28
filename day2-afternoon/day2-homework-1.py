#!/usr/bin/env python3

import sys
import numpy as np

fly_names = {}
a = 0
    
for i, line in enumerate(sys.stdin):
    if "DROME" in line and "FBgn" in line:
        fields = line.rstrip("\r\n").split()
        #fly_names.update({fields[2]:fields[3]})
        a += 1
        print(fields[3] + "\t\t" + fields[2])

print(a)
# for key, value in fly_names:
#     print(key + "\t\t" + value)