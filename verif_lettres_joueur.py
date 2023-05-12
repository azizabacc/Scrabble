""" verification de l'excitence des lettres du mot entre le chevalet et le plateau """
def verif_lettres_joueur(plateau, lettres_joueur, coup):
#On pré-suppose que le mot ne depasse pas les bornes du plateau

    pos=[]
    resultat =True
    mot_list=list(coup[0])#creation d'un liste qui a pour elements toutes les lettres du mot
    commun_lettres_joueur_mot=[ i for i in mot_list if i in lettres_joueur]# liste avec lettres du mot issues du chevalet
    for i in mot_list:
        if i not in commun_lettres_joueur_mot:
            a=mot_list.index(i)
            pos.append((i,a))#liste de tuples avec les lettres ne prevenant pas du chevalet et leurs positions dans le mot
    j=int(coup[1][1]) #numero de colonne de la position de la premiere lettre
    i=int(coup[1][0]) #numero de ligne de la position de la premiere lettre
    if pos!=[]:# s'il y a des lettres non communes entre le mot et le chevalet=> evaluer si ces lettres son sur le plateau et a la bonne position
        if coup[2]=='h':
            for element in pos :
                if plateau[i][j+element[1]]!=element[0]:
                    resultat=False
        elif coup[2]=='v': 
            for element in pos :
                if plateau[i+element[1]][j]!=element[0]:
                    resultat=False
    return resultat
