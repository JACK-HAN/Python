# 函数参数

# 单参数


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            print('point1')
            return True
    else:
        return False
    print('point2')
    return True


result = is_leap(360)
print(result)
print(300 % 400)


# 多参数
def fib_between(start, end):
    a, b = 0, 1
    while a < end:
        if a >= start:
            print(a, end=' ')
        a, b = b, a + b


fib_between(100, 10000)


def say_hi(greeting, *names):
    for name in names:
        print(f'{greeting},{name.capitalize()}!')
        print(type(name))


say_hi('hello', *['mike', 'john', 'zeo'])  # 注意不要把*丢了

# 多关键字参数


def say_hi_2(**names_greetings):
    for name, greeting in names_greetings.items():
        print(f'{greeting},{name}!')


say_hi_2(**{'mike': 'Hello', 'ann': 'Oh, my darling', 'john': 'Hi'})
