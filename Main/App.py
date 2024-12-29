from xml.dom.minidom import Document  # Wird nicht genutzt, kann entfernt werden.
import flask
from flask import Flask, render_template, redirect, url_for, request, jsonify
import os
import subprocess  # Ermöglicht das Ausführen externer Skripte.

# Initialisierung der Flask-App
app = Flask(__name__)

# Beispielzahlen, die in der Anwendung genutzt werden können
number1 = 42
number2 = 17

# Route für die Startseite
@app.route('/')
def Start():
    # Gibt den Inhalt der Datei "Phishify_Signup.html" zurück
    with open("Phishify_Signup.html") as file:
        return file.read()

# Route für die Login-Seite
@app.route('/Phishify_Login.html')
def Login():
    # Gibt den Inhalt der Datei "Phishify_Login.html" zurück
    with open("Phishify_Login.html") as file:
        return file.read()

# Route für die Signup-Seite
@app.route('/Phishify_Signup.html')
def Signup():
    # Gibt den Inhalt der Datei "Phishify_Signup.html" zurück
    with open("Phishify_Signup.html") as file:
        return file.read()

# Route für ein JavaScript-File (Validation)
@app.route('/validation.js')
def Validation():
    # Gibt den Inhalt der Datei "validation.js" zurück
    with open("validation.js") as file:
        return file.read()

# Route für ein JavaScript-File (Darkmode)
@app.route('/darkmode.js')
def Darkmode():
    # Gibt den Inhalt der Datei "darkmode.js" zurück
    with open("darkmode.js") as file:
        return file.read()

# Route für die Home-Seite
@app.route('/Phishify_Home.html')
def Home():
    # Gibt den Inhalt der Datei "Phishify_Home.html" zurück
    with open("Phishify_Home.html") as file:
        return file.read()

# Hauptseite, wird in der main-Funktion gerendert
def main():
    render_template("Phishify_Home.html")

# Route für eine weitere Seite (Liste)
@app.route('/Phishify_List.html')
def List():
    # Gibt den Inhalt der Datei "Phishify_List.html" zurück
    with open("Phishify_List.html") as file:
        return file.read()

# Route für die Status-Seite
@app.route('/Phishify_Status.html')
def Status():
    # Gibt den Inhalt der Datei "Phishify_Status.html" zurück
    with open("Phishify_Status.html") as file:
        return file.read()

# Route für eine Textdatei
@app.route('/Name.txt')
def Listtxt():
    # Gibt den Inhalt der Datei "Name.txt" zurück
    with open("Name.txt") as file:
        return file.read()

# Route für CSS-Dateien (Standardstil)
@app.route('/style.css')
def css():
    # Gibt den Inhalt der Datei "style.css" mit dem MIME-Typ "text/css" zurück
    with open("style.css") as file:
        return flask.Response(file.read(), mimetype="text/css")

# Route für CSS-Dateien (Login-Stil)
@app.route('/StyleLogin.css')
def csslogin():
    # Gibt den Inhalt der Datei "StyleLogin.css" mit dem MIME-Typ "text/css" zurück
    with open("StyleLogin.css") as file:
        return flask.Response(file.read(), mimetype="text/css")

# Route zum Speichern von Text
@app.route('/save_text', methods=['POST'])
def save_text():
    # Daten aus der Anfrage holen
    data = request.get_json()
    text = data.get('text')

    # Zielpfad für die Datei
    file_path = 'Name.txt'

    try:
        # Text in der Datei speichern
        with open(file_path, 'w') as f:
            f.write(text)
        return jsonify({"message": "Text gespeichert!"}), 200
    except Exception as e:
        # Fehlerbehandlung
        return jsonify({"message": f"Fehler: {e}"}), 500

# Route zum Ausführen eines externen Skripts
@app.route("/benistdoof")
def run_script():
    try:
        # Ausführen eines Python-Skripts
        result = subprocess.run(['python3', 'e-mailsender.py'], capture_output=True, text=True)
        print(result.stdout)  # Ausgabe des Skripts in der Konsole
    except Exception as e:
        print(f"Fehler beim Ausführen des Skripts: {e}")

    # Weiterleitung zur Home-Seite
    return redirect(url_for('Home'))

# Route für eine weitere Seite (Kakacke)
@app.route('/kakacke.html')
def Kakacke():
    # Gibt den Inhalt der Datei "Kakacke.html" zurück
    with open("Kakacke.html") as file:
        return file.read()

# Index-Funktion (scheint nicht genutzt zu werden)
def index():
    with open("kakacke.html") as file:
        return render_template('kakacke.html', num1=number1, num2=number2)

# Route für eine weitere CSS-Datei
@app.route('/StyleForSettings.css')
def StyleForSettings():
    # Gibt den Inhalt der Datei "StyleForSettings.css" mit dem MIME-Typ "text/css" zurück
    with open("StyleForSettings.css") as file:
        return flask.Response(file.read(), mimetype="text/css")

# Route zum Speichern von Daten in einer Datei
@app.route('/save', methods=['POST'])
def save_to_file():
    # Zahlen aus dem Formular abrufen
    num1 = request.form['num1']
    num2 = request.form['num2']

    # Daten in eine Datei schreiben
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(f"{num1}\n{num2}")

    # Fehlerhafte Weiterleitung (Phis scheint undefiniert zu sein)
    return redirect(Phis)  # Weiterleitung zurück zur Startseite

# Einstiegspunkt der Flask-Anwendung
if __name__ == '__main__':
    app.run(debug=True)
