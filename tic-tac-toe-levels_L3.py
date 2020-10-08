print()

# L1 How can we place a letter at the empty bottom right position

data = [
    ['O', 'X', 'O'],
    ['X', 'X', 'O'],
    ['X', 'O', '.']
]


# L2 How can we make the print board code above into a print board function we can re-use

# L3 How can we combine the data and the function into a Board class?


class Board:

    # constructor
    def __init__(self):
        self.data = [
            ['O', 'X', 'O'],
            ['X', 'X', 'O'],
            ['X', 'O', '.']
        ]

    # change mark
    def change(self, row, col, mark):
        self.row = row - 1
        self.col = col - 1
        self.mark = mark

        self.data[self.row][self.col] = self.mark

    # print new board
    def print(self):
        for line in self.data:
            print(line)


new_board = Board()
new_board.change(1, 2, '.')
new_board.change(1, 1, '.')
new_board.print()


# L4 How can we say if X, O, or no-one has won?  Can we