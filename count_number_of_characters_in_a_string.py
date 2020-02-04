# count the number of characters in a  string using dictionaries
# display the keys and their values in alphabetical order
import string
yourinput = input('please input a string:')
count_num = {}
for character in yourinput:
    count_num[character] = count_num.get(character,0)+1
print(count_num)
for abc in string.ascii_lowercase:
    if count_num.get(abc):
        print (abc,count_num[abc])
