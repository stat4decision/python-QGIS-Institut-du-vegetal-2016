import sys
from PyQt4 import QtGui, QtCore
#on definit une fonction permettant d'afficher une boite vide
def truc():
	app=QtGui.QApplication(sys.argv)

	w=QtGui.QWidget()
	#taille de la boite
	w.resize(750,550)
	#position de la boite
	w.move(30,30)
	#titre de la boite 
	w.setWindowTitle("Boite 1")
	#bouton de la boite
	qbtn2 = QtGui.QPushButton('Arreter', w)
	qbtn2.clicked.connect(QtCore.QCoreApplication.instance().quit)
	#position auto du bouton 
	qbtn2.resize(qbtn2.sizeHint())
	#position du bouton dans la boite
	qbtn2.move(70, 100)
	#affichage et execution
	w.show()
	sys.exit(app.exec_())

	#fonction pour afficher la boite
truc()