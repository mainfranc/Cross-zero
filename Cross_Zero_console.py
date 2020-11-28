import numpy as np


def print_field(field):
    for cur_row in field:
        print_row = ""
        check_string = "_XO"
        for j in cur_row:
            print_row += (check_string[int(j)] + " ")
        print(print_row)


def empty_field(fieldsize=3):
    return np.zeros((fieldsize, fieldsize))


def game(field, play, fieldsize):
    won_value = 0  ### тут у меня дальше был мисспринт - функция должна возвращать либо, что победителя нет, либо 1 или 2 - индекс для Х и О
    count_moves = 0
    while not won_value:  ### заменил

        ret_val = count_moves % 2
        count_moves += 1
        field = next_move(field, count_moves, ret_val + 1, fieldsize)
        if check_won(field, count_moves, fieldsize):
            won_value = 0 if count_moves == fieldsize ** 2 else ret_val + 1 ### убрал дублирование кода, включил инлайн
            return won_value


def next_move(field, count_moves, val, fieldsize):
    val_lst = ['', 'cross', 'zero']
    x, y = input(("input row num for " + val_lst[val])), input(("input column num for " + val_lst[val]))
    lst_fi = input_val(field, val, x, y, fieldsize)
    field[lst_fi[1]][lst_fi[2]] = lst_fi[0]
    print_field(field)
    return field


def check_won(field, count_moves, fieldsize):
    ### заменил на проверку numpy.all - забыл про нее
    if count_moves == fieldsize ** 2: return True
    for i in field:
        if np.all(i) and len(set(i)) == 1:
            return True
    for i in range(len(field[1])):
        if np.all(field[:, i]) and len(set(field[:, i])) == 1:
            return True
    if np.all(np.diagonal(field)) and len(set(np.diagonal(field))) == 1:
        return True
    if np.all(np.diagonal(field[:,::-1])) and len(set(np.diagonal(field[:,::-1]))) == 1:
        return True
    return False


def input_val(field, val, x, y, f_s):
    while True:
        if not x.isdigit() and not y.isdigit():
            x = input('input row num')
            y = input('input column num')
        else:
            if (int(x) < 0 or int(x) > f_s - 1) or (int(y) < 0 or int(y) > f_s - 1):
                x = input('input row num')
                y = input('input column num')
            else:
                x = int(x)
                y = int(y)
                break

    data_put = False
    while not data_put:
        if field[x][y] == 0:
            data_put = True
        else:
            print('please, input the correct coordinates')
            x = int(input('input row num'))
            y = int(input('input column num'))
    return [val, x, y]


def main(fieldsize=3):
    play = True
    winner = 0
    while play:
        game_field = empty_field(fieldsize)
        print_field(game_field)
        winner = game(game_field, play, fieldsize)
        print('The winner is ' + '_XO'[int(winner)])
        answer = input("input y if you want to play once again").lower()
        play = True if answer == 'y' else False


if __name__ == '__main__':
    main(int(input()))
