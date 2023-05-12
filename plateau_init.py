def plateau_init(dimensions):
	nb_lignes=dimensions[0]
	nb_colonnes=dimensions[1]
	plateau=[]
	sous_liste=[]
	sous_liste=['_']*nb_colonnes#sous_liste = une ligne du plateau
	plateau=[sous_liste]*nb_lignes#multiplier la sous_liste par le nombre de lignes
	return plateau
""" - fonction dont les parametres (tuple) sont les dimensions du plateau ( NB_LIGNES et NB_COLONNES)
    - retourne le plateau = liste de sous listes """
