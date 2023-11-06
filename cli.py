from logic import make_empty_board
from logic import input_move
from logic import get_winner
from logic import other_player
import logging

logging.basicConfig(
    filename='log/msg.log.',
    level=logging.INFO
)

def play_game():
    board = make_empty_board()
    winner = ''
    player = 'X'

    for row in board:
        print(row)

    while winner == '':
        print('Next turn: ', player)
        x, y = input_move(board)
        if x == 'q' and y == 'q':
            return
        board[x][y] = player
        for row in board:
            print(row)
        winner = get_winner(board) 
        logging.info('You win the game.')
        player = other_player(player)


if __name__ == '__main__':
    while True:
        play_game()
        play_again = input('Do you want to play again? (Y/N): ')
        if play_again.upper() != 'Y':
            break
