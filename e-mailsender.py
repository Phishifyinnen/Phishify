import random
import smtplib
from email.mime.text import MIMEText


# Hier wird die E-Mail-Adresse und der Name aus der Datei extrahiert
names_and_emails = []
with open('Name.txt') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        email = lines[i].strip()
        name = lines[i+1].strip()
        lastname = lines[i+2].strip()
        names_and_emails.append((email, name, lastname))

# Zufällige E-Mail und Name auswählen
random_email, random_name, random_lastname = random.choice(names_and_emails)

# Beispielnachrichten
Office1 = '''Sehr geehrter Benutzer,
wir haben verdächtige Aktivitäten in Ihrem Office-Konto festgestellt. Bitte bestätigen Sie Ihre Identität, indem Sie auf den folgenden Link klicken und Ihre Daten eingeben: Office Support
Vielen Dank,
Ihr Office Support Team
'''

Office2 = f'''Hallo {random_name},
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


# Betreff definieren und Nachricht auswählen
subject = f"Sicherheitswarnung an {random_name} {random_lastname}"
message = random.choice(mailText)

# MIMEText-Objekt erstellen, das die Kodierung spezifiziert
mime_message = MIMEText(message, "plain", "utf-8")
mime_message["From"] = "teacherfisher.innen@gmail.com"
mime_message["To"] = random_email
mime_message["Subject"] = subject

# SMTP-Server-Verbindung herstellen und Nachricht senden
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login("teacherfisher.innen@gmail.com", "czqc rfzf qijm vvnf")

# Nachricht senden
server.sendmail("teacherfisher.innen@gmail.com", random_email, mime_message.as_string())

print(f"E-Mail gesendet an {random_name} ({random_email})")
print("Nachricht:")
print(message)
