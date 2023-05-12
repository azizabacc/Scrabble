""" fonction qui a pour parametre occurences_lettres avec :
- occurences_lettres.keys=lettre
- occurences_lettres.values=occurence de la lettre
cette fonction retourne une liste triee de toutes les l'etre a disposition """
def pioche_init(occurences_lettres):
	liste=[]
	for lettre in occurences_lettres:
		liste+=[lettre]*occurences_lettres[lettre]
	liste.sort()
	return liste
