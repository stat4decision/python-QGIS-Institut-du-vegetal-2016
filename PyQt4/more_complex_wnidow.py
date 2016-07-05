
# -*- coding:latin1 -*-
import sys
from PyQt4 import QtGui, QtCore

class Boite(QtGui.QWidget):
    def __init__(self):
        super(Boite, self).__init__()
        self.initBoite()
        
    def initBoite(self):
        #On définit un bouton continue
        qbtn = QtGui.QPushButton('Continue', self)
        #lorsqu'on clique sur continue on quitte l'application
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #la taille du bouton est adaptée
        qbtn.resize(qbtn.sizeHint())
        #la position du bouton est modifiée
        qbtn.move(70, 30)       

        qbtn2 = QtGui.QPushButton('Arreter', self)
        #lorsqu'on clique sur continue on quitte l'application
        qbtn2.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #la taille du bouton est adaptée
        qbtn2.resize(qbtn.sizeHint())
        #la position du bouton est modifiée
        qbtn2.move(70, 100)     
        #on travaille sur la boîte
        #position (700,700), taille (150,50)
        self.setGeometry(700, 700, 550, 550)
        #titre de la boite
        self.setWindowTitle('Boite 2')    
        self.show()
     
        def closeEvent(self, event):
        
            #affichage message en cas de fermeture avec la croix
            reply = QtGui.QMessageBox.question(self, 'Message',
                "Are you sure to quit?", QtGui.QMessageBox.Yes | 
                QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()       


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Boite()
    sys.exit(app.exec_())

main()