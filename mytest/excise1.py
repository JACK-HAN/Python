import random

# 查看随机数是奇数还是偶数
r = random.randrange(1, stop=1000, step=1, _int=int)
print('r is:' + str(r))
if r % 2 == 0:
    print(r, 'is even')
else:
    print(r, 'is odd')

# 找出10以内的奇数
for i in range(10):
    if i % 2 != 0:
        print(i)

# 找出100以内的质数
for i in range(2, 100):
    if i == 2:
        print(i)
        continue
    for n in range(2, i):
        if i % n == 0:
            break
    else:
        print(i)

# 找出100以内的质数,改进做法
for i in range(2, 100):
    if i == 2:
        print(i)
        continue
    for n in range(2, int(i**0.5) + 1):
        if i % n == 0:
            break
    else:
        print(i)

# 对一个功能进行封装，以便以后多次调用，这就需要函数


def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    for m in range(2, int(n**0.5) + 1):
        if n % m == 0:
            return False
    else:
        return True


e = is_prime(r)
print(e)
