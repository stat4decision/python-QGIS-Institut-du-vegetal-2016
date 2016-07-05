## -*- coding:latin1 -*-
from qgis.core import *
from qgis.gui import *
from os import path
from glob import glob
import qgis

#définition d'une classe'
class Charger:
    def __init__(self,iface):
        self.iface=qgis.utils.iface

    def charger_shp(self, path_shp):
        #obtention de la liste des fichiers .shp du répertoire
        files=glob(path.join(path_shp, "*.shp"))
        for file in files:
            #séparation du chemin pour obtenir le nom du fichier
            (repshp,fileshp)=path.split(file)
            layertemp=QgsVectorLayer(file,fileshp,"ogr")
            QgsMapLayerRegistry.instance().addMapLayer(layertemp)
            

def run_script(iface,chemin):
    chargement=Charger(iface)
    chargement.charger_shp(chemin)