import sys
for line in sys.stdin: # input from STDIN
    line = line.strip() # rm leading/trailing whitespace
    words = line.split() # split the line into words
    for word in words: # each with a count of 1
		# write the results to STDOUT;
		# will be the input of the reducer.py
		# tab-delimited; word appears once(1)
        print("%s\t%s" % (word, 1))
