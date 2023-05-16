def crossover_feature(parent1, parent2):
    parent1 , parent2 = parent2 , parent1
    return parent1 , parent2


temp6 = temp6 = [{'feature extraction': 1, 'hidden layer': [20], 'activation function': [1, 2]}, {'feature extraction': 1, 'hidden layer': [], 'activation function': [2]}, {'feature extraction': 3, 'hidden layer': [10], 'activation function': [2, 1]}, {'feature extraction': 1, 'hidden layer': [30], 'activation function': [2, 2]}, {'feature extraction': 3, 'hidden layer': [20, 20], 'activation function': [2, 2, 2]}, {'feature extraction': 1, 'hidden layer': [20, 30], 'activation function': [1, 1, 1]}]

print(crossover_feature(temp[0]['feature extraction'], temp[1]['feature extraction']))
# input ==> (2, 3)
# output ==> (3, 2)