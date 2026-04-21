# DIFFÉRENT DU CODE SUR CODINGAME !!

# TODO:
# TOUJOURS VERIFIER QUE DANS UNE LISTE 2D TU N'INVERSES PAS Y ET X:
# c'est comme ça: liste[y][x] et PAS liste[x][y]


def get_infos_possibilities(speed, motos_infos):
    "Renvoie la vitesse et motos_infos pour chaque action possible."

    # La vitesse peut être calculée facilement
    speed_poss = {
        "SPEED": speed + 1,
        "SLOW": speed - 1,
        "JUMP": speed,
        "WAIT": speed,
        "UP": speed,
        "DOWN": speed
    }

    # Pour motos_infos c'est plus compliqué
    motos_infos_poss = []
    y_occupés = {
        "SPEED": [],
        "SLOW": [],
        "JUMP": [],
        "WAIT": [],
        "UP": [],
        "DOWN": []
    }
    for moto in motos_infos:

        x = {}
        for poss in list(speed_poss.items()):
            x[poss[0]] = moto["x"] + poss[1]  # poss[0] est l'action et poss[1] est la vitesse

        # On vérifie bien que la moto ne sorte pas de la route et qu'il n'y en a pas déjà une.
        if moto["y"] != 0 and moto["y"] - 1 not in y_occupés:
            up = moto["y"] - 1
        else:
            up = moto["y"]
        if moto["y"] != len(road) - 1 and moto["y"] + 1 not in y_occupés:
            down = moto["y"] + 1
        else:
            down = moto["y"]
        y_occupés["UP"].append(up)
        y_occupés["DOWN"].append(down)

        y = {
            "SPEED": moto["y"],
            "SLOW": moto["y"],
            "JUMP": moto["y"],
            "WAIT": moto["y"],
            # y ne change que lorsqu'on fait UP ou DOWN
            "UP": up,
            "DOWN": down
        }
        # Si la moto est active il faut voir s'il l'est encore dans chaque possibilité
        if moto["active"]:
            active = is_active(x, y, moto["x"])
        # Si elle est inactive, on la laisse inactive
        else:
            active = {}
            for action in actions:
                active[action] = False
        motos_infos_poss.append({"x": x, "y": y, "active": active})
    return {"speed_poss": speed_poss, "motos_infos_poss": motos_infos_poss}


def is_active(x_poss, y_poss, actual_x):
    "Renvoie si la moto sera active dans chacune des différentes possibilités."

    active = {}
    # On cacule chaque possibilité
    for action in actions:
        if action in ["SPEED", "SLOW", "WAIT"]:
            # On check s'il n'y a pas un trou entre là d'où on part et l'arrivée (compris)
            active[action] = "0" not in road[y_poss[action]][actual_x:x_poss[action] + 1]
        # Si l'action est JUMP, on check juste l'arrivée et là d'où on part mais pas entre
        elif action == "JUMP":
            active[action] = "0" not in road[y_poss[action]][actual_x] + road[y_poss[action]][x_poss[action]]
        # Si l'action est UP ou DOWN, alors on check toutes les cases concernées
        elif action in ["UP", "DOWN"]:
            # On prend y_poss["WAIT"] car ça renvoie le y dans lequel la moto se trouve actuellement.
            # On prend seulement ensuite y_poss[action] pour que ça y rajoute la ligne du dessus
            # IMPORTANT : la case juste au dessus de la moto n'est pas prise en compte (il faut faire actual_x + 1 pour la skip)
            active[action] = "0" not in road[y_poss["WAIT"]][actual_x:x_poss[action]] + road[y_poss[action]][actual_x + 1:x_poss[action] + 1]

    return active


