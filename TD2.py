##AMELIORATION
# Amelioration du visuel de la matrice quand n > 10
# Taille de la salle NxM => pas une matrice carre
# Mon unite de temps est verife seulemet 1 fois par tour alors que 1 tour peut contenir 1 aspiration et 1 deplacement
# Essayer de faire des fonctions pour enlever les doublons dans la fonction avec obstacles .
# Dans la fonction avec obstacles, verifer le nombre des cases identique sur lequel l'aspi est passe. 

##SAVOIR
#La taille de l'environnement est choisie.
#Le pourcentage de saleté est choisie.
#Les positions de la saleté est aleatoire.
#Le nombre d'obastacle est limité mais et egalement choisie. 
#La durée de vie, Unite de temps est imposée.

#PosAspi prend la valeur de la position de l'aspirateur a l'instant t : c'est le capteur de position.
#Le capteur de position marche seulement sur la position de l'aspirateur. il capte egalemnt si ilrets de la saleté dasn la salle mais ne sait pas où elle est. 

#Chaque aspiration, deplacement, mauvais deplacement prend 1 unité de temps.
#Dans AgentReflexeEtat() et AgentReflexeSimple() , l'aspirateur ce deplace en mode serpent , il va à la case (0,0) et commence son chemin.

#Dans AgentReflexeSimple() , l'aspirateur ne connait pas son environnement donc se prend les murs. Si sales il aspire sinon il se deplace. 
#Dans AgentReflexeEtat() , l'aspirateur connait son environnement donc ne se prend pas les murs, et indique combien de fois il est repassé sur une case.


import copy
from re import *


'''CREATION DE L'ENVIRONNEMENT '''

# Creation Matrice Vide (avec seulement des 0)
def MatriceP(N) :
    matrice = []
    for i in range(N) :
        l =  []
        for j in range(N) :
            l.append("0")
        matrice.append(l)
    return(matrice)
#print(MatriceP(10))

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
#plot_grid(MatriceP(10))

# CREATION DE LA SALETE
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

# M = MatriceP(10)
# P = Salete(M,80,10)
# plot_grid(P,10)



## CREATION DE L'ASPIRATION
def VerifAspiration(M,PosAspi):
    #print(M)
    if (M[PosAspi[0]][PosAspi[1]] == "1") : #Si la case ,sur laquelle l'aspi est, est sale
        Proba = int(random.choices([0, 1], weights=[0.2, 0.8])[0]) # 20% que l'aspiration echoue.
#         print(type(Proba))
#         print(Proba)
        if Proba == 0 :
            print("Il semblerai que l'aspiration est echoué sur la case " + str(PosAspi))
            Reponse = 'Moyen'
        else : 
            (M[PosAspi[0]][PosAspi[1]]) = "0" #on aspire et on rend propre
            print("Bravo tu as nettoyé la case " + str(PosAspi))
            Reponse = True #pour plus tard savoir si oui ou non la case etait sale
    else : Reponse = False
    #print(M)
    return (Reponse)
#VerifAspiration(Salete(MatriceP(10),10,80),(3,2))


## CREATION DEPLACEMENT
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


## ALLER A LA CASE (0,0)
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

   
   
## AFFICHER LA GRILLE AVEC ASPIRATEUR 
def Afficher(M,PosAspi,N):
    Sauvegarde = M[PosAspi[0]][PosAspi[1]] #On garde en memoire si la case est propre ou sale
    M[PosAspi[0]][PosAspi[1]] = "\x1b[0;31mx\x1b[0m" #x est en rouge
    plot_grid(M,N) #on affiche la grille avec l'aspirateur
    M[PosAspi[0]][PosAspi[1]] = Sauvegarde #La salle reprend sa proprete d'origine
    return M

