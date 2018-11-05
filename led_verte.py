import time
from grovepi import *

# Connect the Grove LED to digital port D4
led = 4

pinMode(led,"OUTPUT")
time.sleep(1)

def allumerLedVerte():
#Allume la Led Verte
    try:
        digitalWrite(led,1)     # allume la led Verte
        print ("LED ON!")
        time.sleep(1)
    except KeyboardInterrupt:   # eteint la led Verte avant d'arreter la fonction
        digitalWrite(led,0)
        break
    except IOError:             # Ecrit "Error" si il y a un probleme
        print ("Error")

def eteindreLedVerte():
#Eteint la led Verte
    try:
        digitalWrite(led,0)     # eteint la led Verte
        print ("LED OFF!")
        time.sleep(1)
    except KeyboardInterrupt:   # eteint la led Verte avant d'arreter la fonction
        digitalWrite(led,0)
        break
    except IOError:             # Ecrit "Error" si il y a un probleme
        print ("Error")