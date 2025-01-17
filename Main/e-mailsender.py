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

# Dictionary zum Speichern von Tag und Häufigkeit
tag_haeufigkeit = {}

# Datei öffnen und lesen
with open('output.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 2):  # Iteriere durch 2 Zeilen gleichzeitig
        tag = int(lines[i].strip())  # Tag aus der aktuellen Zeile
        haeufigkeit = int(lines[i + 1].strip())  # Häufigkeit aus der nächsten Zeile
        tag_haeufigkeit[tag] = haeufigkeit  # Speichere Tag und Häufigkeit im Dictionary


# Beispielnachrichten im HTML-Format
Google = f'''<html>
</style><link href=3D"//fonts.googlea=pis.com/css?family=3DGoogle+Sans" rel=3D"stylesheet" type=3D"text/css"
              nonce='e=3D"a5JpJkBI2Cl2HVmUu1etdg"/'>
<head> <meta charset="UTF-8"></head>
<body>
<div style="width: 500px; height: 500px; border-radius: 10px; border-width: thin; border-style: solid; display: grid; place-content: center; border-color: #dadce0; margin-inside: 35px">
   <div style="margin: auto; display: flex; align-items: center; height: 30px;width: 80px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/250px-Google_2015_logo.svg.png" alt="https://www.itespresso.de/wp-content/uploads/2015/03/ms-office-logo-800-684x513.jpg" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/250px-Google_2015_logo.svg.png" style="width: 100%; max-width: 100px; display: block; margin: 0 auto;">
   </div>
    <p style="text-align: center; font-family:Roboto-Regular,Helvetica,Arial; font-size: 25px; margin: auto; margin-top: 2px; margin-bottom: 2px;">Sicherheitswarnung für <br></p>
    <p style="text-align: center; font-family:Roboto-Regular,Helvetica,Arial; font-size: 12px; color: rgba(0,0,0,1); line-height: 1.6;">{email}</p>
    <div style="text-align: center; margin: 15px; font-family:Roboto-Regular,Helvetica,Arial,sans-serif;font-size:14px;color:rgba(0,0,0,0.87);line-height:20px;padding-top:20px; border-width: thin; border-color: #dadce0; border-top-style: solid" margin-top: 5px;>
    <p style="font-size: 14px; color: rgba(0,0,0,1); line-height: 1.6;margin-top:5px; margin: 10px">Sehr geehrter Benutzer,</p>
    <p style="font-size: 14px; color: rgba(0,0,0,1); line-height: 1.6; margin: 10px">wir haben verdächtige Aktivitäten in Ihrem Office-Konto festgestellt. Bitte bestätigen Sie Ihre Identität, indem Sie auf den folgenden Link klicken und Ihre Daten eingeben: <a href="http://example.com">Office Support</a></p>
        <button style="background-color: #3981ec; color: white;font-size:14px; height: 35px; width: 135px; border-width: 0px; border-radius: 5px">Aktivität prüfen</button>
    <p style="font-size: 14px; color: rgba(0,0,0,1); line-height: 1.6; margin: 10px">Vielen Dank,<br>Ihr Office Support Team</p>
    </div>
</div>
<div style="text-align: center; width: 500px">
    <p style="font-size: 10px; color: gray; margin: 10px; margin-bottom: 0px">Diese E-Mail wurde automatisch generiert. Sollten Sie Probleme haben, wenden Sie sich bitte <br>an unseren Kundenservice.</p>
    <p style="font-size: 10px; color: gray; margin: 10px; margin-top: 2.5px">Ⓓ 2024 Office United States of America Ltd., Molton House, Hindstons Street, Antonstans 41, USA</p>
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
<p>Hallo {name},</p>
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
mailText = [Google]

# Zeitintervall festlegen (Sekunden oder Minuten)
# Hier: Intervall zwischen den E-Mails in Sekunden (60 = 1 Minute)

time_interval_seconds =  tag/haeufigkeit # Beispiel: 60 Sekunden zwischen den E-Mails

# SMTP-Server-Verbindung herstellen
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("teacherfisher.innen@gmail.com", "czqc rfzf qijm vvnf")

# Schleife über alle Namen und E-Mails
for i in range(0, haeufigkeit):
    # Betreff definieren und Nachricht auswählen
    subject = f"Sicherheitswarnung an {name} {lastname}"
    message = Google

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
    print(f"[{i + 1}/{haeufigkeit}] E-Mail gesendet an {name} {lastname} ({email})")

    # Wartezeit vor der nächsten E-Mail (außer nach der letzten)

    print(f"Wartezeit: {time_interval_seconds} Sekunden")
    time.sleep(time_interval_seconds)


# Server schließen
server.quit()
