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
# Import de PyQt et qgis 
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
# Initialisation des ressources Qt depuis le fichier resources.py
import resources
# Importation de la boite de dialogue
from ListeDeCouchesDialog import ListeDeCouchesDialog

class ListeDeCouches:

  def __init__(self, iface):
    # Reference a l'interface de qgis
    self.iface = iface

  def initGui(self):  
    # Lancement du plugin 
    self.action = QAction(QIcon(":/plugins/ListeDeCouches/icon.png"), \
        "Liste des couches", self.iface.mainWindow())
    QObject.connect(self.action, SIGNAL("activated()"), self.run) 

    # Ajout du bouton dans la toolbar
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&Liste des couches", self.action)

  def unload(self):
    self.iface.removePluginMenu("&Liste des couches",self.action)
    self.iface.removeToolBarIcon(self.action)

  # fonction qui effectue tout le travail
  def run(self): 
    mapCanvas = self.iface.mapCanvas()
    if mapCanvas.layerCount() == 0:
      QMessageBox.warning(self.iface.mainWindow(), "Plugin de liste des couches" , ("Pas de couche trouvee"), QMessageBox.Ok)
      return 
    layerName = ""
    for i in range(mapCanvas.layerCount()):
      layer = mapCanvas.layer(i)
      layerName += layer.name()+"\n"
    # creation de la boite de dialogue
    dlg=ListeDeCouchesDialog()
    dlg.ui.plainTextEdit.appendPlainText(layerName)
    dlg.show()
    result = dlg.exec_()
    
    if result == 1:
      QMessageBox.warning(self.iface.mainWindow(), "Plugin de liste des couches", ("Voulez allez quitter le plugin !"), QMessageBox.Ok) 