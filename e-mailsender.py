import random
import smtplib
from email.mime.multipart import MIMEMultipart
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

# Beispielnachrichten im HTML-Format
Office1 = '''<html>
<head></head>
<body>
<p>Sehr geehrter Benutzer,</p>
<p>wir haben verdächtige Aktivitäten in Ihrem Office-Konto festgestellt. Bitte bestätigen Sie Ihre Identität, indem Sie auf den folgenden Link klicken und Ihre Daten eingeben: <a href="http://example.com">Office Support</a></p>
<p>Vielen Dank,<br>Ihr Office Support Team</p>
<hr style="border: 0; border-top: 0.5px solid gray; width: 100%; margin: 0px auto;">
<p style="font-size: 9px; color: gray;">Diese E-Mail wurde Automatisch generiert, sollten sie probleme haben wenden sie sich an unseren Kunsenservice: https://support.microsoft.com/de-de/contactus#</p>
</body>
</html>
'''

Office2 = f'''<html>
<head></head>
<body>
<p>Hallo {random_name},</p>
<p>um die Sicherheit Ihres Office-Kontos zu gewährleisten, müssen wir Ihre Kontoinformationen aktualisieren. Klicken Sie bitte hier: <a href="http://example.com">Office Anmeldung</a></p>
<p>Mit freundlichen Grüßen,<br>Office Support</p>
<hr style="border: 0; border-top: 0.5px solid gray; width: 100%; margin: 0px auto;">
<p style="font-size: 9px; color: gray;">Diese E-Mail wurde Automatisch generiert, sollten sie probleme haben wenden sie sich an unseren Kunsenservice: https://support.microsoft.com/de-de/contactus#</p>
</body>
</html>
'''

Office3 = '''<html>
<head></head>
<body>
<p>Lieber Kunde,</p>
<p>Ihr Office 365-Abonnement wird in 3 Tagen ablaufen. Bitte verlängern Sie es sofort, um Unterbrechungen zu vermeiden: <a href="http://example.com">Office Login</a></p>
<p>Danke,<br>Office Support</p>
<hr style="border: 0; border-top: 0.5px solid gray; width: 100%; margin: 0px auto;">
<p style="font-size: 9px; color: gray;">Diese E-Mail wurde Automatisch generiert, sollten sie probleme haben wenden sie sich an unseren Kunsenservice: https://support.microsoft.com/de-de/contactus#</p>
</body>
</html>
'''

mailText = [Office3, Office2, Office1]

# Betreff definieren und Nachricht auswählen
subject = f"Sicherheitswarnung an {random_name} {random_lastname}"
message = random.choice(mailText)

# MIMEMultipart-Objekt erstellen
mime_message = MIMEMultipart()
mime_message["From"] = "01jansch@gmail.com"
mime_message["To"] = random_email
mime_message["Subject"] = subject

# HTML-Nachricht als MIMEText-Objekt hinzufügen
html_part = MIMEText(message, "html", "utf-8")
mime_message.attach(html_part)

# SMTP-Server-Verbindung herstellen und Nachricht senden
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login("teacherfisher.innen@gmail.com", "czqc rfzf qijm vvnf")

# Nachricht senden
server.sendmail("teacherfisher.innen@gmail.com", random_email, mime_message.as_string())

print(f"E-Mail gesendet an {random_name} ({random_email})")
print("Nachricht:")
print(message)
