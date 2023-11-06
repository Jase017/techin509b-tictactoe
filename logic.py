# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
def make_empty_board():
    return [['', '', ''],
            ['', '', ''],
            ['', '', '']]


def input_move(board):
    while True:
        move = input("input row and col (0-2) separated by space or 'q' to quit: ")
        if move.lower() == 'q':
            return 'q', 'q'
        try:
            x, y = map(int, move.split())
            if 0 <= x <= 2 and 0 <= y <= 2 and board[x][y] == '':
                return x, y
            else:
                print('Invalid input, please try again.')
        except ValueError:
            print('Invalid input, please try again.')


def other_player(now):
    if now == 'X':
        next = 'O'
    else:
        next = 'X'
    return next


def get_winner(board):
    for i in range(0, 3):
        if board[i][0] != '' and board[i][0] == board[i][1] == board[i][2]:
            print(board[i][0], ' Won')
            return board[i][0]

    for i in range(0, 3):
        if board[0][i] != '' and board[0][i] == board[1][i] == board[2][i]:
            print(board[0][i], ' Won')
            return board[0][i]

    if board[1][1] != '' and (board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]):
        print(board[1][1], ' Won')
        return board[1][1]
    for row in board:
        for col in row:
            if col == '':
                return ''
    print('Draw')
    return 'Draw'

				return ''
	print('Draw')
	return 'Draw'
