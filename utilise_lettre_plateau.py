""" fct avancee bool retourne true si nouveau mot utilise lettre du plateau """
def utilise_lettre_plateau(coup,plateau):
    i=coup[1][0]#ligne de la premiere lettre du mot a placer
    j=coup[1][1]#colonne de la premiere lettre du mot a placer
    resultat=False 
    l=0
    while l<len(coup[0]):
        if coup[2]=='h':
            if plateau[i][j+l]==coup[0][l]:# defile le mot place horizontement et teste si une lettre du mot est deja placee sur le plateau
                resultat=True
                l+=1
            else:
                l+=1
        elif coup[2]=='v':
            if plateau[i+l][j]==coup[0][l]:# defile le mot place horizontement et teste si une lettre du mot est deja placee sur le plateau
                resultat=True
                l+=1
            else:
                l+=1
    return resultat
