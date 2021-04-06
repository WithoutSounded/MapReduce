#!/usr/bin/env python3
import sys
# dictionary to map words to counts
wordcount = {}
# input comes from STDIN
for line in sys.stdin:
	# rm leading and trailing whitespace
	line = line.strip()
	# parse the input we got from mapper.py
	word, count = line.split('\t', 1)
	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError: # simply ignore if err
		continue
	try: # accumulate the count
		wordcount[word] = wordcount[word]+count
	except:
		wordcount[word] = count
# write the tuples to stdout
for word in wordcount.keys():
	print("%s\t%s" % (word, wordcount[word]))
