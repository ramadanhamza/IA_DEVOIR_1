import time
import heapq
from maze import get_neighbors, find_position


def manhattan_distance(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


def astar(maze):
    start = find_position(maze, 'S')
    goal = find_position(maze, 'G')

    if not start or not goal:
        return None

    start_time = time.perf_counter()

    counter = 0
    open_set = [(manhattan_distance(start, goal), counter, start)]
    heapq.heapify(open_set)

    came_from = {start: None}

    g_score = {start: 0}

    closed_set = set()
    explored_order = []

    while open_set:
        f_current, _, current = heapq.heappop(open_set)

        if current in closed_set:
            continue

        closed_set.add(current)
        explored_order.append(current)

        if current == goal:
            break

        neighbors = get_neighbors(maze, current[0], current[1])
        for neighbor in neighbors:
            if neighbor in closed_set:
                continue

            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan_distance(neighbor, goal)
                came_from[neighbor] = current
                counter += 1
                heapq.heappush(open_set, (f_score, counter, neighbor))

    end_time = time.perf_counter()

    path = []
    if goal in closed_set:
        current = goal
        while current is not None:
            path.append(current)
            current = came_from[current]
        path.reverse()

    return {
        'path': path,
        'explored': explored_order,
        'nodes_explored': len(closed_set),
        'path_length': len(path),
        'time_ms': (end_time - start_time) * 1000
    }