#cette fonction permet de calculer la modalité d'une séquence et de la renvoyée
def modality(sequence):
    mode = 0
    #La boucle prend chaque élément de la séquence.
    for element in sequence:
        #Ici, on prend un élément et on compare son occurrence à la variable mode
        #qui représente la modalité ici. Si l'occurrence est supérieur à la valeur précédente alors
        #on prend cet élément et ont l'attribut à la variable mode.
        if sequence.count(element) > mode:
            mode = element

    return mode