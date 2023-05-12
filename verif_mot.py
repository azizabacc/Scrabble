""" verification de l'excitence du mot dans le dictionnaire """
def verif_mot(mot,dico):
    resultat=False
    longueur_mot=len(mot)
    for element in dico:#element=ligne dico
        for word in element:#word= mot dans ligne
            if mot==word:
                resultat=True
    return resultat
