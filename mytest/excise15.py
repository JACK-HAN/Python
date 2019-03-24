# 迭代器,是一个类
class Counter(object):
    """docstring for Counter"""

    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    # 必需的函数

    def __iter__(self):
        return self
    # 必需的函数

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            c = self.current
            self.current += 1
        return c

# 生成器，是一个函数


def counter(start, stop):
    while start <= stop:
        yield start  # 生成器的关键字yield
        start += 1
# 装饰器，对函数进行装饰，使其在执行前后分别做一些其他的事。操作符是@


def a_decorator(func):
    def wrapper():
        print('we can do sth,before calling func')
        func()
        print('... and we can do sth,after func is called...')
    return wrapper


@a_decorator
def a_func():
    print('Hi,i am a_func!')


a_func()


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_restult = original_result.upper()
        return modified_restult
    return wrapper


@uppercase
def an_output():
    return 'The quick brown fox jumps over the lazy dog.'


r = an_output()
print(r)
