import pandas as pd
from sys import argv
from pandas import DataFrame

path = "data_source/"
filename = "panda_01_write_excel.xlsx"
# filename = argv[1]
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
with pd.ExcelWriter(path + filename) as writer:
    df.to_excel(writer, sheet_name='new1', index=False)
    df.to_excel(writer, sheet_name='new2', index=False)
with pd.ExcelWriter(path + filename) as writer:
    df.to_excel(writer, sheet_name='new3', index=False)
    work_sheets = writer.sheets
    work_sheet = work_sheets['new3']
    # set width of columns
    work_sheet.column_dimensions['A'].width = 20
    print(dir(work_sheet))
    df.to_excel(writer, sheet_name='new4', index=False)
