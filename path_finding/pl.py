

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def is_valid(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[x]) and maze[x][y] != '*'
def heuristic(a, b):
   return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_start_and_end(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 's':
                start_pos = (i, j)
            elif map[i][j] == 'D':
                end_pos = (i, j)
    return start_pos, end_pos


def print_result (path, map, iteratsioone, time_elapsed):
    """if path is not None:
        for i in range(len(map)):
            row = ""
            for j in range(len(map[i])):
                if map[i][j] == "D":
                    row += "D"
                elif (i, j) in path:
                    row += "."
                else:
                    row += map[i][j]
            print(row)
    else:
        print("No path found")"""

    print("clock time", time_elapsed, "number of iterations", iteratsioone, "lenght of path",len(path))