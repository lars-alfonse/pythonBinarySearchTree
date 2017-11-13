from node import node

class SearchTree:

    type = "tree"

    def __init__(self):
        self.root = 0

    def add_data(self, data):
        if self.root == 0:
            self.root = node(data)
        else:
            self.root.add_child(data)
    def search(self, data):
        