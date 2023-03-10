#!/usr/bin/python3
# -*- coding: utf-8 -*-

###################################################
#       FONCTION DE COMPARAISON PAR DEFAUT        #
###################################################
def compare(x, y):
    """
    :param x, y: (quelconque) deux données de mêmes types
    :return: (int) 
      - -1 si x < y
      - 0 si x == y
      - 1 si x > y
    :CU: x et y doivent être d'un type pour lequel les opérateurs de comparaison <, <=, == 
         peuvent s'appliquer
    :Exemples:

    >>> compare(1, 3)
    -1
    >>> compare("aab", "bb")
    -1
    >>> compare(3, 1)
    1
    >>> compare("mange", "bb")
    1
    >>> compare(3, 3)
    0
    >>> compare("bb", "bb")
    0
    """
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0


###################################################
#   PREDICAT EST_TRIE                             #
###################################################

def est_trie(l, comp=compare):
    """
    :param l: (type sequentiel) une séquence 
    :param comp: (fonction) [optionnel] une fonction de comparaison. 
                             Valeur par défaut : compare
    :return: (bool) 
      - True si l est triée selon l'ordre défini par comp
      - False sinon
    :CU: les éléments de l doivent être comparables selon comp
    :Exemples:

    >>> est_trie([1, 2, 3, 4])
    True
    >>> est_trie([1, 2, 4, 3])
    False
    >>> est_trie([])
    True
    """
    return all(comp(l[i], l[i+1]) <= 0 for i in range(len(l) - 1))

###################################################
#   TRI SELECTION                                 #
###################################################

def echanger(l, i, j):
    """
    :param l: (list) une liste 
    :param i, j: (int) deux indices
    :return: (NoneType) aucune
    :Effet de bord: échange les éléments d'indice i et j de l.
    :CU: 0 <= i,j < long(l)
    :Exemples:
    
    >>> l1 =  [3, 1, 4, 9, 5, 1, 2]
    >>> l2 = l1.copy()
    >>> echanger(l2, 3, 5)
    >>> (l1[3], l1[5]) == (l2[5], l2[3])
    True
    """
    l[i], l[j] = l[j], l[i]
    

def select_min(l, a, b, comp=compare):
    """
    :param l: (list) une liste
    :param a, b: (int) deux indices
    :param comp: (fonction) [optionnel] une fonction de comparaison
                   Valeur par défaut compare
    :return: (int) l'indice du minimum dans la tranche l[a:b]
    :CU: 0 <= a < b <= long(l),
         éléments de l comparables avec comp
    :Exemples:
    
    >>> select_min([1, 2, 3, 4, 5, 6, 7, 0], 0, 8)
    7
    >>> select_min([1, 2, 3, 4, 5, 6, 7, 0], 1, 7)
    1
    """
    ind_min = a
    # l'indice du plus petit élément de la tranche l[a:a+1] est ind_min
    for i in range(a + 1, b):
        # supposons que l'indice du plus petit élément de la
        # tranche l[a:i] est ind_min
        if comp(l[i], l[ind_min]) < 0:
            ind_min = i
        # alors l'indice du plus petit élément de la tranche l[a:i+1]
        # est ind_min
    # à l'issue de l'itération l'indice du plus petit élément de la tranche
    # l[a:b] est ind_min
    return ind_min


def tri_select(l, comp=compare):
    """
    :param l: (list) une liste à trier
    :param comp: (fonction) [optionnel] une fonction de comparaison
                             Valeur par défaut : compare
    :return: (NoneType) aucune
    :Effet de bord: modifie la liste l en triant ses éléments selon l'ordre défini par comp
          Algorithme du tri par sélection du minimum
    :CU: l liste homogène d'éléments comparables selon comp
    :Exemples:

    >>> l = [3, 1, 4, 1, 5, 9, 2]
    >>> tri_select(l)
    >>> l == [1, 1, 2, 3, 4, 5, 9]
    True
    >>> from random import randrange
    >>> l1 = [randrange(1000) for k in range(randrange(100))]
    >>> l2 = l1.copy()
    >>> tri_select(l2)
    >>> est_trie(l2)
    True
    >>> all(l1.count(elt) == l2.count(elt) for elt in l1)
    True
    >>> all(l1.count(elt) == l2.count(elt) for elt in l2)
    True
    """
    n = len(l)
    # la tranche l[0:1] est triée
    for i in range(n - 1):
        # supposons la tranche l[0:i+1] triée
        ind_min = select_min(l, i, n, comp=comp)
        echanger(l, i, ind_min)
        # alors la tranche l[0:i+2] est triée
    # à l'issue de l'itération la tranche l[0:n] est triée

