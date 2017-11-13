class node:

    type = "node"
    repeat_message = "data already present"

    def __init__(self, data, parent = 0):
        self.data = data
        self.parent = parent
        self.left_child = 0
        self.right_child = 0

    def add_child(self, data):
        if data > self.data:
            if self.right_child == 0:
                self.right_child = node(data, self)
            else:
                self.right_child.add_child(data)
        elif data < self.data:
            if self.left_child == 0:
                self.left_child = node(data, self)
            else:
                self.left_child.add_child(data)
        else:
            print(self.repeat_message)