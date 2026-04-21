import random

alphabet = " ABCDEFGHIKLMNOPQRSTUVWXYZ"

mini = input("min : ")
maxi = input("max : ")

file_random = open("/home/imstlth/Code/random_objectif_" + mini + "_" + maxi, "w")
for i in range(500):
    file_random.write("".join([random.choice(alphabet) for letter in range(random.randint(int(mini), int(maxi)))]) + "\n")
file_random.close()