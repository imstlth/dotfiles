alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
objectif = input()
output = ""
for letter in objectif:
    output += "+" * alphabet.index(letter) + ".>"
print(output[:-1])