#!/usr/bin/env python3
import string
from string import punctuation
import sys


# Mapper output: ((word, document_name)   1)
for line in sys.stdin:
    line = line.translate(str.maketrans('', '', string.punctuation)).strip('\t')
    line_contents = line.split(" ")
    doc_name = line_contents[0]
    line_contents.remove(doc_name)
    for content in line_contents:
        content = content.strip().lower()
        key = content + "," + doc_name
        print('%s\t%s' % (key, 1))
        