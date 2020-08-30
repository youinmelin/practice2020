# coding:utf-8
import pprint
import io
import sys
'''
read txt files
'''

def read_txt(path, filename):
    openfile = open(path + filename,'r', encoding='UTF-8')
    # openfile = open(path + filename,'rb')
    country_line = total_line = False
    country_list = total_list = []
    for i,line in enumerate(openfile):
        # only print country name
        if country_line :
            line = clean_format(line)
            print ('country:%d %r %r' % (i, line, country_line))
            country_list.append(line)
        if total_line:
            line = clean_format(line)
            print ('total children worker number: %d %r %r' % (i, line, country_line))
            total_list.append(line)


        country_line = turn_on_off(line, country_line, 'and areas')
        total_line = turn_on_off(line,total_line, 'total')
    print('countrys:%d,total:%d'%(len(country_list),len(total_list)))
    pprint.pprint(country_list)
    pprint.pprint(total_list)
    data = dict(zip(country_list, total_list))
    # pprint.pprint(data)

def turn_on_off(line, status, start, previous_line = '', end = '\n'):
    '''
        check out weather lines start or end, start:status = False,
        end:status = True,
        return status->boolean
    '''
    if line.startswith(start):
        status = True
    elif status:
        if line == end:
            status = False
    return status

def clean_format(line):
    # line = line.strip('\n').strip()
    # line = line.replace('\xe2\x80\x93', '-')
    # line = line.replace('\xe2\x80\x99', '\'')
    return line

    


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
path = "book/data/chp5/"
filename = "en-final-table9.txt"
read_txt(path,filename)
