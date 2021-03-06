import capteur_ultrason as CU
import led_rouge as LR
import led_verte as LV
import base_de_donnees as BDD
#import balise_GPS as GPS
import mail as EM
import ecran_LCD as LCD
import time
import datetime



def main():
#A faire tous les x temps :
#Recuperer la distance
#Analyser la distance :
#	Allumer Led Verte ou Rouge (si rouge : stocker la date dans la base de dans la base de donnee)
#	Eteindre l autre
#Si poubelle pleine : Envoyer mail a l organisme avec la localisation de la poubelle
#Stocker la date dans la base de donnees lorsque la poubelle est ramassee (analyseDistance : etat=0)

#--------------------------------CONSTANTES A MODIFIER POUR CHAQUE POUBELLE--------------------------------------------------

	Numero_Poubelle = 1
	Compte_Nb_Meme_Etat = 0
	Distance_Max = 700
	
#----------------------------------------------------------------------------------------------------------------------------

	Pleins = False

	LR.eteindreLedRouge()
	LV.allumerLedVerte()
	LCD.poubelle_libre()
	


	while(1):

		try : 
			print(CU.recupererDistance())
			if Pleins == False :
				if CU.analyseDistance(Distance_Max) == 1 :
					Compte_Nb_Meme_Etat = Compte_Nb_Meme_Etat + 1
				else :
					Compte_Nb_Meme_Etat = 0

				if Compte_Nb_Meme_Etat > 6 :
					#Dire que c'est pleins (LED, MAIL ET LCD)
					LR.allumerLedRouge()
					LV.eteindreLedVerte()
					LCD.poubelle_pleine()
					Pleins = True
					Compte_Nb_Meme_Etat = 0
					EM.envoieEmail()
					Date_Remplie = datetime.datetime.now()

			else :
				if CU.analyseDistance(Distance_Max) == 0 :
					Compte_Nb_Meme_Etat = Compte_Nb_Meme_Etat + 1
				else :
					Compte_Nb_Meme_Etat = 0

				if Compte_Nb_Meme_Etat > 6 :
					#Dire que c'est a nouveau vide (LED,BDD et poubelle vide LCD)
					LR.eteindreLedRouge()
					LV.allumerLedVerte()
					LCD.poubelle_libre()
					Pleins = False
					Compte_Nb_Meme_Etat = 0
					Temps_Avant_Vidage = datetime.datetime.now()-Date_Remplie
					Date_Remplie=0
					print(Temps_Avant_Vidage)
					BDD.stockDonneesPleinVide(Numero_Poubelle, Temps_Avant_Vidage)
					
					

			time.sleep(2)

		except KeyboardInterrupt:
			LR.eteindreLedRouge()
			LV.eteindreLedVerte()
			print "CRASH"
			LCD.setRGB(0,0,0)
			LCD.setText("")
			break
	
	


	
	
main()
