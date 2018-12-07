import smtplib
server = smtplib.SMTP_SSL() # On utilise SMTP_SSL() à la place de SMTP()

server.connect('smtp.toto.fr')

server.ehlo() # ATTENTION, avec SSL, c'est la commande EHLO au lieu de HELO
#(250, 'toto\nPIPELINING\nSIZE 10240000\nVRFY\nETRN\nAUTH LOGIN PLAIN\nAUTH=LOGIN PLAIN\nENHANCEDSTATUSCODES\n8BITMIME\nDSN') # Réponse du serveur
server.login('user', 'pass') # On s'authentifie
# (235, '2.7.0 Authentication successful') # Réponse du serveur
fromaddr = 'TOTO <moi@toto.fr>'
toaddrs = ['lui@toto.fr', 'elle@toto.fr'] # On peut mettre autant d'adresses que l'on souhaite
sujet = "Un Mail avec Python"
message = u"""\
Velit morbi ultrices magna integer.
Metus netus nascetur amet cum viverra ve cum.
Curae fusce condimentum interdum felis sit risus.
Proin class condimentum praesent hendrer
it donec odio facilisi sit.
Etiam massa tempus scelerisque curae habitasse vestibulum arcu metus iaculis hac.
"""
msg = """\
From: %s\r\n\
To: %s\r\n\
Subject: %s\r\n\
\r\n\
%s
""" % (fromaddr, ", ".join(toaddrs), sujet, message)
try:
    server.sendmail(fromaddr, toaddrs, msg)
except smtplib.SMTPException as e:
    print(e)
# {} # Réponse du serveur
server.quit()
# (221, '2.0.0 Bye')
