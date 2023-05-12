def mot_accepte(plateau, lettres_joueur, coup, dico, tour):
    resultat=False
    test1=verif_bornes(coup,(len(plateau),len(plateau[0])))
    test2_1=verif_premier_tour(coup)
    test2_2=verif_lettres_joueur(plateau, lettres_joueur, coup)
    test3=verif_mot(coup[0],dico)
    test4=verif_emplacement(coup,plateau)
    test_final_1=(test2_1 and test4)
    test_final_2=(test2_2 and test4)
    if test1 and test3 :
        if tour==True:
            if (test_final_1) :
                resultat=True
        else:
            if (test_final_2):
                resultat=True
    return resultat
