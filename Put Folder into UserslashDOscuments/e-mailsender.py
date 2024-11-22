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
</style><link href=3D"//fonts.googlea=pis.com/css?family=3DGoogle+Sans" rel=3D"stylesheet" type=3D"text/css"
              nonce='e=3D"a5JpJkBI2Cl2HVmUu1etdg"/'>
<head> <meta charset="UTF-8"></head>
<body>
<div style="width: 500px; height: 450px; border-radius: 10px; border-width: thin; border-style: solid; display: grid; place-content: center; border-color: #dadce0; margin-inside: 35px">
   <div style="margin: auto; display: flex; align-items: center; height: 30px;width: 80px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/250px-Google_2015_logo.svg.png" alt="https://www.itespresso.de/wp-content/uploads/2015/03/ms-office-logo-800-684x513.jpg" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/250px-Google_2015_logo.svg.png" style="width: 100%; max-width: 100px; display: block; margin: 0 auto;">
   </div>
    <p style="text-align: center; font-family:Roboto-Regular,Helvetica,Arial; font-size: 25px; margin: auto; margin-top: 30px;">Sicherheitswarnung für <br></p>
    <p style="text-align: center; font-family:Roboto-Regular,Helvetica,Arial; font-size: 12px; color: rgba(0,0,0,1); line-height: 1.6;">{random_mail}</p>
    <div style="text-align: center; margin: 15px; font-family:Roboto-Regular,Helvetica,Arial,sans-serif;font-size:14px;color:rgba(0,0,0,0.87);line-height:20px;padding-top:20px; border-width: thin; border-color: #dadce0; border-top-style: solid">
    <p style="font-size: 14px; color: rgba(0,0,0,1); line-height: 1.6; margin: 10px"></p>
    <p style="font-size: 14px; color: rgba(0,0,0,1); line-height: 1.6; margin: 10px">Sehr geehrter Benutzer,</p>
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
