import math

#############
# STRATEGIE #
#############

# Stratégie globale :
# 1 héro en attaque du camp adverse
# Les 2 autres en défense

# ATTAQUE:
# 1) On WIND les spiders  Car le WIND est plus efficace que le CONTROL même si la portée est plus petit
# 2) Si l'ennemi n'est pas en SHIELD -> On le CONTROL pour l'éloigner
# 3) L'héro se SHIELD
# 4) Au besoin on peut CONTROL les spiders

# DEFENSE:
# 1) On applique la stratégie de base d'attaque des spiders
# 2) Si l'ennemi est aggressif (dans notre base):
#     - On se SHIELD
#     - On WIND l'ennemi (il faut qu'il n'est pas de SHIELD)
#     - On peut SHIELD les araignées pour empêcher les WIND
# 3) CONTROL spiders pas dangereuses mais dans portée pour envoyer chez l'ennemi


# Attaque des spiders :
# Parmi tous les monstres dangereux,
# le monstre le plus proche de la base se fait attaqué par le héro le plus proche de lui
# Si jamais un monstre est trop proche (distance à définir), on le WIND


base = input().split()
base_coords = {"x": int(base[0]), "y": int(base[1])}
# Les coords de la base ennemie
ennemis_base_coords = {"x": 17630 - int(base[0]), "y": 9000 - int(base[1])}

# Les coordonnées des points défensifs (pour couvrir un max de zone avec 2 héros)
position_add = [[4620, 1910], [1910, 4620]] # C'est les coordonnées à partir de 0, 0
attack = [abs(ennemis_base_coords["x"] - 3540), abs(ennemis_base_coords["y"] - 3540)]
defense = []

# On les adapte en fonction de l'emplacement de la base
for add in position_add:
    defense.append([abs(base_coords["x"] - add[0]), abs(base_coords["y"] - add[1])])

# Le nombre d'héro par joueur -> toujours 3
heros_count = int(input())

# Une fonction pour calculer la distance entre deux coordonnées sur la carte
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# La même fonction mais pour les dict
def distance_coords(coords1, coords2):
    return math.sqrt((coords1["x"] - coords2["x"]) ** 2 + (coords1["y"] - coords2["y"]) ** 2)

# Une fonction pour récupérer une entité avec son id
def get(liste, id):
    for i in liste:
        if i["id"] == id:
            return i
            break

