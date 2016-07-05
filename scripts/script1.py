#chargement d'une couche et changement de la couleur
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *


def run_script(iface):
	#on definit une instance
    mapreg = QgsMapLayerRegistry.instance()
	#on supprime toutes les couches
    mapreg.removeAllMapLayers()
	#on ajoute une couche 
    wb = QgsVectorLayer('C:\Users\Emmanuel\Desktop/qgis_sample_data/shapefiles/alaska.shp', 'world_borders', 'ogr')
    mapreg.instance().addMapLayer(wb)
    #on va aller dans les parametres de la couche 
	renderer = wb.rendererV2()
    symb = renderer.symbol()
	#on change la couleur des symbole (toute la couche dans ce cas)
    symb.setColor(QColor(Qt.green))
	#on fait la meme chose pour une seconde couche
    wb2 = QgsVectorLayer('C:\Users\Emmanuel\Desktop/qgis_sample_data/shapefiles/rivers.shp', 'rivers', 'ogr')
    mapreg.instance().addMapLayer(wb2)
    renderer = wb2.rendererV2()
    symb = renderer.symbol()
    symb.setColor(QColor(Qt.blue))
    #on met a jour le canvas
    iface.mapCanvas().refresh()