"""  verification premier tour : passage par le centre du plateau """
def verif_premier_tour(coup):
    resultat =False
    if coup[2]=='h':
        for i in range(len(coup[0])):
            if i+coup[1][1]==(len(plateau)-1)//2 - 1:# ou ((NB_COLONNES-1)//2-1)
                resultat=True
    elif coup[2]=='v':
        for i in range(len(coup[0])):
            if i+coup[1][0]==(len(plateau[1][1])-1)//2 - 1:# ou((NB_LIGNES-1)//2-1)
                resultat=True
    return resultat
