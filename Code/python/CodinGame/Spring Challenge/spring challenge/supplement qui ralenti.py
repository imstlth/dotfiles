if pair % 2 == 0:

                        if bool(up[tour]):
                            count = 0
                            for t in range(up[tour][0][1], up[tour][-1][1]):
                                if t != up[tour][count][1]:
                                    n = 0
                                    for e in bouboules_x:
                                        if e == up[tour][0][0] and bouboules_y[n] == t:
                                            bouboules_y.pop(n)
                                            bouboules_x.pop(n)
                                            break
                                        n += 1
                                else:
                                    count += 1
                        else:
                            n = 0
                            for e in mur_x:
                                if e == xm[tour] and mur_y[n] == ym[tour] - 1:
                                    break
                                else:
                                    a = 0
                                    for r in bouboules_x:
                                        if r == xm[tour] and bouboules_y[a] == ym[tour] - 1:
                                            bouboules_y.pop(a)
                                            bouboules_x.pop(a)
                                            break
                                        a += 1
                                n += 1
                        if bool(right[tour]):
                            count = 0
                            for t in range(right[tour][0][0], right[tour][-1][0]):
                                if t != right[tour][count][0]:
                                    n = 0
                                    for e in bouboules_x:
                                        if e == t and bouboules_y[n] == right[tour][0][1]:
                                            bouboules_y.pop(n)
                                            bouboules_x.pop(n)
                                            break
                                        n += 1
                                else:
                                    count += 1
                        else:
                            n = 0
                            for e in mur_x:
                                if e == xm[tour] + 1 and mur_y[n] == ym[tour]:
                                    break
                                else:
                                    a = 0
                                    for r in bouboules_x:
                                        if r == xm[tour] + 1 and bouboules_y[a] == ym[tour]:
                                            bouboules_y.pop(a)
                                            bouboules_x.pop(a)
                                            break
                                        a += 1
                                n += 1
                        if bool(down[tour]):
                            count = 0
                            for t in range(down[tour][0][1], down[tour][-1][1]):
                                if t != down[tour][count][1]:
                                    n = 0
                                    for e in bouboules_x:
                                        if e == down[tour][0][0] and bouboules_y[n] == t:
                                            bouboules_y.pop(n)
                                            bouboules_x.pop(n)
                                            break
                                        n += 1
                                else:
                                    count += 1
                        else:
                            n = 0
                            for e in mur_x:
                                if e == xm[tour] and mur_y[n] == ym[tour] + 1:
                                    break
                                else:
                                    a = 0
                                    for r in bouboules_x:
                                        if r == xm[tour] and bouboules_y[a] == ym[tour] + 1:
                                            bouboules_y.pop(a)
                                            bouboules_x.pop(a)
                                            break
                                        a += 1
                                n += 1
                        if bool(left[tour]):
                            count = 0
                            for t in range(left[tour][0][0], left[tour][-1][0]):
                                if t != left[tour][count][0]:
                                    n = 0
                                    for e in bouboules_x:
                                        if e == t and bouboules_y[n] == left[tour][0][1]:
                                            bouboules_y.pop(n)
                                            bouboules_x.pop(n)
                                            break
                                        n += 1
                                else:
                                    count += 1
                        else:
                            n = 0
                            for e in mur_x:
                                if e == xm[tour] - 1 and mur_y[n] == ym[tour]:
                                    break
                                else:
                                    a = 0
                                    for r in bouboules_x:
                                        if r == xm[tour] - 1 and bouboules_y[a] == ym[tour]:
                                            bouboules_y.pop(a)
                                            bouboules_x.pop(a)
                                            break
                                        a += 1
                                n += 1
