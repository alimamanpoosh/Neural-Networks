import random

def mutation_layer(parent):
    index = random.randint(0, len(parent)-1)
    parent[index] = random.choice([10, 20, 30])
    return parent

temp = [{'feature extraction': 1, 'hidden layer': [20], 'activation function': [1, 2]}, {'feature extraction': 1, 'hidden layer': [], 'activation function': [2]}, {'feature extraction': 3, 'hidden layer': [10], 'activation function': [2, 1]}, {'feature extraction': 1, 'hidden layer': [30], 'activation function': [2, 2]}, {'feature extraction': 3, 'hidden layer': [20, 20], 'activation function': [2, 2, 2]}, {'feature extraction': 1, 'hidden layer': [20, 30], 'activation function': [1, 1, 1]}]




print(temp[0]['hidden layer'])

child = mutation_layer(temp[0]['hidden layer'])
print(child)
