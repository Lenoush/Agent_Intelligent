import copy
from re import *
##AMELIORATION
# mon unite de temps est verife seulemet 1 fois par tour alors que 1 tour peut contenir 1 aspiration et 1 deplacement
# Essayer de faire des fonciton pour enlever les doublons dans la fonction aspirateur.
# Faire un fonction verifNbMemePosition



#La taille de l'environnement est choisie.
#Le pourcentage de saleté est choisie.
#Les positions de la saleté est aleatoire.
#La durée de vie, Unite de temps est imposée.

#PosAspi prend la valeur de la position de l'aspirateur a l'instant t : c'est le capteur de position.
#Le capteur de position marche seulement sur la position de l'aspirateur. il capte egalemnt si ilrets de la saleté dasn la salle mais ne sait pas où elle est. 

#Chaque aspiration, deplacement, mauvais deplacement prend 1 unité de temps.
#Dans AgentReflexeEtat() et AgentReflexeSimple() , l'aspirateur ce deplace en mode serpent , il va à la case (0,0) et commence son chemin.

#Dans AgentReflexeSimple() , l'aspirateur ne connait pas son environnement donc se prend les murs. Si sales il aspire sinon il se deplace. 
#Dans AgentReflexeEtat() , l'aspirateur connait son environnement donc ne se prend pas les murs, et indique combien de fois il est repassé sur une case.


##CREATION DE L'ENVIRONNEMENT :
# Creation Matrice Vide (avec seulement des 0)
def MatriceP(N) :
    matrice = []
    for i in range(N) :
        l =  []
        for j in range(N) :
            l.append("0")
        matrice.append(l)
    return(matrice)
#print(MatriceP(N))

# Transforme une Matrice lambda en grille à Jouer 
def plot_grid(M,N) :
    COLONNES = [" "] + [str(i) for i in range (N)]
    LIGNES = [str(i) for i in range (N)]
    PetiteListe = []
    L = [COLONNES]  #Les chiffres de la Grille     #L est une liste de liste
    VarIncrementé = 1
    for i in LIGNES : #i prend la valeur des lettres entre a et j
        PetiteListe = [i] + M[LIGNES.index(i)] 
        L.append(PetiteListe)
    for i in L :
        for j in i :
            if VarIncrementé % (N+1) == 0 :
                VarIncrementé = VarIncrementé +1
                print ( j , end=" \n")
            else :
                VarIncrementé = VarIncrementé +1
                print ( j , end =" ")
    return ""
# MatriceP(N)
# plot_grid(MatriceP)
# print(MatriceP[1][4])





## CREATION DE LA SALETE
import random
def Salete(Matrice,PourcentageS,N):
    NbSalete = round((N*N) * (PourcentageS/100)) # Le nombre de case sales  est un entier qui depends du nombre de cases total et du pourcentage de salete souhaite
    i=0 
    while i < NbSalete : #Tant que le nombre de cases sales est inf au nombre souhaité 
        L,C = random.randint(0,N-1),random.randint(0,N-1) #Position aleatoire de la salete 
        if (Matrice[L][C] == '0') : #Si a cette postion il n'a ni deja de la salte , ni un obstacle alors 
            Matrice[L][C] = '1' #on rajoute de la salete 
            i += 1
    return (Matrice,NbSalete)


# M = MatriceP(N)
# print(M)
# print(MatriceP(N))
# print(Salete(M,80))
# print(MatriceP(N))



##CREATION DE L'ASPIRATION
def VerifAspiration(M,PosAspi):
    #print(M)
    if (M[PosAspi[0]][PosAspi[1]] == "1") : #Si la case ,sur laquelle l'aspi est, est sale
        (M[PosAspi[0]][PosAspi[1]]) = "0" #on aspire et on rend propre
        print("Bravo tu as nettoyé la case " + str(PosAspi))
        Reponse = True #pour plus tard savoir si oui ou non la case etait sale
    else : Reponse = False
    #print(M)
    return (Reponse)
