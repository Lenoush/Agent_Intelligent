N = int(input("Indiquer la taille de l'environnement ? (Pas 1) : "))#Taille de la Salle
while (N == 1): N = input("Indiquer la taille de l'environnement ? PAS 1  : ") # LA salle ne peut pas faire 1 case
PourcentageS = int(input("Indiquer le pourcentage de la salle qui est sale ? "))

COLONNES = [" "] + [str(i) for i in range (N)]
LIGNES = [str(i) for i in range (N)]

##AMELIORATION
#QUAND N > 11 DECALGE DANS LA MATRICE
# pourcentage entre 0 et 100
# quand n type != int
# Calculer les iterations
# Calculer le nombre d'aspiration (= nombre de salete )
# Calculer le nombre de deplacement
# Deplacer l'aspi au plus proche corner
# Taille de la salle
# if deja (0,0) faire un truc
# if N est pair ou impaire 



##CREATION DE L'ENVIRONNEMENT : 

# Creation Matrice Vide ( avec seulement des 0 )
def MatriceP(N) :
    matrice = []
    for i in range(N) :
        l =  []
        for j in range(N) :
            l.append("0")
        matrice.append(l)
    return(matrice)
#print(MatriceP(N))

# Transforme une Matrice lambda en grille a Jouer 
def plot_grid(M) :
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
def Salete(N,PourcentageS):
    ListePosSale =[] #Liste des position de la salete 
    NbSalete = (N*N) * (PourcentageS/100) # Le nombre de case sales depends du nombre de cases total et du pourcentage de salete souhaite
    Matrice = MatriceP(N) # matrice vide de 0 ("propre")
    i=0
    while i < NbSalete : #Tant que le nombre de cases sales est inf au nombre souhaité 
        L,C = random.randint(0,N-1),random.randint(0,N-1) #Position aleatoire de la salete 
        if (Matrice[L][C] == '0') :
            Matrice[L][C] = '1'
            i += 1
            ListePosSale.append([L,C])
    print(len(ListePosSale))
#     print(ListePosSale)
    #plot_grid(Matrice)
    return Matrice 
#Salete(N,PourcentageS)




##CREATION DE L'ASPIRATION

def VerifAspiration(M,PosAspi):
    #print(M)
    if (M[PosAspi[0]][PosAspi[1]] == '1') :
        (M[PosAspi[0]][PosAspi[1]]) = '0'
        print("Bravo tu as nettoyé la case " + str(PosAspi))# si y'a de la salete , l'aspi l'aspire
        Reponse = True
    else : Reponse = False
    #print(M)
    return (Reponse)
#VerifAspiration(Salete(N,PourcentageS),(3,2))



##CREATION DEPLACEMENT
    
def Droite(PosAspi): #verifie si l'aspirateur peux tourner a droite ou si il se prend le mur 
    if PosAspi[1]+1 < N :
        PosAspi = (PosAspi[0],PosAspi[1]+1)
    print("L'aspirateur est alle en position ",PosAspi)
    return (PosAspi)  
#Droite((3,4))

def Gauche(PosAspi): #verifie si l'aspirateur peux tourner a gauche ou si il se prend le mur 
    if PosAspi[1]-1 >= 0 :
        PosAspi = (PosAspi[0],PosAspi[1]-1)
    print("L'aspirateur est alle en position ",PosAspi)
    return (PosAspi)    
#Gauche((3,0))

def Haut(PosAspi): #verifie si l'aspirateur peux tourner en Haut  ou si il se prend le mur 
    if PosAspi[0]-1 >= 0 : #Attention si on va en haut le premier chiffre diminue (pertubant?)
        PosAspi = (PosAspi[0]-1,PosAspi[1])
    print("L'aspirateur est alle en position ",PosAspi)
    return (PosAspi)    
#Haut((0,1))
    
def Bas(PosAspi): #verifie si l'aspirateur peux tourner en Bas  ou si il se prend le mur 
    if PosAspi[0]+1 < N : #Attention si on va en bas le premier chiffre augmente
        PosAspi = (PosAspi[0]+1,PosAspi[1])
    print("L'aspirateur est alle en position ",PosAspi)
    return (PosAspi)   
