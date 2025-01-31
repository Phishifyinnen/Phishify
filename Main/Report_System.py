import imaplib
import email
from email.header import decode_header

email_list = []
with open('List.txt') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        email_o = lines[i].strip()
        name = lines[i + 1].strip()
        lastname = lines[i + 2].strip()
        email_list.append((email_o))

# IMAP-Server und Login-Daten
IMAP_SERVER = "imap.gmail.com"  # Outlook: "imap.outlook.com"
EMAIL_ACCOUNT = "teacherfisher.innen@gmail.com"
EMAIL_PASSWORD = "ypms ppyj rgra shnw "

# Verbindung aufbauen
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
mail.select("inbox")  # Posteingang wählen


# E-Mails von bestimmtem Absender abrufen
for i in range(0, len(email_list)):
    AB_SENDER = email_list[i]
    status, messages = mail.search(None, f'FROM "{AB_SENDER}"')

    mail_ids = messages[0].split()
    print(f"Gefundene E-Mails von {AB_SENDER}: {len(mail_ids)}")

    # E-Mails abrufen und anzeigen
    for mail_id in mail_ids:
        status, msg_data = mail.fetch(mail_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                print(f"\nVon: {msg['From']}\n")
mail.logout()