def AgentReflexeAvecEtat(UniteT,N,PourcentageS) : #SE PREND PAS LES MURS ET RETIENT SA POSTITION 
    #UniteT = unite de Temps = L'aspirateur peut soit nettoyer soit bouger donc = NbAspiration+NbDeplacement
    #Valeur de base aux debut de mon code
    Matrice = MatriceP(N) # matrice vide de 0 ("propre")
    SaleteF = Salete(Matrice,PourcentageS,N) #On met aleatoirement de la salete en fonction du pourcentage 
    MatriceS = SaleteF[0] #Ceci nous renvoie la matrice sale
    NbCSAles = SaleteF[1] #Ceci nous renvoie le nombre de cases sales
    NbAspiration=0
    NbDeplacement =0
    NbMemePosition = 0 #Pour savoir le nombre de cases ou l'aspi est aller plus fois . 
    #Salle sale
    print("Voici votre salle sale :)")
    plot_grid(MatriceS,N)
    #Aspirateur
    PosAspi =  (random.randint(0,N-1),random.randint(0,N-1)) #position de l'aspirateur aleatoire 
    print("Pour l'instant l'aspirateur ce pose aléatoirement dans la salle. Ca position est" ,PosAspi)
    #On veut afficher l'aspirateur sur la grille
    Afficher(MatriceS,PosAspi,N)
    #Si y'a une salete 
    if (MatriceS != MatriceP(N)): 
        #On initialie la position de l'aspirateur en (0,0)
        Info = PremierCornerWithOutObstacle(PosAspi,NbDeplacement)
        ListePositionAspi= Info[2]
        NbDeplacement += Info[1] #On met a jour le nb de deplacement
        PosAspi = Info[0] #PosAspi = (0,0) apres ca
        print("Pour aller en position (0,0), l'aspirateur a fait" , NbDeplacement , "deplacements.")
        Afficher(MatriceS,PosAspi,N) # Affiche la matrice avec l'aspirateur en forme de Croix rouge
        #Verification que la case (0,0) est propre
        if VerifAspiration(MatriceS,PosAspi) == True :
            NbAspiration +=1 
            print("Avec cette case tu as nettoyé",round(NbAspiration*100/NbCSAles,2),"des cases sales.") #Ceci est la mesure de performance. c'est le nb de case nettoyer par rapport aux nb de case sales au debut.

        while (MatriceS != MatriceP(N)): #Tant que la salle est sale
            if ((NbDeplacement+NbAspiration)<UniteT) : # et si bien sur l'aspirateur est encore viable
                if ((PosAspi[1] == N-1 ) and (PosAspi[0]%2 == 0)) or ((PosAspi[1] == 0) and (PosAspi[0]%2 != 0))  :
                    print("L'aspirateur sait être pres d'un mur, il va descendre ")
                    PosAspi = Bas(PosAspi)
                elif PosAspi[0]%2 == 0 : #Si l'aspirateur est sur la derniere colonne :
                    PosAspi= Droite(PosAspi) #Si il est sur une autre colonne il va à droite
                else : PosAspi= Gauche(PosAspi)
                NbDeplacement += 1 #Prend plus 1 car dans tous les cas l'apirateur est soit aller à droite soit en bas.
                for i in ListePositionAspi :
                    if PosAspi == i : NbMemePosition +=1
                if VerifAspiration(MatriceS,PosAspi) == True : #Quand il est sur une case il verifie qu'elle soit propre
                    Afficher(MatriceS,PosAspi,N) #Quand c'est sale on affiche la grille 
                    NbAspiration +=1 #Si sale on aspire
                    print("Avec cette case tu as nettoyé",round(NbAspiration*100/NbCSAles,2),"des cases sales.") #Ceci est la mesure de performance. c'est le nb de case netoyer par rapport aux nb de case sales au debut   
                else : print("Cette case est propre.") # Si propre on affiche pas car sinon trop de matrice 
            else : # Si l'aspirateur n'est pas viable car plus d'unite de temps
                print("L'aspirateur est mort , désolé le temps est écoulé ")
                break #Pour sortir du while
    
    if (MatriceS == MatriceP(N)):
        print("La salle est propre. ") #Si de base la salle est propre

    #Quand tout est propre ou que y'a plus d'unite de temps 
    print("L'aspirateur l'a nettoyé en ",(NbDeplacement+NbAspiration)," Unité de Temps avec ",NbAspiration," aspirations et ",NbDeplacement," deplacements. Et il est passé",NbMemePosition,"fois sur des cases identiques.")


def choix() :

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
    
    AgentReflexeAvecEtat(100,N,PourcentageS)
    

choix()

