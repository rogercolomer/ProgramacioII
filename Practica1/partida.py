from elemen import Element
from jugador import Jugador
import os

class Partida:
    def __init__(self):
        self.jugadors = dict() # {'jugador1': jugador1.Jugador(jugador1,[1,2,3]),'jugador2':jugador2.Jugador(jugador2,[2,3,4])}
        self.elements = dict() # {'element1': [elements.Element(e1,50,False),quantitat_elements]... }
        self.partides = [[],[]]

    def delete_player(self,n):
        if self.comp_player(n):
            del self.jugadors[n]
            print('El jugador '+n+' ha estat eliminat de la partida')
        else:
            print('El jugador '+n+' no existeix en aquesta partida')


    def add_player(self,n,q):
        if self.comp_player(n)==False:
            self.jugadors[n] = Jugador(n,q)
            print('El jugador '+n+' sha unit a la partida')
        else:
            print('El jugador '+n+' ja existeix')

    def add_element(self,n,p,f,q):    #nom preu fungible quantitat
        if self.comp_element(n)==False:
            self.elements[n] = [Element(n,p,f),q]
            print("Sha afegit l'element "+n)
        else:
            self.elements[n][1] = self.elements[n][1]+1

    def dec_salut(self,n,s):
        #input nom jugador i salut a restar
        sal_total = self.jugadors[n].get_sal()-s
        if sal_total >0:
            self.jugadors[n].set_sal(sal_total)
            print("La salut del jugador "+n+ " és de "+str(sal_total))
        else:
            self.delete_player(n)


    def buy_element(self,n,e):      #un  jugador compra un element
        if self.comp_element(e) and self.comp_player(n):
            if self.jugadors[n].get_riquesa()>=self.elements[e][0].get_e()[1] :
                if self.elements[e][1]>0:
                    self.jugadors[n].add_e(e)
                    self.jugadors[n].set_riquesa(self.jugadors[n].get_riquesa()-self.elements[e][0].get_e()[1])
                    self.elements[e][1] -=1
                    print("Element "+e+" comprat per "+n)
                else:
                    print("No queden elements "+e+" a la partida")
            else:
                print("El jugador "+n+" no te prous diners per comprar l'element "+e)
        else:
            print("El jugador o l'element seleccionat no existeix")

    def use_element(self,n,e):
        if self.comp_element(e) and self.comp_player(n):
            print("L'element "+e+" ha estat utilitzat per en "+n)
            if self.elements[e][0].get_e()[2]:
                self.jugadors[n].del_e(e)
                print("Com que l'element es fungible s'ha eliminat")
            else:
                pass
        else:
            print("El jugador o l'element no existeixen")
    def comp_player(self,n):
        #comprovador de jugadors si existeixen
            for key in self.jugadors:
                if key == str(n) :
                    return True
            return False

    def comp_element(self,e):
        # comprovador de elements si existeixen
        for key in self.elements:
            if key == str(e) :
                return True
        return False
    def import_partida(self,path):
        pass

    def read_file(self,fileName):
        f = open(fileName)
        linea = None
        value = []
        while linea != "":
            linea = f.readline()
            if linea != '':
                value.append(linea.split())
            else:
                pass
        f.close()
        return value

    def read_elements(self,name):
        value =self.read_file("elements/"+name)
        for e in value:
            n = e[0]
            p = int(e[1])
            if e[2] == 'True':
                f = True
            else:
                f = False
            q = int(e[3])
            self.add_element(n,p,f,q)

    def read_players(self,name):
        for p in self.read_file("jugadors/"+name):
            if p != []:
                n = p[0]
                s = int(p[1])
                r = int(p[2])
                q = [int(p[3]), int(p[4]), int(p[5])]
                self.add_player(n,q)    #afegim el jugador
                if len(p) > 6:          #mirem que ene el fitxer no hi hagin elements del jugador
                    for i in range(6,len(p)):
                        self.jugadors[n].add_e(p[i])
                self.jugadors[n].set_sal(s)     #realitzem un set de la salut ja que l'init esta a 50
                self.jugadors[n].set_riquesa(r) #realitzem un set de la riquesa ja que l'init esta a 100

    def __str__(self):
        val = '\n'
        #Generem la string de noms i porpietats de cada jugador
        for k in self.jugadors:
            n,s,r,q,e = self.jugadors[k].get_player()
            str1 = 'Jugador: '+n+' , salut: '+str(s)+' , riquesa: '+str(r)+' ,Qualitats: [f: '+str(q[0])+' ,m: '+str(q[1])+' ,v: '+str(q[2])+' ], elements: '+str(e)+'\n'
            val = val+str1

        for k in self.elements:
            ne,pe,f = self.elements[k][0].get_e()
            qe = self.elements[k][1]

            if qe>1:
                str1 = 'Hi ha ' + str(qe) + ' elements ' + ne + ' de preu ' + str(pe) +  '\n'
            elif qe==1:
                str1 = 'Hi ha ' + str(qe) + ' element ' + ne + ' de preu ' + str(pe) +  '\n'
            else:
                str1 = 'No hi ha cap element ' + ne + ' de preu ' + str(pe) + ' '+'\n'
            val = val+str1
        return val