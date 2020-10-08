print()

# L1 How can we place a letter at the empty bottom right position

data = [
    ['O', 'X', 'O'],
    ['X', 'X', 'O'],
    ['X', 'O', '.']
]

# L2 How can we make the print board code above into a print board function we can re-use


def change_board(pos1 = -1, pos2 = -1, mark = 'X'):

    data[pos1][pos2] = mark
    for line in data:
        print(line)
    return data


changed = change_board(-1, 1, 'X')




# L3 How can we combine the data and the function into a Board class?



# L4 How can we say if X, O, or no-one has won?  Can we