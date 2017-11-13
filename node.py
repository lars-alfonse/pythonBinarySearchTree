class node:

    type = "node"
    repeat_message = "data already present"

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_child(self, data):
        if data > self.data:
            if not self.right_child:
                self.right_child = node(data)
            else:
                self.right_child.add_child(data)
        elif data < self.data:
            if not self.left_child:
                self.left_child = node(data)
            else:
                self.left_child.add_child(data)
        else:
            print(self.repeat_message)

    def check_value(self, data):
        if self.data == data:
            return True
        elif data > self.data and not self.right_child:
            return self.right_child.check_value(data)
        elif data < self.data and not  self.left_child:
            return self.left_child.check_value(data)
        else:
            return False

    def display(self, level=0):
        if not self.right_child == None:
            self.right_child.display(level+1)
        print("")
        for i in range(level):
            print("    ")
        print(self.data)
        if not self.left_child == None:
            self.left_child.display(level+1)


