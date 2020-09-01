from csv import DictReader
import pprint
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

path = 'book/data/unicef/'
filename_data = 'mn.csv'
filename_header = 'mn_headers.csv'
data_file = open(path + filename_data, 'rt')
header_file = open(path + filename_header, "r")

header_rdr = DictReader(header_file)
data_rdr = DictReader(data_file)
# print(type(header_rdr.reader))
# pprint.pprint(header_rdr)
header_list = []
data_list = []

# read header
for i, row in enumerate(header_rdr):
    if i > 1090:
        break
    # print(row)
    header_list.append(row)
print(len(header_list))
# header_list = [data_list for d in header_rdr]
print(header_list[:5])
# read data
for i, row in enumerate(data_rdr):
    if i > 50:
        break
    # print(row)
    data_list.append(row)
print(len(data_list))
pprint.pprint(data_list[:2])

# substitute old header for new headers
data_new_list = []
    # loop data_list
for data_dict in data_list:
    new_row_dict = {}
    # loop dict in data_list
    for data_key_str, data_value_str in data_dict.items():
        # print(data_key_str,data_value_str)
    # loop header_list
        for header_dict in header_list:
    # loop dict in header_list
            if header_dict['Name'] == data_key_str:
    # judge same name between two dicts
                # print('%s = %s' % (data_key_str, header_dict['Label']))
                new_row_dict[header_dict['Label']] = data_value_str
    data_new_list.append(new_row_dict)
print(data_new_list)
