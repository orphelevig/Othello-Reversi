/**
 * Simule le jeu de société Reversi / Othello, en choisissant si l'on joue seul contre l'IA ou en 1 contre 1.
*/

class Reversi{
	
	char[][] tab = {
		{'|','|','|','|','|','|','|','|'},
		{'|','O',' ','X',' ',' ','X','|'},
		{'|','X','X','O','O','O','O','|'},
		{'|','X','O','O','O','O',' ','|'},
		{'|',' ','O','X','O','O','X','|'},
		{'|',' ','O','X','O',' ',' ','|'},
		{'|','X','O','X','O','X',' ','|'},
		{'|','|','|','|','|','|','|','|'}
	};
	char[][] tab2 = {
		{'|','|','|','|','|','|','|','|'},
		{'|',' ',' ',' ',' ',' ',' ','|'},
		{'|',' ',' ',' ',' ',' ',' ','|'},
		{'|',' ',' ','O','X',' ',' ','|'},
		{'|',' ',' ','X','O',' ',' ','|'},
		{'|',' ',' ',' ',' ',' ',' ','|'},
		{'|',' ',' ',' ',' ',' ',' ','|'},
		{'|','|','|','|','|','|','|','|'}
	};
	char[][] tab3 = {
		{'X','X','O','O','O','X','X','O'},
		{'O','X','O','O','X','O','O','O'},
		{'X','X','O','O','O','X','X','X'},
		{'O','X','O','O','X','O','O','O'},
		{'X','X','O','O','O','X','X','X'},
		{'O','X','O','O','X','O','O','O'},
		{'X','X','O','O','O','X','X','O'},
		{'O','X','O','O','X','O','O','O'},
	};
	
	void principal(){
		int compteurTour = 0;
		int modeDeJeu;  // 1v1 ou contre un bot IA
		testCoupDispo();
		System.out.println();
		char[][] plateau = creationPlateau();
		afficherPlateau(plateau);
		do{
			modeDeJeu = SimpleInput.getInt("Souhaitez vous jouer seul (répondre 1) ou jouer en 1 contre 1 (répondre 2)? : ");
		} while (modeDeJeu != 1 && modeDeJeu != 2);
		if (modeDeJeu == 1){
			
		}else{
			joueurCourant(plateau, compteurTour);
		}
	}	
	
	/**
	 * retourne l'élément aux coordonnées entrées en paramètres
	 * @param coordonnees de l'élément
	 * @author : M.CISSOKO-KONATE
	 */
	void retourner(char[][]tab, int coordonnees){
		int x = coordonnees / 100;
		int y = convertireColonne(coordonnees);
		char z = 'O';
		if(tab[x][y] == 'O'){z='X';}
		
		tab[x][y] = z ;
		
		System.out.println(z);
	}
	
	/**
	 * donne le num de la colonne de la coordonée
	 * @param coord coordonée du coup 
	 * @return la colonne
	 */
	int convertireColonne(int coord){
		return (coord > 1000) ? coord%100:coord%10;
	}





