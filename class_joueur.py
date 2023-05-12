
def tirage_multi_joueur(liste_joueur):
    for i in range(NB_JOUEURS):
        liste_joueur[i][1]=tirage(liste_joueur[i][1],PIOCHE)#tous les joueurs piochent


def tour(liste_joueur):
    tirage_multi_joueur(liste_joueur)
    i=0
    while i<len(liste_joueur):
        coup=propose_mot(msg_position_ligne,msg_position_colonne,msg_direction,msg_mot)
        test_mot=mot_accepte(PLATEAU,liste_joueur[i][1] , coup, DICO, TOUR)
        if test_mot==True:
            mot_formés=mots_perpendiculaires(coup,PLATEAU,DICO)
        for mot in mot_formés :
            liste_joueur[i][2]+=compte_points(mot,POINTS_LETTRES)
        TOUR+=1
        
def jeu(liste_joueur):
    while len(PIOCHE)>=1:
        tirage_multi_joueur(liste_joueur)
        tour(liste_joueur)
        
