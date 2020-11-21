import random
import itertools

# Map, Filter
# 1
def even_odd_filtered_squares(in_tpl):
    def sqr_func(n):
        return n ** 2

    def is_even(n):
        return True if n % 2 == 0 else False

    return map(sqr_func, filter(is_even, in_tpl))


test_tpl = (2, 3, 4, 7, 11, 12, 24, 0, 22,13)
for i in even_odd_filtered_squares(test_tpl):
    print(i)


# 2
test_str = 'всем привет кого не видел'
test_tpl = (2, 3, 4, 7)
print(test_tpl)

def string_by_indexes(in_str, num_tpl):
    result = ""
    def return_letter(in_str, n):
        return in_str[n]

    # for i in [in_str[i] for i in num_tpl]:
    #     result += i
    for i in map(return_letter, [in_str for _ in range(len(num_tpl))], num_tpl):
        result += i
    return result


print(string_by_indexes(test_str, test_tpl))


# Iterators
def total_capitalization(in_str):
    return in_str[0].upper() + ''.join([in_str[i].upper() if in_str[i - 1] == '.' else in_str[i].lower() for i in range(1, len(in_str))])


test_str = "пРИВЕТ.этО ТеСтовое ПреДлОжение.оно НЕ имеет ЗНаЧения"
print(total_capitalization(test_str))
