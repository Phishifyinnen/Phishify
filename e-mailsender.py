
import smtplib
from email.message import Message
import hyperlink

email = "teacherfisher.innen@gmail.com"
receiver_email = input("Receiver E-Mail:")

subject = ("Sicherheitswarnung an " + receiver_email)
message = '''Sehr geehrter Benutzer,
wir haben verdaechtige Aktivitaeten in Ihrem Office-Konto festgestellt. Bitte bestaetigen Sie Ihre Identitaet, indem Sie auf den folgenden Link klicken und Ihre Daten eingeben: Office Suport
Vielen Dank,
Ihr Office Support Team
'''
text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "czqc rfzf qijm vvnf ")


server.sendmail(email, receiver_email, text)

print("Email sent to " + receiver_email)
