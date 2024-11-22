from xml.dom.minidom import Document

import flask
from flask import Flask, render_template, redirect, url_for, request, jsonify
import os
import subprocess

app = Flask(__name__)


# Route für die Startseite
@app.route('/')
def Start():
    with open("Phishify_Home.html") as file:
        return file.read()
@app.route('/Phishify_Home.html')
def Home():
    with open("Phishify_Home.html") as file:
        return file.read()

@app.route('/Phishify_List.html')
def List():
    with open("Phishify_List.html") as file:
        return file.read()

@app.route('/Phishify_Status.html')
def Status():
    with open("Phishify_Status.html") as file:
        return file.read()

@app.route('/Name.txt')
def Listtxt():
    with open("Name.txt") as file:
        return file.read()



@app.route('/style.css')
def css():
        with open("style.css") as file:
            return flask.Response( file.read(), mimetype="text/css")
@app.route('/save_text', methods=['POST'])
def save_text():
    data = request.get_json()  # Text aus der Anfrage extrahieren
    text = data.get('text')

    # Speicherort der Datei
    file_path = 'Name.txt'

    try:
        # Speichern des Textes in der Datei
        with open(file_path, 'w') as f:
            f.write(text)
        return jsonify({"message": "Text gespeichert!"}), 200
    except Exception as e:
        return jsonify({"message": f"Fehler: {e}"}), 500

    # Speicherort der Datei
    file_path = 'Name.txt'

    try:
        # Speichern des Textes in der Datei
        with open(file_path, 'w') as f:
            f.write(text)
        return jsonify({"message": "Text gespeichert!"}), 200
    except Exception as e:
        return jsonify({"message": f"Fehler: {e}"}), 500

@app.route("/benistdoof")
def run_script():
    try:
        # Hier führst du dein Python-Skript aus, z.B.:
        result = subprocess.run(['python3', 'e-mailsender.py'], capture_output=True, text=True)
        print(result.stdout)  # Ausgabe des Skripts in der Konsole
    except Exception as e:
        print(f"Fehler beim Ausführen des Skripts: {e}")

    return redirect(url_for('Home'))  # Weiterleitung zurück zur Startseite



if __name__ == '__main__':
    app.run(debug=True)
