from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder=os.getcwd())  # Setzt den aktuellen Ordner als template_folder

# Die Textdatei, in die die Eingaben gespeichert werden
FILENAME = "namese.txt"

# Startseite, leitet zu /Test-Eingabe-Feld weiter
@app.route('/')
def home():
    return redirect(url_for('index'))  # Leitet auf den Pfad '/Test-Eingabe-Feld' weiter

@app.route('/Test-Eingabe-Feld', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Die Werte aus den Formularfeldern abholen
        email = request.form['E-Mail']
        name = request.form['Name']
        nachname = request.form['Nachname']

        # In die Textdatei speichern, jeweils mit einem Zeilenumbruch nach jedem Wert
        with open(FILENAME, 'a') as file:
            file.write(f"{email}\n")
            file.write(f"{name}\n")
            file.write(f"{nachname}\n")
            file.write("\n")  # Leere Zeile nach jedem Eintrag für bessere Lesbarkeit

        return "Daten wurden gespeichert!"

    # Die HTML-Datei direkt aus dem aktuellen Ordner laden
    return render_template('Test-Eingabe-Feld.html')


if __name__ == '__main__':
    app.run(debug=True)
