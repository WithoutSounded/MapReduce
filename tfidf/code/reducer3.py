#!/usr/bin/env python3
import math

NUMBER_OF_TOTAL_DOCUMENT = 12

storage_dict_2 = {}

for line in sys.stdin:
    line = line.strip()
    word, value = line.split('\t')
    doc, wc, dwc, num_1 = value.split(',')
    
    if word in storage_dict_2:
        storage_dict_2[word][doc] = float(wc)/float(dwc)
    else:
        storage_dict_2.setdefault(word, {doc:float(wc)/float(dwc)})

for word in storage_dict_2:
    for doc in storage_dict_2[word]:
        
        tf = storage_dict_2[word][doc]
        
        idf_log_e = math.log(NUMBER_OF_TOTAL_DOCUMENT / (len(storage_dict_2[word])))
        idf_log_10 = math.log10(NUMBER_OF_TOTAL_DOCUMENT / (len(storage_dict_2[word])))

        
        tfidf_loge = tf*idf_log_e
        tfidf_log_10 = tf*idf_log_10
        
        
        key = word + ',' + doc
        
        value = tfidf_log_10
        print("%s\t%s" % (key, value))
        