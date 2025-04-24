class pion:

    def __init__(self,jeu,ordre,l=0,c=1,d=1):
        self.l=l
        self.c=c
        self.d=d
        self.jeu=jeu
        self.ordre=ordre
    '''on initialise un pion avec ses coordonées, sa dirrection, un pointeur vers l'instance de jeu et son ordre d'arrivé dans le jeu'''

    def action(self,num):
        if num==0:
            if self.d==1: self.d=-1
            else: self.d=1
        elif num==1:
            self.jeu.grotte[self.l][self.c].depart()
            self.jeu.grotte[self.l+1][self.c].arrivee(self)
            self.l+=1
        else:
            self.jeu.grotte[self.l][self.c].depart()
            self.jeu.grotte[self.l][self.c+self.d].arrivee(self)
            self.c+=self.d
    '''effectue les différentes actions sur le pion'''

    def quite(self):
        self.jeu.grotte[self.l][self.c].depart()
        self.jeu.nb+=1
        print ('score: '+str(self.jeu.nb))
        '''retire le pion du jeu et incrémente le score'''



    def __str__(self):
        if self.d ==1:
            return '>'
        else:
            return '<'



