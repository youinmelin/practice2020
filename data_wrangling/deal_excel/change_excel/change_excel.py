# conding=utf-8
import pandas as pd
import os
import operator
from pandas import DataFrame
import pprint
    
path = 'data_source/'
filename = '7月未申报0716.xlsx'
# read excel file to list(dicts)
df = pd.read_excel(path + filename)
data = df.values
data_list = df.to_dict(orient='dict')
pprint.pprint (data_list)