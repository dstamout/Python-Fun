# Helper that prints the 2D array
def print2D(array):
    for r in array:
        for c in r:
            print(c, end = " ")
        print()

# Modifies board for X turn, checks bounds
def modify2DX(array, r, c):
    if not 0 <= r <= 2 or not 0 <= c <= 2 or array[r][c] != "-":
        raise ValueError
    array[r][c] = "X"
    print2D(array)

# Modifies board for O turn, checks bounds
def modify2DO(array, r, c):
    if not 0 <= r <= 2 or not 0 <= c <= 2 or array[r][c] != "-":
        raise ValueError
    array[r][c] = "O"
    print2D(array)

# Checks if board is filled
def filled(array):
    filled = True
    for r in array:
        if "-" in r:
            filled = False
            break
    return filled

# Checks win for all rows
def checkRow(array):
    for r in array:
        if len(set(r)) == 1:
            return r[0]
    return 0

# Checks win for all columns
def checkCol(array):
    for i in range(0, 3):
        if len(set([array[0][i], array[1][i], array[2][i]])) == 1:
            return array[i][0]
    return 0

# Checks win for all diagonals
def checkDiag(array):
    if len(set([array[0][0], array[1][1], array[2][2]])) == 1:
        return array[0][0]
    if len(set([array[0][2], array[1][1], array[2][0]])) == 1:
        return array[2][0]
    return 0

# Checks for any winner
def checkWinner(array):
    if checkCol(array) == "X" or checkRow(array) == "X" or checkDiag(array) == "X":
        return "\nX Wins!"
    if checkCol(array) == "O" or checkRow(array) == "O" or checkDiag(array) == "O":
        return "\nO Wins!"
    return 0

# Initial values
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
rowX, colX, rowO, colO = -1, -1, -1, -1

# Initial output
print2D(board)
print("Welcome to Tic-Tac-Toe! Get 3 in a row, column, or diagonal, to win! Rows and columns start at 0.")

# Game loop
while True:
    # X input loop
    while True:
        # Except invalid input
        try:
            rowX = int(input("\nX is up. \nPlease input what row X would like to play: "))
            colX = int(input("\nPlease input what column X would like to play: "))
            modify2DX(board, rowX, colX)
            break
        except ValueError:
            print("\nInvalid input. Inputs must be an integer within bounds 0 - 2 and located at a space unfilled.")
            print2D(board)

    # If board filled, break
    if filled(board):
        break

    # If winner exists, print and break
    if checkWinner(board) != 0:
        print(checkWinner(board))
        break

    # O input loop
    while True:
        # Except invalid input
        try:
            rowO = int(input("\nO is next. \nPlease input what row O would like to play: "))
            colO = int(input("\nPlease input what column O would like to play: "))
            modify2DO(board, rowO, colO)
            break
        except ValueError:
            print("\nInvalid input. Input must be an integer within bounds 0 - 2 and located at a space unfilled.")
            print2D(board)

    # If winner exists, print and break
    if checkWinner(board) != 0:
        print(checkWinner(board))
        break

exit()