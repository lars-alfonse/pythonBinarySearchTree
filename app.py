import random
from SearchTree import SearchTree

tree = SearchTree()

data = []

for i in range(20):
    data.append(round(random.random()*30))

for number in data:
    tree.add_data(number)

print(tree.search(5))
print(tree.search(10))
tree.display()
