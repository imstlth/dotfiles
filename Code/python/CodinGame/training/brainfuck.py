import subprocess
import random

mini = input("min  : ")
maxi = input("max  : ")

file_random = open("/home/imstlth/Code/random_objectif_" + mini + "_" + maxi, "r")
random_objectif = file_random.read().split("\n")
file_random.close()

def score_code(iterations, program):
    sum_score = 0
    for i in range(iterations):
        objectif = random_objectif[i]
        sum_score += len(subprocess.check_output(f"/bin/echo '{objectif}' | python3 {program}", shell=True))
    return sum_score / iterations

print(score_code(int(input("iter : ")), input("prog : ")))