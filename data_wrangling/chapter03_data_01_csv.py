import csv
'''
 read csv file and print the data
'''


path = "book/data/chp3/"
filename = "data-text.csv"
path = 'book/data/unicef/'
filename_data = 'mn.csv'
filename = 'mn_headers.csv'
csv_file = open(path + filename, 'r')
# save data as list
reader = csv.reader(csv_file)
# print(type(reader))
for i,row_list in enumerate(reader):
    if i < 5:
        print(i,row_list)
    else:
        break

# save data as dict 
reader = csv.DictReader(csv_file)
print(type(reader))
for i,row_dict in enumerate(reader):
    if i < 5:
        print(type(row_dict))
        print(i,row_dict)
    else:
        break

