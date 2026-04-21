import math
import random

width, height = [int(i) for i in input().split()]
bouboules_x = []
bouboules_y = []
mur_x = []
mur_y = []
y = 0
for i in range(height):
    ligne = list(input())
    x = 0
    for t in ligne:
        if t == " ":
            bouboules_x.append(x)
            bouboules_y.append(y)
        elif t == "#":
            mur_x.append(x)
            mur_y.append(y)
        x += 1
    y += 1

avant_x = [[], []]
avant_y = [[], []]
pair = 0
# game loop
while True:

    input()

    idm = []
    xm = []
    ym = []
    typem = []
    ability_cooldownm = []

    xe = []
    ye = []
    typee = []

    up = []
    right = []
    down = []
    left = []

    avant_x.append([])
    avant_y.append([])

    dist_grosse = []
    dist = []
    mega_x = []
    mega_y = []
    pair += 1

    sortie = ""
    tour = 0
    for i in range(int(input())):
        pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown = input().split()
        if mine == "1":

            idm.append(int(pac_id))
            xm.append(int(x))
            ym.append(int(y))
            typem.append(type_id)
            ability_cooldownm.append(int(ability_cooldown))

            up.append([])
            right.append([])
            down.append([])
            left.append([])

            dist_grosse.append([])
            dist.append([])

            if pair == 1:
                avant_x[0].append(0)
                avant_y[0].append(0)
                avant_x[1].append(1)
                avant_x[1].append(1)
        else:
            xe.append(int(x))
            ye.append(int(y))
            typee.append(type_id)

        n = 0
        for t in bouboules_x:
            if t == int(x) and bouboules_y[n] == int(y):
                bouboules_y.pop(n)
                bouboules_x.pop(n)
            n += 1

    for i in range(int(input())):

        t = input().split()
        t0 = int(t[0])
        t1 = int(t[1])
        t2 = int(t[2])
        if t2 == 10:
            mega_x.append(t0)
            mega_y.append(t1)

        tour = 0
        for e in xm:
            if t0 == e:
                if t1 < ym[tour]:
                    up[tour].append([t0, t1])
                else:
                    down[tour].append([t0, t1])
            elif t1 == ym[tour]:
                if t0 < e:
                    left[tour].append([t0, t1])
                else:
                    right[tour].append([t0, t1])
            tour += 1

    n = 0
    for i in mega_x:
        c = 0
        for t in xm:
            dist_x = abs(i - t)
            dist_y = abs(mega_y[n] - ym[c])
            dist_grosse[c].append(math.sqrt(dist_x ** 2 + dist_y ** 2))
            c += 1
        n += 1

    n = 0
    for i in bouboules_x:
        c = 0
        for t in xm:
            dist_x = abs(i - t)
            dist_y = abs(bouboules_y[n] - ym[c])
            dist[c].append(math.sqrt(dist_x ** 2 + dist_y ** 2))
            c += 1
        n += 1

    if pair == 1:
        speed = [True] * len(idm)

    tour = 0
    for i in idm:

        if not speed[tour]:
            avant_x[-1].append(xm[tour])
            avant_y[-1].append(ym[tour])
        else:
            avant_x[-1].append(0)
            avant_y[-1].append(0)
        speed[tour] = False

        if bool(up[tour]):
            count = 0
            for t in range(up[tour][0][1], up[tour][-1][1]):
                if t != up[tour][count][1]:
                    n = 0
                    for e in bouboules_x:
                        if e == up[tour][0][0] and bouboules_y[n] == t:
                            bouboules_y.pop(n)
                            bouboules_x.pop(n)
                        n += 1
                else:
                    count += 1
        else:
            count = 0
            while True:
                n = 0
                breaking = False
                for t in mur_x:
                    if t == xm[tour] and mur_y[n] == ym[tour] - count:
                        breaking = True
                    else:
                        a = 0
                        for e in bouboules_x:
                            if e == xm[tour] and bouboules_y[a] == ym[tour] - count:
                                bouboules_y.pop(a)
                                bouboules_x.pop(a)
                            a += 1
                    n += 1
                if breaking:
                    break
                if count >= 10:
                    print("Bouh")
                count += 1
        if bool(right[tour]):
            count = 0
            for t in range(right[tour][0][0], right[tour][-1][0]):
                if t != right[tour][count][0]:
                    n = 0
                    for e in bouboules_x:
                        if e == t and bouboules_y[n] == right[tour][0][1]:
                            bouboules_y.pop(n)
                            bouboules_x.pop(n)
                        n += 1
                else:
                    count += 1
        else:
            count = 0
            while True:
                n = 0
                breaking = False
                for t in mur_x:
                    if t == xm[tour] + count and mur_y[n] == ym[tour]:
                        breaking = True
                    else:
                        a = 0
                        for e in bouboules_x:
                            if e == xm[tour] + count and bouboules_y[a] == ym[tour]:
                                bouboules_y.pop(a)
                                bouboules_x.pop(a)
                            a += 1
                    n += 1
                if breaking:
                    break
                if count >= 10:
                    print("Bouh")
                count += 1
        if bool(down[tour]):
            count = 0
            for t in range(down[tour][0][1], down[tour][-1][1]):
                if t != down[tour][count][1]:
                    n = 0
                    for e in bouboules_x:
                        if e == down[tour][0][0] and bouboules_y[n] == t:
                            bouboules_y.pop(n)
                            bouboules_x.pop(n)
                        n += 1
                else:
                    count += 1
        else:
            count = 0
            while True:
                n = 0
                breaking = False
                for t in mur_x:
                    if t == xm[tour] and mur_y[n] == ym[tour] + count:
                        breaking = True
                    else:
                        a = 0
                        for e in bouboules_x:
                            if e == xm[tour] and bouboules_y[a] == ym[tour] + count:
                                bouboules_y.pop(a)
                                bouboules_x.pop(a)
                            a += 1
                    n += 1
                if breaking:
                    break
                if count >= 10:
                    print("Bouh")
                count += 1
        if bool(left[tour]):
            count = 0
            for t in range(left[tour][0][0], left[tour][-1][0]):
                if t != left[tour][count][0]:
                    n = 0
                    for e in bouboules_x:
                        if e == t and bouboules_y[n] == left[tour][0][1]:
                            bouboules_y.pop(n)
                            bouboules_x.pop(n)
                        n += 1
                else:
                    count += 1
        else:
            count = 0
            while True:
                n = 0
                breaking = False
                for t in mur_x:
                    if t == xm[tour] - count and mur_y[n] == ym[tour]:
                        breaking = True
                    else:
                        a = 0
                        for e in bouboules_x:
                            if e == xm[tour] - count and bouboules_y[a] == ym[tour]:
                                bouboules_y.pop(a)
                                bouboules_x.pop(a)
                            a += 1
                    n += 1
                if breaking:
                    break
                if count >= 10:
                    print("Bouh")
                count += 1

        count = 0
        joue = False
        for t in xe:
            if (xm[tour] == t and ye[count] - 1 <= ym[tour] <= ye[count] + 1) or (ym[tour] == ye[count] and t - 1 <= xm[tour] <= t + 1):

                typee_ = typee[count]
                typem_ = typem[tour]
                moins = "PAPER"
                if typee_ == "ROCK":
                    moins = "SCISSORS"
                elif typee_ == "PAPER":
                    moins = "ROCK"
                if typem_ == moins:
                    if (xm[tour] == t):
                        if ye[count] - 1 < ym[tour]:
                            sortie += "MOVE " + str(i) + " " + str(xm[tour]) + " " + str((ym[tour] + 2) % height) + "|"
                        else:
                            sortie += "MOVE " + str(i) + " " + str(xm[tour]) + " " + str((ym[tour] - 2) % height) + "|"
                    else:
                        if t - 1 < xm[tour]:
                            sortie += "MOVE " + str(i) + " " + str((xm[tour] + 2) % width) + " " + str(ym[tour]) + "|"
                        else:
                            sortie += "MOVE " + str(i) + " " + str((xm[tour] - 2) % width) + " " + str(ym[tour]) + "|"
                    joue = True
                    break

            count += 1

        if not joue:

            if avant_x[-1][tour] == avant_x[-2][tour] and avant_y[-1][tour] == avant_y[-2][tour] and pair > 2:
                sortie += "MOVE " + str(i) + " " + str(random.randint(2, width - 2)) + " " + str(random.randint(2, height - 2)) + " RANDOM|"

            elif ability_cooldownm[tour] == 0:
                sortie += "SPEED " + str(i) + "|"
                speed[tour] = True

            elif len(mega_x) > 0:
                num = dist_grosse[tour].index(min(dist_grosse[tour]))
                sortie += "MOVE " + str(i) + " " + str(mega_x[num]) + " " + str(mega_y[num]) + " MEGA|"

            else:

                tout = [len(up[tour]), len(right[tour]), len(down[tour]), len(left[tour])]
                maxi = max(tout)
                num = tout.index(maxi)

                if maxi == 0:
                    num = dist[tour].index(min(dist[tour]))
                    sortie += "MOVE " + str(i) + " " + str(bouboules_x[num]) + " " + str(bouboules_y[num]) + " NORMAL|"
                else:

                    if num == 0:
                        sortie += "MOVE " + str(i) + " " + str(up[tour][-1][0]) + " " + str(up[tour][-1][1]) + " UP|"
                    elif num == 1:
                        sortie += "MOVE " + str(i) + " " + str(right[tour][-1][0]) + " " + str(right[tour][-1][1]) + " RIGHT|"
                    elif num == 2:
                        sortie += "MOVE " + str(i) + " " + str(down[tour][-1][0]) + " " + str(down[tour][-1][1]) + " DOWN|"
                    elif num == 3:
                        sortie += "MOVE " + str(i) + " " + str(left[tour][-1][0]) + " " + str(left[tour][-1][1]) + " LEFT|"

        tour += 1

    sortie = list(sortie)
    rien = sortie.pop()
    sortie = "".join(sortie)
    print(sortie)