#Bas((4,1))


##ALLER A LA CASE (0,0)
def PremierCorner(PosAspi):
    while (PosAspi[0] != 0) or (PosAspi[1] != 0) :
        PosAspi=Haut(PosAspi)
        PosAspi=Gauche(PosAspi)
    PosAspi=(0,0)
    return(PosAspi)
    #NbAspiration += VerifAspiration(MatriceS,PosAspi,NbAspiration)#Veriiification a (0,0)
        
#Afficher la grille avec l'aspirateur
def Afficher(M,PosAspi):
    Sauvegarde = M[PosAspi[0]][PosAspi[1]] #On garde en memoire si la case est propre ou sale
    M[PosAspi[0]][PosAspi[1]] = "\x1b[0;31mx\x1b[0m" #x est en rouge
    plot_grid(M) #on affiche la grille avec l'aspirateur
    M[PosAspi[0]][PosAspi[1]] = Sauvegarde #La salle reprend sa proprete d'origine
    return M

##CREATION FINAL

def Aspirateur() :
    #Valeur de base aux debut de mon code
    MatriceS = Salete(N,PourcentageS)
    NbAspiration=0
    NbDeplacement =0
    I = NbAspiration+NbDeplacement
    
    #Salle sale
    print("Voici votre salle sale :)")
    plot_grid(MatriceS)
    
    #Aspirateur
    PosAspi =  (random.randint(0,N-1),random.randint(0,N-1))
    print("Pour l'instant l'aspirateur ce pose aléatoirement dans la salle. Ca position est" ,PosAspi)
    #On veut afficher l'aspirateur sur la grille
    Afficher(MatriceS,PosAspi)
    
    #Si y'a une salete 
    if (MatriceS != MatriceP(N)): #Faut mettre While
        #On initialie la position de l'aspirateur en (0,0)
        NbDeplacement = int(PosAspi[0])+ int(PosAspi[1])#NbDeplacement pour aller en (0,0)
        PosAspi = PremierCorner(PosAspi) #PosAspi = (0,0) apres ca
        print("Pour aller en position (0,0), l'aspirateur a fait" , NbDeplacement , "deplacements.")
        Afficher(MatriceS,PosAspi)
        VerifAspiration(MatriceS,PosAspi)
        if VerifAspiration(MatriceS,PosAspi) == True :
            NbAspiration +=1
        
        #On comence le deplacement Serpent
        for i in range (N) : # Pour N nombre de lignes
            for j in range (N): #Pour N nombre de colonnes
                PosAspi=Droite(PosAspi)#Aspirateur va à Droite (il fait toute la ligne)
                if VerifAspiration(MatriceS,PosAspi) == True :
                    Afficher(MatriceS,PosAspi)
                    NbAspiration +=1
            PosAspi = Bas(PosAspi)
            if VerifAspiration(MatriceS,PosAspi) == True :
                    Afficher(MatriceS,PosAspi)
                    NbAspiration +=1
            for j in range (N):
                PosAspi=Gauche(PosAspi)
                if VerifAspiration(MatriceS,PosAspi) == True :
                    Afficher(MatriceS,PosAspi)
                    NbAspiration +=1
            PosAspi = Bas(PosAspi)
            if VerifAspiration(MatriceS,PosAspi) == True :
                    Afficher(MatriceS,PosAspi)
                    NbAspiration +=1
    
    #Quand tout est propre

    print("Bravo , la salle est Propre. L'aspirateur la nettoyé en ",I," iterations avec ",NbAspiration," aspirations et ",NbDeplacement," deplacemennts.")
    
#     
#     #VerifAspiration(MatriceS,PosAspi)
#     #print(NbAsspiration)#PROBLEME SUR LE NOMDRE D'ASSPIRATION EFFECTUE
#     
#         
        
            ##IL FAUT REDEFINIR MATRICEs POUR QUE LE WHILE S'ARRETE 
    
            
            
   
      
Aspirateur()
    







