""" fonction qui traitement toutes les conditions requises au placement du nouveau mot sur plateau """
def verif_bornes(coup,dimensions): #coup=propose_mot(l,c,d,m) et dimensions=(NB_LIGNE,NB_COLONNE)
    l=len(coup[0])#longueur du mot
    resultat = True
    direction=coup[2]#'v' ou 'h'
    if direction=='h' and l>dimensions[1]-coup[1][1]: #cas d'un mot horizontal
        print('mot trop long, faites une nouvelle tentative')
        resultat=False
    elif direction=='v' and l>dimensions[0]-coup[1][0]: #cas d'un mot vertical
        print('mot trop long, faites une nouvelle tentative')
        resultat=False 
    return resultat

