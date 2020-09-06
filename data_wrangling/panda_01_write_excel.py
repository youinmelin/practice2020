import pandas as pd
from pandas import DataFrame

path = "data_source/"
filename = "panda_01_write_excel.xlsx"
# write excel file
dict1 = {
    'name': ['Nancy', 'lin'],
    'gander': ['female', 'male']
}
list1 = [{'id': 1.0, 'name': 'Nasa', 'gender': 'male', 'age': 8.0, 'class': '3-4'}, {'id': 2.0, 'name': 'Lin', 'gender': 'male', 'age': 40.0, 'class': '3-4'}, {'id': 3.0, 'name': 'Nancy', 'gender': 'famale', 'age': 37.0, 'class': '3-3'}, {'id': 4.0, 'name': 'XiangYu', 'gender': 'famale', 'age': 35.0, 'class': '3-1'}, {'id': 5.0, 'name': '郑林', 'gender': 'male', 'age': 20.0, 'class': '3-2'}]

df = pd.DataFrame(dict1)
df.to_excel(path + filename, index=False)
df = pd.DataFrame(list1)
filename = "panda_01_write_excel_02.xlsx"
df.to_excel(path + filename, sheet_name='new', index=False)
