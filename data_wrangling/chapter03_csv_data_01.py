import csv

path = "data_source/"
filename = "students.csv"
csvfile = open(path + filename, 'r')
reader = csv.reader(csvfile)
// print(type(reader))
for row_list in reader:
    print(row_list)
