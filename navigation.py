import linked_list
import json

class navigation:
    def __init__(self, data):
        self.llist = linked_list.linked_list()

        for nome_pokemon in pokedex:
            dados = pokedex[nome_pokemon]
            self.node = linked_list.node(dados)
            self.llist.add(self.node)

    def add_node(self):
        for item in pokedex:
            node = self.node(item)
            self.llist.add(node)
    
    # def vizu(self):
    #     atual = self.llist.head
    #     if not atual:
    #         print("A lista está vazia.")
    #         return

    #     print("\n--- Navegação na Linked List ---")
    #     while atual:
    #         # Exibimos apenas o nome para não poluir o console
    #         print(f"[{atual.data['name']}]", end=" -> ")
    #         atual = atual.next
    #     print("None")


with open("pokedex.json", "r", encoding="utf-8") as check:
    pokedex = json.load(check)

nav = navigation(pokedex)
# nav.vizu()