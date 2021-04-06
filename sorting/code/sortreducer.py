#!/usr/bin/env python3
import sys

wordcount = {}

for line in sys.stdin:
    unsortedvalue = line.strip()
    key, value = unsortedvalue.split('\t', 1)
    print("%s\t%s" % (key, ""))