    /**
     * demande au joueur quelle coup jouer et dit si c'est un coup jouable ou pas et joue le coup .
     * @param tab le plateau de jeux
     * @param tour le nombre de tour dans la partie
     */	
    void joueurCourant(char[][] tab, int tour){
		int[] listTab;
		int x;
		char cara;
		boolean pasPossible = true;

		if(tour % 2 == 1){
			cara = 'X';
		}else{
			cara = 'O';
		}


		do {
			pasPossible = true;
			boolean virgule = true;
			System.out.print("Au Joueur "+tour%2+" ('"+cara+"') de jouer. Merci de mettre des coordonées entre 11 (cote supérieur gauche)");
			System.out.println(" et "+(tab.length-2)*11+" (coté inférieur droit)");
			System.out.print("les coup jouables sont : ");
			for(int i =0;i<tab.length;i++){
				for(int j =0;j<tab.length;j++){
					int coord=i*100+j;
					int[] ijTab = coupDispo(tab,coord,tour);
					//System.out.print(coord);
					//System.out.print(ijTab.length+"+"+tab[coord/10][coord%10]);
					if((ijTab.length > 0)&& (tab[i][j] == ' ')){
						pasPossible = false;
						if(virgule){
							if(coord<999){
								System.out.print("0"+coord);
							}else{
								System.out.print(+coord);
							}
							virgule = false;
						}else{
							if(coord<999){
								System.out.print(", 0"+coord);
							}else{
								System.out.print(", "+coord);
							}						
						}
					}
				}
			}
			if(pasPossible){
				System.out.println("Vous n'avez pas de coup possible, vous passez votre tour");
			}
			System.out.println();
			x = SimpleInput.getInt("Quelle coup voulez vous jouer ?\t");
			listTab=coupDispo(tab,x,tour);
			//System.out.println(listTab.length+"+"+tab[x/10][x%10]);

		} while (
			! (x/100 >= 0 && x/100 < tab.length &&
			   convertireColonne(x) >= 0 && convertireColonne(x) < tab[0].length) //coordonée valide
			|| listTab.length == 0 || tab[x/100][convertireColonne(x)] != ' '
			|| pasPossible
		);		
		if(!pasPossible){
			tab[x/100][convertireColonne(x)] = cara;
			for(int i=0; i<listTab.length;i++){
				retourner(tab, listTab[i]);
			}
		}
	}
    
    
    /**
     * Donne dans un liste les coord des pion retourne en fonction du pion qui veint d'etre jouer
     * @param tab le plateau de jeux
     * @param coord les coordéonnee qui viennent d'être jouer
     * @param tour le nombre de tour dans la partie
     * @return resTab qui est un tableau avec tout les pion qui doivent etre returner (renvoie un liste vide si il y en a aucun
     */	
    int[] coupDispo(char[][] tab, int coord, int tour){
		int[][] t = new int[8][];
		t[0] = coupDispoHV(tab, coord, 1 , 0 ,tour);
		t[1] = coupDispoHV(tab, coord, 0 , 1 ,tour);
		t[2] = coupDispoHV(tab, coord,-1 , 0 ,tour);
		t[3] = coupDispoHV(tab, coord, 0 ,-1 ,tour);
		t[4] = coupDispoHV(tab, coord,-1 ,-1 ,tour);
		t[5] = coupDispoHV(tab, coord,-1 , 1 ,tour);
		t[6] = coupDispoHV(tab, coord, 1 ,-1 ,tour);
		t[7] = coupDispoHV(tab, coord, 1 , 1 ,tour);
		int sum = 0;
		for(int i = 0; i<t.length; i++){ //compte le nombre de pions a retourne pour pouvoir fair un tableau avec la bonnne longueur
			for(int j = 0; j < t[i].length; j++){
				if(t[i][j] !=0){sum++;}
			}
		}
		int[] resTab = new int[sum];
		int z=0;
		for(int i =0; i<t.length; i++){
			for(int j =0; j<t[i].length;j++){
				if(t[i][j] !=0){
					resTab[z] = t[i][j];
					z++;
				}
			}
		}	
		return resTab;	
	}
	
		
    /**
     * Donne dans un liste les coord des pion retourne en fonction du pion qui veint d'etre jouer DANS UN DIRECTION PRECISE donne par a et b 
     * @param tab le plateau de jeux
     * @param coord les coordéonnee qui viennent d'être jouer
     * @param a =0 si on veut verifier horizontalement (-1 à gauche 1 a droite)
     * @param b =0 si on veut verifier verticalement (-1 en haut 1 en bas)
     * @param tour le nombre de tour dans la partie
     * @return resTab qui est un tableau remplie de 0 ou les coordonne des pion qui se retourne grâce au coup jouer
     */	
	int[] coupDispoHV(char[][] tab, int coord, int a, int b, int tour) {
		int[] resTab = new int[tab.length*tab.length]; 
		int ligne = coord / 100;
		int col = convertireColonne(coord);
		char adv;
		char cara;
		
		if(tour % 2 == 1){
			cara = 'X';
			adv = 'O';
		}else{
			cara = 'O';
			adv = 'X';
		}

		int index = 0;
		int i = 1;
		boolean advTrouve = false;
		boolean fin = false;

		while(!fin && ligne+i*a >= 0 &&ligne+i* a < tab.length && /*si elle sort du ligne ou col sorte du tableau*/
			   col+i*b >= 0 && col+i*b < tab.length){

			char c = tab[ligne+i*a][col+i*b]; /*caractere de la coordonner qu'on scanne*/

			if(c == adv){
				advTrouve = true;
			} else{
				if(c == cara && advTrouve){/*si trouve la cara du jouer et que qui a trouve un adversaire alors il fuat forcement le changer*/
					int j = 1;
					while(j < i){
						resTab[index] = (ligne+j*a)*100+(col+j*b);/*rajjoute les caractere au tableau*/
						index++;
						j++;
					}
				}
				fin = true; /*si il a trouve le cara du jouer sans trouver un adv = aucun pion a retourne*/
			}
			i++;
		}

		return resTab;

	}
	
