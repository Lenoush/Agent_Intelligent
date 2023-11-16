##AMELIORATION
# QUAND N > 11 DECALGE DANS LA MATRICE (que du visuel)
# Taille de la salle NxM peut etre ? pas une matrice carre
# mon unite de temps est verife seulemet 1 fois par tour alors que 1 tour peut contenir 1 aspiration et 1 deplacement


#La taille de l'environnement est choisie.
#Le pourcentage de saleté est choisie.
#Les positions de la saleté est aleatoire.
#La durée de vie, Unite de temps est imposée.
#Chaque aspiration, deplacement, mauvais deplacement prend 1 unité de temps.
#Dans AgentReflexeEtat() et AgentReflexeSimple() , l'aspirateur ce deplace en mode serpent , il va à la case (0,0) et commence son chemin. 
#Dans AgentReflexeEtat() , l'aspirateur connait son environnement donc ne se prend pas les murs, et indique combien de fois il est repassé sur une case.
#Dans AgentReflexeAvecSimple() , l'aspirateur ne connait pas son environnement donc se prend les murs.



#Demande de valeur
N = input("Indiquer la taille de l'environnement ? : ")#Taille de la Salle
while (N.isdigit()==False) : #Verification que se soit un nombre 
    N = input("Indiquer la taille de l'environnement , cela doit être une Entier ? : ")
N = int(N) #Cela doit etre un entier

PourcentageS = input("Indiquer le pourcentage de la salle qui est sale (nb entre 0 et 100) ? ")
while (PourcentageS.isdigit()==False) : #Verification que se soit un nombre 
    PourcentageS = input("Indiquer le pourcentage de la salle qui est sale (nb entre 0 et 100) ? ")
while (int(PourcentageS) < 0) or (int(PourcentageS) > 100) :
    PourcentageS = input("Indiquer le pourcentage de la salle qui est sale (nb entre 0 et 100) ? ")
PourcentageS = int(PourcentageS) #Cela doit etre un entier




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
def plot_grid(M) :
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
#plot_grid(MatriceP(N))






## CREATION DE LA SALETE
import random
def Salete(N,PourcentageS):
    NbSalete = round((N*N) * (PourcentageS/100)) # Le nombre de case sales  est un entier qui depends du nombre de cases total et du pourcentage de salete souhaite
    Matrice = MatriceP(N) # matrice vide de 0 ("propre")
    i=0 
    while i < NbSalete : #Tant que le nombre de cases sales est inf au nombre souhaité 
        L,C = random.randint(0,N-1),random.randint(0,N-1) #Position aleatoire de la salete 
        if (Matrice[L][C] == '0') :
            Matrice[L][C] = '1' #transfome 0 en 1 , transforme propre en salete 
            i += 1
    #print(len(ListePosSale))
    return (Matrice,NbSalete)
#Salete(N,PourcentageS)




##CREATION DE L'ASPIRATION
def VerifAspiration(M,PosAspi):
    #print(M)
    if (M[PosAspi[0]][PosAspi[1]] == '1') : #Si la case ,sur laquelle l'aspi est, est sale
        (M[PosAspi[0]][PosAspi[1]]) = '0' #on aspire et on rend propre
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
def PremierCorner(PosAspi,NbDeplacement):
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
        
#Afficher la grille avec l'aspirateur
def Afficher(M,PosAspi):
    Sauvegarde = M[PosAspi[0]][PosAspi[1]] #On garde en memoire si la case est propre ou sale
    M[PosAspi[0]][PosAspi[1]] = "\x1b[0;31mx\x1b[0m" #x est en rouge
    plot_grid(M) #on affiche la grille avec l'aspirateur
    M[PosAspi[0]][PosAspi[1]] = Sauvegarde #La salle reprend sa proprete d'origine
    return M



##CREATION FINAL

