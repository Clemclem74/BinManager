# GrovePi + Grove Ultrasonic Ranger

from grovepi import *

# Connect the Grove Ultrasonic Ranger to digital port D6
# SIG,NC,VCC,GND

ultrasonic_ranger = 5

def recupererDistance():
#Renvoie la distance entre le couvercle et les dechets
    try:
        #verifier la distance obtenue
        #print ultrasonicRead(ultrasonic_ranger)
        #retourne la distance
        return ultrasonicRead(ultrasonic_ranger)
    except TypeError :
        return -1
    except IOError :
        return -1

def analyseDistance():
#Analyse une distance et si Distance>ValeurMin

#si etat etait a 1: mettre etat a 0 (poubelle ramassee)
#renvoie False (la poubelle n est pas pleine)
#sinon:renvoie Trueet met l etat a 1 (poubelle pleine)

#Contrainte: si Distance<hauteurPoubelle => on refais la mesure 
#jusqu a avoir une distance entre 0 et hateurPoubelle(correspond au cas ou le $
        dist=recupererDistance()
        if dist>700:
                return -1
        elif dist<20:
                return 1
        else :
                return 0
