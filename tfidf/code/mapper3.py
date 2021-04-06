#!/usr/bin/env python3
import sys

# Mapper output: (word, (document_name, word_count, number_of_words_in_document, 1))
mapper = []
for line in sys.stdin:
    line = line.strip()
    word_and_doc, wordcount_and_num_words_in_doc = line.split('\t')
    word, doc_name = word_and_doc.split(',')
    word_count, num_words_in_doc = wordcount_and_num_words_in_doc.split(',')
    
    
    key = word
    value = doc_name + "," + word_count + "," + num_words_in_doc + "," + '1'
    print('%s\t%s' % (key, value))
    mapper.append('%s\t%s' % (key, value))
    