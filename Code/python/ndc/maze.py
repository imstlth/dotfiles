import ast
import random

# IMPORTANT: On considère que la première coord dans le tableau python est x et la deuxième correspond à y
def maze_gen_recursion(cases_grid, case_coords, lvl = 0):
    # D'abord x puis y
    case = cases_grid[case_coords[0]][case_coords[1]]
    case["visited"] = True
    # On trouve les voisins
    neighbors = []
    neighbors_direction = ["left", "right", "up", "down"]
    # L'index de la direction opposé
    opposite_direction = [1, 0, 3, 2]
    neighbors_add = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for (x, y) in neighbors_add:
        # On vérifie si la case existe
        if 0 <= case_coords[0] + x < len(cases_grid) and 0 <= case_coords[1] + y < len(cases_grid):
            neighbors.append(cases_grid[case_coords[0] + x][case_coords[1] + y])
        else:
            neighbors.append(None)
    # Les index des voisins non visités dans la list neighbors
    unvisited_neighbors_index = []
    for n_neighbor in range(len(neighbors)):
        if neighbors[n_neighbor] is not None:
            if not neighbors[n_neighbor]["visited"]:
                unvisited_neighbors_index.append(n_neighbor)
    # On continue tant que au moins un voisin a été visité
    while len(unvisited_neighbors_index) != 0:
        # On choisit un voisin aléatoire qui n'a pas été visité
        choosen_neighbor = random.choice(unvisited_neighbors_index)
        # Obtenir le dict de la case du voisin n'est pas si simple
        choosen_case_coords = [case_coords[0] + neighbors_add[choosen_neighbor][0], case_coords[1] + neighbors_add[choosen_neighbor][1]]
        choosen_case = cases_grid[choosen_case_coords[0]][choosen_case_coords[1]]
        # On dit que les deux cases sont connectés - d'ailleurs il faut l'indiquer dans le dict de chacune des cases
        case[neighbors_direction[choosen_neighbor]] = True
        choosen_case[opposite_direction[choosen_neighbor]] = True
        # On appelle la fonction récursive pour le voisin choisi
        maze_gen_recursion(cases_grid, choosen_case_coords, lvl+1)
        # On regen la variable pour être sûr que la boucle s'arrête
        unvisited_neighbors_index = []
        for n_neighbor in range(len(neighbors)):
            if neighbors[n_neighbor] is not None:
                if not neighbors[n_neighbor]["visited"]:
                    unvisited_neighbors_index.append(n_neighbor)

cases_grid = [[{"visited": False, "left": False, "right": False, "up": False, "down": False}] * 4] * 4
cases_grid = ast.literal_eval(str(cases_grid))
maze_gen_recursion(cases_grid, [0, 0])
print(cases_grid)
