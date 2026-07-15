import random
def jeuDuo():
    """
     * Jeu Reversi en mode Duo
     * Contre un adversaire réel
    """
    print("--M O D E  D U O--\n")
    
    plateau = creationPlateau()
    
    tour = 1
    maxTours = ((len(plateau) - 3) * (len(plateau) - 3))
    tabScore = [0,0]
    
    while not (len(coupJouable(plateau,tour)) == 0 and len(coupJouable(plateau,(tour + 1))) == 0) or (displayScore(plateau)[0] +  displayScore(plateau)[1] < maxTours ):
        print(f"• T O U R {tour} : ")
        afficherPlateau(plateau)
        tabScore = displayScore(plateau)
        
        print(f"[ Score Joueur 'O' : \t {tabScore[0]} ]")
        print(f"[ Score Joueur 'X' : \t {tabScore[1]} ]")
        
        joueurCourant(plateau, tour)
        
        print(f"\n\t• Plateau apres le tour {tour} :")
        afficherPlateau(plateau)
        displayScore(plateau)
        
        tour += 1
        
    print("\n\n--F I N  D E  L A  P A R T I E--\n")
    
    tabScore = displayScore(plateau)
    print(f"[ Score Joueur 'O' : \t {tabScore[0]} ]")
    print(f"[ Score Joueur 'X' : \t {tabScore[1]} ]\n")
    
    if tabScore[0] > tabScore[1]:
        print("--V A I N Q U E U R  'O' !-- ")
    else :
        print("--V A I N Q U E U R  'X' !-- ")
def jeuSolo():
    """
     * Jeu Reversi en mode solo 
     * Contre l'IA avec un niveau de difficulté variable
    """
    caraBot = ' '
    caraJoueur = ' '
    botChoisi = 0
    print("--M O D E  S O L O-- \n")
    
    caraJoueur = str(input("\t• Quel caractère souhaitez vous jouer ? 'O' pour commencer, 'X' sinon : \n"))
    while caraJoueur not in ["O","X"]:
        caraJoueur = str(input("\t• Quel caractère souhaitez vous jouer ? 'O' pour commencer, 'X' sinon : \n"))
    
    if caraJoueur == "O":
        caraBot = "X"
    else :
        caraBot = "O"
        
    plateau = creationPlateau()
    
    botChoisi = int(input("\t• Choisissez la difficulté de jeu : '1' [facile], '2' [moyen], '3' [difficile]. "))
    while botChoisi not in [1,2,3]:
        botChoisi = int(input("\t• Choisissez la difficulté de jeu : '1' [facile], '2' [moyen], '3' [difficile]. "))
    
    tour = 1
    maxTours = ((len(plateau) - 3) * (len(plateau) - 3))
    tabScore = [0,0]
    
    while not (len(coupJouable(plateau,tour)) == 0 and len(coupJouable(plateau,(tour + 1))) == 0) or (displayScore(plateau)[0] +  displayScore(plateau)[1] < maxTours ):
        print(f"• Tour {tour} : ")
        afficherPlateau(plateau)
        
        tabScore = displayScore(plateau)
        print(f"[ Score Joueur 'O' : \t {tabScore[0]} ]")
        print(f"[ Score Joueur 'X' : \t {tabScore[1]} ]")
        
        if (tour % 2 == 1 and caraJoueur == "O") or (tour % 2 == 0 and caraJoueur == "X"):
            joueurCourant(plateau, tour)
        
        else :
            if botChoisi == 1 :
                botMin(plateau,caraBot,tour)
            elif(botChoisi == 2):
                botRNG(plateau,caraBot,tour)
            else :
                botMax(plateau,caraBot,tour)
        tour += 1
        
    print("")
    
    tabScore = displayScore(plateau) 
    
    if (tabScore[0] > tabScore[1] and caraJoueur =='O') or (tabScore[0] < tabScore[1] and caraJoueur =='X'):
        print("--V O U S  Ê T E S  L  E  V A I N Q U E U R--\n")
    else :
        print("--D E F A I T E  F A C E  A  L A  M A C H I N E--\n")

    afficherPlateau(plateau)
    
    print(f"[ Score Joueur 'O' : \t {tabScore[0]} ]")
    print(f"[ Score Joueur 'X' : \t {tabScore[1]} ]\n")