###################################################
#   TRI INSERTION                                 #
###################################################
def inserer(l, i, comp=compare):
    """
    :param l: (list) une liste
    :param i: (int) indice de l'élément de l à insérer dans l[0:i+1]
    :param comp: (fonction) [optionnel] une fonction de comparaison
                             Valeur par défaut : compare
    :return: (NoneType) aucune
    :Effet de bord: insère l'élément l[i] à sa place dans la tranche l[0:i+1]
             de sorte que cette tranche soit triée si l[0:i] l'est auparavant
    :CU: 0 <= i < long(l)
         éléments de l comparables par comp
         la tranche l[0:i] est triée
    :Exemples:

    >>> l = [1, 2, 4, 5, 3, 7, 6]
    >>> inserer(l, 4)
    >>> l == [1, 2, 3, 4, 5, 7, 6]
    True
    >>> inserer(l, 5)
    >>> l == [1, 2, 3, 4, 5, 7, 6]
    True
    >>> inserer(l, 6)
    >>> l == [1, 2, 3, 4, 5, 6, 7]
    True
    """
    aux = l[i]
    k = i
    while k >= 1 and comp(aux, l[k - 1]) < 0:
        l[k] = l[k - 1]
        k = k - 1    
    l[k] = aux

def tri_insert(l, comp=compare):
    """
    :param l: (list) une liste à trier
    :param comp: (fonction) [optionnel] une fonction de comparaison
    :return: (NoneType) aucune
    :Effet de bord : modifie la liste l en triant ses éléments selon l'ordre défini par comp
          Algorithme du tri par insertion
    :CU: l liste homogène d'éléments comparables selon comp
    :Exemples:

    >>> l = [3, 1, 4, 1, 5, 9, 2]
    >>> tri_insert(l)
    >>> l == [1, 1, 2, 3, 4, 5, 9]
    True
    >>> from random import randrange
    >>> l1 = [randrange(1000) for k in range(randrange(100))]
    >>> l2 = l1.copy()
    >>> tri_insert(l2)
    >>> est_trie(l2)
    True
    >>> all(l1.count(elt) == l2.count(elt) for elt in l1)
    True
    >>> all(l1.count(elt) == l2.count(elt) for elt in l2)
    True
    """
    n = len(l)
    # la tranche l[0:1] est triée
    for i in range(1, n):
        # supposons la tranche l[0:i] triée
        inserer (l, i, comp=comp)
        # alors la tranche l[0:i+1] est triée
    # à l'issue de l'itération la tranche l[0:n] est triée


###################################################
#   TRI RAPIDE                                    #
###################################################
def partitionner(l, debut, fin, comp=compare):
    '''
    :param l: (list) liste à partitionner
    :param debut, fin: (int) indices de début et de fin de la tranche de l
                       à partionner
    :return: (int) indice où se trouve le pivot (initialement à l'indice debut)
                   après le partionnement
    :effet de bord: après partionnement tous les éléments de la tranche l[debut:fin]
                    ont été déplacés de sorte que ceux situés à gauche du pivot soient
                    situés à sa gauche, et les autres à sa droite
    :CU: 0 <= debut < fin <= len(l)
    :Exemples:

    >>> l = [3, 1, 4, 1, 5, 9, 2]
    >>> ind_pivot = partitionner(l, 2, 6)
    >>> ind_pivot
    3
    >>> l
    [3, 1, 1, 4, 5, 9, 2]
    '''
    pivot = l[debut]
    ind_pivot = debut
    for i in range (debut+1, fin):
        if comp(pivot, l[i]) > 0:
            l[ind_pivot] = l[i]
            l[i] = l[ind_pivot+1]
            ind_pivot += 1
    l[ind_pivot] = pivot
    return ind_pivot

