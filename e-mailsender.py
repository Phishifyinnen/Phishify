import random
import smtplib
from email.mime.text import MIMEText

name = []

Office1 = '''Sehr geehrter Benutzer,
wir haben verdächtige Aktivitäten in Ihrem Office-Konto festgestellt. Bitte bestätigen Sie Ihre Identität, indem Sie auf den folgenden Link klicken und Ihre Daten eingeben: Office Support
Vielen Dank,
Ihr Office Support Team
'''

Office2 = '''Hallo,
um die Sicherheit Ihres Office-Kontos zu gewährleisten, müssen wir Ihre Kontoinformationen aktualisieren. Klicken Sie bitte hier: [Link]
Mit freundlichen Grüßen,
Office Support
'''

Office3 = '''Lieber Kunde,
Ihr Office 365-Abonnement wird in 3 Tagen ablaufen. Bitte verlängern Sie es sofort, um Unterbrechungen zu vermeiden: [Link]
Danke,
Office Support
'''

mailText = [Office3, Office2, Office1]

# Hier wird die E-Mail-Adresse ausgewählt
with open('Name.txt') as f:
    name = [line.rstrip() for line in f]

RandomName = random.choice(name)

print(RandomName)

# E-Mail-Adresse und Betreff definieren
email = "teacherfisher.innen@gmail.com"
subject = f"Sicherheitswarnung an {RandomName}"
message = random.choice(mailText)

# MIMEText-Objekt erstellen, das die Kodierung spezifiziert
mime_message = MIMEText(message, "plain", "utf-8")
mime_message["From"] = email
mime_message["To"] = RandomName
mime_message["Subject"] = subject

# SMTP-Server-Verbindung herstellen und Nachricht senden
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "czqc rfzf qijm vvnf")

# Nachricht senden (nur `mime_message.as_string()` verwenden)
server.sendmail(email, RandomName, mime_message.as_string())

print(message)
print("Email sent to " + RandomName)
