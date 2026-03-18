import json
import requests

class Pokemon:
    def __init__(self, dados):
        self.name = dados['name']
        # self.description = dados['description']
        self.height = dados['height'] #ex: 0.7 m - float
        self.weight = dados['weight'] #ex: 6.7 kg - float
        # self.category = dados['category'] #ex: seed - string
        # self.skills = dados['skills'] #ex: Overgrow - string
        # self.sex = dados['sex'] #M ou H - string
        self.type = dados['type'] #ex: Plant, poison - string - list
        self.url = dados['url']
        # self.weakness = dados['weakness'] #ex: Fire, ice - string - list
        
    def to_json(self):
        return {
            "name": self.name,
            # "description": self.description,
            "height": self.height,
            "weight": self.weight,
            # "category": self.category,
            # "skills": self.skills,
            # "sex": self.sex,
            "type": self.type,
            "url": self.url
            # "weakness": self.weakness
        }

    def add_in_pokedex(self, pokedex_name):
        #Estudar dicionário e conjuntos para validar os dados de "pokemon"
        if self.name not in pokedex_name:
            pokedex_name[self.name] = self.to_json()

        # print(f"{self.name} foi adicionado na pokedex")

    def display(self):
        if pokedex[f"{self.name}"]:
            print(f"Nome: {self.name}\n\nAltura: {self.height} m\nPeso: {self.weight} kg")
        else:
            print("Pokemon não encontrado")

pokedex = {}

with open("pokedex.json", "r", encoding="utf-8") as check:
    pokedex = json.load(check)

# i = 1

# while i < 100:
#     url = f"https://pokeapi.co/api/v2/pokemon/{i}"
#     response = requests.get(url)
#     response = response.json()

#     pokemon = Pokemon({"name": response['name'], "height": response['height'], "weight":response['weight'], "type": response['types'][0]['type']['name'], "url": response['sprites']['front_default'] })

#     pokemon.add_in_pokedex(pokedex)

#     i += 1


# print(pokemon)



# venusaur.add_in_pokedex()


with open("pokedex.json", "w", encoding="utf-8") as f:
    json.dump(pokedex, f, indent=4, ensure_ascii=False)