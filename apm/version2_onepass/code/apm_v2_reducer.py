import sys
SUPPORT = 2


patternCounter = {}
for tx in sys.stdin:
    tx=tx.strip()
    pattern, count = tx.split('\t')
    if pattern in patternCounter:
        patternCounter[pattern]+=1
    else:
        patternCounter[pattern] = 1
      
      
final_pattern = []
for i in patternCounter.keys():
    if patternCounter[i] >= SUPPORT:
        final_pattern.append(i)
#         print(i)
final_pattern = sorted(final_pattern, key = len,reverse = True)
for pattern in final_pattern:
    print("%s"%pattern)
