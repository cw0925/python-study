import re
pattern = 'yue'
string = 'http://yum..com'
result = re.search(pattern,string)
print(result)