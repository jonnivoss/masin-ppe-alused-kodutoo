import os

numbers = ["1","2","3","4","5","6","7"]


def create_board():
    board = [["0" for _ in range(7)] for _ in range(6)]
    columns = [5 for _ in range(7)]
    return board, columns


# initialize board
board,columns = create_board()
# We will initialize the game_over as False.
game_over = False
turn = 0

def printBoard(board):
    for row in board:
        for cell in row:
            print(cell,end=" ")
        print()

turn = 1
while not game_over:

    selection = input(f"Player {turn+1} Make your Selection(0-6):")
    print()
    if selection in numbers:
        print("tupli")
        selected = int(selection)-1
        board[columns[selected]][selected] = turn+1
        columns[selected] = columns[selected] - 1
        printBoard(board)
    else:
        print("fuga u")
        continue
    turn = turn+1
    turn = turn%2

