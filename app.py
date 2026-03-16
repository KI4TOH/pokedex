from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def main():
    pokedex = {}
    with open("pokedex.json", "r", encoding="utf-8") as f:
        pokedex = json.load(f)
    return render_template("index.html", pokemons = pokedex)

# if __name__ == '__main__':
#     app.run()