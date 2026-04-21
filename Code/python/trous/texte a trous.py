import random
import math
import colorama
import time
import sys

def new_print(text):
    for caract in text:
        sys.stdout.write(caract)
        sys.stdout.flush()
        time.sleep(0.05)

colorama.init()

while True:

    def color_input(text):
        return input(colorama.Back.LIGHTWHITE_EX + colorama.Fore.BLACK + text + colorama.Fore.RESET + colorama.Back.RESET + " " + colorama.Fore.BLUE)

    text_file = color_input("Entrez le texte :")
    text_file = open(text_file)
    text = text_file.read().split("\n")
    for line_number in range(len(text)):
        text[line_number] = text[line_number].split(" ")
    text_file.close()
    ntrous = int(color_input("Combien voulez-vous de trous ?"))
    long = int(input(colorama.Back.LIGHTWHITE_EX + colorama.Fore.BLACK + "Quelle longueur devront faire les trous" + colorama.Fore.RESET + colorama.Back.RESET + colorama.Fore.MAGENTA + " - en nombre de mots" + colorama.Fore.RESET + " (Recommandé : 2) ? " + colorama.Fore.BLUE))

    bookmark = int(color_input("À quel endroit vous étiez ?"))

    len_text = 0
    for line in text:
        len_text += len(line)

    emp_div = list(range(math.floor(len_text / long)))  # Liste des emplacements divisé par "long"
    trous_div = []  # Emplacement, divisé par "long", des trous

    for i in range(ntrous):
        emp = random.choice(emp_div)
        emp_div.pop(emp_div.index(emp))
        trous_div.append(emp)

    trous = []
    for trou in trous_div:
        trous.append(trou * long)
        minus = 0
        while minus != long - 1:
            minus += 1
            trous.append(trou * long - minus)

    index = 0
    end = True
    for line in text:
        for word in line:
            if word != "":
                if index in trous or (not end and word[0].isupper()) or word.isnumeric() or word[:-1].isnumeric():
                    reponse = input().lower()
                    lower_word = word.lower()
                    if reponse == lower_word or reponse == lower_word[:-1]:
                        new_print(" (" + colorama.Fore.GREEN + "✔" + colorama.Fore.RESET + ") ")
                    else:
                        new_print(" (" + colorama.Fore.RED + "✘ : " + word + colorama.Fore.RESET + ") ")
                else:
                    for letter in word:
                        new_print(letter)
                new_print(" ")
                time.sleep(0.07)
            index += 1
            end = (word.endswith(".") or word == "" or word.endswith("?") or word.endswith("/"))
        print()
        time.sleep(0.5)

    refaire = input("Refaire (Oui/non) ?")
    if refaire.lower() not in ["oui", "o"]:
        print("Bye !")
        break
