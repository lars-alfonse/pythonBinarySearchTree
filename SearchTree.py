from node import node

class SearchTree:

    type = "tree"
    def __init__(self):
        self.root = None

    def add_data(self, data):
        if self.root is None:
            self.root = node(data)
        else:
            self.root.add_child(data)
    def search(self, data):
        if self.root is None:
            return False
        else:
            self.root.check_value(data)

    def display(self):
        if not self.root is None:
            self.root.display()
        else:
            print("Nothing to display")
