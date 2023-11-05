from logic import make_empty_board
from logic import input_move
from logic import get_winner
from logic import other_player

if __name__ == '__main__':
    board = make_empty_board()
    winner = ''
    player = 'X'
    for row in board:
         print(row)
    while winner == '':
        print('Next turn: ', player)
        x, y = input_move(board)
        board[x][y] = player
        for row in board:
              print(row)
        winner = get_winner(board)
        player = other_player(player)