def AgentReflexeSimple(UniteT) : #SE PREND LES MURS (Amelioration : se predn aussi le smur lors de l'initialisation)
    #UniteT = unite de Temps = L'aspirateur peut soit nettoyer soit bouger donc = NbAspiration+NbDeplacement
    #Valeur de base aux debut de mon code
    SaleteF = Salete(N,PourcentageS) #On met aleatoirement de la salete en fonction du pourcentage 
    MatriceS = SaleteF[0] #Ceci nous renvoie la matrice sale
    NbCSAles = SaleteF[1] #Ceci nous renvoie le nombre de cases sales
    NbAspiration=0
    NbDeplacement =0
    #Salle sale
    print("Voici votre salle sale :)")
    plot_grid(MatriceS)
    #Aspirateur
    PosAspi =  (random.randint(0,N-1),random.randint(0,N-1)) #position de l'aspirateur aleatoire 
    print("Pour l'instant l'aspirateur ce pose aléatoirement dans la salle. Ca position est" ,PosAspi)
    #On veut afficher l'aspirateur sur la grille
    Afficher(MatriceS,PosAspi)
    #Si y'a une salete 
    if (MatriceS != MatriceP(N)): 
        #On initialie la position de l'aspirateur en (0,0)
        Info = PremierCorner(PosAspi,NbDeplacement)
        NbDeplacement += Info[1] #On met a jour le nb de deplacement
        PosAspi = Info[0] #PosAspi = (0,0) apres ca
        print("Pour aller en position (0,0), l'aspirateur a fait" , NbDeplacement , "deplacements.")
        Afficher(MatriceS,PosAspi) # Affiche la matrice avec l'aspirateur en forme de Croix rouge
        #Verification que la case (0,0) est propre
        if VerifAspiration(MatriceS,PosAspi) == True :
            NbAspiration +=1 
            print("Avec cette case tu as nettoyé",round(NbAspiration*100/NbCSAles,2),"des cases sales.") #Ceci est la mesure de performance. c'est le nb de case nettoyer par rapport aux nb de case sales au debut.

        while (MatriceS != MatriceP(N)): #Tant que la salle est sale
            if ((NbDeplacement+NbAspiration)<UniteT) : # et si bien sur l'aspirateur est encore viable
                if ((PosAspi[1] == N-1 ) and (PosAspi[0]%2 == 0)) or ((PosAspi[1] == 0) and (PosAspi[0]%2 != 0))  :
                    print("Aïe, l'aspirateur est rentré dans le mur en allant à gauche . Et si il descendait ")
                    NbDeplacement += 1 #Il se prend le mur mais ca compte comme un deplacement
                    PosAspi = Bas(PosAspi)
                elif PosAspi[0]%2 == 0 : #Si l'aspirateur est sur la derniere colonne :
                    PosAspi= Droite(PosAspi) #Si il est sur une autre colonne il va à droite
                else : PosAspi= Gauche(PosAspi)
                NbDeplacement += 1 #Prend plus 1 car dans tous les cas l'apirateur est soit aller à droite soit en bas. 
                if VerifAspiration(MatriceS,PosAspi) == True : #Quand il est sur une case il verifie qu'elle soit propre
                    Afficher(MatriceS,PosAspi) #Quand c'est sale on affiche la grille 
                    NbAspiration +=1 #Si sale on aspire
                    print("Avec cette case tu as nettoyé",round(NbAspiration*100/NbCSAles,2),"des cases sales.") #Ceci est la mesure de performance. c'est le nb de case netoyer par rapport aux nb de case sales au debut   
                else : print("Cette case est propre.") # Si propre on affiche pas car sinon trop de matrice 
            else : # Si l'aspirateur n'est pas viable car plus d'unite de temps
                print("L'aspirateur est mort , désolé le temps est écoulé ")
                break #Pour sortir du while
    else : print("La salle est propre. ") #Si de base la salle est propre

    #Quand tout est propre ou que y'a plus d'unite de temps 
    print("L'aspirateur l'a nettoyé en ",(NbDeplacement+NbAspiration)," Unité de Temps avec ",NbAspiration," aspirations et ",NbDeplacement," deplacements.")

    


