# X = placed and hit ships
# ' ' for avialable space
# "-" = missed shot

from random import randint

# Creates the player and computers board sizes
PLAYER_BOARD = [[' '] * 8 for x in range(8)]
COMPUTER_BOARD = [[' '] * 8 for x in range(8)]

# Converts letters to numbers
letter_to_number = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

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
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'

def ship_position():
    """
    Input field to enter ship row and column
    Checks if the input is valid
    Returns row as an integer and removes 1 for indexing, converts letters to numbers
    """
    row = input('Please enter a ship row 1-8')
    while row not in '12345678':
        print('Please enter a valid row number')
        row = input('Please enter a ship row 1-8')

    column = input('Please enter a ship column A-H')
    while column not in 'ABCDEFGH':
        print('Please enter a valid ship column')
        column = input('Please enter a ship column A-H').upper()
    return int(row) - 1, letter_to_number[column]