# Merge all the txt files where are in the subpath into one txt file. And save the new txt file in current path.

import os
walk_files = os.walk('.')
files_list = []
txt_files_list = []
# add all files name in files_list
for root,path,files in walk_files:
    for filename in files:
        files_list.append(root+'\\'+filename)
#print(files_list)
# remain txt files in the list
for files_name in files_list:
    if files_name[-3:] == 'srt':
        txt_files_list.append(files_name)
print(txt_files_list)
new_file_name='new_file.txt'
with open(new_file_name,'w') as new_f:
    for txt_file_name in txt_files_list:
        with open (txt_file_name,'r') as txt_f:
            txt_content=txt_f.readlines()
            new_f.write('\n')
            new_f.write(txt_file_name)
            for txt_row in txt_content:
                new_f.write('\n')
                new_f.write(txt_row)
