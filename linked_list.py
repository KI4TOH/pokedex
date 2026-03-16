class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def add(self, node):
        if self.head == None:
            self.head = node
            return
        
        atual_node = self.head

        while atual_node.next:
            atual_node = atual_node.next
        
        atual_node.next = node