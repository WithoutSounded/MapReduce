#!/usr/bin/env python3
import sys



storage_dict = {}

for line in sys.stdin:
    line = line.strip()
    doc_name, value = line.split('\t')
    word, word_count = value.split(',')
    if doc_name in storage_dict:
        if word in storage_dict[doc_name]:
            storage_dict[doc_name][word] += int(word_count)
        else:
            storage_dict[doc_name][word] = int(word_count)
    
    else:
        storage_dict.setdefault(doc_name, {word:int(word_count)})

for doc_name in storage_dict:
    total = sum(storage_dict[doc_name].values())
    for word in storage_dict[doc_name]:
        key = word +','+ doc_name
        value = str(storage_dict[doc_name][word])+','+str(total)
        print('%s\t%s' % (key, value))