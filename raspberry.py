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
