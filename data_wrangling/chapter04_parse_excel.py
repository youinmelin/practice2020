import xlrd
# read excel files

path = "book/data-wrangling/data/chp4/"
filename = "SOWC 2014 Stat Tables_Table 9.xlsx"
book = xlrd.open_workbook(path + filename)
sheets_list = []
sheets_name_list = []
for sheet in book.sheets():
    sheets_list.append(sheet)  
    sheets_name_list.append(sheet.name)
print (sheets_list, sheets_name_list)
# print (dir(sheets_list[0]))
# return rows number
print(sheet.nrows)
for i in range(sheet.nrows):
    print (sheets_list[1].row_values(i))
