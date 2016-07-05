"""
/***************************************************************************
Name			 	 : liste_de_couches
Description          : Affiche la liste des couches
Date                 : 04/Jul/16 
copyright            : (C) 2016 by E Jakobowicz
email                : ej@stat4decision.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4 import QtCore, QtGui 
from Ui_ListeDeCouches import Ui_ListeDeCouches
# creation de la boite ListeDeCouches
class ListeDeCouchesDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    self.ui = Ui_ListeDeCouches ()
    self.ui.setupUi(self)