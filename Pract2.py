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
def incrementer(start_val):
    r_var = start_val
    def inner():
        nonlocal r_var
        m = randint(2,5)
        a = randint(0,m + 5)
        c = randint(0,m + 5)
        r_var = (a * r_var + c) % m
        return r_var
    return inner
test_func = incrementer(2)

print(test_func())
print(test_func())
print(test_func())
print(test_func())
print(test_func())
print(test_func())
print(test_func())
print(test_func())
