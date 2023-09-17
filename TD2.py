def exo1():
    i1 = int(input("Entrez l'entier numerro 1 :"))
    i2 = int(input("Entrez l'entier numero 2 : "))
    print(f"La somme des deux entiers est: {i1+i2}")
#exo1()


#prix_horstaxe =float(input("Veuillez entrez le prix hors taxe :"))

  
def exo2(prix_horstaxe):
    tva = 0.20 
    prix_ttc = prix_horstaxe * (1 + tva)
    print(f"Le prix toutes taxes comprises est de : {prix_ttc}")
#exo2(prix_horstaxe)

def exo3():
    x= int(input("Entrez l'entier numero  :"))
    valpoly= 3 * x**2 + 5 * x + 1
    print(f"La valeur du polynôme f(x): {valpoly}")
#exo3()