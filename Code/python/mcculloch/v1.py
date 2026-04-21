#!/bin/python3

# Version 1 de la machine de McCulloch dans "Le livre qui rend fou".
# Règles :
# Règle 1: Pour tout nombre X le nombre 2X, formé du chiffre 2 suivi des chiffres de X, est acceptable, et il donne X.
# Règle 2: Si X est un nombre acceptable qui donne Y, alors 3X est acceptable et il donne l'associé de Y.

def acceptable(nombre):
    if nombre.startswith("2") or nombre.startswith("3"):
        return True
    else:
        return False

def main(nombre):
    if not acceptable(nombre):
        return "Not acceptable."
    Y = nombre[1:]
    if nombre.startswith("2"):
        if Y == "":
            return "Not acceptable."
        return Y
    elif nombre.startswith("3"):
        if not acceptable(Y):
            return "Not acceptable."
        resultY = main(Y)
        return resultY + "2" + resultY

while True:
    nombre = input("Input: ")
    if nombre == "exit":
        exit()
    try:
        result = main(nombre)
        print("Output: " + result)
    except:
        print("Not acceptable.")
