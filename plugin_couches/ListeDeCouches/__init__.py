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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "liste_de_couches" 
def description():
  return "Affiche la liste des couches"
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "1.0"
def classFactory(iface): 
  # load ListeDeCouches class from file ListeDeCouches
  from ListeDeCouches import ListeDeCouches
  return ListeDeCouches(iface)
