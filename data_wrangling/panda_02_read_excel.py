import pandas as pd
import operator
from pandas import DataFrame
import pprint

path = "data_source/"
filename = "panda_02_read_excel_02.xlsx"
# read excel file
df = pd.read_excel(path + filename)
data = df.values
# print(data.values[0])
# print("{0}".format(df))
data_list = df.to_dict(orient='records')
# pprint.pprint(data_dict)
# print(data_dict)
for row_dict in data_list:
    for key, value in row_dict.items():
        # print('key:%s, value:%s' % (k, row_dict[k]))
        print(key, ":", value)


def pick_data(pick_list, key, value):
    """
    pick data from dicts in a list
    :param key: dict's key
    :param value: dict's value
    :return: list after picking
    """
    list_picked = []
    for row_dict in pick_list:
        if value in row_dict[key]:
            list_picked.append(row_dict)
    return list_picked


print(pick_data(data_list, '主管税务所', '沙河'))


def find_the_one_digital_in_str(origin_str, number=-1):
    """
     find_the_digital_from_str
    :param origin_str:
    :param number: which number of the digital do you want, the first is zero, the last is -1
    :return: one digital in the str you want
    """
    list_digitals = [i for i in origin_str if i.isdigit()]
    the_digital = list_digitals[number]
    return the_digital


def sort_data(sort_list, by_key, order='desc'):
    list_sorted = []
    # list_sorted = sorted(sort_list, key=operator.itemgetter(by_key))
    for i in range(10):
        for row_dict in sort_list:
            if find_the_one_digital_in_str(row_dict[by_key]) == str(i):
                list_sorted.append(row_dict)
    return list_sorted;


new_list = sort_data(data_list, '纳税人识别号')
print('排序后的结果:', new_list)
df = pd.DataFrame(new_list)
filename = "panda_02_read_excel_02_sorted.xlsx"
df.to_excel(path + filename, sheet_name='new', index=False)

list_taxpayer_number = []
list_master = []
