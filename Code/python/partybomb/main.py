fichier = open("/home/caracole/Code/python/partybomb/list_fr.txt")
liste = fichier.read().splitlines()
fichier.close()

def tri(mot):
    score = 0
    for lettre in "abcedfghijklmnopqrstuvwxyz":
        score += lettre in mot.lower()
    return score

while True:
    lettres = input()
    matchs = []
    for mot in liste:
        if lettres.lower() in mot.lower():
            matchs.append(mot)
    best_lettres = sorted(matchs, key=tri)[::-1]
    best_len = sorted(matchs, key=len)[::-1]
    print("+ varié : ", best_lettres[:2])
    print("+ long : ", best_len[:2])
    print("+ court : ", best_len[-2:])
    print()
