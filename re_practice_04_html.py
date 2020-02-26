# to find files in the html string
import re
import requests

url = 'https://www.sina.com.cn'
url = 'https://www.hlgnet.com'

text = requests.get(url).text
# print(text)
text_list = text.split('img')
yes = 0
no = 0
for text_str in text_list:
    # re_str = r'src = "(.*?\.jpg)"'
    re_str = r'https:.+\.jpg' 
    ret = re.search(re_str, text_str)
    if ret:
        print(ret.group())
        yes += 1
    else:
        #print(text_str)
        no += 1
print(len(text_list),yes,no)
# re_str = r'https:.+\.jpg' 
#file_name_list = re.findall(re_str, text)
#print(file_name_list)
