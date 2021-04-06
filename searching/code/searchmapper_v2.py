import os
import sys

import re


target_pattern = 'abc'

word = []
for value in sys.stdin:
	value = value.strip()
	
	match = re.search(target_pattern, value)
	
	if match:
		filename = os.path.split(os.environ["mapreduce_map_input_file"])[-1]
		print('%s\t%s' % (filename, '_'))
