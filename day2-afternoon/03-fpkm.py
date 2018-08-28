#!/usr/bin/env python3

import sys
import numpy as np 

def read_fpkms_from_t_data(fname):
    all_fpkms = []
    for i, line in enumerate(open(fname)):
        if i == 0:
            continue
        fields = line.rstrip("\r\n").split("\t")
        fpkm = fields[11]
        all_fpkms.append(float(fpkm))
    return all_fpkms

all_fpkms_1 = read_fpkms_from_t_data(sys.argv[1])
all_fpkms_2 = read_fpkms_from_t_data(sys.argv[2])

print(len(all_fpkms_1), len(all_fpkms_2))
correlation = np.corrcoef(all_fpkms_1, all_fpkms_2)
print("Pearson's R:", correlation[0,1])