import time
from grovepi import *

# Connect the Grove LED to digital port D4
led = 4

pinMode(led,"OUTPUT")
time.sleep(1)

def allumerLedRouge():
#Allume la Led Rouge
    try:
        digitalWrite(led,1)     # allume la led Rouge
        print ("LED ON!")
        time.sleep(1)
    except KeyboardInterrupt:   # eteint la led Rouge avant d'arreter la fonction
        digitalWrite(led,0)
        break
    except IOError:             # Ecrit "Error" si il y a un probleme
        print ("Error")

def eteindreLedRouge():
#Eteint la led Rouge
    try:
        digitalWrite(led,0)     # eteint la led Rouge
        print ("LED OFF!")
        time.sleep(1)
    except KeyboardInterrupt:   # eteint la led Rouge avant d'arreter la fonction
        digitalWrite(led,0)
        break
    except IOError:             # Ecrit "Error" si il y a un probleme
        print ("Error")