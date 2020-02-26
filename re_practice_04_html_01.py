# to find files in the html string
import re
import requests

url = 'https://www.sina.com.cn'
url = 'https://www.hlgnet.com'

text = requests.get(url).text
# print(text)
re_str = r'src = "(.*?\.jpg)"'
re_str = r'https:.+\.jpg' 
re_str = r'[jpg|gif]'
file_name_list = re.findall(re_str, text)
print(file_name_list)
