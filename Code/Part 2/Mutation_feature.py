import random 

def mutation_feature(parent):
    parent = random.randint(1,3)
    return parent

temp = [{'feature extraction': 1, 'hidden layer': [20], 'activation function': [1, 2]}, {'feature extraction': 1, 'hidden layer': [], 'activation function': [2]}, {'feature extraction': 3, 'hidden layer': [10], 'activation function': [2, 1]}, {'feature extraction': 1, 'hidden layer': [30], 'activation function': [2, 2]}, {'feature extraction': 3, 'hidden layer': [20, 20], 'activation function': [2, 2, 2]}, {'feature extraction': 1, 'hidden layer': [20, 30], 'activation function': [1, 1, 1]}]




print(temp[0]['feature extraction'])

child = mutation_feature(temp[0]['feature extraction'])
print(child)
