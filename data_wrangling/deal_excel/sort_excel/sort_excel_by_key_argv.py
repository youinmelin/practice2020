# encoding=utf-8
from sys import argv

import pandas as pd
import os
import operator
from pandas import DataFrame
import pprint
import yaml_read

"""
 py文件相同目录下要有yaml_read.py文件，还要有个子文件夹data_source存放key_words.yml文件
 把excel表格中沙河税务所的行筛查出来，再按照尾号排序，另存一份
 步骤：
 1.读取文件
 2.按照事先指定的关键字列表，确定两个关键列：主管税务所、纳税人识别码 ,注意要先把空格过滤掉 
     search_keyword(object_keyword, keywords_list) -> final_keyword
 3.提取出沙河所的列 pick_data(pick_list, key, value)
 4.按照尾号排序 sort_data(sort_list, by_key)
 5.保存文件   
"""


def search_keyword(origin_list, keywords_list):
    """
     寻找对应的表头，如果表格中的标题列与关键词列有相同的字符串，
     那么就把这个列当做要操作的列，可以进行排序，筛选等
    :param origin_list: 表格中的标题列
    :param keywords_list:  事先写好的关键词列
    :return:
    """
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

    # read excel file to list(dicts)
    xl = pd.ExcelFile(path + filename)
    sheet_names = xl.sheet_names # get all name of sheets

    for i, sheet_name_str in enumerate(sheet_names):
        print("begin sheet: " + sheet_name_str)
        df = pd.read_excel(path + filename, sheet_name=sheet_name_str)
        if df.keys().size == 0:
            print(sheet_name_str + ' is empty.')
            continue
        data_list = df.to_dict(orient='records')

        keyword_master = search_keyword(data_list, list_master_keywords)
        print('keyword_master', keyword_master)
        keyword_taxpayer = search_keyword(data_list, list_taxpayer_number_keywords)
        print('keyword_taxpayer', keyword_taxpayer)

        # 如果标题栏中找不到纳税人信息，则不进行数据清洗,原样输出
        new_list = data_list
        if keyword_taxpayer is None:
            print('can not find taxpayers keywords in sheet: ' + sheet_name_str)
        else:
            # 如果标题栏含有部门信息，就要筛选出本部门的内容
            if keyword_master is not None:
                new_list = pick_data(data_list, keyword_master, keyword_department)

            # 按尾号排序
            new_list = sort_data(new_list, keyword_taxpayer)
            # print('排序后的结果:', new_list)

        # write list into a new excel file
        df = pd.DataFrame(new_list)
        # filename = "panda_02_read_excel_02_sorted.xlsx"
        prefix_filename = os.path.splitext(filename)[0]
        suffix_filename = os.path.splitext(filename)[1]
        new_filename = prefix_filename + '_已排序' + suffix_filename
        print('i:', i)
        if i == 0:
            df.to_excel(path + new_filename, sheet_name=sheet_name_str, index=False)
        else:
            with pd.ExcelWriter(path + new_filename, mode='a', engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name=sheet_name_str, index=False)
        print("end sheet: " + sheet_name_str)
    # os.remove((path+filename))
    # os.rename(path+new_filename, path+filename)
    # break # 暂时循环一次，只处理第一个sheet
        # 后续还有问题要解决：
        #   1.空sheet: if df.keys().size == 0: 解决
        #   2.多个sheets的话如果用to_excel的话，后边的sheet会覆盖前边的。如果用ExcelWriter可以追加sheet在最后
        #       但是会在最左侧增加一条索引列，另外用新文件名的话会提示找不到，用原文件名会每次都追加一堆sheet


if __name__ == '__main__':
    path = os.getcwd() + '\\data_source\\'
    filename = "panda_02_read_excel_02.xlsx"
    filename = "附件：2017-2018年未超期多缴清册7.24.xlsx"
    # filename = argv[1]
    # yaml_filename = 'key_words.yml'
    # with open(path+filename, 'r', encoding='utf-8') as f:
    #     s = f.read()
    # key_words = yaml.load(s, Loader=yaml.FullLoader)

    list_taxpayer_number_keywords = yaml_read.read_keywords_from_yaml()['taxpayer_number_keywords']
    list_master_keywords = yaml_read.read_keywords_from_yaml()['master_keywords']
    keyword_department = yaml_read.read_keywords_from_yaml()['keyword_department']
    # main(path, filename, keyword_department, list_master_keywords, list_taxpayer_number_keywords)
    try:
        main(path, filename, keyword_department, list_master_keywords, list_taxpayer_number_keywords)
        # pass
    except Exception as e:
        print(e)
    else:
        print('succeed')
