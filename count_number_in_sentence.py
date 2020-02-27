# count the number of times each word appears in a sentence

def main():
    sentence = input('please input a sentence:')
    sentence_list = sentence.split()
    count_items={}
    count_num = 0
    for word in sentence_list:
        if word[-1] in ',.?:;!':
            print(word)
            word = word[0:-1]
        count_items[word] = count_items.get(word,0)+1
        count_num += 1
    print (count_num,count_items)

if __name__ == '__main__':
    main()
    
