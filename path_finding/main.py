from queue import Queue, PriorityQueue

lava_map1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
]
lava_map2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
]

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def is_valid(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[x]) and maze[x][y] != '*'

def find_start_and_end(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 's':
                start_pos = (i, j)
            elif map[i][j] == 'D':
                end_pos = (i, j)
    return start_pos, end_pos

def find_path_bfs(maze, start, end):
    queue = Queue()
    queue.put((start, []))
    visited = set()

    while not queue.empty():
        (x, y), path = queue.get()

        if (x, y) == end:
            return path

        if (x, y) not in visited:
            visited.add((x, y))

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) not in visited:
                    if is_valid(new_x, new_y, maze):
                        new_path = path + [(new_x, new_y)]
                        queue.put(((new_x, new_y), new_path))

    return None

def heuristic(a, b):
   return abs(a[0] - b[0]) + abs(a[1] - b[1])
def find_path_gbfs(maze, start, end):
    queue = PriorityQueue()
    queue.put((0, start, []))
    visited = set()

    while not queue.empty():
        no,(x, y), path = queue.get()

        if (x, y) == end:
            return path

        if (x, y) not in visited:
            visited.add((x, y))

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) not in visited:
                    if is_valid(new_x, new_y, maze):
                        priority = heuristic(end,(new_x, new_y))
                        new_path = path + [(new_x, new_y)]
                        queue.put((priority,(new_x, new_y), new_path))

    return None

def search_bfs(map):
    start_pos ,end_pos = find_start_and_end(map)
    path = find_path_bfs(map, start_pos, end_pos)
    print_result(path,map)

def search_gbfs(map):
    start_pos ,end_pos = find_start_and_end(map)
    path = find_path_gbfs(map, start_pos, end_pos)
    print_result(path,map)

with open("cave300x300") as f:
    map_data1 = [l.strip() for l in f.readlines() if len(l)>1]
with open("cave600x600") as f:
    map_data2 = [l.strip() for l in f.readlines() if len(l)>1]
with open("cave900x900") as f:
    map_data3 = [l.strip() for l in f.readlines() if len(l)>1]

def print_result (path, map):
    if path is not None:
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
        print("No path found")

search_gbfs(map_data1)
#search_bfs(map_data1)


