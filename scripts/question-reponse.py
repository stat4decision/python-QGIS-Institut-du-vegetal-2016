
# -*- coding:latin1 -*-
import qgis.core

def reponse(question,nb_essais):
	chaine1=""
	for essai in range(nb_essais):
		chaine1=raw_input(question)
		if chaine1=="O":
			return 1
		elif chaine1=="N":
			return 0
		else:
			print "Vérifiez votre réponse"

print reponse("Voulez-vous continuer ? (O/N)",2)