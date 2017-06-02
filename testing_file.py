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

# import operator
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_x = sorted(x.items(), key=operator.itemgetter(1))
# print(dict(sorted_x))

# import json
# with open('data/Hasil.json', 'r') as f:
# 	for line in f:
# 		tweet = json.loads(line)
# 		# tokens = preprocess(str(tweet['text']))
# 		print(tweet['text'])

# import numpy as np
# import numpy.random
# import matplotlib.pyplot as plt
#
# # Create data
# x = np.random.randn(4096)
# y = np.random.randn(4096)
#
# # Create heatmap
# heatmap, xedges, yedges = np.histogram2d(x, y, bins=(64, 64))
# extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
#
# print(len(heatmap))
# # Plot heatmap
# plt.clf()
# plt.title('Pythonspot.com heatmap example')
# plt.ylabel('y')
# plt.xlabel('x')
# plt.imshow(heatmap, extent=extent)
# plt.show()
