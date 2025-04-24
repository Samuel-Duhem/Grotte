class case:

    def __init__(self,symbole):
        self.terrain=symbole
        self.occupant=None
    '''on initialise la case avec son terrain et son occupant'''
    def libre(self):
        if self.terrain!= '#':
            return self.occupant ==None
        else :
            return False
    ''' on vérifie si la case est libre'''
    def depart (self):
        self.occupant=None
        '''fait partir le pion de la case'''
    def arrivee (self,pion):
        if self.terrain== 'O':
            pion.quite()
        else:
            self.occupant=pion
    ''' self.occupant pointe vers l'instance de la classe pion dans la case'''

    def __str__(self):
        if self.occupant:
            return str(self.occupant)
        return self.terrain












