from qualitats import Qualitats

class Jugador:
    def __init__(self,n,q):
        self.nom = n
        self.salut = 50
        self.riquesa = 100
        self.qualitats = Qualitats(q[0],q[1],q[2])
        self.elements = []

    def get_sal(self):
        return self.salut

    def get_player(self):
        return self.nom, self.salut, self.riquesa, self.qualitats.get_q(),self.elements

    def get_e_player(self):
        #consutla els elements que te el jugador
        return self.elements

    def get_riquesa(self):
        return self.riquesa

    def set_riquesa(self,r):
        self.riquesa = r

    def set_sal(self,s):
        self.salut = s

    def add_e(self,e):  #afegir element a el jugador
        self.elements.append(e)

    def del_e(self,e):
        self.elements.remove(e)