def tri_rapide(l, debut=0, fin=None, comp=compare):
    """
    :param l: (list) une liste à trier
    :param comp: (fonction) [optionnel] une fonction de comparaison
    :param debut, fin: (int) [optionnel] indices délimitant la tranche à trier
    :return: (NoneType) aucune
    :Effet de bord : modifie la liste l en triant 
          les éléments de la tranche l[debut:fin] selon l'ordre défini par comp
          Algorithme du tri rapide
    :CU: l liste homogène d'éléments comparables selon comp
    :Exemples:

    >>> l = [3, 1, 4, 1, 5, 9, 2]
    >>> tri_rapide(l)
    >>> l == [1, 1, 2, 3, 4, 5, 9]
    True
    >>> from random import randrange
    >>> l1 = [randrange(1000) for k in range(randrange(100))]
    >>> l2 = l1.copy()
    >>> tri_rapide(l2)
    >>> est_trie(l2)
    True
    >>> all(l1.count(elt) == l2.count(elt) for elt in l1)
    True
    >>> all(l1.count(elt) == l2.count(elt) for elt in l2)
    True
    """
    if fin is None: fin = len(l)
    if fin - debut > 1:
        ind_pivot = partitionner(l, debut, fin, comp=comp)
        tri_rapide(l, debut=debut, fin=ind_pivot, comp=comp)
        tri_rapide(l, debut=ind_pivot+1, fin=fin, comp=comp)

###################################################
#   TRI FUSION                                    #
###################################################

def separer(l):
    """
    :param l: (list) liste à séparer en deux
    :return: (tuple) couple de listes d'égales longueurs (à 1 près)
    :CU: aucune
    :Exemples:

    >>> l = [3, 1, 4, 1, 5, 9, 2]
    >>> l1, l2 = separer(l)
    >>> l3 = l1 + l2
    >>> len(l3) == len(l)
    True
    >>> all(k in l for k in l3)
    True
    >>> all(k in l3 for k in l)
    True
    """
    n = len(l)
    if n == 0:
        return ([], [])
    elif n == 1:
        return ([l[0]], [])
    else:
        l1, l2 = separer(l[2:])
        return ([l[0]] + l1, [l[1]] + l2)
    # autre possibilité
    # return (l[0:n//2], l[n//2:])

def fusionner(l1, l2, comp=compare):
    """
    :param l1, l2: (list) deux listes (supposées triées)
    :param comp: (optional) une fonction de comparaison
    :return: (list) une liste contenant les éléments de l1 et l2
              cette liste est triée si l1 et l2 le sont
    :UC: les éléments de l1 et l2 doivent être comparables selon comp
    :Exemples:

    >>> fusionner([1, 3, 4, 9], [1, 2, 5])
    [1, 1, 2, 3, 4, 5, 9]
    """
    if l1 == []:
        return l2.copy()
    elif l2 == []:
        return l1.copy()
    else:
        cmp = comp(l1[0], l2[0])
        if cmp <= 0:
            return [l1[0]] + fusionner(l1[1:], l2, comp=comp)
        else:
            return [l2[0]] + fusionner(l1, l2[1:], comp=comp)

