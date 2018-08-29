#!/usr/bin/env python3

import sys

print("Hello " + sys.argv[1])
#print("Hello {0}".format(sys.argv[1]))

print("with indexing:")
for i in range(1,len(sys.argv)):
    print("{1} Hello {0}".format(sys.argv[i], "Hey!"))

print("With iterations:")
for name in sys.argv[1:]:
    print("{1} Hello {0}".format(name, "Hey!"))

#print("Hello %s" % sys.argv[1])

