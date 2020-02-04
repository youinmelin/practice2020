# to find all five characters long word in a string.
import re

with open (r'.\files\Integration tests.txt') as f:
    string = f.read()
pattern_str = r'\s\w{5}\s'
result = re.findall(pattern_str,string)
#result=result_re.groups()
print(result)