# Boucle principale
while True:


    ############################
    # ENREGISTREMENT DES INFOS #
    ############################

    info = input().split()
    base_life = int(info[0])
    mana = int(info[1])
    # On se fout des infos d'en face
    input()
    entity_count = int(input())
    monsters = []
    heros = []
    dangerous_monsters = []
    dangerous_ennemis_monsters = []
    ennemis = []

    for entity in range(entity_count):

        data = input().split()

        if data[1] == "0": # Si c'est un monstre, on l'enregistre dans les monstres
            x = int(data[2])
            y = int(data[3])
            monster_data = {
                "id": int(data[0]),
                "coords": {"x": x, "y": y}, # Sa position actuelle
                "SHIELD": bool(int(data[4])), # S'il a un SHIELD
                "CONTROL": bool(int(data[5])), # S'il est sous CONTROL
                "hp": int(data[6]),
                "move": {"x": int(data[7]), "y": int(data[8])}, # Les coords de son vecteur vitesse
                "next_coords": {"x": x + int(data[7]), "y": y + int(data[8])}, # Ses coords le tour suivant
                "attacking": bool(int(data[9])),
                "dangerous": int(data[10]) # S'il risque d'atteindre dataase
            }
            monsters.append(monster_data)
            # On l'enregisre dans la liste des dangereux s'il l'est
            if monster_data["dangerous"] == 1:
                dangerous_monsters.append(monster_data)
            # On l'enregistre dans la liste des dangereux pour l'ennemi s'il l'est
            if monster_data["dangerous"] == 2:
                dangerous_ennemis_monsters.append(monster_data)
                
        
        elif data[1] == "1": # Si c'est un de mes héros, on le mets dans la liste
            heros.append({
                "id": int(data[0]),
                "coords": {"x": int(data[2]), "y": int(data[3])}, # Sa position actuelle
                "SHIELD": bool(int(data[4])), # S'il a un SHIELD
                "CONTROL": bool(int(data[5])) # S'il est sous CONTROL
            })
        
        else: # Si c'est un héro ennemi
            ennemis.append({
                "id": int(data[0]),
                "coords": {"x": int(data[2]), "y": int(data[3])}, # Sa position actuelle
                "SHIELD": bool(int(data[4])), # S'il a un SHIELD
                "CONTROL": bool(int(data[5])) # S'il est sous CONTROL
            })


    # On classe les monstres dangereux par distance avec la base
    sortedbydist_danger_monsters = [] # La liste des id des monstres dangereux classés par distance avec la base
    # Pour chaque monstre dangereux
    for monster1 in dangerous_monsters:
        n = 0
        last = True
        for monster2_id in sortedbydist_danger_monsters:
            # On le mets avant celui qui est plus loin que lui
            if distance_coords(monster1["coords"], base_coords) < distance_coords(get(monsters, monster2_id)["coords"], base_coords):
                sortedbydist_danger_monsters.insert(n, monster1["id"])
                last = False
                break
            n += 1
        # S'il est moins dangereux que tous, on le met à la fin
        # Ça va aussi se déclencher si la liste est vide
        if last:
            sortedbydist_danger_monsters.append(monster1["id"])

    # La même mais pour l'adversaire    
    # On classe les monstres dangereux par distance avec la base ADVERSE
    sortedbydist_ennemis_monsters = [] # La liste des id des monstres dangereux classés par distance avec la base adverse
    # Pour chaque monstre tout court
    for monster1 in dangerous_ennemis_monsters:
        n = 0
        last = True
        for monster2_id in sortedbydist_ennemis_monsters:
            # On le mets avant celui qui est plus loin que lui
            if distance_coords(monster1["coords"], ennemis_base_coords) < distance_coords(get(monsters, monster2_id)["coords"], ennemis_base_coords):
                sortedbydist_ennemis_monsters.insert(n, monster1["id"])
                last = False
                break
            n += 1
        # S'il est moins dangereux que tous, on le met à la fin
        # Ça va aussi se déclencher si la liste est vide
        if last:
            sortedbydist_ennemis_monsters.append(monster1["id"])
    
    # Classement des ennemis en fonction de leur distance par rapport à leur base
    sortedbydist_ennemis = [] # Attention ! Ce sont seulement les ennemis visibles
    for ennemi1 in ennemis:
        n = 0
        last = True
        for ennemi2_id in sortedbydist_ennemis:
            # On le mets avant celui qui est plus loin que lui
            if distance_coords(ennemi1["coords"], ennemis_base_coords) < distance_coords(get(ennemis, ennemi2_id)["coords"], ennemis_base_coords):
                sortedbydist_ennemis.insert(n, ennemi1["id"])
                last = False
                break
            n += 1
        # S'il est plus loin que tous, on le met à la fin
        # Ça va aussi se déclencher si la liste est vide
        if last:
            sortedbydist_ennemis.append(ennemi1["id"])


    ##########
    # ACTION #
    ##########

    output = ["WAIT"] * heros_count


    ################
    # PREMIER HÉRO #
    ################

    # Le monstre le plus proche de la base ennemi qui est dangereux pour eux
    if sortedbydist_ennemis_monsters != []:
        closest_monster = get(monsters, sortedbydist_ennemis_monsters[0])
    else:
        closest_monster = None
    cible = None
    # L'ennemi le plus proche de sa base mais qui n'a pas de SHIELD
    for ennemi_id in sortedbydist_ennemis:
        if not get(ennemis, ennemi_id)["SHIELD"]:
            cible = get(ennemis, ennemi_id)
            break

    # On applique la tactique seulement s'il y a suffisament de mana
    if mana >= 10:
        # S'il y a un monstre et qu'il est du côté adverse
        if closest_monster is not None:
            # Techniquement, la limite est à 9897 de rayon mais on va compter 7000
            if distance_coords(closest_monster["coords"], ennemis_base_coords) <= 7000:

                # On prédit les positions du monstre dans 2 tours
                next_x_2round = closest_monster["coords"]["x"] + closest_monster["move"]["x"]
                next_y_2round = closest_monster["coords"]["y"] + closest_monster["move"]["y"]

                # On voit si on peut faire un WIND du monstre le plus proche de la base
                # Donc, on voit s'il est dans la portée du héro.
                if distance_coords(closest_monster["coords"], heros[0]["coords"]) <= 1280:
                    # On détermine le vecteur pour qu'il aille dans le direction de la base
                    # Ça va déterminer un parallélogramme comme en cours de maths
                    x = heros[0]["coords"]["x"] - closest_monster["coords"]["x"] + ennemis_base_coords["x"]
                    y = heros[0]["coords"]["y"] - closest_monster["coords"]["y"] + ennemis_base_coords["y"]
                    output[0] = "SPELL WIND " + str(x) + " " + str(y)
                
                # Si jamais en se déplaçant vers ses prochaines coords (rappel : MOVE = 800),
                # il devient à porté : on le fait, pour ensuite faire un WIND.
                elif distance_coords(closest_monster["next_coords"], heros[0]["coords"]) <= 1280 + 800:
                    output[0] = "MOVE " + str(closest_monster["next_coords"]["x"]) + " " + str(closest_monster["next_coords"]["y"])

                # Si jamais en se déplaçant vers ses prochaines coords dans 2 tours (rappel : MOVE = 800),
                # il devient à porté : on le fait, pour ensuite faire un WIND.
                elif distance(next_x_2round, next_y_2round, heros[0]["coords"]["x"], heros[0]["coords"]["y"]) <= 1280 + 1600:
                    output[0] = "MOVE " + str(next_x_2round) + " " + str(next_y_2round)

        # On voit un ennemi n'a pas de SHIELD
        # On ne fait pas de WIND au cas où il y a une araignée
        # et puis le WIND est trop court pour pouvoir le faire sur des entités qui bouge
        elif cible is not None:
            # On regarde s'il est à portée
            # On ne peut pas mettre sur la même ligne sinon il va y avoir une erreur car on fait None["coords"]
            if distance_coords(cible["coords"], heros[0]["coords"]) <= 2200:
                # Les coordonnées du vecteur vitesse pour l'éjecter de la base
                # C'est-à-dire le point ennemi' par la translation base-ennemi
                # Il est obtenu en multipliant la différence des coords de la base et de l'ennemi par 2
                eject_x = abs(cible["coords"]["x"] - ennemis_base_coords["x"]) * 2
                eject_y = abs(cible["coords"]["y"] - ennemis_base_coords["y"]) * 2
                output[0] = f"SPELL CONTROL {cible['id']} {eject_x} {eject_y}"
            
            # S'il est hors de portée, on teste si jamais en se déplaçant, il pourrait possiblement devenir à porté
            # C'est seulement possiblement car on ne sait pas dans quelle direction il va se déplacer.
            elif distance_coords(cible["coords"], heros[0]["coords"]) <= 2200 + 800:
                # Dans ce cas, on se déplace vers ses prochaines coords pour ensuite faire un CONTROL
                output[0] = "MOVE " + str(cible["coords"]["x"]) + " " + str(cible["coords"]["y"])

    # Dans la situation où aucune des conditions du haut ne sont validées
    # On se met en SHIELD ou si on l'a déjà, on va en position centrale d'attaque
    if output[0] == "WAIT":
        if not heros[0]["SHIELD"] and mana >= 10:
            output[0] = "SPELL SHIELD " + str(heros[0]["id"])
        else:
            output[0] = "MOVE " + str(attack[0]) + " " + str(attack[1])
    
    # On écrit la sortie du héro 1
    print(output[0])


    #################
    # 2e & 3e HÉROS #
    #################

    # Pour chaque monstre, on assigne le héro le plus proche parmi les 2 défensifs
    # On cible juste 2 monstres
    for monster_id in sortedbydist_danger_monsters[:1]:
        # La liste des distances entre chaque héro et le monstre
        dists_hero = []
        monster_coords = get(monsters, monster_id)["coords"]
        for hero in heros[1:]: # On ne compte pas le premier héro
            dists_hero.append(distance_coords(monster_coords, hero["coords"]))
        # On créé la sortie
        hero_index = dists_hero.index(min(dists_hero)) + 1
        output[hero_index] = "MOVE " + str(monster_coords["x"]) + " " + str(monster_coords["y"])
        # On enlève le héro qui devient occupé comme ça l'autre bosse aussi
        heros.pop(hero_index)

    n = 0
    for out in output[1:]:
        # Celui qui fait rien, on le met sur le plus proche s'il y a au moins un monstre
        if out == "WAIT" and len(sortedbydist_danger_monsters) != 0:
            monster = get(monsters, sortedbydist_danger_monsters[0])
            print("MOVE " + str(monster["coords"]["x"]) + " " + str(monster["coords"]["y"]))
        # S'il y a pas de monstre, on reprend les positions de défense
        elif out == "WAIT":
            print("MOVE " + str(defense[n][0]) + " " + str(defense[n][1]))
        else:
            print(out)
        n += 1