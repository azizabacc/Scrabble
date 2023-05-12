def pioche_unitaire(liste_joueur,liste_triee,pioche):
    random.shuffle(pioche)
    liste_joueur[i][1].append(pioche[0])
    liste_triee.append(pioche[0])
    """-Chaque joueur pioche A tour de rôle une lettre dans la pioche
       -Celui qui obtient la lettre la plus proche de A (dans l'ordre alphabétique) joue en premier.
       - Si plusieurs joueurs ont pioché la même lettre, ils piochent chacun une nouvelle lettre dans le pioche.
       - le gagnant joue le premier, l'odre ensuite se fera par l'ordre de l'aiguille d'une montre"""
def ordre_de_passage(liste_joueur,pioche):
    liste_triee=[]
    premiere_lettre=[]
    for i in range(int(NB_JOUEURS)):
        pioche_unitaire()
    liste_triee.sort()
    premiere_lettre=liste_triee.cout(liste_triee[0])
    while premiere_lettre != 1:
        premiere_lettre=[]
        liste_triee=[]
        list_prioritaire=[]
        for i in range(NB_JOUEURS):
            if liste_triee[0] in liste_joueur[i][1]:
                list_prioritaire.append(liste_joueur[i][0])
                pioche_unitaire()
                liste_triee.sort()
                premiere_lettre=liste_triee.cout(liste_triee[0])
        
    if liste_joueur[i][1][len(liste_joueur[i][1])-1]==liste_triee[0]:
            ordre_passage=[]
            a=[]# liste de tuples (type liste_joueur) intermediaire pour effectuer la copie
            ordre_passage.extend(liste_joueur[i:])
            if i!=0:
                a.extend(liste_joueur[0:i])
                liste_joueur=[]
                liste_joueur=ordre_passage+a""" ajouter le reste de la liste de tuples """
            else:
                liste_joueur=[]
                liste_joueur=ordre_passage
    return liste_joueur#liste triée par ordre de passage des joueurs 

            
            

 


                
                
        
    
