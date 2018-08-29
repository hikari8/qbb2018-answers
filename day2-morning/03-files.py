#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

#print(f)
#print(type(f))

#for i in range(20):
#    print(f.readline().rstrip())

#count = 0
#for line in f:
#    print(line.strip())
#    count += 1
#    if count > 10:
#        break

for i, line in enumerate(f):
    print(line.rstrip())
    if i > 10:
        break