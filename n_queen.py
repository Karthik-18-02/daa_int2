global n
n = 4

def board(n):

    l = [[0 for i in range(n)] for j in range(n)]
    return l

def printSolution(board):

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print('Q', end = ' ')
            else:
                print('.', end = ' ')
        print()

    return

def isSafe(board, row, column):

    for i in range(column):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQ(board, col):

    if col >= n:
        return True

    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQ(board, col+1) == True:
                return True
            board[i][col] = 0
    return False


o = board(4)

printSolution(o)
print(solveNQ(o, 0))
printSolution(o)


