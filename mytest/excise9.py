# 匿名函数 lambda
def add(y):
  print(y)
  return lambda x: x * y


f = add(2)
f0 = f(3)
print(f0)

a_list = [1, 2, 3, 4]
b_list = list(map(lambda n: n * 2, a_list))
print(b_list)


phonebook = [
    {
        'name': 'john',
        'phone': 9876
    },
    {
        'name': 'mike',
        'phone': 5603
    },
    {
        'name': 'stan',
        'phone': 6898
    },
    {
        'name': 'eric',
        'phone': 7898
    }
]

name_list = list(map(lambda n: n['name'], phonebook))
phone_list = list(map(lambda p: p['phone'], phonebook))
print(name_list)
print(phone_list)

pairs = [(1, 'one', 3), (2, 'two', 2), (3, 'three', 1), (4, 'four', 0)]
pairs.sort(key=lambda p: p[2])
print(pairs)
