DICO=open('dico.txt', "r") #ouverture du fichier dico.txt
print("Dimensionnement du plateau :")#demander les nombre de lignes et colonnes du plateau
NB_LIGNES=input("Donnez le nombre de cases vertical du plateau de jeu")
    while int(NB_LIGNES)%2==0:
        NB_LIGNES=input("Donnez un nombre impair de cases vertical du plateau de jeu")
NB_COLONNES=input("Donnez le nombre de cases horizontal du plateau de jeu")
while int(NB_COLONNES)%2==0:
        NB_COLONNES=input("Donnez un nombre impair de cases horizontal du plateau de jeu")
DIMENSIONS=(int(NB_LIGNES),int(NB_COLONNES))
LETTRE_INFO=load_fichier_lettres(lettres.txt)
PLATEAU=plateau_init(DIMENSIONS)
OCCURENCES_LETTRES=LETTRE_INFO[0]#dictionnaire: cle(lettre) et valeur(occurence de la lettre)
POINTS_LETTRES=LETTRE_INFO[1]#dictionne: cle(lettre majuscule) et valeur(point de la lettre)
PIOCHE=pioche_init(OCCURENCES_LETTRES)#creation de la pioche
"""donnees joueurs"""
NB_JOUEURS=input("Saisir le nombre de joueurs :")
while int(NB_JOUEURS)<1:
    NB_JOUEURS=input("Saisir le nombre de joueurs, il faut minimum un joueur :")
    
LISTE_JOUEURS= joueur_init()#liste de tuples,triee par ordre de passage,
                            #chaque tuple (nom_jour,chevalet,score) caracterise un joueur (nom_jour,chevalet,score)
LISTE_JOUEURS=ordre_de_passage(LISTE_JOUEURS,PIOCHE)#meme liste mais triee par ordre de passage
msg_position_ligne="Donnez le numéro de la ligne de la première lettre"
msg_position_colonne="Donnez le numéro de la colonne de la première lettre"
msg_direction=" Tapez 'h' pour une direction horizontale et 'v' pour une direction verticale"
msg_mot=" Donnez votre proposition de mot "
TOUR=1
PREMIER_JEU=True
while len(PIOCHE)>=1:
    for i in range(int(NB_JOUEURS)):
        tirage(LISTE_JOUEURS[i][1],PIOCHE)#remplir le chevalet du joueur
        jeu_joueur(LISTE_JOUEURS[i])#propose et place mot/ affecte les points
    TOUR+=1
    PREMIER_JEU=True
"""dernierr tour, une fois la pioche vide"""
for i in range(int(NB_JOUEURS)):
    tirage(LISTE_JOUEURS[i][1],PIOCHE)#remplir le chevalet du joueur
    jeu_joueur(LISTE_JOUEURS[i])#propose et place mot/ affecte les points
""" qui gagne """
scores=[]#liste de tous les score
for i in range(len(LISTE_JOUEURS)):
    score[i].append(LISTE_JOUEURS[i][2])
score.list()
index=0
for i in range(len(LISTE_JOUEURS)):
    for scor in LISTE_JOUEURS[i][2]:
        if score[0]==scor:
           print(LISTE_JOUEURS[i][0],' gagne avec un score de : ',score[0],' au bout de ', TOUR,' tours.')
""" end. """
