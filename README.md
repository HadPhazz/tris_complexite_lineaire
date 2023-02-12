# NSI Terminale : MSD Radix Sort 

**Prérequis de l'	activité :**
-  Avoir vu les tris par comparaison
- Avoir vu la méthode "Diviser Pour Régner". 
- Connaitre les classes de complexité suivantes : $O(1), O(n), O(n \log n), O(n2)$ 
- Savoir illustrer la complexité temporelle d'un tri par un graphique 

**Apports de l'activité :**
- Présentation des tris par distribution
- Présentation du *MSD Radix Sort*
- Mise en place de ce tri sur des listes de mots (implémentation en Python)
- Etude de complexité de ce tri (analyse et interprétation de courbes)

## Présentation du tri par base / Radix sort

Le  **tri par base**  (Radix Sort en anglais) est un algorithme de tri par distribution, utilisant le tri par dénombrement comme routine d’exécution, sur des listes de  **nombres entiers**  (naturels et relatifs), de  **nombres décimaux**  finis, mais aussi sur des listes de  **chaines de caractères**  (mots, emails, …).

Cet algorithme trie les données avec des clés définies selon l’ordre lexicographique, en les regroupant par des digits individuels (chiffres, caractères, symboles) qui partagent la même position significative et la même valeur.  
Le  **Radix**  (la base) est le nombre de digits utilisé pour représenter un nombre dans un système de numérotation positionnel. (2 pour le binaire, 8 pour l’octal, 10 pour le décimal, …).

Quelque soit le type des éléments de la liste passée en paramètre de cet algorithme, une clé, sous la forme d’un entier, sera associée à chaque digit.  Les éléments ne seront donc pas triés d’une manière comparative, mais en fonction des digits significatifs qui les composent.

Le tri par base se décompose en deux variantes :

-   Le **LSD Radix Sort**  (bit de poids faible/plus petit élément significatif) : Généralement utilisé pour les données numériques (entiers, flottants) en commençant par le chiffre des unités, puis celui des dizaines, … de la droite vers la gauche.

-  Le  **MSD Radix Sort**  (bit de poids fort/plus grand élément significatif) : Généralement utilisé pour les données lexicographiques (mots, phrases, …) en triant les éléments dans le sens de lecture (de gauche à droite), du premier caractère rencontré jusqu’au dernier.

Les deux versions peuvent traiter des données numériques et lexicographiques, cependant, la version MSD prends en charge des mots de longueur différente, à l'inverse de la version LSD.

Dans la version du tri par base que nous allons analyser au cours de cette activité, nous nous intéresserons à la version **MSD** ce de dernier sur des chaines de caractères. Le *MSD Radix Sort* opère de la sorte : 

1.  Prendre le  **caractère le plus significatif**  de chaque chaine de caractère de la liste comme clé (la première lettre du mot dans notre cas)
2.  **Trier par comptage**  les mots en les ordonnant selon cette  **clé** dans des structures de données temporaires (processus de distribution)
3. Assembler les mots triés en une seule liste (concaténation selon l'ordre alphabétique)
4.  Répéter avec les  **caractères moins significatifs**  (la deuxième lettre, puis la troisième, ...).

Pour toute liste de nombres en base  _n_, cet algorithme utilisera au maximum  _n_  structures de données temporaires, définies en fonction des chiffres qui composent les nombres de la liste. Dans le cas de chaines de caractères, et en particulier de mots de la langue Française, il y'aura, au plus, vingt-six structures de données temporaires (cela correspond au nombre de lettres de notre alphabet).


## Activité

### Questions de compréhension

**1.** En faisant appel aux notions apprises en classe de première et en classe de terminale, citez au moins quatre algorithmes de tri, expliquez brièvement leur fonctionnement et indiquez ceux qui utilisent la méthode "Diviser pour régner".

**2.** En utilisant vos connaissances et la brève présentation de l'algorithme du *tri par base*, expliquez le fonctionnement de ce dernier, dans sa version *LSD*, sur la liste de nombre suivante : [7, 19, 0, 1, 74, 36].
Indiquez de plus le nombre de passes de l'algorithme sur cette liste. Peut-on le savoir, avant même de commencer le tri ? Si oui, comment ?

**3.** Expliquez maintenant le fonctionnement de l'algorithme du *tri par base*, dans sa version *MSD*, sur la liste de mots suivante :  [RUE, BAR, BUS, HUB, ARC]. Indiquez également le nombre de passes à réaliser.

**4.** Ecrivez un pseudo-algorithme du *tri par base*, dans sa version *MSD*, tel qu'il agirais sur une liste finie de mots de tailles égales.

### Etude de cas : Le dictionnaire

Vous interprétez le rôle d'un lexicographe (un rédacteur de dictionnaire de langue) qui, après validation de leur définition et de leur légitimité à intégrer la langue Française, reçoit la liste des nouveaux mots à ajouter dans le dictionnaire pour la nouvelle année. 

Cependant, la liste de mots que vous avez reçu n'est pas triée (les mots ne sont pas classés dans l'ordre alphabétique), vous devez le faire par l’intermédiaire d’un algorithme informatique, afin de les intégrer au dictionnaire par la suite.

