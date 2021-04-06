import sys

prefix = []
postfix = []

for tx in sys.stdin:
#     print(tx)
    tx = tx.strip()
    key, value = tx.split('\t')
    if key == '_':
        key = value
        
    else: # round2
        key = key +','+ value
    prefix.append(key)
    postfix.append(value)
for pre in prefix:  
    for post in postfix:
        print_format = pre+','+post
        print("%s\t%s"%(print_format, '_'))

