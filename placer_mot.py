""" fonction qui place le mot sur le plateau
cette fonction renvoie la liste de lettres utilisees du plateau"""
def placer_mot(coup,plateau):
    if coup[2]=='h':#placement d'un mot horizontal
        l=coup[1][0]#ligne de la premiere lettre du mot a placer
        c=coup[1][1]#colonne de la premiere lettre du mot a placer
        i=0
        lettres_presentes=''
        while i<len(coup[0]):
            if plateau[l][c]=='_':#cas d'une case vide
                plateau[l][c]=coup[0][i]#placer lettre du chevalt sur le plateau
                c+=1
                i+=1
            else:# cas de lettre presente sur le plateau
                lettres_presentes+=plateau[l][c]# ajouter cette lettre a la liste a renvoyer a la fin de la fonction 
                c+=1
                i+=1
    elif coup[2]=='v':#placement d'un mot vertical (meme raisonnement que pour 'h')
        l=coup[1][0]
        c=coup[1][1]
        i=0
        lettres_presentes=''
        while i<len(coup[0]):
            if plateau[l][c]=='_':
                plateau[l][c]=coup[0][i]
                l+=1
                i+=1
            else:
                lettres_presentes+=plateau[l][c]
                l+=1
                i+=1
    return lettres_presentes
