import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# dataset = pd.read_csv("/home/farinam_hz/PycharmProjects/Apriori-algorithm/Project1 - groceries.csv", sep=";", header= None)
unique_items_list = []

dataset_list =[]

for index, row in dataset.iterrows():
    items_series = list(row.str.split(','))

    for item in items_series[0]:
        if item == '':
            items_series[0].remove(item)
        if item not in unique_items_list and item != '':
            unique_items_list.append(item)
    print(items_series[0])
    dataset_list.append(items_series[0])

# print(dataset_list)


# print(dataset.shape)
# print(dataset.info())


# print(len(unique_items_list))

# print(dataset_list)
# inverted_index_dic = {}
# for trans in dataset: