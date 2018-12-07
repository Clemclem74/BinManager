
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText



def envoieEmail():
#Envoie un email a l organisme de ramassage des poubelles avec la localisation$
        msg = MIMEMultipart()
        msg['From'] = 'binmanager.maintenance@gmail.com'
        msg['To'] = 'camille.thomas42140@gmail.com'
        msg['Subject'] = 'Poubelle pleine'
        message = 'La Poubelle numero x est pleine. Veuillez la collecter le plus rapidement possible'
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('binmanager.maintenance@gmail.com', 'binmanagerIG3')
        mailserver.sendmail('binmanager.maintenance@gmail.com', 'camille.thomas42@gmail.com', msg.as_string())
        mailserver.quit()
