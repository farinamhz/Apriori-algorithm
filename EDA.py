import numpy as np
import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt

dataset = pd.read_csv("/home/farinam_hz/PycharmProjects/Apriori-algorithm/Project1 - groceries.csv", sep=";", header= None)
unique_items_list = []

dataset_list =[]

for index, row in dataset.iterrows():
    items_series = list(row.str.split(','))

    items_series_copy = items_series[0].copy()
    for item in items_series_copy:
        if item == '':
            items_series[0].remove(item)
        elif item not in unique_items_list:
            unique_items_list.append(item)
    dataset_list.append(items_series[0])

# print(len(unique_items_list))
# print(dataset_list)
# print(dataset.shape)
# print(dataset.info())
# print(len(unique_items_list))
# print(dataset_list)


inverted_index_default = defaultdict(list)
trans_num = 0
for trans in dataset_list:
    for i in range(len(trans)):
        inverted_index_default[trans[i]].append(trans_num)
    trans_num += 1
inverted_index = dict(inverted_index_default)
# print(inverted_index)

x=[]
y=[]
count_dic = {}
for item in unique_items_list:
    count_dic[item] = len(inverted_index[item])

count_item_list = sorted(count_dic, key=count_dic.get, reverse= True)
print(count_dic)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

count_number_list = []
for item in count_item_list:
    count_number_list.append(count_dic[item])
ax.bar(count_item_list,count_number_list)
plt.show()