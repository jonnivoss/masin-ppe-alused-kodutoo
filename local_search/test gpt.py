import random


def generate_random_board(n):
    """Generate a random board configuration."""
    board = [random.randint(0, n - 1) for _ in range(n)]
    return board


def calculate_cost(board):
    """Calculate the cost of a board configuration."""
    n = len(board)
    cost = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                cost += 1
    return cost


def hill_climb_n_queens(n, max_iterations=1000):
    """Solve the N-Queens problem using hill climbing."""
    current_board = generate_random_board(n)
    print_board(current_board)
    current_cost = calculate_cost(current_board)

    for _ in range(max_iterations):
        neighbors = []

        for i in range(n):
            for j in range(n):
                if current_board[i] != j:
                    neighbor_board = current_board.copy()
                    neighbor_board[i] = j
                    neighbors.append((neighbor_board, calculate_cost(neighbor_board)))

        neighbors.sort(key=lambda x: x[1])
        best_neighbor, best_neighbor_cost = neighbors[0]

        if best_neighbor_cost >= current_cost:
            # If no better neighbor, return current solution
            return current_board

        current_board, current_cost = best_neighbor, best_neighbor_cost

    # If max_iterations reached, return the current best solution
    return current_board


def print_board(board):
    """Print the board configuration."""
    n = len(board)
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(" ".join(row))



n = 8  # Change this to the desired board size
solution = hill_climb_n_queens(n)
print("N-Queens Solution:")
print_board(solution)