La sélection de mots est la suivante, elle se présente sous la forme d’une liste d’éléments :
liste_mots = [VISIO, CRYPTO, ECOANXIETE, AQUAPONIE, WOKE, NFT, DISTANCIEL, IEL]

**1.** Ecrivez une fonction qui renvoi le/les plus long mot/s de la liste, en l'occurrence "ECOANXIETE" et "DISTANCIEL".

> La longueur de ce mot sert à déterminer le nombre maximum de passes qu'effectuera l'algorithme sur la liste de mots, afin de trier alphabétiquement ces derniers. 

**2.** Ecrivez une fonction qui crée un dictionnaire, dont les clés seront les lettres de l'alphabet Français, et les valeurs, des listes. 
Exemple pour la première ligne de ce dictionnaire, appliqué à notre liste :  mots = {"A" : [AQUAPONIE], ...}

**3.** Citez la méthode qui renvoi le code Unicode d'un caractère donné en paramètre. En déduire l'intervalle des valeurs pour les lettres allant du A au Z (en majuscule). 

**4.** Avec l'aide de vos collègues, vous avez appris à appliquer l'algorithme de *tri par base* dans sa version *MSD*, et souhaitez le mettre en œuvre afin de trier la liste de mots définie préalablement.
Complétez cet algorithme réalisé en Python : 

    def tri_radix_MSD(liste, i=0):
    '''
    :param l: (list) une liste de mots
    :param i: (int) la position du premier caractère à regarder, 0 par défaut
    :return: (list) la liste initiale, avec les mots triés dans l'ordre alphabétique
    '''
		
	    if ... : #Cas de la liste vide ou avec un seul élément
	        return ...
	        
	    res = []
	    tmp_struct = []
	    
	    for x in range(...):
	        tmp_struct.append([])
	        
	    for word in l: 
	        if ... >= len(word): 
	            res.append(word)
	        else:
	            tmp_struct[ord(word[i]) - ... ].append(word)
	            
	    tmp_struct = [tri_radix_MSD(... , ...) for j in tmp_struct]
	    
	    for e_l in tmp_struct:
	        for e in e_l:
	            res.append(e)
	            
	    return res

*NB :* N'hésitez pas à demander de l'aide à votre professeur.

### Etude de complexité

A partir des fonctions implémentant les modules *matplotlib* et *timeit* déjà réalisées lors d'une activité précédente, **réalisez un graphique illustrant la complexité temporelle du tri par base sur des chaines de caractères**.  Vous implémenterez le tri par base, dans sa version MSD, dans le module "*tris .py*", et réaliserez les fonctions relatives à la mesure du temps et à la création du graphique dans le module "*main .py*". Veillez à adapter le code de l'activité passée. Pour ce qui est de la liste de mots, vous utiliserez la fonction *listeMotsAleatoires()*, disponible dans le module "*listes .py*".

**Rappel**

L'utilisation de **timeit** se fait de la sorte : 

    for i in range(début, fin):
            timeList.append(timeit(setup='from module import fonction',
               stmt='monTri(maListe(i))',
               number=n))
où *début* et *fin* sont les bornes de l'intervalle sur lesquelles la mesure du temps doit être effectuée,
*n* correspond au nombre de fois où l'instruction présente dans le champ *stmt* sera réalisée.

*Exemple*

    def timeitFunction(tri, liste, n):
    timeList = []
    for i in range(1, n+1):
	    timeList.append(timeit(setup='from tris import {}; from listes import {}'.format(tri, liste),
        stmt='{}({}({}))'.format(tri, liste, i),
        number=n))
    return timeList        

L'utilisation de **matplotlib** pour des graphique se fait de la sorte :

    def graphiqueMatPlotLib(tri, liste, n):
	    x = np.linspace(0, n, n)
	    fig, ax = plt.subplots()
	    y = timeitFunction(tri, liste, n)
	    ax.plot(x, y, label=tri) 
	    plt.show()

Vous utiliserez de plus les méthodes suivantes pour agrémenter votre graphique :

 - title()
 - xlabel() & ylabel()
 - legend()
 - grid()

Votre graphique doit **prouver que l'algorithme à une complexité temporelle en $O(n)$** dans le meilleur des cas, et en $O(n*m)$ dans le pire des cas ($m$ étant la longueur de la plus longue chaine de caractère).

Vous pouvez, en adaptant votre code, comparer le temps d'exécution ce cet algorithme de tri à la méthode *sort()* de Python, en réalisant une courbe avec le tri *tri_sort_python()* (qui adapte la méthode native *sorted()*).

> La complexité spatiale de ce tri est en $O(n + m*b)$, où $m$ est la longueur de la plus longue chaine de caractère, et $b$ la taille du radix (10 dans le cas des entiers de 0 à 9, 256 dans le cas des caractères, 26 dans le cas des lettres majuscules de l'alphabet, ...).
> Cette version du tri par base utilise la récursivité, elle est optimisée pour un fonctionnement sur de larges collections de données, elle devient plus lente que la version *LSD* dans le cas contraire. 
