from queue import Queue, PriorityQueue
import time
import pl

def find_path(maze, start, end):
    queue = Queue()
    queue.put((start, []))
    visited = set()
    iterations = 0
    while not queue.empty():
        (x, y), path = queue.get()

        if (x, y) == end:
            return path, iterations

        if (x, y) not in visited:
            visited.add((x, y))

            for dx, dy in pl.directions:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) not in visited:
                    if pl.is_valid(new_x, new_y, maze):
                        iterations += 1
                        new_path = path + [(new_x, new_y)]
                        queue.put(((new_x, new_y), new_path))

    return None


def search(map):
    start_pos ,end_pos = pl.find_start_and_end(map)
    start_time = time.time()
    path, i = find_path(map, start_pos, end_pos)
    end_time = time.time()
    pl.print_result(path,map, i, end_time - start_time)

