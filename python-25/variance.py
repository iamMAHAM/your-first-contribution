from math import sqrt
L = [9, 10, 11, 20.5, 0, 12.0, -5, -8.3]

# def est le mot clé pour créer une fonction
#pour le nom de la fonction on met nom_fonction():
def rec_moy(liste:list[float]) -> float:
    #cette variable recevra la somme des valeur
    somme = 0

    #on à deux méthode pour faire la somme des éléments du tableau
    #soit la fonction native sum()
    #soit une boucle pour faire l'addition 
    for element in liste:

        #somme = somme + element 
        somme += element
    moyenne = somme / len(liste) #len = 7
    return moyenne

def rec_variance(liste:list[float]) -> float:
    moyenne = rec_moy(liste)
    somme_ecart = 0
    for element in liste:
        somme_ecart += (element-moyenne)**2
    variance = somme_ecart/len(liste)
    return variance

def rec_ecart_type(liste:list[float]):
    variance = rec_variance(liste)
    ecart_type = sqrt(variance)
    return ecart_type

if __name__ == "__main__":
   
    print("variance: ",rec_variance(L))
    
