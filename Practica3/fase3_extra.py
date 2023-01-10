from PyQt5.QtWidgets import *
from PyQt5 import uic


class FinPpal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.dial = QDial(self)
        self.lcdNumber = QLCDNumber(self)
        self.progressBar = QProgressBar(self)
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(0)
        self.lcdNumber.display(0)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        lay1 = QHBoxLayout(self)
        lay1.addWidget(self.dial)
        lay1.addWidget(self.lcdNumber)

        lay2 = QVBoxLayout(self)
        lay2.addWidget(self.progressBar)
        lay2.addLayout(lay1)

        cw = QWidget()
        cw.setLayout(lay2)
        self.setCentralWidget(cw)


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