def AgentReflexeAvecEtat(UniteT) : #SE PREND PAS LES MURS ET RETIENT SA POSTITION 
    #UniteT = unite de Temps = L'aspirateur peut soit nettoyer soit bouger donc = NbAspiration+NbDeplacement
    #Valeur de base aux debut de mon code
    SaleteF = Salete(N,PourcentageS) #On met aleatoirement de la salete en fonction du pourcentage 
    MatriceS = SaleteF[0] #Ceci nous renvoie la matrice sale
    NbCSAles = SaleteF[1] #Ceci nous renvoie le nombre de cases sales
    NbAspiration=0
    NbDeplacement =0
    NbMemePosition = 0 #Pour savoir le nombre de cases ou l'aspi est aller plus fois . 
    #Salle sale
    print("Voici votre salle sale :)")
    plot_grid(MatriceS)
    #Aspirateur
    PosAspi =  (random.randint(0,N-1),random.randint(0,N-1)) #position de l'aspirateur aleatoire 
    print("Pour l'instant l'aspirateur ce pose aléatoirement dans la salle. Ca position est" ,PosAspi)
    #On veut afficher l'aspirateur sur la grille
    Afficher(MatriceS,PosAspi)
    #Si y'a une salete 
    if (MatriceS != MatriceP(N)): 
        #On initialie la position de l'aspirateur en (0,0)
        Info = PremierCorner(PosAspi,NbDeplacement)
        ListePositionAspi= Info[2]
        NbDeplacement += Info[1] #On met a jour le nb de deplacement
        PosAspi = Info[0] #PosAspi = (0,0) apres ca
        print("Pour aller en position (0,0), l'aspirateur a fait" , NbDeplacement , "deplacements.")
        Afficher(MatriceS,PosAspi) # Affiche la matrice avec l'aspirateur en forme de Croix rouge
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
                    Afficher(MatriceS,PosAspi) #Quand c'est sale on affiche la grille 
                    NbAspiration +=1 #Si sale on aspire
                    print("Avec cette case tu as nettoyé",round(NbAspiration*100/NbCSAles,2),"des cases sales.") #Ceci est la mesure de performance. c'est le nb de case netoyer par rapport aux nb de case sales au debut   
                else : print("Cette case est propre.") # Si propre on affiche pas car sinon trop de matrice 
            else : # Si l'aspirateur n'est pas viable car plus d'unite de temps
                print("L'aspirateur est mort , désolé le temps est écoulé ")
                break #Pour sortir du while
    else : print("La salle est propre. ") #Si de base la salle est propre

    #Quand tout est propre ou que y'a plus d'unite de temps 
    print("L'aspirateur l'a nettoyé en ",(NbDeplacement+NbAspiration)," Unité de Temps avec ",NbAspiration," aspirations et ",NbDeplacement," deplacements. Et il est passé",NbMemePosition,"fois sur des cases identiques.")


