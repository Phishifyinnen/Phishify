
import smtplib
from email.message import Message
string = "ü"
email = input("Sender E-Mail:")
receiver_email = input("Receiver E-Mail:")

subject = ("Sicherheitswarnung" + receiver_email)
message = input("Message:")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "czqc rfzf qijm vvnf ")


server.sendmail(email, receiver_email, text)

print("Email sent to " + receiver_email)
