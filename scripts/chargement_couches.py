#chargement des couches lakes et rivers
lakes=QgsVectorLayer("C:\Users\Emmanuel\Desktop\cle_QGIS\donnees\shapefiles/lakes.shp","lakes","ogr")
QgsMapLayerRegistry.instance().addMapLayer(lakes)
#avec iface 
rivers=qgis.utils.iface.addVectorLayer("C:\Users\Emmanuel\Desktop\cle_QGIS\donnees\shapefiles/rivers.shp","rivers","ogr")

#importation d'un raster 
raster1=QgsRasterLayer("C:\Users\Emmanuel\Desktop\cle_QGIS\donnees/raster/landcover.img","Raster1")
QgsMapLayerRegistry.instance().addMapLayer(raster1)


#pour base PostGIS
uri=QgsDataSourceURI()
uri.setConnection("host","port","bnom_bdd","user","pwd")
uri.setDataSource("schema","table",...)

layerPostGIS=QgsVectorLayer(uri.uri(),"LayerPostGIS","postgres")