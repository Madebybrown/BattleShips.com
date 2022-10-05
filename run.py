# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Creates the player and computers board sizes
PLAYER_BOARD = [[' '] * 10 for x in range(10)]
COMPUTER_BOARD = [[' '] * 10 for x in range(10)]

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