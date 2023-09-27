class Exo1:
    def factorielle(self, n):
        assert type(n) is int, "Factorielle d'un entier"
        fact = 1
        for i in range(1, n+1):
            fact = fact * i

        return (fact)

    def coefficient_binomial(self, n, k):
        assert type(n) is int, "n est un entier"
        assert type(k) is int, "k est un entier"
        coeff = self.factorielle(n)//(self.factorielle(k) * self.factorielle(n-k))
        return (coeff)

    def newton(self, n):
        assert type(n) is int, "n est un entier"
        assert not (n == 0), "n différent de 0"
        assert not (n > 10), "n inférieur a 10"
        chaine = "(a + b)^" + str(n) + " = "

        for k in range(n+1):
            c = self.coefficient_binomial(n, k)
            p = n-k

            if not (c == 1):
                chaine = chaine + str(c)
            if not (p == 0):
                chaine = chaine + "a"
                if not (p == 1):
                    chaine = chaine + "^" + str(p)
            if not (k == 0):
                chaine = chaine + "b"
                if not (k == 1):
                    chaine = chaine + "^" + str(k)
            if k < n:
                chaine = chaine + " + "

        print(chaine)
        

        
    def triangle_de_pascal(self,n):
        assert type(n) is int, "n est un entier"
        assert not (n == 0), "n différent de 0"
        assert not (n > 10), "n inférieur a 10"
        for i in range(n+1):
            chaine = ""
            for k in range (i+1):
                c=self.coefficient_binomial(i,k)
                chaine = chaine + str(c)+ " "
            print(chaine)
   
     
    def new_ton(self,n):
        assert type(n) is int, "n est un entier"
        assert not (n == 0), "n différent de 0"
        assert not (n > 10), "n inférieur a 10"
        resultat = "(a + b)^" + str(n) + " = "
    
        for k in range(n + 1):
            coeff = self.coefficient_binomial(n,k)
            
            if coeff != 0:
                if coeff > 0 and k != 0:
                    resultat = resultat + "+"
                resultat = resultat + str(coeff)
                
                if k != 0:
                    resultat = resultat + "^" + str({n-k})
                if k != n:
                    resultat =  resultat + "^" + str(k)
        
        print(resultat)

        
        
        
        


def main():
    print("Hello World!")
    exo1 = Exo1()  # instancier la classe
    #f = int(input("Calculer la factorielle pour f = "))
    #facto = exo1.factorielle(f)
    #print(facto)
    #c = int(input("Calculer le coeff binomial pour c = "))
    #d = int(input("Calculer le coeff binomial pour d = "))
    #coeff_bin = exo1.coefficient_binomial(c, d)
    #print(coeff_bin)
    #n = int(input("Calculer le binome de Newton pour n = "))
    #exo1.newton(n)
    #exo1.triangle_de_pascal(3)
    n = int(input("Calculer le binome de Newton pour n = "))
    exo1.new_ton(n)


if __name__ == "__main__":
    main()
