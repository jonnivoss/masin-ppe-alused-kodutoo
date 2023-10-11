import random

numbers = ["1", "2", "3", "4", "5", "6", "7"]
players = ["x", "o"]

board_X = 7
board_Y = 6


def create_board():
    board = [["." for _ in range(board_X)] for _ in range(board_Y)]
    columns = [0 for _ in range(7)]
    return board, columns


def printBoard(board):
    for row in board:
        for cell in row:
            print("|", cell, end=" ")
        print("|")
        for i in range(board_X * 2):
            print("- ", end="")
        print("- ")
    for i in range(board_X):
        print(f"  {i + 1}", end=" ")


def check(board, colum):
    col_counter = 0
    for i in colum:
        if i >= board_Y:
            col_counter += 1

    if col_counter >= board_X:
        return -1


    winner = 0
    # check for columns
    for i in range(board_X):
        column = [row[i] for row in board]
        winner = counter(column)
        if winner != 0:
            return winner

    # check for rows
    for i in range(board_Y):
        row = board[i]
        winner = counter(row)
        if winner != 0:
            return winner

    # check for ULDR diagonals
    for k in range(-3, 3):
        diagonal = []
        for i in range(board_Y):
            for j in range(board_X):
                if i == j + k:
                    diagonal.append(*[board[i][j]])
        winner = counter(diagonal)
        if winner != 0:
            return winner

    # check for DLUR diagonals
    for k in range(3, 9):
        diagonal = []
        for i in range(board_Y):
            for j in range(board_X):
                if i == k - j:
                    diagonal.append(*[board[i][j]])
        winner = counter(diagonal)
        if winner != 0:
            return winner

    return 0


def counter(line):
    count = 0
    for i in line:
        if i == "x":
            count += 1
            if count == 4:
                return 1
        else:
            count = 0
    count = 0
    for i in line:
        if i == "o":
            count += 1
            if count == 4:
                return 2
        else:
            count = 0
    return 0


def ch_input(selection, columns):
    # check if the input is a column number
    if selection not in numbers:
        print(f"{selection} is not a row you can use")
        return -1
    # make the input an int
    selected = int(selection) - 1
    # check if the column is full
    if columns[selected] >= board_Y:
        print(f"No more room in the {selected + 1} column, please go again")
        return -1
    return selected


def player_move(columns):
    selected = -1
    while selected == -1:
        # Select column to put a piece in
        selection = input(f"Player make your Selection(1-7):")

        selected = ch_input(selection, columns)
    return selected


def add_piece(board, columns, selected, player):
    board[board_Y - columns[selected] - 1][selected] = player
    columns[selected] += 1
    return board, columns

def copy_matrix(matrix):
    # Get the dimensions of the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with the same dimensions as the original
    new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Copy the values from the original matrix to the new matrix
    for i in range(rows):
        for j in range(cols):
            new_matrix[i][j] = matrix[i][j]

    return new_matrix

def monte_carlo(board, columns):
    selected = [0 for _ in range(board_X)]
    num_moves = [0 for _ in range(board_X)]
    win_percent = ["0.0" for _ in range(board_X)]

    for i in range(1000):
        start,winner = ai_move(board, columns)
        num_moves[start] += 1
        if winner == 2:
            selected[start] += 1
        elif winner == -1:
            selected[start] += 0.5
    for i in range(board_X):
        if num_moves[i] != 0:
            win_percent[i] = round(selected[i]/num_moves[i] * 100,3)
    print("win precent",*win_percent)
    best = win_percent[0]
    best_index = 0
    for i in range(board_X):
        if win_percent[i] > best:
            best = win_percent[i]
            best_index = i

    return best_index

def ai_move(board, columns):
    turn = 1
    game_over = False
    selction = 0
    moves = 0
    temp_board = copy_matrix(board)
    temp_col = columns[:]
    winner = 0
    while not game_over:
        sel = random.randint(0, 6)

        if moves == 0:
            selction = sel

        if temp_col[sel] >= board_Y:
            continue
        # Add a piece to the board
        temp_board,temp_col = add_piece(temp_board, temp_col, sel, players[turn])

        # printBoard(temp_board)
        moves += 1
        winner = check(temp_board,temp_col)
        if winner != 0:
            break

        # change player
        turn = turn + 1
        turn = turn % 2

    return selction, winner


def play_game():
    game_over = False
    turn = 0
    # initialize board
    board, columns = create_board()
    # We will initialize the game_over as False.

    while not game_over:
        if turn == 0:
            # Select column to put a piece in
            selected = player_move(columns)
            print("\n", selected + 1, "see on mangja ome \n")
        else:
            selected = monte_carlo(board, columns)
            print("\n", selected+1, "see on ai ome \n")

        # Add a piece to the board
        board,columns = add_piece(board, columns, selected, players[turn])

        printBoard(board)
        print()

        winner = check(board,columns)
        if winner != 0:
            print("Winner is player", winner)
            game_over = True

        # change player
        turn = turn + 1
        turn = turn % 2

play_game()
