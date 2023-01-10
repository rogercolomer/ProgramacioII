from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
'''
Author: Roger Colomer & Arnau Tomassa
    No shan modificat valors del designer, els límits s'han establert mitjançant codi
    S'utilitza uic per importar el fitxer file1.uic creada amb el designer
    Es fan els sets del dial, LCD i els widgets no sinicialitzen (defecte blanc)
    També sha posat el fons de la finestra de color blanc, quda mes cuqui
    Es posen els limits del dial i del progress bar

    Finalment cada vegada que es canvia el dial s'executa la funció dialMogut
    es guarda el valor llegit a la variable v, i s'executa la funcion color_widget 
    s'han guardat els colors de cada cas en una llista per cridar a la funció
    també es fa el set del LCD
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
        self.setStyleSheet("""QMainWindow{background-color: rgb(255, 255, 255);}""")
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(0)
        self.lcdNumber.display(0)

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
