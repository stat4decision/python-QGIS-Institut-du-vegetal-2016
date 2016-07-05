from PyQt4.QtCore import QFileInfo
from qgis.core import QgsProject 

#creation d'une instance QGIS
projet=QgsProject.instance()

#ouverture du projet (changer le chemin)
projet.read(QFileInfo("C:\Users\Emmanuel\Desktop\cle_QGIS\donnees/alaska.qgs"))

#recuperer toutes les couches
layers=qgis.utils.iface.legendInterface().layers()

#afficher tous les noms des couches
for layer in layers:
    print layer.name()

