# Fonction etape1


def etape1(chaine):
    n = len(chaine)
    chainebis = ""
    for i in range(n):
        if i % 2 == 0:
            temp = int(chaine[i]) * 2
            if temp > 9:
                temp = temp - 9
            chainebis = chainebis + str(temp)
        else:
            chainebis = chainebis + str(chaine[i])
    print("Le resultat obtenu est : ", chainebis)
    return (chainebis)

# fonction sommeChiffre


def sommeChiffre(chaine):
    n = len(chaine)
    somme = 0
    for i in range(n):
        a = int(chaine[i])
        somme = somme + a
    dif = somme % 10
    cle = 10 - dif
    return somme, cle


# Programme principal (main)
carteBancaire = input(
    "Saisir les 15 chiffres affichés sur la carte bancaire :")
chaine = etape1(carteBancaire)
somme, cle = sommeChiffre(chaine)
print("La somme des 15 chiffres obtenus lors de l'étape 1 est :", somme)
print("La clé de Lunh est : ", cle)
chiffre = input("Saisir le dernier chiffre de la carte bancaire: ")
if chiffre != cle:
    print("Le numero correspond à la clé de lunh !")
else:
    print("Le numero correspond pas à la clé de lunh !")
