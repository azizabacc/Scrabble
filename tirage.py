""" remplir chevalet et reinitialisation de la pioche"""
def tirage(chevalet,pioche):
    while len(chevalet)<7:
        random.shuffle(pioche) # melange la pioche
        chevalet.append(pioche[0]) # le chevalet prend a chaque fois le premier element da liste pioche apres l'avoir melange
        pioche.remove(pioche[0])
        if pioche==[]:
            print("La pioche est vide")
     return chevalet
