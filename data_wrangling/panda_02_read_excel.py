import pandas as pd
import operator
from pandas import DataFrame
import pprint

path = "data_source/"
filename = "panda_02_read_excel_02.xlsx"
# read excel file
xl = pd.ExcelFile(path + filename)
sheet_names = xl.sheet_names
print(sheet_names)
for sheet_str in sheet_names:
    df = pd.read_excel(path + filename, sheet_name=sheet_str)
    # print("keys:", df.keys().size)
    if df.keys().size == 0:
        print(sheet_str + ' is empty.')
        continue
    print("keys:", df.keys())
    data = df.values
# print(data.values[0])
# print("{0}".format(df))

data_list = df.to_dict(orient='records')
# pprint.pprint(data_dict)
# print(data_dict)
# for row_dict in data_list:
#     for key, value in row_dict.items():
#         # print('key:%s, value:%s' % (k, row_dict[k]))
#         print(key, ":", value)



