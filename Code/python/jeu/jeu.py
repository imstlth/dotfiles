# FIX:
# Il doit y avoir un problème car ça prend beaucoup trop de temps

# TEST:
# C'est peut-être en rapport avec que par exemple :
# les 4 bleus sont considérés comme différents
# (si on en échange deux c'est pas la même config)

DIMENSIONS = (4, 5)

PIECES = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1)],
    [(0, 0), (1, 0)],
    [(0, 0)]
]

INIT = [
    [[1, 0]],
    [[0, 0], [3, 0], [0, 3], [3, 3]],
    [[1, 2]],
    [[1, 3], [1, 4], [2, 3], [2, 4]]
]

def est_correct(plateau):
    grille = [ [ False for i in range(DIMENSIONS[0]) ] for j in range(DIMENSIONS[1]) ]
    for num_piece in range(len(plateau)):
        for emp_x, emp_y in plateau[num_piece]:
            for dx, dy in PIECES[num_piece]:
                x = emp_x + dx
                y = emp_y + dy
                if x < 0 or x >= DIMENSIONS[0] or y < 0 or y >= DIMENSIONS[1]:
                    return False
                if grille[y][x]:
                    return False
                grille[y][x] = True
    return True

def poss(plateau):
    for num_piece in range(len(plateau)):
        for piece_ind in range(len(plateau[num_piece])):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_plat = [ [ coords.copy() for coords in pieces ] for pieces in plateau ] # On doit copier en profondeur
                new_plat[num_piece][piece_ind][0] += dx
                new_plat[num_piece][piece_ind][1] += dy
                if est_correct(new_plat):
                    yield new_plat

def succes(plateau):
    return plateau[0] == [[1, 3]]

def deep(plateau):
    return tuple([ tuple([ tuple(coords) for coords in pieces ]) for pieces in plateau])

def undeep(plateau):
    return [ [ list(coords) for coords in pieces ] for pieces in plateau]

def parcours(plateau_0=INIT):
    vus = {}
    a_voir = [plateau_0]
    final = None
    n = 0
    first = True
    particulier = plateau_0
    while len(a_voir) != 0 and final is None:
        plateau = a_voir.pop(0)
        if plateau == particulier:
            first = True
        for suivant in poss(plateau):
            if deep(suivant) not in vus:
                vus[deep(suivant)] = plateau
                a_voir.append(suivant)
                if succes(suivant):
                    final = suivant
                    break
                if first:
                    first = False
                    particulier = suivant
                    n += 1
                    print(n, "coups")
    if final is None:
        print("Pas trouvé !")
    else:
        suite = [final]
        while final != plateau_0:
            suite.append(vus[deep(final)])
            final = vus[deep(final)]
        for plat in suite[::-1]:
            print(plat)
            print()

parcours()
