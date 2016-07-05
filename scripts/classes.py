class Client:
    
    def __init__(self, nouveau_client=True, ville="Paris"):
        self.nouveau_client=nouveau_client
        self.ville=ville

    def affiche_type(self):
        print self.nouveau_client
    
def est_parisien(self):
    if self.ville=="Paris":
        return True
    else:
        return False
        
        
class CompteBancaire:
    def __init__(self,nom="A",solde=0):
        self.nom=nom
        self.solde=solde
    
    def depot(self,somme):
        self.solde+=somme
        
    def retrait(self,somme):
        self.solde-=somme
    
    def affiche(self):
        print self.solde



class Vehicule:
    def __init__(self,type_trans=""):
        self.type_trans=type_trans

    def affiche(self):
        print 333
    
class Train(Vehicule):
    def __init__(self, vitesse=100, **kwargs):
        super(Train, self).__init__(**kwargs)
        self.vitesse=vitesse
        
    def affiche(Train, self):
        print 444
    
        