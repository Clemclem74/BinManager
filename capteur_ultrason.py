# GrovePi + Grove Ultrasonic Ranger

from grovepi import *

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

ultrasonic_ranger = 4

def recupererDistance():
#Renvoie la distance entre le couvercle et les déchets
    try:
    	#verifier la distance obtenue
    	print ultrasonicRead(ultrasonic_ranger)
        #retourne la distance
        return ultrasonicRead(ultrasonic_ranger)
    except TypeError :
        return -1
    except IOError :
        return -1

def analyseDistance(distance, etat):
#Analyse une distance et si Distance>ValeurMin

#si etat était à 1: mettre etat à 0 (poubelle ramassée)
#renvoie False (la poubelle n’est pas pleine)
#sinon:renvoie Trueet met l’état à 1 (poubelle pleine)

#Contrainte: si Distance<hauteurPoubelle => on refais la mesure 
#jusqu’à avoir une distance entre 0 et hateurPoubelle(correspond au cas où le couvercle de la poubelle est ouvert).
	return 0