# count the number of words in a sentence.
import pytest

sentences_list = [
['either express or implied. Neither the author, nor Packt Publishing or its dealers and distributors,', 15],
['Packt Publishing has endeavored to provide trademark information about all of the companies and products mentioned in this book', 19],
['Commissioning Editor: Kunal Chaudhari Acquisition Editor:?Siddharth Mandal', 8],
['Did you know that Packt offers eBook versions of every book published,', 12],
['All rights reserved.', 3],
['This book is for anyone who wants to start using pytest to improve their testing skills in their daily workflow.', 20]
]

@pytest.fixture(params = sentences_list)
def sentence(request):
    return request.param

def count(sentence_str):
    sentence_list = sentence_str.split()
    count_items={}
    count_num = 0
    for word in sentence_list:
        if word[-1] in ',.?:;!':
            word = word[0:-1]
        count_items[word] = count_items.get(word,0)+1
        count_num += 1
    return count_num

def test_sent(sentence):
    num = count(sentence[0])
    assert num == sentence[1]
