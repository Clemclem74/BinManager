
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText



def envoieEmail():
#Envoie un email a l organisme de ramassage des poubelles avec la localisation$
        msg = MIMEMultipart()
        msg['From'] = 'camille.thomas42140@gmail.com'
        msg['To'] = 'camille.thomas42140@gmail.com'
        msg['Subject'] = 'Poubelle pleine'
        message = 'La Poubelle numero x est pleine. Veuillez la collecter le p$
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('camille.thomas42140@gmail.com', 'cxmdp12021997')
        mailserver.sendmail('camille.thomas42140@gmail.com', 'camille.thomas42$
        mailserver.quit()



envoieEmail()

