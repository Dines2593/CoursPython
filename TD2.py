from math import sqrt


def exo1():
    i1 = int(input("Entrez l'entier numerro 1 :"))
    i2 = int(input("Entrez l'entier numero 2 : "))
    print(f"La somme des deux entiers est: {i1+i2}")
# exo1()


# prix_horstaxe =float(input("Veuillez entrez le prix hors taxe :"))


def exo2(prix_horstaxe):
    tva = 0.20
    prix_ttc = prix_horstaxe * (1 + tva)
    print(f"Le prix toutes taxes comprises est de : {prix_ttc}")
# exo2(prix_horstaxe)


def exo4():
    x = int(input("Entrez l'entier numero  :"))
    valpoly = 3 * x**2 + 5 * x + 1
    print(f"La valeur du polynôme f(x): {valpoly}")
# exo4()


def exo3():
    x = int(input("Entrez l'entier numero  :"))
    res = 2*x+3
    print(f"L'image de x avec F(x)= 2x+ 3 est {res}")
# exo3()


def permutation():
    a = input("Entrez la valeur de a :")
    b = input("Entrez la valeur de b :")
    temp = a
    a = b
    b = temp
    print(
        f"La nouvelle valeur de a est {a} et la nouvelle valeur de b est : {b}")
# permutation()


def permutation_circulaire():
    a = input("Entrez la valeur de a :")
    b = input("Entrez la valeur de b :")
    c = input("Entrez la valeur de c :")
    temp = a
    a = c
    c = b
    b = temp
    print(
        f"La nouvelle valeur de a est {a} et la nouvelle valeur de b est : {b} et la nouvelle valeur de c est : {c}")
# permutation_circulaire()


def permutation_sans_temp():
    a = int(input("Entrez la valeur de a :"))
    b = int(input("Entrez la valeur de b :"))
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(
        f"La nouvelle valeur de a est {a} et la nouvelle valeur de b est : {b}")
# permutation_sans_temp()
# il est donc possible grâce au OU EXCLUSIF XOR d'échanger deux variables sans variables temporaires


def date1():
    JJ = input("Veuillez entrez le jour : ")
    MM = input("Veuillez entrez le mois : ")
    AA = input("Veuillez entrez l' année : ")
    print(f"La date d'aujourd'hui est le {JJ}/{MM}/{AA}")
# date1()


def date2():
    JJ = int(input("Veuillez entrez le jour : "))
    MM = input("Veuillez entrez le mois : ")
    AA = int(input("Veuillez entrez l' année : "))
    date = str(JJ)+"/"+str(MM)+"/"+str(AA)
    print("La date d'aujourd'hui est le ", date)
# date2()


def convertisseur_secondes():
    s = int(input("Veuillez entrez le nombre de secondes : "))
    jours = s//86400
    reste_secondes = s % 86400
    heures = reste_secondes // 3600
    reste_secondes = reste_secondes % 3600  # reste_secondes %=3600
    minutes = reste_secondes // 60
    s = reste_secondes % 60
    print(f"{s} secondes correspondent à {jours} jour(s), {heures} heure(s), {minutes} minute(s), {s} seconde(s)")
# convertisseur_secondes()


def maximus():
    a = int(input("Veuillez entrez la valeur de a : "))
    b = int(input("Veuillez entrez la valeur de b : "))
    maximus = max(a, b)
    print(f"Le maximus est {maximus}")
# maximus()


def maximusprime():
    a = int(input("Veuillez entrez la valeur de a : "))
    b = int(input("Veuillez entrez la valeur de b : "))
    c = int(input("Veuillez entrez la valeur de c : "))
    if a > b and a > c:
        maximusprime = a
    elif b > a and b > c:
        maximusprime = b
    else:
        maximusprime = c
    print(f"Le maximum est {maximusprime}")
# maximusprime()


def estpere():
    p = int(input("Veuillez entrez la valeur de p : "))
    if p % 2 == 0:
        print(f" {p} est paire")
    else:
        print(f" {p} est impaire")
# estpere()

# j'ai pas compris comment faire sans le modulo


def fullsecondegre():
    a = int(input("Veuillez entrez la valeur de a : "))
    b = int(input("Veuillez entrez la valeur de b : "))
    c = int(input("Veuillez entrez la valeur de c : "))
    delta = (b*b)-(4*a*c)
    print(delta)
    if delta > 0:
        x1 = ((-b) + (sqrt(delta))) / (2*a)
        x2 = ((-b) - (sqrt(delta))) / (2*a)
        print(
            f"Le discriminant est positif et les deux racinnes sont {x1} et {x2}")
    elif delta == 0:
        x3 = (-b) / (2*a)
        print(f"Le discriminant est nulle et la racine unique est {x3}")
    else:
        print("il n'y a pas de solutions réelles dans R")
# fullsecondegre()


def boucles():
    n = int(input("Entrez la valeur de n : "))
    """
    for i in range(1, n+1): #n+1 pour avoir le n inclu 
        print(i)
    
    for i in range(2, 2*(n+1), 2):
        print(i)
    
    i = 1
    c = 0
    while c < n:
        if i % 2 != 0:
            print(i)
            c += 1
        i += 1
    
    somme=0
    for i in range(1, n+1):
        somme +=i
    print(f"La somme des entiers de {n} est de {somme}")
    verif=n*(n+1)/2
    if verif == somme:
        print("Le résultat est correct")
    else:
        print(f"La somme ne correspond pas à la vérification qui est de {verif}")
    """
    somme_impair = 0
    for i in range(1, 2*n+1, 2):
        somme_impair += i
    print(f"Somme des {n} premiers nombres impairs : {somme_impair}")
    verif2 = n*n
    if somme_impair == verif2:
        print("Le résultat est correct")
    else:
        print(
            f"La somme ne correspond pas à la vérification qui est de {verif2}")
#boucles()

def divisiondemerde():
    dividende = int(input("Veuillez entrez la valeur de dividende : "))
    diviseur = int(input("Veuillez entrez la valeur de diviseur : "))
    quotient=0
    while dividende >= diviseur:
        dividende-= diviseur
        quotient +=1
        reste=dividende
    print(f"Quotient : {quotient} Reste : {reste}")
#divisiondemerde()

def bases_nb():
    n = int(input("Entrez la valeur de n : "))
    for i in range(1, n+1):
        print(f"Décimal : {i}")
        print(f"Binaire : {bin(i)}")  # Convertit en binaire '0b'
        print(f"Octal : {oct(i)}")    # Convertit en octal '0o'
        print(f"Hexadécimal : {hex(i)}\n")  # Convertit en hexadécimal '0x'
#bases_nb()

def suite_de_lucas():
    n = int(input("Entrez la valeur de n : "))
    u0=2
    u1=1
    print(f"U0 : {u0}")
    if n>0:
        print(f"U1 : {u1}")
    for i in range(2,n+1):
        Un = u1 +u0
        print(f"U{i} : {Un}")
        u0=u1
        u1=Un
#suite_de_lucas()


