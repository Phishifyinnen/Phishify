import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Hier wird die E-Mail-Adresse und der Name aus der Datei extrahiert
names_and_emails = []
with open('Name.txt') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        email = lines[i].strip()
        name = lines[i + 1].strip()
        lastname = lines[i + 2].strip()
        names_and_emails.append((email, name, lastname))

# Beispielnachrichten im HTML-Format
Office1 = '''<html>
<head> <meta charset="UTF-8"></head>
<body>
<div style="width: 500px; height: 450px; border-radius: 10px; border-width: thin; border-style: solid; display: grid; place-content: center; border-color: #dadce0; margin-inside: 35px">
    <p style="font-size: 14px; color: rgba(0,0,0,1); line-height: 1.6; margin: 10px">Sehr geehrter Benutzer,</p>
    <p style="font-size: 14px; color: rgba(0,0,0,1); line-height: 1.6; margin: 10px">wir haben verdächtige Aktivitäten in Ihrem Office-Konto festgestellt. Bitte bestätigen Sie Ihre Identität.</p>
    <p>Danke,<br>Office Support</p>
</div>
</body>
</html>
'''

Office2 = f'''<html>
<head></head>
<body>
<div style="width: 100%px; height: 100%; border-radius: 50px; border-width: 1px; border-style: solid; display: grid; place-content: center">
 <img src="https://cdn.worldvectorlogo.com/logos/office-365-1.svg">
    <p style="font-size: 10px; color: gray;"></p>
<p>Hallo {random_name},</p>
<p>um die Sicherheit Ihres Office-Kontos zu gewährleisten, müssen wir Ihre Kontoinformationen aktualisieren. Klicken Sie bitte hier: <a href="http://example.com">Office Anmeldung</a></p>
<p>Mit freundlichen Grüßen,<br>Office Support</p>
<hr style="border: 0; border-top: 0.5px solid gray; width: 100%; margin: 0px auto;">
<p style="font-size: 10px; color: gray;">Diese E-Mail wurde automatisch generiert. Sollten Sie Probleme haben, wenden Sie sich bitte an unseren <a href="https://support.microsoft.com/de-de/contactus#">Kundenservice</a>.</p>
</div>
</body>
</html>
'''

Office3 = '''<html>
<head></head>
<body>
<div style="width: 100%px; height: 100%; border-radius: 50px; border-width: 1px; border-style: solid; display: grid; place-content: center">
 <img src="https://cdn.worldvectorlogo.com/logos/office-365-1.svg">
    <p style="font-size: 10px; color: gray;"></p>
<p>Lieber Kunde,</p>
<p>Ihr Office 365-Abonnement wird in 3 Tagen ablaufen. Bitte verlängern Sie es sofort, um Unterbrechungen zu vermeiden: <a href="http://example.com">Office Login</a></p>
<p>Danke,<br>Office Support</p>
<hr style="border: 0; border-top: 0.5px solid gray; width: 100%; margin: 0px auto;">
<p style="font-size: 10px; color: gray;">Diese E-Mail wurde automatisch generiert. Sollten Sie Probleme haben, wenden Sie sich bitte an unseren <a href="https://support.microsoft.com/de-de/contactus#">Kundenservice</a>.</p>
</div>
</body>
</html>
'''

# Alle Nachrichten in einer Liste
mailText = [Office1]

# Zeitintervall festlegen (Sekunden oder Minuten)
# Hier: Intervall zwischen den E-Mails in Sekunden (60 = 1 Minute)
Tage = 86400
Haeufigkeit_Mail = 86400/60
time_interval_seconds =  Tage/Haeufigkeit_Mail # Beispiel: 60 Sekunden zwischen den E-Mails

# SMTP-Server-Verbindung herstellen
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("teacherfisher.innen@gmail.com", "czqc rfzf qijm vvnf")

# Schleife über alle Namen und E-Mails
for i, (email, name, lastname) in enumerate(names_and_emails):
    # Betreff definieren und Nachricht auswählen
    subject = f"Sicherheitswarnung an {name} {lastname}"
    message = Office1

    # MIMEMultipart-Objekt erstellen
    mime_message = MIMEMultipart()
    mime_message["From"] = "01jansch@gmail.com"
    mime_message["To"] = email
    mime_message["Subject"] = subject

    # HTML-Nachricht als MIMEText-Objekt hinzufügen
    html_part = MIMEText(message, "html", "utf-8")
    mime_message.attach(html_part)

    # Nachricht senden
    server.sendmail("teacherfisher.innen@gmail.com", email, mime_message.as_string())
    print(f"[{i + 1}/{len(names_and_emails)}] E-Mail gesendet an {name} {lastname} ({email})")

    # Wartezeit vor der nächsten E-Mail (außer nach der letzten)
    if i < len(names_and_emails) - 1:
        print(f"Wartezeit: {time_interval_seconds} Sekunden")
        time.sleep(time_interval_seconds)

# Server schließen
server.quit()
