import random
import time

FichierSource = "DixLettres.txt"


def anagramme(mot):
    """ retourne l'anagramme d'un mot
    """
    global nouveau
    mot = list(mot)
    nouveau = ""
    for i in range(0, len(mot)):
        index = random.randrange(0, len(mot))
        nouveau += mot[index]
        del mot[index]


fichier = open(FichierSource, "r")
liste = fichier.readlines()
fichier.close()
temp = ".".join(liste)
liste = temp.split("\n.")
liste2 = []

for mot in liste:
    anagramme(mot)
    liste2.append(nouveau)


launched = 1
while (launched == 1):
    n = int(input("\nNombre de mots : "))
    compteur = point_essai = 0
    point_total = 0
    for i in range(n):
        index = random.randint(0, len(liste2) - 1)
        print(f"\n({i + 1}/{n}) {liste2[index]}")

        essai = input("--> ")
        point1 = len(essai)
        point_essai += point1
        point2 = len(liste2[index])
        point_total += point2

        if essai.upper() == liste[index]:
            print("Bingo")
            compteur += 1
        else:
            print("Désolé, c'était ---", liste[index])

    time.sleep(1)
    print("\nVous avez eu", compteur, "bonnes réponses sur", n)
    print("Vous obtenez", point_essai, "points sur", point_total)
    time.sleep(1)
    launched = int(input("\nOn repart ? (Si oui, tapez 1) "))