#VerifAspiration(Salete(N,PourcentageS),(3,2))


##CREATION DEPLACEMENT
def Droite(PosAspi): #verifie si l'aspirateur peux tourner a droite ou si il se prend le mur 
    PosAspi = (PosAspi[0],PosAspi[1]+1)
    print("L'aspirateur est allé à droite. Sur la case" , PosAspi)
    return (PosAspi)  
#Droite((3,4))

def Gauche(PosAspi): #verifie si l'aspirateur peux tourner a gauche ou si il se prend le mur
    PosAspi = (PosAspi[0],PosAspi[1]-1)
    print("L'aspirateur est allé à gauche. Sur la case" , PosAspi)
    return (PosAspi)
#Gauche((3,0))

def Haut(PosAspi): #verifie si l'aspirateur peux tourner en Haut  ou si il se prend le mur
    PosAspi = (PosAspi[0]-1,PosAspi[1])
    print("L'aspirateur est allé en haut. Sur la case" , PosAspi)
    return (PosAspi)
#Haut((0,1))
    
def Bas(PosAspi): #verifie si l'aspirateur peux tourner en Bas  ou si il se prend le mur 
    PosAspi = (PosAspi[0]+1,PosAspi[1])
    print("L'aspirateur est allé en bas. Sur la case" , PosAspi)
    return (PosAspi)   
#Bas((4,1))


##ALLER A LA CASE (0,0)
def PremierCornerWithOutObstacle(PosAspi,NbDeplacement):
    ListePositionAspi =[PosAspi]
    while (PosAspi[0] != 0) :
        PosAspi=Haut(PosAspi)
        NbDeplacement += 1
        ListePositionAspi.append(PosAspi)
    while (PosAspi[1] != 0) :
        PosAspi=Gauche(PosAspi)
        NbDeplacement += 1
        ListePositionAspi.append(PosAspi)
    PosAspi=(0,0)
    return(PosAspi,NbDeplacement,ListePositionAspi)
    #NbAspiration += VerifAspiration(MatriceS,PosAspi,NbAspiration)#Veriiification a (0,0)

def PremierCornerWithObstacle(PosAspi,NbDeplacement,ListePosObstacle,N):
    ListePositionAspi = [PosAspi]
    while (PosAspi != (0,0)) :
        PositionPossiblePremierCorner = [(PosAspi[0],PosAspi[1]-1),(PosAspi[0]-1,PosAspi[1])] #L'aspirateur peut soit aller en haut , soit a gauche.
        for i in PositionPossiblePremierCorner : 
            if ((i[0] < 0) or (i[1] < 0) or (i[0]>=N) or (i[1]>=N) or (i in ListePosObstacle)) : #Si l'une des position est sur un obstacle ou est or grille 
                PositionPossiblePremierCorner.remove(i) # On retire cette position des posibilités
        PosAspi=random.choices(PositionPossiblePremierCorner) #Le choix est aleatoire.
        PosAspi = PosAspi[0] #mais nous on veut pas une liste mais jutse le tuple.
        NbDeplacement +=1
        ListePositionAspi.append(PosAspi)
    return(PosAspi,NbDeplacement,ListePositionAspi)

   
   
#AFFICHER LA GRILLE AVEC ASPIRATEUR 
def Afficher(M,PosAspi,N):
    Sauvegarde = M[PosAspi[0]][PosAspi[1]] #On garde en memoire si la case est propre ou sale
    M[PosAspi[0]][PosAspi[1]] = "\x1b[0;31mx\x1b[0m" #x est en rouge
    plot_grid(M,N) #on affiche la grille avec l'aspirateur
    M[PosAspi[0]][PosAspi[1]] = Sauvegarde #La salle reprend sa proprete d'origine
    return M



