from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Charger les données JSON existantes à partir du fichier
def charger_base_connaissance():
    with open('intents.json', 'r') as json_file:
        return json.load(json_file)

# Enregistrer les données mises à jour dans le fichier JSON
def sauvegarder_base_connaissance(data):
    with open('intents.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Page d'accueil de l'interface d'administration
@app.route('/')
def index():
    return render_template('index.html')

# Page de traitement du formulaire pour ajouter une intention
@app.route('/ajouter_intention', methods=['POST'])
def ajouter_intention():
    data = charger_base_connaissance()

    tag = request.form['tag']
    patterns = request.form['patterns'].split(',')
    responses = request.form['responses'].split(',')


    nouvel_intention = {
        "tag": tag,
        "patterns": patterns,
        "responses": responses,
        "context_set": ""
    }

    data['intents'].append(nouvel_intention)

    sauvegarder_base_connaissance(data)

    return render_template('index.html', message='L\'intention a été ajoutée avec succès.')

if __name__ == '__main__':
    app.run()