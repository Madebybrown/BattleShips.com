# X = placed and hit ships
# ' ' for avialable space
# "-" = missed shot

from random import randint

# Creates the player and computers board sizes
PLAYER_BOARD = [[' '] * 10 for x in range(10)]
COMPUTER_BOARD = [[' '] * 10 for x in range(10)]

# Converts letters to numbers
letter_to_number = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,}

def print_board(board):
    """
    Print the players and computers board to the terminal
    """
    print('     A B C D E F G H I J')
    print('     -------------------')
    row_num = 1

    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1

def spawn_ship(board):
    """
    Randomly creates the ships on the board
    Checks if row and column is already taken (If "X" is already placed)
    Otherwise place "X" on the board
    """
    
    for ship in range(5):
        ship_row, ship_column = randint(0, 9), randint(0, 9)
        
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 9), randint(0, 9)
        board[ship_row][ship_column] = 'X'