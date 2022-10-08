from random import randint

# Creates the player and computers board sizes
PLAYER_BOARD = [[" "] * 5 for x in range(5)]
COMPUTER_BOARD = [[" "] * 5 for i in range(5)]

# Converts letters to numbers
letter_to_number = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3,
    'E': 4
}


def print_board(board):
    """
    Prints the player and computer board to the terminal
    """
    print('  A B C D E')
    print('  ---------')
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
        ship_row, ship_column = randint(0,4), randint(0,4)     
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0,4), randint(0,4)
        board[ship_row][ship_column] = "X"


def ship_position():
    """
    Input field to enter ship row and column
    Checks if the input is valid
    Returns row as an integer and removes 1 for indexing, converts letters to numbers
    """
    row = input("Please enter a ship row 1-5: \n")
    while row not in '12345':
        print("Please enter a valid row number: \n")
        row = input("Please enter a ship row 1-5: \n")

    column = input("Please enter a ship column A-E: \n")
    while column not in "ABCDE":
        print("Please enter a valid ship column: \n")
        column = input("Please enter a ship column A-E: \n").upper()
    return int(row) - 1, letter_to_number[column]


def hit_ships(board):
    """
    Loops through the board and checks for "X"
    If "X" exists increase count(score) by 1
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


# Spawns board, sets the turns to 10
# Displays messages in relation to what input data is recieved from the player
def main():
    if __name__ == "__main__":
        spawn_ship(PLAYER_BOARD)
        turns = 10
        while turns > 0:
            print("Welcome to Battleship!")
            print_board(COMPUTER_BOARD)
            row, column = ship_position()
            if COMPUTER_BOARD[row][column] == "-":
                print("You already guessed that")
            elif PLAYER_BOARD[row][column] == "X":
                print("Congrats! You hit a ship!")
                COMPUTER_BOARD[row][column] = "X"
                turns -= 1
            else:
                print("Sorry you missed!")
                COMPUTER_BOARD[row][column] = "-"
                turns -= 1
            if hit_ships(COMPUTER_BOARD) == 5:
                print("Congratulations, you have sunk all the ships!")
                break
            print("You have " + str(turns) + " turns remaining")
            if turns == 0:
                print("You ran out of turns, Game Over!")            
main()