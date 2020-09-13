# conding=utf-8
import pandas as pd
import os
import operator
from pandas import DataFrame
import pprint
import find_files
import rename_filename
"""
 从未申报名单中，提取出单位名称，联系人电话（法人，财务，办税）
 最终形成两列：1,电话；2,单位名称，其中电话列去除重复行
"""
    
# path = 'data_source/'
path = ''
filename = '7月未申报0716.xlsx'
filename = find_files.pick_file()
# read excel file to list(dicts)
df = pd.read_excel(path + filename)
data = df.values
data_dict = df.to_dict(orient='list')
# print(data_dict)
list_text = []
list_company_name = []
list_tel = []
for key in data_dict.keys():
    if '移动电话' in key:
        list_company_name += data_dict['纳税人名称']
        list_tel += data_dict[key]
# print(len(list_company_name))
# print(len(list_tel))
print('共计', len(list_tel), '行')
list_text.append(list_company_name)
list_text.append(list_text)
dict_text = dict()
dict_text['tel'] = list_tel
dict_text["companies"] = list_company_name
# print(dict_text)
# create dict to
df = pd.DataFrame(dict_text)
# 去除重复行
df = df.drop_duplicates(['tel'])
# 按照order指定的顺序排列
order = ['tel', 'companies']
df = df[order]


new_filename = rename_filename.add_filename_on_last(filename, '_new')
df.to_excel(path + new_filename,  index=False)
print('已经重新排列，新文件名： ', new_filename)
