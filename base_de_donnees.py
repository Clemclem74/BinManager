def StockDonnees(date, poubelle, temps):

	#Ajoute (date, poubelle, temps), qui sont la date, le numero de la poubelle et le temps entre la poubelle pleine et la poubelle ramassee
	#Dans la base de données pour permettre de faire des graphes (optimisation du dispositif)
	
	requests.post('https://docs.google.com/forms/d/e/1FAIpQLSei5ygsYkcSmhMgWVwfSCcaVQQ4UNeeNVcOqjRrgUHTWjVm6g/viewform',data = {'entry.679099635':date, 'entry.1606041453':poubelle, 'entry.2022895418':temps},verify=False)