##CREATION FINAL
def Aspirateur(UniteT) : #SE PREND PAS LES MURS ET RETIENT SA POSTITION 
    #UniteT = unite de Temps = L'aspirateur peut soit nettoyer soit bouger donc = NbAspiration+NbDeplacement
    
    ##ValeurS
    #Demande de valeur de la taille de la matrice 
    N = input("Indiquer la taille de l'environnement ? : ")#Taille de la Salle
    while (N.isdigit()==False) : #Verification que se soit un nombre 
        N = input("Indiquer la taille de l'environnement , cela doit être une Entier ? : ")
    N = int(N) #Cela doit etre un entier

    #Demande de valeur du pourcentage de Salete 
    PourcentageS = input("Indiquer le pourcentage de la salle qui est sale (nb entre 0 et 100) ? ")
    while search("^(100|[1-9]?[0-9])$",PourcentageS) == None: #verification que ce soit un entier entre 0 et 100
        PourcentageS = input("Indiquer le pourcentage de la salle qui est sale (nb entre 0 et 100) ? ")
    PourcentageS = int(PourcentageS)

    #Demande de valeur du nombre d'obstacle souhaité. 
    while True:
        try:
            NbObstacle = int(input("Combien d'obstacle y'a t il dans votre simulation ? Ce nombre doit etre entre 0 et " + str(((N**2)//9)+1) +" : "))
            if (0 <= NbObstacle <= (((N**2)//9)+1)) :
                break
        except ValueError:
            print("La valeur entrée n'est pas un entier, veuillez entrer un entier.")


    #Valeur de base aux debut de mon code
    NbAspiration=0
    NbDeplacement =0
    NbMemePosition = 0 #Pour savoir le nombre de cases ou l'aspi est aller plus fois .
    
    #Au debut on a une matrice propre.
    MatriceOriginal = MatriceP(N)  
    
    #On rajoute les obstacles dans la salle. 
    Obstacle ="☐"
    ListePosObstacle =[] #liste des positions de tous les obstacles 
    i = 0
    PosObstacleAutour= [] #Liste des positions des cases entourant les obstacles
    while i<NbObstacle : 
        PosObstacle = (random.randint(1,N-1),random.randint(0,N-1)) #Position des obstacles aleatoires.
        PosObstacleAutour = PosObstacleAutour + [(PosObstacle[0],PosObstacle[1]+1),(PosObstacle[0],PosObstacle[1]-1),(PosObstacle[0]+1,PosObstacle[1]),(PosObstacle[0]-1,PosObstacle[1]),(PosObstacle[0]+1,PosObstacle[1]+1),(PosObstacle[0]+1,PosObstacle[1]-1),(PosObstacle[0]-1,PosObstacle[1]+1),(PosObstacle[0]-1,PosObstacle[1]-1)]
        if (PosObstacle not in ListePosObstacle) and (PosObstacle not in PosObstacleAutour): #Si cette case est vide
            MatriceOriginal[PosObstacle[0]][PosObstacle[1]] = Obstacle #on rajoute un obstacle
            ListePosObstacle.append(PosObstacle) #la liste ce met a jour
            i+=1 #Le nb d'obstacle deposé s'accremente
    
    #On veut conserver la matrice propre avec obstacles pour faire des comparaisons. 
    MatriceSale = copy.deepcopy(MatriceOriginal)
    
    #On met de la salete aleatoirement dans notre salle.
    SaleteFonction = Salete(MatriceSale,PourcentageS,N)#On met aleatoirement de la salete en fonction du pourcentage
    MatriceSale = SaleteFonction[0] #Ceci nous renvoie la matrice sale avec obstacle
    NbCSAles = SaleteFonction[1] #Ceci nous renvoie le nombre de cases sales
    print("Voici votre salle sale avec obstacles :)")
    plot_grid(MatriceSale,N)
    
    #Aspirateur
    PosAspi =  (random.randint(0,N-1),random.randint(0,N-1)) #Position de l'aspirateur aleatoire 
    while PosAspi in ListePosObstacle : #il ne faut pas que l'aspirateur atterisse sur un obstacle 
        PosAspi =  (random.randint(0,N-1),random.randint(0,N-1)) #Position de l'aspirateur aleatoire et sur de ne pas etre sur un obstacle
    print("Pour l'instant l'aspirateur ce pose aléatoirement dans la salle. Ca position est" ,PosAspi)
    #On veut afficher l'aspirateur sur la grille
    Afficher(MatriceSale,PosAspi,N)
    
    
    #Si y'a une salete 
    if (MatriceSale != MatriceOriginal): 
        #On initialie la position de l'aspirateur en (0,0)
        Info = PremierCornerWithObstacle(PosAspi,NbDeplacement,ListePosObstacle,N)
        ListePositionAspi = Info[2]
        NbDeplacement += Info[1] #On met a jour le nb de deplacement
        PosAspi = Info[0] #PosAspi = (0,0) apres ca
        print("Pour aller en position (0,0), l'aspirateur a fait" , NbDeplacement , "deplacements.")
        Afficher(MatriceSale,PosAspi,N) # Affiche la matrice avec l'aspirateur en forme de Croix rouge
        #Verification que la case (0,0) est propre
        if VerifAspiration(MatriceSale,PosAspi) == True :
            NbAspiration +=1 
            print("Avec cette case tu as nettoyé",round(NbAspiration*100/NbCSAles,2),"des cases sales.") #Ceci est la mesure de performance. c'est le nb de case nettoyer par rapport aux nb de case sales au debut.

        while (MatriceSale != MatriceOriginal): #Tant que la salle est sale
            if ((NbDeplacement+NbAspiration)<UniteT) : # et si bien sur l'aspirateur est encore viable
                
                #Si pres d'un bord à droite ou il doit descendre. 
                if ((PosAspi[1] == N-1 ) and (PosAspi[0]%2 == 0))  : 
                    print("L'aspirateur sait être pres d'un mur, il va descendre ")
                    PositionPossible = (PosAspi[0]+1,PosAspi[1]) #Possition ou il voudrait aller. 
                    if PositionPossible in ListePosObstacle : #Mais si y'a un obstacle
                        print("L'aspirateur ne peux pas continuer son trajet car il y'a un obstacle, il va faire un petit detour.")
                        PosAspi=Gauche(PosAspi) #Il fait un detour en allant a gauche puis dans tous le scas il va en bas .
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                        NbDeplacement+=1
                    PosAspi = Bas(PosAspi) #Si pas d'obstacle il va direct en bas
                    NbDeplacement+=1
                    if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                    
                #Si pres d'un bord à gauche ou il doit descendre.  
                elif ((PosAspi[1] == 0) and (PosAspi[0]%2 != 0)) :
                    print("L'aspirateur sait être pres d'un mur, il va descendre ")
                    PositionPossible = (PosAspi[0]+1,PosAspi[1]) #Possition ou il voudrait aller.
                    if PositionPossible in ListePosObstacle : #Mais si y'a un obstacle
                        print("L'aspirateur ne peux pas continuer son trajet car il y'a un obstacle, il va faire un petit detour.")
                        PosAspi=Droite(PosAspi) #Il fait un detour en allant a droite puis dans tous les cas apres il va en bas .
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                        NbDeplacement+=1
                    PosAspi = Bas(PosAspi)
                    NbDeplacement+=1
                    if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                
                #Si l'aspi est a une case d'un bord à gauche.  
                elif ((PosAspi[1] == 1) and (PosAspi[0]%2 != 0)) :
                    PositionPossible = (PosAspi[0],PosAspi[1]-1) #Possition ou il voudrait aller.
                    if PositionPossible in ListePosObstacle : #Mais si y'a un obstacle
                        print("L'aspirateur ne peux pas continuer son trajet car il y'a un obstacle, il va faire un petit detour.")
                        PosAspi=Bas(PosAspi) #Il fait un detour en allant en bas puis dans tous les cas apres il va à gauche .
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                        NbDeplacement+=1
                    PosAspi = Gauche(PosAspi)
                    NbDeplacement+=1
                    if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                
                #Si l'aspi est a une case d'un bord à droite.  
                elif ((PosAspi[1] == N-2) and (PosAspi[0]%2 == 0)) :
                    PositionPossible = (PosAspi[0],PosAspi[1]+1) #Possition ou il voudrait aller.
                    if PositionPossible in ListePosObstacle : #Mais si y'a un obstacle
                        print("L'aspirateur ne peux pas continuer son trajet car il y'a un obstacle, il va faire un petit detour.")
                        PosAspi=Bas(PosAspi) #Il fait un detour en allant en bas puis dans tous les cas apres il va à droite .
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                        NbDeplacement+=1
                    PosAspi = Droite(PosAspi)
                    NbDeplacement+=1
                    if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                
                #Si en allant a droite il rencontre un obstacle
                elif PosAspi[0]%2 == 0 : #Si l'aspirateur est sur une colonne pair  l'aspirateur veut tjs aller a droite 
                    PositionPossible = (PosAspi[0],PosAspi[1]+1) #Possition ou il voudrait aller.
                    if PositionPossible in ListePosObstacle : #Mais si y'a un obstacle
                        print("L'aspirateur ne peux pas continuer son trajet car il y'a un obstacle, il va faire un petit detour.")
                        PosAspi=Haut(PosAspi) #Il fait un detour en allant en haut puis deux fois a droite puis bas. 
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                        PosAspi=Droite(PosAspi)
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                        PosAspi=Droite(PosAspi)
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                        PosAspi=Bas(PosAspi)
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                        NbDeplacement+=4
                    else :
                        PosAspi = Droite(PosAspi) #Si pas d'obstacle il va direct à droite
                        NbDeplacement+=1
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                 
                #Si en allant a gauche il rencontre un obstacle
                elif PosAspi[0]%2 != 0 : #Si l'aspirateur est sur une colonne pair  l'aspirateur veut tjs aller a droite 
                    PositionPossible = (PosAspi[0],PosAspi[1]-1) #Possition ou il voudrait aller.
                    if PositionPossible in ListePosObstacle : #Mais si y'a un obstacle
                        print("L'aspirateur ne peux pas continuer son trajet car il y'a un obstacle, il va faire un petit detour.")
                        PosAspi=Haut(PosAspi) #Il fait un detour en allant en haut puis deux fois a gauche puis bas. 
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                        PosAspi=Gauche(PosAspi)
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                        PosAspi=Gauche(PosAspi)
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                        PosAspi=Bas(PosAspi)
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)
                        NbDeplacement+=4
                    else :
                        PosAspi = Gauche(PosAspi) #Si pas d'obstacle il va direct à gauche
                        NbDeplacement+=1
                        if PosAspi in ListePositionAspi : ListePositionAspi.append(PosAspi)

                if PosAspi in ListePositionAspi : NbMemePosition +=1
                
                if VerifAspiration(MatriceSale,PosAspi) == True : #Quand il est sur une case il verifie qu'elle soit propre
                    Afficher(MatriceSale,PosAspi,N) #Quand c'est sale on affiche la grille 
                    NbAspiration +=1 #Si sale on aspire
                    print("Avec cette case tu as nettoyé",round(NbAspiration*100/NbCSAles,2),"des cases sales.") #Ceci est la mesure de performance. c'est le nb de case netoyer par rapport aux nb de case sales au debut   
                else : print("Cette case est propre.") # Si propre on affiche pas car sinon trop de matrice 
            else : # Si l'aspirateur n'est pas viable car plus d'unite de temps
                print("L'aspirateur est mort , désolé le temps est écoulé ")
                break #Pour sortir du while
    
    if (MatriceSale == MatriceOriginal):
        print("La salle est propre. ") #Si de base la salle est propre

    #Quand tout est propre ou que y'a plus d'unite de temps 
    print("L'aspirateur l'a nettoyé en ",(NbDeplacement+NbAspiration)," Unité de Temps avec ",NbAspiration," aspirations et ",NbDeplacement," deplacements. Et il est passé",NbMemePosition,"fois sur des cases identiques.")


Aspirateur(100)
    

