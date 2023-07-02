import random

def mutation_activition(parent):
    index = random.randint(1, len(parent)-1)
    parent[index] = random.randint(1,2)
    return parent

temp = [{'feature extraction': 1, 'hidden layer': [20], 'activation function': [1, 2]}, {'feature extraction': 1, 'hidden layer': [], 'activation function': [2]}, {'feature extraction': 3, 'hidden layer': [10], 'activation function': [2, 1]}, {'feature extraction': 1, 'hidden layer': [30], 'activation function': [2, 2]}, {'feature extraction': 3, 'hidden layer': [20, 20], 'activation function': [2, 2, 2]}, {'feature extraction': 1, 'hidden layer': [20, 30], 'activation function': [1, 1, 1]}]

print(temp[0]['activation function'])

child = mutation_activition(temp[0]['activation function'])
print(child)


# important Point : if we mutation 'activation function': [] and we most attention them