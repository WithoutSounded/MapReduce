import sys

DEFINE_SUPPORT = 3

storage_dict = {}
double_check = {}

for data in sys.stdin:
    data = data.strip()
    key, value = data.split('\t')

    if value in storage_dict:
        storage_dict[value] += 1
    else:
        storage_dict[value] = 1

for i in storage_dict.keys():
    if storage_dict[i] >= DEFINE_SUPPORT:
# Output #1
        print("%s\t%s"%(i, storage_dict[i]))
    else:
        for separated_value in i:
            if separated_value in double_check:
                double_check[separated_value] += 1
            else:
                double_check[separated_value] = 1
# Output #2
for i in double_check.keys():
    if double_check[i] >= DEFINE_SUPPORT:
        print("%s\t%s"%(i, double_check[i]))

