import sys
SUPPORT=2

data = """
100 A1,B2,C3,E7
200 A1,B2,E3,E5
300 A1,B2,G3
400 A1,E8
"""
input_data = data
input_data = input_data.strip()
input_data_pre = input_data.split('\n')


########### input pattern data
db_pattern = []
for tx in input_data_pre:
    key, value = tx.split(' ')
    db_pattern.append(value)

    
can_p_dic = {}    
for tx in sys.stdin:
    tx = tx.strip()
    pattern, _ = tx.split('\t')
    if pattern in can_p_dic:
        continue
    else:
        can_p_dic[pattern] = 0
    
   
    for db_tx in db_pattern:
        ptr1 =0
        ptr2 =0
        flag =0
        while(ptr1<len(pattern) and ptr2<len(db_tx)):
            if pattern[ptr1] == db_tx[ptr2]:
                ptr1 +=1
                ptr2 +=1
            else:
                ptr2+=1
        if ptr1 == len(pattern):
            can_p_dic[pattern] += 1
            
for value in can_p_dic.keys():
    if can_p_dic[value] >= SUPPORT:
        print("%s\t%s"%(value, can_p_dic[value]))

#for i in db_pattern:
#    print("%s\t%s"%(i, 1))
