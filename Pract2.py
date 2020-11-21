from random import randint
from datetime import datetime
# lambda
# 1
lst = [(randint(0,9), randint(0,9)) for i in range(6)]

def sort_lst1(lst):
    return sorted(lst, key=lambda x: x[1])

print(sort_lst1(lst))
# 2
lst = ['привет', 'a', 'кто']
def sort_lst2(lst):
    return sorted(lst, key=lambda x: len(x), reverse=True)

# 3
def incrementer(start_val, modulator, productor,addition):
    r_var = start_val
    m = modulator
    a = productor
    c = addition
    def inner():
        nonlocal r_var
        nonlocal m
        nonlocal a
        nonlocal c
        r_var = (a * r_var + c) % m
        return r_var
    return inner
test_func = incrementer(7, 10,7,7)

# print(test_func())
# print(test_func())
# print(test_func())
# print(test_func())
# print(test_func())
# print(test_func())
# print(test_func())
# print(test_func())

# Generator
# 1, 2
def rand_progression(start_val, modulator, productor,addition):
    r_var = start_val
    while True:
        yield r_var
        r_var = (productor * r_var + addition) % modulator


r_p = rand_progression(7, 10,7,7)
# print(next(r_p))
# print(next(r_p))
# print(next(r_p))
# print(next(r_p))

# 3
def rand_progression2(start_val, modulator, productor):
    r_var = start_val
    while True:
        addition = (yield)
        r_var = (productor * r_var + addition) % modulator
        print(r_var)
        yield r_var

r_p2 = rand_progression2(7, 10,7)
next(r_p2)

for i in range(10):
    r_p2.send(7)
    print(i)


# decorators
# 1

def test_foo(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result


def decorator_func1(func):
    test_foo.counter = 0
    test_foo.were_called = []
    def wrapper(n):
        start_time = datetime.now()
        a = func(n)
        fin_time = datetime.now()
        print('it took ' + str(fin_time - start_time))
        test_foo.counter += 1
        test_foo.were_called.append(datetime.now())
        print(f"job was done {test_foo.counter} time(s)")
        return a
    return wrapper


decorated_func_1 = decorator_func1(test_foo)
# decorated_func_1.counter = 0
# decorated_func_1.were_called = []
# decorator_func1.cache = {}
print(decorated_func_1(4))
print(decorated_func_1(5))
decorated_func_1(1000000)
print(test_foo.were_called)


