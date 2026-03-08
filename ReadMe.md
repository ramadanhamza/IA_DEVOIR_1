## INF-5183 – Fondements de l'Intelligence Artificielle

# Devoir I – Algorithmes de Recherche dans un Labyrinthe

**Session** : Hiver 2026  
**Université** : Université du Québec en Outaouais

---

## Description

Ce projet contient l'implémentation de trois algorithmes de recherche (informé et non informé) pour résoudre un labyrinthe de taille 16x16 :

- **DFS** (Depth-First Search) – Recherche en profondeur avec pile (LIFO)
- **BFS** (Breadth-First Search) – Recherche en largeur avec file (FIFO)
- **A\*** (A-Star) – Recherche informée avec distance de Manhattan

## Prérequis

- Python 3.11+
- Aucune dépendance externe requise

## Exécution

```bash
# Avec le seed par défaut (42)
python main.py

# Avec un seed spécifique
python main.py --seed 123
```

## Représentation du Labyrinthe

| Symbole | Signification          |
|---------|------------------------|
| `#`     | Mur                    |
| `.`     | Case libre             |
| `S`     | Point de départ        |
| `G`     | Point d'arrivée        |
| `p`     | Case explorée          |
| `*`     | Chemin solution        |

## Sortie du Programme

Pour chaque algorithme, le programme affiche :
1. La visualisation de l'exploration (cases marquées `p`)
2. La visualisation de la solution (chemin marqué `*`)
3. La liste des coordonnées du chemin sous la forme : Chemin: S(1, 1) -> (2, 1) -> (3, 1) -> ... -> G(14, 14)
4. Les statistiques (noeuds explorés, longueur, temps)

Et à la fin :
1. Un tableau comparatif des trois algorithmes