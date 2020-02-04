# count the number of times each word appears in a sentence

def main():
    sentence = input('please input a sentence:')
    sentence_list = sentence.split()
    count_items={}
    for word in sentence_list:
        count_items[word] = count_items.get(word,0)+1
    print (count_items)

if __name__ == '__main__':
    main()
    
