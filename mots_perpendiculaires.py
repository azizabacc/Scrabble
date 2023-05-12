"""fonction qui copie un mot vertical partant d'une lettre du plateau vers le bas du plateau """
def mot_vertical_haut_vers_bas(plateau,i,j,pos):
    p=0
    mot=''
    mot+=plateau[i][j+pos]#lettre de depart a la position [i][j+pos]
    if plateau[i+1+p][j+pos]!="_" :
        mot+=plateau[i+1+p][j+pos]#copier toute les lettres adjacentes vers le bas jusqu'a la rencontre d'une case vide
        p+=1
    return mot
"""fonction qui copie un mot vertical partant d'une lettre du plateau vers le haut du plateau """   
def mot_vertical_bas_vers_haut(plateau,i,j,pos):#meme raisonnement mot_vertical_haut_vers_bas mais en effectuant une copie dans le sens inverse
    p=0
    mot=''
    mot+=plateau[i][j+pos]#lettre de depart a la position [i][j+pos]
    if plateau[i-1-p][j+pos]!='_'  ::#meme raisonnement mot_vertical_haut_vers_bas mais en effectuant une copie dans le sens inverse
        mot+=plateau[i-1-p][j+pos]
        p+=1
    return mot
"""fonction qui copie un mot horizontal partant d'une lettre du plateau vers la gauche du plateau """
def mot_horizontal_gauche(plateau,i,j,pos):
    p=0
    mot=''
    mot+=plateau[i+pos][j]#lettre de depart a la position [i][j+pos]
    while plateau[i+pos][j-1-p]!='_':#copier toute les lettres adjacentes vers la gauche jusqu'a la rencontre d'une case vide
        mot+=plateau[i+pos][j-1-p]
        p+=1
    return mot
    """fonction qui copie un mot horizontal partant d'une lettre du plateau vers la droite du plateau """
def mot_horizontal_droit(plateau,i,j,pos):
    p=0
    mot=''
    mot+=plateau[i+pos][j]#lettre de depart a la position [i][j+pos]
    while plateau[i+pos][j+1+p]!='_' :#copier toute les lettres adjacentes vers la droite jusqu'a la rencontre d'une case vide
        mot+=plateau[i+pos][j+1+p]
        p+=1
    return mot
    
"""fonction qui renvoie un mot inverse"""
def inverse(mot):
    mot_inverse=''
    for lettre in mot:
        mot_inverse = lettre + mot_inverse #on ajoute la lettre en premier
    return mot_inverse
""" formation de mots perpendiculaires au nouveau mot """
def mots_perpendiculaires(coup,plateau,dico) :
    i=coup[1][0]#ligne de la premiere lettre du mot a placer
    j=coup[1][1]#colonne de la premiere lettre du mot a placer
    direction=coup[2]#direction du mot a placer 'v' ou 'h'
    lettres_presentes = placer_mot(coup,plateau)
    A=[]#liste a renvoyer a la fin contenant tous les nouveaux mots formes
    if direction=='h':
        pos=0
        while pos<len(coup[0]):#parcours de tout le mot placé
            m1=inverse(mot_vertical_bas_vers_haut(plateau,i,j,pos))
            print('m1 avant if: ',m1)
            m2=mot_vertical_haut_vers_bas(plateau,i,j,pos)
            print('m2 avant if: ',m2)
            if len(m1)>1 and len(m2)>1:# mots de part et d'autre de la lettre du plateau
                m3=m1[0:len(m1)-1]
                print('m1 + M2 :',m3+m2) 
                A.append(m3+m2)
            elif len(m1)>1 and len(m2)==1:# mot qu'en haut de la lettre du plateau
                print('m1: ',m1)
                A.append(m1)
            elif len(m1)==1 and len(m2)>1:# mot qu'en bas de la lettre du plateau
                print('m2: ',m2)
                A.append(m2)
            pos+=1
    if direction=='v':
        pos=0
        while pos<len(coup[0]):
            m1=inverse(mot_horizontal_gauche(plateau,i,j,pos))
            print('m1 avant if: ',m1)
            m2= mot_horizontal_droit(plateau,i,j,pos)
            print('m2 avant if: ',m2)
            if len(m1)>1 and len(m2)>1:# mots de part et d'autre de la lettre du plateau
                m3=m1[0:len(m1)-1]
                print('m1 + M2 :',m3+m2) 
                A.append(m3+m2)
            elif len(m1)>1 and len(m2)==1:# mot qu'a gauche de la lettre du plateau
                print('m1: ',m1)
                A.append(m1)
            elif len(m1)==1 and len(m2)>1:# mot qu'a droite de la lettre du plateau
                print('m2: ',m2)
                A.append(m2)
            pos+=1
    A.append(coup[0])#affecter le mot place a la liste
    test=utilise_lettre_plateau(coup,plateau)#test s'il y a des lettres du mot place deja sur le plateau
    if test==True:
        l=len(lettres_presentes)
        i=1
        while i <=l :
            del A[0]
            i+=1
    
    index=0
    resultat_dico_test=[]
    while index<len(A):#verifie si les mots formes sont dans le dictionnaire
        resultat_dico_test.append(verif_mot(A[index],dico))
        index+=1
    print(resultat_dico_test)
    if False in resultat_dico_test:
        A=[]
    A.sort()
    return A#liste des mots formes 
