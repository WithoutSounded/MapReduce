#!/usr/bin/env python3
import sys

# Mapper output: (filename, (word, word_count))
for line in sys.stdin:
    line = line.strip('\n')
    key, word_count = line.split('\t')
    word, filename = key.split(',')
    
    key = filename
    values = word + "," + word_count
    print('%s\t%s' % (key, values))