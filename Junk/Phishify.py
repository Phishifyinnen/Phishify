import subprocess
import tkinter as tk
from logging import root
from tkinter import ttk
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PIL.ImageEnhance import Color


def mailrunner():
    script_path = "e-mailsender.py"

    try:
        # Skript ausführen (ersetze den Pfad mit dem deiner Datei)
        subprocess.run(["python3", script_path], check=True)
        print("Skript erfolgreich ausgeführt!")
    except subprocess.CalledProcessError:
        print("Fehler beim Ausführen des Skripts!")


# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = tk.Label(master=window, text='This button sends an E-Mail to a random Person in your List.')
label.pack()

# tk.text

# ttk button
button = tk.Button(master=window, text='Send Mail', command=mailrunner, bg = "#415A77", fg="white")
button.pack()

# run
window.mainloop()
