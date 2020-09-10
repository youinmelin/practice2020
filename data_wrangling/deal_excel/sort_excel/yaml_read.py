# coding=utf-8
import yaml
import os


def read_keywords_from_yaml():
    filename = os.getcwd() + '\\data_source\\key_words.yml'
    # filename =os.getcwd() + '\\key_words.yml'
    with open(filename, 'rb') as f:
        s = f.read()
    return yaml.load(s, Loader=yaml.FullLoader)
