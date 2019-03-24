# 正则表达式,也叫规则表达式
import re
str = 'The quick brown fox jumps over the lazy dog'
pttn = re.compile(r'\wo\w')
res = re.findall(pttn, str)
print(res)


pttn_2 = r'beg[iau]ns?'
with open('regex-target-text-sample.txt', 'r') as f:
    str_2 = f.read()
res_2 = re.findall(pttn_2, str_2)
print(res_2)
