from flask import Flask, render_template, jsonify, request
import json
import navigation
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

@app.route("/navigation")
def navig():
    with open("pokedex.json", "r", encoding="utf-8") as f:
        pokedex = json.load(f)

    nav = navigation.Navigation(pokedex)

    return jsonify(nav.to_list())


@app.route("/data/send", methods=['POST'])
def add_in_pokedex():
    data = request.get_json()

    if not data:
        return jsonify({"erro": "deu merda filho"}), 400
    
    #abrir a pokedex
    with open("pokedex.json", "r", encoding="utf-8") as check:
        pokedex = json.load(check)

    bixo = pokemon.Pokemon(data)

    bixo.add_in_pokedex()

    with open("pokedex.json", "w", encoding="utf-8") as f:
        json.dump(pokedex, f, indent=4, ensure_ascii=False)
    
    # Processa os dados (exemplo)
    
    return jsonify({"mensagem": f"Pokemon {bixo.name} adicionado!"}), 201

# if __name__ == '__main__':
#     app.run()