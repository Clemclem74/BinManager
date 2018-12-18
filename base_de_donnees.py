import time
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def stockDonneesPleinVide(poubelle, temps):
	#Ajoute (date, poubelle, temps), qui sont la date, le numero de la poubelle et le temps entre la poubelle pleine et la poubelle ramassee
	#Dans la base de donnees pour permettre de faire des graphes (optimisation du dispositif)
	requests.post('https://docs.google.com/forms/d/e/1FAIpQLSei5ygsYkcSmhMgWVwfSCcaVQQ4UNeeNVcOqjRrgUHTWjVm6g/formResponse', data = {'entry.679099635':date, 'entry.1606041453':poubelle, 'entry.2022895418':temps} ,verify=False)

#def stockDonneesVidePlein(mois, poubelle, nombre):
	#Ajoute (mois, poubelle, nombre), qui sont le mois, le numero de la poubelle et le nombre de fois que la poubelle a ete pleine
	#Dans la base de donnees pour permettre de faire des graphes (optimisation du dispositif)
	#requests.post('h',data = {'':mois, '':poubelle, '':nombre},verify=False)

stockDonneesPleinVide('25/11','2','1')
#stockDonneesVidePlein('janvier','2','11')
