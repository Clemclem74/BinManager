import capteur_ultrason as CU
import led_rouge as LR
import led_verte as LV
#import base_de_donnees.py as BDD
#import balise_GPS.py as GPS
#import email.py as EM
import ecran_LCD.py as LCD
import time



def main():
#A faire tous les x temps :
#Recuperer la distance
#Analyser la distance :
#	Allumer Led Verte ou Rouge (si rouge : stocker la date dans la base de dans la base de donnee)
#	Eteindre l autre
#Si poubelle pleine : Envoyer mail a l organisme avec la localisation de la poubelle
#Stocker la date dans la base de donnees lorsque la poubelle est ramassee (analyseDistance : etat=0)


	Compte_Nb_Meme_Etat = 0
	Pleins = False

	LR.eteindreLedRouge()
	LV.allumerLedVerte()
	LCD.poubelle_libre()


	while(1):

		try : 
			print(CU.recupererDistance())
			if Pleins == False :
				if CU.analyseDistance() == 1 :
					Compte_Nb_Meme_Etat = Compte_Nb_Meme_Etat + 1
				else :
					Compte_Nb_Meme_Etat = 0

				if Compte_Nb_Meme_Etat > 6 :
					#Dire que c'est pleins (LED, MAIL ET TOUT)
					LR.allumerLedRouge()
					LV.eteindreLedVerte()
					LCD.poubelle_pleine()
					Pleins = True

			else :
				if CU.analyseDistance == 0 :
					Compte_Nb_Meme_Etat = Compte_Nb_Meme_Etat + 1
				else :
					Compte_Nb_Meme_Etat = 0

				if Compte_Nb_Meme_Etat > 6 :
					#Dire que c'est a nouveau vide (LED,BDD ET TOUT et poubelle vide LCD)
					LR.eteindreLedRouge()
					LV.allumerLedVerte()
					LCD.poubelle_libre()
					Pleins = False

			time.sleep(2)

		except KeyboardInterrupt:
			LR.eteindreLedRouge()
			LV.eteindreLedVerte()
			print "CRASH"
			LCD.setRGB(0,0,0)
			break
	
	


	
	
