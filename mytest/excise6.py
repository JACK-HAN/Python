# 文件操作
import os

f = open('test_file.txt', 'w')
f.write('which is always equal to the length of the string')
f.close()

f = open('test_file.txt', 'r')
r = f.read()
print(r)
f.close()


# if os.path.exists(f.name):
#     os.remove(f.name)
#     print('the file is deleted')
# else:
#     print('no file exist')

with open('test_file.txt', 'w') as f:
    f.write('which is always equal to\n the length of the string')

with open('test_file.txt', 'r') as f:
    for line in f.readlines():
        print(line)
