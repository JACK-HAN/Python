# 一个打开的文件只能读取一次，不能被多种方法多次读取
import re
filename = 'excise16.py'
with open(filename) as f:
    content = f.readlines()
    # content2 = f2.readline()
    # content3 = f3.read()
pttn = r'[0-9]'
regx = re.compile(pttn)
for t in content:
    if len(re.findall(regx, t)) != 0:
        print(t, end='')
# print(content)
# print(content2)
# print(content2)
