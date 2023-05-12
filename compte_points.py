"""fonction qui donne la valeur en points d'un mot"""
def compte_points(mot, points_lettres):
    i=0
    score=0
    while i <len(mot):
        point=points_lettres.get(mot[i])
        score+=point
        i+=1
    return score
