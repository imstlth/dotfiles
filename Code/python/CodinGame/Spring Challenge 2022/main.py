import math

#############
# STRATEGIE #
#############

# Parmi tous les monstres dangereux,
# le monstre le plus proche de la base se fait attaqué par le héro le plus proche de lui


# TODO:
# Comprendre WTF
# C'est quoi l'output generator object machin ???

base = input().split()
base_coords = {"x": int(base[0]), "y": int(base[1])}


# Une fonction pour calculer la distance entre deux coordonnées sur la carte
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# La même fonction mais pour les dict
def distance_coords(coords1, coords2):
    return math.sqrt(
        (coords1["x"] - coords2["x"]) ** 2 + (coords1["y"] - coords2["y"]) ** 2
    )


# Boucle principale
while True:
    ############################
    # ENREGISTREMENT DES INFOS #
    ############################

    base_life = int(input().split()[0])  # On ignore le mana pour cette ligue
    # On se fout des infos d'en face
    input()
    input()  # WTF
    entity_count = int(input())
    monsters = {}
    heros = {}
    dangerous_monsters = {}

    for _entity in range(entity_count):
        data = input().split()

        if data[1] == "0":  # Si c'est un monstre, on l'enregistre dans les monstres
            x = int(data[2])
            y = int(data[3])
            monster_data = {
                "coords": {"x": x, "y": y},  # Sa position actuelle
                "hp": int(data[6]),
                "move": {
                    "x": int(data[7]),
                    "y": int(data[8]),
                },  # Les coords de son vecteur vitesse
                "next_coords": {
                    x + int(data[7]),
                    y + int(data[8]),
                },  # Ses coords le tour suivant
                "attacking": bool(int(data[9])),
                "dangerous": data[10] == "1",  # S'il risque d'atteindre la base
            }
            monsters[int(data[0])] = monster_data
            # On l'enregisre dans la liste des dangereux s'il l'est
            if monster_data["dangerous"]:
                dangerous_monsters[int(data[0])] = monster_data

        elif data[1] == "1":  # Si c'est un de mes héros, on le mets dans la liste
            heros[int(data[0])] = {
                "coords": {"x": int(data[2]), "y": int(data[3])}  # Sa position actuelle
            }

        # On se fout des héro ennemis pour l'instant

    # On classe les monstres dangereux par distance avec la base
    sortedbydist_danger_monsters = []  # La liste des id des monstres dangereux classés par distance avec la base
    # Pour chaque monstre dangereux
    for monster1 in dangerous_monsters:
        n = 0
        last = True
        for monster2_id in sortedbydist_danger_monsters:
            # On le mets avant celui qui est moins dangereux que lui
            if distance_coords(monster1["coords"], base_coords) < distance_coords(
                monsters[monster2_id]["coords"], base_coords
            ):
                sortedbydist_danger_monsters.insert(n, monster1["id"])
                last = False
                break
            n += 1
        # S'il est moins dangereux que tous, on le mets à la fin
        # Ça va aussi se déclencher si la liste est vide
        if last:
            sortedbydist_danger_monsters.append(monster1["id"])

    ##########
    # ACTION #
    ##########

    output = ["WAIT"] * len(heros)
    # Pour chaque monstre, on assigne le héro le plus proche
    # C'est [:len(heros)] car on cible autant de monstre qu'il y a de héros
    for monster_id in sortedbydist_danger_monsters[: len(heros) - 1]:
        # La liste des distances entre chaque héro et le monstre
        dists_hero = []
        monster_coords = monsters[monster_id]["coords"]
        for hero in heros:
            dists_hero.append(distance_coords(monster_coords, hero["coords"]))
        hero_index = dists_hero.index(min(dists_hero))
        output[hero_index] = "MOVE " + monster_coords["x"] + " " + monster_coords["y"]

    print(out for out in output)
