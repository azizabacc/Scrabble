def load_fichier_lettres(file):
    lettres = open(file, "r")
    LETTRES=[]
    NOMBRES=[]
    POINTS=[]
    for line in lettres:
        LETTRES.append(line.strip().split()[0])#affectation du chaque colonne du fichier a une liste
        NOMBRES.append(line.strip().split()[1])
        POINTS.append(line.strip().split()[2])
    for p in range(len(NOMBRES)) :# changement de variable de char a int pour les occurences et les points
        NOMBRES[p]=int(NOMBRES[p])
        POINTS[p]=int(POINTS[p])
    occurences_lettres={}#initiallisation des dictionnaires
    points_lettres={}
    i=0
    while i<len(LETTRES):
        occurences_lettres[LETTRES[i]]=NOMBRES[i]
        points_lettres[LETTRES[i]]=POINTS[i]
        i+=1
    return occurences_lettres ,points_lettres
""" return :
- occurences_lettres : dictionaire keys=lettre et values=occurence
- points_lettres : dictionnaire keys=lettre et values=points """
