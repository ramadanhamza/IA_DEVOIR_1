import time
from collections import deque
from maze import get_neighbors, find_position


def bfs(maze):
    start = find_position(maze, 'S')
    goal = find_position(maze, 'G')

    if not start or not goal:
        return None

    start_time = time.perf_counter()

    queue = deque([start])
    came_from = {start: None}
    explored_set = set([start])
    explored_order = [start]

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        neighbors = get_neighbors(maze, current[0], current[1])
        for neighbor in neighbors:
            if neighbor not in explored_set:
                explored_set.add(neighbor)
                explored_order.append(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)

    end_time = time.perf_counter()

    path = []
    if goal in explored_set:
        current = goal
        while current is not None:
            path.append(current)
            current = came_from[current]
        path.reverse()

    return {
        'path': path,
        'explored': explored_order,
        'nodes_explored': len(explored_set),
        'path_length': len(path),
        'time_ms': (end_time - start_time) * 1000
    }