def modeJeu():
    """
     * Choix du mode de jeu
     * Contre une IA ou en duo
     * @return le mode de jeu selectionné
    """
    print("--S A I S I E  M O D E  D E  J E U--")
    
    modeDeJeu = int(input("	• SEUL (entrez 1) ou DUO (entrez 2) : \t"))
    while modeDeJeu not in [1,2]:
        modeDeJeu = int(input("	• SEUL (entrez 1) ou DUO (entrez 2) : \t"))
    
    return modeDeJeu
def convertirColonne(coord):
    """
     * Donne la colonne de la coordonée
     * @param coord coordonées du coup 
     * @return la colonne
    """
    colonne = coord % 10
    if coord > 1000 :
        colonne = coord % 100
    return coord - ((coord // 100) * 100)
def retourner(tab, coordonnees):
    """
     * Retourne l'élément aux coordonnées entrées en paramètres
     * @param coordonnées de l'élément
    """
    x = coordonnees // 100
    y = convertirColonne(coordonnees)
    z = "O"
    
    if tab[x][y] == "O":
        z = "X"
        
    tab[x][y] = z
def coupJouable(tab, tour):
    """
     * Détermine si un coup est jouable ou non
     * @param tab : tableau à double-entrée (plateau du jeu)
     * @param tour : tour de jeu
     * @return liste des coups jouables
    """
    
    x, sum = 0, 0
    cara = None
    
    for i in range(1, len(tab)-1):
        for j in range(1, len(tab)-1):
            
            coord = i * 100 + j
            ijTab = coupDispo(tab, coord, tour)
            
            if len(ijTab) > 0 and tab[i][j] == ' ' :
                sum += 1
                
    resTab = [0] * sum
    sum = 0
    
    for i in range(1, len(tab)-1):
        for j in range (1, len(tab)-1):
            
            coord = i * 100 + j
            ijTab = coupDispo(tab, coord, tour)
            if len(ijTab) > 0 and tab[i][j] == ' ' :
                resTab[sum] = coord
                sum += 1
                
    return resTab
def joueurCourant(tab, tour):
    listeTab = []
    plateau = []
    x = 0
    cara = None
    
    if tour % 2 == 1:
        cara = 'O'
    else :
        cara = 'X'
        
    joueurNum = None
    if tour % 2 == 1:
        joueurNum = 1
    else :
        joueurNum = 2
    
    possible = False
    
    while not possible :
        
        print(f"\n\t• [ Tour du joueur {joueurNum} ('{cara}')]")
        print("\n Merci de mettre des coordonées entre 0101 (cote supérieur gauche)", end="")
        print(f" et {len(tab) - 2}")
        
        print(f"{len(tab) - 2} (coté inférieur droit)\n")
        print("\t• [Coups jouables] : ", end="")
        
        plateau = coupJouable(tab, tour)
        i = 0
        print("", end="")
        
        while i < len(plateau) :
            if plateau[i] < 999:
                print("0", end="") 
            
            print(plateau[i], end="") 
            
            if i < len(plateau) - 1 : 
                print(", ", end="")
            i+=1
            
        print("") 
        
        
        if len(plateau) == 0 :
            print(" • [ Aucun coup possible, passez votre tour]")
            possible = True 
        else :
            print("")
            try:
                x = int(input("\t• [Quel coup voulez-vous jouer ?]\t"))
            except ValueError:
                x = -1 
            
            listeTab = coupDispo(tab, x, tour)
            
            if x in plateau:
                possible = True
            else:
                print("/!\\ Coup non valide ou mal écrit, réessayez /!\\")

    if len(plateau) > 0 :
        tab[x // 100][convertirColonne(x)] = cara
        for i in range(len(listeTab)):
            retourner(tab, listeTab[i])
def coupDispo(tab, coord, tour):
    """
     * Donne dans une liste des coordonnées des pions pouvant être retournés en fonction du pion qui vient d'être joué
     * @param tab : le plateau de jeux
     * @param coord : les coordonnées qui viennent d'être jouées
     * @param tour : le nombre de tours dans la partie
     * @return resTab : tableau avec tous les pions devant être retourné (renvoie un liste vide si il y en a aucun)
    """
    t = [0] * 8
    t[0] = coupDispoHV(tab, coord, 1 , 0 ,tour)
    t[1] = coupDispoHV(tab, coord, 0 , 1 ,tour)
    t[2] = coupDispoHV(tab, coord,-1 , 0 ,tour)
    t[3] = coupDispoHV(tab, coord, 0 ,-1 ,tour)
    t[4] = coupDispoHV(tab, coord,-1 ,-1 ,tour)
    t[5] = coupDispoHV(tab, coord,-1 , 1 ,tour)
    t[6] = coupDispoHV(tab, coord, 1 ,-1 ,tour)
    t[7] = coupDispoHV(tab, coord, 1 , 1 ,tour)
    
    sum = 0
    for i in range(len(t)) :
        for j in range(len(t)):
            if t[i][j] != 0 :
                sum+=1
            j+=1
    resTab = [0] * sum
    z = 0
    
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] != 0 :
                    resTab[z] = t[i][j]
                    z += 1
    return resTab
def coupDispoHV(tab, coord, a, b, tour):
    """
     * Donne dans une liste les coordonnées des pions retournés en fonction du pion qui vient d'être joué DANS UNe DIRECTION PRECISE donnée par a et b 
     * @param tab : le plateau de jeu
     * @param coord :  les coordonnées qui viennent d'être jouées
     * @param a = 0 : si on veut vérifier horizontalement (-1 à gauche 1 à droite)
     * @param b = 0 : si on veut vérifier verticalement (-1 en haut 1 en bas)
     * @param tour : le nombre de tours dans la partie
     * @return resTab : qui est un tableau rempli de 0 ou les coordonnées des pions qui se sont retournés grâce au coup joué
    """
    resTab = [0] * (len(tab)*len(tab))
    ligne = coord // 100
    col = convertirColonne(coord)
    
    c = ' '
    if tour % 2 == 1 :
        cara = 'O'
        adv = 'X'
    else :
        cara = 'X'
        adv = 'O'
    
    index = 0
    i = 1
    advTrouve = False
    fin = False
    
    while not fin :
        nL = ligne + i * a
        nC = col + i * b
        
        if nL < 0 or nL >= len(tab) or nC < 0 or nC >= len(tab[0]): #en dehors
            fin = True
        else :
            c = tab[nL][nC] # caractère de la coordonnée qu'on scanne
        
        if not fin:
            if c == adv :
                advTrouve = True
            else :
                if c == cara and advTrouve : #si trouve la cara du jouer et que qui a trouve un adversaire alors il faut forcement le changer
                    j = 1
                    
                    while j < i :
                        resTab[index] = (ligne+j*a)*100+(col+j*b) # rajoute les caractere au tableau
                        index += 1
                        j+=1
                fin = True 
        i+=1
    return resTab
def testCoupDispo():
    """
    * Teste coupDispo
    """
    tabTest = [['|','|','|','|','|','|','|','|'],
               ['|','O',' ','X',' ',' ','X','|'],
               ['|','X','X','O','O','O','O','|'],
               ['|','X','O','O','O','O',' ','|'],
               ['|',' ','O','X','O','O','X','|'],
               ['|',' ','O','X','O',' ',' ','|'],
               ['|','X','O','X','O','X',' ','|'],
               ['|','|','|','|','|','|','|','|']]
    
    print()
    print("************testCoupDispo(char[][] tab, int coord, int tour)")
    print("tabTest :")
    afficherPlateau(tabTest)
    t1 = [402, 502]
    t2 = []
    t3 = [203,305]
    testCasCoupDispo (tabTest,401,28,t1)
    testCasCoupDispo (tabTest,506,28,t2)
    testCasCoupDispo (tabTest,204,40,t3)
    print()
    print("************")
    print()
def testCasCoupDispo(tab, coord, tour, result):
    """
    * Teste un appel de coupDispo()
	* @param tab : plateau de jeu
	* @param coord : les coordonner du pion jouer
	* @param tour : le nombre de tour (utile pour savoir qui joue)
	* @param result : le resultat attendue
    """
    print(f"coupDispo (tabTest, {coord}, {tour}) =   ", end = "")
    displayTab(result)
    print("\t : ")
    
    resExec = coupDispo(tab, coord, tour)
    semblable = True
    i = 0
    
    if len(result) != len(resExec) :
        semblable = False
    
    while semblable and i < len(result) :
        if result[i] != resExec[i] :
            semblable = False
        i+=1
    
    # Vérif
    if semblable :
        print("OK")
    else :
        print("ERREUR")
        
    print()
def botMin(tab, cara, tour):
    """
     * Simule un bot qui joue le coup qui retourne le moins de pion
     * @param tab plateau
     * @param cara le caractere du joueur
     * @param tour le nombre de tour
    """
    joueurNum = None
    if tour % 2 == 1:
        joueurNum = 1
    else :
        joueurNum = 2

    min = 99
    coordMin = 00
    LG = len(tab)
    tabCoup = [[0]*LG for _ in range(LG)] 
    
    for i in range(1, LG - 1):
        for j in range(1, LG - 1):
            coup = coupDispo(tab, (i*100+j),tour)
            coupMin = len(coup)
            tabCoup[i][j] = coupMin
            if tab[i][j] == ' ' and (coupMin < min and coupMin > 0):
                min = coupMin
                coordMin = i*100+j
                
    if not min == 99:
        tab[coordMin // 100][convertirColonne(coordMin)] = cara
        listTab = coupDispo(tab, coordMin,tour)
        
        for i in range(len(listTab)): 
            retourner(tab, listTab[i])

    else :
        print(f"Le joueur {joueurNum} ({cara}) ne peux pas jouer")
def botRNG(tab, cara, tour):
    """
     * Simule un bot qui joue un coup aléatoire
     * @param tab plateau
     * @param cara le caractere du joueur
     * @param tour le nombre de tour
    """
    joueurNum = None
    if tour % 2 == 1:
        joueurNum = 1
    else :
        joueurNum = 2
    
    cumul = 0
    LG = len(tab)
    
    for i in range(1, LG-1):
        for j in range(1, LG-1):
            coup = coupDispo(tab, (i*100+j), tour)
            if len(coup) > 0 and tab[i][j] == ' ':
                cumul+=1
    
    if cumul > 0:
        listeCoup = [0]*cumul
        idx = 0 
        for i in range(1, LG-1):
            for j in range(1, LG-1):
                coup = coupDispo(tab, (i*100+j), tour)
                if len(coup) > 0 and tab[i][j] == ' ':
                    listeCoup[idx] = i*100+j
                    idx += 1
        
        rng = random.randint(0, cumul-1) 
        coord = listeCoup[rng]
        
        tab[coord // 100][convertirColonne(coord)] = cara
        listeTab = coupDispo(tab, coord, tour)
        
        for i in range(len(listeTab)):
            retourner(tab, listeTab[i])
        
    else :
        print(f"Le joueur {joueurNum} ({cara}) ne peux pas jouer")
def botMax(tab, cara, tour):
    """
     * Simule un bot qui joue le coup qui retourne le plus de pion
     * @param tab plateau
     * @param cara le caractere du joueur
     * @param tour le nombre de tour
    """
    joueurNum = None
    if tour % 2 == 1:
        joueurNum = 1
    else:
        joueurNum = 2
    max = 0
    coordMax = 00
    LG = len(tab)
    tabCoup = [[0]*LG for _ in range(LG)]
    
    for i in range(1, LG-1):
        for j in range(1, LG-1):
            coup = coupDispo(tab, (i*100+j),tour)
            coupMax = len(coup)
            tabCoup[i][j] = coupMax
            if coupMax > max and coupMax > 0 and tab[i][j] == ' ':
                max = coupMax
                coordMax = i*100+j

    if not max == 0:
        tab[coordMax // 100][convertirColonne(coordMax)] = cara
        listTab = coupDispo(tab, coordMax,tour)
        
        for i in range(len(listTab)):
            retourner(tab, listTab[i])

    else:
        print(f"Le joueur {joueurNum} ({cara}) ne peux pas jouer")
def creationPlateau():
    """
    * Créer un plateau de Reversi de la taille voulue par le joueur, à certaines conditions
    * @return un tableau 2D contenant un plateau de Reversi
    """
    tailleGrille = int(input("	• Taille souhaitée de la grille (entre 4 et 16 inclus) : \t "))
    print()
    while tailleGrille % 2 != 0 or tailleGrille < 4 or tailleGrille > 16:
        tailleGrille = int(input("	• Taille souhaitée de la grille (entre 4 et 16 inclus) : \t "))
        print()
    taille = tailleGrille + 2
    plateau = [[' ' for t in range(taille)] for t in range(taille)]
    
    for i in range(taille):
        for j in range(taille):
            plateau[i][j] = ' '
    
    milieu = taille // 2
    
    plateau[milieu - 1][milieu - 1] = 'X'
    plateau[milieu][milieu] = 'X'
    plateau[milieu - 1][milieu] = 'O'
    plateau[milieu][milieu - 1] = 'O'
    
    return plateau
def afficherPlateau(tab):
    """
     * Affiche le plateau
     * @param tab : plateau du jeu
    """
    print()
    print()
    print("     ", end="") 
    
    for i in range(1, len(tab)-1):
        if i < 10:
            print(f"0{i}  ", end="") 
        else :
            print(f"{i}  ", end="")
        
    print()
    
    for i in range(1, len(tab)-1):
        if i < 10:
            print(f"0{i} |", end="") 
        else :
            print(f"{i} |", end="")
            
        displayTabChar(tab[i])
        
        print("|") 
            
    print()
    print()
def displayTab(tab):
    """
     * Affiche le contenu d'un tableau d'entier
     * @param tab le tableau
    """
    i = 0
    print("{", end="") 
    while i < len(tab):
        print(tab[i], end="")
        if i < len(tab)-1 :
            print(", ", end="")
        i+=1
    print("}") 
def displayTabChar(tab):
    """
    * Affiche une ligne du plateau
    * @param tab : une ligne du plateau
    """
    for i in range(1, len(tab)-1):
        print(f" {tab[i]} ", end="")
        
        if i < len(tab) - 2:
            print("|", end="")
def displayScore(tab):
    """
    * Affiche le score des deux joueurs 
	* @param tab : (plateau du jeu)
	* @return liste des deux scores
    """
    res = [0,0]
    compteurX = 0
    compteurO = 0
    
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i][j] == 'O':
                compteurO += 1
            elif tab[i][j] == 'X':
                compteurX += 1
    
    res[0] = compteurO
    res[1] = compteurX
    
    return res
def principal():
    print("//=========================================================\\"+"\\")
    print("||     B I E N V E N U E   D A N S   R E V E R S I !       ||");
    print("\\"+"\\=========================================================//");
    
    testCoupDispo()
    
    if modeJeu() == 1:
        jeuSolo()
    else :
        jeuDuo()
def main():
    principal()
main()
