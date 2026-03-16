import json

class pokemon:
    def __init__(self, dados):
        self.name = dados['name']
        self.description = dados['description']
        self.height = dados['height'] #ex: 0.7 m - float
        self.weight = dados['weight'] #ex: 6.7 kg - float
        self.category = dados['category'] #ex: seed - string
        self.skills = dados['skills'] #ex: Overgrow - string
        self.sex = dados['sex'] #M ou H - string
        self.type = dados['type'] #ex: Plant, poison - string - list
        self.weakness = dados['weakness'] #ex: Fire, ice - string - list
        
    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "height": self.height,
            "weight": self.weight,
            "category": self.category,
            "skills": self.skills,
            "sex": self.sex,
            "type": self.type,
            "weakness": self.weakness
        }

    def add_in_pokedex(self):
        #Estudar dicionário e conjuntos para validar os dados de "pokemon"
        if self.name not in pokedex:
            pokedex[self.name] = self.to_json()

        print(f"{self.name} foi adicionado na pokedex")

    def display(self):
        if pokedex[f"{self.name}"]:
            print(f"Nome: {self.name}\nDescricao: {self.description}\nAltura: {self.height} m\nPeso: {self.weight} kg\nCategoria: {self.category}")
        else:
            print("Pokemon não encontrado")


with open("pokedex.json", "r", encoding="utf-8") as check:
    pokedex = json.load(check)

# venusaur = pokemon({"name": "Venusaur", "description": "Enquanto se banha ao sol, consegue converter a luz em energia. Consequentemente, é mais potente no verão.", "height": 2.0, "weight": 100.0, "category": "Seed", "skills": "Overgrow", "sex": ["H", "M"], "type": ["Plant", "Poison"], "weakness": ["Fire", "Ice", "Flying", "Psychic"]})

# venusaur.add_in_pokedex()
# bulbasaur.display()


with open("pokedex.json", "w", encoding="utf-8") as f:
    json.dump(pokedex, f, indent=4, ensure_ascii=False)