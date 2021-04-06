#!/usr/bin/env python3
import sys

word_count = {}

for line in sys.stdin:
    key, value = line.split('\t')
    if key in word_count:
        word_count[key] += 1
    else:
        word_count[key] = 1

for key in word_count.keys():
    print("%s\t%s"%(key, word_count[key]))