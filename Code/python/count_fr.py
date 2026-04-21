import sys

def replace(text, symbols, rep):
    for symbol in symbols:
        text = text.replace(symbol, rep)
    return text

texte = sys.argv[-1]
texte = replace(texte, "-',;:.?!\"", " ")
texte = texte.split(" ")

print(len(texte) - texte.count(""), "mots")
