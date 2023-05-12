""" fonction qui demander au joueur le mot la position et la direction"""
def propose_mot(msg_position_ligne,msg_position_colonne,msg_direction,msg_mot):
    l=input(msg_position_ligne)
    while (int(l)<0) or (int(l)>=NB_LIGNES):# redemander tant que la position est hors du plateau
        l=input(msg_position_ligne)
    c=input(msg_position_colonne)
    while int(c) not in range(NB_COLONNES):
        c=input(msg_position_colonne)
    d=input(msg_direction)
    direction=["h","v","H","V"]
    while d not in direction :#redemander tant que d est different de h ou v
        d=input(msg_direction)
    m=input(msg_mot)
    i=0
    while i<len(m):#verification des lettres du mot
        if (ord(m[i]) in range(65,91)):#ascii lettres majuscules
            i+=1
        elif (ord(m[i]) in range(97,123)) :#ascii lettres minuscules
            i+=1
        else:# si une lettre n'appartient pass a l'alphabet redemander un nouveau mot
            m=input(msg_mot)
            i=0
    ligne1=int(l) # char => int
    colonne1=int(c)
    direc=d.lower()# 'v' ou 'h'
    mot_majuscule=m.upper() 
    return mot_majuscule, (ligne1,colonne1) , direc
