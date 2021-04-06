import sys

number = []
for value in sys.stdin:
	if value != '':
		number.append(value.strip())

for value in number:
	print("%s\t%s" % (value, '_'))
