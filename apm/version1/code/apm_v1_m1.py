import sys

for tx in sys.stdin:
    tx = tx.strip()
#    print(tx)
    key,value = tx.split()
    value = value.split(',')
    for i in value:
        print("%s\t%s"%(key,i))