def tri_fusion(l, comp=compare):
    """
    :param l: (list) une liste à trier
    :param comp: (fonction) [optionnel] une fonction de comparaison
                             Valeur par défaut : compare
    :return: (list) 
    :Effet de bord: aucun
          Algorithme du tri fusion
    :CU: l liste homogène d'éléments comparables selon comp
    :Exemples:

    >>> l = [3, 1, 4, 1, 5, 9, 2]
    >>> l2 = tri_fusion(l)
    >>> l2 == [1, 1, 2, 3, 4, 5, 9]
    True
    >>> from random import randrange
    >>> l1 = [randrange(1000) for k in range(randrange(100))]
    >>> l2 = tri_fusion(l1)
    >>> est_trie(l2)
    True
    >>> all(l1.count(elt) == l2.count(elt) for elt in l1)
    True
    >>> all(l1.count(elt) == l2.count(elt) for elt in l2)
    True    """
    n = len(l)
    if n <= 1:
        return l.copy()
    else:
        l1, l2 = separer(l)
        l1s = tri_fusion(l1, comp=comp)
        l2s = tri_fusion(l2, comp=comp)
        return fusionner(l1s, l2s, comp=comp)

###################################################
#   PYTHON SORTED                                 #
###################################################

def Python_sorted(l):
    return sorted(l)

def Python_sort(l):
    return l.sort()

###################################################
#   TRI PAR DENOMBREMENT / COUNTING SORT          #
###################################################

def count_sort(arr):
    size = len(arr)
    max_element = max(arr)
    min_element = min(arr)
    range = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count = [0 for _ in range(range)]
    output = [0] * size
    # Store count of each character
    for i in range(0, size):
        count[arr[i]-min_element] += 1
    # Change count[i] so that count[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count)):
        count[i] += count[i-1]
    # Build the output character array
    for i in range(len(arr)-1, -1, -1):
        output[count[arr[i] - min_element] - 1] = arr[i]
        count[arr[i] - min_element] -= 1
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, size):
        arr[i] = output[i]
    return arr

###################################################
#   LSD RADIX SORT ON INTEGERS                    #
###################################################

def tri_denombrement(l, significant_digit):
    size = len(l)
    output = [0] * size #Tableau de sortie
    count = [0] * 10 # Pour mémoriser le chiffre significatif à "regarder"
    # Calculer le nombre d'éléments
    for i in range(0, size):
        index1 = l[i] // significant_digit
        count[index1 % 10] += 1
    for i in range(1, 10): # 1 à 10 car on est sur du tri en base 10
        count[i] += count[i - 1]
    # Placement des éléments dans l'ordre trié en fonction de la clé actuelle
    i = size - 1
    while i >= 0:
        index1 = l[i] // significant_digit
        output[count[index1 % 10] - 1] = l[i]
        count[index1 % 10] -= 1
        i -= 1
    for i in range(0, size):
        l[i] = output[i]

def tri_radix_LSD(l, base=10): #version en base 10
    v_max = max(l) # Valeur maximale, qui définira le nombre de passes à effectuer sur la liste
    significant_digit = 1 # Chiffre significatif / clé 
    while v_max // significant_digit > 0: # Se termine quand il n'y a plus de chiffre significatif
        tri_denombrement(l, significant_digit) # Tri dénombrement
        significant_digit *= base # dizaines, centaines, ...
    return l

###################################################
#   MSD RADIX SORT ON STRINGS                     #
###################################################

def tri_radix_MSD(l, i=0):
    '''
    :param l: (list) une liste de mots
    :param i: (int) la position du premier caractère à regarder, 0 par défaut
    :return: (list) la liste initiale, avec les mots triés dans l'ordre alphabétique
    '''
    if len(l) <= 1: #Cas de la liste vide ou avec un seul élément
        return l
    
    wordsDict = {}
    keys = range(26)
    res = []
    tmp_struct = []
    
    for x in range(26):
        tmp_struct.append([])
        
    #for i in keys:
        #wordsDict[i] = []
        
    for word in l: #Pour chaque mot
        #print(word)
        if i >= len(word):
            res.append(word)
        else:
            #print(word[i]) # Digit que l'on examine
            #print(ord(word[i])) # Son code ASCII
            tmp_struct[ord(word[i]) - 65].append(word) #Code ASCII du caractère - 65 pour rentrer dans la liste
    #print(tmp_struct)
    tmp_struct = [tri_radix_MSD(j, i+1) for j in tmp_struct]
    for e_l in tmp_struct:
        for e in e_l:
            res.append(e)
            
    return res