#!/bin/python3

# Version 1 de la machine de McCulloch dans "Le livre qui rend fou".
# Règles :
# Règle 1: Pour tout nombre X le nombre 2X, formé du chiffre 2 suivi des chiffres de X, est acceptable, et il donne X.
# Règle 2: Si X est un nombre acceptable qui donne Y, alors 3X est acceptable et il donne l'associé de Y.
# Règle 3: Si X donne Y, le nombre 4X donne le retourné de Y.
# Règle 4: Si X donne Y, alors 5X donne YY.

def acceptable(nombre):
    accept_list = [2, 3, 4, 5]
    for a in accept_list:
        if nombre.startswith(str(a)):
            re = True
            break
        else:
            re = False
    return re


def main(nombre):
    if not acceptable(nombre):
        return "Not acceptable."
    Y = nombre[1:]
    if nombre.startswith("2"):
        if Y == "":
            return "Not acceptable."
        return Y
    else:
        if not acceptable(Y):
            return "Not acceptable."
        resultY = main(Y)
    if nombre.startswith("3"):
        return resultY + "2" + resultY
    elif nombre.startswith("4"):
        return resultY[::-1]
    elif nombre.startswith("5"):
        return resultY * 2


while True:
    nombre = input("Input  : ")
    if nombre == "exit":
        exit()
    try:
        result = main(nombre)
        if result is not None:
            print("Output : " + str(result))
    except:
        print("Not acceptable.")
