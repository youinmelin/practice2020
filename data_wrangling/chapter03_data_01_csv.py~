import csv
'''
 read csv file and print the data
'''


path = "book/data-wrangling/data/chp3/"
filename = "data-text.csv"
csvfile = open(path + filename, 'r')
# save data as list
reader = csv.reader(csvfile)
# print(type(reader))
for i,row_list in enumerate(reader):
    if i < 5:
        print(i,row_list)
    else:
        break

# save data as dict 
reader = csv.DictReader(csvfile)
print(type(reader))
for i,row_dict in enumerate(reader):
    if i < 5:
        print(type(row_dict))
        print(i,row_dict)
    else:
        break

