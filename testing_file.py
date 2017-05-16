# import csv
#
# my_dict = {"test": [1,2,3,4], "testing": [1,2,3,4]}
#
# # with open('mycsvfile.csv', 'wb') as f:  # Just use 'w' mode in 3.x
# #     w = csv.DictWriter(f, my_dict.keys())
# #     w.writeheader()
# #     w.writerow(my_dict)
#
# d = {"key1": [1,2,3], "key2": [4,5,6], "key3": [7,8,9]}
# with open("mycsvfile.csv", "wb") as outfile:
#    writer = csv.writer(outfile)
#    writer.writerow(my_dict.keys())
#    writer.writerows(zip(*d.values()))

import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(dict(sorted_x))