def AgentReflexeSimpleRandom(UniteT) : #SE PREND LES MURS (Amelioration : se predn aussi le smur lors de l'initialisation)
    #UniteT = unite de Temps = L'aspirateur peut soit nettoyer soit bouger donc = NbAspiration+NbDeplacement
    #Valeur de base aux debut de mon code
    SaleteF = Salete(N,PourcentageS) #On met aleatoirement de la salete en fonction du pourcentage 
    MatriceS = SaleteF[0] #Ceci nous renvoie la matrice sale
    NbCSAles = SaleteF[1] #Ceci nous renvoie le nombre de cases sales
    NbAspiration=0
    NbDeplacement =0
    #Salle sale
    print("Voici votre salle sale :)")
    plot_grid(MatriceS)
    #Aspirateur
    PosAspi =  (random.randint(0,N-1),random.randint(0,N-1)) #position de l'aspirateur aleatoire 
    print("Pour l'instant l'aspirateur ce pose aléatoirement dans la salle. Ca position est" ,PosAspi)
    #On veut afficher l'aspirateur sur la grille
    Afficher(MatriceS,PosAspi)
    #on verifie que la case est propre 
    if VerifAspiration(MatriceS,PosAspi) == True : 
                NbAspiration +=1 #Si sale on aspire
                print("Avec cette case tu as nettoyé",round(NbAspiration*100/NbCSAles,2),"des cases sales.") #Ceci est la mesure de performance. c'est le nb de case netoyer par rapport aux nb de case sales au debut   
    while (MatriceS != MatriceP(N)): #Tant que la salle est sale
        if ((NbDeplacement+NbAspiration)<UniteT) : # et si bien sur l'aspirateur est encore viable
            NouveauDeplacement = random.choice(['Droite','Gauche','Bas','Haut'])
            if (NouveauDeplacement == 'Droite' and PosAspi[1] == N-1 ) :
                print("Aïe, l'aspirateur est rentré dans le mur en allant à Droite.")
                NbDeplacement+=1
            elif (NouveauDeplacement == 'Gauche' and PosAspi[1] == 0 ) :
                print("Aïe, l'aspirateur est rentré dans le mur en allant à Gauche.")
                NbDeplacement+=1
            elif (NouveauDeplacement == 'Haut' and PosAspi[0] == 0 ) :
                print("Aïe, l'aspirateur est rentré dans le mur en allant en Haut.")
                NbDeplacement+=1
            elif (NouveauDeplacement == 'Bas' and PosAspi[0] == N-1 ) :
                print("Aïe, l'aspirateur est rentré dans le mur en allant en Bas.")
                NbDeplacement+=1
            else :
                if (NouveauDeplacement == 'Droite') : PosAspi= Droite(PosAspi)
                elif (NouveauDeplacement == 'Gauche') : PosAspi= Gauche(PosAspi)
                elif (NouveauDeplacement == 'Haut') : PosAspi= Haut(PosAspi)
                else : PosAspi= Bas(PosAspi)
                
                NbDeplacement+=1
                if VerifAspiration(MatriceS,PosAspi) == True : #Quand il est sur une case il verifie qu'elle soit propre
                    Afficher(MatriceS,PosAspi) #Quand c'est sale on affiche la grille 
                    NbAspiration +=1 #Si sale on aspire
                    print("Avec cette case tu as nettoyé",round(NbAspiration*100/NbCSAles,2),"des cases sales.") #Ceci est la mesure de performance. c'est le nb de case netoyer par rapport aux nb de case sales au debut   
                else : print("Cette case est propre.") # Si propre on affiche pas car sinon trop de matrice 
        else : # Si l'aspirateur n'est pas viable car plus d'unite de temps
            print("L'aspirateur est mort , désolé le temps est écoulé ")
            
            break #Pour sortir du while

    #Quand tout est propre ou que y'a plus d'unite de temps 
    print("L'aspirateur a nettoyé la salle en ",(NbDeplacement+NbAspiration)," Unité de Temps avec ",NbAspiration," aspirations et ",NbDeplacement," deplacements.")

  
    
    

