from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
'''
Authors: Roger Colomer & Arnau Tomassa
    Primer de tot es creen els objectes widget (1,2,3,4)
    
    S'utilitza el codi de la fase 2 pero s'inicialitzen els objectes de widgets, dial i el lcd per codi
    es creen dos Layouts horitzontals i s'ajunten a un de vertical perquè es mostri correctament
    finalment es crea el widget final que agrupa el layout vertical i es fa el central widget.
    
    La funcionalitat és com la fase 2 es connecta la signal de canvi de valor del dial amb la funció que pinta
    els widgets
     '''
cas0 = ["(255, 255, 255)", "(255, 255, 255)", "(255, 255, 255)", "(255, 255, 255)"]
cas1 = ["(0, 255, 0)", "(255, 255, 255)", "(255, 255, 255)", "(255, 255, 255)"]
cas2 = ["(0, 255, 0)", "(255, 255, 0)", "(255, 255, 255)", "(255, 255, 255)"]
cas3 = ["(0, 255, 0)", "(255, 255, 0)", "(255, 165, 0)", "(255, 255, 255)"]
cas4 = ["(0, 255, 0)", "(255, 255, 0)", "(255, 165, 0)", "(255, 0, 0)"]


class FinPpal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('file2.ui', self)
        self.widget_1 = QWidget(self)
        self.widget_2 = QWidget(self)
        self.widget_3 = QWidget(self)
        self.widget_4 = QWidget(self)

        self.setStyleSheet("""QMainWindow{background-color: rgb(255, 255, 255);}""")
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(0)
        self.lcdNumber.display(0)

        lay1 = QHBoxLayout(self)
        lay1.addWidget(self.dial)
        lay1.addWidget(self.lcdNumber)

        lay2 = QHBoxLayout(self)
        lay2.addWidget(self.widget_1)
        lay2.addWidget(self.widget_2)
        lay2.addWidget(self.widget_3)
        lay2.addWidget(self.widget_4)

        lay3 = QVBoxLayout(self)
        lay3.addLayout(lay2)
        lay3.addLayout(lay1)

        cw = QWidget()
        cw.setLayout(lay3)
        self.setCentralWidget(cw)

        self.dial.valueChanged.connect(self.dialMogut)

    def dialMogut(self):
        v = self.dial.value()
        self.lcdNumber.display(v)
        if v == 0:
            self.color_widget(cas0)
        elif 0 < v <= 25:
            self.color_widget(cas1)
        elif 25 < v <= 50:
            self.color_widget(cas2)
        elif 50 < v <= 75:
            self.color_widget(cas3)
        elif 75 < v <= 100:
            self.color_widget(cas4)

    def color_widget(self,val):
        self.widget_1.setStyleSheet("QWidget{background-color: rgb"+val[0]+";}")
        self.widget_2.setStyleSheet("QWidget{background-color: rgb"+val[1]+";}")
        self.widget_3.setStyleSheet("QWidget{background-color: rgb"+val[2]+";}")
        self.widget_4.setStyleSheet("QWidget{background-color: rgb"+val[3]+";}")

app = QApplication([])
window = FinPpal()
window.show()
app.exec_()
