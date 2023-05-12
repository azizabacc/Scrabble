""" verifier que le mot a placer ne rentre pas en conflit avec d'autres mot du plateau
=> tester si lettre du plateau correspond ou case vide """
def verif_emplacement(coup,plateau):
    l=coup[1][0]
    c=coup[1][1]
    resultat=True
    if coup[2]=='h':#mot horizontal
        i=0
        while i <len(coup[0]):
            if plateau[l][i+c]==coup[0][i] or plateau[l][i+c]=='_':
                i+=1
            else:
                resultat=False
                i+=1
    elif coup[2]=='v':#mot vertical
        i=0
        while i <len(coup[0]):
            if plateau[l+i][c]==coup[0][i] or plateau[l+i][c]=='_':
                i+=1
            else:
                resultat=False
                i+=1
    return resultat