    void displayTab(int[] t) {
        int i = 0;
        System.out.print("{");
        while (i < t.length) {
            System.out.print(t[i]);
            if (i < t.length - 1) {
                System.out.print(", ");
            }
            i++;
        }
        System.out.print("}");
    }
    /**
     * Tester coupDispo
     */
	void testCoupDispo () {
		System.out.println ();
		System.out.println ("*** testCoupDispo(char[][] tab, int coord, int tour)");
		System.out.println("Voici le plateau sur lequel les tests seront effectués : ");
		afficherPlateau(tab);
		System.out.println();
		int[] t1 = {44, 45, 33, 23, 32, 34, 25, 52, 54};
		int[] t2 = {};
		int[] t3 = {23,35};
		testCasCoupDispo (tab,43,27,t1);
		testCasCoupDispo (tab,56,28,t2);
		testCasCoupDispo (tab,24,41,t3);
	}

	/**
	* teste un appel de coupDispo
	* @param tab plateau de jeu
	* @param coord les coordonner du pion jouer
	* @param tour le nombre de tour (utile pour savoir qui joue)
	* @param result le resultat attendue
	*/
	void testCasCoupDispo (char[][] tab, int coord, int tour, int[] result) {
		// Affichage
		System.out.print ("coupDispo (tab, "+ coord +", "+tour);
		System.out.print(") \t= ");
		displayTab(result); 
		System.out.print("\t : ");
		// Appel
		int[] resExec = coupDispo(tab,coord,tour);
		boolean semblable = true;
		int i = 0;
		if(result.length != resExec.length){
			semblable = false;
		}

		while(true && i<result.length){
			if(result[i] != resExec[i]){
				semblable = false;
			}
			i++;
		}
		// Verification
		if (semblable){
			System.out.println ("OK");
		} else {
			System.err.println ("ERREUR");
		}
	}
	
	
	/**
	 * Simule un bot qui joue le coup le plus nul ( retourne le moins de coup
	 * @param tab plateau
	 * @param le nombre de tour
	 * @author LE GUENNEC Arthur
	 */
	void botMin(char tab[][],int tour){
		char cara;
		if(tour % 2 == 1){
			cara = 'X';
		}else{
			cara = 'O';
		}
		int min=99;
		int coordMin = 00;
		final int LG = tab.length;
		int[][] tabCoup = new int[LG][LG];
		for(int i =0;i<LG;i++){
			for(int j=0;j<LG;j++){
				int [] coup = coupDispo(tab, (i*100+j),tour);
				int coupMin = coup.length;
				tabCoup[i][j] = coupMin;
				if(coupMin<min && coupMin >0){
					min = coupMin;
					coordMin = i*100+j;
				}	
			}
		}
		if(!(min == 99)){
			tab[coordMin/100][convertireColonne(coordMin)] = cara;
			int[] listTab = coupDispo(tab, coordMin,tour);
			for(int i=0; i<listTab.length;i++){
				retourner(tab, listTab[i]);
			}
		}else{
			
			System.out.println("Le joueur "+(tour%2)+" ("+cara+") ne peux pas jouer");
		}
	}

	/**
	 * Simule un bot qui joue le coup qui retourne le moin de pion
	 * @param tab plateau
	 * @param le nombre de tour
	 * @autor LE GUENNEC Arthur
	 */
	void botRNG(char tab[][],int tour){
		char cara;
		if(tour % 2 == 1){
			cara = 'X';
		}else{
			cara = 'O';
		}
		int cumul = 0;
		int cumul2 = 0;

		final int LG = tab.length;
		for(int i =0;i<LG;i++){
			for(int j=0;j<LG;j++){
				int [] coup = coupDispo(tab, (i*100+j),tour);
				if(coup.length > 0){
					cumul++;
				}
			}
		}
		if(cumul >0){;
			int[] listCoup= new int[cumul];
			for(int i =0;i<LG;i++){
				for(int j=0;j<LG;j++){
					int [] coup = coupDispo(tab, (i*100+j),tour);
					if(coup.length > 0){
						listCoup[cumul2] = i*100+j;
						cumul2++;
					}
				}
			}
			int rng = (int) Math.random() *cumul;
			int coord = listCoup[rng];
			tab[coord/100][convertireColonne(coord)] = cara;
			int[] listTab = coupDispo(tab, coord,tour);
			for(int i=0; i<listTab.length;i++){
					retourner(tab, listTab[i]);
			}
		}else{System.out.println("Le joueur "+tour%2+" ("+cara+") ne peux pas jouer");
		}
	}
	/**
	 * Simule un bot qui joue le coup qui retourn le plus de pion
	 * @param tab plateau
	 * @param le nombre de tour
	 * @autor LE GUENNEC Arthur
	 */
	void botMax(char tab[][],int tour){
		char cara;
		if(tour % 2 == 1){
			cara = 'X';
		}else{
			cara = 'O';
		}
		int max=0;
		int coordMax = 00;
		final int LG = tab.length;
		int[][] tabCoup = new int[LG][LG];
		for(int i =0;i<LG;i++){
			for(int j=0;j<LG;j++){
				int [] coup = coupDispo(tab, (i*100+j),tour);
				int coupMax = coup.length;
				tabCoup[i][j] = coupMax;
				if(coupMax>max && coupMax >0){
					max = coupMax;
					coordMax = i*100+j;
				}	
			}
		}
		if(!(max == 0)){
			tab[coordMax/100][convertireColonne(coordMax)] = cara;
			int[] listTab = coupDispo(tab, coordMax,tour);
			for(int i=0; i<listTab.length;i++){
				retourner(tab, listTab[i]);
			}
		}else{
			
			System.out.println("Le joueur "+(tour%2)+" ("+cara+") ne peux pas jouer");
		}
	}
	
