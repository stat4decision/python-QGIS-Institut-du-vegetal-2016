#chargement de la couche actuelle
layer = iface.activeLayer()
#afficha ge de toutes les fonction
dir(layer)
#affichage des features
for f in layer.getFeatures():
  print f
#affichage du nom et du code de chaque aeroport
for f in layer.getFeatures():
  print f['name'], f['iata_code']
  #on veut accéder à la géométrie de chaque point
for f in layer.getFeatures():
  geom = f.geometry()
  print geom.asPoint()
  #si on ne recherche que x
for f in layer.getFeatures():
  geom = f.geometry()
  print geom.asPoint().x()
  #affichage de combinaisons
for f in layer.getFeatures():
    geom = f.geometry()
    print '%s, %s, %f, %f' % (f['name'], f['iata_code'],
         geom.asPoint().y(), geom.asPoint().x())
         

#stockage des sorties dans un fichier
output_file = open('C:\Users\Emmanuel\Desktop/airports.txt', 'w')
for f in layer.getFeatures():
    geom = f.geometry()
    line = '%s, %s, %f, %f\n' % (f['name'], f['iata_code'],
          geom.asPoint().y(), geom.asPoint().x())
    unicode_line = line.encode('utf-8')
    output_file.write(unicode_line)
output_file.close()