from PyQt5.QtWidgets import *
from PyQt5 import uic

'''
Author: Roger Colomer & Arnau Tomassa
    No shan modificat valors del designer, els límits s'han establert mitjançant codi
    S'utilitza uic per importar el fitxer file1.uic creada amb el designer
    Es fan els sets del dial, LCD i del progress bar a 0 
    Es posen els limits del dial i del progress bar
    
    Finalment cada vegada que es canvia el dial s'executa la funció dialMogut
    es guarda el valor llegit a la variable v, la imprimeix per pantalla, fa el display del LCD
    i fa el set del progress bar
     '''

class FinPpal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('file1.ui', self)
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(0)
        self.lcdNumber.display(0)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        self.dial.valueChanged.connect(self.dialMogut)

    def dialMogut(self):
        v = self.dial.value()
        print(v)
        self.lcdNumber.display(v)
        self.progressBar.setValue(v)



app = QApplication([])
window = FinPpal()
window.show()
app.exec_()
