# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_ListeDeCouches.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ListeDeCouches(object):
	def setupUi(self, ListeDeCouches):
		ListeDeCouches.setObjectName("ListeDeCouches")
		ListeDeCouches.resize(389, 279)
		self.buttonBox = QtGui.QDialogButtonBox(ListeDeCouches)
		self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.plainTextEdit = QtGui.QPlainTextEdit(ListeDeCouches)
		self.plainTextEdit.setGeometry(QtCore.QRect(10, 30, 361, 201))
		self.plainTextEdit.setObjectName("plainTextEdit")
		self.label = QtGui.QLabel(ListeDeCouches)
		self.label.setGeometry(QtCore.QRect(10, 10, 181, 17))
		self.label.setObjectName("label")
		self.retranslateUi(ListeDeCouches)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ListeDeCouches.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ListeDeCouches.reject)
		QtCore.QMetaObject.connectSlotsByName(ListeDeCouches)

 
	def retranslateUi(self, ListeDeCouches):
		ListeDeCouches.setWindowTitle(QtGui.QApplication.translate("ListeDeCouches", "ListeDeCouches", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("ListeDeCouches", "Les couches actives sont :", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ListeDeCouches = QtGui.QDialog()
    ui = Ui_ListeDeCouches()
    ui.setupUi(ListeDeCouches)
    ListeDeCouches.show()
    sys.exit(app.exec_())