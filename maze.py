import random


def generate_maze(size=16, seed=None):
    if seed is not None:
        random.seed(seed)

    maze = [['#' for _ in range(size)] for _ in range(size)]

    start = (1, 1)
    g_x = size - 3 if (size - 2) % 2 == 0 else size - 2
    g_y = size - 3 if (size - 2) % 2 == 0 else size - 2

    stack = [start]
    maze[start[1]][start[0]] = '.'

    while stack:
        x, y = stack[-1]
        directions = [(2, 0), (0, 2), (-2, 0), (0, -2)]
        random.shuffle(directions)

        found = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < size - 1 and 1 <= ny < size - 1 and maze[ny][nx] == '#':
                maze[y + dy // 2][x + dx // 2] = '.'
                maze[ny][nx] = '.'
                stack.append((nx, ny))
                found = True
                break

        if not found:
            stack.pop()

    for y in range(2, size - 2):
        for x in range(2, size - 2):
            if maze[y][x] == '#' and random.random() < 0.10:
                adj_passages = sum(1 for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]
                                   if maze[y+dy][x+dx] == '.')
                if adj_passages >= 2:
                    maze[y][x] = '.'

    maze[1][1] = 'S'
    maze[g_y][g_x] = 'G'

    from collections import deque
    visited = set()
    q = deque([(1, 1)])
    visited.add((1, 1))
    while q:
        cx, cy = q.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx2, ny2 = cx+dx, cy+dy
            if 0 <= nx2 < size and 0 <= ny2 < size and (nx2,ny2) not in visited and maze[ny2][nx2] != '#':
                visited.add((nx2, ny2))
                q.append((nx2, ny2))

    if (g_x, g_y) not in visited:
        return generate_maze(size, seed=(seed or 0) + 1)

    return maze


def print_maze(maze, title=""):
    if title:
        print(f"\n{title}")
        print("-" * (len(maze[0]) * 2))
    for row in maze:
        print(' '.join(row))
    print()


def print_maze_with_path(maze, explored=None, path=None, mode="solution"):
    size = len(maze)
    display = [row[:] for row in maze]

    if mode == "exploration" and explored:
        for (x, y) in explored:
            if display[y][x] not in ('S', 'G'):
                display[y][x] = 'p'
    elif mode == "solution" and path:
        if explored:
            for (x, y) in explored:
                if display[y][x] not in ('S', 'G'):
                    display[y][x] = 'p'
        for (x, y) in path:
            if display[y][x] not in ('S', 'G'):
                display[y][x] = '*'

    for row in display:
        print(' '.join(row))
    print()


def get_neighbors(maze, x, y):
    size = len(maze)
    neighbors = []
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size and maze[ny][nx] != '#':
            neighbors.append((nx, ny))
    return neighbors


def find_position(maze, char):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == char:
                return (x, y)
    return None