def recursion_determine(speed, motos_infos):
    "Renvoie une liste avec la liste des actions à faire et le nombre de motos actives à la fin de ces actions."

    # Tout d'abord, si une des motos actives est plus loin que le dernier trou
    # ou qu'elle est au bout de la carte
    # On renvoie, la premier des actions car n'importe laquelle suffit et il n'est pas nécéssaire de faire un arbre de possibilités.
    # S'il n'y a plus de motos actives, on renvoie n'importe quoi (SPEED) avec un nombre de motos actives de 0
    end = False
    not_active = True
    for moto in motos_infos:
        if moto["active"]:
            not_active = False
            if moto["x"] > x_last_hole or moto["x"] == len(road[0]) - 1:
                return [["SPEED"], 9999]  # On peut remarque que ça renvoie 9999 en nombre de motos actives pour que cette possibilité est un poid beaucoup plus important.
                end = True
                break

    if not end:
        if not_active:
            return [["SPEED"], 0]

        else:
            infos_poss = get_infos_possibilities(speed, motos_infos)

            # On calcul quelle action fait le plus de motos actives
            best_actions = ["SPEED"]  # On dit que SPEED en fait le plus et on voit si une action est meilleure que SPEED
            best_active = 0
            for moto in range(n_motos):
                # On ajoute à best_active l'activité de chaque moto (True = 1 & False = 0)
                best_active += infos_poss["motos_infos_poss"][moto]["active"]["SPEED"]

            # Pour chaque possibilité
            for action in actions[1:]:
                # On vérifie d'abord que ça ne mets pas la vitesse à 0 (inutile)
                if infos_poss["speed_poss"][action] != 0:
                    # On regarde combien de motos sont actives dans cette possibilité
                    active = 0
                    for moto in range(n_motos):
                        active += infos_poss["motos_infos_poss"][moto]["active"][action]
                    # Si c'est mieux que la meilleure action, on la remplace
                    if active > best_active:
                        best_actions = [action]
                        best_active = active
                    # Si c'est égale, on la rajoute à la liste des choix.
                    elif active == best_active:
                        best_actions.append(action)

            # Si une possibilité est meilleure que toutes les autres
            if len(best_actions) == 1:
                return [best_actions, best_active]

            # Sinon, on refait un étage de possibilité en partant des meilleurs qu'on a trouvée
            else:
                # On calcul quelle action (à notre niveau de récursion) fait le plus de motos actives (dans les niveaux supérieurs)
                default_action = best_actions[0]
                next_best_actions = default_action  # On dit que la premier action en fait le plus et on voit si une action (de ce niveau) est meilleure que celle-ci
                next_best_active = 0  # Le nombre de motos activées dans le futur avec cette action et par celles qui suivent
                # On fait une liste des actions qui ont été choisies par les niveaux supérieurs
                # Comme ça on enregistrera la liste et on ne sera pas obligé de refaire tous les calculs à chaque fois.
                queue = []
                # On transforme infos_poss["motos_infos_poss"] dans le même format que motos_infos (pour la première action)
                motos_infos_poss_formated = []
                for moto in infos_poss["motos_infos_poss"]:
                    motos_infos_poss_formated.append({
                        "x": moto["x"][default_action],
                        "y": moto["y"][default_action],
                        "active": moto["active"][default_action]
                    })
                next_one = recursion_determine(infos_poss["speed_poss"][default_action], motos_infos_poss_formated)
                queue = next_one[0]  # On enregistre les actions considérées comme les meilleurs par les niveaux supérieurs
                next_best_active = next_one[1]  # Le nombre de motos qui seront actives si on suit ces actions

                for action in best_actions[1:]:
                    # On transforme infos_poss["motos_infos_poss"] dans le même format que motos_infos (pour chaque action)
                    motos_infos_poss_formated = []
                    for moto in infos_poss["motos_infos_poss"]:
                        motos_infos_poss_formated.append({
                            "x": moto["x"][action],
                            "y": moto["y"][action],
                            "active": moto["active"][action]
                        })
                    next_one = recursion_determine(infos_poss["speed_poss"][action], motos_infos_poss_formated)
                    next_active = next_one[1]
                    # Si c'est mieux que la meilleure action, on la remplace
                    if next_active > next_best_active:
                        next_best_actions = action
                        next_best_active = next_best_active
                        queue = next_one[0]
                    # Si c'est égale, cela veut dire qu'elle donne les même résultat que la meilleur action actuelle
                    # Donc, on ne la prend pas en compte

                # Pour finir, on renvoie les actions du futur (choisies par les niveaux supérieures) avec l'action choisie à ce niveau
                # NOTE : queue est dans le sens futur (index 0) -> présent (index -1)
                return [queue + [next_best_actions], next_best_active]

# Données d'initialisation
n_motos = int(input())  # Le nombre de motos au début
n_objectif = int(input())  # Le nombre de motos qui doivent atteindre l'objectif
road = [list(input()), list(input()), list(input()), list(input())]  # La route (. = safe & 0 = dead)
actions = ["SPEED", "SLOW", "JUMP", "WAIT", "UP", "DOWN"]  # Les actions possibles

x_last_hole = 0
for line in road:
    try:
        last_hole_line = len(line) - line[::-1].index("0") - 1
    except:
        last_hole_line = 0
    if last_hole_line > x_last_hole:
        x_last_hole = last_hole_line

# Boucle principale
# poss = possibilities
strategie = []
while True:
    speed = int(input())
    motos_infos = []

    for moto in range(n_motos):
        infos = input().split()
        x = int(infos[0])
        y = int(infos[1])
        active = infos[2] == "1"
        motos_infos.append({"x": x, "y": y, "active": active})
    if speed == 0:
        print("SPEED")
    else:
        if strategie == []:
            strategie = recursion_determine(speed, motos_infos)[0][::-1]
        print(strategie[0])
        strategie.pop(0)

# NOTE
# On peut faire :
# On teste chacune des possibilités qui s'offrent actuellement
# On regarde combien de motos sont encore actives après chaque possibilités.
# IMPORTANT : On ne doit jamais être à la vitesse 0
# Si 2 possibilités ou + donnent le même nombre de motos restantes, il faut le départager.
# Pour les départager, on calcule le nombre de motos restantes après 2 tours où on a fait toutes les possibilités.
# À partir du moment, il où il ne reste plus qu'un choix (ou qu'il ne reste plus de trous)
# On prend la possibilité calculée et on enregistre les actions à faire suivantes.
# Comme ça, s'il y a des actions dans la liste des actions enregistrées, on les fait et on ne calcul pas la suite.
