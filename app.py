from flask import Flask, render_template, jsonify
import json
import pokemon

app = Flask(__name__)

@app.route("/")
def main():
    pokedex = {}
    with open("pokedex.json", "r", encoding="utf-8") as f:
        pokedex = json.load(f)
    return render_template("index.html", pokemons = pokedex)

@app.route("/data/pokedex")
def send_data():
    pokedex = {}
    with open("pokedex.json", "r", encoding="utf-8") as f:
        pokedex = json.load(f)
    return pokedex

@app.route("/data/<pokemon_name>")
def search_pokemon(pokemon_name):
    with open("pokedex.json", "r", encoding="utf-8") as f:
        pokedex = json.load(f)

    if pokedex[pokemon_name]:
        return pokedex[pokemon_name]
    else:
        return jsonify({"erro": "Pokemon não existe"}), 404

# if __name__ == '__main__':
#     app.run()