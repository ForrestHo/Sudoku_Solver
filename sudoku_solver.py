import numpy as np
board1 = np.array([
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
])

# Magic algorithm to solve
def solve(board):

    if not find_empty(board):
        return print_board(board)
    else:
        coordinates = find_empty(board)
    for i in range (1, 10):
        if valid(board, coordinates, i):
            board[coordinates[0], coordinates[1]] = i
            solve(board)
            board[coordinates[0], coordinates[1]] = 0


# Checks if number fits in board
def valid(board, position, value):
    #Check row
    for i in range(len(board)):
        if board[position[0],i] == value:
            return False
    #Check column
    for i in range(len(board[0])):
        if board[i,position[1]] == value:
            return False
    #Check box
    X = position[0] // 3 #Finds x-cord of box
    Y = position[1] // 3 #Finds y-cord of box

    for i in range(X*3, X*3+3):
        for j in range(Y*3, Y*3+3):
            if board[i,j] == value:
                return False

    return True


# Prints board in nice manner
def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('----------------------')

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            if j == 8:
                print(board[i,j])
            else:
                print(str(board[i,j]) + ' ', end='')


# Returns index of first 0 looping through row,col
def find_empty(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i,j] == 0:
                return (i,j) #row, col
    return None


solve(board1)