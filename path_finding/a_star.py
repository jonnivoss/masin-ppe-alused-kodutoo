from queue import Queue, PriorityQueue
import time
import pl

def find_path(maze, start, end):
    queue = PriorityQueue()
    queue.put((0, start, []))
    visited = set()
    cost_so_far = {}
    cost_so_far[start] = 0
    iterations = 0
    while not queue.empty():
        cost, (x, y), path = queue.get()

        if (x, y) == end:
            return path, iterations

        if (x, y) not in visited:
            visited.add((x, y))

            for dx, dy in pl.directions:
                new_x, new_y = x + dx, y + dy
                new_cost = cost_so_far[(x, y)] + 1
                if (new_x, new_y) not in visited:
                    if pl.is_valid(new_x, new_y, maze):
                        iterations += 1
                        cost_so_far[(new_x, new_y)] = new_cost
                        priority = new_cost + pl.heuristic(end,(new_x, new_y))
                        new_path = path + [(new_x, new_y)]
                        queue.put((priority,(new_x, new_y), new_path))

    return None

def search(map):
    start_pos, end_pos = pl.find_start_and_end(map)
    start_time = time.time()
    path, i = find_path(map, start_pos, end_pos)
    end_time = time.time()
    pl.print_result(path,map, i, end_time - start_time)