def print2D(array):
    for r in array:
        for c in r:
            print(c, end = " ")
        print()

def modify2DX(array, r, c):
    array[r][c] = "X"
    print2D(array)

def modify2DO(array, r, c):
    array[r][c] = "O"
    print2D(array)

def filled(array):
    filled = False
    for r in array:
        if "-" not in r:
            filled = True
        else:
            filled = False
    return filled

def checkRow(array):
    for r in array:
        if len(set(r)) == 1:
            return array[0]
    return 0

def checkCol(array):
    for i in range(0, 3):
        if len(set(list(array[0][i], array[1][i], array[2][i]))) == 1:
            return array[i][0]
    return 0

def checkDiag(array):
    pass

def checkWinner(array):
    pass

board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
print2D(board)
print("Welcome to Tic-Tac-Toe! Rows and columns start at 1.")

while True:
    rowX = input("\nX is up. \nPlease input what row X would like to play: ")
    colX = input("\nPlease input what column X would like to play: ")
    modify2DX(board, int(rowX) - 1, int(colX) - 1)

    if filled(board):
        break

    rowO = input("\nO is next. \nPlease input what row O would like to play: ")
    colO = input("\nPlease input what column O would like to play: ")
    modify2DO(board, int(rowO) - 1, int(colO) - 1)

exit()