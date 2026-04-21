# 0 = rien
# 1 = joueur
# 2 = IA
actual_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for n in range(9)]
# Quels grilles ont été gagnées, et par qui
# 0 : il reste au moins 1 move possible à faire
# 1 : l'IA a gagné
# 2 : l'humain a gagné
# 3 : égalité
boards_won = [0 for n in range(9)]

# L'arbre des possibilités à partir du move du joueur, avec le score de la possibilité
tree = {actual_board: 0}

def score(board):
    boards_scores = []
    super_lines = []
    boards_lines = []
    for mini in board:
        board_lines = []
        for i in range(3):
            # Les horizontales
            board_lines.append(mini[i*3:(i+1)*3])
            # Les verticales
            board_lines.append(mini[i::3])
        # Les diagonales
        board_lines.append(mini[0::4])
        board_lines.append(mini[2:7:2])
        boards_lines.append(board_lines)

    # Pour chaque board, on regarde son score
    for board_lines in boards_lines:
        board_score = 0
        # Les lines dans chaque mini grille
        for line in board_lines:
            for player_n in range(1, 3):
                # S'il y a possibilité de gagner sur cette ligne, on rajoute 1
                if line.count(player_n) == 2 and line.count(0) == 1:
                    board_score += (-1) ** player_n
                # Si la ligne est gagnée, on met 8 en temps que score de la board (voir +loin)
                elif line.count(player_n) == 3:
                    winning_player = player_n
                    break
            else:
                break
        else:
            board_score = (-8) ** winning_player
        boards_scores.append(board_score)

    # Maintenant, on regarde si il y a des possibilités de gagner sur une ligne du super morpion
    for i in range(3):
        # Les lignes horizontales du super morpion
        super_lines.append(boards_scores[i*3:(i+1)*3])
        # Les lignes verticales du super morpion
        super_lines.append(boards_scores[i::3])
    # Les diagonales
    super_lines.append(boards_scores[0::4])
    super_lines.append(boards_scores[2:7:2])

    for super_line in super_lines:
        for player_n in range(1, 3):
            if super_line.count((-8) ** n_player) == 2 and line.count()

##### BON EN FAIT GIGA FLEMME


    return score

n_tour = 0
while True:
    # TODO : Empêcher toute triche et vérifier que le move est légal
    player_move = input()
    for branch in tree:
        # On supprime toutes les possibilités que le joueur n'a pas jouées
        tree.pop(branch)

        # Pour les autres, on rajoute une couche de prévision et la rajoute à tree
        if branch.startswith(player_move):
            branch = branch.removeprefix(player_move)
            history += player_move

            # Dans le cas où la fin de la branch nous emmène sur une board qui n'est pas finie, on fait la liste des possibilités dans cette board
            if boards_won[int(branch[-1])] == 0:
                for move in range(9):
                    if branch[-1] + str(move) not in history + branch:
                        new_branch = branch + str(move)
                        tree[new_branch] = score(history + new_branch)

            # Dans le cas où la board ne peut plus être jouée, on choisit une autre board et une autre case disponibles
            else:
                for board in range(9):
                    if boards_won[board] == 0:
                        for move in range(9):
                            if str(board) + str(move) not in history + branch:
                                new_branch = branch + f".{board}{move}"
                                tree[new_branch] = score(history + new_branch)

            # Ne pas oublier d'enlever les possibilités que l'IA ne choisit pas, une fois qu'elle a choisit

    n_tour += 1
