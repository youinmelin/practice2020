''' Given an Input File Which Contains a List of Names?and
Phone Numbers Separated by Spaces in the Following Format:
Alex 80-23425525
Emily 322-56775342
Grace 20-24564555
Anna 194-49611659
Phone Number Contains a 3- or 2-Digit Area Code and a Hyphen Followed By an
8-Digit Number.
Find All Names Having Phone Numbers with a 3-Digit Area Code Using Regular
Expressions.'''

import re
tel_list=['Alex 80-23425525', 'Emily 322-56775342', 'Grace 20-24564555', 'Anna 194-49611659']
re_str = r'\d{3}-\d{8}'
for num in tel_list:
    ret = re.search(re_str,num)
    if ret:
        # print (ret.group()) 
        print(num,'yes')
    else:
        print (num,'no')
