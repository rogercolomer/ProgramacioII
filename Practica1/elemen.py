class Element:
    def __init__(self,n,p,f):
        self.nom = n        #string
        self.preu = p       #enter (si es 0 element trobat)
        self.fun = f        #bolea si es fungible o no

    def set_e(self,n,p,f):
        self.nom = n
        self.preu = p
        self.fun = f

    def get_e(self):
        return self.nom, self.preu, self.fun

    def __str__(self):
        string = "L'element "+self.nom+" amb preu "+str(self.preu)
        return string