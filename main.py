import sys
from maze import generate_maze, print_maze, print_maze_with_path, find_position
from dfs import dfs
from bfs import bfs
from astar import astar


def format_path(path):
    if not path:
        return "Aucun chemin trouvé"

    parts = []
    for i, (x, y) in enumerate(path):
        if i == 0:
            parts.append(f"S ({x}, {y})")
        elif i == len(path) - 1:
            parts.append(f"G ({x}, {y})")
        else:
            parts.append(f"({x}, {y})")

    return " -> ".join(parts)


def run_algorithm(name, algorithm_func, maze):
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}")

    result = algorithm_func(maze)

    if result is None or not result['path']:
        print("  Aucun chemin trouvé!")
        return None

    print(f"\n--- Exploration ({name}) ---")
    print_maze_with_path(maze, explored=result['explored'], mode="exploration")

    print(f"--- Solution ({name}) ---")
    print_maze_with_path(maze, explored=result['explored'],
                         path=result['path'], mode="solution")

    print(f"Chemin : {format_path(result['path'])}")

    print(f"\nStatistiques:")
    print(f"  Noeuds explorés  : {result['nodes_explored']}")
    print(f"  Longueur du chemin: {result['path_length']}")
    print(f"  Temps d'exécution : {result['time_ms']:.3f} ms")

    return result


def print_comparison_table(results):
    print("\nTABLEAU COMPARATIF :")
    print(f"{'Algorithme':<20} {'Noeuds':<10} {'Longueur':<12} {'Temps (ms)':<12}")
    print("-" * 54)
    for name, result in results.items():
        if result:
            print(f"{name:<20} {result['nodes_explored']:<10} "
                  f"{result['path_length']:<12} {result['time_ms']:<12.3f}")
        else:
            print(f"{name:<20} {'N/A':<10} {'N/A':<12} {'N/A':<12}")
    print()


def main():
    seed = None
    if len(sys.argv) > 1:
        if sys.argv[1] == "--seed" and len(sys.argv) > 2:
            try:
                seed = int(sys.argv[2])
            except ValueError:
                print("Erreur: Le seed doit être un entier.")
                sys.exit(1)
        else:
            print("Usage: python main.py [--seed <entier>]")
            sys.exit(1)

    if seed is None:
        seed = 42
        print(f"Utilisation du seed par défaut: {seed}")
    else:
        print(f"Utilisation du seed: {seed}")

    print(f"\n{'='*60}")
    print("  GÉNÉRATION DU LABYRINTHE (16x16)")
    print(f"{'='*60}")
    maze = generate_maze(size=16, seed=seed)

    print("\n--- Labyrinthe original ---")
    print_maze(maze)

    start = find_position(maze, 'S')
    goal = find_position(maze, 'G')
    print(f"Départ (S) : {start}")
    print(f"Arrivée (G): {goal}")

    results = {}
    results['DFS'] = run_algorithm("DFS (Depth-First Search)", dfs, maze)
    results['BFS'] = run_algorithm("BFS (Breadth-First Search)", bfs, maze)
    results['A* (manhattan)'] = run_algorithm("A* (Manhattan Distance)", astar, maze)

    print_comparison_table(results)

if __name__ == "__main__":
    main()