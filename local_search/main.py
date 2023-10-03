#aia bljad ma tahan giti maha lasta

from random import randint

def is_safe(board,queens):
    for q in queens:

        piece = q
        letter = piece[2]
        row = piece[0]
        col = piece[1]

        for i in range(N):
            if board[i][col] != 'q':
                board[i][col] = letter
            if board[row][i] != 'q':
                board[row][i] = letter

        offset = row - col
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 'q':
                    if i == (j + offset):
                        board[i][j] = letter
                    if i == ((col+row) - j):
                        board[i][j] = letter


    return board


def place_queens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    queens = []
    for i in range(N):
        while True:
            a = randint(0, N - 1)
            b = randint(0, N - 1)

            if board[a][b] != 'q':
                queens.append((a, b, str(i)))
                board[a][b] = 'q'
                break

    return board, queens


def print_board(board):
    for row in board:
        print(' '.join(row))


N = 5
board,queens = place_queens(N)
board = is_safe(board, queens)
print("Initial Random Placement:")

print_board(board)