	/**
	 * Créee un plateau de reversi de la taille voulue par le joueur, à certaines conditions.
	 * @return un tableau 2D contenant un plateau de reversi
     * @author O. Le Vigoureux
	*/
	char[][] creationPlateau(){
		int tailleGrille; 
		
		do{ // Demande une taille de plateau tant que la taille de la grille n'est pas comprise entre 4 et 16 et qu'elle n'est pas pair.
			tailleGrille = SimpleInput.getInt ("Donnez la taille de la grille souhaitée, pair tel que 4 <= taille <= 16 : ");
		}while (tailleGrille % 2 != 0 || tailleGrille < 4 || tailleGrille > 16);
		
		tailleGrille = tailleGrille + 2;
		char[][] plateau = new char[tailleGrille + 1][tailleGrille];
		int milieu = tailleGrille / 2;
		for (int i = 0; i < plateau[0].length; i++){
			for (int j = 0; j < plateau[0].length; j++){
				plateau[i][j] = ' ';
			}
		}
		plateau[milieu-1][milieu-1] = 'x';
		plateau[milieu][milieu] = 'x';
		
		plateau[milieu-1][milieu] = 'o';
		plateau[milieu][milieu-1] = 'o';
		
		for (int j = 0; j < plateau[0].length; j++){
			int i = 0;
			plateau[i][j] = '|';
		}
		for (int j = 0; j < plateau[0].length; j++){
			int i = tailleGrille - 1;
			plateau[i][j] = '|';
		}
		for (int i = 0; i < plateau[0].length; i++){
			int j = 0;
			plateau[i][j] = '|';
		}
		for (int i = 0; i < plateau[0].length; i++){
			int j = tailleGrille - 1;
			plateau[i][j] = '|';
		}
		return plateau;
	}
	
	/**
	 * affiche un tableau 2D de caractères mis en paramètre
	 * @param tab tableau de tableau contenant des caractères
     * @author O. Le Vigoureux
	*/
	void afficherPlateau(char[][] tab){
		System.out.print("  ");
		for (int i = 0; i < tab.length - 1; i++){
			if (i>0 && i < tab.length - 2){
				System.out.print(i + " ");
			}else{
				System.out.print("  ");
			}
		}System.out.println("  ");
		for (int i = 0; i < tab.length - 1; i++){
			if (i>0 && i < tab.length - 2){
				System.out.print(i);
			}else{
				System.out.print(" ");
			}displayTabChar(tab[i]);
			System.out.println("  ");
		}
	}
	
	/**
	 * affiche un tableau de caractères
	 * @param t tableau de type char
     * @author O. Le Vigoureux
	*/
	void displayTabChar(char[] t){
		int i = 0;
		System.out.print(" ");
		while(i<t.length-1){
			System.out.print(t[i] + "|");
			i=i+1;
		}if(t.length !=0){
			System.out.print(t[i]+" ");
		}else{
			System.out.print(" ");
		}
	}
	/**
	* Affiche le score des deux joueurs 
	* @param tab (plateau du jeu)
	* @author : M.CISSOKO-KONATE
	*/
	
	void displayScore(char[][]tab){
		
		int[] res = new int[2];
		int compteurX = 0;
		int compteurO = 0;
		
		for (int i =0; i< tab.length; i++){
			for (int j=0; j< tab[i].length; j++){
				 
				if ( tab[i][j] == 'O'){
					compteurO ++;
				} else if (tab[i][j] == 'X'){
					compteurX ++;
				}
			}
		}
				
		res[0] = compteurO;
		res[1] = compteurX;	
		
		
		System.out.println ("{ Score Joueur 'O' : \t " + res[0] +"}");
		System.out.println ("{ Score Joueur 'X' : \t " + res[1]+ "}");
	}
}
	
	
