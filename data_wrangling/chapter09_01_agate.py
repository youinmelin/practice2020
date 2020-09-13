import xlrd
from pprint import pprint

path = 'book/data/unicef/'
filename = 'unicef_oct_2014.xls'
workbook = xlrd.open_workbook(path + filename)
print('sheets number',  workbook.nsheets)
print('sheet name', workbook.sheet_names())
sheet = workbook.sheets()[0]
print(sheet.nrows)
print('row_values(num):', len(sheet.row_values(5)), sheet.row_values(5))
print('row(num):', len(sheet.row(4)), sheet.row(4))
# 第5和第6列（index4,5）两行都是标题行，所以合并到一起
title_rows = zip(sheet.row_values(4), sheet.row_values(5))
# strip 去掉字符串开头和末尾的空格
titles = [(t[0] + ' ' + t[1]).strip() for t in title_rows]
print(titles)
# 第7到第114行是有用的数据，提取出来
country_rows = [sheet.row_values(i) for i in range(6, 114)]
print('country_rows:', country_rows)

from xlrd.sheet import ctype_text
import agate

text_type = agate.Text()
number_type = agate.Number()
boolean_type = agate.Boolean()
date_type = agate.Date()

example_row = sheet.row(6)
print('example_row:', example_row)
# check the type of the cell
print('example_row(ctype):', example_row[1].ctype)
# check the value of the cell
print('example_row(value):', example_row[1].value)
print('ctype_text: ', type(ctype_text), ctype_text)

types = []
for t in example_row:
    # 构建列表，包含数据集中所有的类型
    value_type = ctype_text[t.ctype]
    if value_type == 'text':
        types.append(text_type)
    elif value_type == 'number':
        types.append(number_type)
    elif value_type == 'xldate':
        types.append(date_type)
    else:
        # 根据agate的建议，未知的类型使用text类型
        types.append(text_type)
# print(types)


def remove_bad_chars(val):
    if val == '-':
        return None
    return val


def get_new_array(old_array, function_to_clean):
    """
    use function_to_clean to clear data in old_array
    :param old_array:
    :param function_to_clean:
    :return: cleaned data
    """
    new_arr = []
    for row in old_array:
        # remove all '-' chars in list
        cleared_row = [function_to_clean(ret) for ret in row]
        new_arr.append(cleared_row)
    return new_arr


cleared_rows = get_new_array(country_rows, remove_bad_chars)
table = agate.Table(cleared_rows, titles, types)
print(table.column_names)
most_egregious = table.order_by('Female', reverse=True).limit(10)
for data in most_egregious.rows:
    print('{}: {}%'.format(data['Countries and areas'], data['Female']))


