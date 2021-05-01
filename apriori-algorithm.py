import itertools

import numpy as np
import pandas as pd
from collections import defaultdict
from mlxtend.frequent_patterns import apriori, association_rules

dataset = pd.read_csv("/home/farinam_hz/PycharmProjects/Apriori-algorithm/Project1 - groceries.csv",
                      sep=";", header=None)
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

inverted_index_default = defaultdict(list)
trans_num = 0
for trans in dataset_list:
    for i in range(len(trans)):
        inverted_index_default[trans[i]].append(trans_num)
    trans_num += 1
inverted_index = dict(inverted_index_default)

count_dic = {}
for item in unique_items_list:
    count_dic[item] = len(inverted_index[item])

count_item_list = sorted(count_dic, key=count_dic.get, reverse= True)
count_number_list = []
for item in count_item_list:
    count_number_list.append(count_dic[item])


'''''
def min_support(number_list):
    support_count_list = []
    sum_count = sum(number_list)
    for num in number_list:
        support_count_list.append(num/sum_count)

    print(*support_count_list)
    return sum(support_count_list)/len(support_count_list)
'''''

def check_subset_frequency(itemset, l, n):
    # if n == 1:
    if n > 1:
        subsets = list(itertools.combinations(itemset, n))
    else:
        subsets = itemset
    for iter1 in subsets:
        if not iter1 in l:
            return False
    return True


class Arules:
    def __init__(self):
        pass

    def get_frequent_item_sets(self, transactions, min_support):
        l1 = {}
        L1 = []
        for i in range(len(count_number_list)):
            if count_number_list[i] >= min_support:
                l1[count_item_list[i]] = count_number_list[i]
        k = 2
        x = l1
        while True:
            if k == 2:
                x = sorted(list(x.keys()))
                L1 = list(itertools.combinations(x, k))
            if k > 2:
                x = list(x.keys())
                L1 = sorted(list(set([item for t in x for item in t])))
                L1 = list(itertools.combinations(L1, k))
            c2 = {}
            l2 = {}
            for iter1 in L1:
                count = 0
                for iter2 in transactions:
                    if set(list(iter1)).issubset(set(iter2)):
                        count += 1
                c2[iter1] = count
            for key, value in c2.items():
                if value >= min_support:
                    if check_subset_frequency(key, x, k-1):
                        l2[key] = value
            if not l2:
                break
            k += 1
            x = l2
            print(l2)

    def get_arules(self,min_support=None, min_confidence=None,min_lift=None, sort_by='lift'):
        pass


arules = Arules()
Arules.get_frequent_item_sets(arules, dataset_list, 50 )
# '''''
