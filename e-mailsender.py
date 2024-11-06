import smtplib
from email.message import Message
import hyperlink
import random

name = []

#Hier wird die email adresse ausgewählt
with open('Name.txt') as f:
    name = [line.rstrip() for line in f]

RandomName = random.choice(name)

print(RandomName)


#hier wird die email versendet
email = "teacherfisher.innen@gmail.com"
#receiver_email = input("Receiver E-Mail:")

subject = ("Sicherheitswarnung an " + RandomName)
message = '''Sehr geehrter Nutzer,
wir haben verdaechtige Aktivitaeten in Ihrem Google-Konto festgestellt. Bitte bestaetigen Sie Ihre Identitaet, um den Zugriff auf Ihr Konto zu sichern.

Jetzt verifizieren

Vielen Dank,
Google Support'''

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "czqc rfzf qijm vvnf ")


server.sendmail(email, RandomName, text)

print(message)
print("Email sent to " + RandomName)
