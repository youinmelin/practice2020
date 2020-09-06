# conding=utf-8
import pandas as pd
import os
import operator
from pandas import DataFrame
import pprint

"""
 把excel表格中沙河税务所的行筛查出来，再按照尾号排序，另存一份
 步骤：
 1.读取文件
 2.按照事先指定的关键字列表，确定两个关键列：主管税务所、纳税人识别码 ,注意要先把空格过滤掉 
     search_keyword(object_keyword, keywords_list) -> final_keyword
 3.提取出沙河所的列 pick_data(pick_list, key, value)
 4.按照尾号排序 sort_data(sort_list, by_key)
 5.保存文件   
"""


# 寻找对应的表头
def search_keyword(origin_list, keywords_list):
    header_list = [header for header in origin_list[0]]
    for header_k in header_list:
        for k in keywords_list:
            if header_k == k:
                return k


def pick_data(pick_list, key, value):
    """
    pick data from dicts in a list
    从列表中的字典中寻找指定的内容，并返回符合条件的字典存入字典中
    :param pick_list:
    :param key: dict's key
    :param value: dict's value
    :return: list after picking
    """
    list_picked = []
    for row_dict in pick_list:
        if value in row_dict[key]:
            list_picked.append(row_dict)
    return list_picked


def find_the_one_digital_in_str(origin_str, number=-1):
    """
     find_the_digital_from_str
     根据指定的字符串和number，返回第number位的数字，从0开始，倒数第一位是-1(默认值)
    :param origin_str:
    :param number: which number of the digital do you want, the first is zero, the last is -1(default)
    :return: one digital in the str you want
    """
    list_digitals = [i for i in origin_str if i.isdigit()]
    the_digital = list_digitals[number]
    return the_digital


def sort_data(sort_list, by_key, order='ascend'):
    list_sorted = []
    # list_sorted = sorted(sort_list, key=operator.itemgetter(by_key))
    for i in range(10):
        for row_dict in sort_list:
            if find_the_one_digital_in_str(row_dict[by_key]) == str(i):
                list_sorted.append(row_dict)
    return list_sorted;


def main(path, filename, keyword_department, list_master_keywords='', list_taxpayer_number_keywords=''):
    if list_master_keywords == '':
        list_taxpayer_number_keywords = ['纳税人识别号', '纳税识别号', '纳税人识别码', '纳税人识别码']
    if list_taxpayer_number_keywords == '':
        list_master_keywords = ['主管所', '主管税务所', '税务所', '管理所']

    # read excel file to list(dicts)
    df = pd.read_excel(path + filename)
    data = df.values
    data_list = df.to_dict(orient='records')

    keyword_master = search_keyword(data_list, list_master_keywords)
    print('keyword_master', keyword_master)
    keyword_taxpayer = search_keyword(data_list, list_taxpayer_number_keywords)
    print('keyword_taxpayer', keyword_taxpayer)

    new_list = pick_data(data_list, keyword_master, keyword_department)
    new_list = sort_data(new_list, keyword_taxpayer)
    print('排序后的结果:', new_list)

    # write list into a new excel file
    df = pd.DataFrame(new_list)
    filename = "panda_02_read_excel_02_sorted.xlsx"
    prefix_filename = os.path.splitext(filename)[0]
    suffix_filename = os.path.splitext(filename)[1]
    new_filename = prefix_filename + '_sorted' + suffix_filename
    df.to_excel(path + filename, sheet_name='new', index=False)


if __name__ == '__main__':
    path = "data_source/"
    filename = "panda_02_read_excel_02.xlsx"
    list_taxpayer_number_keywords = ['纳税人识别号', '纳税识别号', '纳税人识别码', '纳税人识别码']
    list_master_keywords = ['主管所', '主管税务所', '税务所', '管理所']
    keyword_department = '沙河'
    main(path, filename, keyword_department, list_master_keywords, list_taxpayer_number_keywords)
