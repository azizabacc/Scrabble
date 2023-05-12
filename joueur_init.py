def joueur_init():
    liste_joueur=[]
    for i in range(int(NB_JOUEURS)):
        nom=input("Saisir le nom du joueur")
        j=(nom,[],0)
        liste_joueur.append(j)#liste de tuples, chaque tuple caractérise un joueur (nom_jour,chevalet,score)


