# 列表生成式
import random

n = 10
a_list = [random.randrange(1, 100) for x in range(n)]

print(f'a_list comprehands {len(a_list)} random numbers: {a_list}')

b_list = [x for x in a_list if x % 2 == 0]
print(f'... and b_list has {len(b_list)} even numbers: {b_list}')

# 元组Tuple
a = (1,)
b = 2,
print(a, b)

# 集合Set与字典dict
s = set()  # 这是集合set的创建方法
sc = {chr(x) for x in range(90, 95)}  # 列表生成式创建set
d = {}  # 这样是字典dict的创建方法

print(sc)


phonebook1 = {'ann': 6575, 'bob': 8982, 'joe': 2598, 'zoe': 1225, 'ann': 6585}
print(phonebook1)
phonebook2 = {'john': 9876, 'mike': 5603, 'stan': 6898, 'eric': 7898}
phonebook1.update(phonebook2)

l = len(phonebook1)
mx = max(phonebook1)
mn = min(phonebook1)
lt = list(phonebook1)
tp = tuple(phonebook1)
st = set(phonebook1)
sd = sorted(phonebook1)
st = sorted(phonebook1, reverse=True)

print(mn)
