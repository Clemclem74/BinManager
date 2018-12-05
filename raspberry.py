import capteur_ultrason.py
import led_rouge.py
import led_verte.py
import base_de_donnees.py
import balise_GPS.py
import email.py
import ecran_LCD.py


def main():
#A faire tous les x temps :
#Recuperer la distance
#Analyser la distance :
#	Allumer Led Verte ou Rouge (si rouge : stocker la date dans la base de dans la base de donnee)
#	Eteindre l’autre
#Si poubelle pleine : Envoyer mail à l’organisme avec la localisation de la poubelle
#Stocker la date dans la base de données lorsque la poubelle est ramassée (analyseDistance : etat=0)


import time


Compte_Nb_Meme_Etat = 0
Pleins = False

while(1):
	
	if Pleins = False :
		if analyseDistance == 1 :
			Compte_Nb_Meme_Etat = Compte_Nb_Meme_Etat + 1
		else :
			Compte_Nb_Meme_Etat = 0
		
		if Compte_Nb_Meme_Etat > 6 :
			#Dire que c'est pleins (LED, MAIL ET TOUT)
			
			Pleins = True
	
	else :
		if analyseDistance == 0 :
			Compte_Nb_Meme_Etat = Compte_Nb_Meme_Etat + 1
		else :
			Compte_Nb_Meme_Etat = 0
		
		if Compte_Nb_Meme_Etat > 6 :
			#Dire que c'est a nouveau vide (LED,BDD ET TOUT et poubelle vide LCD)
			Pleins = False
	
	time.sleep(10)
	
	
	
	
	