'''
Building a Tic-Tac-Toe game
'''
import random

def tictactoe():
    '''
    This function will play a game of tic-tac-toe
    '''
    board = [' '] * 10
    player = 'X'
    computer = 'O'
    winner = None
    while winner is None:
        display_board(board)
        player_move(board, player)
        winner = check_winner(board, player)
        if winner is None:
            computer_move(board, computer)
            winner = check_winner(board, computer)
    display_board(board)
    if winner is None:
        print('Tie game!')
    else:
        print(winner, 'wins!')

def display_board(board):
    '''
    This function will display the board
    '''
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def player_move(board, player):
    '''
    This function will get the player's move
    '''
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(move)):
        move = input('What is your next move? (1-9) ')
    board[int(move)] = player

def space_check(board, move):
    '''
    This function will check if the space is empty
    '''
    return board[move] == ' '

def check_winner(board, player):
    '''
    This function will check if the player has won
    '''
    return ((board[1] == player and board[2] == player and board[3] == player) or # across the top
    (board[4] == player and board[5] == player and board[6] == player) or # across the middle
    (board[7] == player and board[8] == player and board[9] == player) or # across the bottom
    (board[7] == player and board[4] == player and board[1] == player) or # down the middle
    (board[8] == player and board[5] == player and board[2] == player) or # down the middle
    (board[9] == player and board[6] == player and board[3] == player) or # down the right side
    (board[7] == player and board[5] == player and board[3] == player) or # diagonal
    (board[9] == player and board[5] == player and board[1] == player)) # diagonal

def computer_move(board, computer):
    '''
    This function will get the computer's move
    '''
    move = random.randint(1, 9)
    while not space_check(board, move):
        move = random.randint(1, 9)
    board[move] = computer

def play_again():
    '''
    This function will ask the player if they want to play again
    '''
    choice = input('Do you want to play again? (y/n) ')
    return choice == 'y'

def main():
    '''
    This function will run the game
    '''
    while True:
        tictactoe()
        if not play_again():
            break

main()
