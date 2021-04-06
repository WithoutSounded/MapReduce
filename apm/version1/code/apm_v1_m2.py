import sys


for tx in sys.stdin:
#    print(tx)
    tx = tx.strip()
    item , value = tx.split('\t')
    item = item.split(',')
    prefix = ''
    for i in item[:-1]:
        if prefix == '':
            prefix = str(i)
        else:
            prefix = prefix+','+str(i)
    if prefix =='':
        prefix = '_'
    print("%s\t%s"%(prefix, item[-1]))


