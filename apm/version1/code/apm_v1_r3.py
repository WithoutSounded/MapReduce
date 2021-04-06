# a = ['A1,A2,A3\t4', 'A2,B1,E2\t3']
import sys

mapper2_output = []
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
#    print("%s\t%s"%(prefix, item[-1]))
    mapper2_output.append("%s\t%s"%(prefix, item[-1]))
#    print('-----------------------------')

reducer2_output = []
prefix = []
postfix = []

for tx in mapper2_output:
#     print(tx)
    tx = tx.strip()
    key, value = tx.split('\t')
    if key == '_':
        key = value
    # round 2
    else:
        key = key +','+ value
    
    prefix.append(key)
    postfix.append(value)
for pre in prefix:  
    for post in postfix:
        print_format = pre+','+post
        print("%s\t%s"%(print_format, '_'))
        reducer2_output.append("%s\t%s"%(print_format, '_'))
