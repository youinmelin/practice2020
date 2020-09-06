import pandas as pd
from pandas import DataFrame
import pprint

path = "data_source/"
filename = "panda_01_write_excel.xlsx"
filename = "panda_02_read_excel_02.xlsx"
# read excel file
df = pd.read_excel(path + filename)
data = df.values
# print(data.values[0])
# print("{0}".format(df))
data_dict = df.to_dict(orient='records')
# pprint.pprint(data_dict)
# print(data_dict)
for row_dict in data_dict:
    for k in row_dict:
        print('key:%s, value:%s' % (k, row_dict[k]))

