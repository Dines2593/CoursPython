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

def exo4():
    x= int(input("Entrez l'entier numero  :"))
    valpoly= 3 * x**2 + 5 * x + 1
    print(f"La valeur du polynôme f(x): {valpoly}")
#exo4()

def exo3():
    x= int(input("Entrez l'entier numero  :"))
    res = 2*x+3
    print(f"L'image de x avec F(x)= 2x+ 3 est {res}")
#exo3()

def permutation():
    a= input("Entrez la valeur de a :")
    b= input("Entrez la valeur de b :")
    temp =a 
    a = b
    b= temp
    print(f"La nouvelle valeur de a est {a} et la nouvelle valeur de b est : {b}")
#permutation()

def permutation_circulaire():
    a= input("Entrez la valeur de a :")
    b= input("Entrez la valeur de b :")
    c= input("Entrez la valeur de c :")
    temp =a
    a = c
    c =b
    b= temp
    print(f"La nouvelle valeur de a est {a} et la nouvelle valeur de b est : {b} et la nouvelle valeur de c est : {c}")
#permutation_circulaire()

def permutation_sans_temp():
    a= int(input("Entrez la valeur de a :"))
    b= int(input("Entrez la valeur de b :"))    
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"La nouvelle valeur de a est {a} et la nouvelle valeur de b est : {b}")
#permutation_sans_temp()
#il est donc possible grâce au OU EXCLUSIF XOR d'échanger deux variables sans variables temporaires

def date1():
    JJ = input("Veuillez entrez le jour : ")   
    MM = input("Veuillez entrez le mois : ")
    AA = input("Veuillez entrez l' année : ")
    print(f"La date d'aujourd'hui est le {JJ}/{MM}/{AA}")
#date1()

def date2():
    JJ = int(input("Veuillez entrez le jour : "))   
    MM = input("Veuillez entrez le mois : ")
    AA =int(input("Veuillez entrez l' année : "))
    date = str(JJ)+"/"+str(MM)+"/"+str(AA)
    print("La date d'aujourd'hui est le ",date)
#date2()
    
def convertisseur_secondes():
    s = int(input("Veuillez entrez le nombre de secondes : "))
    jours = s//86400
    reste_secondes= s % 86400
    heures = reste_secondes // 3600
    reste_secondes = reste_secondes % 3600   #reste_secondes %=3600
    minutes = reste_secondes // 60
    s = reste_secondes % 60
    print(f"{s} secondes correspondent à {jours} jour(s), {heures} heure(s), {minutes} minute(s), {s} seconde(s)")
convertisseur_secondes()


    
    

