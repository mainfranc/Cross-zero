from random import randint

# lambda
# Создать список, в котором каждый элемент – кортеж из двух чисел. Отсортировать данный список по убыванию вторых элементов кортежей.​
#
# Отсортируйте список слов по убыванию длины слова.​
#
# Реализуйте пример замыкания (например, «инкрементатор»)
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

# Coroutine
def rand_progression2(start_val, modulator, productor):
    r_var = start_val
    while True:
        addition = (yield)
        r_var = (productor * r_var + addition) % modulator
        print(r_var)

r_p2 = rand_progression2(7, 10,7)
next(r_p2)

for i in range(10):
    r_p2.send(7)


# decorators
# 1
test_foo_counter = 0
def test_foo():
    return randint(1, 8) ** 2


def decorator_func1(func):
    global test_foo_counter

    def wrapper():
        global test_foo_counter
        a = func()
        test_foo_counter += 1
        print(f"job was done {test_foo_counter} time(s)")
        return a
    return wrapper


decorated_func_1 = decorator_func1(test_foo)
print(decorated_func_1())
print(decorated_func_1())


