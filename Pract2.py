from random import randint

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
def increment():
    r_var = randint(0,2)
    def inner():
        nonlocal r_var
        r_var += 1
        print('print ' + r_var)
    return inner
