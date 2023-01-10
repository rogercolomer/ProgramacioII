from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import *
import time
import random

class Quadrat(QPushButton):
    ide = pyqtSignal(list)
    def __init__(self, text, pare, c, pos, n):
        super().__init__(text, pare)
        self.text = text
        self.off = int(c/n)
        self.setFixedSize(int(c/n), int(c/n))
        self.position = pos
        self.move(self.position[0]*int(c/n), self.position[1]*int(c/n))
        self.clicked.connect(self.identifier)

    def identifier(self):
        self.ide.emit(self.position)

    def set_position(self,pos):
        self.position = pos

    def moving(self,position):
        self.move(position[0]*self.off, position[1]*self.off)

    def get_t(self):
        return self.text


class Marc(QWidget):
    co = pyqtSignal(bool)
    def __init__(self, pare, c, n):
        super().__init__(pare)
        self.setFixedSize(c, c)
        self.n = n
        self.c = c
        self.q = []
        self.off = int(c/n)
        self.whitespace = [n-1, n-1]
        self.correct = False
        self.enable = False
        self.matrix()            #creem la matriu

        #Inicialitzem les senyals
        p = 1
        for i in self.q:
            for j in i:
                if p != n * n:
                    if j!=0:
                        j.ide.connect(self.prem)
                else:
                    break
        pare.button.estat.connect(self.selestat)

    def matrix(self):
        self.a = []
        for k in range(self.n*self.n - 1):
            self.a.append(k + 1)
        random.shuffle(self.a)
        p=0
        for i in range(self.n):
            fila = []
            for j in range(self.n):
                if p != (self.n*self.n)-1:
                    fila.append(Quadrat(str(self.a[p]), self, self.c, [i,j], self.n))
                    p += 1
                else:
                     fila.append(0)
            self.q.append(fila)

    def prem(self, a):
        e1 = a[0] + 1 == self.whitespace[0] and a[1] == self.whitespace[1]
        e2 = a[0] == self.whitespace[0] and a[1]+1 == self.whitespace[1]
        e3 = a[0] - 1 == self.whitespace[0] and a[1] == self.whitespace[1]
        e4 = a[0] == self.whitespace[0] and a[1] - 1 == self.whitespace[1]
        if self.enable:
            if e1 or e2 or e3 or e4:
                #process events
                self.q[a[0]][a[1]].move(self.whitespace[0]*self.off, self.whitespace[1]*self.off)
                self.q[a[0]][a[1]].set_position(self.whitespace)
                self.q[self.whitespace[0]][self.whitespace[1]] = self.q[a[0]][a[1]]
                self.q[a[0]][a[1]] = 0
                self.whitespace = a

                self.co.emit(True)
                print('done')
                self.correct = self.verify()
                print(self.correct)
        else:
            pass

    def verify(self):
        '''
        metode per verificar si la solució és correcte
        '''
        com = 1
        veri = []
        correct = 0
        for i in range(self.n):
            fila = []
            for j in range(self.n):
                if com != self.n*self.n:
                    fila.append(com)
                else:
                    fila.append(0)
                com += 1
            veri.append(fila)

        for i in range(self.n):
            for j in range(self.n):
                if self.q[j][i]!=0:
                    # print(self.q[j][i].get_t(),veri[i][j])
                    if int(self.q[j][i].get_t()) == veri[i][j]:
                        correct += 1
                else:
                    if self.whitespace == [self.n -1,self.n-1]:
                        correct += 1
        if correct == self.n*self.n:
            return True
        else:
            return False

    def selestat(self, a):
        if a == 1:
            self.enable = True
        else:
            self.enable = False
            # self.reset_quadrats()

    def set_enable(self, b):
        self.enable = b

    def get_correct(self):
        return self.correct


class button_v2(QPushButton):
    estat = pyqtSignal(int)

    def __init__(self,text,pare):
        super().__init__(text, pare)
        self.clicked.connect(self.state)
        self.es = 0
    def state(self):
        self.es += 1
        if self.es>2:
            self.es=1
        self.estat.emit(self.es)


class SpinH(QSpinBox):
    change_n = pyqtSignal(int)
    def __init__(self,n):
        super().__init__()
        self.setValue(n)
        self.valueChanged.connect(self.new_value)

    def new_value(self):
        self.change_n.emit(self.value())


class FinestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n = 3
        self.c = 600
        self.comptador_general = 0
        self.comptador_timer = 0
        self.estado = 0

        self.progressBar = QProgressBar(self)
        self.lcdNumber = QLCDNumber(self)
        self.button = button_v2('Gaas!', self)
        self.sp = SpinH(self.n)
        self.lb = QLabel()


        self.m = Marc(self, self.c, self.n)

        self.lb.setText('Molta sort!')
        self.lcdNumber.display(0)
        self.lcdNumber.setFixedHeight(200)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        self.sp.setFixedWidth(200)

        lay1 = QVBoxLayout(self)

        lay1.addWidget(self.lcdNumber)
        lay1.addWidget(self.sp)
        lay1.addWidget(self.progressBar)
        lay1.addWidget(self.button)
        lay1.addWidget(self.lb)

        self.lay2 = QHBoxLayout(self)
        self.lay2.addLayout(lay1)
        self.lay2.addWidget(self.m)

        cw = QWidget()
        cw.setLayout(self.lay2)
        self.setCentralWidget(cw)

        self.timer = QTimer()
        self.timer.setInterval(1000)

        self.timer.timeout.connect(self.update_bar)     #comptador timer
        self.m.co.connect(self.comp_gen)                #comptador de passos
        self.button.estat.connect(self.maquina_estats)             #connector de lestat del boto
        self.sp.change_n.connect(self.set_n)

    def maquina_estats(self,a):
        '''

        :param a: esta de la maquina
            0 = inici
            1 = jugant
            2 = reset/stop
        :return: Null
        '''
        self.estado = a
        if a == 0:
            pass
        elif a == 1:
            self.button.setText('Stop')
            self.timer.start()
            # self.reiniciar_marc()
        elif a == 2:
            self.button.setText('Tornar a començar')
            self.lb.setText('Molta sort!')
            self.timer.stop()
            self.comptador_general = 0
            self.comptador_timer = 0
            self.lcdNumber.display(self.comptador_general)
            self.progressBar.setValue(self.comptador_timer)
            self.reiniciar_marc()

    def set_n(self, a):
        self.n = a
        if self.estado == 2 or self.estado == 0 and self.n>0:
            self.reiniciar_marc()

    def reiniciar_marc(self):
        self.lay2.removeWidget(self.m)
        self.m.deleteLater()
        self.m = Marc(self, self.c, self.n)
        self.m.co.connect(self.comp_gen)
        self.lay2.addWidget(self.m)

    def comp_gen(self,a):
        self.comptador_general += 1
        self.lcdNumber.display(self.comptador_general)
        print(self.comptador_general)

    def update_bar(self):
        self.comptador_timer += 1
        if self.comptador_timer == 100:
            self.estado = 2
            self.m.set_enable(False)
        self.progressBar.setValue(self.comptador_timer)
        if self.m.get_correct():
            self.lb.setText('SOLUCIONAT!')
            self.m.set_enable(False)
            self.timer.stop()
            self.estado = 2


app = QApplication([])
window = FinestraPrincipal()
window.show()
app.exec_()
