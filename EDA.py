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
# print(count_dic)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

count_number_list = []
for item in count_item_list:
    count_number_list.append(count_dic[item])
ax.bar(count_item_list,count_number_list)
plt.show()


def bestselling(number_list, item_list):
    print("\nBESTSELLING PRODUCT:")
    max_number=number_list[0]
    for i in range(len(number_list)):
        if number_list[i] == max_number:
            print("Item:\t", item_list[i])
            print("Count:\t", number_list[i])


# bestselling(count_number_list, count_item_list)


def find_longest_transaction(trans_list):
    imax=[]
    max_trans = []
    imax.append(0)
    max_trans.append(trans_list[0])
    for i in range(len(trans_list)):
        if len(trans_list[i]) > len(max_trans[0]):
            imax.clear()
            max_trans.clear()
            max_trans.append(trans_list[i])
            imax.append(i)
        elif len(trans_list[i]) == len(max_trans[0]):
            imax.append(i)
            max_trans.append(trans_list[i])

    print("\nMAX TRANSACTIONS: ")
    for i in range(len(imax)):
        print("Transaction index:\t", imax[i])
        print("Length:\t", len(max_trans[0]))
        print("Items list:\t", max_trans[i])


# find_longest_transaction(dataset_list)


def transaction_length_barplot(trans_list):

    # transaction_index
    trans_dic = {}
    for i in range(len(trans_list)):
        trans_dic[i] = trans_list[i]
    trans_number_sorted = sorted(trans_dic, key=lambda k: len(trans_dic[k]), reverse=True)

    trans_number_label = []
    for trans in trans_number_sorted:
        trans_number_label.append(str(trans))

    # transactions_length
    trans_len_list = []
    for i in range(len(trans_number_sorted)):
        trans_len_list.append(len(trans_dic[trans_number_sorted[i]]))

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(trans_number_label, trans_len_list)
    plt.plot(range(max(trans_len_list)))
    plt.xlabel("Index of Transactions")
    plt.ylabel("Length of Transactions")
    plt.show()

    return trans_len_list

    # x_pos = np.arange(len(trans_number_label))
    # # y_pos = np.arange(32)
    #
    # plt.bar(x_pos, trans_len_list)
    # plt.xticks(x_pos, trans_number_label)
    # plt.show()


trans_len_list = transaction_length_barplot(dataset_list)


def transaction_length_boxplot(trans_list):

    plt.boxplot(trans_list)
    plt.show()


transaction_length_boxplot(trans_len_list)