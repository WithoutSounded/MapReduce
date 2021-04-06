import sys

def masking(pattern, mask):
    ptr_pattern = 0
    ptr_mask = 0
    pattern_f = ''
    while(ptr_mask<len(mask)):
        # adding , w/ condition
#         print("pointer of pattern : ",ptr_pattern)
#         print("pointer of mask : ",ptr_mask)
        if pattern[ptr_pattern] == ',':
#             print(pattern[ptr_pattern])
#             print(ptr_pattern)
#             print(pattern_f)
            if pattern_f == '' or pattern_f[-1] == ',':
                ptr_pattern += 1
            else:
                pattern_f = pattern_f+','
                ptr_pattern +=1
        # masking
        if mask[ptr_mask] == '1':
#             print('masking 1')
            pattern_f += pattern[ptr_pattern]
            ptr_pattern += 1
            ptr_mask += 1
        else:
#             print('masking 0')
            ptr_pattern += 1
            ptr_mask += 1
    # Last times checking if , is in the end
    if pattern_f[-1] == ',':
        pattern_f = pattern_f[:-1]
    return pattern_f



for tx in sys.stdin:
    tx = tx.strip()
    key, pattern = tx.split(' ')
    a = len(pattern.replace(',', ''))
#     print(a)
    for mask in range(1, 2**a):
        mask = bin(mask)
#         only fill 0 to the left not right, 01, 10, 11, 100 ->  0100, 1000, 1100 , 1000, value missed
        mask = mask[2:].zfill(a)
#         print("mask is ",mask)
#         print("tx is ",tx)
        possible_pattern = masking(pattern, mask)
#         print(possible_pattern)
        print("%s\t%s"%(possible_pattern, 1))

