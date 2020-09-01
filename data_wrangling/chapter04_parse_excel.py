# coding:utf-8
import xlrd
import pprint

'''
read excel files
excel to dicts in a list
the 1st line must be title line
'''


def excel_to_dict_in_list(path, filename, sheet_num=0):
    # xlrd.Book.encoding = "utf-8"
    # xlrd.Book.encoding = "gbk"
    book = xlrd.open_workbook(path + filename, encoding_override='gbk')
    sheets_list = []
    sheets_name_list = []
    for sheet in book.sheets():
        sheets_list.append(sheet)
        sheets_name_list.append(sheet.name)
    # print (sheets_list, sheets_name_list)
    # print (dir(sheets_list[0]))
    # return rows number
    print("row number:", sheet.nrows)
    all_list = []
    key_list = sheets_list[0].row_values(0);
    key_num = len(key_list);
    print("col number:", key_num)
    print("titles:", key_list)
    # for key in key_list:
    #     key_dict[key]=''
    # pprint.pprint(key_dict)

    for i in range(1, sheet.nrows):
        # 从索引1开始循环，因为索引0是标题行
        key_dict = {}
        # 必须把空字典的定义放在for循环内部，每次会申请一个新地址
        # 如果放在for循环外边，总是同一个地址，造成列表内的每个字典内容都一样
        row = (sheets_list[sheet_num].row_values(i))
        for j, cell in enumerate(row):
            key_dict[key_list[j]] = cell
        all_list.append(key_dict)
        # print(i, all_list[i] )
    # print('all_list', all_list)
    return (all_list)


import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

path = "book/data/chp4/"
filename = "SOWC 2014 Stat Tables_Table 9.xlsx"
path = 'data_source/'
filename = 'students.xlsx'
all_list = excel_to_dict_in_list(path, filename)
print('all_list', all_list)
