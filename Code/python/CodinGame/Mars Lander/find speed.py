""" gravity = 3.711

def datas(*temps):
    ""Renvoi des informations importantes sur le rover.

    Returns
    ---
        infos: dict
            config = Les temps pour chaque puissance (*temps).
            vitesse = La vitesse que le rover aura lors une fois que les temps se seront écoulés.
            carburant = Le carburant consommé au total.
            distance = La distance parcourue.""
    vitesse = 0
    carburant = 0
    distance = 0
    n_puissance = 0
    for temps_puissance in temps:
        vitesse += (gravity - n_puissance) * temps_puissance ** 2
        carburant += n_puissance * temps_puissance
        distance += vitesse
        n_puissance += 1
    infos = {
        "config": temps,
        "vitesse": vitesse,
        "carburant": carburant,
        "distance": distance
    }
    return infos

while True:
    t_chute = int(input())
    t1 = int(input())
    t2 = int(input())
    t3 = int(input())
    t4 = int(input())
    print(datas(t_chute, t1, t2, t3, t4))

configs = []
for temps_chute in range(10):
    for temps_power1 in range(30):
        for temps_power2 in range(30):
            for temps_power3 in range(30):
                for temps_power4 in range(30):
                    infos = datas(temps_chute, temps_power1, temps_power2, temps_power3, temps_power4)
                    if infos["distance"] >= 5000:
                        configs.append(infos)

def sort_by_carburant(config):
    return config["carburant"]

sorted(configs, key=sort_by_carburant)

print(configs[:50])"""