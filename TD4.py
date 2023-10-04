import random
import turtle
import tkinter 

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
        
class Exo3():    
    def recherche(self,m,t):
        for i in range(len(t)):
            if t[i:i+len(m)] == m:
                return i
                break
        return -1

class Exo4():
    def maj(self,txt):
        resultat = ""
        for char in txt:
            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                if 97 <= ord(char) <= 122:
                    char = str.upper(char)
                resultat += char
        return resultat
    
    def cesar(self,txt,dec):
        txt = self.maj(txt)
        texte_chiffre = []

        for char in txt:
            if 'A' <= char <= 'Z':
                # Appliquer le chiffrement de César aux majuscules
                char_chiffre = chr((ord(char) - ord('A') + dec) % 26 + ord('A'))
            else:
                # Ne rien faire pour les caractères non alphabétiques
                char_chiffre = char

            texte_chiffre.append(char_chiffre)

        return ''.join(texte_chiffre)
    
class Exo7():
    def dragon(self,n):
        if n == 1:
            return [False]
        dragon_n_1 = self.dragon(n - 1)  
        return dragon_n_1 + [False] + [not x for x in reversed(dragon_n_1)]
        #courbe_dragon = dragon(n)
        #print(courbe_dragon)
    
    
    def afficheDragon(self,n):
        # Récupérer la courbe du dragon d'ordre n
        courbe_dragon = self.dragon(n)
        
        # Configurer la tortue
        #turtle.speed(2)  # Vitesse de dessin
        #turtle.penup()   # Lever le stylo pour se déplacer sans dessiner
        #turtle.goto(-200, 0)  # Position initiale
        
        # Dessiner la courbe du dragon
        for virage_a_gauche in courbe_dragon:
            if virage_a_gauche:
                turtle.left(90)
            else:
                turtle.right(90)
            turtle.forward(10)
        
        # Afficher la fenêtre graphique
        turtle.done()
        turtle.Terminator()



        
        
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
    exo3=Exo3()
    #v=exo3.recherche("bra","acadbraabra")
    #print(v)
    exo4=Exo4()
    #v=exo4.maj("bonjourejbdfjkez")
    #print(v)
    #v=exo4.cesar("BONJOUrzORG ",2)
    #print(v)
    exo7=Exo7()
    #v=exo7.dragon(2)
    #print(v)
    exo7.afficheDragon(10)
    
    
    
    
if __name__=="__main__":
    main()
    
        
        
    