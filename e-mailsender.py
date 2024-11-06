import smtplib
from email.message import Message
import hyperlink
import random

name = []

Office1 = '''Sehr geehrter Benutzer,
wir haben verdächtige Aktivitäten in Ihrem Office-Konto festgestellt. Bitte bestätigen Sie Ihre Identität, indem Sie auf den folgenden Link klicken und Ihre Daten eingeben: Office Suport
Vielen Dank,
Ihr Office Support Team
'''

Office2 = '''Hallo,
um die Sicherheit Ihres Office-Kontos zu gewaehrleisten, muessen wir Ihre Kontoinformationen aktualisieren. Klicken Sie bitte hier: [Link]
Mit freundlichen Grüßen,
Office Support
'''

Office3 = '''Lieber Kunde,
Ihr Office 365-Abonnement wird in 3 Tagen ablaufen. Bitte verlängern Sie es sofort, um Unterbrechungen zu vermeiden: [Link]
Danke,
Office Support
'''

mailText = [Office3, Office2, Office1]


#Hier wird die email adresse ausgewählt
with open('Name.txt') as f:
    name = [line.rstrip() for line in f]

RandomName = random.choice(name)

print(RandomName)


#hier wird die email versendet
email = "teacherfisher.innen@gmail.com"
#receiver_email = input("Receiver E-Mail:")

subject = ("Sicherheitswarnung an " + RandomName)
message = (random.choice(messagteText))

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "czqc rfzf qijm vvnf ")


server.sendmail(email, RandomName, text)

print(message)
print("Email sent to " + RandomName)
