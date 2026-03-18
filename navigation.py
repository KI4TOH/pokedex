import linked_list
import json

class Navigation:
    def __init__(self, pokedex):
        self.llist = linked_list.linked_list()

        for nome_pokemon in pokedex:
            dados = pokedex[nome_pokemon]
            self.node = linked_list.node(dados)
            self.llist.add(self.node)

    def add_node(self, pokedex):
        for item in pokedex:
            node = self.node(item)
            self.llist.add(node)
    
    def to_list(self):
        """Converte a linked list em uma lista comum para o Flask conseguir ler"""
        resultado = []
        atual = self.llist.head
        while atual:
            resultado.append([atual.data["name"], atual.data['url']])
            atual = atual.next
        return resultado


# with open("pokedex/pokedex.json", "r", encoding="utf-8") as check:
#     pokedex = json.load(check)

# nav = navigation(pokedex)
# nav.vizu()