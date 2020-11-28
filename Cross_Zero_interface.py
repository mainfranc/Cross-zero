import numpy as np
import tkinter

count_moves = 1
play = True
winner = 0
field = np.ndarray(2)


def print_field(field, root, fieldsize):
    global winner
    for row in range(fieldsize):
        for col in range(fieldsize):
            button = tkinter.Button(root, text=' XO'[int(field[row][col])], width=4, height=2,
                            font=('arial', 24, 'bold'),
                            state='normal' if play else 'disabled',
                            command=lambda row=row, col=col: on_click(field, row, col, fieldsize, root))
            button.grid(row=row, column=col, sticky='nsew')

    lab = tkinter.Label(width=20, bg='black', fg='white')
    lab.grid(row=int(fieldsize), column=0, columnspan=fieldsize, sticky='nsew')

    new_button = tkinter.Button(root, text='new game', command=lambda: new_game(root, fieldsize))
    new_button.grid(row=fieldsize + 1, column=0, columnspan=fieldsize + 1, sticky='nsew')
    if not play:
        lab['text'] = f'{" XO"[winner]} has won. \n Press new game to start the new game'
    root.mainloop()


def empty_field(fieldsize):
    return np.zeros((fieldsize, fieldsize))


def game(sc, root):
    global field
    fieldsize = sc.get()
    root.destroy()
    root = tkinter.Tk()
    root.title('X-O')
    won_value = 0
    field = empty_field(fieldsize)
    print_field(field, root, fieldsize)


def new_game(root, fieldsize):
    global field
    global count_moves
    global play
    count_moves = 1
    field = empty_field(fieldsize)
    play = True
    won_value = 0
    print_field(field, root, fieldsize)


def on_click(field, x, y, fieldsize, root):
    global count_moves
    global play
    global winner
    val_lst = ['', 'X', 'O']
    val = 1 if count_moves % 2 != 0 else 2
    if field[x][y] == 0:
        count_moves += 1
        field[x][y] = val
    play = not check_won(field, count_moves, fieldsize)
    if not play:
        if count_moves == fieldsize ** 2:
            won_value = 0
        else:
            won_value = val
        winner = won_value
    print_field(field, root, fieldsize)



def check_line(lst):
    return len(set(lst)) == 1 and lst[0] != 0


def check_won(field, count_moves, fieldsize):
    if count_moves > fieldsize ** 2: return True
    for i in field:
        if check_line(i):
            return True
    for i in range(len(field[1])):
        if check_line(field[:, i]):
            return True
    if check_line(np.diagonal(field)):
        return True
    if check_line(np.diagonal(field[:,::-1])):
        return True
    return False


def input_val(field, val, x, y, f_s):
    data_put = False
    while not data_put:
        if field[x][y] == 0:
            data_put = True
        else:
            print('please, input the correct coordinates')
            x = int(input('input row num'))
            y = int(input('input column num'))
    return [val, x, y]

def main():
    root = tkinter.Tk()
    lab = tkinter.Label(root, width=40)
    lab['text'] = 'choose the field size'
    lab.pack()
    sc = tkinter.Scale(root, width=40, from_=2, to=10, orient='horizontal')
    sc.pack()
    start_button = tkinter.Button(text="Start Game", command=lambda: game(sc, root))
    start_button.pack()
    root.mainloop()
if __name__ == '__main__':
    main()
