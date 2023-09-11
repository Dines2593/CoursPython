def qst1():
    print("hello world!")

#qst1()

def qst2():
    r = 17
    n = 3.14
    print(r)
    print(n)
    r = input("Saisissez un réel: ")
    n = input("Saisissez un entier: ")
    p= input("Saisissez votre pushing P :")
    print(f"Bonjour {p}")
    k="Bonjour "+ p 
    print(k)
    print("Bonjour",p)

#qst2()

def qst3():
    a,b,c,d,e,f=12,7.53, "A", "abc def", True, b'TG lUQMAN' 
    for element in [a,b,c,d,e,f]:
        print(element , type(element))
#qst3()

def qst4():
    numbers = [4 / 3, 4-3 * 5, 10 == 5, 4 // 3, (4-3)**5,18 / 3 // 2, 5 == 11-6, 4.3 // 3.0, 0.2-0.1, False or (5!= 4), 0 / 1.3,0.3 - 0.2 == 0.2 - 0.1] # création d'une liste entre crochets
    for element in numbers:
        print(type(element))
#qst4()

def qst5():
    n1 = int(input("Veuillez saisir votre note 1: "))
    n2 =int(input("Veuillez saisir votre note 2: "))
    print(f"Votre Moyenne entière de {n1} et {n2} est de {(n1+n2)/2}")
    print(f"Votre Moyenne réelle de {n1} et {n2} est de {(n1+n2)//2}")
#qst5()

def qst6():
    e1 = int(input("Entrez votre entier n°1 : "))
    e2 = int(input("Entrez votre entier n°2 : "))
    print(f"Le quotient de la division de {e1} par {e2} est {e1//e2}, et le reste est {e1%e2}")
#qst6()

def qst7():
    i1 = int(input("Entrez votre entier n°1 : "))
    i2 =  int(input("Entrez votre entier n°2 : "))
    print(f"Le résultat est {(-i2)/(i1)}")
qst7()


