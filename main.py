from collections import deque

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



def find_path_bfs(maze, start, end):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path

        if (x, y) not in visited:
            visited.add((x, y))

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (new_x,new_y) not in visited:
                    if is_valid(new_x, new_y, maze):
                        new_path = path + [(new_x, new_y)]
                        queue.append(((new_x, new_y), new_path))

    return None



start_pos = None
end_pos = None

with open("cave900x900") as f:
    map_data = [l.strip() for l in f.readlines() if len(l)>1]



def search_bfs(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 's':
                start_pos = (i, j)
            elif map[i][j] == 'D':
                end_pos = (i, j)
    path = find_path_bfs(map, start_pos, end_pos)

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

#search_bfs(lava_map1)
search_bfs(map_data)