def Aspirateur(UniteT) : #SE PREND PAS LES MURS ET RETIENT SA POSTITION 
    #UniteT = unite de Temps = L'aspirateur peut soit nettoyer soit bouger donc = NbAspiration+NbDeplacement
    #Valeur de base aux debut de mon code
    SaleteF = Salete(N,PourcentageS) #On met aleatoirement de la salete en fonction du pourcentage 
    MatriceS = SaleteF[0] #Ceci nous renvoie la matrice sale
    NbCSAles = SaleteF[1] #Ceci nous renvoie le nombre de cases sales
    NbAspiration=0
    NbDeplacement =0
    #Salle sale
    print("Voici votre salle sale :)")
    plot_grid(MatriceS)
    #Aspirateur
    PosAspi =  (random.randint(0,N-1),random.randint(0,N-1)) #position de l'aspirateur aleatoire 
    print("Pour l'instant l'aspirateur ce pose aléatoirement dans la salle. Ca position est" ,PosAspi)
    #On veut afficher l'aspirateur sur la grille
    Afficher(MatriceS,PosAspi)
    #Si y'a une salete 
    if (MatriceS != MatriceP(N)): 
        #On initialie la position de l'aspirateur en (0,0)
        Info = PremierCorner(PosAspi,NbDeplacement)
        ListePositionAspi= Info[2]
        NbDeplacement += Info[1] #On met a jour le nb de deplacement
        PosAspi = Info[0] #PosAspi = (0,0) apres ca
        print("Pour aller en position (0,0), l'aspirateur a fait" , NbDeplacement , "deplacements.")
        Afficher(MatriceS,PosAspi) # Affiche la matrice avec l'aspirateur en forme de Croix rouge
        #Verification que la case (0,0) est propre
        if VerifAspiration(MatriceS,PosAspi) == True :
            NbAspiration +=1 
            print("Avec cette case tu as nettoyé",round(NbAspiration*100/NbCSAles,2),"des cases sales.") #Ceci est la mesure de performance. c'est le nb de case nettoyer par rapport aux nb de case sales au debut.

        while (MatriceS != MatriceP(N)): #Tant que la salle est sale
            if ((NbDeplacement+NbAspiration)<UniteT) : # et si bien sur l'aspirateur est encore viable
                if ((PosAspi[1] == N-1 ) and (PosAspi[0]%2 == 0)) or ((PosAspi[1] == 0) and (PosAspi[0]%2 != 0))  :
                    print("Aïe, l'aspirateur est rentré dans le mur en allant à gauche . Et si il descendait ")
                    NbDeplacement += 1 #Il se prend le mur mais ca compte comme un deplacement
                    PosAspi = Bas(PosAspi)
                elif PosAspi[0]%2 == 0 : #Si l'aspirateur est sur la derniere colonne :
                    PosAspi= Droite(PosAspi) #Si il est sur une autre colonne il va à droite
                else : PosAspi= Gauche(PosAspi)
                NbDeplacement += 1 #Prend plus 1 car dans tous les cas l'apirateur est soit aller à droite soit en bas. 
                if VerifAspiration(MatriceS,PosAspi) == True : #Quand il est sur une case il verifie qu'elle soit propre
                    Afficher(MatriceS,PosAspi) #Quand c'est sale on affiche la grille 
                    NbAspiration +=1 #Si sale on aspire
                    print("Avec cette case tu as nettoyé",round(NbAspiration*100/NbCSAles,2),"des cases sales.") #Ceci est la mesure de performance. c'est le nb de case netoyer par rapport aux nb de case sales au debut   
                else : print("Cette case est propre.") # Si propre on affiche pas car sinon trop de matrice 
            else : # Si l'aspirateur n'est pas viable car plus d'unite de temps
                print("L'aspirateur est mort , désolé le temps est écoulé ")
                break #Pour sortir du while
    else : print("La salle est propre. ") #Si de base la salle est propre

    #Quand tout est propre ou que y'a plus d'unite de temps 
    print("L'aspirateur l'a nettoyé en ",(NbDeplacement+NbAspiration)," Unité de Temps avec ",NbAspiration," aspirations et ",NbDeplacement," deplacements.")



#for i in range (5) : AgentReflexeSimple(1000)
#AgentReflexeSimple(1000)
#AgentReflexeAvecEtat(100)
#AgentReflexeSimpleRandom(1000)
#Aspirateur(100)
    







