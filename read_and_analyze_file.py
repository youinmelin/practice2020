#Write a program that prompts the user to enter a text file, reads words from the file, and displays all the non-duplicate words in ascending order.
path = 'files'
file_name = 'Integration tests.txt'
words_dict = {}
words_set=set()
with open('%s\\%s'%(path,file_name),'r') as f:
    for content in f.readlines():
        words_list = content.split()
#        print(words_list)
        for word in words_list:
            words_dict[word]=words_dict.get(word,0)+1
            words_set.add(word)
#print(words_dict)
words_list = list(words_set)
words_list.sort()
print(words_list)

