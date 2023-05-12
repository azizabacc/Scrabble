def jeu_joueur(joueur):#tuple (nom_joueur,chevalet,score)
    chance=0
    test_mot=False
    while chance<=3 and test_mot==False: #chaque joueur a 3 tentatives de jeu sinon il passe son tour
        coup=propose_mot(msg_position_ligne,msg_position_colonne,msg_direction,msg_mot)
        test_mot=mot_accepte(PLATEAU,joueur[1], coup, DICO, TOUR)
        chance+=1
    if test_mot==True:
        mot_formes=mots_perpendiculaires(coup,PLATEAU,DICO)
        print('Vous avez forme : ',mot_formes,' mots.')
        affichage(PLATEAU)
    for mot in mot_formes :
        joueur[2]+=compte_points(mot,POINTS_LETTRES)
        print('Vous avez ',compte_points(mot,score),' vous atteignez un score total de ,',joueur[2]) 
    PREMIER_JEU=FALSE#apres le premier jeu il ne faut plus passer par le centre du plateau


