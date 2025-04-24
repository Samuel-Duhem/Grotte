import Classe_cases as c
import Classe_pion as p

class jeu:

    def __init__(self):
        f=open('CircuitGrotte.txt','r',encoding= 'utf-8')
        terrain=f.readlines()
        f.close()
        cases=[]
        for i in range(len(terrain)):
            cases.append([])
            terrain[i]=terrain[i].rstrip('\n')
            cases[i]=list(terrain[i])
            for j in range(len(cases[i])):
                cases[i][j]=c.case(cases[i][j])
        self.grotte=cases
        self.nb=0
        self.nbPions=0
    '''initialise une matrice qui prend chaque élément du fichier et en fait un objet de type case représentant la grotte.
    Il y a aussi une variable de score et la nombre de pions pour avoir l'ordre de chaque pions'''

    def affiche(self):
        for ligne in self.grotte:
            print(''.join(str(case) for case in ligne))
    '''afficher la grotte ligne par ligne'''

    def tour(self):
        Occupe=[]
        for inter in self.grotte:
            for InCase in range(len(inter)):
                if inter[InCase].occupant!= None:
                    Occupe.append(inter[InCase].occupant)
        for pion in sorted(Occupe, key=lambda pion:pion.ordre):
            '''actionne chaque pion par leur ordre d'arrivée'''
            dir=pion.d
            if self.grotte[pion.l+1][pion.c].libre():
                pion.action(1)
            elif not self.grotte[pion.l][pion.c+dir].libre():
                pion.action(0)
            else:
                pion.action(2)

    def demarre(self):
        while True:
            commande = input("Commandes : + pour ajouter un pion, q pour quitter, Entrée pour jouer un tour, s pour afficher le score : ")
            if commande == '+':
                self.tour()
                self.nbPions+=1
                self.grotte[0][1].arrivee(p.pion(self,self.nbPions))
                self.affiche()
            elif commande == 'q':
                print ('score final: '+str(self.nb))
                break
            elif commande == '':
                self.tour()
                self.affiche()
            elif commande == 's':
                print ('score: '+str(self.nb))
    '''lance une boucle infini qui demande si on ajoute un pion, les fait avancer, affiche le score ou finit le jeu'''

