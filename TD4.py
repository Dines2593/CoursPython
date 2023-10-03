import random

class Exo1():
    def tableau_aleatoire(self,n):
        array=[]
        for i in range(n):
            array.append(random.randint)
            
        return array

    def affiche_array(self,n): 
        s=""
        for x in (n):
            s+= str(x) + " "
        print(s)
    
    def double_les_impaires(self,tab):
        s=""
        for x in (tab):
            if x % 2 != 0:
                x = x+x
            s+= str(x) + " "
        print(s)
            
        
    def somme_valeurs(self,tab):
        total = 0
        for x in tab:
            total += x
        print(total)
        
    def somme_indices(self,tab):
        total = 0
        for i in range(len(tab)):
            total += tab[i]
        print(total)
    
    
    def mintab(self,tab):
        min_val = tab[0]
        for x in tab:
                if x < min_val:
                    min_val = x
        print(min_val)

    def indmin(self,tab):
        indice_min = 0
        for i in range(1, len(tab)):
            if tab[i] < tab[indice_min]:
                indice_min = i
        print(indice_min)
    
    def indice(self,tab,x):
        for i in range(len(tab)):
            if tab[i] == x:
                return i 
        return -1
    
    def triage(self,tab, x):
        elements_inf_x, elements_sup_x= [],[]
        for element in tab:
            if element < x:
                elements_inf_x.append(element)
            else:
                elements_sup_x.append(element)
        return elements_inf_x, elements_sup_x

class Exo2():
    def affichage_correct(self,n):
        print(n)
    
    def recherche(self,m,t):
        for i in range(len(t)):
            if t[i:i+len(m)] == m:
                return i
                break
        return -1


        
        
def main():
    exo1=Exo1()
    #exo1.affiche_array([2,3,4,5])
    #exo1.double_les_impaires([2,3,4,5])
    #exo1.somme_valeurs([2,3,4,5])
    #exo1.somme_indices([2,3,4,5])
    #exo1.mintab([2,3,4,1,5])
    #exo1.indmin([2,3,4,1,5])
    #v =exo1.indice([2,3,4,1,5],5)
    #print(v)
    #l1,l2 = exo1.triage([2,3,4,1,5],3)   
    #print(l1,l2)
    exo2=Exo2()
    #exo2.affichage_correct(str(int("3"+"4")))
    v=exo2.recherche("bra","acadbraabra")
    print(v)
    
if __name__=="__main__":
    main()
    
        
        
    