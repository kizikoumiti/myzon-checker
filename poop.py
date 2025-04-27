import random

def generer_numeros(nb):
    numeros = []
    for _ in range(nb):
        # Générer 8 chiffres aléatoires
        suite = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        numero = '06' + suite
        numeros.append(numero)
    return numeros

def sauvegarder_numeros(numeros, nom_fichier="numeros.txt"):
    with open(nom_fichier, "w") as f:
        for numero in numeros:
            f.write(numero + "\n")
    print(f"{len(numeros)} numéros enregistrés dans '{nom_fichier}'.")

if __name__ == "__main__":
    nb = int(input("Combien de numéros veux-tu générer ? "))
    resultats = generer_numeros(nb)
    sauvegarder_numeros(resultats)
