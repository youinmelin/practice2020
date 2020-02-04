# remove all leading zeros' from an IP address

import re

ip_pattern = r'(\d{1,3}.){3}\d{1,3}'
ip_list = ['002.1.1.111','01,01,01,011','090,0,0,1','999,,001,100']
for ip in ip_list:
    re_result = re.match(ip_pattern,ip)
    if re_result:
        result = re_result.group()
        for _ in range(2):
            if result[0] == '0':
                result = result[1:]
    else:
        result ='no match'
    print (ip,":",result)
